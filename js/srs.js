// IndexLab — powtórki rozłożone w czasie (system Leitnera z 6 pudełkami).
//
//  Pudełko:           1    2    3    4    5    6
//  Następna powtórka: 1d   2d   4d   8d   16d  32d
//
//  „Nie wiem” → pudełko 1, fiszka wraca jeszcze w tej samej sesji.
//  „Trudne”   → fiszka nie awansuje (z pudełka 3+ spada o jedno), wraca jutro.
//  „Umiem”    → awans o jedno pudełko, przerwa coraz dłuższa.
//  Fiszka jest „opanowana” od pudełka 4 (przerwa ≥ 8 dni).
//  Nowe fiszki: dzienny limit na przedmiot (Ustawienia → „Nowe fiszki dziennie”).

import { get, startOfDay, addDays, endOfToday, dayKey } from './store.js';

export const INTERVALS = [0, 1, 2, 4, 8, 16, 32];
export const MAX_BOX = 6;
export const MASTERED_BOX = 4;
export const DEFAULT_NEW_PER_DAY = 20;
const MINUTE = 60000;

export const cardKey = (sid, uid, cid) => `${sid}/${uid}/${cid}`;

export function nextState(prev, rating, now = Date.now()) {
  const c = { box: 0, reps: 0, lapses: 0, ...(prev || {}) };
  c.reps += 1;
  c.last = now;
  if (!c.first) c.first = now;
  if (rating === 'nie') {
    c.box = 1;
    c.lapses += 1;
    c.due = now + MINUTE;
  } else if (rating === 'trudne') {
    c.box = c.box >= 3 ? c.box - 1 : Math.max(1, c.box);
    c.due = addDays(startOfDay(now), 1);
  } else {
    c.box = Math.min(MAX_BOX, c.box + 1);
    c.due = addDays(startOfDay(now), INTERVALS[c.box]);
  }
  return c;
}

export function intervalLabel(prev, rating) {
  if (rating === 'nie') return 'za chwilę';
  const c = nextState(prev, rating);
  const days = Math.round((c.due - startOfDay()) / 86400000);
  return days === 1 ? 'jutro' : `za ${days} dni`;
}

// Tempo nauki: „auto” (domyślnie) — liczba nowych fiszek wyliczana z planu do matury dla każdego przedmiotu;
// albo stała liczba wybrana w ustawieniach.
const autoRates = {};
export const setAutoRate = (sid, n) => { autoRates[sid] = n; };
export const tempoAuto = () => (get().settings.tempo || 'auto') === 'auto';
export const newPerDay = (sid) => (tempoAuto() && sid && autoRates[sid]) || Number(get().settings.newPerDay) || DEFAULT_NEW_PER_DAY;

// Ile nowych fiszek z danego przedmiotu można jeszcze dziś zacząć.
export function newAllowance(sid) {
  const today = dayKey();
  const prefix = sid + '/';
  let started = 0;
  for (const [k, c] of Object.entries(get().cards)) {
    if (k.startsWith(prefix) && c.first && dayKey(c.first) === today) started++;
  }
  return Math.max(0, newPerDay(sid) - started);
}

// Podsumowanie zbioru poddziałów (jednego poddziału, działu albo całego przedmiotu).
export function summary(sid, units, allowance = newAllowance(sid)) {
  const cards = get().cards;
  const end = endOfToday();
  let total = 0, due = 0, fresh = 0, mastered = 0, points = 0;
  for (const u of units) {
    for (const f of u.fiszki) {
      total++;
      const c = cards[cardKey(sid, u.id, f.id)];
      if (!c || !c.reps) { fresh++; continue; }
      if (c.due <= end) due++;
      if (c.box >= MASTERED_BOX) mastered++;
      points += Math.min(c.box, MASTERED_BOX);
    }
  }
  const newToday = Math.min(fresh, allowance);
  return {
    total,
    due,
    fresh,
    newToday,
    todo: due + newToday,
    mastered,
    seen: total - fresh,
    progress: total ? points / (total * MASTERED_BOX) : 0,
  };
}

// Kolejka sesji: najpierw zaległe powtórki, potem nowe fiszki (w kolejności poddziałów).
export function buildQueue(sid, units) {
  const cards = get().cards;
  const end = endOfToday();
  const due = [];
  const fresh = [];
  for (const u of units) {
    for (const f of u.fiszki) {
      const c = cards[cardKey(sid, u.id, f.id)];
      if (!c || !c.reps) fresh.push({ f, u });
      else if (c.due <= end) due.push({ f, u, due: c.due });
    }
  }
  due.sort((a, b) => a.due - b.due);
  return [...due.map(({ f, u }) => ({ f, u })), ...fresh.slice(0, newAllowance(sid))];
}
