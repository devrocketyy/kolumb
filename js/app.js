// IndexLab — aplikacja do nauki do matury (dawniej Kolumb).
import * as store from './store.js';
import { loadIndex, loadFull, takeErrors } from './data.js';
import * as game from './game.js';
import * as cloud from './cloud.js';
import * as dostep from './dostep.js';
import { cardKey, nextState, intervalLabel, summary, buildQueue, newAllowance, MASTERED_BOX, setAutoRate, tempoAuto, newPerDay } from './srs.js';

const REPORT_EMAIL = 'kontakt.indexlab@gmail.com';
const TEST_SIZE = 10;
const LITERY = ['A', 'B', 'C', 'D'];

const app = document.getElementById('app');
let subjects = [];
let loadErrors = [];
let keyHandler = null;
let installEvent = null;

// ---------- marka IndexLab (logo z plików marki, kolor dziedziczony: currentColor) ----------
const BRAND_MARK = '<svg class="brand-mark" viewBox="14.14 14.14 171.72 171.72" aria-hidden="true"><circle cx="100" cy="100" r="76" fill="none" stroke="currentColor" stroke-width="7"/><path d="M92.509765625 145.5325H107.490234375V91.9075H92.509765625Z" fill="currentColor"/><path d="M100.00,54.47 Q101.87,68.20 115.60,70.07 Q101.87,71.94 100.00,85.67 Q98.13,71.94 84.40,70.07 Q98.13,68.20 100.00,54.47Z" fill="currentColor"/></svg>';
const BRAND_NAME = '<svg class="brand-name" viewBox="3.73 18.89 378.32 95.83" role="img" aria-label="indexlab"><path d="M15.078125 110.0H29.482421875V58.4375H15.078125ZM51.04296875 81.337890625C51.04296875 73.330078125 55.193359375 69.765625 61.150390625 69.765625C67.15625 69.765625 70.623046875 73.427734375 70.623046875 80.361328125V110.0H84.978515625V77.724609375C84.978515625 64.6875 77.8984375 57.36328125 66.912109375 57.36328125C59.490234375 57.36328125 54.265625 60.68359375 50.798828125 66.54296875V58.4375H36.638671875V110.0H51.04296875ZM112.251953125 111.07421875C119.0390625 111.07421875 124.556640625 108.095703125 127.53515625 102.08984375H127.583984375V110.0H141.744140625V37.24609375H127.388671875V65.56640625H127.33984375C124.01953125 60.0 118.84375 57.36328125 112.154296875 57.36328125C98.970703125 57.36328125 89.9375 68.349609375 89.9375 84.169921875C89.9375 100.33203125 98.775390625 111.07421875 112.251953125 111.07421875ZM115.962890625 99.35546875C108.98046875 99.35546875 104.439453125 93.837890625 104.439453125 84.169921875C104.439453125 74.501953125 108.98046875 68.984375 115.962890625 68.984375C123.23828125 68.984375 128.072265625 74.990234375 128.072265625 84.169921875C128.072265625 93.3984375 123.23828125 99.35546875 115.962890625 99.35546875ZM172.484375 111.171875C184.984375 111.171875 194.9453125 104.04296875 196.849609375 93.7890625H183.71484375C182.396484375 97.79296875 178.5390625 100.380859375 172.923828125 100.380859375C165.35546875 100.380859375 160.9609375 95.44921875 160.716796875 87.83203125H197.38671875V83.974609375C197.38671875 68.251953125 187.181640625 57.265625 171.99609375 57.265625C157.201171875 57.265625 146.703125 68.544921875 146.703125 84.267578125C146.703125 99.94140625 156.859375 111.171875 172.484375 111.171875ZM160.814453125 78.65234375C161.595703125 72.20703125 165.84375 68.203125 172.2890625 68.203125C178.783203125 68.203125 183.080078125 72.20703125 183.8125 78.65234375ZM197.609375 110.0H213.33203125L218.60546875 102.08984375C220.509765625 98.96484375 222.21875 96.1328125 223.9765625 93.251953125C225.63671875 96.1328125 227.345703125 98.96484375 229.201171875 102.08984375L234.376953125 110.0H250.1484375L231.935546875 83.388671875L249.318359375 58.4375H233.83984375L229.201171875 65.6640625C227.345703125 68.642578125 225.734375 71.42578125 224.123046875 74.208984375C222.51171875 71.42578125 220.900390625 68.642578125 219.142578125 65.6640625L214.6015625 58.4375H198.87890625L216.06640625 83.73046875ZM267.216796875 37.24609375H252.8125V110.0H267.216796875ZM290.14453125 110.87890625C298.0546875 110.87890625 302.498046875 107.75390625 305.232421875 102.724609375H305.427734375V110.0H319.490234375V75.0390625C319.490234375 64.00390625 311.384765625 57.36328125 297.2734375 57.36328125C283.11328125 57.36328125 274.71484375 64.1015625 274.080078125 74.74609375H287.60546875C287.947265625 70.791015625 291.462890625 68.056640625 296.833984375 68.056640625C302.107421875 68.056640625 305.28125 70.693359375 305.28125 74.501953125V74.84375C305.28125 78.1640625 301.9609375 78.603515625 292.537109375 79.53125C281.794921875 80.5078125 272.419921875 83.828125 272.419921875 95.44921875C272.419921875 105.751953125 279.841796875 110.87890625 290.14453125 110.87890625ZM294.1484375 100.869140625C289.314453125 100.869140625 286.189453125 98.720703125 286.189453125 95.05859375C286.189453125 90.95703125 290.095703125 89.052734375 295.02734375 88.3203125C299.666015625 87.587890625 303.71875 86.904296875 305.37890625 85.9765625V91.15234375C305.37890625 96.71875 301.08203125 100.869140625 294.1484375 100.869140625ZM356.1875 111.07421875C369.6640625 111.07421875 378.501953125 100.33203125 378.501953125 84.169921875C378.501953125 68.349609375 369.46875 57.36328125 356.28515625 57.36328125C349.595703125 57.36328125 344.419921875 60.0 341.099609375 65.56640625H341.05078125V37.24609375H326.646484375V110.0H340.85546875V102.08984375H340.904296875C343.8828125 108.095703125 349.400390625 111.07421875 356.1875 111.07421875ZM352.4765625 99.35546875C345.201171875 99.35546875 340.3671875 93.3984375 340.3671875 84.169921875C340.3671875 74.990234375 345.201171875 68.984375 352.4765625 68.984375C359.458984375 68.984375 364.0 74.501953125 364.0 84.169921875C364.0 93.837890625 359.458984375 99.35546875 352.4765625 99.35546875Z" fill="currentColor"/><path d="M22.28,22.44 Q24.08,35.64 37.28,37.44 Q24.08,39.24 22.28,52.44 Q20.48,39.24 7.28,37.44 Q20.48,35.64 22.28,22.44Z" fill="currentColor"/></svg>';

// ---------- narzędzia ----------
const esc = (s) =>
  String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

function plural(n, one, few, many) {
  if (n === 1) return one;
  const d = n % 10, h = n % 100;
  return d >= 2 && d <= 4 && (h < 12 || h > 14) ? few : many;
}
const nFiszek = (n) => `${n} ${plural(n, 'fiszka', 'fiszki', 'fiszek')}`;
const nZadan = (n) => `${n} ${plural(n, 'zadanie', 'zadania', 'zadań')}`;

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

const pct = (x) => Math.round(x * 100);
const enc = encodeURIComponent;
const findSubject = (sid) => subjects.find((s) => s.id === sid);
const findDzial = (s, did) => s?.dzialy.find((d) => d.id === did);
const dzialOf = (s, u) => findDzial(s, u.dzialId);
const allUnits = (s) => s.dzialy.flatMap((d) => d.poddzialy);
const hrefDzial = (sid, did) => `#/d/${enc(sid)}/${enc(did)}`;
const hrefUnit = (sid, uid) => `#/p/${enc(sid)}/${enc(uid)}`;

// Zakres nauki: cały dział ("d") albo poddział ("p").
function resolveScope(sid, type, id) {
  const s = findSubject(sid);
  if (!s) return null;
  if (type === 'x') { // test diagnostyczny: cały kurs, pytania dobierane według wag działów
    const units = allUnits(s).filter((u) => !u.zablokowany && u.pytania.length);
    return units.length ? { s, type, id, units, title: 'Test diagnostyczny', sub: s.nazwa, back: '#/' } : null;
  }
  if (type === 'w') { // własna powtórka: tematy wybrane przez ucznia (#/powtorka)
    const sel = wlasnaSel(s);
    const units = (sel.tematy?.length ? sel.tematy.map((x) => s.units.get(x)).filter(Boolean) : allUnits(s)).filter((u) => !u.zablokowany);
    if (!units.length) return null;
    return { s, type, id, units, title: 'Własna powtórka', sub: s.nazwa, back: '#/powtorka' };
  }
  if (type === 'd') {
    const d = findDzial(s, id);
    if (!d) return null;
    return { s, type, id, units: d.poddzialy, title: d.nazwa, sub: s.nazwa, back: hrefDzial(s.id, d.id), dzial: d };
  }
  const u = s.units.get(id);
  if (!u) return null;
  const d = dzialOf(s, u);
  return { s, type, id, units: [u], title: u.nazwa, sub: d?.nazwa || s.nazwa, back: hrefUnit(s.id, u.id), dzial: d, unit: u };
}
const scopePath = (sc) => `${enc(sc.s.id)}/${sc.type}/${enc(sc.id)}`;
const scopeQuestions = (sc) => sc.units.flatMap((u) => u.pytania.map((q) => ({ q, u })));

const tasksOf = (s, did) => s.arkusze.flatMap((a) => a.zadania.filter((z) => !did || z.dzialy.includes(did)));
const taskKey = (sid, z) => `${sid}/${z.arkusz}/${z.nr}`;

const ICONS = {
  compass: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.25" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 8.2 13.4 13.4 8.2 15.8 10.6 10.6Z" fill="currentColor"/></svg>',
  back: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  next: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
  flag: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 21V4m0 0h11l-2 4 2 4H5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  cards: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="14" height="14" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7 3h11.5A2.5 2.5 0 0 1 21 5.5V17" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
  quiz: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.25" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9.5 9.3a2.6 2.6 0 1 1 3.6 2.4c-.7.3-1.1.9-1.1 1.6v.4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="12" cy="17" r="1.1" fill="currentColor"/></svg>',
  doc: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h9l4 4v14H6z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 12h7M9 16h5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
  book: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5zM4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
  exam: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M14 3v5h5M10 13h6M10 17h6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
  check: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  flame: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22c4 0 7-2.8 7-6.8 0-3.4-2.2-5.6-3.6-7.2-.3 1.9-1.2 3-2.4 3.5.4-3.4-1.2-6.6-4-8.5.2 3.2-1.4 5-2.9 6.8C4.8 11.4 5 13 5 15.2 5 19.2 8 22 12 22z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
  download: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0-4.5-4.5M12 15l4.5-4.5M4 20h16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  bolt: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 2 4.5 13.5h6L9.5 22l9-11.5h-6z" fill="currentColor"/></svg>',
  heart: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7.5-4.6-9.4-9.3C1.2 8.2 3.4 4.5 7 4.5c2 0 3.6 1.1 5 3 1.4-1.9 3-3 5-3 3.6 0 5.8 3.7 4.4 7.2C19.5 16.4 12 21 12 21z" fill="currentColor"/></svg>',
  star: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.8 5.8 6.3.9-4.6 4.4 1.1 6.3L12 17.2l-5.6 3 1.1-6.3L2.9 9.5l6.3-.9z" fill="currentColor"/></svg>',
  crown: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8l4.5 4L12 4l4.5 8L21 8l-2 11H5z" fill="currentColor"/></svg>',
  trophy: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h10v5a5 5 0 0 1-10 0zM7 5H3.5a3.5 3.5 0 0 0 3.6 4M17 5h3.5a3.5 3.5 0 0 1-3.6 4M12 13v4M8 21h8M9 17h6v4H9z" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  target: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.9"/><circle cx="12" cy="12" r="5" fill="none" stroke="currentColor" stroke-width="1.9"/><circle cx="12" cy="12" r="1.6" fill="currentColor"/></svg>',
  play: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l10.5-6.5z" fill="currentColor"/></svg>',
  lock: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M8 11V8a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>',
  clock: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>',
  search: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
  redo: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12a8 8 0 1 0 2.4-5.7M4 4v4h4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  cog: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.5 5.5l1.7 1.7M16.8 16.8l1.7 1.7M5.5 18.5l1.7-1.7M16.8 7.2l1.7-1.7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
  news: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h13v14H6a2 2 0 0 1-2-2zM17 9h3v8a2 2 0 0 1-2 2h-1M7.5 9h6M7.5 12.5h6M7.5 16h3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  sound: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4zM16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
};

function toast(msg, action) {
  const el = document.getElementById('toast');
  el.innerHTML = `<span>${esc(msg)}</span>${action ? `<button type="button" class="toast-btn">${esc(action.label)}</button>` : ''}`;
  el.hidden = false;
  el.classList.add('show');
  if (action) el.querySelector('button').onclick = action.run;
  clearTimeout(toast.t);
  toast.t = setTimeout(() => {
    el.classList.remove('show');
    setTimeout(() => (el.hidden = true), 300);
  }, action ? 10000 : 2600);
}

// ---------- zgłaszanie błędów ----------
function mailto(subject, lines) {
  return `mailto:${REPORT_EMAIL}?subject=${enc(subject)}&body=${enc(lines.join('\n'))}`;
}

function reportHref(s, u, kind, item) {
  const d = dzialOf(s, u);
  const lines = [
    'Dzień dobry,', '',
    `zgłaszam błąd w ${kind === 'fiszka' ? 'fiszce' : 'pytaniu testowym'} w aplikacji IndexLab.`, '',
    `Przedmiot: ${s.nazwa}`,
    `Dział: ${d ? d.nazwa : ''}`,
    `Poddział: ${u.nazwa}`,
    `ID: ${s.id}/${u.id}/${item.id}`, '',
  ];
  if (kind === 'fiszka') {
    lines.push(`Pytanie: ${item.przod}`, `Odpowiedź: ${item.tyl}`);
  } else {
    lines.push(`Pytanie: ${item.pytanie}`);
    item.odpowiedzi.forEach((o, i) => lines.push(`${LITERY[i]}) ${o}${i === item.poprawna ? '  ← oznaczona jako poprawna' : ''}`));
    if (item.wyjasnienie) lines.push(`Wyjaśnienie: ${item.wyjasnienie}`);
  }
  lines.push(`Źródło: ${item.zrodlo || '—'}`, '', 'Na czym polega błąd:', '', '');
  return mailto(`[IndexLab] Błąd: ${s.skrot} — ${kind} ${u.id}/${item.id}`, lines);
}

function reportTaskHref(s, a, z) {
  return mailto(`[IndexLab] Błąd: ${s.skrot} — ${a.nazwa}, zadanie ${z.nr}`, [
    'Dzień dobry,', '', 'zgłaszam błąd w zadaniu maturalnym w aplikacji IndexLab.', '',
    `Przedmiot: ${s.nazwa}`, `Arkusz: ${a.nazwa}`, `Zadanie: ${z.nr}`, '',
    `Polecenie: ${z.polecenie}`, '', `Odpowiedź w aplikacji: ${z.odpowiedz}`, '',
    'Na czym polega błąd:', '', '',
  ]);
}

// Przycisk otwiera okienko w aplikacji (link mailto: wyrzucał z aplikacji zainstalowanej na telefonie).
const reportBtn = (href) => `<button type="button" class="btn-report" data-report="${esc(href)}">${ICONS.flag}<span>Zgłoś błąd</span></button>`;

const REPORT_KINDS = ['Błąd merytoryczny', 'Literówka', 'Zła odpowiedź w kluczu', 'Niejasne polecenie', 'Coś nie działa'];
function openReport(href) {
  const u = new URL(href);
  const subject = u.searchParams.get('subject') || '[IndexLab] Zgłoszenie';
  const ctx = (u.searchParams.get('body') || '').replace(/\n*Na czym polega błąd:\s*$/, '').replace(/^Dzień dobry,\n\n/, '');
  document.querySelector('.report-layer')?.remove();
  const layer = document.createElement('div');
  layer.className = 'report-layer';
  layer.innerHTML = `<div class="report-box" role="dialog" aria-modal="true" aria-labelledby="rep-title">
    <div class="report-top"><h2 id="rep-title">Zgłoś błąd</h2><button type="button" class="icon-btn" data-rep="close" aria-label="Zamknij">${ICONS.close}</button></div>
    <div class="rep-kinds">${REPORT_KINDS.map((k, i) => `<button type="button" class="rep-kind ${i ? '' : 'active'}" data-kind="${esc(k)}">${esc(k)}</button>`).join('')}</div>
    <textarea class="type-input rep-text" rows="4" maxlength="2000" placeholder="Co jest nie tak? (opcjonalnie)" aria-label="Opis błędu"></textarea>
    <div class="rep-actions">
      ${cloud.enabled() ? '<button type="button" class="btn btn-primary btn-lg" data-rep="send">Wyślij zgłoszenie</button>' : ''}
      <button type="button" class="btn ${cloud.enabled() ? 'btn-ghost' : 'btn-primary'} btn-lg" data-rep="copy">Skopiuj zgłoszenie</button>
      ${cloud.enabled() ? '' : `<p class="muted small">Wklej je w wiadomości na <strong>${REPORT_EMAIL}</strong>.</p>`}
    </div>
    <p class="muted small">Zgłoszenie zawiera treść fiszki lub zadania, więc szybko znajdziemy błąd.</p>
  </div>`;
  document.body.appendChild(layer);
  let kind = REPORT_KINDS[0];
  const text = () => `${kind}\n\n${layer.querySelector('.rep-text').value.trim() || '(bez opisu)'}\n\n---\n${ctx}`;
  const close = () => { layer.remove(); keyHandler = prevKey; };
  const prevKey = keyHandler;
  keyHandler = (e) => { if (e.key === 'Escape') close(); };
  layer.addEventListener('click', async (e) => {
    if (e.target === layer) return close();
    const k = e.target.closest('[data-kind]');
    if (k) { kind = k.dataset.kind; layer.querySelectorAll('.rep-kind').forEach((b) => b.classList.toggle('active', b === k)); return; }
    const act = e.target.closest('[data-rep]')?.dataset.rep;
    if (act === 'close') close();
    if (act === 'copy') {
      try { await navigator.clipboard.writeText(`${subject}\n\n${text()}`); toast(`Skopiowano — wklej w wiadomości na ${REPORT_EMAIL}.`); }
      catch { layer.querySelector('.rep-text').value = `${subject}\n\n${text()}`; layer.querySelector('.rep-text').select(); toast('Zaznaczono tekst — skopiuj go ręcznie.'); }
    }
    if (act === 'send') {
      if (cloud.enabled()) {
        try {
          await cloud.api('/rest/v1/zgloszenia', { method: 'POST', token: await cloud.tokenOrNull(), headers: { Prefer: 'return=minimal' }, body: { temat: subject, rodzaj: kind, opis: text() } });
          close(); toast('Dziękujemy! Zgłoszenie wysłane.'); game.sound('ok');
        } catch (err) { toast(err.message); }
        return;
      }
      // nowa karta/aplikacja pocztowa — IndexLab zostaje otwarty
      const a = document.createElement('a');
      a.href = `mailto:${REPORT_EMAIL}?subject=${enc(subject)}&body=${enc(text())}`;
      a.target = '_blank'; a.rel = 'noopener';
      document.body.appendChild(a); a.click(); a.remove();
      close(); toast('Otwieram pocztę… Jeśli się nie otworzyła, użyj „Skopiuj zgłoszenie”.');
    }
  });
  layer.querySelector('.rep-text').focus({ preventScroll: true });
}
document.addEventListener('click', (e) => {
  const b = e.target.closest('[data-report]');
  if (!b) return;
  e.preventDefault();
  e.stopPropagation();
  openReport(b.dataset.report);
}, true);
const sourceTag = (z) => (z ? `<span class="source">Źródło: ${esc(z)}</span>` : '');

// ---------- elementy wspólne ----------
function progressBar(value, label) {
  const p = pct(value);
  return `<div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${p}" aria-label="${esc(label || 'Postęp')}"><span style="width:${p}%"></span></div>`;
}

function pageHead(title, backHref, sub) {
  return `<header class="page-head">
    ${backHref ? `<a class="icon-btn" href="${backHref}" aria-label="Wróć">${ICONS.back}</a>` : ''}
    <div class="page-head-text">${sub ? `<p class="eyebrow">${esc(sub)}</p>` : ''}<h1>${esc(title)}</h1></div>
  </header>`;
}

function unitRow(href, name, sm, extra = '') {
  return `<a class="dzial-row" href="${href}">
    <div class="dzial-row-top">
      <span class="dzial-name">${esc(name)}</span>
      ${sm.todo ? `<span class="badge" aria-label="Do powtórki dziś: ${sm.todo}">${sm.todo}</span>` : sm.total ? `<span class="badge badge-ok" aria-label="Na dziś gotowe">${ICONS.check}</span>` : ''}
    </div>
    ${progressBar(sm.progress, `Opanowanie: ${name}`)}
    <div class="dzial-meta"><span>${pct(sm.progress)}% opanowania</span><span>${sm.mastered}/${nFiszek(sm.total)}${extra}</span></div>
  </a>`;
}

function statsCard(sm) {
  return `<section class="card">
    <div class="ring-row">
      <div class="ring" style="--p:${pct(sm.progress)}"><span>${pct(sm.progress)}%</span></div>
      <div class="ring-text"><strong>Opanowanie</strong>
        <span>${sm.mastered} z ${sm.total} ${plural(sm.total, 'fiszki', 'fiszek', 'fiszek')} opanowanych na dłużej</span></div>
    </div>
    <div class="mini-stats">
      <div><strong>${sm.due}</strong><span>do powtórki</span></div>
      <div><strong>${sm.newToday}</strong><span>nowe na dziś</span></div>
      <div><strong>${sm.fresh}</strong><span>jeszcze nieznane</span></div>
    </div>
  </section>`;
}

function notFound() {
  app.innerHTML = `<div class="empty">
    <div class="empty-icon">${ICONS.compass}</div>
    <h1>Nie ma takiej strony</h1>
    <p>Możliwe, że treści zostały przeniesione.</p>
    <a class="btn btn-primary" href="#/">Wróć na start</a></div>`;
}

// ---------- ekran główny ----------
// ---------- ścieżka nauki (ekran główny) ----------
const lessonKey = (sid, type, id) => `${sid}/${type}/${id}`;
const lessonRec = (sid, type, id) => store.get().lekcje?.[lessonKey(sid, type, id)] || { n: 0 };

// Przedmiot wybrany przez ucznia (na start i w zakładce Nauka).
const PLANNED = ['Historia', 'Geografia', 'Język polski', 'Matematyka', 'Biologia', 'Język angielski'];
function currentSubject() {
  return findSubject(store.get().settings.przedmiot) || subjects[0] || null;
}

function recommendedUnit(s) {
  const allowance = newAllowance(s.id);
  for (const d of s.dzialy) for (const u of d.poddzialy) {
    if (!u.fiszki.length && !u.pytania.length) continue;
    const sm = summary(s.id, [u], allowance);
    if (sm.progress < 0.8 && !(lessonRec(s.id, 'p', u.id).n >= 3 && sm.progress >= 0.5)) return { d, u };
  }
  const d = s.dzialy[0];
  return d ? { d, u: d.poddzialy[0] } : null;
}

// ---------- trasa nauki: działy jako odcinki, poddziały jako kolejne przystanki ----------
function pathHtml(s, rec) {
  const allowance = newAllowance(s.id);
  return s.dzialy.map((d, di) => {
    const smD = summary(s.id, d.poddzialy, allowance);
    const open = rec ? rec.d === d : di === 0;
    const doneN = d.poddzialy.filter((u) => summary(s.id, [u], allowance).progress >= 0.8).length;
    const stops = d.poddzialy.map((u, ui) => {
      if (u.zablokowany) { // treść premium bez aktywnego dostępu
        return `<li class="stop locked"><span class="stop-dot" aria-hidden="true"><i>${ICONS.lock}</i></span>
          <div class="stop-main"><a class="stop-body" href="#/plany"><span class="stop-name">${esc(u.nazwa)}</span><span class="stop-meta">Premium — odblokuj pełny kurs</span></a></div></li>`;
      }
      if (!u.fiszki.length && !u.pytania.length) { // temat bez treści (kurs w budowie)
        return `<li class="stop soon"><span class="stop-dot" aria-hidden="true"><i>${ui + 1}</i></span>
          <div class="stop-main"><div class="stop-body" aria-disabled="true"><span class="stop-name">${esc(u.nazwa)}</span><span class="stop-meta">wkrótce</span></div></div></li>`;
      }
      const sm = summary(s.id, [u], allowance);
      const lr = lessonRec(s.id, 'p', u.id);
      const cur = rec && rec.u === u;
      const state = sm.progress >= 0.8 ? 'done' : cur ? 'current' : sm.seen || lr.n ? 'started' : 'new';
      const meta = [`${pct(sm.progress)}%`, lr.n ? `${lr.n} ${plural(lr.n, 'lekcja', 'lekcje', 'lekcji')}` : '', sm.todo && sm.seen ? `${sm.todo} do powtórki` : ''].filter(Boolean).join(' · ');
      return `<li class="stop ${state}">
        <span class="stop-dot" style="--p:${pct(sm.progress)}" aria-hidden="true"><i>${state === 'done' ? ICONS.check : ui + 1}</i></span>
        <div class="stop-main">
          <button type="button" class="stop-body" data-unit="${esc(u.id)}" aria-expanded="false">
            <span class="stop-name">${esc(u.nazwa)}${cur ? ' <em class="here">tu jesteś</em>' : ''}</span>
            <span class="stop-meta">${meta}</span>
          </button>
          <div class="stop-pop" data-pop="${esc(u.id)}" hidden></div>
        </div>
      </li>`;
    }).join('');
    return `<details class="leg" ${open ? 'open' : ''}>
      <summary class="leg-head">
        <span class="leg-num">${di + 1}</span>
        <span class="leg-text"><strong>${esc(d.nazwa)}</strong><small>${d.zablokowany ? `${ICONS.lock} Premium · ${d.poddzialy.length} ${plural(d.poddzialy.length, 'temat', 'tematy', 'tematów')}` : `${doneN}/${d.poddzialy.length} opanowanych · ${pct(smD.progress)}%`}</small>${d.zablokowany ? '' : progressBar(smD.progress, d.nazwa)}</span>
        <span class="leg-chev" aria-hidden="true">${ICONS.next}</span>
      </summary>
      <ol class="stops">${stops}</ol>
    </details>`;
  }).join('');
}

