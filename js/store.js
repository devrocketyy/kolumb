// IndexLab — zapis postępów w localStorage, z osobnymi profilami (każdy uczeń ma swoje postępy).
const LEGACY_KEY = 'kolumb.v1';           // zapis sprzed profili — przenoszony do pierwszego profilu
const PROFILES_KEY = 'kolumb.profile';    // { active, session, list: [{ id, name, color, created, cloud? }] }
const DAY = 86400000;
const dataKey = (id) => `kolumb.v1.${id}`;

const defaults = () => ({
  version: 1,
  cards: {},      // "przedmiot/dzial/idFiszki" -> { box, due, reps, lapses, first, last }
  days: {},       // "RRRR-MM-DD" -> liczba aktywności (ocen fiszek, odpowiedzi w testach)
  tests: [],      // { sid, scope, name, score, total, at }
  zadania: {},    // "przedmiot/arkusz/nrZadania" -> { pkt, max, at } (samoocena zadań maturalnych)
  egzaminy: {},   // próbne matury: id -> { sid, nazwa, seed, cke, start, koniec, odp:{}, pkt:{}, ... }
  xp: 0,          // wszystkie zdobyte punkty doświadczenia
  daily: {},      // "RRRR-MM-DD" -> { xp, lekcje, fiszki, poprawne, zadania, idealne }
  lekcje: {},     // "przedmiot/zakres/id" -> { n, best, idealne }
  odznaki: {},    // id odznaki -> czas zdobycia
  bledy: {},      // "przedmiot/poddział/id" -> { t: 'f'|'q', uid, id, n, at } — pomyłki do poprawy
  updatedAt: 0,   // czas ostatniej zmiany (do synchronizacji z chmurą)
  settings: { theme: 'auto', installDismissed: false, newPerDay: 20, dailyGoal: 20, sound: true, przedmiot: null },
});

const COLORS = ['#1b7ae6', '#e06a10', '#1f9d5c', '#7c4ddb', '#e04848', '#0f9488', '#c58a00'];
const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);

function readJSON(key) {
  try { const raw = localStorage.getItem(key); return raw ? JSON.parse(raw) : null; } catch { return null; }
}
function writeJSON(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; }
}
function normalize(s) {
  const d = defaults();
  return { ...d, ...(s || {}), settings: { ...d.settings, ...((s && s.settings) || {}) } };
}

// ---------- profile ----------
let profiles = readJSON(PROFILES_KEY);
if (!profiles || !Array.isArray(profiles.list) || !profiles.list.length) {
  const id = uid();
  profiles = { active: id, session: null, list: [{ id, name: 'Mój profil', color: COLORS[0], created: Date.now(), placeholder: true }] };
  const legacy = readJSON(LEGACY_KEY);
  if (legacy) {
    // dotychczasowy użytkownik: przedmiot z jego postępów, żeby nie pokazywać ekranu wyboru
    const first = Object.keys(legacy.cards || {})[0];
    legacy.settings = { ...(legacy.settings || {}), przedmiot: legacy.settings?.przedmiot || (first ? first.split('/')[0] : null) };
    writeJSON(dataKey(id), legacy);
    delete profiles.list[0].placeholder;
    profiles.session = id; // dotychczasowy użytkownik zostaje zalogowany
  }
  writeJSON(PROFILES_KEY, profiles);
}
if (!('session' in profiles)) { profiles.session = profiles.active; writeJSON(PROFILES_KEY, profiles); }
if (!profiles.list.some((p) => p.id === profiles.active)) profiles.active = profiles.list[0].id;

let state = normalize(readJSON(dataKey(profiles.active)));
const saveHooks = [];

export const profileList = () => profiles.list.filter((p) => !p.placeholder);
export const loggedIn = () => !!profiles.session && profiles.session === profiles.active;
export function login(id) {
  switchProfile(id);
  profiles.session = id;
  saveProfiles();
}
export function logout() {
  save({ touch: false });
  profiles.session = null;
  saveProfiles();
}
export const activeProfile = () => profiles.list.find((p) => p.id === profiles.active);
export function saveProfiles() { writeJSON(PROFILES_KEY, profiles); }

