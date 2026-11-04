// Kolumb — grywalizacja: punkty XP, cel dnia, zadania dnia, odznaki, dźwięki i konfetti.
import * as store from './store.js';

// ---------- XP i dzienne liczniki ----------
export const GOALS = [10, 20, 30, 50];
export const goal = () => Number(store.get().settings.dailyGoal) || 20;

export function today() {
  const st = store.get();
  const k = store.dayKey();
  st.daily ||= {};
  st.daily[k] ||= { xp: 0, lekcje: 0, fiszki: 0, poprawne: 0, zadania: 0, idealne: 0 };
  return st.daily[k];
}

export const xpTotal = () => store.get().xp || 0;
export const level = (xp = xpTotal()) => Math.floor(Math.sqrt(xp / 25)) + 1; // 25, 100, 225, 400… XP
export const levelFloor = (lv) => (lv - 1) ** 2 * 25;

let listeners = [];
export const onChange = (fn) => listeners.push(fn);

// Dodaje XP i liczniki dnia; zwraca listę świeżo zdobytych odznak.
export function award(xp, counters = {}) {
  const st = store.get();
  const d = today();
  const before = d.xp;
  const lvBefore = level();
  st.xp = (st.xp || 0) + xp;
  d.xp += xp;
  for (const [k, v] of Object.entries(counters)) d[k] = (d[k] || 0) + v;
  const events = [];
  if (before < goal() && d.xp >= goal()) events.push({ type: 'goal' });
  if (level() > lvBefore) events.push({ type: 'level', level: level() });
  events.push(...checkBadges().map((b) => ({ type: 'badge', badge: b })));
  store.save();
  listeners.forEach((fn) => fn(events));
  return events;
}

// ---------- zadania dnia ----------
const QUEST_POOL = [
  { id: 'xp', name: (n) => `Zdobądź ${n} XP`, key: 'xp', n: () => goal() },
  { id: 'lekcje', name: (n) => `Ukończ ${n} ${n === 1 ? 'lekcję' : 'lekcje'}`, key: 'lekcje', n: () => 2 },
  { id: 'fiszki', name: (n) => `Oceń ${n} fiszek`, key: 'fiszki', n: () => 20 },
  { id: 'poprawne', name: (n) => `Odpowiedz poprawnie na ${n} pytań`, key: 'poprawne', n: () => 15 },
  { id: 'idealne', name: () => 'Ukończ lekcję bez błędu', key: 'idealne', n: () => 1 },
  { id: 'zadania', name: (n) => `Rozwiąż ${n} zadania maturalne`, key: 'zadania', n: () => 3 },
];
export function quests() {
  const k = store.dayKey();
  let h = 0;
  for (const c of k) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  const rest = QUEST_POOL.slice(1);
  const pick = [QUEST_POOL[0]];
  while (pick.length < 3) {
    const q = rest[h % rest.length];
    h = (h * 1103515245 + 12345) >>> 0;
    if (!pick.includes(q)) pick.push(q);
  }
  const d = today();
  return pick.map((q) => { const n = q.n(); return { id: q.id, name: q.name(n), n, v: Math.min(n, d[q.key] || 0) }; });
}

// ---------- odznaki ----------
export const BADGES = [
  { id: 'start', name: 'Wypłynięcie', opis: 'Zdobądź pierwsze punkty XP', test: (s) => (s.xp || 0) > 0 },
  { id: 'lekcja1', name: 'Pierwszy rejs', opis: 'Ukończ pierwszą lekcję', test: (s) => lessonsDone(s) >= 1 },
  { id: 'lekcja25', name: 'Stary wilk morski', opis: 'Ukończ 25 lekcji', test: (s) => lessonsDone(s) >= 25, max: 25, val: (s) => lessonsDone(s) },
  { id: 'idealna', name: 'Bez skazy', opis: 'Ukończ lekcję bez żadnego błędu', test: (s) => Object.values(s.lekcje || {}).some((l) => l.idealne) },
  { id: 'seria3', name: 'Pomyślne wiatry', opis: 'Ucz się 3 dni z rzędu', test: () => store.streak().longest >= 3, max: 3, val: () => store.streak().longest },
  { id: 'seria7', name: 'Tydzień na morzu', opis: 'Ucz się 7 dni z rzędu', test: () => store.streak().longest >= 7, max: 7, val: () => store.streak().longest },
  { id: 'seria30', name: 'Wielka wyprawa', opis: 'Ucz się 30 dni z rzędu', test: () => store.streak().longest >= 30, max: 30, val: () => store.streak().longest },
  { id: 'cel', name: 'Cel osiągnięty', opis: 'Zrealizuj dzienny cel XP', test: (s) => Object.values(s.daily || {}).some((d) => d.xp >= goal()) },
  { id: 'xp1000', name: 'Kartograf', opis: 'Zdobądź 1000 XP', test: (s) => (s.xp || 0) >= 1000, max: 1000, val: (s) => s.xp || 0 },
  { id: 'fiszki100', name: 'Pamięć kapitana', opis: 'Opanuj 100 fiszek', test: (s) => mastered(s) >= 100, max: 100, val: (s) => mastered(s) },
  { id: 'fiszki1000', name: 'Encyklopedysta', opis: 'Opanuj 1000 fiszek', test: (s) => mastered(s) >= 1000, max: 1000, val: (s) => mastered(s) },
  { id: 'test100', name: 'Celny strzał', opis: 'Zdobądź 100% w teście', test: (s) => s.tests.some((t) => t.score === t.total && t.total >= 5) },
  { id: 'zadania20', name: 'Maturzysta', opis: 'Rozwiąż 20 zadań maturalnych', test: (s) => Object.keys(s.zadania).length >= 20, max: 20, val: (s) => Object.keys(s.zadania).length },
  { id: 'egzamin', name: 'Próba generalna', opis: 'Ukończ próbną maturę', test: (s) => Object.values(s.egzaminy || {}).some((e) => e.koniec) },
];
const lessonsDone = (s) => Object.values(s.lekcje || {}).reduce((n, l) => n + (l.n || 0), 0);
const mastered = (s) => Object.values(s.cards).filter((c) => c.box >= 4).length;