function popHtml(s, u) {
  const sm = summary(s.id, [u]);
  const nQ = u.pytania.length;
  const nZ = bankTasks(s, u.dzialId).length;
  const nC = tasksOf(s, u.dzialId).length;
  const zHref = nZ ? `#/zadania/${enc(s.id)}/b/${enc(u.dzialId)}` : nC ? `#/zadania/${enc(s.id)}/d/${enc(u.dzialId)}` : '';
  return `<div class="pop-grid">
      <a class="pop-act main" href="#/lekcja/${enc(s.id)}/p/${enc(u.id)}">${ICONS.play}<span>Lekcja</span></a>
      ${u.fiszki.length ? `<a class="pop-act" href="#/fiszki/${enc(s.id)}/p/${enc(u.id)}">${ICONS.cards}<span>Fiszki${sm.todo ? ` · ${sm.todo}` : ''}</span></a>` : ''}
      ${nQ ? `<a class="pop-act" href="#/test/${enc(s.id)}/p/${enc(u.id)}">${ICONS.quiz}<span>Test</span></a>` : ''}
      ${zHref ? `<a class="pop-act" href="${zHref}">${ICONS.doc}<span>Zadania</span></a>` : ''}
      <a class="pop-act" href="${hrefUnit(s.id, u.id)}">${ICONS.book}<span>Treści</span></a>
    </div>`;
}

// „Na dziś”: zwykła lista kroków zamiast zadań z nagrodami.
function planHtml(s, rec, todo, best) {
  const d = game.today();
  const items = [
    best ? { done: !todo, href: `#/fiszki/${enc(s.id)}/d/${enc(best.d.id)}`, icon: ICONS.cards, name: todo ? `Powtórz fiszki: ${todo}` : 'Powtórki na dziś zrobione' } : null,
    rec ? { done: (d.lekcje || 0) > 0, href: `#/lekcja/${enc(s.id)}/p/${enc(rec.u.id)}`, icon: ICONS.play, name: `Lekcja: ${rec.u.nazwa}` } : null,
    rec && s.bank.length ? { done: (d.zadania || 0) > 0, href: `#/zadania/${enc(s.id)}/b/${enc(rec.d.id)}`, icon: ICONS.exam, name: `Zadanie maturalne: ${rec.d.nazwa}` } : null,
    s.aktualnosci ? { done: false, href: '#/aktualnosci', icon: ICONS.news, name: s.aktualnosci.nazwa ? s.aktualnosci.nazwa : 'Aktualności — kto jest kim' } : null,
  ].filter(Boolean);
  return `<section class="card plan">
    <h2 class="card-title">Na dziś</h2>
    ${items.map((x) => `<a class="plan-item ${x.done ? 'done' : ''}" href="${x.href}">
      <span class="plan-check" aria-hidden="true">${x.done ? ICONS.check : x.icon}</span>
      <span class="plan-name">${esc(x.name)}</span>${ICONS.next}</a>`).join('')}
  </section>`;
}

function goalCard(s, rec, todo) {
  const n = store.get().days[store.dayKey()] || 0;
  const g = game.goal();
  const st = store.streak();
  return `<section class="goal-card">
    <div class="goal-top">
      <div class="ring ring-goal ${n >= g ? 'ring-ok' : ''} ${n >= 1000 ? 'digits-4' : n >= 100 ? 'digits-3' : ''}" style="--p:${Math.min(100, pct(n / g))}"><span>${n > 9999 ? '9999+' : n}</span></div>
      <div class="goal-text">
        <strong>${n >= g ? 'Cel dnia zrobiony' : `${n} / ${g} odpowiedzi dzisiaj`}</strong>
        <span>${ICONS.flame} ${st.current ? `${st.current} ${plural(st.current, 'dzień', 'dni', 'dni')} nauki z rzędu${st.today ? '' : ' · dziś jeszcze bez nauki'}` : 'Zacznij serię — ucz się codziennie'}</span>
      </div>
    </div>
    ${rec ? `<a class="btn btn-primary btn-xl btn-continue" href="#/lekcja/${enc(s.id)}/p/${enc(rec.u.id)}">${ICONS.play}<span>Kontynuuj<small>${esc(rec.u.nazwa)}</small></span></a>` : ''}
  </section>`;
}


// Duży licznik: ile podstawy programowej przedmiotu uczeń już przerobił.
// Przerobione = fiszki, które były już w nauce; opanowane = fiszki w najwyższych pudełkach Leitnera.
const pctFine = (x) => (x > 0 && x < 0.1 ? (Math.round(x * 1000) / 10).toLocaleString('pl-PL') : String(pct(x)));
function coreCard(s) {
  const all = s.dzialy.flatMap((d) => d.poddzialy);
  const sm = summary(s.id, all, 0);
  if (!sm.total) return '';
  const done = sm.seen / sm.total;
  const mast = sm.mastered / sm.total;
  const tematy = all.filter((u) => { const x = summary(s.id, [u], 0); return x.total && x.seen === x.total; }).length;
  const rows = s.dzialy.map((d) => { const x = summary(s.id, d.poddzialy, 0); return { d, p: x.total ? x.seen / x.total : 0, m: x.total ? x.mastered / x.total : 0 }; });
  return `<section class="core-card" aria-label="Postęp w podstawie programowej">
    <div class="core-head"><span class="eyebrow">Podstawa programowa · ${esc(s.skrot || s.nazwa)}</span><a href="#/nauka" class="core-link">Nauka ${ICONS.next}</a></div>
    <div class="core-num"><b>${pctFine(done)}</b><span>%</span></div>
    <p class="core-sub">materiału przerobione</p>
    <div class="core-bar" role="img" aria-label="Przerobione ${pct(done)}%, opanowane ${pct(mast)}%"><i style="width:${done * 100}%"></i><i class="m" style="width:${mast * 100}%"></i></div>
    <p class="core-legend"><span><i class="m"></i>opanowane</span><span><i></i>przerobione</span></p>
    <dl class="core-stats">
      <div><dt>Opanowane</dt><dd>${pctFine(mast)}%</dd></div>
      <div><dt>Tematy</dt><dd>${tematy} / ${all.length}</dd></div>
      <div><dt>Fiszki</dt><dd>${sm.seen.toLocaleString('pl-PL')} / ${sm.total.toLocaleString('pl-PL')}</dd></div>
    </dl>
    <details class="core-dz"><summary>Postęp w działach</summary>
      <ol>${rows.map((r) => `<li><a href="#/nauka"><span class="core-dz-name">${esc(r.d.nazwa)}</span><b>${pctFine(r.p)}%</b><span class="core-mini"><i style="width:${r.p * 100}%"></i><i class="m" style="width:${r.m * 100}%"></i></span></a></li>`).join('')}</ol>
    </details>
  </section>`;
}

// Dotychczasowi użytkownicy Kolumba (mają już postępy) widzą raz krótką informację o nowej marce.
function rebrandNote() {
  const st = store.get();
  const veteran = Object.keys(st.cards).length || st.tests.length || (st.xp || 0) > 0;
  if (!veteran || st.settings.rebrandSeen) return '';
  return `<section class="ink rebrand-note" role="status">${BRAND_MARK}
    <div><strong>Kolumb jest teraz częścią IndexLab</strong>
      <p>Ta sama aplikacja pod nową nazwą — Twoje postępy, seria i odznaki zostały zachowane.</p></div>
    <button type="button" class="icon-btn" data-act="rebrand-ok" aria-label="Zamknij informację">${ICONS.close}</button></section>`;
}

// ---------- zakładka „Dziś” ----------
// ---------- plan do matury (personalizacja tempa) ----------
// Uczeń wybiera suwakiem dzień, w którym chce skończyć materiał; z tego wynika dzienna porcja fiszek i zadań.
const MIN_NA_FISZKE = 0.8; // nowa fiszka + jej późniejsze powtórki ≈ 50 s
const MIN_NA_ZADANIE = 3;
// Faza powtórek przed maturą: fiszka z ostatniego dnia nowego materiału potrzebuje ok. 4 tygodni (1+2+4+8+16 dni),
// żeby przejść kolejne pudełka; do tego 4–5 pełnych arkuszy z przedmiotu. Minimum 4 tygodnie, zalecane 6.
const POWTORKI_MIN = 28;
const POWTORKI_ZALECANE = 42;
const DAY = 86400000;
const parseDay = (iso) => { const [y, m, d] = String(iso).split('-').map(Number); return new Date(y, m - 1, d).getTime(); };
const isoDay = (t) => { const d = new Date(t); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };
const fmtDay = (t) => new Date(t).toLocaleDateString('pl-PL', { day: 'numeric', month: 'long', year: 'numeric' });
const fmtShort = (t) => new Date(t).toLocaleDateString('pl-PL', { day: 'numeric', month: 'short' });
const todayStart = () => { const d = new Date(); d.setHours(0, 0, 0, 0); return d.getTime(); };
const allTasks = (s) => [...tasksOf(s), ...bankTasks(s)];

function planOf(s, over) {
  const p = { ...(store.get().settings.plan?.[s.id] || {}), ...(over || {}) };
  const data = p.data || s.egzamin || null;
  if (!data) return { data: null };
  const today = todayStart();
  const egz = parseDay(data);
  const dniDoMatury = Math.max(1, Math.round((egz - today) / DAY));
  let koniec = p.koniec ? parseDay(p.koniec) : egz - Math.min(POWTORKI_ZALECANE, Math.floor(dniDoMatury / 4)) * DAY;
  koniec = Math.min(egz, Math.max(today + DAY, koniec));
  const dni = Math.max(1, Math.round((koniec - today) / DAY));
  const fresh = summary(s.id, allUnits(s), 0).fresh;
  const st = store.get().zadania;
  const zad = allTasks(s);
  const zLeft = zad.filter((z) => !st[taskKey(s.id, z)]).length;
  const dk = store.dayKey();
  const zDzis = zad.filter((z) => { const r = st[taskKey(s.id, z)]; return r?.at && store.dayKey(r.at) === dk; }).length;
  const rate = fresh ? Math.min(150, Math.max(3, Math.ceil(fresh / dni))) : 0;
  const zRate = zLeft ? Math.ceil(zLeft / dni) : 0;
  return {
    ustawiony: !!p.koniec, data, egz, koniec, dni, dniDoMatury, rezerwa: Math.round((egz - koniec) / DAY),
    fresh, zLeft, zTotal: zad.length, zDzis, rate, zRate,
    minuty: Math.ceil(rate * MIN_NA_FISZKE + zRate * MIN_NA_ZADANIE),
  };
}

function refreshAutoRates() {
  for (const s of subjects) { const p = planOf(s); setAutoRate(s.id, p.data && !trybWlasny() ? p.rate || 3 : 0); }
}

// Następne zadania: najpierw z działu, którego uczeń się teraz uczy.
function nextTasksHref(s) {
  const st = store.get().zadania;
  const open = (list) => list.some((z) => !st[taskKey(s.id, z)]);
  const rec = recommendedUnit(s);
  const order = rec ? [rec.d, ...s.dzialy.filter((d) => d !== rec.d)] : s.dzialy;
  for (const d of order) {
    if (open(bankTasks(s, d.id))) return `#/zadania/${enc(s.id)}/b/${enc(d.id)}`;
    if (open(tasksOf(s, d.id))) return `#/zadania/${enc(s.id)}/d/${enc(d.id)}`;
  }
  const a = s.arkusze.find((x) => !x.zablokowany && open(x.zadania));
  return a ? `#/zadania/${enc(s.id)}/a/${enc(a.id)}` : '#/matura';
}

function planCard(s) {
  const p = planOf(s);
  if (!p.data) return '';
  const npd = newPerDay(s.id);
  const zOk = p.zRate && p.zDzis >= p.zRate;
  return `<section class="card plan-card">
    <a class="plan-top" href="#/plan" aria-label="Zmień plan">
      <div class="plan-days"><b>${p.dniDoMatury}</b><span>${plural(p.dniDoMatury, 'dzień', 'dni', 'dni')} do matury</span></div>
      <div class="plan-text"><strong>Plan na dziś</strong><small>koniec materiału: ${fmtShort(p.koniec)} · ok. ${p.minuty} min${p.rezerwa < POWTORKI_MIN && p.fresh ? ' · <b>za mało czasu na powtórki</b>' : ''}</small></div>
      <span class="plan-edit">${ICONS.next}</span>
    </a>
    <div class="plan-today">
      <a class="plan-chip" href="${(() => { const r = recommendedUnit(s); return r?.u ? `#/lekcja/${enc(s.id)}/p/${enc(r.u.id)}` : '#/nauka'; })()}"><b>${npd}</b><span>${plural(npd, 'nowa fiszka', 'nowe fiszki', 'nowych fiszek')} →</span></a>
      <a class="plan-chip ${zOk ? 'ok' : ''}" href="${nextTasksHref(s)}"><b>${p.zDzis}/${p.zRate}</b><span>zadania ${zOk ? '✓' : '→'}</span>
        <i style="width:${p.zRate ? Math.min(100, (p.zDzis / p.zRate) * 100) : 100}%"></i></a>
    </div>
  </section>`;
}

// ---------- prognoza wyniku matury ----------
// Szacunek celowo ostrożny: lepiej zaniżyć niż rozczarować. Składniki:
//  • wiedza w dziale — ile fiszek pamiętasz (szansa przypomnienia zależy od pudełka; zaległe i często mylone liczą się słabiej,
//    nieprzerobione = 0), albo wynik testów ABCD z przerobionych tematów;
//  • skuteczność w zadaniach maturalnych z działu (samoocena pomniejszona o 10%, przy małej liczbie zadań przyciągana do 50%);
//  • wagi działów = udział punktów działu w prawdziwych arkuszach CKE;
//  • próbne matury (do 60% wagi przy kilku rozwiązanych);
//  • prognoza na maj: Twoje faktyczne tempo z ostatnich 14 dni, a nie tempo z planu.
const PAMIEC = [0, 0.3, 0.45, 0.6, 0.78, 0.88, 0.94];
const PRIOR_ZADANIA = 0.5;
const A_CEL = 0.72; // skuteczność w zadaniach osiągalna przy regularnym ćwiczeniu arkuszy (ostrożnie, poniżej 3/4)

function wagiDzialow(s) {
  const w = {};
  const ids = new Set(s.dzialy.map((d) => d.id));
  for (const a of s.arkusze) for (const z of a.zadania) {
    const ds = z.dzialy.filter((d) => ids.has(d));
    ds.forEach((d) => (w[d] = (w[d] || 0) + z.punkty / ds.length));
  }
  const sum = Object.values(w).reduce((a, b) => a + b, 0);
  s.dzialy.forEach((d) => (w[d.id] = sum ? (w[d.id] || 0) / sum : 1 / s.dzialy.length));
  return w;
}

function prognoza(s, tempo) {
  const st = store.get();
  const now = Date.now();
  const wagi = wagiDzialow(s);
  const dzialy = [];
  let odpowiedzi = 0, nowe14 = 0;
  for (const d of s.dzialy) {
    let n = 0, pam = 0, fresh = 0, odpDz = 0;
    for (const u of d.poddzialy) for (const f of u.fiszki) {
      n++;
      const c = st.cards[cardKey(s.id, u.id, f.id)];
      if (!c || !c.reps) { fresh++; continue; }
      odpowiedzi += c.reps; odpDz += c.reps;
      if (c.first && now - c.first < 14 * DAY) nowe14++;
      let r = PAMIEC[Math.min(6, c.box || 0)];
      if (c.due && c.due < now - 3 * DAY) r *= 0.8;          // zaległa powtórka — część już się zatarła
      r /= 1 + 0.08 * (c.lapses || 0);                         // często mylona
      pam += r;
    }
    const K = n ? pam / n : 0;
    // testy ABCD z tematów działu
    let tOk = 0, tAll = 0;
    const tematy = new Set();
    for (const t of st.tests) {
      if (t.sid !== s.id) continue;
      const [typ, id] = String(t.scope).split(':');
      const uid = typ === 'p' && s.units.get(id)?.dzialId === d.id ? id : null;
      if (typ === 'd' && id === d.id) d.poddzialy.forEach((u) => tematy.add(u.id));
      else if (uid) tematy.add(uid);
      else continue;
      tOk += t.score; tAll += t.total;
    }
    const Ktest = tAll ? (tematy.size / Math.max(1, d.poddzialy.length)) * (tOk / tAll) * 0.8 : 0;
    // zadania maturalne z działu
    let zp = 0, zm = 0;
    const lista = [...tasksOf(s, d.id), ...bankTasks(s, d.id)];
    for (const z of lista) {
      const r = st.zadania[taskKey(s.id, z)];
      if (!r || !r.max) continue;
      const udzial = 1 / Math.max(1, (z.dzialy || []).length);
      zp += r.pkt * 0.9 * udzial; zm += r.max * udzial;
    }
    const A = (zp + PRIOR_ZADANIA * 8) / (zm + 8);
    // test diagnostyczny: wiedza „ze szkoły” w dziale, z poprawką na zgadywanie (25% w ABCD) i ostrożnym ściąganiem do 20%
    const dg = st.diagnoza?.[s.id]?.dz?.[d.id];
    const Kdiag = dg ? (Math.max(0, (dg[0] / dg[1] - 0.25) / 0.75) * dg[1] + 0.3) / (dg[1] + 1) : 0;
    const wiedza = Math.max(K, Ktest, Kdiag);
    // dział znany tylko z testu diagnostycznego: wynik ABCD (po odjęciu zgadywania) przekładamy wprost na punkty —
    // bez drugiego mnożenia przez nieznaną jeszcze skuteczność w zadaniach (podwójna kara)
    const tylkoDiag = dg && !odpDz && !tAll && !zm;
    const wynikDz = tylkoDiag ? 0.12 + 0.6 * Kdiag : wiedza * A;
    dzialy.push({ d, w: wagi[d.id], n, fresh, pam, K: wiedza, A, zm, wynik: wynikDz });
  }
  // dział „umiejętności” (źródła, chronologia) sprawdza wiedzę ze wszystkich epok — liczymy go z całego kursu
  const przekroj = (arr) => {
    const inne = arr.filter((x) => x.d.id !== 'umiejetnosci' && x.n);
    const sr = inne.reduce((a, x) => a + x.K * x.n, 0) / Math.max(1, inne.reduce((a, x) => a + x.n, 0));
    return arr.map((x) => (x.d.id === 'umiejetnosci' ? { ...x, K: 0.3 * x.K + 0.7 * sr, wynik: (0.3 * x.K + 0.7 * sr) * x.A } : x));
  };
  dzialy.splice(0, dzialy.length, ...przekroj(dzialy));
  const model = (arr) => arr.reduce((a, x) => a + x.w * x.wynik, 0);
  const dzis = model(dzialy);
  // próbne matury
  const proby = Object.values(st.egzaminy || {}).filter((e) => e.sid === s.id && e.koniec && e.ocena?.max).sort((a, b) => b.koniec - a.koniec).slice(0, 3);
  const M = proby.length ? proby.reduce((a, e) => a + e.ocena.pkt / e.ocena.max, 0) / proby.length * 0.95 : null;
  const wm = Math.min(0.6, 0.25 * proby.length);
  // prognoza na maj: obecne tempo (albo podane suwakiem), nowe fiszki dochodzą do działów w kolejności kursu
  const p = planOf(s);
  const dniDo = p.data ? Math.max(0, Math.round((Math.min(p.koniec, p.egz) - todayStart()) / DAY)) : 0;
  const tempoTeraz = Math.round(nowe14 / 14);
  // nowy uczeń nie ma jeszcze własnego tempa — wtedy liczymy tempem z planu
  const tempoBaza = Math.max(tempoTeraz, trybWlasny() ? 0 : p.rate || 0);
  let zapas = Math.round((tempo ?? tempoBaza) * dniDo);
  // Kto trzyma plan, robi też zadania maturalne — skuteczność w zadaniach rośnie proporcjonalnie do realizacji planu
  const realizacja = Math.min(1.2, (tempo ?? tempoBaza) / Math.max(1, p.rate || 30));
  const maj = dzialy.map((x) => {
    const ile = Math.min(x.fresh, zapas);
    zapas -= ile;
    const K = x.n ? Math.max(x.K, (x.pam + ile * 0.75) / x.n) : x.K;
    const A = x.A + (A_CEL - x.A) * Math.min(1, realizacja);
    return { ...x, K, A, wynik: Math.max(x.wynik, K * A) };
  });
  const majModel = model(przekroj(maj));
  const laczenie = (m) => (M == null ? m : (1 - wm) * m + wm * Math.min(M, m + 0.15));
  const punkt = laczenie(dzis);
  const punktMaj = laczenie(majModel) + (M == null ? 0 : wm * (majModel - dzis));
  // niepewność: im mniej danych, tym szerszy przedział; pokazujemy dolną połowę
  const diag = st.diagnoza?.[s.id];
  const dowody = odpowiedzi / 40 + dzialy.reduce((a, x) => a + x.zm, 0) / 4 + proby.length * 8 + st.tests.filter((t) => t.sid === s.id).length + (diag ? 2 : 0);
  const margines = Math.min(diag && odpowiedzi < 60 ? 0.12 : 0.25, Math.max(0.05, 0.04 + 0.22 / Math.sqrt(1 + dowody)));
  const szacunek = (x) => ({
    pokaz: Math.max(0, Math.floor((x - margines / 2) * 100)),
    od: Math.max(0, Math.floor((x - margines) * 100)),
    do: Math.min(95, Math.ceil((x + margines / 2) * 100)),
  });
  // ile punktów dałoby opanowanie działu (od stanu na dziś)
  const zysk = dzialy.map((x) => ({ d: x.d, pkt: x.w * (x.A * PAMIEC[6] - x.wynik) * 60 })).sort((a, b) => b.pkt - a.pkt).filter((x) => x.pkt >= 0.5).slice(0, 3);
  return {
    gotowa: odpowiedzi >= 60 || dzialy.some((x) => x.zm >= 5) || proby.length > 0 || !!diag,
    postepDanych: Math.min(1, Math.max(odpowiedzi / 60, dzialy.reduce((a, x) => a + x.zm, 0) / 5)),
    dzis: szacunek(punkt), maj: szacunek(punktMaj), dzialy, zysk, proby: proby.length,
    tempoTeraz, tempoBaza, zPlanu: !tempoTeraz && tempoBaza > 0, planTempo: p.rate || 0, dniDo, srednia: s.srednia,
  };
}

function prognozaCard(s) {
  const pr = prognoza(s);
  if (!pr.gotowa) {
    return `<a class="card prog-card" href="#/prognoza"><div class="prog-left"><span class="eyebrow">Prognoza matury</span>
      <strong>Sprawdź swój punkt startowy</strong><small>Test diagnostyczny: ok. 20 pytań, 4 minuty — od razu prognoza wyniku</small></div>${ICONS.next}</a>`.replace('href="#/prognoza"', 'href="#/diagnoza"');
  }
  return `<a class="card prog-card" href="#/prognoza">
    <div class="prog-left"><span class="eyebrow">Prognoza matury</span>
      <div class="prog-nums"><div><b>${pr.dzis.pokaz}%</b><small>gdyby matura była dziś</small></div><div><b>${pr.maj.pokaz}%</b><small>${pr.zPlanu ? 'w maju, jeśli trzymasz plan' : 'w maju przy Twoim tempie'}</small></div></div></div>
    ${ICONS.next}</a>`;
}

function viewPrognoza() {
  const s = currentSubject();
  if (!s) return notFound();
  const pr0 = prognoza(s);
  let tempo = pr0.tempoBaza;
  const render = () => {
    const pr = prognoza(s, tempo);
    const box = app.querySelector('.prog-body');
    if (!pr.gotowa) {
      box.innerHTML = `<section class="card"><h2 class="card-title">Potrzebujemy trochę więcej danych</h2>
        ${progressBar(pr.postepDanych, 'Dane do prognozy')}
        <p class="muted">Zrób krótki test diagnostyczny albo odpowiedz na 60 fiszek lub rozwiąż 5 zadań maturalnych — wtedy policzymy prognozę.</p>
        <div class="actions"><a class="btn btn-primary btn-lg" href="#/diagnoza">Test diagnostyczny — 4 min</a><a class="btn btn-ghost btn-lg" href="#/nauka">Do nauki</a></div></section>`;
      return;
    }
    const pas = (x) => `<div class="prog-range" aria-label="Zakres od ${x.od} do ${x.do}%"><i style="left:${x.od}%;width:${Math.max(1, x.do - x.od)}%"></i><b style="left:${x.pokaz}%"></b>${pr.srednia ? `<em style="left:${pr.srednia.procent}%" title="Średnia w kraju"></em>` : ''}</div>`;
    const hero = (q) => `
        <div class="prog-nums big">
          <div><b>${q.dzis.pokaz}%</b><small>gdyby matura była dziś</small></div>
          <div><b>${q.maj.pokaz}%</b><small>w maju · ok. ${Math.round(q.maj.pokaz * 0.6)} / 60 pkt</small></div>
        </div>
        ${pas(q.maj)}
        <p class="prog-scale"><span>prawdopodobnie ${q.maj.od}–${q.maj.do}%</span>${q.srednia ? `<span>średnia w kraju ${q.srednia.procent}% (${esc(q.srednia.rok)})</span>` : ''}</p>`;
    const zysk = (q) => q.zysk.length ? `<section class="card"><h2 class="card-title">Gdzie zyskasz najwięcej</h2>
        <div class="prog-zysk">${q.zysk.map((z) => `<a href="#/d/${enc(s.id)}/${enc(z.d.id)}"><span>${esc(z.d.nazwa)}</span><b>+${Math.floor(z.pkt)} pkt</b>${ICONS.next}</a>`).join('')}</div></section>` : '';
    box.innerHTML = `
      <section class="prog-hero">${hero(pr)}</section>
      <section class="card prog-tempo">
        <h2 class="card-title">A gdybyś robił więcej?</h2>
        <output class="prog-tempo-val"><b>${tempo}</b> nowych fiszek dziennie</output>
        <input type="range" id="pr-tempo" min="0" max="120" step="1" value="${tempo}" aria-label="Nowe fiszki dziennie">
        <p class="muted small">Zakładamy, że razem z fiszkami robisz zadania z planu — to one podnoszą wynik najbardziej.</p>
        <p class="prog-scale"><span>teraz: ${pr.tempoTeraz}/dzień</span><span>plan: ${pr.planTempo}/dzień</span></p>
      </section>
      <div class="prog-zysk-wrap">${zysk(pr)}</div>
      <section class="card"><h2 class="card-title">Działy</h2>
        <div class="prog-dz">${pr.dzialy.map((x) => `<div class="prog-dz-row"><span>${esc(x.d.nazwa)}</span><small>${Math.round(x.w * 60)} pkt na maturze · znasz ${pct(x.K)}% · zadania ${x.zm ? pct(x.A) + '%' : '—'}</small>
          <div class="core-mini"><i style="width:${x.wynik * 100}%"></i></div></div>`).join('')}</div>
      </section>
      <details class="card prog-how"><summary>Jak to liczymy</summary>
        <ul>
          <li>Wiedza: ile fiszek z działu pamiętasz — im wyższe pudełko, tym pewniej; zaległe powtórki i częste pomyłki obniżają wynik, nieprzerobione liczą się jako 0.</li>
          <li>Skuteczność: Twoje punkty z zadań maturalnych z działu (samoocenę pomniejszamy o 10%). Przy kilku zadaniach zakładamy 50%.</li>
          <li>Wagi działów jak w prawdziwych arkuszach CKE.${pr.proby ? ` Uwzględniamy też ${pr.proby} ${plural(pr.proby, 'próbną maturę', 'próbne matury', 'próbnych matur')}.` : ' Rozwiąż próbną maturę, a prognoza będzie dokładniejsza.'}</li>
          <li>Pokazujemy ostrożny szacunek — prawdziwy wynik częściej będzie wyższy niż niższy.</li>
        </ul></details>`;
    const r = box.querySelector('#pr-tempo');
    const upd = () => {
      r.style.setProperty('--v', `${(tempo / 120) * 100}%`);
      const q = prognoza(s, tempo);
      box.querySelector('.prog-hero').innerHTML = hero(q);
      box.querySelector('.prog-tempo-val b').textContent = tempo;
      box.querySelector('.prog-zysk-wrap').innerHTML = zysk(q);
    };
    r.addEventListener('input', () => { tempo = Number(r.value); upd(); });
    upd();
  };
  app.innerHTML = `${pageHead('Prognoza matury', '#/', s.nazwa)}<div class="prog-body"></div>`;
  render();
}

// ---------- tryb „na własną rękę” i własna powtórka ----------
// Uczeń bez planu sam wybiera, co i kiedy powtarza. Ekran #/powtorka jest dostępny w obu trybach.
const trybWlasny = () => store.get().settings.tryb === 'wlasny';
const RODZAJE = [
  { id: 'trudne', nazwa: 'Trudne', opis: 'mylone i słabo zapamiętane' },
  { id: 'dawno', nazwa: 'Dawno niepowtarzane', opis: 'najdłużej bez powtórki' },
  { id: 'losowo', nazwa: 'Losowo', opis: 'przemieszane z wybranych tematów' },
  { id: 'opanowane', nazwa: 'Odśwież opanowane', opis: 'szybki przegląd tego, co umiesz' },
  { id: 'zalegle', nazwa: 'Zaległe powtórki', opis: 'według harmonogramu' },
  { id: 'nowe', nazwa: 'Nowe fiszki', opis: 'jeszcze nieznane' },
];
const RODZAJE_SRS = new Set(['zalegle', 'nowe']); // te liczą się do harmonogramu; reszta to trening
const wlasnaSel = (s) => ({ rodzaj: 'trudne', ile: 20, tematy: [], ...(store.get().settings.wlasna?.[s.id] || {}) });

function pulaWlasna(sc, rodzaj) {
  const cards = store.get().cards;
  const end = store.endOfToday();
  const all = sc.units.flatMap((u) => u.fiszki.map((f) => ({ f, u, c: cards[cardKey(sc.s.id, u.id, f.id)] })));
  const seen = all.filter((x) => x.c?.reps);
  switch (rodzaj) {
    case 'trudne': return seen.filter((x) => x.c.lapses > 0 || x.c.box <= 2).sort((a, b) => a.c.box - b.c.box || b.c.lapses - a.c.lapses);
    case 'dawno': return seen.slice().sort((a, b) => (a.c.last || 0) - (b.c.last || 0));
    case 'losowo': return shuffle(seen.length ? seen : all);
    case 'opanowane': return shuffle(seen.filter((x) => x.c.box >= MASTERED_BOX));
    case 'zalegle': return seen.filter((x) => x.c.due <= end).sort((a, b) => a.c.due - b.c.due);
    case 'nowe': return all.filter((x) => !x.c?.reps);
    default: return [];
  }
}

function kolejkaWlasna(sc, rodzaj) {
  const ile = wlasnaSel(sc.s).ile || 20;
  return pulaWlasna(sc, rodzaj).slice(0, ile).map(({ f, u }) => ({ f, u }));
}

function wlasnaCard(s) {
  const p = planOf(s);
  const sel = wlasnaSel(s);
  const sc = resolveScope(s.id, 'w', sel.rodzaj);
  const ile = (r) => (sc ? pulaWlasna(sc, r).length : 0);
  return `<section class="card plan-card">
    <a class="plan-top" href="#/powtorka">
      ${p.data ? `<div class="plan-days"><b>${p.dniDoMatury}</b><span>${plural(p.dniDoMatury, 'dzień', 'dni', 'dni')} do matury</span></div>` : ''}
      <div class="plan-text"><strong>Twoja powtórka</strong><small>uczysz się na własną rękę · ${sel.tematy.length ? `${sel.tematy.length} ${plural(sel.tematy.length, 'temat', 'tematy', 'tematów')}` : 'cały kurs'}</small></div>
      <span class="plan-edit">${ICONS.next}</span>
    </a>
    <div class="quick-rev">${['trudne', 'dawno', 'zalegle', 'nowe'].map((r) => { const n = ile(r); const R = RODZAJE.find((x) => x.id === r);
      return `<button type="button" class="plan-chip ${n ? '' : 'off'}" data-szybko="${r}" ${n ? '' : 'disabled'}><b>${n}</b><span>${R.nazwa.toLowerCase()}</span></button>`; }).join('')}</div>
  </section>`;
}

function startWlasna(s, rodzaj, typ = 'fiszki') {
  const st = store.get().settings;
  st.wlasna = { ...(st.wlasna || {}), [s.id]: { ...wlasnaSel(s), rodzaj } };
  store.save();
  session = null; test = null;
  location.hash = typ === 'test' ? `#/test/${enc(s.id)}/w/test` : `#/fiszki/${enc(s.id)}/w/${rodzaj}`;
}