export function createProfile(name) {
  const ph = profiles.list.find((x) => x.placeholder);
  if (ph) { // pierwszy profil zajmuje miejsce pustego profilu startowego
    delete ph.placeholder;
    ph.name = String(name || '').trim().slice(0, 30) || 'Nowy profil';
    saveProfiles();
    return ph;
  }
  const p = { id: uid(), name: String(name || '').trim().slice(0, 30) || 'Nowy profil', color: COLORS[profiles.list.length % COLORS.length], created: Date.now() };
  profiles.list.push(p);
  saveProfiles();
  return p;
}
export function switchProfile(id) {
  if (!profiles.list.some((p) => p.id === id)) return;
  save({ touch: false });
  profiles.active = id;
  saveProfiles();
  state = normalize(readJSON(dataKey(id)));
}
export function renameProfile(id, name) {
  const p = profiles.list.find((x) => x.id === id);
  if (p) { p.name = String(name || '').trim().slice(0, 30) || p.name; saveProfiles(); }
}
export function deleteProfile(id) {
  if (profiles.list.length < 2) {
    const only = profiles.list[0];
    if (only.id !== id) return false;
    try { localStorage.removeItem(dataKey(id)); } catch { /* brak dostępu */ }
    only.placeholder = true; only.name = 'Mój profil'; delete only.cloud;
    state = normalize(null);
    saveProfiles();
    return true;
  }
  profiles.list = profiles.list.filter((p) => p.id !== id);
  try { localStorage.removeItem(dataKey(id)); } catch { /* brak dostępu */ }
  if (profiles.active === id) {
    profiles.active = profiles.list[0].id;
    state = normalize(readJSON(dataKey(profiles.active)));
  }
  saveProfiles();
  return true;
}
// Dane konta w chmurze przypięte do aktywnego profilu (e-mail, tokeny sesji).
export function setCloud(info) {
  const p = activeProfile();
  if (info) p.cloud = info; else delete p.cloud;
  saveProfiles();
}

// ---------- zapis ----------
export function save({ touch = true } = {}) {
  if (touch) state.updatedAt = Date.now();
  writeJSON(dataKey(profiles.active), state); // w trybie prywatnym zapis może się nie udać — aplikacja działa dalej
  if (touch) saveHooks.forEach((fn) => fn());
}
export const onSave = (fn) => saveHooks.push(fn);
export const get = () => state;

export function replace(newState, { touch = true } = {}) {
  state = normalize(newState);
  save({ touch });
}

export function reset() {
  const { theme, przedmiot } = state.settings;
  state = defaults();
  state.settings.theme = theme;
  state.settings.przedmiot = przedmiot;
  save();
}

// ---------- daty (czas lokalny) ----------
export function dayKey(t = Date.now()) {
  const d = new Date(t);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}
export function startOfDay(t = Date.now()) {
  const d = new Date(t);
  d.setHours(0, 0, 0, 0);
  return d.getTime();
}
export function addDays(t, n) {
  const d = new Date(t);
  d.setDate(d.getDate() + n);
  return d.getTime();
}
export const endOfToday = () => addDays(startOfDay(), 1) - 1;

export function markActivity(n = 1) {
  const k = dayKey();
  state.days[k] = (state.days[k] || 0) + n;
}

export function streak() {
  const days = state.days;
  let current = 0;
  let t = startOfDay();
  if (!days[dayKey(t)]) t = addDays(t, -1); // seria trwa, dopóki dziś jeszcze można się uczyć
  while (days[dayKey(t)]) {
    current++;
    t = addDays(t, -1);
  }
  const keys = Object.keys(days).filter((k) => days[k]).sort();
  let longest = 0;
  let run = 0;
  let prev = null;
  for (const k of keys) {
    const t2 = new Date(k + 'T12:00:00').getTime();
    run = prev !== null && Math.round((t2 - prev) / DAY) === 1 ? run + 1 : 1;
    longest = Math.max(longest, run);
    prev = t2;
  }
  return { current, longest, today: !!days[dayKey()] };
}

export function addTest(result) {
  state.tests.push(result);
  if (state.tests.length > 100) state.tests = state.tests.slice(-100);
}