export function checkBadges() {
  const st = store.get();
  st.odznaki ||= {};
  const fresh = [];
  for (const b of BADGES) {
    if (st.odznaki[b.id]) continue;
    let ok = false;
    try { ok = b.test(st); } catch { ok = false; }
    if (ok) { st.odznaki[b.id] = Date.now(); fresh.push(b); }
  }
  return fresh;
}

export function badgeProgress(b) {
  const st = store.get();
  if (st.odznaki?.[b.id]) return 1;
  if (!b.max) return 0;
  try { return Math.min(1, b.val(st) / b.max); } catch { return 0; }
}

// ---------- dźwięki (syntezowane, bez plików) ----------
let ctx = null;
const soundOn = () => store.get().settings.sound !== false;
function tone(freq, start, dur, type = 'sine', vol = 0.12) {
  const o = ctx.createOscillator();
  const g = ctx.createGain();
  o.type = type;
  o.frequency.setValueAtTime(freq, ctx.currentTime + start);
  g.gain.setValueAtTime(0, ctx.currentTime + start);
  g.gain.linearRampToValueAtTime(vol, ctx.currentTime + start + 0.01);
  g.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + start + dur);
  o.connect(g).connect(ctx.destination);
  o.start(ctx.currentTime + start);
  o.stop(ctx.currentTime + start + dur + 0.02);
}
export function sound(kind) {
  if (!soundOn()) return;
  try {
    ctx ||= new (window.AudioContext || window.webkitAudioContext)();
    if (ctx.state === 'suspended') ctx.resume();
    if (kind === 'ok') { tone(660, 0, 0.12); tone(990, 0.09, 0.18); }
    else if (kind === 'bad') { tone(220, 0, 0.18, 'triangle', 0.14); tone(180, 0.12, 0.22, 'triangle', 0.12); }
    else if (kind === 'match') tone(880, 0, 0.1, 'sine', 0.08);
    else if (kind === 'win') [523, 659, 784, 1047].forEach((f, i) => tone(f, i * 0.11, 0.28, 'sine', 0.1));
    else if (kind === 'tap') tone(520, 0, 0.05, 'sine', 0.05);
  } catch { /* brak dźwięku — nic się nie dzieje */ }
  if (kind === 'bad') navigator.vibrate?.(60);
}

// ---------- konfetti ----------
export function confetti(n = 70) {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const box = document.createElement('div');
  box.className = 'confetti';
  box.setAttribute('aria-hidden', 'true');
  const colors = ['var(--c-blue)', 'var(--c-gold)', 'var(--c-green)', 'var(--c-red)', 'var(--c-purple)', 'var(--c-orange)'];
  for (let i = 0; i < n; i++) {
    const p = document.createElement('i');
    p.style.left = `${Math.random() * 100}%`;
    p.style.background = colors[i % colors.length];
    p.style.animationDelay = `${Math.random() * 0.5}s`;
    p.style.animationDuration = `${1.6 + Math.random() * 1.4}s`;
    p.style.setProperty('--dx', `${(Math.random() - 0.5) * 160}px`);
    p.style.setProperty('--r', `${Math.random() * 720 - 360}deg`);
    if (i % 3 === 0) p.style.borderRadius = '50%';
    box.appendChild(p);
  }
  document.body.appendChild(box);
  setTimeout(() => box.remove(), 3600);
}
