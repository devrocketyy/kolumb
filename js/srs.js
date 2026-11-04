// Kolumb — powtórki rozłożone w czasie (system Leitnera z 6 pudełkami).
//
//  Pudełko:          1    2    3    4    5    6
//  Następna powtórka: 1d   2d   4d   8d   16d  32d
//
//  „Nie wiem” → pudełko 1, fiszka wraca jeszcze w tej samej sesji.
//  „Trudne”   → fiszka nie awansuje (z pudełka 3+ spada o jedno), wraca jutro.
//  „Umiem”    → awans o jedno pudełko, przerwa coraz dłuższa.
//  Fiszka jest „opanowana” od pudełka 4 (przerwa ≥ 8 dni).

import { get, startOfDay, addDays, endOfToday, dayKey } from './store.js';

export const INTERVALS = [0, 1, 2, 4, 8, 16, 32];
export const MAX_BOX = 6;
export const MASTERED_BOX = 4;
export const NEW_PER_DAY = 10; // nowych fiszek dziennie na dział
const MINUTE = 60000;

export const cardKey = (sid, did, cid) => `${sid}/${did}/${cid}`;

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

// Podsumowanie jednego działu.
export function dzialSummary(sid, d) {
  const cards = get().cards;
  const end = endOfToday();
  const today = dayKey();
  let due = 0, fresh = 0, mastered = 0, learnedToday = 0, points = 0;
  for (const f of d.fiszki) {
    const c = cards[cardKey(sid, d.id, f.id)];
    if (!c || !c.reps) { fresh++; continue; }
    if (c.first && dayKey(c.first) === today) learnedToday++;
    if (c.due <= end) due++;
    if (c.box >= MASTERED_BOX) mastered++;
    points += Math.min(c.box, MASTERED_BOX);
  }
  const total = d.fiszki.length;
  const newToday = Math.min(fresh, Math.max(0, NEW_PER_DAY - learnedToday));
  return {
    total,
    due,
    fresh,
    newToday,
    todo: due + newToday,
    mastered,
    progress: total ? points / (total * MASTERED_BOX) : 0,
  };
}

// Kolejka na dzisiejszą sesję: najpierw zaległe powtórki, potem nowe fiszki.
export function buildQueue(sid, d) {
  const cards = get().cards;
  const end = endOfToday();
  const s = dzialSummary(sid, d);
  const due = [];
  const fresh = [];
  for (const f of d.fiszki) {
    const c = cards[cardKey(sid, d.id, f.id)];
    if (!c || !c.reps) fresh.push(f);
    else if (c.due <= end) due.push({ f, due: c.due });
  }
  due.sort((a, b) => a.due - b.due);
  return [...due.map((x) => x.f), ...fresh.slice(0, s.newToday)];
}
