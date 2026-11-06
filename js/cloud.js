// IndexLab — konto w chmurze (Supabase: logowanie e-mailem i zapis postępów).
// Aplikacja działa bez tego modułu; gdy w js/config.js nie ma adresu projektu, konta są wyłączone.
import * as store from './store.js';
import { CLOUD } from './config.js';

export const enabled = () => !!(CLOUD.url && CLOUD.anonKey);
const base = () => CLOUD.url.replace(/\/+$/, '');
const TABLE = CLOUD.table || 'postepy';

async function api(path, { method = 'GET', body, token, headers = {} } = {}) {
  const res = await fetch(base() + path, {
    method,
    headers: {
      apikey: CLOUD.anonKey,
      Authorization: `Bearer ${token || CLOUD.anonKey}`,
      'Content-Type': 'application/json',
      ...headers,
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let data = null;
  try { data = text ? JSON.parse(text) : null; } catch { data = text; }
  if (!res.ok) {
    const msg = (data && (data.msg || data.error_description || data.message || data.error)) || `Błąd ${res.status}`;
    const err = new Error(translate(String(msg)));
    err.status = res.status;
    throw err;
  }
  return data;
}

function translate(m) {
  if (/invalid login credentials/i.test(m)) return 'Nieprawidłowy e-mail lub hasło.';
  if (/already registered|already exists/i.test(m)) return 'Konto z tym adresem już istnieje — zaloguj się.';
  if (/email not confirmed/i.test(m)) return 'Potwierdź adres e-mail (link w wiadomości), a potem zaloguj się.';
  if (/password should be at least/i.test(m)) return 'Hasło musi mieć co najmniej 6 znaków.';
  if (/rate limit/i.test(m)) return 'Za dużo prób — spróbuj za kilka minut.';
  if (/failed to fetch|network/i.test(m)) return 'Brak połączenia z serwerem.';
  return m;
}

function sessionFrom(d) {
  return { email: d.user?.email, uid: d.user?.id, access: d.access_token, refresh: d.refresh_token, exp: Date.now() + (d.expires_in || 3600) * 1000, synced: 0 };
}

export const account = () => store.activeProfile()?.cloud || null;

async function token() {
  const c = account();
  if (!c) throw new Error('Nie zalogowano.');
  if (Date.now() < c.exp - 60000) return c.access;
  const d = await api('/auth/v1/token?grant_type=refresh_token', { method: 'POST', body: { refresh_token: c.refresh } });
  store.setCloud({ ...c, ...sessionFrom(d), synced: c.synced });
  return d.access_token;
}

export async function signUp(email, password) {
  const d = await api('/auth/v1/signup', { method: 'POST', body: { email, password } });
  if (!d.access_token) return { confirm: true }; // projekt wymaga potwierdzenia adresu e-mail
  store.setCloud(sessionFrom(d));
  await push();
  return { confirm: false };
}

// Logowanie: jeśli w chmurze są nowsze postępy — wczytujemy je, w przeciwnym razie wysyłamy lokalne.
export async function signIn(email, password) {
  const d = await api('/auth/v1/token?grant_type=password', { method: 'POST', body: { email, password } });
  store.setCloud(sessionFrom(d));
  return sync();
}

export async function signOut() {
  try { await api('/auth/v1/logout', { method: 'POST', token: await token() }); } catch { /* sesja i tak zostanie usunięta */ }
  store.setCloud(null);
}

async function pull() {
  const c = account();
  const rows = await api(`/rest/v1/${TABLE}?select=data,updated_at&user_id=eq.${c.uid}`, { token: await token() });
  return rows && rows[0] ? rows[0] : null;
}

export async function push() {
  const c = account();
  if (!c) return;
  const st = store.get();
  await api(`/rest/v1/${TABLE}`, {
    method: 'POST',
    token: await token(),
    headers: { Prefer: 'resolution=merge-duplicates,return=minimal' },
    body: { user_id: c.uid, data: st, updated_at: new Date(st.updatedAt || Date.now()).toISOString() },
  });
  store.setCloud({ ...account(), synced: Date.now() });
}

// Scalanie postępów z dwóch urządzeń — nic nie ginie: z każdej pary bierzemy „więcej” lub „nowsze”.
export function merge(a, b) {
  const out = JSON.parse(JSON.stringify(a));
  const pickBy = (x, y, f) => (!x ? y : !y ? x : f(y) > f(x) ? y : x);
  out.cards = { ...a.cards };
  for (const [k, c] of Object.entries(b.cards || {})) out.cards[k] = pickBy(out.cards[k], c, (v) => v.last || 0);
  out.days = { ...a.days };
  for (const [k, n] of Object.entries(b.days || {})) out.days[k] = Math.max(out.days[k] || 0, n);
  const seen = new Set((a.tests || []).map((t) => `${t.at}|${t.scope}`));
  out.tests = [...(a.tests || []), ...(b.tests || []).filter((t) => !seen.has(`${t.at}|${t.scope}`))].sort((x, y) => x.at - y.at).slice(-100);
  out.zadania = { ...a.zadania };
  for (const [k, z] of Object.entries(b.zadania || {})) out.zadania[k] = pickBy(out.zadania[k], z, (v) => v.at || 0);
  out.egzaminy = { ...a.egzaminy };
  for (const [k, e] of Object.entries(b.egzaminy || {})) out.egzaminy[k] = pickBy(out.egzaminy[k], e, (v) => (v.koniec ? 2e13 : 0) + Object.keys(v.odp || {}).length);
  out.xp = Math.max(a.xp || 0, b.xp || 0);
  out.daily = { ...a.daily };
  for (const [k, d] of Object.entries(b.daily || {})) {
    const m = { ...(out.daily[k] || {}) };
    for (const [f, v] of Object.entries(d)) m[f] = Math.max(m[f] || 0, v);
    out.daily[k] = m;
  }
  out.lekcje = { ...a.lekcje };
  for (const [k, l] of Object.entries(b.lekcje || {})) out.lekcje[k] = pickBy(out.lekcje[k], l, (v) => v.n || 0);
  out.odznaki = { ...(b.odznaki || {}), ...(a.odznaki || {}) };
  out.bledy = { ...(b.bledy || {}), ...(a.bledy || {}) };
  out.settings = { ...(b.settings || {}), ...(a.settings || {}) };
  if (!a.settings?.przedmiot && b.settings?.przedmiot) out.settings.przedmiot = b.settings.przedmiot;
  out.updatedAt = Math.max(a.updatedAt || 0, b.updatedAt || 0);
  return out;
}

export async function sync() {
  const remote = await pull();
  const local = store.get();
  if (remote && remote.data) {
    const merged = merge(local, remote.data);
    store.replace(merged, { touch: false });
    await push();
    return 'merged';
  }
  await push();
  return 'pushed';
}

// Automatyczne wysyłanie po zmianach (z opóźnieniem, żeby nie wysyłać przy każdej fiszce).
let timer = null;
export function startAutoSync(onError) {
  store.onSave(() => {
    if (!enabled() || !account()) return;
    clearTimeout(timer);
    timer = setTimeout(() => push().catch((e) => onError?.(e)), 8000);
  });
  window.addEventListener('online', () => { if (enabled() && account()) push().catch(() => {}); });
}