function viewPowtorka() {
  const s = currentSubject();
  if (!s) return notFound();
  const st = store.get().settings;
  const sel = wlasnaSel(s);
  const zapisz = () => { st.wlasna = { ...(st.wlasna || {}), [s.id]: sel }; store.save(); };
  const render = () => {
    const wyb = new Set(sel.tematy);
    const sc = resolveScope(s.id, 'w', sel.rodzaj);
    const pula = sc ? pulaWlasna(sc, sel.rodzaj).length : 0;
    const nQ = sc ? scopeQuestions(sc).length : 0;
    app.innerHTML = `
      ${pageHead('Własna powtórka', '#/', s.nazwa)}
      ${subjSwitch()}
      <section class="card">
        <h2 class="card-title">Co powtarzasz?</h2>
        <div class="rev-kinds">${RODZAJE.map((r) => { const n = sc ? pulaWlasna(sc, r.id).length : 0;
          return `<button type="button" class="rev-kind ${sel.rodzaj === r.id ? 'on' : ''}" data-rodzaj="${r.id}" aria-pressed="${sel.rodzaj === r.id}"><strong>${r.nazwa}</strong><small>${r.opis} · ${n}</small></button>`; }).join('')}</div>
      </section>
      <section class="card">
        <div class="rev-head"><h2 class="card-title">Z jakich tematów?</h2>
          <button type="button" class="link-btn" data-act="all">${wyb.size ? 'Cały kurs' : ''}</button></div>
        <div class="rev-dz">${s.dzialy.filter((d) => !d.zablokowany).map((d) => {
          const ids = d.poddzialy.map((u) => u.id);
          const ile = ids.filter((x) => wyb.has(x)).length;
          return `<details class="rev-group" ${ile && ile < ids.length ? 'open' : ''}>
            <summary><button type="button" class="rev-dzial ${ile === ids.length ? 'on' : ile ? 'part' : ''}" data-dzial="${esc(d.id)}">${esc(d.nazwa)}${ile ? `<small>${ile}/${ids.length}</small>` : ''}</button></summary>
            <div class="rev-units">${d.poddzialy.map((u) => `<button type="button" class="rev-unit ${wyb.has(u.id) ? 'on' : ''}" data-unit-sel="${esc(u.id)}">${esc(u.nazwa)}</button>`).join('')}</div>
          </details>`; }).join('')}</div>
        <p class="muted small">${wyb.size ? `Wybrane tematy: ${wyb.size}` : 'Nic nie wybrano — powtarzasz z całego kursu.'} Stuknij dział, aby zaznaczyć cały, albo rozwiń go strzałką.</p>
      </section>
      <section class="card">
        <h2 class="card-title">Ile fiszek?</h2>
        <div class="segmented seg-4">${[10, 20, 30, 50].map((v) => `<button type="button" data-ile="${v}" class="${sel.ile === v ? 'active' : ''}" aria-pressed="${sel.ile === v}">${v}</button>`).join('')}</div>
      </section>
      <div class="rev-start">
        <button type="button" class="btn btn-primary btn-lg" data-start="fiszki" ${pula ? '' : 'disabled'}>${ICONS.cards}<span>${pula ? `Fiszki · ${Math.min(pula, sel.ile)}` : 'Brak fiszek w tym wyborze'}</span></button>
        <button type="button" class="btn btn-ghost btn-lg" data-start="test" ${nQ ? '' : 'disabled'}>${ICONS.quiz}<span>Test z wybranych tematów</span></button>
      </div>
      <p class="muted small rev-info">${RODZAJE_SRS.has(sel.rodzaj) ? 'Te oceny trafiają do harmonogramu powtórek.' : 'Trening nie zmienia harmonogramu powtórek — możesz powtarzać do woli.'}</p>
      <section class="card rev-mode">
        <h2 class="card-title">Tryb nauki</h2>
        <div class="segmented" style="grid-template-columns:1fr 1fr">
          <button type="button" data-tryb="plan" class="${trybWlasny() ? '' : 'active'}">Z planem</button>
          <button type="button" data-tryb="wlasny" class="${trybWlasny() ? 'active' : ''}">Na własną rękę</button>
        </div>
        <p class="muted small">${trybWlasny() ? 'Na ekranie Dziś zamiast planu widzisz szybkie powtórki. Nowych fiszek dziennie: ' + (Number(st.newPerDay) || 20) + ' (zmienisz w Ustawieniach).' : 'Plan dobiera dzienne porcje do daty matury. Własną powtórkę możesz robić zawsze.'}</p>
      </section>`;
    bindSubjSwitch(viewPowtorka);
    app.querySelectorAll('[data-rodzaj]').forEach((b) => b.addEventListener('click', () => { sel.rodzaj = b.dataset.rodzaj; zapisz(); game.sound('tap'); render(); }));
    app.querySelectorAll('[data-ile]').forEach((b) => b.addEventListener('click', () => { sel.ile = Number(b.dataset.ile); zapisz(); render(); }));
    app.querySelector('[data-act="all"]')?.addEventListener('click', () => { sel.tematy = []; zapisz(); render(); });
    app.querySelectorAll('[data-dzial]').forEach((b) => b.addEventListener('click', (e) => {
      e.preventDefault();
      const ids = findDzial(s, b.dataset.dzial).poddzialy.map((u) => u.id);
      const wszystkie = ids.every((x) => wyb.has(x));
      sel.tematy = wszystkie ? sel.tematy.filter((x) => !ids.includes(x)) : [...new Set([...sel.tematy, ...ids])];
      zapisz(); game.sound('tap'); render();
    }));
    app.querySelectorAll('[data-unit-sel]').forEach((b) => b.addEventListener('click', () => {
      const id = b.dataset.unitSel;
      sel.tematy = wyb.has(id) ? sel.tematy.filter((x) => x !== id) : [...sel.tematy, id];
      zapisz(); render();
    }));
    app.querySelectorAll('[data-start]').forEach((b) => b.addEventListener('click', () => startWlasna(s, sel.rodzaj, b.dataset.start)));
    app.querySelectorAll('[data-tryb]').forEach((b) => b.addEventListener('click', () => ustawTryb(b.dataset.tryb, render)));
  };
  render();
}

function ustawTryb(tryb, po) {
  const st = store.get().settings;
  if ((st.tryb || 'plan') === tryb) return;
  st.tryb = tryb;
  store.save();
  refreshAutoRates();
  game.sound('tap');
  toast(tryb === 'wlasny' ? 'Uczysz się na własną rękę — plan wyłączony, powtórki wybierasz samodzielnie.' : 'Plan nauki znów jest włączony.');
  po?.();
}

function viewPlan() {
  const s = currentSubject();
  if (!s) return notFound();
  const settings = store.get().settings;
  const first = !settings.plan?.[s.id];
  const draft = { ...(settings.plan?.[s.id] || {}) };
  delete draft.pominiety;
  draft.data ||= s.egzamin || isoDay(todayStart() + 180 * DAY);
  const p0 = planOf(s, draft);
  draft.koniec ||= isoDay(p0.koniec);
  app.innerHTML = `
    ${pageHead('Plan nauki', first ? null : '#/', s.nazwa)}
    <section class="card plan-slider">
      <p class="eyebrow">Kończę materiał</p>
      <output class="plan-date" id="pl-date"></output>
      <div class="plan-track">
        <input type="range" id="pl-range" min="1" step="1" aria-label="Dzień końca nauki nowego materiału">
        <div class="plan-marks" aria-hidden="true"><i id="pl-m6"><span>zalecany koniec</span></i></div>
      </div>
      <div class="plan-scale"><span>jutro</span><span id="pl-egz"></span></div>
      <div class="plan-bar" aria-hidden="true"><i id="pl-learn"></i><i id="pl-rez" class="rez"></i></div>
      <p class="plan-legend"><span><i></i>nowy materiał · <b id="pl-dni"></b></span><span><i class="rez"></i>powtórki i arkusze · <b id="pl-rezn"></b></span></p>
      <p class="plan-status" id="pl-status"></p>
    </section>
    <div class="plan-tiles" aria-live="polite">
      <div class="plan-tile"><b id="pl-f"></b><span>fiszek dziennie</span></div>
      <div class="plan-tile"><b id="pl-z"></b><span>zadań dziennie</span></div>
      <div class="plan-tile" id="pl-mt"><b id="pl-m"></b><span>minut dziennie</span></div>
    </div>
    <details class="card plan-exam"><summary>Matura: <b id="pl-ed"></b></summary>
      <input class="type-input" type="date" id="plan-data" value="${esc(draft.data)}" min="${isoDay(todayStart() + 2 * DAY)}" aria-label="Data matury">
    </details>
    <button type="button" class="btn btn-primary btn-lg" data-act="save">${first ? 'Zaczynam' : 'Zapisz plan'}</button>
    <div class="plan-more">
      <button type="button" class="btn btn-ghost" data-act="zalecany">${ICONS.redo}<span>Zalecany plan</span></button>
      ${first ? '' : `<button type="button" class="btn btn-ghost" data-act="reset">${ICONS.close}<span>Resetuj plan</span></button>`}
    </div>`;
  const range = app.querySelector('#pl-range');
  const $ = (id) => app.querySelector(id);
  const sync = (fromRange) => {
    const today = todayStart();
    const egz = parseDay(draft.data);
    const max = Math.max(1, Math.round((egz - today) / DAY));
    range.max = max;
    if (fromRange) draft.koniec = isoDay(today + Number(range.value) * DAY);
    const p = planOf(s, draft);
    range.value = p.dni;
    range.style.setProperty('--v', `${(p.dni / max) * 100}%`);
    $('#pl-date').textContent = fmtDay(p.koniec);
    $('#pl-egz').textContent = `matura ${fmtShort(egz)}`;
    $('#pl-ed').textContent = fmtDay(egz);
    $('#pl-learn').style.width = `${(p.dni / max) * 100}%`;
    $('#pl-rez').style.width = `${100 - (p.dni / max) * 100}%`;
    $('#pl-dni').textContent = `${p.dni} ${plural(p.dni, 'dzień', 'dni', 'dni')}`;
    $('#pl-rezn').textContent = `${p.rezerwa} ${plural(p.rezerwa, 'dzień', 'dni', 'dni')}`;
    const mark = (el, d) => { el.style.left = `${((max - d) / max) * 100}%`; el.hidden = d >= max; };
    mark($('#pl-m6'), POWTORKI_ZALECANE);
    const st = $('#pl-status');
    st.className = `plan-status ${p.rezerwa >= POWTORKI_ZALECANE ? 'ok' : p.rezerwa >= POWTORKI_MIN ? 'mid' : 'bad'}`;
    st.textContent = p.rezerwa >= POWTORKI_ZALECANE ? '✓ Zalecane: co najmniej 6 tygodni na powtórki i arkusze'
      : p.rezerwa >= POWTORKI_MIN ? 'Minimum — lepiej zostawić 6 tygodni na powtórki'
      : 'Za mało na utrwalenie — ostatnie fiszki potrzebują ok. 4 tygodni powtórek';
    $('#pl-f').textContent = p.rate;
    $('#pl-z').textContent = p.zRate;
    $('#pl-m').textContent = p.minuty;
    $('#pl-mt').classList.toggle('warn', p.minuty > 90);
  };
  range.addEventListener('input', () => sync(true));
  $('[data-act="zalecany"]').addEventListener('click', () => {
    draft.data = s.egzamin || draft.data;
    draft.koniec = isoDay(planOf(s, { data: draft.data, koniec: null }).koniec);
    $('#plan-data').value = draft.data;
    game.sound('tap');
    sync(false);
    toast('Zalecany plan: 6 tygodni przed maturą na powtórki i arkusze. Zapisz, aby zatwierdzić.');
  });
  $('[data-act="reset"]')?.addEventListener('click', () => {
    const stary = settings.plan[s.id];
    delete settings.plan[s.id];
    store.save();
    refreshAutoRates();
    viewPlan();
    toast('Plan zresetowany — ułóż go od nowa.', { label: 'Cofnij', run: () => { settings.plan[s.id] = stary; store.save(); refreshAutoRates(); viewPlan(); } });
  });
  $('#plan-data').addEventListener('change', (e) => { if (e.target.value) { draft.data = e.target.value; sync(false); } });
  $('[data-act="save"]').addEventListener('click', () => {
    settings.plan = { ...(settings.plan || {}), [s.id]: { data: draft.data, koniec: draft.koniec } };
    settings.tempo = 'auto';
    settings.tryb = 'plan';
    store.save();
    refreshAutoRates();
    game.sound('ok');
    location.hash = first && !store.get().diagnoza?.[s.id] ? '#/diagnoza' : '#/';
  });
  sync(false);
}

function viewHome() {
  refreshAutoRates();
  const showInstall = installEvent && !store.get().settings.installDismissed;
  const s = currentSubject();
  const rec = s ? recommendedUnit(s) : null;
  const nb = s ? mistakesOf(s).length : 0;
  let todo = 0, best = null;
  if (s) {
    // limit nowych fiszek dotyczy całego przedmiotu — liczymy go raz, nie osobno w każdym dziale
    const allowance = newAllowance(s.id);
    todo = summary(s.id, allUnits(s), allowance).todo;
    s.dzialy.forEach((dz) => {
      const k = summary(s.id, dz.poddzialy, 0).due;
      if (k && (!best || k > best.n)) best = { d: dz, n: k };
    });
    if (!best && todo && rec) best = { d: rec.d, n: todo };
  }
  app.innerHTML = `
    <header class="today-head"><h1>Dziś</h1></header>
    ${subjSwitch()}
    ${s ? coreCard(s) : ''}
    ${s ? (trybWlasny() ? wlasnaCard(s) : planCard(s)) : ''}
    ${s ? prognozaCard(s) : ''}
    ${premiumCard()}
    ${s ? goalCard(s, rec, todo) : ''}
    ${showInstall ? `<div class="install-banner">
        <div><strong>Zainstaluj IndexLab</strong><span>Ikona na ekranie głównym i nauka bez internetu.</span></div>
        <div class="install-actions">
          <button type="button" class="btn btn-gold btn-sm" data-act="install">Zainstaluj</button>
          <button type="button" class="icon-btn" data-act="dismiss" aria-label="Nie teraz">${ICONS.close}</button>
        </div></div>` : ''}
    ${loadErrors.length ? `<div class="alert">Nie udało się wczytać: ${esc(loadErrors.join('; '))}</div>` : ''}
    ${nb ? `<a class="card mistakes-card" href="#/bledy/${enc(s.id)}">
      <span class="quest-icon">${ICONS.redo}</span>
      <span class="mistakes-text"><strong>Błędy do poprawy: ${nb}</strong><small>Lekcja z pytań, w których była pomyłka</small></span>
      ${ICONS.next}</a>` : ''}
    ${s ? planHtml(s, rec, todo, best) : ''}
    ${s ? '' : '<p class="muted">Brak przedmiotów.</p>'}
  `;
  bindSubjSwitch(viewHome);
  app.querySelectorAll('[data-szybko]').forEach((b) => b.addEventListener('click', () => startWlasna(s, b.dataset.szybko)));
  app.querySelector('[data-act="rebrand-ok"]')?.addEventListener('click', () => {
    store.get().settings.rebrandSeen = true;
    store.save();
    viewHome();
  });
  app.querySelector('[data-act="install"]')?.addEventListener('click', promptInstall);
  app.querySelector('[data-act="dismiss"]')?.addEventListener('click', () => {
    store.get().settings.installDismissed = true;
    store.save();
    viewHome();
  });
}

// ---------- przełącznik kursów (widoczny na Dziś i w Nauce) ----------
let wrocPoWyborze = null; // gdzie wrócić po zmianie kursu
function subjSwitch() {
  if (subjects.length < 2) return '';
  const cur = currentSubject();
  return `<a class="course-pill" href="#/przedmiot" data-course-pill>
    <span class="course-pill-icon">${subjectIcon(cur)}</span>
    <span class="course-pill-text"><small>Twój kurs</small><b>${esc(cur.nazwa)}</b></span>
    <span class="course-pill-change">Zmień</span></a>`;
}
function bindSubjSwitch() {
  app.querySelector('[data-course-pill]')?.addEventListener('click', () => { wrocPoWyborze = location.hash || '#/'; });
}

