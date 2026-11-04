// Kolumb — zapis postępów w localStorage.
const KEY = 'kolumb.v1';
const DAY = 86400000;

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
  settings: { theme: 'auto', installDismissed: false, newPerDay: 20, dailyGoal: 20, sound: true },
});

let state = load();

function load() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return defaults();
    const s = JSON.parse(raw);
    const d = defaults();
    return { ...d, ...s, settings: { ...d.settings, ...(s.settings || {}) } };
  } catch {
    return defaults();
  }
}

export function save() {
  try {
    localStorage.setItem(KEY, JSON.stringify(state));
  } catch {
    /* tryb prywatny lub brak miejsca — aplikacja działa dalej bez zapisu */
  }
}

export const get = () => state;

export function replace(newState) {
  const d = defaults();
  state = { ...d, ...newState, settings: { ...d.settings, ...(newState.settings || {}) } };
  save();
}

export function reset() {
  const theme = state.settings.theme;
  state = defaults();
  state.settings.theme = theme;
  save();
}

// ---- daty (czas lokalny) ----
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
