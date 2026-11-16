// IndexLab — płatny dostęp: stan subskrypcji, zakup (Stripe Checkout), panel klienta i kody dostępu.
// Działa tylko, gdy w js/config.js PREMIUM.wlaczone = true i skonfigurowano Supabase (CLOUD).
import * as cloud from './cloud.js';
import { PREMIUM } from './config.js';

export const wlaczone = () => !!PREMIUM.wlaczone && cloud.enabled();
export const plany = () => PREMIUM.plany || [];
export const sklepKodow = () => PREMIUM.sklepKodow || '';

let stan = null; // { plan, zrodlo, status, wazne_do } albo null

export async function odswiez() {
  stan = null;
  const c = cloud.account();
  const token = await cloud.tokenOrNull();
  if (!token) return null;
  const rows = await cloud.api(`/rest/v1/dostep?select=plan,zrodlo,status,wazne_do&user_id=eq.${c.uid}`, { token });
  stan = rows?.[0] || null;
  return stan;
}

export const biezacy = () => stan;
export const aktywny = () => !!(stan?.wazne_do && new Date(stan.wazne_do) > new Date());

async function funkcja(nazwa, body) {
  const token = await cloud.tokenOrNull();
  if (!token) throw new Error('Najpierw zaloguj się e-mailem — dostęp przypisujemy do konta.');
  const d = await cloud.api(`/functions/v1/${nazwa}`, { method: 'POST', token, body: body || {} });
  if (d?.error) throw new Error(d.error);
  return d;
}

export async function kup(plan) {
  const { url } = await funkcja('checkout', { plan });
  location.href = url;
}

export async function panelKlienta() {
  const { url } = await funkcja('portal');
  location.href = url;
}

export async function wykorzystajKod(kod) {
  const token = await cloud.tokenOrNull();
  if (!token) throw new Error('Najpierw zaloguj się e-mailem — kod przypiszemy do konta.');
  await cloud.api('/rest/v1/rpc/wykorzystaj_kod', { method: 'POST', token, body: { kod } });
  return odswiez();
}

// Wszystkie treści dostępne dla tego konta (RLS w bazie: demo albo aktywny dostęp) — jedno zapytanie.
// Ostatnia pobrana wersja trafia do pamięci podręcznej przeglądarki, żeby kurs działał bez internetu.
const CACHE = 'ixl-tresci'; // inna nazwa niż pamięć sw.js (tę czyści każda aktualizacja)
export async function pobierzTresci() {
  const token = await cloud.tokenOrNull();
  const key = new Request(`${location.origin}/__tresci/${cloud.account()?.uid || 'demo'}.json`);
  try {
    const rows = await cloud.api('/rest/v1/tresci?select=plik,dane', { token });
    const map = new Map(rows.map((r) => [r.plik, r.dane]));
    try { const c = await caches.open(CACHE); await c.put(key, new Response(JSON.stringify(rows))); } catch { /* brak Cache API */ }
    return map;
  } catch (e) {
    try {
      const hit = await (await caches.open(CACHE)).match(key);
      if (hit) return new Map((await hit.json()).map((r) => [r.plik, r.dane]));
    } catch { /* brak kopii */ }
    throw e;
  }
}

// Program poleceń
export async function mojePolecenia() {
  const token = await cloud.tokenOrNull();
  if (!token) return null;
  return cloud.api('/rest/v1/rpc/moj_kod_polecajacy', { method: 'POST', token, body: {} });
}
export async function dodajPolecenie(kod) {
  const token = await cloud.tokenOrNull();
  if (!token) throw new Error('Najpierw zaloguj się.');
  await cloud.api('/rest/v1/rpc/uzyj_polecenia', { method: 'POST', token, body: { kod } });
}
// Kod z linku polecającego (?ref=KOD) czeka w przeglądarce, aż uczeń założy konto.
const REF = 'ixl-ref';
export function zapamietajRef() {
  const m = location.search.match(/[?&]ref=([A-Za-z0-9]{4,12})/);
  if (m) { try { localStorage.setItem(REF, m[1].toUpperCase()); } catch { /* brak pamięci */ } history.replaceState(null, '', location.pathname + location.hash); }
}
export const czekajacyRef = () => { try { return localStorage.getItem(REF) || ''; } catch { return ''; } };
export async function wykorzystajRef(kod = czekajacyRef()) {
  if (!kod || !cloud.account()) return null;
  try { await dodajPolecenie(kod); localStorage.removeItem(REF); return 'ok'; }
  catch (e) { if (!/połączenia|fetch/i.test(e.message)) try { localStorage.removeItem(REF); } catch { /* */ } return e.message; }
}