// ---------- zakładka „Nauka” ----------
function viewNauka() {
  const s = currentSubject();
  if (!s) return notFound();
  const rec = recommendedUnit(s);
  const allowance = newAllowance(s.id);
  const sm = summary(s.id, allUnits(s), allowance);
  let best = null;
  s.dzialy.forEach((d) => { const k = summary(s.id, d.poddzialy, allowance).due; if (k && (!best || k > best.n)) best = { d, n: k }; });
  const st = store.get().zadania;
  const zad = allTasks(s);
  const zDone = zad.filter((z) => st[taskKey(s.id, z)]).length;
  const u = rec?.u;
  const usm = u ? summary(s.id, [u], allowance) : null;
  app.innerHTML = `
    <header class="today-head">
      <h1>Nauka</h1>
      <a class="icon-btn" href="#/szukaj" aria-label="Szukaj pojęć">${ICONS.search}</a>
    </header>
    ${subjSwitch()}
    ${u ? `<section class="nauka-hero">
      <span class="eyebrow">${esc(rec.d.nazwa)}</span>
      <h2>${esc(u.nazwa)}</h2>
      <div class="core-bar" role="img" aria-label="Opanowanie ${pct(usm.progress)}%"><i style="width:${usm.progress * 100}%"></i></div>
      <div class="hero-actions">
        <a class="btn hero-main" href="#/lekcja/${enc(s.id)}/p/${enc(u.id)}">${ICONS.play}<span>Lekcja</span></a>
        ${u.fiszki.length ? `<a class="btn hero-sec" href="#/fiszki/${enc(s.id)}/p/${enc(u.id)}" aria-label="Fiszki">${ICONS.cards}<span>${usm.todo || ''}</span></a>` : ''}
        ${u.pytania.length ? `<a class="btn hero-sec" href="#/test/${enc(s.id)}/p/${enc(u.id)}" aria-label="Test">${ICONS.quiz}</a>` : ''}
      </div>
    </section>` : ''}
    <div class="plan-tiles nauka-tiles">
      <a class="plan-tile" href="#/statystyki"><b>${pct(sm.progress)}%</b><span>opanowane</span></a>
      <a class="plan-tile ${best ? '' : 'off'}" href="${best ? `#/fiszki/${enc(s.id)}/d/${enc(best.d.id)}` : '#/nauka'}"><b>${sm.due}</b><span>do powtórki</span></a>
      <a class="plan-tile" href="${nextTasksHref(s)}"><b>${zDone}<small>/${zad.length}</small></b><span>zadań</span></a>
    </div>
    <a class="card rev-link" href="#/powtorka"><span class="quest-icon">${ICONS.redo}</span><span class="plan-text"><strong>Własna powtórka</strong><small>Wybierz tematy i powtarzaj, co chcesz</small></span>${ICONS.next}</a>
    <div class="route" data-sid="${esc(s.id)}">${pathHtml(s, rec)}</div>`;
  bindSubjSwitch(viewNauka);
  const wrap = app.querySelector('.route');
  wrap.addEventListener('click', (e) => {
    const b = e.target.closest('.stop-body[data-unit]');
    if (!b) return;
    const un = s.units.get(b.dataset.unit);
    const pop = wrap.querySelector(`[data-pop="${CSS.escape(un.id)}"]`);
    const open = !pop.hidden;
    wrap.querySelectorAll('.stop-pop').forEach((p) => (p.hidden = true));
    wrap.querySelectorAll('.stop-body').forEach((x) => x.setAttribute('aria-expanded', 'false'));
    if (!open) { pop.innerHTML = popHtml(s, un); pop.hidden = false; b.setAttribute('aria-expanded', 'true'); game.sound('tap'); }
  });
}


// ---------- pasek u góry: seria i XP ----------
function updateTopStats() {
  const sb = document.getElementById('subj-btn');
  const cs = subjects.length ? currentSubject() : null;
  if (sb) sb.innerHTML = `${BRAND_MARK}${cs ? `<span class="subj-btn-name">${esc(cs.skrot || cs.nazwa)}</span>` : ''}`;
  const newsTab = document.querySelector('.tabbar [data-tab="news"]');
  if (newsTab) {
    newsTab.hidden = !cs?.aktualnosci; // zakładka tylko dla przedmiotów z modułem aktualności
    const lbl = newsTab.querySelector('span');
    if (lbl) lbl.textContent = cs?.aktualnosci?.zakladka || 'Aktualności';
  }
  const el = document.getElementById('top-stats');
  if (!el) return;
  const st = store.streak();
  el.innerHTML = `<a class="top-chip chip-flame ${st.today ? 'on' : ''}" href="#/profil" aria-label="Seria: ${st.current} ${plural(st.current, 'dzień', 'dni', 'dni')} nauki">${ICONS.flame}<span>${st.current}</span></a>`;
}

function onGameEvents(events) {
  updateTopStats();
}

// ---------- lekcja: mieszane ćwiczenia ----------
const LESSON_SIZE = 12;
const MAX_HEARTS = 5;
const PRAISE = ['Dobrze!', 'Świetnie!', 'Tak!', 'Zgadza się!'];
let lesson = null;

const P_DEF = 'Wyjaśnij pojęcie: ';
const P_TERM = 'Podaj nazwę pojęcia: ';
const kindOf = (f) => (f.przod.startsWith(P_DEF) ? 'def' : f.przod.startsWith(P_TERM) ? 'term' : 'q');
const promptOf = (f) => (kindOf(f) === 'term' ? f.przod.slice(P_TERM.length) : kindOf(f) === 'def' ? termOf(f) : f.przod);
const termOf = (f) => (kindOf(f) === 'def' ? f.przod.slice(P_DEF.length) : kindOf(f) === 'term' ? f.tyl : f.przod);

function norm(s) {
  return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/ł/g, 'l')
    .replace(/[„”"'’.,;:!?()[\]–—-]/g, ' ').replace(/\s+/g, ' ').trim();
}
function lev(a, b) {
  if (Math.abs(a.length - b.length) > 2) return 9;
  const m = Array.from({ length: a.length + 1 }, (_, i) => [i]);
  for (let j = 1; j <= b.length; j++) m[0][j] = j;
  for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++)
    m[i][j] = Math.min(m[i - 1][j] + 1, m[i][j - 1] + 1, m[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
  return m[a.length][b.length];
}
function acceptedAnswers(ans) {
  const out = new Set([norm(ans)]);
  const noPar = ans.replace(/\([^)]*\)/g, '');
  out.add(norm(noPar));
  (ans.match(/\(([^)]*)\)/g) || []).forEach((p) => out.add(norm(p.slice(1, -1))));
  noPar.split(/\s*(?:\/|;| lub | albo )\s*/).forEach((p) => p.trim() && out.add(norm(p)));
  out.delete('');
  return [...out];
}
function checkTyped(input, ans) {
  const v = norm(input);
  if (!v) return 'bad';
  const acc = acceptedAnswers(ans);
  if (acc.includes(v)) return 'ok';
  if (acc.some((a) => a.length > 5 && lev(v, a) <= (a.length > 12 ? 2 : 1))) return 'typo';
  return 'bad';
}

function pickDistractors(pool, item, n, val) {
  const seen = new Set([norm(val(item))]);
  const out = [];
  for (const x of shuffle(pool)) {
    const v = val(x);
    if (x === item || seen.has(norm(v))) continue;
    seen.add(norm(v)); out.push(x);
    if (out.length >= n) break;
  }
  return out;
}

function buildLesson(sc) {
  const own = sc.units.flatMap((u) => u.fiszki.map((f) => ({ f, u })));
  const wide = (sc.dzial ? sc.dzial.poddzialy : sc.units).flatMap((u) => u.fiszki.map((f) => ({ f, u })));
  const qs = shuffle(scopeQuestions(sc));
  const sameKind = (it) => (x) => kindOf(x.f) === kindOf(it.f);
  const poolFor = (it, min) => { const p = own.filter(sameKind(it)); return p.length > min ? p : wide.filter(sameKind(it)); };
  const ex = [];
  const used = new Set();
  const take = (filter) => { const it = shuffle(own).find((x) => !used.has(x.f) && filter(x)); if (it) used.add(it.f); return it; };

  qs.slice(0, 3).forEach(({ q, u }) => ex.push({ type: 'abcd', u, q, order: shuffle(q.odpowiedzi.map((_, i) => i)) }));
  // dopasuj pary
  const pairs = shuffle(own.filter((x) => kindOf(x.f) === 'def' && termOf(x.f).length <= 48 && x.f.tyl.length <= 110));
  const pick = [];
  const pn = new Set();
  for (const x of pairs) { const k = norm(termOf(x.f)); if (!pn.has(k)) { pn.add(k); pick.push(x); } if (pick.length === 4) break; }
  if (pick.length === 4) { pick.forEach((x) => used.add(x.f)); ex.push({ type: 'match', u: pick[0].u, items: pick, right: shuffle(pick.map((_, i) => i)) }); }
  // wpisywanie
  for (let i = 0; i < 2; i++) {
    const it = take((x) => (kindOf(x.f) === 'term' || kindOf(x.f) === 'q') && x.f.tyl.length <= 28 && !/\d{3,}/.test(x.f.tyl));
    if (it) ex.push({ type: 'type', u: it.u, f: it.f });
  }
  // prawda / fałsz
  for (let i = 0; i < 2; i++) {
    const it = take((x) => kindOf(x.f) !== 'term' && x.f.tyl.length <= 220);
    if (!it) break;
    const truth = Math.random() < 0.5;
    const other = truth ? null : pickDistractors(poolFor(it, 1), it, 1, (x) => x.f.tyl)[0];
    ex.push({ type: 'tf', u: it.u, f: it.f, shown: other ? other.f.tyl : it.f.tyl, truth: !other });
  }
  // wybór odpowiedzi
  while (ex.length < LESSON_SIZE) {
    const it = take((x) => x.f.tyl.length <= 200);
    if (!it) break;
    const d = pickDistractors(poolFor(it, 3), it, 3, (x) => x.f.tyl);
    if (d.length < 2) continue;
    const opts = shuffle([it, ...d]);
    ex.push({ type: 'choose', u: it.u, f: it.f, opts: opts.map((x) => x.f.tyl), good: opts.indexOf(it) });
  }
  const match = ex.filter((e) => e.type === 'match');
  const rest = shuffle(ex.filter((e) => e.type !== 'match'));
  rest.splice(Math.min(4, rest.length), 0, ...match);
  return rest.slice(0, LESSON_SIZE);
}


// ---------- błędy do poprawy ----------
const mistakeKey = (sid, uid, id) => `${sid}/${uid}/${id}`;
function addMistake(sid, u, item, t) {
  const st = store.get();
  st.bledy ||= {};
  const k = mistakeKey(sid, u.id, item.id);
  const m = st.bledy[k] || { t, uid: u.id, id: item.id, n: 0 };
  m.n++; m.at = Date.now();
  st.bledy[k] = m;
}
function clearMistake(sid, uid, id) {
  const st = store.get();
  if (st.bledy) delete st.bledy[mistakeKey(sid, uid, id)];
}
function mistakesOf(s) {
  const st = store.get().bledy || {};
  return Object.entries(st).filter(([k]) => k.startsWith(s.id + '/')).map(([k, m]) => {
    const u = s.units.get(m.uid);
    if (!u) return null;
    const item = m.t === 'q' ? u.pytania.find((q) => q.id === m.id) : u.fiszki.find((f) => f.id === m.id);
    return item ? { k, m, u, item } : null;
  }).filter(Boolean).sort((a, b) => a.m.at - b.m.at);
}
function buildMistakeLesson(s) {
  const ex = [];
  for (const { u, item, m } of mistakesOf(s).slice(0, LESSON_SIZE)) {
    if (m.t === 'q') { ex.push({ type: 'abcd', u, q: item, order: shuffle(item.odpowiedzi.map((_, i) => i)), blad: true }); continue; }
    const it = { f: item, u };
    const pool = u.fiszki.filter((f) => f !== item && kindOf(f) === kindOf(item)).map((f) => ({ f, u }));
    const wide = pool.length >= 3 ? pool : (dzialOf(s, u)?.poddzialy || [u]).flatMap((x) => x.fiszki.filter((f) => f !== item && kindOf(f) === kindOf(item)).map((f) => ({ f, u: x })));
    const d = pickDistractors(wide, it, 3, (x) => x.f.tyl);
    if (d.length >= 2) {
      const opts = shuffle([it, ...d]);
      ex.push({ type: 'choose', u, f: item, opts: opts.map((x) => x.f.tyl), good: opts.indexOf(it), blad: true });
    } else ex.push({ type: 'tf', u, f: item, shown: item.tyl, truth: true, blad: true });
  }
  return ex;
}
function viewBledy(sid) {
  const s = findSubject(sid);
  if (!s) return notFound();
  const key = `${sid}/b/bledy`;
  if (!lesson || lesson.key !== key) {
    const queue = buildMistakeLesson(s);
    if (!queue.length) {
      app.innerHTML = `${pageHead('Błędy do poprawy', '#/')}<div class="empty"><div class="empty-icon">${ICONS.check}</div><h1>Brak błędów</h1><p>Pomyłki z lekcji i testów pojawią się tutaj do powtórki.</p><a class="btn btn-primary" href="#/">Wróć</a></div>`;
      return;
    }
    const sc = { s, type: 'b', id: 'bledy', units: [], title: 'Błędy do poprawy', back: '#/' };
    lesson = { key, sc, queue, total: queue.length, done: 0, correct: 0, wrong: 0, start: Date.now(), state: 'ask', sel: null, finished: false };
  }
  renderExercise();
}

// ---------- wyszukiwarka pojęć ----------
let searchQ = '';
function viewSzukaj() {
  app.innerHTML = `${pageHead('Szukaj', null)}
    <input class="type-input search-input" id="q" type="search" autocomplete="off" placeholder="np. kontrasygnata, art. 104, NATO…" aria-label="Szukaj w fiszkach" value="${esc(searchQ)}">
    <p class="muted small" id="q-info"></p>
    <div class="review-list" id="q-res"></div>`;
  const inp = app.querySelector('#q');
  const run = () => {
    searchQ = inp.value;
    const q = norm(searchQ);
    const res = app.querySelector('#q-res');
    const info = app.querySelector('#q-info');
    if (q.length < 2) { res.innerHTML = ''; info.textContent = 'Wpisz co najmniej 2 znaki. Przeszukiwane są wszystkie fiszki i pytania.'; return; }
    const words = q.split(' ');
    const hits = [];
    for (const s of subjects) for (const u of allUnits(s)) {
      for (const f of u.fiszki) {
        const a = norm(f.przod), b = norm(f.tyl);
        if (words.every((w) => a.includes(w) || b.includes(w))) hits.push({ s, u, f, score: (a.includes(q) ? 0 : 1) + (kindOf(f) === 'term' ? 2 : 0) });
      }
    }
    hits.sort((x, y) => x.score - y.score);
    info.textContent = hits.length ? `Znaleziono: ${hits.length}${hits.length > 60 ? ' (pokazuję 60)' : ''}` : 'Nic nie znaleziono.';
    res.innerHTML = hits.slice(0, 60).map(({ s, u, f }) => `<article class="card review">
      <h3>${esc(f.przod)}</h3><p>${esc(f.tyl)}</p>
      <div class="review-foot">${sourceTag(f.zrodlo) || '<span></span>'}<a class="btn-report" href="${hrefUnit(s.id, u.id)}">${ICONS.book}<span>${esc(u.nazwa)}</span></a></div>
    </article>`).join('');
  };
  let t;
  inp.addEventListener('input', () => { clearTimeout(t); t = setTimeout(run, 120); });
  run();
  setTimeout(() => inp.focus(), 50);
}

function viewLekcja(sid, type, id) {
  const sc = resolveScope(sid, type, id);
  if (!sc) return notFound();
  const key = lessonKey(sid, type, id);
  if (!lesson || lesson.key !== key) {
    const queue = buildLesson(sc);
    if (!queue.length) return notFound();
    lesson = { key, sc, queue, total: queue.length, done: 0, correct: 0, wrong: 0, start: Date.now(), retried: new Set(), state: 'ask', sel: null, finished: false };
  }
  renderExercise();
}

function lessonTop() {
  const L = lesson;
  return `<div class="session-top lesson-top">
      <a class="icon-btn" href="#/" aria-label="Zakończ lekcję">${ICONS.close}</a>
      <div class="session-progress">${progressBar(L.done / L.total, 'Postęp lekcji')}</div>
      <span class="session-count">${Math.min(L.done + 1, L.total)}/${L.total}</span>
    </div>`;
}

function renderExercise() {
  const L = lesson;
  document.body.classList.add('in-session', 'in-lesson');
  if (L.finished || !L.queue.length) return renderLessonEnd();
  const e = L.queue[0];
  L.state = 'ask'; L.sel = null;
  let body = '';
  if (e.type === 'abcd' || e.type === 'choose') {
    const prompt = e.type === 'abcd' ? e.q.pytanie : promptOf(e.f);
    const opts = e.type === 'abcd' ? e.order.map((oi) => e.q.odpowiedzi[oi]) : e.opts;
    body = `<p class="ex-kind">${e.type === 'abcd' ? 'Wybierz poprawną odpowiedź' : kindOf(e.f) === 'term' ? 'Jak nazywa się to pojęcie?' : kindOf(e.f) === 'def' ? 'Co oznacza to pojęcie?' : 'Wybierz właściwą odpowiedź'}</p>
      <h2 class="ex-prompt">${esc(prompt)}</h2>
      <div class="options" role="group" aria-label="Odpowiedzi">${opts.map((o, i) => `<button type="button" class="option" data-i="${i}"><span class="option-letter">${i + 1}</span><span class="option-text">${esc(o)}</span></button>`).join('')}</div>`;
  } else if (e.type === 'tf') {
    body = `<p class="ex-kind">Prawda czy fałsz?</p>
      <h2 class="ex-prompt">${kindOf(e.f) === 'def' ? `Czy to znaczenie pojęcia „${esc(termOf(e.f))}”?` : esc(e.f.przod)}</h2>
      <div class="tf-claim"><span>Odpowiedź:</span> ${esc(e.shown)}</div>
      <div class="tf-row" role="group" aria-label="Prawda czy fałsz"><button type="button" class="option tf" data-i="1">${ICONS.check}<span>Prawda</span></button><button type="button" class="option tf" data-i="0">${ICONS.close}<span>Fałsz</span></button></div>`;
  } else if (e.type === 'type') {
    body = `<p class="ex-kind">${kindOf(e.f) === 'term' ? 'Wpisz nazwę pojęcia' : 'Wpisz odpowiedź'}</p>
      <h2 class="ex-prompt">${esc(promptOf(e.f))}</h2>
      <input class="type-input" id="typed" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Twoja odpowiedź…" aria-label="Twoja odpowiedź">
      <p class="muted small">Wielkość liter i polskie znaki nie mają znaczenia.</p>`;
  } else if (e.type === 'match') {
    body = `<p class="ex-kind">Dopasuj pary</p>
      <h2 class="ex-prompt">Połącz pojęcie z jego znaczeniem</h2>
      <div class="match">
        <div class="match-col">${e.items.map((x, i) => `<button type="button" class="match-item" data-side="l" data-i="${i}">${esc(termOf(x.f))}</button>`).join('')}</div>
        <div class="match-col">${e.right.map((i) => `<button type="button" class="match-item" data-side="r" data-i="${i}">${esc(e.items[i].f.tyl)}</button>`).join('')}</div>
      </div>`;
  }
  app.innerHTML = `${lessonTop()}<section class="exercise" data-type="${e.type}">${body}</section>
    <div class="lesson-bar" id="bar">${e.type === 'match' ? '<p class="muted center">Dotknij pojęcia, a potem jego znaczenia.</p>' : '<button type="button" class="btn btn-primary btn-lg btn-cta" id="check" disabled>Sprawdź</button>'}</div>`;

  const check = app.querySelector('#check');
  if (e.type === 'type') {
    const inp = app.querySelector('#typed');
    inp.addEventListener('input', () => (check.disabled = !inp.value.trim()));
    inp.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' && inp.value.trim() && L.state === 'ask') { ev.preventDefault(); evaluate(); } });
    setTimeout(() => inp.focus(), 50);
  } else if (e.type !== 'match') {
    app.querySelector('.exercise').addEventListener('click', (ev) => {
      const b = ev.target.closest('.option');
      if (!b || L.state !== 'ask') return;
      app.querySelectorAll('.option').forEach((o) => o.classList.toggle('selected', o === b));
      L.sel = Number(b.dataset.i);
      check.disabled = false;
      game.sound('tap');
    });
  } else bindMatch(e);
  check?.addEventListener('click', evaluate);
  keyHandler = (ev) => {
    if (L.state === 'ask' && e.type !== 'type' && e.type !== 'match') {
      const n = Number(ev.key);
      const opts = app.querySelectorAll('.option');
      if (n >= 1 && n <= opts.length) { opts[n - 1].click(); return; }
      if (ev.key === 'Enter' && L.sel !== null) { ev.preventDefault(); evaluate(); }
    } else if (L.state === 'fb' && ev.key === 'Enter') { ev.preventDefault(); nextExercise(); }
  };
}

function bindMatch(e) {
  const L = lesson;
  let left = null;
  let missed = false;
  let left_n = e.items.length;
  app.querySelector('.match').addEventListener('click', (ev) => {
    const b = ev.target.closest('.match-item');
    if (!b || b.disabled) return;
    if (b.dataset.side === 'l') {
      app.querySelectorAll('.match-item[data-side="l"]').forEach((x) => x.classList.toggle('selected', x === b));
      left = b; game.sound('tap'); return;
    }
    if (!left) { b.classList.add('nudge'); setTimeout(() => b.classList.remove('nudge'), 400); return; }
    if (left.dataset.i === b.dataset.i) {
      [left, b].forEach((x) => { x.classList.remove('selected'); x.classList.add('matched'); x.disabled = true; });
      left = null; left_n--; game.sound('match');
      if (!left_n) finishAnswer(!missed, missed ? 'Udało się, ale z pomyłką.' : '');
    } else {
      [left, b].forEach((x) => { x.classList.add('wrong-flash'); setTimeout(() => x.classList.remove('wrong-flash', 'selected'), 450); });
      left = null;
      if (!missed) { missed = true; game.sound('bad'); }
    }
  });
}

function evaluate() {
  const L = lesson;
  const e = L.queue[0];
  let ok = false, note = '', right = '';
  if (e.type === 'abcd') {
    ok = e.order[L.sel] === e.q.poprawna;
    right = e.q.odpowiedzi[e.q.poprawna];
    note = e.q.wyjasnienie || '';
    markOptions(e.order.indexOf(e.q.poprawna));
  } else if (e.type === 'choose') {
    ok = L.sel === e.good; right = e.f.tyl; markOptions(e.good);
  } else if (e.type === 'tf') {
    ok = (L.sel === 1) === e.truth;
    right = e.truth ? 'Prawda' : `Fałsz. Poprawna odpowiedź: ${e.f.tyl}`;
    markOptions(e.truth ? 0 : 1);
  } else if (e.type === 'type') {
    const inp = app.querySelector('#typed');
    const r = checkTyped(inp.value, e.f.tyl);
    ok = r !== 'bad'; right = e.f.tyl;
    if (r === 'typo') note = 'Uwaga na literówkę!';
    inp.disabled = true;
    inp.classList.add(ok ? 'ok' : 'bad');
  }
  finishAnswer(ok, note, right);
}

function markOptions(goodIdx) {
  app.querySelectorAll('.option').forEach((o, i) => {
    o.disabled = true;
    if (i === goodIdx) o.classList.add('correct');
    else if (o.classList.contains('selected')) o.classList.add('wrong');
  });
}

function finishAnswer(ok, note = '', right = '') {
  const L = lesson;
  const e = L.queue[0];
  L.state = 'fb';
  const sid = L.sc.s.id;
  if (ok && e.blad) clearMistake(sid, e.u.id, (e.f || e.q).id);
  if (!ok && (e.f || e.q)) addMistake(sid, e.u, e.f || e.q, e.f ? 'f' : 'q');
  if (ok) { L.correct++; game.sound('ok'); }
  else {
    L.wrong++;
    if (e.type !== 'match') game.sound('bad');
  }
  store.markActivity();
  store.save();
  const src = e.f?.zrodlo || e.q?.zrodlo || '';
  const report = e.f ? reportHref(L.sc.s, e.u, 'fiszka', e.f) : e.q ? reportHref(L.sc.s, e.u, 'pytanie', e.q) : '';
  const bar = app.querySelector('#bar');
  bar.className = `lesson-bar sheet ${ok ? 'ok' : 'bad'}`;
  bar.innerHTML = `<div class="sheet-head"><span class="sheet-icon">${ok ? ICONS.check : ICONS.close}</span>
      <strong>${ok ? PRAISE[Math.floor(Math.random() * PRAISE.length)] : 'Niestety, nie'}</strong></div>
    ${!ok && right ? `<p class="sheet-right"><b>Poprawna odpowiedź:</b> ${esc(right)}</p>` : ''}
    ${note ? `<p class="sheet-note">${esc(note)}</p>` : ''}
    <div class="sheet-foot">${src ? `<span class="sheet-src">${esc(src)}</span>` : '<span></span>'}${report ? reportBtn(report) : ''}</div>
    <button type="button" class="btn btn-lg btn-cta ${ok ? 'btn-success' : 'btn-danger-solid'}" id="next">Dalej</button>`;
  bar.querySelector('#next').addEventListener('click', nextExercise);
  bar.querySelector('#next').focus({ preventScroll: true });
  // błędne ćwiczenie wraca raz na koniec lekcji (jak w powtórkach)
  if (!ok && !e.retry && e.type !== 'match') { L.queue.push({ ...e, retry: true, order: e.order && shuffle(e.order) }); L.total++; }
}

function nextExercise() {
  const L = lesson;
  L.queue.shift();
  L.done++;
  renderExercise();
  window.scrollTo({ top: 0 });
}

function renderLessonEnd() {
  const L = lesson;
  const answered = L.correct + L.wrong;
  const acc = answered ? L.correct / answered : 0;
  const perfect = L.wrong === 0;
  if (!L.finished) {
    L.finished = true;
    const st = store.get();
    st.lekcje ||= {};
    const r = st.lekcje[L.key] || { n: 0, best: 0 };
    r.n++; r.best = Math.max(r.best || 0, pct(acc)); if (perfect) r.idealne = (r.idealne || 0) + 1;
    st.lekcje[L.key] = r;
    store.markActivity();
    game.award(0, { lekcje: 1, poprawne: L.correct, idealne: perfect ? 1 : 0 });
  }
  document.body.classList.remove('in-lesson');
  const secs = Math.round((Date.now() - L.start) / 1000);
  app.innerHTML = `
    <section class="result lesson-end">
      <p class="eyebrow">${esc(L.sc.title)}</p>
      <h1>${perfect ? 'Bez ani jednego błędu' : 'Lekcja zaliczona'}</h1>
      <div class="end-tiles">
        <div class="end-tile"><span>Celność</span><strong>${pct(acc)}%</strong></div>
        <div class="end-tile"><span>Poprawne</span><strong>${L.correct}/${answered}</strong></div>
        <div class="end-tile"><span>Czas</span><strong>${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, '0')}</strong></div>
      </div>
      ${L.wrong ? '<p class="muted">Pytania z błędami trafiły do „Błędów do poprawy”.</p>' : ''}
      <div class="actions">
        <a class="btn btn-primary btn-lg btn-cta" href="#/">Kontynuuj</a>
        <button type="button" class="btn btn-ghost btn-lg" id="again">Jeszcze jedna lekcja</button>
      </div>
    </section>`;
  app.querySelector('#again').addEventListener('click', () => { const sc = L.sc; lesson = null; if (sc.type === 'b') viewBledy(sc.s.id); else viewLekcja(sc.s.id, sc.type, sc.id); });
  keyHandler = (ev) => { if (ev.key === 'Enter') { ev.preventDefault(); location.hash = '#/'; } };
}

// ---------- dział i poddział ----------
function learnActions(sc, sm) {
  const base = scopePath(sc);
  const nQ = Math.min(TEST_SIZE, scopeQuestions(sc).length);
  const total = sc.units.reduce((n, u) => n + u.fiszki.length, 0);
  let fiszki = '';
  if (total) {
    fiszki = sm.todo
      ? `<a class="btn btn-ghost btn-xl" href="#/fiszki/${base}">${ICONS.cards}<span>Fiszki<small>${nFiszek(sm.todo)} na dziś</small></span></a>`
      : `<div class="done-note">${ICONS.check}<span>${sm.fresh ? 'Dzienny limit nowych fiszek wykorzystany. Wróć jutro albo poćwicz swobodnie.' : 'Na dziś wszystko powtórzone! Wróć jutro albo poćwicz swobodnie.'}</span></div>`;
    fiszki += `<a class="btn btn-ghost btn-xl" href="#/fiszki/${base}/trening">${ICONS.cards}<span>Trening swobodny<small>losowe fiszki, bez wpływu na harmonogram</small></span></a>`;
  }
  const lekcja = total || nQ ? `<a class="btn btn-primary btn-xl" href="#/lekcja/${base}">${ICONS.play}<span>Lekcja<small>12 różnych ćwiczeń · +10 XP</small></span></a>` : '';
  return `${lekcja}${fiszki}
    ${nQ ? `<a class="btn btn-gold btn-xl" href="#/test/${base}">${ICONS.quiz}<span>Test<small>${nQ} ${plural(nQ, 'losowe pytanie', 'losowe pytania', 'losowych pytań')} ABCD</small></span></a>` : ''}`;
}

function lastTestNote(sc) {
  const key = `${sc.type}:${sc.id}`;
  const tests = store.get().tests.filter((t) => t.sid === sc.s.id && t.scope === key);
  if (!tests.length) return '';
  const last = tests[tests.length - 1];
  const best = tests.reduce((m, t) => Math.max(m, t.score / t.total), 0);
  return `<p class="muted center">Ostatni test: <strong>${pct(last.score / last.total)}%</strong> · najlepszy: <strong>${pct(best)}%</strong></p>`;
}

function viewDzial(sid, did) {
  const sc = resolveScope(sid, 'd', did);
  if (!sc) return notFound();
  const { s, dzial: d } = sc;
  const allowance = newAllowance(s.id);
  const sm = summary(s.id, d.poddzialy, allowance);
  const nTasks = tasksOf(s, d.id).length;

  app.innerHTML = `
    ${pageHead(d.nazwa, '#/nauka', s.nazwa)}
    ${d.opis ? `<p class="lead">${esc(d.opis)}</p>` : ''}
    ${statsCard(sm)}
    <div class="actions">
      ${learnActions(sc, sm)}
      ${nTasks ? `<a class="btn btn-ghost btn-xl" href="#/zadania/${enc(s.id)}/d/${enc(d.id)}">${ICONS.exam}<span>Zadania maturalne<small>${nZadan(nTasks)} CKE z tego działu</small></span></a>` : ''}
    </div>
    ${lastTestNote(sc)}
    ${d.poddzialy.length > 1 || d.poddzialy[0].id !== d.id ? `<h2 class="section-title">Poddziały (${d.poddzialy.length})</h2>
      <div class="dzial-list">${d.poddzialy.map((u) => unitRow(hrefUnit(s.id, u.id), u.nazwa, summary(s.id, [u], allowance), u.pytania.length ? ` · ${u.pytania.length} pyt.` : '')).join('')}</div>`
      : `<div class="actions"><a class="btn btn-ghost btn-xl" href="#/lista/${enc(s.id)}/${enc(d.poddzialy[0].id)}">${ICONS.book}<span>Przeglądaj treści<small>wszystkie fiszki i pytania ze źródłami</small></span></a></div>`}
  `;
}

function viewUnit(sid, uid) {
  const sc = resolveScope(sid, 'p', uid);
  if (!sc) return notFound();
  const { s, unit: u, dzial: d } = sc;
  const sm = summary(s.id, [u]);
  app.innerHTML = `
    ${pageHead(u.nazwa, d ? hrefDzial(s.id, d.id) : '#/', d?.nazwa || s.nazwa)}
    ${u.opis ? `<p class="lead">${esc(u.opis)}</p>` : ''}
    ${statsCard(sm)}
    <div class="actions">
      ${learnActions(sc, sm)}
      <a class="btn btn-ghost btn-xl" href="#/lista/${enc(s.id)}/${enc(u.id)}">${ICONS.book}<span>Przeglądaj treści<small>wszystkie fiszki i pytania ze źródłami</small></span></a>
    </div>
    ${lastTestNote(sc)}`;
}

// ---------- fiszki ----------
let session = null;

function viewFiszki(sid, type, id, mode) {
  const sc = resolveScope(sid, type, id);
  if (!sc) return notFound();
  const wlasna = type === 'w';
  const training = wlasna ? !RODZAJE_SRS.has(id) : mode === 'trening';
  const key = `${sid}/${type}/${id}/${mode || ''}`;
  if (!session || session.key !== key) {
    const queue = wlasna ? kolejkaWlasna(sc, id) : training
      ? shuffle(sc.units.flatMap((u) => u.fiszki.map((f) => ({ f, u })))).slice(0, 50)
      : buildQueue(sc.s.id, sc.units);
    session = { key, sc, queue, done: 0, training, counts: { nie: 0, trudne: 0, umiem: 0 } };
  }
  renderCard();
}

function renderCard() {
  const { sc, queue, training } = session;
  const s = sc.s;
  document.body.classList.add('in-session');
  if (!queue.length) return renderSessionEnd();

  const { f, u } = queue[0];
  const st = store.get().cards[cardKey(s.id, u.id, f.id)];
  const total = session.done + queue.length;
  const isNew = !st || !st.reps;

  app.innerHTML = `
    <div class="session-top">
      <a class="icon-btn" href="${sc.back}" aria-label="Zakończ sesję">${ICONS.close}</a>
      <div class="session-progress">${progressBar(session.done / total, 'Postęp sesji')}</div>
      <span class="session-count">${session.done + 1}/${total}</span>
    </div>
    <p class="session-label">${training ? (sc.type === 'w' ? 'Własna powtórka — bez zmiany harmonogramu' : 'Trening swobodny') : isNew ? '<span class="tag tag-new">Nowa fiszka</span>' : '<span class="tag">Powtórka</span>'}
      ${sc.type === 'd' ? `<span class="session-unit">${esc(u.nazwa)}</span>` : ''}</p>

    <div class="flashcard" id="card" role="button" tabindex="0" aria-label="Fiszka — dotknij, aby odwrócić">
      <div class="flashcard-inner">
        <div class="face face-front">
          <span class="face-label">Pytanie</span>
          <p class="face-text">${esc(f.przod)}</p>
          <span class="face-hint">Dotknij, aby zobaczyć odpowiedź</span>
        </div>
        <div class="face face-back" aria-hidden="true">
          <span class="face-label">Odpowiedź</span>
          <p class="face-text">${esc(f.tyl)}</p>
          ${sourceTag(f.zrodlo)}
        </div>
      </div>
    </div>

    <div class="card-actions">
      <button type="button" class="btn btn-primary btn-lg" id="flip">Pokaż odpowiedź</button>
      <div class="rate-row" id="rate" hidden>
        <button type="button" class="btn btn-rate rate-nie" data-r="nie"><span>Nie wiem</span><small>${training ? '' : intervalLabel(st, 'nie')}</small></button>
        <button type="button" class="btn btn-rate rate-trudne" data-r="trudne"><span>Trudne</span><small>${training ? '' : intervalLabel(st, 'trudne')}</small></button>
        <button type="button" class="btn btn-rate rate-umiem" data-r="umiem"><span>Umiem</span><small>${training ? '' : intervalLabel(st, 'umiem')}</small></button>
      </div>
      ${reportBtn(reportHref(s, u, 'fiszka', f))}
    </div>
  `;

  const card = app.querySelector('#card');
  const flipBtn = app.querySelector('#flip');
  const rate = app.querySelector('#rate');
  let flipped = false;
  const flip = () => {
    flipped = !flipped;
    card.classList.toggle('flipped', flipped);
    card.querySelector('.face-front').setAttribute('aria-hidden', String(flipped));
    card.querySelector('.face-back').setAttribute('aria-hidden', String(!flipped));
    if (flipped) {
      flipBtn.hidden = true;
      rate.hidden = false;
    }
  };
  card.addEventListener('click', flip);
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') { e.preventDefault(); flip(); }
  });
  flipBtn.addEventListener('click', flip);
  rate.addEventListener('click', (e) => {
    const b = e.target.closest('[data-r]');
    if (b) rateCard(b.dataset.r);
  });
  keyHandler = (e) => {
    if (e.key === ' ') { e.preventDefault(); flip(); return; }
    if (!flipped) return;
    const r = { 1: 'nie', 2: 'trudne', 3: 'umiem' }[e.key];
    if (r) rateCard(r);
  };
}

function rateCard(r) {
  const { sc, queue, training } = session;
  const item = queue.shift();
  session.counts[r]++;
  if (!training) {
    const key = cardKey(sc.s.id, item.u.id, item.f.id);
    const cards = store.get().cards;
    cards[key] = nextState(cards[key], r);
  }
  store.markActivity();
  game.award(r === 'umiem' ? 2 : 1, { fiszki: 1 });
  if (r === 'nie') queue.splice(Math.min(3, queue.length), 0, item); // wróci za kilka fiszek
  else session.done++;
  renderCard();
  window.scrollTo({ top: 0 });
}

function renderSessionEnd() {
  const { sc, counts, training } = session;
  const sm = summary(sc.s.id, sc.units);
  const reviewed = counts.nie + counts.trudne + counts.umiem;
  const base = scopePath(sc);
  app.innerHTML = `
    <div class="session-top"><a class="icon-btn" href="${sc.back}" aria-label="Zamknij">${ICONS.close}</a></div>
    <section class="result">
      <div class="result-icon">${ICONS.compass}</div>
      <h1>${reviewed ? 'Koniec sesji' : 'Na dziś wszystko!'}</h1>
      <p class="lead">${reviewed
        ? `Liczba ocen: ${reviewed}. ${training ? 'Trening nie zmienia harmonogramu powtórek.' : 'Kolejne powtórki zaplanowane.'}`
        : 'Nie ma teraz fiszek do powtórki. Wróć jutro albo poćwicz swobodnie.'}</p>
      ${reviewed ? `<div class="mini-stats">
        <div class="c-bad"><strong>${counts.nie}</strong><span>Nie wiem</span></div>
        <div class="c-warn"><strong>${counts.trudne}</strong><span>Trudne</span></div>
        <div class="c-ok"><strong>${counts.umiem}</strong><span>Umiem</span></div>
      </div>` : ''}
      <p class="muted">Opanowanie: <strong>${pct(sm.progress)}%</strong></p>
      <div class="actions">
        ${sm.todo && !training ? `<a class="btn btn-primary btn-lg" href="#/fiszki/${base}" data-restart>Kontynuuj (${sm.todo})</a>` : ''}
        ${training ? `<a class="btn btn-primary btn-lg" href="#/fiszki/${base}${sc.type === 'w' ? '' : '/trening'}" data-restart>${sc.type === 'w' ? 'Jeszcze raz' : 'Kolejne 50 fiszek'}</a>` : ''}
        ${scopeQuestions(sc).length ? `<a class="btn btn-gold btn-lg" href="#/test/${base}">Sprawdź się w teście</a>` : ''}
        <a class="btn btn-ghost btn-lg" href="${sc.back}">Wróć</a>
      </div>
    </section>`;
  app.querySelectorAll('[data-restart]').forEach((a) => a.addEventListener('click', () => {
    session = null;
    if (location.hash === a.getAttribute('href')) route();
  }));
  keyHandler = null;
}

// ---------- test ABCD ----------
let test = null;

function viewTest(sid, type, id) {
  const sc = resolveScope(sid, type, id);
  if (!sc) return notFound();
  if (!test || test.key !== `${sid}/${type}/${id}`) startTest(sc);
  renderQuestion();
}

const DIAG_SIZE = 20;
function pytaniaDiagnozy(sc) {
  const s = sc.s;
  const w = wagiDzialow(s);
  const out = [];
  for (const d of s.dzialy) {
    const pula = shuffle(sc.units.filter((u) => u.dzialId === d.id).flatMap((u) => u.pytania.map((q) => ({ q, u }))));
    out.push(...pula.slice(0, Math.max(2, Math.round((w[d.id] || 0) * DIAG_SIZE))));
  }
  return shuffle(out).slice(0, DIAG_SIZE + 6);
}

function startTest(sc) {
  const qs = (sc.type === 'x' ? pytaniaDiagnozy(sc) : shuffle(scopeQuestions(sc)).slice(0, TEST_SIZE))
    .map(({ q, u }) => ({ q, u, order: shuffle(q.odpowiedzi.map((_, i) => i)) }));
  test = { key: `${sc.s.id}/${sc.type}/${sc.id}`, sc, qs, i: 0, answers: [], saved: false };
}

function renderQuestion() {
  const { sc, qs, i } = test;
  document.body.classList.add('in-session');
  if (!qs.length) return notFound();
  if (i >= qs.length) return renderTestEnd();
  const { q, u, order } = qs[i];

  app.innerHTML = `
    <div class="session-top">
      <a class="icon-btn" href="${sc.back}" aria-label="Przerwij test">${ICONS.close}</a>
      <div class="session-progress">${progressBar(i / qs.length, 'Postęp testu')}</div>
      <span class="session-count">${i + 1}/${qs.length}</span>
    </div>
    <section class="question">
      <p class="eyebrow">${sc.type === 'x' ? `Diagnoza · ${esc(dzialOf(sc.s, u)?.nazwa || '')}` : `Pytanie ${i + 1}${sc.type === 'd' ? ` · ${esc(u.nazwa)}` : ''}`}</p>
      <h2 class="question-text">${esc(q.pytanie)}</h2>
      <div class="options" role="group" aria-label="Odpowiedzi">
        ${order.map((oi, pos) => `<button type="button" class="option" data-oi="${oi}">
            <span class="option-letter">${LITERY[pos]}</span><span class="option-text">${esc(q.odpowiedzi[oi])}</span>
          </button>`).join('')}
      </div>
      ${sc.type === 'x' ? '<button type="button" class="btn btn-ghost btn-lg diag-idk" data-idk>Nie wiem — pomiń</button><p class="muted small diag-hint">Nie zgaduj: „Nie wiem” daje dokładniejszy wynik.</p>' : ''}
      <div id="feedback" aria-live="polite"></div>
      ${sc.type === 'x' ? '' : reportBtn(reportHref(sc.s, u, 'pytanie', q))}
    </section>`;
  app.querySelector('[data-idk]')?.addEventListener('click', () => { if (test.answers[i] === undefined) answer(-1); });

  app.querySelector('.options').addEventListener('click', (e) => {
    const b = e.target.closest('.option');
    if (b && test.answers[i] === undefined) answer(Number(b.dataset.oi));
  });
  if (test.answers[i] !== undefined && sc.type !== 'x') showFeedback();
  keyHandler = (e) => {
    const pos = ['1', '2', '3', '4'].includes(e.key) ? Number(e.key) - 1 : LITERY.indexOf(e.key.toUpperCase());
    if (test.answers[i] === undefined && pos >= 0 && pos < order.length) answer(order[pos]);
    else if (test.answers[i] !== undefined && e.key === 'Enter') { e.preventDefault(); nextQuestion(); }
  };
}

function answer(oi) {
  test.answers[test.i] = oi;
  store.markActivity();
  const ok = oi === test.qs[test.i].q.poprawna;
  if (test.sc.type === 'x') { // diagnoza: bez oceniania na bieżąco — od razu następne pytanie
    game.sound('tap');
    setTimeout(nextQuestion, 160);
    return;
  }
  if (!ok) addMistake(test.sc.s.id, test.qs[test.i].u, test.qs[test.i].q, 'q');
  game.sound(ok ? 'ok' : 'bad');
  game.award(ok ? 2 : 0, { poprawne: ok ? 1 : 0 });
  showFeedback();
}

function showFeedback() {
  const { q } = test.qs[test.i];
  const chosen = test.answers[test.i];
  const ok = chosen === q.poprawna;
  app.querySelectorAll('.option').forEach((b) => {
    const oi = Number(b.dataset.oi);
    b.disabled = true;
    if (oi === q.poprawna) b.classList.add('correct');
    else if (oi === chosen) b.classList.add('wrong');
  });
  const last = test.i === test.qs.length - 1;
  const fb = app.querySelector('#feedback');
  fb.innerHTML = `<div class="feedback ${ok ? 'ok' : 'bad'}">
      <strong>${ok ? `${ICONS.check} Dobrze!` : `${ICONS.close} Niestety, źle`}</strong>
      ${q.wyjasnienie ? `<p>${esc(q.wyjasnienie)}</p>` : ''}
      ${sourceTag(q.zrodlo)}
    </div>
    <button type="button" class="btn btn-primary btn-lg" id="next">${last ? 'Zobacz wynik' : 'Dalej'}</button>`;
  fb.querySelector('#next').addEventListener('click', nextQuestion);
  fb.querySelector('#next').focus({ preventScroll: true });
  fb.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function nextQuestion() {
  test.i++;
  renderQuestion();
  window.scrollTo({ top: 0 });
}

function renderTestEnd() {
  if (test.sc.type === 'x') return renderDiagnozaEnd();
  const { sc, qs, answers } = test;
  const s = sc.s;
  const score = qs.reduce((n, { q }, i) => n + (answers[i] === q.poprawna ? 1 : 0), 0);
  const p = pct(score / qs.length);
  if (!test.saved) {
    store.addTest({ sid: s.id, scope: `${sc.type}:${sc.id}`, name: sc.title, score, total: qs.length, at: Date.now() });
    test.saved = true;
    game.award(5 + (score === qs.length ? 5 : 0));
  }
  const msg = p >= 90 ? 'Bardzo dobrze' : p >= 70 ? 'Dobry wynik' : p >= 50 ? 'Połowa za Tobą' : 'Warto powtórzyć fiszki';
  const wrong = qs.map((x, i) => ({ ...x, a: answers[i] })).filter((x) => x.a !== x.q.poprawna);

  app.innerHTML = `
    <div class="session-top"><a class="icon-btn" href="${sc.back}" aria-label="Zamknij">${ICONS.close}</a></div>
    <section class="result">
      <div class="ring ring-xl ${p >= 70 ? 'ring-ok' : p >= 50 ? 'ring-warn' : 'ring-bad'}" style="--p:${p}"><span>${p}%</span></div>
      <h1>${msg}</h1>
      <p class="lead">Poprawne odpowiedzi: <strong>${score} z ${qs.length}</strong></p>
      <div class="actions">
        <button type="button" class="btn btn-gold btn-lg" id="again">Nowy test</button>
        <a class="btn btn-ghost btn-lg" href="${sc.back}">Wróć</a>
      </div>
    </section>
    ${wrong.length ? `<h2 class="section-title">Do poprawki</h2>
      <div class="review-list">${wrong.map(({ q, u, a }) => `<article class="card review">
        <h3>${esc(q.pytanie)}</h3>
        <p class="ans bad">${ICONS.close}<span>Twoja odpowiedź: ${esc(q.odpowiedzi[a])}</span></p>
        <p class="ans ok">${ICONS.check}<span>Poprawna: ${esc(q.odpowiedzi[q.poprawna])}</span></p>
        ${q.wyjasnienie ? `<p class="muted">${esc(q.wyjasnienie)}</p>` : ''}
        <div class="review-foot">${sourceTag(q.zrodlo) || '<span></span>'}${reportBtn(reportHref(s, u, 'pytanie', q))}</div>
      </article>`).join('')}</div>` : ''}`;

  app.querySelector('#again').addEventListener('click', () => {
    startTest(sc);
    renderQuestion();
    window.scrollTo({ top: 0 });
  });
  keyHandler = null;
}

// ---------- test diagnostyczny: wynik ----------
function renderDiagnozaEnd() {
  const { sc, qs, answers } = test;
  const s = sc.s;
  if (!test.saved) {
    const dz = {};
    qs.forEach(({ q, u }, i) => { const r = (dz[u.dzialId] ||= [0, 0]); r[1]++; if (answers[i] === q.poprawna) r[0]++; });
    const st = store.get();
    st.diagnoza = { ...(st.diagnoza || {}), [s.id]: { at: Date.now(), dz } };
    store.save();
    test.saved = true;
    game.award(10);
  }
  const score = qs.reduce((n, { q }, i) => n + (answers[i] === q.poprawna ? 1 : 0), 0);
  const pr = prognoza(s);
  const dz = store.get().diagnoza[s.id].dz;
  const slabe = s.dzialy.filter((d) => dz[d.id]).map((d) => ({ d, r: dz[d.id], w: wagiDzialow(s)[d.id] }))
    .sort((a, b) => a.r[0] / a.r[1] - b.r[0] / b.r[1] || b.w - a.w);
  const start = slabe[0]?.d;
  app.innerHTML = `
    <div class="session-top"><a class="icon-btn" href="#/" aria-label="Zamknij">${ICONS.close}</a></div>
    <section class="result">
      <p class="eyebrow">Twój punkt startowy · ${esc(s.nazwa)}</p>
      <div class="prog-nums big diag-nums"><div><b>${pr.dzis.pokaz}%</b><small>gdyby matura była dziś</small></div><div><b>${score}/${qs.length}</b><small>poprawnych odpowiedzi</small></div></div>
      <p class="lead">Ostrożny szacunek z krótkiego testu. W maju: <strong>${pr.maj.pokaz}%</strong>, jeśli będziesz trzymać się planu — z każdą fiszką i zadaniem prognoza będzie dokładniejsza.</p>
    </section>
    <section class="card"><h2 class="card-title">Wynik w działach</h2>
      <div class="prog-dz">${slabe.map(({ d, r }) => { const q = r[0] / r[1]; const et = q >= 0.75 ? 'mocna strona' : q >= 0.4 ? 'średnio' : 'do nauki';
        return `<div class="prog-dz-row"><span>${esc(d.nazwa)} <em class="diag-tag ${et === 'do nauki' ? 'bad' : et === 'mocna strona' ? 'ok' : ''}">${et}</em></span><small>${r[0]} z ${r[1]} poprawnie</small>
        <div class="core-mini"><i style="width:${(r[0] / r[1]) * 100}%"></i></div></div>`; }).join('')}</div>
    </section>
    <div class="actions">
      ${start ? `<a class="btn btn-primary btn-lg" href="#/d/${enc(s.id)}/${enc(start.id)}">Zacznij od: ${esc(start.nazwa)}</a>` : ''}
      <a class="btn btn-ghost btn-lg" href="#/prognoza">Zobacz prognozę</a>
    </div>`;
  keyHandler = null;
}

function viewDiagnoza() {
  const s = currentSubject();
  if (!s) return notFound();
  const byl = store.get().diagnoza?.[s.id];
  app.innerHTML = `
    ${pageHead('Test diagnostyczny', '#/', s.nazwa)}
    <section class="card diag-intro">
      <div class="plan-tiles"><div class="plan-tile"><b>~${DIAG_SIZE}</b><span>pytań</span></div><div class="plan-tile"><b>4</b><span>minuty</span></div><div class="plan-tile"><b>${s.dzialy.length}</b><span>działów</span></div></div>
      <p>Co najmniej 2 pytania z każdego działu. Bez podpowiedzi w trakcie — jeśli nie wiesz, wybierz „Nie wiem” zamiast zgadywać. Na końcu: punkt startowy, prognoza i dział, od którego warto zacząć.</p>
      ${byl ? `<p class="muted small">Ostatni test: ${fmtDay(byl.at)}. Nowy wynik zastąpi poprzedni.</p>` : ''}
    </section>
    <a class="btn btn-primary btn-lg" href="#/test/${enc(s.id)}/x/start">Zaczynam</a>
    <a class="link-btn" href="#/">Pomiń</a>`;
}

// ---------- przegląd treści poddziału ----------
function viewLista(sid, uid) {
  const sc = resolveScope(sid, 'p', uid);
  if (!sc) return notFound();
  const { s, unit: u } = sc;
  const cards = store.get().cards;
  const boxLabel = (c) => (!c || !c.reps ? 'nowa' : c.box >= MASTERED_BOX ? 'opanowana' : `poziom ${c.box}/6`);
  app.innerHTML = `
    ${pageHead('Treści', sc.back, u.nazwa)}
    <div class="tabs" role="tablist">
      <button type="button" role="tab" class="tab active" aria-selected="true" data-tab="f">Fiszki (${u.fiszki.length})</button>
      <button type="button" role="tab" class="tab" aria-selected="false" data-tab="p">Pytania (${u.pytania.length})</button>
    </div>
    <div data-panel="f" class="review-list">${u.fiszki.map((f, i) => {
      const c = cards[cardKey(s.id, u.id, f.id)];
      return `<article class="card review">
        <div class="review-head"><span class="muted">${i + 1}.</span><span class="tag ${c && c.box >= MASTERED_BOX ? 'tag-ok' : ''}">${boxLabel(c)}</span></div>
        <h3>${esc(f.przod)}</h3><p>${esc(f.tyl)}</p>
        <div class="review-foot">${sourceTag(f.zrodlo) || '<span></span>'}${reportBtn(reportHref(s, u, 'fiszka', f))}</div>
      </article>`;
    }).join('')}</div>
    <div data-panel="p" class="review-list" hidden>${u.pytania.map((q, i) => `<article class="card review">
        <div class="review-head"><span class="muted">${i + 1}.</span></div>
        <h3>${esc(q.pytanie)}</h3>
        <ol class="abcd">${q.odpowiedzi.map((o, j) => `<li class="${j === q.poprawna ? 'ok' : ''}"><b>${LITERY[j]}</b> ${esc(o)}${j === q.poprawna ? ` ${ICONS.check}` : ''}</li>`).join('')}</ol>
        ${q.wyjasnienie ? `<p class="muted">${esc(q.wyjasnienie)}</p>` : ''}
        <div class="review-foot">${sourceTag(q.zrodlo) || '<span></span>'}${reportBtn(reportHref(s, u, 'pytanie', q))}</div>
      </article>`).join('') || '<p class="muted">Ten poddział nie ma jeszcze pytań testowych.</p>'}</div>`;

  app.querySelector('.tabs').addEventListener('click', (e) => {
    const t = e.target.closest('[data-tab]');
    if (!t) return;
    app.querySelectorAll('.tab').forEach((b) => {
      b.classList.toggle('active', b === t);
      b.setAttribute('aria-selected', String(b === t));
    });
    app.querySelectorAll('[data-panel]').forEach((p) => (p.hidden = p.dataset.panel !== t.dataset.tab));
  });
}

// ---------- zadania maturalne ----------
function taskScore(sid, list) {
  const st = store.get().zadania;
  let done = 0, pkt = 0, max = 0;
  for (const z of list) {
    const r = st[taskKey(sid, z)];
    if (r) { done++; pkt += r.pkt; max += r.max; }
  }
  return { done, pkt, max, total: list.length };
}

const MATURA_TABS = [['proba', 'Próbna'], ['cke', 'Arkusze CKE'], ['dzialy', 'Działy']];
const scoreTag = (sc) => (sc.done ? `<span class="score ${sc.pkt / sc.max >= .7 ? 'ok' : sc.pkt / sc.max >= .5 ? 'warn' : 'bad'}">${pct(sc.pkt / sc.max)}%</span>` : '');

function lockedRow(name) {
  return `<a class="dzial-row locked-row" href="#/plany">
    <div class="dzial-row-top"><span class="dzial-name">${esc(name)}</span><span class="badge">${ICONS.lock}</span></div>
    <div class="dzial-meta"><span>Premium — odblokuj wszystkie arkusze z omówieniem</span></div>
  </a>`;
}

function taskRow(href, name, sc, right = '') {
  return `<a class="dzial-row" href="${href}">
    <div class="dzial-row-top"><span class="dzial-name">${esc(name)}</span>${scoreTag(sc)}</div>
    ${progressBar(sc.done / (sc.total || 1), `Rozwiązane zadania: ${name}`)}
    <div class="dzial-meta"><span>${sc.done}/${nZadan(sc.total)} rozwiązanych</span>${right}</div>
  </a>`;
}

function viewMatura(tab) {
  if (tab === 'autorskie') tab = 'dzialy';
  tab = MATURA_TABS.some(([k]) => k === tab) ? tab : 'proba';
  const s = currentSubject();
  if (!s) return notFound();
  let body = '';
  if (tab === 'proba') {
    body = examSection(s);
  } else if (tab === 'cke') {
    body = `<div class="dzial-list">${s.arkusze.map((a) => a.zablokowany ? lockedRow(a.nazwa) : taskRow(`#/zadania/${enc(s.id)}/a/${enc(a.id)}`, a.nazwa, taskScore(s.id, a.zadania), `<span>${a.punkty} pkt</span>`)).join('')}</div>`
      || '<p class="muted">Brak arkuszy CKE.</p>';
  } else {
    body = `<div class="dzial-list">${s.dzialy.map((d) => {
        const cke = tasksOf(s, d.id);
        const own = bankTasks(s, d.id);
        if (!cke.length && !own.length) return '';
        const sc = taskScore(s.id, [...cke, ...own]);
        return `<div class="dzial-row">
          <div class="dzial-row-top"><span class="dzial-name">${esc(d.nazwa)}</span>${scoreTag(sc)}</div>
          ${progressBar(sc.done / (sc.total || 1), `Rozwiązane zadania: ${d.nazwa}`)}
          <div class="pop-row">
            ${cke.length ? `<a class="btn btn-ghost btn-sm" href="#/zadania/${enc(s.id)}/d/${enc(d.id)}">Z arkuszy CKE <b>${cke.length}</b></a>` : ''}
            ${own.length ? `<a class="btn btn-ghost btn-sm" href="#/zadania/${enc(s.id)}/b/${enc(d.id)}">Autorskie <b>${own.length}</b></a>` : ''}
          </div>
        </div>`;
      }).join('')}</div>`;
  }
  app.innerHTML = `
    ${pageHead('Matura', null)}
    <nav class="seg-tabs" aria-label="Sekcje matury">${MATURA_TABS.map(([k, l]) => `<a href="#/matura/${k}" class="${k === tab ? 'active' : ''}" ${k === tab ? 'aria-current="page"' : ''}>${l}</a>`).join('')}</nav>
    ${body}`;
  if (tab === 'proba') bindExamSection(s);
}

let zs = null; // sesja zadań

function viewZadania(sid, type, id) {
  const s = findSubject(sid);
  if (!s) return notFound();
  const key = `${sid}/${type}/${id}`;
  if (!zs || zs.key !== key) {
    let list, title;
    if (type === 'a') {
      const a = s.arkusze.find((x) => x.id === id);
      if (!a) return notFound();
      if (a.zablokowany) { location.hash = '#/plany'; return; }
      list = a.zadania;
      title = a.nazwa;
    } else if (type === 'b') {
      const d = findDzial(s, id);
      if (!d) return notFound();
      list = bankTasks(s, d.id);
      title = `${d.nazwa} — zadania autorskie`;
    } else {
      const d = findDzial(s, id);
      if (!d) return notFound();
      list = tasksOf(s, d.id);
      title = d.nazwa;
    }
    if (!list.length) return notFound();
    const st = store.get().zadania;
    const firstOpen = list.findIndex((z) => !st[taskKey(s.id, z)]);
    zs = { key, s, list, title, i: Math.max(0, firstOpen), drafts: {}, revealed: {} };
  }
  renderTask();
}

const pre = (t) => `<div class="pre">${esc(t)}</div>`;

// Materiał z blokami: [[wykres: tytuł | jednostka]] … [[/]], [[linia: …]], [[tabela: tytuł]], [[rysunek: tytuł]], [[mapa: tytuł]]
const num = (v) => Number(String(v).replace(/\s/g, '').replace(',', '.').replace(/[^\d.\-]/g, ''));
const fmtNum = (v) => String(v).trim();
function richBlock(kind, head, lines) {
  const [tytul = '', jedn = ''] = head.split('|').map((x) => x.trim());
  const rows = lines.filter((l) => l.trim()).map((l) => l.split('|').map((x) => x.trim()));
  const cap = tytul ? `<figcaption>${esc(tytul)}${jedn ? ` <span class="muted">(${esc(jedn)})</span>` : ''}</figcaption>` : '';
  if (kind === 'tabela') {
    const [h, ...body] = rows;
    return `<figure class="mat-fig">${cap}<div class="mat-table-wrap"><table class="mat-table">
      <thead><tr>${(h || []).map((c) => `<th scope="col">${esc(c)}</th>`).join('')}</tr></thead>
      <tbody>${body.map((r) => `<tr>${r.map((c, i) => i ? `<td>${esc(c)}</td>` : `<th scope="row">${esc(c)}</th>`).join('')}</tr>`).join('')}</tbody></table></div></figure>`;
  }
  if (kind === 'rysunek' || kind === 'mapa') {
    return `<figure class="mat-fig mat-drawing ${kind}"><div class="mat-drawing-label">${kind === 'mapa' ? 'Mapa — opis' : 'Rysunek — opis'}</div>${tytul ? `<strong>${esc(tytul)}</strong>` : ''}${lines.map((l) => l.trim() ? `<p>${esc(l)}</p>` : '').join('')}</figure>`;
  }
  // wykres słupkowy / liniowy; wiersz zaczynający się od "#" to nagłówek serii
  let series = [''];
  let data = rows;
  if (rows[0] && rows[0][0] === '#') { series = rows[0].slice(1); data = rows.slice(1); }
  const max = Math.max(...data.flatMap((r) => r.slice(1).map(num)).filter((x) => !isNaN(x)), 0) || 1;
  const legend = series.length > 1 ? `<div class="chart-legend">${series.map((s, i) => `<span><i class="sw s${i}"></i>${esc(s)}</span>`).join('')}</div>` : '';
  if (kind === 'linia') {
    // dane: wiersz = seria, kolumny = kolejne punkty (nagłówek "#" = etykiety osi X)
    const xs = series.length > 1 || series[0] ? series : data[0].slice(1).map((_, i) => String(i + 1));
    const W = 320, H = 170, L = 34, R = 12, T = 12, B = 26;
    const x = (i) => L + (xs.length < 2 ? 0 : (i * (W - L - R)) / (xs.length - 1));
    const pw = 10 ** Math.floor(Math.log10(max));
    const top = [1, 2, 2.5, 5, 10].map((m) => m * pw).find((v) => v >= max);
    const y = (v) => T + (H - T - B) * (1 - v / top);
    const ticks = [0, .25, .5, .75, 1].map((f) => Math.round(top * f * 100) / 100);
    const svg = `<svg viewBox="0 0 ${W} ${H}" class="chart-line" role="img" aria-label="${esc(tytul)}">
      ${ticks.map((v) => `<line x1="${L}" x2="${W - R}" y1="${y(v)}" y2="${y(v)}" class="grid"/><text x="${L - 4}" y="${y(v) + 3}" text-anchor="end">${v}</text>`).join('')}
      ${xs.map((lbl, i) => `<text x="${x(i)}" y="${H - 8}" text-anchor="middle">${esc(lbl)}</text>`).join('')}
      ${data.map((r, si) => `<polyline class="ln s${si}" points="${r.slice(1).map((v, i) => `${x(i)},${y(num(v))}`).join(' ')}"/>${r.slice(1).map((v, i) => `<circle class="pt s${si}" cx="${x(i)}" cy="${y(num(v))}" r="3"><title>${esc(r[0])}, ${esc(xs[i])}: ${esc(v)}</title></circle>`).join('')}`).join('')}
    </svg>`;
    const leg = data.length < 2 ? '' : `<div class="chart-legend">${data.map((r, i) => `<span><i class="sw s${i}"></i>${esc(r[0])}</span>`).join('')}</div>`;
    const tbl = `<details class="chart-data"><summary>Dane w tabeli</summary><table class="mat-table"><thead><tr><th></th>${xs.map((v) => `<th>${esc(v)}</th>`).join('')}</tr></thead><tbody>${data.map((r) => `<tr><th scope="row">${esc(r[0])}</th>${r.slice(1).map((v) => `<td>${esc(v)}</td>`).join('')}</tr>`).join('')}</tbody></table></details>`;
    return `<figure class="mat-fig chart">${cap}${svg}${leg}${tbl}</figure>`;
  }
  return `<figure class="mat-fig chart">${cap}${legend}<div class="bars">${data.map((r) => `<div class="bar-row"><span class="bar-label">${esc(r[0])}</span><div class="bar-group">${r.slice(1).map((v, i) => `<div class="bar-line"><span class="bar s${i}" style="width:${Math.max(0, Math.min(100, (num(v) / max) * 100))}%"></span><span class="bar-val">${esc(fmtNum(v))}</span></div>`).join('')}</div></div>`).join('')}</div></figure>`;
}
function rich(text) {
  if (!text.includes('[[')) return pre(text);
  const out = []; let buf = []; let blk = null;
  const flush = () => { if (buf.join('').trim()) out.push(pre(buf.join('\n').replace(/^\n+|\n+$/g, ''))); buf = []; };
  for (const line of text.split('\n')) {
    const m = line.match(/^\s*\[\[(wykres|linia|tabela|rysunek|mapa)\s*:?\s*(.*?)\]\]\s*$/);
    if (m && !blk) { flush(); blk = { kind: m[1], head: m[2], lines: [] }; continue; }
    if (blk && /^\s*\[\[\/\]\]\s*$/.test(line)) { out.push(richBlock(blk.kind, blk.head, blk.lines)); blk = null; continue; }
    (blk ? blk.lines : buf).push(line);
  }
  if (blk) out.push(richBlock(blk.kind, blk.head, blk.lines));
  flush();
  return `<div class="rich">${out.join('')}</div>`;
}

const BANK_PREFIX = 'bank-';
function bankTasks(s, did) {
  return s.bank.filter((w) => !did || w.dzial === did).flatMap((w, i) => {
    const wz = { ...w, nr: String(i + 1) };
    return w.zadania.map((z) => ({ ...z, arkusz: BANK_PREFIX + w.id, wiazka: wz }));
  });
}

// Materiał źródłowy: przepisany w aplikacji albo (historia) link do właściwej strony arkusza CKE.
const linkMaterial = (w) => w.link && !w.material
  ? `<a class="card material-link" href="${esc(w.link)}" target="_blank" rel="noopener">${ICONS.exam}<span><strong>Materiał źródłowy w arkuszu CKE</strong><small>${w.tytul ? esc(w.tytul) + ' · ' : ''}otwórz PDF${w.strona ? `, s. ${w.strona}` : ''}</small></span>${ICONS.next}</a>` : '';

function renderTask() {
  const { s, list, i, title } = zs;
  document.body.classList.add('in-session');
  const z = list[i];
  const w = z.wiazka;
  const a = s.arkusze.find((x) => x.id === z.arkusz) || { nazwa: 'Zadanie autorskie IndexLab', zrodlo: w.zrodlo };
  const k = taskKey(s.id, z);
  const prev = store.get().zadania[k];
  const revealed = zs.revealed[k];

  app.innerHTML = `
    <div class="session-top">
      <a class="icon-btn" href="#/matura/${{ a: 'cke', b: 'dzialy', d: 'dzialy' }[zs.key.split('/')[1]] || 'proba'}" aria-label="Zamknij">${ICONS.close}</a>
      <div class="session-progress">${progressBar((i + 1) / list.length, 'Postęp')}</div>
      <span class="session-count">${i + 1}/${list.length}</span>
    </div>
    <p class="eyebrow">${esc(title)}${title !== a.nazwa ? ` · ${esc(a.nazwa)}` : ''}</p>
    <h1 class="task-title">Zadanie ${esc(z.nr)} <span class="muted">(0–${z.punkty} pkt)</span>${prev ? ` <span class="tag tag-ok">${prev.pkt}/${prev.max} pkt</span>` : ''}</h1>

    ${linkMaterial(w)}
    ${w.material || w.uwaga ? `<details class="card material" ${i === 0 || list[i - 1].wiazka !== w ? 'open' : ''}>
      <summary>Materiał do zadania ${esc(w.nr)}${w.tytul ? ` — ${esc(w.tytul)}` : ''}</summary>
      ${w.uwaga ? `<p class="note">${esc(w.uwaga)}</p>` : ''}
      ${w.material ? rich(w.material) : ''}
    </details>` : ''}

    <section class="card task-body">
      ${pre(z.polecenie)}
      <label class="answer-label" for="draft">Twoja odpowiedź <span class="muted">(opcjonalnie, nie jest zapisywana)</span></label>
      <textarea id="draft" rows="4" placeholder="Zapisz odpowiedź, zanim zajrzysz do klucza…">${esc(zs.drafts[k] || '')}</textarea>
    </section>

    <div id="key-area">${revealed ? keyHtml(z, prev) : `<button type="button" class="btn btn-primary btn-lg" id="reveal">Sprawdź z kluczem</button>`}</div>

    <div class="task-nav">
      <button type="button" class="btn btn-ghost" id="prev" ${i === 0 ? 'disabled' : ''}>${ICONS.back}<span>Poprzednie</span></button>
      <button type="button" class="btn btn-ghost" id="nextT" ${i === list.length - 1 ? 'disabled' : ''}><span>Następne</span>${ICONS.next}</button>
    </div>
    <div class="center">${reportBtn(reportTaskHref(s, a, z))}</div>
    ${a.zrodlo ? `<p class="muted center small">${esc(a.zrodlo)}</p>` : ''}
  `;

  const draft = app.querySelector('#draft');
  draft.addEventListener('input', () => (zs.drafts[k] = draft.value));
  app.querySelector('#reveal')?.addEventListener('click', () => {
    zs.revealed[k] = true;
    app.querySelector('#key-area').innerHTML = keyHtml(z, prev);
    bindScore(z, k);
    app.querySelector('#key-area').scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
  if (revealed) bindScore(z, k);
  app.querySelector('#prev').addEventListener('click', () => go(-1));
  app.querySelector('#nextT').addEventListener('click', () => go(1));
  keyHandler = (e) => {
    if (e.key === 'ArrowLeft') go(-1);
    if (e.key === 'ArrowRight') go(1);
  };
}

function keyHtml(z, prev) {
  const ark = zs?.s?.arkusze?.find((x) => x.id === z.arkusz);
  const label = String(z.arkusz).startsWith(BANK_PREFIX) ? 'Przykładowa odpowiedź (klucz IndexLab)'
    : ark?.link ? 'Wzorcowa odpowiedź (opracowanie IndexLab na podstawie zasad CKE)' : 'Odpowiedź według klucza CKE';
  const btns = Array.from({ length: z.punkty + 1 }, (_, p) =>
    `<button type="button" class="btn btn-score ${prev && prev.pkt === p ? 'active' : ''}" data-pkt="${p}">${p} pkt</button>`).join('');
  return `<section class="card key">
      <h2 class="card-title">${ICONS.check} ${label}</h2>
      ${pre(z.odpowiedz || '—')}
      ${z.omowienie ? `<div class="omowienie"><strong>Omówienie</strong>${pre(z.omowienie)}</div>` : ''}
      ${z.zasady ? `<details class="rules"><summary>Jak to jest punktowane</summary>${pre(z.zasady)}</details>` : ''}
      ${ark?.linkZasady ? `<a class="small" href="${esc(ark.linkZasady)}" target="_blank" rel="noopener">Oficjalne zasady oceniania CKE (PDF)</a>` : ''}
    </section>
    <p class="score-q">Ile punktów przyznajesz sobie?</p>
    <div class="score-row">${btns}</div>`;
}

function bindScore(z, k) {
  app.querySelector('.score-row').addEventListener('click', (e) => {
    const b = e.target.closest('[data-pkt]');
    if (!b) return;
    const first = !store.get().zadania[k];
    store.get().zadania[k] = { pkt: Number(b.dataset.pkt), max: z.punkty, at: Date.now() };
    store.markActivity();
    game.award(first ? 2 + Number(b.dataset.pkt) * 2 : 0, { zadania: first ? 1 : 0 });
    toast(`Zapisano: ${b.dataset.pkt}/${z.punkty} pkt`);
    if (zs.i < zs.list.length - 1) go(1);
    else renderTask();
  });
}

function go(d) {
  const n = zs.i + d;
  if (n < 0 || n >= zs.list.length) return;
  zs.i = n;
  renderTask();
  window.scrollTo({ top: 0 });
}

// ---------- próbna matura ----------
const EXAM_MIN = 180;
const DEFAULT_WAGI = { spoleczenstwo: 9, obywatel: 7, polityka: 3, 'ustroj-rp': 13, 'systemy-panstw': 3, prawo: 2, 'prawa-czlowieka': 2, miedzynarodowe: 5, ue: 2 };

function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const seededShuffle = (arr, r) => {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
};
const wPts = (w) => w.zadania.reduce((n, z) => n + z.punkty, 0);
const isExt = (w) => w.zadania.length === 1 && w.zadania[0].punkty >= 5;

// Wiązki z arkuszy CKE w tym samym formacie co bank autorski.
function ckeWiazki(s) {
  return s.arkusze.flatMap((a) => a.wiazki.map((w) => {
    const c = {};
    w.zadania.forEach((z) => z.dzialy.forEach((d) => (c[d] = (c[d] || 0) + z.punkty)));
    const dzial = Object.keys(c).sort((x, y) => c[y] - c[x])[0] || 'spoleczenstwo';
    return { ...w, id: `cke-${a.id}-${w.nr}`, dzial, zrodlo: `CKE — ${a.nazwa}, zadanie ${w.nr}`, autorskie: false };
  }));
}

function examPool(s, cke) {
  return [...s.bank, ...(cke ? ckeWiazki(s) : [])];
}

// Układa arkusz w formule od 2026 r.: ok. 43 pkt w krótkich wiązkach (proporcje działów jak w arkuszach CKE 2026)
// + jedno zadanie rozszerzonej odpowiedzi za 7 pkt — razem ok. 50 pkt.
const SHORT_PTS = 43;
function buildExam(s, seed, cke) {
  const r = rng(seed);
  const pool = examPool(s, cke);
  const shortW = pool.filter((w) => !isExt(w));
  const ext7 = seededShuffle(pool.filter((w) => isExt(w) && wPts(w) >= 6), r);
  const wagi = s.wagi || DEFAULT_WAGI;
  const sum = Object.values(wagi).reduce((a, b) => a + b, 0);
  const byD = {};
  seededShuffle(shortW, r).forEach((w) => (byD[w.dzial] ||= []).push(w));
  const quota = {};
  Object.keys(wagi).forEach((d) => (quota[d] = (wagi[d] / sum) * SHORT_PTS));
  const picked = [];
  let total = 0;
  let progress = true;
  while (total < SHORT_PTS - 1 && progress) {
    progress = false;
    for (const d of seededShuffle(Object.keys(wagi), r)) {
      if (total >= SHORT_PTS) break;
      const list = byD[d] || [];
      if (!list.length || quota[d] <= 0.5) continue;
      const w = list.shift();
      picked.push(w); total += wPts(w); quota[d] -= wPts(w); progress = true;
    }
  }
  if (total < SHORT_PTS - 1) { // brak zadań w części działów — dobierz z dowolnych
    const rest = Object.values(byD).flat();
    while (total < SHORT_PTS - 1 && rest.length) { const w = rest.shift(); picked.push(w); total += wPts(w); }
  }
  const order = s.dzialy.map((d) => d.id);
  picked.sort((a, b) => order.indexOf(a.dzial) - order.indexOf(b.dzial));
  const ext = [ext7[0]].filter(Boolean);
  return [...picked, ...ext].map((w) => w.id);
}

function examById(s, ids, cke) {
  const pool = examPool(s, true);
  const m = new Map(pool.map((w) => [w.id, w]));
  return ids.map((id) => m.get(id)).filter(Boolean);
}

const examMax = (ws) => ws.reduce((n, w) => n + wPts(w), 0);
const fmtTime = (ms) => {
  const t = Math.max(0, Math.round(ms / 1000));
  const h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), sec = t % 60;
  return `${h}:${String(m).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
};

function examSection(s) {
  const st = store.get().egzaminy;
  const cke = store.get().settings.examCke !== false;
  const nBank = s.bank.length;
  const mine = Object.values(st).filter((e) => e.sid === s.id).sort((a, b) => b.start - a.start);
  const numbered = Array.from({ length: 12 }, (_, i) => i + 1);
  const res = (e) => (e && e.koniec && e.ocena ? `${e.ocena.pkt}/${e.ocena.max} pkt` : e ? 'w trakcie' : '');
  return `<section class="card exam-card">
    <h2 class="card-title">Próbna matura</h2>
    <ul class="exam-facts">
      <li><b>180</b><span>minut</span></li>
      <li><b>~50</b><span>punktów</span></li>
      <li><b>${(s.bank.reduce((n, w) => n + w.zadania.length, 0) + (cke ? tasksOf(s).length : 0)).toLocaleString('pl-PL')}</b><span>zadań w puli</span></li>
    </ul>
    <p class="muted small">Układ jak na prawdziwym arkuszu: wiązki ze wszystkich działów i na końcu wypracowanie.</p>
    <label class="switch"><input type="checkbox" id="exam-cke" ${cke ? 'checked' : ''}> <span>Dobieraj też zadania z arkuszy CKE</span></label>
    <button type="button" class="btn btn-gold btn-lg" id="exam-random">Losowa próbna matura</button>
    <h3 class="sub-title">Ponumerowane próbne matury</h3>
    <div class="exam-grid">${numbered.map((n) => {
      const e = st[`${s.id}-nr${n}-${cke ? 'c' : 'a'}-26`];
      return `<a class="exam-tile ${e?.koniec ? 'done' : e ? 'open' : ''}" href="#/egzamin/${enc(s.id)}/${enc(`nr${n}-${cke ? 'c' : 'a'}-26`)}"><strong>${n}</strong><span>${res(e) || 'rozpocznij'}</span></a>`;
    }).join('')}</div>
    ${mine.length ? `<h3 class="sub-title">Twoje podejścia</h3><ul class="test-list">${mine.slice(0, 8).map((e) => `<li><div><strong>${esc(e.nazwa)}</strong><span>${new Date(e.start).toLocaleString('pl-PL', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}</span></div>
      <a class="score ${e.koniec ? (e.ocena.pkt / e.ocena.max >= .7 ? 'ok' : e.ocena.pkt / e.ocena.max >= .4 ? 'warn' : 'bad') : ''}" href="#/egzamin/${enc(s.id)}/${enc(e.key)}">${e.koniec ? pct(e.ocena.pkt / e.ocena.max) + '%' : 'wróć'}</a></li>`).join('')}</ul>` : ''}
    ${nBank ? '' : '<p class="note">Baza zadań autorskich jest w przygotowaniu — próbne matury korzystają teraz z zadań CKE.</p>'}
  </section>`;
}

function bindExamSection(s) {
  app.querySelector('#exam-cke')?.addEventListener('change', (e) => {
    store.get().settings.examCke = e.target.checked; store.save(); viewMatura();
  });
  app.querySelector('#exam-random')?.addEventListener('click', () => {
    const cke = store.get().settings.examCke !== false;
    const key = `los-${Date.now().toString(36)}`;
    createExam(s, key, Math.floor(Math.random() * 1e9), cke, 'Losowa próbna matura');
    location.hash = `#/egzamin/${enc(s.id)}/${enc(key)}`;
  });
}

function createExam(s, key, seed, cke, nazwa) {
  const ids = buildExam(s, seed, cke);
  const e = { key, sid: s.id, nazwa, seed, cke, ids, start: Date.now(), koniec: null, odp: {}, pkt: {}, i: 0 };
  store.get().egzaminy[`${s.id}-${key}`] = e;
  store.save();
  return e;
}

let examTimer = null;

function viewEgzamin(sid, key) {
  const s = findSubject(sid);
  if (!s) return notFound();
  let e = store.get().egzaminy[`${sid}-${key}`];
  if (!e) {
    const m = key.match(/^nr(\d+)-(c|a)(?:-26)?$/);
    if (!m) return notFound();
    const n = Number(m[1]);
    e = createExam(s, key, 1000 + n * 7919, m[2] === 'c', `Matura próbna nr ${n}${m[2] === 'a' ? ' (autorska)' : ''}`);
  }
  const ws = examById(s, e.ids);
  if (!ws.length) return notFound();
  if (e.koniec) return renderExamResult(s, e, ws);
  renderExamTask(s, e, ws);
}

function renderExamTask(s, e, ws) {
  document.body.classList.add('in-session');
  const w = ws[e.i] || ws[0];
  const left = e.start + EXAM_MIN * 60000 - Date.now();
  app.innerHTML = `
    <div class="session-top exam-top">
      <a class="icon-btn" href="#/matura" aria-label="Wyjdź (postęp zostaje zapisany)">${ICONS.close}</a>
      <div class="exam-clock ${left < 15 * 60000 ? 'late' : ''}" id="clock" aria-live="off">${fmtTime(left)}</div>
      <button type="button" class="btn btn-sm btn-gold" id="finish">Zakończ</button>
    </div>
    <nav class="exam-strip" aria-label="Zadania">${ws.map((x, i) => {
      const done = x.zadania.some((z) => (e.odp[`${x.id}/${z.nr}`] || '').trim());
      return `<button type="button" class="${i === e.i ? 'cur' : ''} ${done ? 'done' : ''}" data-i="${i}">${i + 1}</button>`;
    }).join('')}</nav>
    <p class="eyebrow">${esc(e.nazwa)} · wiązka ${e.i + 1} z ${ws.length} · ${wPts(w)} pkt</p>
    <section class="card material">
      <h2 class="card-title">${esc(w.tytul || 'Zadanie ' + (e.i + 1))}</h2>
      ${w.uwaga ? `<p class="note">${esc(w.uwaga)}</p>` : ''}
      ${w.material ? rich(w.material) : ''}
      ${linkMaterial(w)}
      <p class="muted small">${esc(w.zrodlo)}</p>
    </section>
    ${w.zadania.map((z, j) => `<section class="card task-body">
      <p class="eyebrow">Zadanie ${e.i + 1}.${j + 1} · 0–${z.punkty} pkt</p>
      ${pre(z.polecenie)}
      <textarea data-k="${esc(`${w.id}/${z.nr}`)}" rows="${z.punkty >= 5 ? 14 : 4}" aria-label="Odpowiedź do zadania ${e.i + 1}.${j + 1}" placeholder="Twoja odpowiedź…">${esc(e.odp[`${w.id}/${z.nr}`] || '')}</textarea>
    </section>`).join('')}
    <div class="task-nav">
      <button type="button" class="btn btn-ghost" id="prev" ${e.i === 0 ? 'disabled' : ''}>${ICONS.back}<span>Poprzednia</span></button>
      <button type="button" class="btn btn-ghost" id="nextW" ${e.i === ws.length - 1 ? 'disabled' : ''}><span>Następna</span>${ICONS.next}</button>
    </div>
    <div id="finish-confirm"></div>`;

  let saveT;
  app.querySelectorAll('textarea[data-k]').forEach((t) => t.addEventListener('input', () => {
    e.odp[t.dataset.k] = t.value;
    clearTimeout(saveT); saveT = setTimeout(() => store.save(), 400);
  }));
  const goW = (i) => { store.save(); e.i = Math.max(0, Math.min(ws.length - 1, i)); store.save(); renderExamTask(s, e, ws); window.scrollTo({ top: 0 }); };
  app.querySelector('.exam-strip').addEventListener('click', (ev) => { const b = ev.target.closest('[data-i]'); if (b) goW(Number(b.dataset.i)); });
  app.querySelector('#prev').addEventListener('click', () => goW(e.i - 1));
  app.querySelector('#nextW').addEventListener('click', () => goW(e.i + 1));
  app.querySelector('#finish').addEventListener('click', () => {
    const box = app.querySelector('#finish-confirm');
    const answered = ws.flatMap((x) => x.zadania.map((z) => (e.odp[`${x.id}/${z.nr}`] || '').trim())).filter(Boolean).length;
    const all = ws.reduce((n, x) => n + x.zadania.length, 0);
    box.innerHTML = `<section class="card key"><h2 class="card-title">Zakończyć egzamin?</h2>
      <p>Odpowiedzi: ${answered} z ${all}. Po zakończeniu zobaczysz klucz i ocenisz swoje odpowiedzi.</p>
      <div class="actions"><button type="button" class="btn btn-primary btn-lg" id="finish-yes">Zakończ i sprawdź</button>
      <button type="button" class="btn btn-ghost btn-lg" id="finish-no">Wróć do pisania</button></div></section>`;
    box.scrollIntoView({ behavior: 'smooth' });
    box.querySelector('#finish-no').onclick = () => (box.innerHTML = '');
    box.querySelector('#finish-yes').onclick = () => finishExam(s, e, ws);
  });
  clearInterval(examTimer);
  examTimer = setInterval(() => {
    const c = document.getElementById('clock');
    if (!c) return clearInterval(examTimer);
    const l = e.start + EXAM_MIN * 60000 - Date.now();
    c.textContent = fmtTime(l);
    c.classList.toggle('late', l < 15 * 60000);
    if (l <= 0) { clearInterval(examTimer); toast('Czas minął — egzamin zakończony.'); finishExam(s, e, ws); }
  }, 1000);
}

function finishExam(s, e, ws) {
  clearInterval(examTimer);
  e.koniec = Date.now();
  e.i = 0;
  e.ocena = { pkt: 0, max: examMax(ws) };
  store.markActivity();
  game.award(30);
  renderExamResult(s, e, ws);
  window.scrollTo({ top: 0 });
}

function renderExamResult(s, e, ws) {
  document.body.classList.add('in-session');
  const max = examMax(ws);
  const pktSum = Object.values(e.pkt).reduce((a, b) => a + b, 0);
  e.ocena = { pkt: pktSum, max };
  const graded = ws.flatMap((w) => w.zadania.map((z) => `${w.id}/${z.nr}`)).filter((k) => e.pkt[k] !== undefined).length;
  const all = ws.reduce((n, w) => n + w.zadania.length, 0);
  const byD = {};
  ws.forEach((w) => w.zadania.forEach((z) => {
    const d = (byD[w.dzial] ||= { pkt: 0, max: 0 });
    d.max += z.punkty; d.pkt += e.pkt[`${w.id}/${z.nr}`] || 0;
  }));
  const p = max ? pct(pktSum / max) : 0;
  const czas = Math.round((e.koniec - e.start) / 60000);
  app.innerHTML = `
    <div class="session-top"><a class="icon-btn" href="#/matura" aria-label="Zamknij">${ICONS.close}</a></div>
    <section class="result">
      <div class="ring ring-xl ${p >= 70 ? 'ring-ok' : p >= 40 ? 'ring-warn' : 'ring-bad'}" style="--p:${p}"><span>${p}%</span></div>
      <h1>${esc(e.nazwa)}</h1>
      <p class="lead"><strong>${pktSum} z ${max} pkt</strong> · czas pisania: ${czas} min · ocenione: <span id="graded">${graded}</span>/${all}</p>
      ${s.srednia ? `<p class="muted">Średni wynik w kraju (${esc(s.srednia.rok)}): ${s.srednia.procent}%</p>` : ''}
    </section>
    <section class="card"><h2 class="card-title">Wynik w działach</h2>
      ${s.dzialy.filter((d) => byD[d.id]).map((d) => `<div class="stat-row"><div class="stat-row-top"><span>${esc(d.nazwa)}</span><strong>${byD[d.id].pkt}/${byD[d.id].max}</strong></div>${progressBar(byD[d.id].pkt / byD[d.id].max, d.nazwa)}</div>`).join('')}
    </section>
    <h2 class="section-title">Sprawdź z kluczem i przyznaj punkty</h2>
    <div class="review-list">${ws.map((w, i) => w.zadania.map((z, j) => {
      const k = `${w.id}/${z.nr}`;
      return `<article class="card review" data-k="${esc(k)}">
        <p class="eyebrow">Zadanie ${i + 1}.${j + 1} · ${esc(w.tytul)} · 0–${z.punkty} pkt</p>
        ${pre(z.polecenie)}
        <div class="exam-answer"><strong>Twoja odpowiedź</strong>${pre(e.odp[k] || '— brak —')}</div>
        <div class="exam-key"><strong>${ICONS.check} Klucz</strong>${pre(z.odpowiedz || '—')}
          ${z.zasady ? `<details class="rules"><summary>Zasady oceniania</summary>${pre(z.zasady)}</details>` : ''}</div>
        <div class="score-row">${Array.from({ length: z.punkty + 1 }, (_, q) => `<button type="button" class="btn btn-score ${e.pkt[k] === q ? 'active' : ''}" data-pkt="${q}" data-max="${z.punkty}">${q} pkt</button>`).join('')}</div>
        <div class="review-foot"><span class="source">${esc(w.zrodlo)}</span>${reportBtn(mailto(`[IndexLab] Błąd w zadaniu: ${w.id}/${z.nr}`, ['Dzień dobry,', '', `zgłaszam błąd w zadaniu ${w.id}/${z.nr} (${w.zrodlo}).`, '', `Polecenie: ${z.polecenie}`, '', `Klucz: ${z.odpowiedz}`, '', 'Na czym polega błąd:', '']))}</div>
      </article>`;
    }).join('')).join('')}</div>
    <div class="actions"><a class="btn btn-ghost btn-lg" href="#/matura">Wróć do listy próbnych matur</a></div>`;

  app.querySelector('.review-list').addEventListener('click', (ev) => {
    const b = ev.target.closest('[data-pkt]');
    if (!b) return;
    const k = b.closest('[data-k]').dataset.k;
    e.pkt[k] = Number(b.dataset.pkt);
    b.parentElement.querySelectorAll('.btn-score').forEach((x) => x.classList.toggle('active', x === b));
    const sum = Object.values(e.pkt).reduce((a, c) => a + c, 0);
    e.ocena = { pkt: sum, max };
    store.save();
    const g = app.querySelector('#graded');
    if (g) g.textContent = Object.keys(e.pkt).length;
    const lead = app.querySelector('.result .lead strong');
    if (lead) lead.textContent = `${sum} z ${max} pkt`;
    const ring = app.querySelector('.result .ring');
    if (ring) { const pp = pct(sum / max); ring.style.setProperty('--p', pp); ring.querySelector('span').textContent = pp + '%'; }
  });
}

// ---------- zakładka „Aktualności” ----------
let newsQ = '';
let newsSec = '';
function viewAktualnosci() {
  const s = currentSubject();
  const A = s?.aktualnosci;
  if (!A) return notFound();
  const q = norm(newsQ);
  const ALIAS = { rpo: 'rzecznik praw obywatelskich', rpd: 'rzecznik praw dziecka', sn: 'sadu najwyzszego', tk: 'trybunalu konstytucyjnego', sg: 'sekretarz generalny', ke: 'komisji europejskiej', pe: 'parlamentu europejskiego', rm: 'rady ministrow', nbp: 'nbp' };
  const match = (row) => { const txt = norm(row.join(' ')); return !q || q.split(' ').every((w) => txt.includes(w) || (ALIAS[w] && txt.includes(ALIAS[w]))); };
  const all = A.sekcje.map((sec, i) => ({ sec, rows: sec.wiersze.filter(match), i }));
  if (!A.sekcje.some((x) => x.id === newsSec)) newsSec = A.sekcje[0].id;
  const sections = q ? all.filter((x) => x.rows.length) : all.filter((x) => x.sec.id === newsSec);
  const withDate = (t) => { const m = String(t).match(/^(.*?)\s*\(([^)]+)\)$/); return m ? [m[1], m[2]] : [t, '']; };
  const body = (sec, rows) => {
    const k = sec.kolumny || [];
    if (k[2] === 'Jest') return `<div class="nw-changes">${rows.map((r) => { const [who, when] = withDate(r[2]); return `<article class="nw-change">
        <div class="nw-role">${esc(r[0])}${when ? `<span class="nw-date">${esc(when)}</span>` : ''}</div>
        <div class="nw-now">${esc(who)}</div>
        <div class="nw-was"><span>wcześniej</span> ${esc(r[1])}</div></article>`; }).join('')}</div>`;
    if (k[0] === 'Data') return `<ol class="nw-time">${rows.map((r) => `<li><time>${esc(r[0])}</time><p>${esc(r[1])}</p></li>`).join('')}</ol>`;
    return `<ul class="nw-people">${rows.map((r) => { const [who, extra] = k[2] ? [r[1], r[2]] : withDate(r[1]); return `<li>
        <span class="nw-role">${esc(r[0])}</span><strong>${esc(who)}</strong>${extra ? `<small>${k[2] === 'Od' && /^[0-9IVX]/.test(extra) ? 'od ' : ''}${esc(extra)}</small>` : ''}</li>`; }).join('')}</ul>`;
  };
  app.innerHTML = `
    ${pageHead(A.nazwa || 'Aktualności', null)}
    <p class="news-meta">${A.stan ? `<span class="nw-pill">Stan na ${esc(A.stan)}</span>` : ''} ${esc(A.podtytul || 'Kto jest kim i najważniejsze wydarzenia')}</p>
    <input class="type-input search-input" id="news-q" type="search" autocomplete="off" placeholder="${esc(A.szukaj || 'Szukaj: RPO, Węgry, MTK…')}" aria-label="Szukaj w aktualnościach" value="${esc(newsQ)}">
    ${q ? '' : `<nav class="nw-chips" aria-label="Sekcje">${A.sekcje.map((x) => `<button type="button" class="nw-chip ${x.id === newsSec ? 'on' : ''}" data-sec="${esc(x.id)}" aria-pressed="${x.id === newsSec}">${esc(x.tytul)}</button>`).join('')}</nav>`}
    <div class="news">${sections.map(({ sec, rows }) => `<section class="nw-sec">
        ${q ? `<h2 class="nw-title">${esc(sec.tytul)}<small>${rows.length}</small></h2>` : ''}
        ${body(sec, rows)}
        ${!q && sec.notatki ? sec.notatki.map((n) => `<p class="nw-note"><b>Warto wiedzieć</b>${esc(n)}</p>`).join('') : ''}
      </section>`).join('') || '<p class="muted">Nic nie znaleziono.</p>'}</div>
    ${A.uwaga || A.zrodlo ? `<p class="muted small news-foot">${esc(A.uwaga || '')}${A.zrodlo ? ` Źródło: ${esc(A.zrodlo)}.` : ''}</p>` : ''}`;
  app.querySelectorAll('.nw-chip').forEach((b) => b.addEventListener('click', () => {
    newsSec = b.dataset.sec; viewAktualnosci();
    app.querySelector('.nw-chip.on')?.scrollIntoView({ inline: 'center', block: 'nearest' });
  }));
  const inp = app.querySelector('#news-q');
  let tm;
  inp.addEventListener('input', () => { clearTimeout(tm); tm = setTimeout(() => { newsQ = inp.value; const pos = inp.selectionStart; viewAktualnosci(); const n = app.querySelector('#news-q'); n.focus(); n.setSelectionRange(pos, pos); }, 200); });
}

// ---------- profil, logowanie i wybór przedmiotu ----------
const initials = (n) => (String(n).trim().split(/\s+/).map((w) => w[0]).join('').slice(0, 2) || '?').toUpperCase();
const avatar = (p, big) => p.photo
  ? `<span class="avatar avatar-photo ${big ? 'avatar-lg' : ''}" aria-hidden="true"><img src="${esc(p.photo)}" alt=""></span>`
  : `<span class="avatar ${big ? 'avatar-lg' : ''}" style="--av:${esc(p.color)}" aria-hidden="true">${esc(initials(p.name))}</span>`;

// Zdjęcie profilowe: przycinane do kwadratu i zmniejszane do 160 px (kilka KB), zapisane tylko na urządzeniu.
function zdjecieDoDataUrl(file) {
  return new Promise((resolve, reject) => {
    const url = URL.createObjectURL(file);
    const img = new Image();
    img.onload = () => {
      const k = Math.min(img.width, img.height), size = 160;
      const c = document.createElement('canvas'); c.width = c.height = size;
      c.getContext('2d').drawImage(img, (img.width - k) / 2, (img.height - k) / 2, k, k, 0, 0, size, size);
      URL.revokeObjectURL(url);
      resolve(c.toDataURL('image/jpeg', 0.82));
    };
    img.onerror = () => { URL.revokeObjectURL(url); reject(new Error('Nie udało się wczytać zdjęcia.')); };
    img.src = url;
  });
}
function bindAvatarUpload() {
  app.querySelector('#avatar-file')?.addEventListener('change', async (e) => {
    const f = e.target.files?.[0];
    if (!f) return;
    if (!f.type.startsWith('image/')) return toast('Wybierz plik ze zdjęciem.');
    try { store.setPhoto(store.activeProfile().id, await zdjecieDoDataUrl(f)); toast('Zdjęcie profilowe zmienione.'); viewSettings(); updateTopStats(); }
    catch (err) { toast(err.message); }
  });
  app.querySelector('[data-act="photo-del"]')?.addEventListener('click', () => { store.setPhoto(store.activeProfile().id, null); viewSettings(); });
}
const SUBJECT_ICONS = {
  wos: '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6 6 15v3h36v-3z" fill="currentColor"/><path d="M10 21h4v15h-4zM18 21h4v15h-4zM26 21h4v15h-4zM34 21h4v15h-4z" fill="currentColor" opacity=".85"/><path d="M6 38h36v4H6z" fill="currentColor"/></svg>',
};
SUBJECT_ICONS.historia = '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M14 6h20v6a10 10 0 0 1-10 10A10 10 0 0 1 14 12zM14 42h20v-6a10 10 0 0 0-10-10 10 10 0 0 0-10 10z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M10 5h28M10 43h28" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M18 40c1-4 3-6 6-6s5 2 6 6z" fill="currentColor"/></svg>';
SUBJECT_ICONS.filozofia = '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 7c-8 0-13 5-13 12 0 5 3 8 6 10v6h14v-6c3-2 6-5 6-10 0-7-5-12-13-12z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M18 40h12M20 44h8" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M24 16v10M20 20h8" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/></svg>';
const subjectIcon = (s) => SUBJECT_ICONS[s.id] || `<span class="subj-letters">${esc((s.skrot || s.nazwa).slice(0, 3))}</span>`;
let gateMsg = '';

function afterProfileChange() {
  session = test = zs = lesson = null;
  applyTheme();
  updateTopStats();
  if (dostep.wlaczone()) zaladujTresci().then(route).catch((e) => toast(e.message)); // inne konto = inny dostęp
}

// Ekran logowania: wybór profilu na urządzeniu albo logowanie e-mailem (gdy konta są włączone).
function viewKonto() {
  document.body.classList.add('in-gate');
  const list = store.profileList();
  app.innerHTML = `<section class="gate">
    <div class="gate-brand">${BRAND_NAME}<span class="eyebrow">Matura rozszerzona · kursy autorskie</span></div>
    <h1 class="gate-title">Kto się uczy?</h1>
    <div class="who">${list.map((p) => `<button type="button" class="who-item" data-pid="${esc(p.id)}">${avatar(p, true)}<span>${esc(p.name)}</span></button>`).join('')}
      <button type="button" class="who-item" data-act="new"><span class="avatar avatar-lg avatar-add" aria-hidden="true">+</span><span>Nowy</span></button></div>
    <form class="gate-form" id="new-form" hidden>
      <input class="type-input" name="name" maxlength="30" placeholder="Imię" aria-label="Imię" autocomplete="given-name" required>
      <button type="submit" class="btn btn-primary btn-lg">Utwórz profil</button>
    </form>
    ${cloud.enabled() ? `<button type="button" class="link-btn" data-act="email">Zaloguj się e-mailem</button>
    <form class="gate-form" id="acc-form" hidden novalidate>
      <input class="type-input" name="email" type="email" autocomplete="email" placeholder="E-mail" aria-label="E-mail">
      <input class="type-input" name="pass" type="password" autocomplete="current-password" placeholder="Hasło" aria-label="Hasło">
      <button type="submit" class="btn btn-primary btn-lg" data-mode="in">Zaloguj się</button>
      <button type="submit" class="link-btn" data-mode="up">Nie mam konta — załóż</button>
    </form>` : ''}
    ${gateMsg ? `<p class="acc-msg" role="status">${esc(gateMsg)}</p>` : ''}
  </section>`;
  gateMsg = '';
  const enter = (id) => { store.login(id); afterProfileChange(); location.hash = '#/przedmiot'; if (location.hash === '#/przedmiot') route(); };
  app.querySelector('.who').addEventListener('click', (e) => {
    const b = e.target.closest('[data-pid]');
    if (b) return enter(b.dataset.pid);
    if (e.target.closest('[data-act="new"]')) { const f = app.querySelector('#new-form'); f.hidden = false; f.name.focus(); }
  });
  app.querySelector('#new-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = e.target.name.value.trim();
    if (!name) return;
    enter(store.createProfile(name).id);
  });
  app.querySelector('[data-act="email"]')?.addEventListener('click', () => { const f = app.querySelector('#acc-form'); f.hidden = false; f.email.focus(); });
  const form = app.querySelector('#acc-form');
  if (form) {
    let mode = 'in';
    form.querySelectorAll('[data-mode]').forEach((b) => b.addEventListener('click', () => (mode = b.dataset.mode)));
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = form.email.value.trim().toLowerCase();
      const pass = form.pass.value;
      const fail = (m) => { gateMsg = m; viewKonto(); };
      if (!/^\S+@\S+\.\S+$/.test(email)) return fail('Podaj poprawny adres e-mail.');
      if (pass.length < 6) return fail('Hasło musi mieć co najmniej 6 znaków.');
      form.querySelectorAll('button').forEach((b) => (b.disabled = true));
      const prev = store.activeProfile().id;
      const p = store.profileList().find((x) => x.cloud?.email === email) || store.createProfile(email.split('@')[0]);
      store.switchProfile(p.id);
      try {
        if (mode === 'up') {
          const r = await cloud.signUp(email, pass);
          if (r.confirm) { store.switchProfile(prev); return fail('Kliknij link w wiadomości e-mail, a potem zaloguj się.'); }
        } else await cloud.signIn(email, pass);
        enter(p.id);
      } catch (err) {
        if (!p.cloud && !store.get().updatedAt) store.deleteProfile(p.id);
        store.switchProfile(prev);
        fail(err.message);
      }
    });
  }
}

// Wybór przedmiotu — po każdym zalogowaniu i po dotknięciu ikony przedmiotu w górnym pasku.
function viewPrzedmiot() {
  document.body.classList.add('in-gate');
  const cur = store.get().settings.przedmiot;
  app.innerHTML = `<section class="gate">
    <div class="gate-who">${avatar(store.activeProfile())}<span>${esc(store.activeProfile().name)}</span></div>
    <h1 class="gate-title">Twoje kursy</h1>
    <div class="subj-grid">${subjects.map((s) => `<button type="button" class="subj-tile ${s.id === cur ? 'active' : ''}" data-sid="${esc(s.id)}" aria-label="${esc(s.nazwa)}">
        <span class="subj-icon">${subjectIcon(s)}</span><span class="subj-name">${esc(s.skrot || s.nazwa)}</span></button>`).join('')}</div>
    <button type="button" class="link-btn" data-act="logout">Zmień profil</button>
  </section>`;
  app.querySelector('.subj-grid').addEventListener('click', (e) => {
    const b = e.target.closest('[data-sid]');
    if (!b) return;
    const st = store.get().settings;
    st.przedmiot = b.dataset.sid;
    store.save();
    game.sound('tap');
    const wroc = wrocPoWyborze; wrocPoWyborze = null;
    location.hash = st.plan?.[b.dataset.sid] ? (wroc || '#/') : '#/plan';
  });
  app.querySelector('[data-act="logout"]').addEventListener('click', () => { store.logout(); location.hash = '#/konto'; });
}

function profileHeadHtml() {
  const prof = store.activeProfile();
  const acc = cloud.account();
  const st = store.streak();
  return `<section class="profile-head">
    ${avatar(prof, true)}
    <div class="profile-meta"><h1>${esc(prof.name)}</h1><span class="muted">${acc ? esc(acc.email) : 'Profil na tym urządzeniu'}</span>
      <div class="lv-row">${ICONS.flame}<b>${st.current} ${plural(st.current, 'dzień', 'dni', 'dni')} nauki z rzędu</b><small>najdłuższa seria: ${st.longest}</small></div></div>
  </section>`;
}

function connectHtml(open, intro) {
  if (!cloud.enabled() || cloud.account()) return '';
  return `<details class="card connect" ${open ? 'open' : ''}><summary class="card-title">${open ? 'Zaloguj się albo załóż konto' : 'Zapisuj postępy na koncie'}</summary>
    <form class="gate-form" id="acc-form" novalidate>
      <p class="muted small">${intro || 'Zaloguj się, aby mieć te same postępy na każdym urządzeniu.'}</p>
      <input class="type-input" name="email" type="email" autocomplete="email" placeholder="E-mail" aria-label="E-mail">
      <input class="type-input" name="pass" type="password" autocomplete="current-password" placeholder="Hasło (min. 6 znaków)" aria-label="Hasło">
      <button type="submit" class="btn btn-primary btn-lg" data-mode="in">Zaloguj się</button>
      <button type="submit" class="link-btn" data-mode="up">Załóż konto</button>
    </form></details>`;
}

function bindProfil() {
  app.querySelector('[data-act="logout"]').addEventListener('click', async () => {
    store.logout();
    location.hash = '#/konto';
  });
  bindConnect(viewStats);
}

function bindConnect(after) {
  const form = app.querySelector('#acc-form');
  if (form) {
    let mode = 'in';
    form.querySelectorAll('[data-mode]').forEach((b) => b.addEventListener('click', () => (mode = b.dataset.mode)));
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = form.email.value.trim().toLowerCase();
      const pass = form.pass.value;
      if (!/^\S+@\S+\.\S+$/.test(email) || pass.length < 6) return toast('Podaj e-mail i hasło (min. 6 znaków).');
      form.querySelectorAll('button').forEach((b) => (b.disabled = true));
      try {
        if (mode === 'up') { const r = await cloud.signUp(email, pass); if (r.confirm) toast('Kliknij link w wiadomości e-mail, a potem zaloguj się.'); }
        else await cloud.signIn(email, pass);
        afterProfileChange();
        after();
        if (cloud.account()) toast('Połączono z kontem.');
      } catch (err) {
        toast(err.message);
        form.querySelectorAll('button').forEach((b) => (b.disabled = false));
      }
    });
  }
}

// ---------- statystyki ----------
function viewStats() {
  const st = store.streak();
  const state = store.get();
  let mastered = 0, total = 0, seen = 0;
  const per = [];
  let tPkt = 0, tMax = 0, tDone = 0, tAll = 0;
  subjects.forEach((s) => {
    const allowance = newAllowance(s.id);
    s.dzialy.forEach((d) => {
      const sm = summary(s.id, d.poddzialy, allowance);
      mastered += sm.mastered;
      total += sm.total;
      seen += sm.seen;
      per.push({ s, d, sm });
    });
    const ts = taskScore(s.id, tasksOf(s));
    tPkt += ts.pkt; tMax += ts.max; tDone += ts.done; tAll += ts.total;
  });
  const activity = Object.values(state.days).reduce((a, b) => a + b, 0);
  const tests = state.tests.slice(-10).reverse();
  const avg = state.tests.length ? state.tests.reduce((a, t) => a + t.score / t.total, 0) / state.tests.length : null;
  const fmt = new Intl.DateTimeFormat('pl-PL', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' });

  const days = [];
  for (let k = 13; k >= 0; k--) {
    const t = store.addDays(store.startOfDay(), -k);
    days.push({ t, on: !!state.days[store.dayKey(t)] });
  }
  const dfmt = new Intl.DateTimeFormat('pl-PL', { weekday: 'narrow' });

  const week = [];
  for (let k = 6; k >= 0; k--) {
    const t = store.addDays(store.startOfDay(), -k);
    week.push({ t, xp: state.days[store.dayKey(t)] || 0 });
  }
  const wMax = Math.max(game.goal(), ...week.map((w) => w.xp));
  const wfmt = new Intl.DateTimeFormat('pl-PL', { weekday: 'short' });
  app.innerHTML = `
    ${profileHeadHtml()}
    ${premiumCard()}
    <section class="card">
      <h2 class="card-title">Aktywność w tym tygodniu</h2>
      <div class="week" role="list">${week.map((w) => `<div class="week-day ${w.xp >= game.goal() ? 'hit' : ''}" role="listitem" aria-label="${wfmt.format(w.t)}: ${w.xp} odpowiedzi">
        <span class="week-val">${w.xp || ''}</span>
        <div class="week-bar"><span style="height:${Math.round((w.xp / wMax) * 100)}%"></span></div>
        <small>${wfmt.format(w.t).replace('.', '')}</small></div>`).join('')}</div>
      <p class="muted small">Liczba odpowiedzi dziennie. Cel dnia: ${game.goal()} — dni z osiągniętym celem są wyróżnione.</p>
    </section>
    ${connectHtml()}
    <details class="card more"><summary class="card-title">Więcej statystyk</summary>
    <div class="tiles">
      <div class="tile"><span class="tile-label">Opanowane fiszki</span><strong>${mastered}<small>/${total}</small></strong>${progressBar(total ? mastered / total : 0, 'Opanowane fiszki')}</div>
      <div class="tile tile-gold"><span class="tile-label">Seria dni nauki</span><strong>${st.current}<small> ${plural(st.current, 'dzień', 'dni', 'dni')}</small></strong><span class="tile-sub">Najdłuższa: ${st.longest} ${plural(st.longest, 'dzień', 'dni', 'dni')}</span></div>
      <div class="tile"><span class="tile-label">Poznane fiszki</span><strong>${seen}<small>/${total}</small></strong><span class="tile-sub">Łącznie ${activity} ${plural(activity, 'odpowiedź', 'odpowiedzi', 'odpowiedzi')}</span></div>
      <div class="tile"><span class="tile-label">Średni wynik testów</span><strong>${avg === null ? '—' : pct(avg) + '%'}</strong><span class="tile-sub">${state.tests.length} ${plural(state.tests.length, 'test', 'testy', 'testów')}</span></div>
      ${tAll ? `<div class="tile tile-wide"><span class="tile-label">Zadania maturalne</span><strong>${tMax ? pct(tPkt / tMax) + '%' : '—'}</strong><span class="tile-sub">${tDone}/${nZadan(tAll)} rozwiązanych · ${tPkt}/${tMax} pkt</span></div>` : ''}
    </div>

    <section class="card">
      <h2 class="card-title">Ostatnie 14 dni</h2>
      <div class="days" role="list">${days.map((x) => `<div role="listitem" class="day ${x.on ? 'on' : ''}" title="${store.dayKey(x.t)}"><span class="dot">${x.on ? ICONS.check : ''}</span><small>${dfmt.format(x.t)}</small></div>`).join('')}</div>
    </section>

    <section class="card">
      <h2 class="card-title">Opanowanie działów</h2>
      ${per.map(({ s, d, sm }) => `<a class="stat-row" href="${hrefDzial(s.id, d.id)}">
        <div class="stat-row-top"><span>${esc(s.skrot)} · ${esc(d.nazwa)}</span><strong>${pct(sm.progress)}%</strong></div>
        ${progressBar(sm.progress, d.nazwa)}
      </a>`).join('') || '<p class="muted">Brak działów.</p>'}
    </section>

    <section class="card">
      <h2 class="card-title">Ostatnie testy</h2>
      ${tests.length ? `<ul class="test-list">${tests.map((t) => {
        const p = pct(t.score / t.total);
        return `<li><div><strong>${esc(t.name || t.did || 'Test')}</strong><span>${fmt.format(t.at)} · ${t.score}/${t.total}</span></div>
          <span class="score ${p >= 70 ? 'ok' : p >= 50 ? 'warn' : 'bad'}">${p}%</span></li>`;
      }).join('')}</ul>` : '<p class="muted">Nie masz jeszcze żadnego testu.</p>'}
    </section>
    </details>
    <nav class="menu-list" aria-label="Konto">
      <a href="#/ustawienia">${ICONS.cog}<span>Ustawienia</span>${ICONS.next}</a>
      ${cloud.account() ? `<button type="button" data-act="sync">${ICONS.redo}<span>Synchronizuj z kontem</span></button>` : ''}
      <button type="button" data-act="logout">${ICONS.back}<span>Wyloguj</span></button>
    </nav>`;
  bindProfil();
  app.querySelector('[data-act="sync"]')?.addEventListener('click', async () => {
    try { await cloud.sync(); afterProfileChange(); toast('Zsynchronizowano z kontem.'); } catch (err) { toast(err.message); }
  });
}

// ---------- płatny dostęp: plany, zakup, kody ----------
const maZablokowane = () => subjects.some((s) => s.dzialy.some((d) => d.zablokowany) || s.arkusze.some((a) => a.zablokowany));

function premiumCard() {
  if (!dostep.wlaczone()) return '';
  if (dostep.aktywny()) {
    const st = dostep.biezacy();
    return `<a class="card plan-card" href="#/plany"><span class="quest-icon">${ICONS.check}</span>
      <span class="plan-text"><strong>IndexLab Premium</strong><small>Aktywny do ${fmtDay(new Date(st.wazne_do).getTime())}${st.plan === 'miesiac' && st.status === 'active' ? ' · odnawia się automatycznie' : ''}</small></span>${ICONS.next}</a>`;
  }
  return maZablokowane() ? `<a class="card plan-card premium-cta" href="#/plany"><span class="quest-icon">${ICONS.lock}</span>
    <span class="plan-text"><strong>Odblokuj pełny kurs</strong><small>Wszystkie działy, arkusze CKE z omówieniem i bank zadań. Pierwszy dział jest za darmo.</small></span>${ICONS.next}</a>` : '';
}

async function viewPlany(ok) {
  if (!dostep.wlaczone()) {
    app.innerHTML = `${pageHead('Plany', '#/profil')}<section class="card"><p>Wszystkie treści IndexLab są teraz dostępne bez opłat.</p></section>`;
    return;
  }
  const zalogowany = !!cloud.account();
  const render = (msg = '') => {
    const st = dostep.biezacy();
    const akt = dostep.aktywny();
    app.innerHTML = `
      ${pageHead('IndexLab Premium', '#/', 'Plany')}
      ${ok && !akt ? '<section class="card"><p><strong>Dziękujemy!</strong> Czekamy na potwierdzenie płatności — to zwykle kilka sekund.</p></section>' : ''}
      ${akt ? `<section class="card premium-on">
          <h2 class="card-title">Masz pełny dostęp</h2>
          <p>Aktywny do <strong>${fmtDay(new Date(st.wazne_do).getTime())}</strong>${st.plan === 'miesiac' && st.status === 'active' ? ' — subskrypcja odnawia się co miesiąc.' : '.'}</p>
          ${st.zrodlo === 'stripe' ? '<button type="button" class="btn btn-ghost btn-lg" data-act="portal">Zarządzaj płatnościami</button>' : ''}
        </section>` : `<section class="card">
          <h2 class="card-title">Co dostajesz</h2>
          <ul class="premium-list">
            <li>Wszystkie działy: fiszki, lekcje i pytania testowe z całej podstawy programowej</li>
            <li>Arkusze CKE z omówieniem każdego zadania</li>
            <li>Bank zadań maturalnych i próbne matury na czas</li>
            <li>Plan nauki dopasowany do daty matury</li>
          </ul>
        </section>
        ${zalogowany ? '' : connectHtml(true, 'Dostęp przypisujemy do konta e-mail, żeby działał na telefonie, tablecie i komputerze. Twoje dotychczasowe postępy zostaną zachowane.')}
        <div class="plany">${dostep.plany().map((p) => `<section class="card plan-oferta ${p.polecany ? 'polecany' : ''}">
          ${p.polecany ? '<span class="eyebrow">Najczęściej wybierany</span>' : ''}
          <h2 class="card-title">${esc(p.nazwa)}</h2>
          <p class="plan-cena"><b>${esc(p.cena)}</b><span>${esc(p.okres)}</span></p>
          <p class="muted">${esc(p.opis)}</p>
          <button type="button" class="btn ${p.polecany ? 'btn-primary' : 'btn-ghost'} btn-lg" data-kup="${esc(p.id)}" ${zalogowany ? '' : 'disabled'}>Wybieram</button>
        </section>`).join('')}</div>`}
      <section class="card">
        <h2 class="card-title">Masz kod dostępu?</h2>
        <form class="pop-row" id="kod-form"><input class="type-input" name="kod" maxlength="40" placeholder="np. ABCD-EFGH-JKLM" autocomplete="off" autocapitalize="characters" aria-label="Kod dostępu" ${zalogowany ? '' : 'disabled'}><button type="submit" class="btn btn-ghost btn-sm" ${zalogowany ? '' : 'disabled'}>Aktywuj</button></form>
        ${dostep.sklepKodow() ? `<p class="muted">Kod możesz też kupić <a href="${esc(dostep.sklepKodow())}" target="_blank" rel="noopener">w naszym sklepie</a>.</p>` : ''}
      </section>
      ${msg ? `<p class="acc-msg" role="status">${esc(msg)}</p>` : ''}
      <p class="muted small">Płatności obsługuje Stripe — IndexLab nie widzi danych Twojej karty. Subskrypcję anulujesz w każdej chwili w „Zarządzaj płatnościami”.</p>`;
    bindConnect(() => viewPlany());
    app.querySelectorAll('[data-kup]').forEach((b) => b.addEventListener('click', async () => {
      b.disabled = true;
      try { await dostep.kup(b.dataset.kup); } catch (e) { b.disabled = false; toast(e.message); }
    }));
    app.querySelector('[data-act="portal"]')?.addEventListener('click', () => dostep.panelKlienta().catch((e) => toast(e.message)));
    app.querySelector('#kod-form').addEventListener('submit', async (e) => {
      e.preventDefault();
      const kod = e.target.kod.value.trim();
      if (!kod) return;
      e.submitter && (e.submitter.disabled = true);
      try {
        await dostep.wykorzystajKod(kod);
        await zaladujTresci();
        game.sound('ok');
        render('Kod aktywny — pełny kurs odblokowany.');
      } catch (err) { render(err.message); }
    });
  };
  render();
  await dostep.odswiez().catch(() => null);
  if (ok && !dostep.aktywny()) { // webhook Stripe może przyjść z kilkusekundowym opóźnieniem
    for (let i = 0; i < 10 && !dostep.aktywny() && location.hash === '#/plany/ok'; i++) {
      await new Promise((r) => setTimeout(r, 2000));
      await dostep.odswiez().catch(() => null);
    }
  }
  if (!location.hash.startsWith('#/plany')) return;
  if (dostep.aktywny() && maZablokowane()) await zaladujTresci();
  render(ok && dostep.aktywny() ? 'Płatność przyjęta — pełny kurs odblokowany.' : '');
}

// ---------- ustawienia ----------
function viewSettings() {
  const settings = store.get().settings;
  const theme = settings.theme;
  const auto = tempoAuto();
  const npd = auto ? 'auto' : Number(settings.newPerDay) || 20;
  const ios = /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  const standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  app.innerHTML = `
    ${pageHead('Ustawienia', '#/profil')}
    <section class="card">
      <h2 class="card-title">Motyw</h2>
      <div class="segmented" role="radiogroup" aria-label="Motyw">
        ${[['auto', 'Systemowy'], ['light', 'Jasny'], ['dark', 'Ciemny']].map(([v, l]) => `<button type="button" role="radio" aria-checked="${theme === v}" class="${theme === v ? 'active' : ''}" data-theme-set="${v}">${l}</button>`).join('')}
      </div>
    </section>

    <section class="card">
      <h2 class="card-title">Nowe fiszki dziennie</h2>
      <p class="muted">„Plan” dobiera liczbę nowych fiszek do dnia, w którym chcesz skończyć materiał${currentSubject() && auto ? ` (teraz: ${newPerDay(currentSubject().id)} dziennie)` : ''}. Możesz też ustawić stałą liczbę. Powtórki są zawsze bez limitu.</p>
      <div class="segmented seg-5" role="radiogroup" aria-label="Nowe fiszki dziennie">
        ${['auto', 10, 20, 30, 50].map((v) => `<button type="button" role="radio" aria-checked="${npd === v}" class="${npd === v ? 'active' : ''}" data-npd="${v}">${v === 'auto' ? 'Plan' : v}</button>`).join('')}
      </div>
    </section>

    <section class="card">
      <h2 class="card-title">Plan nauki do matury</h2>
      ${(() => { const cs = currentSubject(); const pp = cs && planOf(cs); return pp?.data ? `<p class="muted">${esc(cs.nazwa)}: koniec materiału ${fmtDay(pp.koniec)}, matura ${fmtDay(pp.egz)}.</p>` : ''; })()}
      <div class="actions">
        <a class="btn btn-ghost btn-lg" href="#/plan">Zmień plan</a>
        <button type="button" class="btn btn-danger btn-lg" data-act="plan-reset">Resetuj plan</button>
      </div>
    </section>

    <section class="card">
      <h2 class="card-title">Zdjęcie profilowe</h2>
      <div class="photo-row">${avatar(store.activeProfile(), true)}
        <label class="btn btn-ghost btn-sm file-btn">${store.activeProfile().photo ? 'Zmień zdjęcie' : 'Dodaj zdjęcie'}<input type="file" id="avatar-file" accept="image/*"></label>
        ${store.activeProfile().photo ? '<button type="button" class="link-btn" data-act="photo-del">Usuń</button>' : ''}</div>
      <p class="muted small">Zdjęcie zostaje tylko na tym urządzeniu.</p>
    </section>

    <section class="card">
      <h2 class="card-title">Nazwa profilu</h2>
      <div class="pop-row"><input class="type-input" id="pname" maxlength="30" value="${esc(store.activeProfile().name)}" aria-label="Nazwa profilu"><button type="button" class="btn btn-ghost btn-sm" data-act="rename">Zapisz</button></div>
    </section>

    <section class="card">
      <h2 class="card-title">Dzienny cel</h2>
      <p class="muted">Ile odpowiedzi dziennie (fiszki, pytania testowe, ćwiczenia w lekcjach) chcesz udzielić.</p>
      <div class="segmented seg-4" role="radiogroup" aria-label="Dzienny cel — liczba odpowiedzi">
        ${game.GOALS.map((v) => `<button type="button" role="radio" aria-checked="${game.goal() === v}" class="${game.goal() === v ? 'active' : ''}" data-goal="${v}">${v}</button>`).join('')}
      </div>
      <div class="pop-row goal-own"><input class="type-input" id="goal-own" type="number" inputmode="numeric" min="5" max="2000" placeholder="Własny cel, np. 150" value="${game.GOALS.includes(game.goal()) ? '' : game.goal()}" aria-label="Własny dzienny cel"><button type="button" class="btn btn-ghost btn-sm" data-act="goal-own">Ustaw</button></div>
    </section>

    ${standalone ? '' : `<section class="card">
      <h2 class="card-title">Aplikacja na ekranie głównym</h2>
      ${installEvent ? '<button type="button" class="btn btn-gold btn-lg" data-act="install">Zainstaluj IndexLab</button>'
        : ios ? '<p>Na iPhonie lub iPadzie otwórz stronę w Safari, stuknij <strong>Udostępnij</strong>, a potem <strong>Do ekranu początkowego</strong>.</p>'
        : '<p>Otwórz menu przeglądarki i wybierz <strong>Zainstaluj aplikację</strong> lub <strong>Dodaj do ekranu głównego</strong>.</p>'}
      <p class="muted">Po instalacji IndexLab działa także bez internetu.</p>
    </section>`}

    <section class="card">
      <h2 class="card-title">Kopia postępów</h2>
      <p class="muted">Postępy są zapisane tylko na tym urządzeniu. Zrób kopię, aby przenieść je na inne urządzenie.</p>
      <div class="actions">
        <button type="button" class="btn btn-ghost btn-lg" data-act="export">${ICONS.download}<span>Pobierz kopię</span></button>
        <label class="btn btn-ghost btn-lg file-btn">Wczytaj kopię<input type="file" accept="application/json,.json" data-act="import"></label>
      </div>
    </section>

    <section class="card">
      <h2 class="card-title">Strefa ryzyka</h2>
      <div class="actions">
        <button type="button" class="btn btn-danger btn-lg" data-act="reset">Wyzeruj postępy tego profilu</button>
        <button type="button" class="btn btn-danger btn-lg" data-act="delprof">Usuń ten profil z urządzenia</button>
      </div>
    </section>

    <section class="card about">
      <h2 class="card-title">Kontakt</h2>
      <p>Widzisz błąd albo masz pomysł? Napisz do nas:</p>
      <p class="contact-mail"><strong>${REPORT_EMAIL}</strong></p>
      <div class="actions">
        <button type="button" class="btn btn-primary btn-lg" data-act="copy-mail">Kopiuj adres e-mail</button>
      </div>
      <p class="muted small">Zadania z arkuszy CKE pochodzą z egzaminów maturalnych Centralnej Komisji Egzaminacyjnej i są oznaczone źródłem. Fiszki, lekcje, omówienia i zadania autorskie przygotowuje IndexLab. Aplikacja nie jest związana z CKE.</p>
    </section>`;

  app.querySelectorAll('.segmented').forEach((seg) => seg.addEventListener('click', (e) => {
    const b = e.target.closest('button');
    if (!b) return;
    if (b.dataset.themeSet) {
      settings.theme = b.dataset.themeSet;
      applyTheme();
    }
    if (b.dataset.npd === 'auto') settings.tempo = 'auto';
    else if (b.dataset.npd) { settings.tempo = 'manual'; settings.newPerDay = Number(b.dataset.npd); }
    if (b.dataset.goal) settings.dailyGoal = Number(b.dataset.goal);
    if (b.dataset.sound) { settings.sound = b.dataset.sound === 'true'; game.sound('ok'); }
    store.save();
    viewSettings();
  }));
  app.querySelector('[data-act="plan-reset"]')?.addEventListener('click', () => {
    const cs = currentSubject();
    if (!cs) return;
    const stary = settings.plan?.[cs.id];
    if (settings.plan) delete settings.plan[cs.id];
    store.save();
    refreshAutoRates();
    location.hash = '#/plan';
    if (stary) toast('Plan zresetowany — ułóż go od nowa.', { label: 'Cofnij', run: () => { settings.plan[cs.id] = stary; store.save(); refreshAutoRates(); location.hash = '#/'; } });
  });
  app.querySelector('[data-act="goal-own"]').addEventListener('click', () => {
    const v = Math.round(Number(app.querySelector('#goal-own').value));
    if (!(v >= 5 && v <= 2000)) return toast('Podaj liczbę od 5 do 2000.');
    settings.dailyGoal = v; store.save(); toast(`Cel dnia: ${v} odpowiedzi.`); viewSettings();
  });
  bindAvatarUpload();
  app.querySelector('[data-act="copy-mail"]')?.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(REPORT_EMAIL); toast('Adres skopiowany.'); } catch { toast(REPORT_EMAIL); }
  });
  app.querySelector('[data-act="rename"]').addEventListener('click', () => { store.renameProfile(store.activeProfile().id, app.querySelector('#pname').value); toast('Zapisano nazwę profilu.'); });
  app.querySelector('[data-act="delprof"]')?.addEventListener('click', () => {
    if (!confirm('Usunąć ten profil i jego postępy z tego urządzenia?')) return;
    store.deleteProfile(store.activeProfile().id);
    store.logout();
    location.hash = '#/konto';
  });
  app.querySelector('[data-act="install"]')?.addEventListener('click', promptInstall);
  app.querySelector('[data-act="export"]').addEventListener('click', () => {
    const blob = new Blob([JSON.stringify(store.get(), null, 2)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `indexlab-postepy-${store.dayKey()}.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  });
  app.querySelector('[data-act="import"]').addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    try {
      const data = JSON.parse(await file.text());
      if (!data || typeof data.cards !== 'object' || !Array.isArray(data.tests)) throw new Error();
      if (!confirm('Wczytanie kopii zastąpi obecne postępy na tym urządzeniu. Kontynuować?')) return;
      store.replace(data);
      applyTheme();
      toast('Wczytano kopię postępów.');
    } catch {
      toast('To nie jest poprawny plik kopii postępów IndexLab.');
    }
    e.target.value = '';
  });
  app.querySelector('[data-act="reset"]').addEventListener('click', () => {
    if (!confirm('Na pewno usunąć wszystkie postępy, serię, wyniki testów i zadań? Tej operacji nie można cofnąć.')) return;
    store.reset();
    session = test = zs = null;
    toast('Postępy wyzerowane.');
  });
}

// ---------- motyw ----------
function applyTheme() {
  const t = store.get().settings.theme;
  if (t === 'auto') document.documentElement.removeAttribute('data-theme');
  else document.documentElement.dataset.theme = t;
  const dark = t === 'dark' || (t === 'auto' && matchMedia('(prefers-color-scheme: dark)').matches);
  document.querySelector('meta[name="theme-color"]').setAttribute('content', dark ? '#0D0D0D' : '#F1F2F1');
  const btn = document.getElementById('theme-toggle');
  if (btn) { btn.setAttribute('aria-label', dark ? 'Włącz jasny motyw' : 'Włącz ciemny motyw'); btn.dataset.dark = String(dark); }
}

document.getElementById('theme-toggle')?.addEventListener('click', () => {
  const dark = document.getElementById('theme-toggle').dataset.dark === 'true';
  store.get().settings.theme = dark ? 'light' : 'dark';
  store.save();
  applyTheme();
});
matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change', applyTheme);

// ---------- instalacja PWA ----------
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  installEvent = e;
  if (!location.hash || location.hash === '#/' || location.hash === '#/ustawienia') route();
});
window.addEventListener('appinstalled', () => {
  installEvent = null;
  toast('IndexLab zainstalowany!');
});
async function promptInstall() {
  if (!installEvent) return;
  installEvent.prompt();
  await installEvent.userChoice.catch(() => {});
  installEvent = null;
  route();
}

// ---------- routing ----------
const routes = [
  [/^#?\/?$/, viewHome],
  [/^#\/d\/([^/]+)\/([^/]+)$/, viewDzial],
  [/^#\/p\/([^/]+)\/([^/]+)$/, viewUnit],
  [/^#\/fiszki\/([^/]+)\/(d|p|w)\/([^/]+)(?:\/(trening))?$/, viewFiszki],
  [/^#\/test\/([^/]+)\/(d|p|w|x)\/([^/]+)$/, viewTest],
  [/^#\/lekcja\/([^/]+)\/(d|p|w)\/([^/]+)$/, viewLekcja],
  [/^#\/bledy\/([^/]+)$/, viewBledy],
  [/^#\/szukaj$/, viewSzukaj],
  [/^#\/aktualnosci$/, viewAktualnosci],
  [/^#\/lista\/([^/]+)\/([^/]+)$/, viewLista],
  [/^#\/matura(?:\/(proba|cke|dzialy|autorskie))?$/, viewMatura],
  [/^#\/zadania\/([^/]+)\/(a|d|b)\/([^/]+)$/, viewZadania],
  [/^#\/egzamin\/([^/]+)\/([^/]+)$/, viewEgzamin],
  [/^#\/statystyki$/, viewStats],
  [/^#\/profil$/, viewStats],
  [/^#\/nauka$/, viewNauka],
  [/^#\/start$/, viewPrzedmiot],
  [/^#\/przedmiot$/, viewPrzedmiot],
  [/^#\/konto$/, viewKonto],
  [/^#\/ustawienia$/, viewSettings],
  [/^#\/plan$/, viewPlan],
  [/^#\/powtorka$/, viewPowtorka],
  [/^#\/diagnoza$/, viewDiagnoza],
  [/^#\/prognoza$/, viewPrognoza],
  [/^#\/plany(?:\/(ok))?$/, viewPlany],
];

let lastHash = null;
function route() {
  const hash = location.hash || '#/';
  const changed = hash !== lastHash;
  lastHash = hash;
  keyHandler = null;
  document.querySelector('.report-layer')?.remove();
  document.body.classList.remove('in-session', 'in-lesson', 'in-gate');
  if (!hash.startsWith('#/lekcja/') && !hash.startsWith('#/bledy/')) lesson = null;
  if (!hash.startsWith('#/fiszki/')) session = null;
  if (!hash.startsWith('#/test/')) test = null;
  if (!hash.startsWith('#/zadania/')) zs = null;
  if (!hash.startsWith('#/egzamin/')) clearInterval(examTimer);

  // bramka: najpierw logowanie (profil), potem wybór przedmiotu
  const gate = !store.loggedIn() ? viewKonto : !store.get().settings.przedmiot && subjects.length && !/^#\/(przedmiot|start)$/.test(hash) ? viewPrzedmiot : null;
  const hit = gate ? null : routes.find(([re]) => re.test(hash));
  if (!gate && hit && !/^#\/(konto|przedmiot|start)$/.test(hash) && czekajNaTresc(hash)) { updateTopStats(); return; }
  if (gate) gate();
  else if (hit) {
    const m = hash.match(hit[0]);
    hit[1](...m.slice(1).map((x) => (x === undefined ? undefined : decodeURIComponent(x))));
  } else notFound();

  const tab = /^#\/(statystyki|profil|ustawienia)/.test(hash) ? 'stats'
    : hash.startsWith('#/matura') || hash.startsWith('#/zadania') || hash.startsWith('#/egzamin') ? 'matura'
    : hash.startsWith('#/aktualnosci') ? 'news'
    : /^#\/(nauka|szukaj|d\/|p\/|lista|fiszki|test|lekcja)/.test(hash) ? 'nauka' : 'home';
  document.querySelectorAll('.tabbar a').forEach((a) => {
    const on = a.dataset.tab === tab;
    a.classList.toggle('active', on);
    if (on) a.setAttribute('aria-current', 'page');
    else a.removeAttribute('aria-current');
  });
  updateTopStats();
  if (changed) {
    window.scrollTo({ top: 0 });
    app.focus({ preventScroll: true });
  }
}

window.addEventListener('hashchange', route);
document.addEventListener('keydown', (e) => {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  if (e.target.closest('input, textarea, select')) return;
  if (document.querySelector('.report-layer')) { keyHandler?.(e); return; }
  if (e.key === 'Escape' && document.body.classList.contains('in-session')) {
    app.querySelector('.session-top .icon-btn')?.click();
    return;
  }
  keyHandler?.(e);
});

// ---------- start ----------
// Treści: z plików (tryb bezpłatny) albo z bazy — tylko to, do czego konto ma dostęp (tryb premium).
// Szybki start: najpierw spis przedmiotów (kilka KB) — ekrany profilu i wyboru kursu są od razu gotowe;
// pełne treści dochodzą w tle, zaczynając od przedmiotu, którego uczeń się uczy.
let gotowe = {};                     // id przedmiotu → Promise (treść wczytana)
let ladowanie = Promise.resolve();   // wszystkie przedmioty wczytane
async function startTresci() {
  let zrodlo;
  if (dostep.wlaczone()) {
    await dostep.odswiez().catch(() => null);
    zrodlo = await dostep.pobierzTresci();
  }
  const wpisy = await loadIndex(zrodlo);
  subjects = wpisy.map((w) => w.stub).sort((a, b) => a.nazwa.localeCompare(b.nazwa, 'pl'));
  loadErrors = takeErrors();
  const cur = store.get().settings.przedmiot;
  const kolej = [...wpisy].sort((a, b) => (b.stub.id === cur) - (a.stub.id === cur));
  gotowe = {};
  let prev = Promise.resolve();
  for (const w of kolej) {
    const p = prev.then(() => loadFull(w)).then((full) => {
      const i = subjects.findIndex((x) => x.id === full.id);
      if (i >= 0) subjects[i] = full;
    }).catch((e) => { loadErrors.push(`${w.file}: ${e.message}`); });
    gotowe[w.stub.id] = p;
    prev = p;
  }
  ladowanie = prev.then(() => { loadErrors.push(...takeErrors()); refreshAutoRates(); updateTopStats(); });
}
async function zaladujTresci() {
  await startTresci();
  await ladowanie;
}
// Czy widok może się wyświetlić; jeśli nie — pokazuje wczytywanie i wraca do routingu, gdy treść dojdzie.
function czekajNaTresc(hash) {
  if (!subjects.some((x) => x.szkielet)) return false;
  const wszystkie = /^#\/(statystyki|profil|szukaj|ustawienia|plany)/.test(hash);
  const cs = currentSubject();
  const czekaj = wszystkie ? ladowanie : cs?.szkielet ? gotowe[cs.id] : null;
  if (!czekaj) return false;
  app.innerHTML = `<div class="skeleton" role="status" aria-label="Wczytywanie"><i class="sk-title"></i><i class="sk-card"></i><i class="sk-card short"></i><i class="sk-card"></i></div>`;
  czekaj.then(() => { if ((location.hash || '#/') === hash) route(); });
  return true;
}

async function init() {
  applyTheme();
  game.onChange(onGameEvents);
  cloud.startAutoSync(() => {});
  updateTopStats();
  try {
    await startTresci();
    // uczeń z wybranym kursem: poczekaj na jego treść (z pamięci telefonu to ułamek sekundy) — bez ekranu wczytywania
    const cur = store.loggedIn() && store.get().settings.przedmiot;
    if (cur && gotowe[cur]) await gotowe[cur];
  } catch (e) {
    app.innerHTML = `<div class="empty"><div class="empty-icon">${ICONS.compass}</div>
      <h1>Nie udało się wczytać treści</h1>
      <p>Sprawdź połączenie z internetem i spróbuj ponownie.</p>
      <p class="muted"><small>${esc(e.message)}</small></p>
      <button type="button" class="btn btn-primary" onclick="location.reload()">Spróbuj ponownie</button></div>`;
    return;
  }
  refreshAutoRates();
  route();
}

if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  window.addEventListener('load', () => {
    const hadController = !!navigator.serviceWorker.controller; // pierwsza instalacja ≠ aktualizacja
    navigator.serviceWorker.register('sw.js').then((reg) => {
      reg.addEventListener('updatefound', () => {
        const sw = reg.installing;
        sw?.addEventListener('statechange', () => {
          if (sw.state === 'activated' && hadController) {
            toast('Dostępna nowa wersja IndexLab.', { label: 'Odśwież', run: () => location.reload() });
          }
        });
      });
    }).catch(() => {});
  });
}

init();
