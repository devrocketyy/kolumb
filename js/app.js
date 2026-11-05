// Kolumb — aplikacja do nauki do matury.
import * as store from './store.js';
import { loadSubjects } from './data.js';
import * as game from './game.js';
import * as cloud from './cloud.js';
import { cardKey, nextState, intervalLabel, summary, buildQueue, newAllowance, MASTERED_BOX } from './srs.js';

const REPORT_EMAIL = 'roc7et@gmail.com';
const TEST_SIZE = 10;
const LITERY = ['A', 'B', 'C', 'D'];

const app = document.getElementById('app');
let subjects = [];
let loadErrors = [];
let keyHandler = null;
let installEvent = null;

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
  clock: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>',
  search: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 21 21" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
  redo: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12a8 8 0 1 0 2.4-5.7M4 4v4h4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  cog: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.5 5.5l1.7 1.7M16.8 16.8l1.7 1.7M5.5 18.5l1.7-1.7M16.8 7.2l1.7-1.7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
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
    `zgłaszam błąd w ${kind === 'fiszka' ? 'fiszce' : 'pytaniu testowym'} w aplikacji Kolumb.`, '',
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
  return mailto(`[Kolumb] Błąd: ${s.skrot} — ${kind} ${u.id}/${item.id}`, lines);
}

function reportTaskHref(s, a, z) {
  return mailto(`[Kolumb] Błąd: ${s.skrot} — ${a.nazwa}, zadanie ${z.nr}`, [
    'Dzień dobry,', '', 'zgłaszam błąd w zadaniu maturalnym w aplikacji Kolumb.', '',
    `Przedmiot: ${s.nazwa}`, `Arkusz: ${a.nazwa}`, `Zadanie: ${z.nr}`, '',
    `Polecenie: ${z.polecenie}`, '', `Odpowiedź w aplikacji: ${z.odpowiedz}`, '',
    'Na czym polega błąd:', '', '',
  ]);
}

const reportBtn = (href) => `<a class="btn-report" href="${esc(href)}">${ICONS.flag}<span>Zgłoś błąd</span></a>`;
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
        <span class="leg-text"><strong>${esc(d.nazwa)}</strong><small>${doneN}/${d.poddzialy.length} opanowanych · ${pct(smD.progress)}%</small>${progressBar(smD.progress, d.nazwa)}</span>
        <span class="leg-chev" aria-hidden="true">${ICONS.next}</span>
      </summary>
      <ol class="stops">${stops}</ol>
    </details>`;
  }).join('');
}

function popHtml(s, u) {
  const sm = summary(s.id, [u]);
  const nQ = u.pytania.length;
  return `<div class="pop-row">
      <a class="btn btn-primary btn-sm" href="#/lekcja/${enc(s.id)}/p/${enc(u.id)}">${ICONS.play}<span>Lekcja</span></a>
      ${u.fiszki.length ? `<a class="btn btn-ghost btn-sm" href="#/fiszki/${enc(s.id)}/p/${enc(u.id)}">${ICONS.cards}<span>Fiszki${sm.todo ? ` (${sm.todo})` : ''}</span></a>` : ''}
      ${nQ ? `<a class="btn btn-ghost btn-sm" href="#/test/${enc(s.id)}/p/${enc(u.id)}">${ICONS.quiz}<span>Test</span></a>` : ''}
      <a class="btn btn-ghost btn-sm" href="${hrefUnit(s.id, u.id)}">${ICONS.book}<span>Treści</span></a>
    </div>`;
}

function questsHtml() {
  return `<section class="card quests">
    <h2 class="card-title">Zadania dnia</h2>
    ${game.quests().map((q) => `<div class="quest ${q.v >= q.n ? 'done' : ''}">
      <span class="quest-icon">${q.v >= q.n ? ICONS.check : q.id === 'xp' ? ICONS.bolt : q.id === 'lekcje' || q.id === 'idealne' ? ICONS.star : q.id === 'fiszki' ? ICONS.cards : q.id === 'zadania' ? ICONS.exam : ICONS.target}</span>
      <div class="quest-body"><span>${esc(q.name)}</span>
        <div class="quest-bar">${progressBar(q.v / q.n, q.name)}<small>${q.v}/${q.n}</small></div></div>
    </div>`).join('')}
  </section>`;
}

function goalCard(s, rec) {
  const d = game.today();
  const g = game.goal();
  const st = store.streak();
  const allowance = newAllowance(s.id);
  let todo = 0, best = null;
  s.dzialy.forEach((dz) => {
    const n = summary(s.id, dz.poddzialy, allowance).todo;
    todo += n;
    if (n && (!best || n > best.n)) best = { d: dz, n };
  });
  return `<section class="goal-card">
    <div class="goal-top">
      <div class="ring ring-goal ${d.xp >= g ? 'ring-ok' : ''}" style="--p:${Math.min(100, pct(d.xp / g))}"><span>${ICONS.bolt}</span></div>
      <div class="goal-text">
        <strong>${d.xp >= g ? 'Cel dnia zrobiony' : `${d.xp} / ${g} XP dzisiaj`}</strong>
        <span>${st.current ? `${ICONS.flame} ${st.current} ${plural(st.current, 'dzień', 'dni', 'dni')} z rzędu${st.today ? '' : ' · dziś jeszcze bez nauki'}` : 'Seria: 0 dni'}</span>
      </div>
    </div>
    ${rec ? `<a class="btn btn-gold btn-xl btn-continue" href="#/lekcja/${enc(s.id)}/p/${enc(rec.u.id)}">${ICONS.play}<span>Kontynuuj<small>${esc(rec.u.nazwa)}</small></span></a>` : ''}
    ${best ? `<a class="goal-link" href="#/fiszki/${enc(s.id)}/d/${enc(best.d.id)}">${ICONS.cards}<span>Powtórki na dziś: <b>${todo}</b></span>${ICONS.next}</a>` : ''}
  </section>`;
}


// ---------- zakładka „Dziś” ----------
function viewHome() {
  const showInstall = installEvent && !store.get().settings.installDismissed;
  const s = currentSubject();
  const rec = s ? recommendedUnit(s) : null;
  const nb = s ? mistakesOf(s).length : 0;
  app.innerHTML = `
    <header class="today-head"><h1>Dziś</h1></header>
    ${s ? goalCard(s, rec) : ''}
    ${showInstall ? `<div class="install-banner">
        <div><strong>Zainstaluj Kolumba</strong><span>Ikona na ekranie głównym i nauka bez internetu.</span></div>
        <div class="install-actions">
          <button type="button" class="btn btn-gold btn-sm" data-act="install">Zainstaluj</button>
          <button type="button" class="icon-btn" data-act="dismiss" aria-label="Nie teraz">${ICONS.close}</button>
        </div></div>` : ''}
    ${loadErrors.length ? `<div class="alert">Nie udało się wczytać: ${esc(loadErrors.join('; '))}</div>` : ''}
    ${nb ? `<a class="card mistakes-card" href="#/bledy/${enc(s.id)}">
      <span class="quest-icon">${ICONS.redo}</span>
      <span class="mistakes-text"><strong>Błędy do poprawy: ${nb}</strong><small>Lekcja z pytań, w których była pomyłka</small></span>
      ${ICONS.next}</a>` : ''}
    ${questsHtml()}
    ${s ? '' : '<p class="muted">Brak przedmiotów.</p>'}
  `;
  app.querySelector('[data-act="install"]')?.addEventListener('click', promptInstall);
  app.querySelector('[data-act="dismiss"]')?.addEventListener('click', () => {
    store.get().settings.installDismissed = true;
    store.save();
    viewHome();
  });
}

// ---------- zakładka „Nauka” ----------
function viewNauka() {
  const s = currentSubject();
  if (!s) return notFound();
  const rec = recommendedUnit(s);
  const sm = summary(s.id, allUnits(s));
  app.innerHTML = `
    <header class="today-head">
      <h1>${esc(s.nazwa)}</h1>
      <a class="icon-btn" href="#/szukaj" aria-label="Szukaj pojęć">${ICONS.search}</a>
    </header>
    <p class="muted route-sum">${pct(sm.progress)}% opanowane · ${sm.mastered}/${nFiszek(sm.total)} · ${sm.todo} do powtórki</p>
    <div class="route" data-sid="${esc(s.id)}">${pathHtml(s, rec)}</div>`;
  const wrap = app.querySelector('.route');
  wrap.addEventListener('click', (e) => {
    const b = e.target.closest('.stop-body');
    if (!b) return;
    const u = s.units.get(b.dataset.unit);
    const pop = wrap.querySelector(`[data-pop="${CSS.escape(u.id)}"]`);
    const open = !pop.hidden;
    wrap.querySelectorAll('.stop-pop').forEach((p) => (p.hidden = true));
    wrap.querySelectorAll('.stop-body').forEach((x) => x.setAttribute('aria-expanded', 'false'));
    if (!open) { pop.innerHTML = popHtml(s, u); pop.hidden = false; b.setAttribute('aria-expanded', 'true'); game.sound('tap'); }
  });
  wrap.querySelector('.stop.current')?.scrollIntoView({ block: 'center' });
}


// ---------- pasek u góry: seria i XP ----------
function updateTopStats() {
  const sb = document.getElementById('subj-btn');
  const cs = subjects.length ? currentSubject() : null;
  if (sb) sb.innerHTML = cs ? `<span class="subj-icon subj-icon-sm">${subjectIcon(cs)}</span><span class="subj-btn-name">${esc(cs.skrot || cs.nazwa)}</span>` : '';
  const el = document.getElementById('top-stats');
  if (!el) return;
  const st = store.streak();
  const d = game.today();
  el.innerHTML = `<a class="top-chip chip-flame ${st.today ? 'on' : ''}" href="#/statystyki" aria-label="Seria: ${st.current} ${plural(st.current, 'dzień', 'dni', 'dni')}">${ICONS.flame}<span>${st.current}</span></a>
    <a class="top-chip chip-xp" href="#/statystyki" aria-label="Dziś ${d.xp} XP">${ICONS.bolt}<span>${d.xp}</span></a>`;
}

function onGameEvents(events) {
  updateTopStats();
  const msgs = [];
  for (const ev of events) {
    if (ev.type === 'goal') { msgs.push('Cel dnia zrobiony'); game.confetti(); game.sound('win'); }
    if (ev.type === 'level') msgs.push(`Nowy poziom: ${ev.level}!`);
    if (ev.type === 'badge') { msgs.push(`Nowa odznaka: ${ev.badge.name}`); game.confetti(40); }
  }
  if (msgs.length) toast(msgs.join(' · '), { label: 'Zobacz', run: () => (location.hash = '#/statystyki') });
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
    lesson = { key, sc, queue, total: queue.length, done: 0, hearts: MAX_HEARTS, correct: 0, wrong: 0, combo: 0, maxCombo: 0, start: Date.now(), state: 'ask', sel: null, finished: false };
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
    lesson = { key, sc, queue, total: queue.length, done: 0, hearts: MAX_HEARTS, correct: 0, wrong: 0, combo: 0, maxCombo: 0, start: Date.now(), retried: new Set(), state: 'ask', sel: null, finished: false };
  }
  renderExercise();
}

function lessonTop() {
  const L = lesson;
  return `<div class="session-top lesson-top">
      <a class="icon-btn" href="#/" aria-label="Zakończ lekcję">${ICONS.close}</a>
      <div class="session-progress">${progressBar(L.done / L.total, 'Postęp lekcji')}</div>
      <span class="hearts" aria-label="Serca: ${L.hearts}">${ICONS.heart}<b>${L.hearts}</b></span>
    </div>
    ${L.combo >= 3 ? `<p class="combo">${ICONS.flame} ${L.combo} z rzędu!</p>` : ''}`;
}

function renderExercise() {
  const L = lesson;
  document.body.classList.add('in-session', 'in-lesson');
  if (L.finished || !L.queue.length || L.hearts <= 0) return renderLessonEnd();
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
      if (!missed) { missed = true; L.hearts--; game.sound('bad'); app.querySelector('.hearts b').textContent = L.hearts; app.querySelector('.hearts').classList.add('lost'); }
      if (L.hearts <= 0) finishAnswer(false, '');
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
  if (ok) { L.correct++; L.combo++; L.maxCombo = Math.max(L.maxCombo, L.combo); game.sound('ok'); }
  else {
    L.wrong++; L.combo = 0;
    if (e.type !== 'match') { L.hearts--; game.sound('bad'); }
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
  app.querySelector('.hearts b').textContent = Math.max(0, L.hearts);
  if (!ok) app.querySelector('.hearts').classList.add('lost');
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
  const s = L.sc.s;
  const failed = L.hearts <= 0;
  const acc = L.correct + L.wrong ? L.correct / (L.correct + L.wrong) : 0;
  const perfect = !failed && L.wrong === 0;
  if (!L.finished) {
    L.finished = true;
    L.xp = failed ? Math.floor(L.correct / 2) : 10 + (perfect ? 5 : 0) + (L.maxCombo >= 5 ? 3 : 0);
    const st = store.get();
    st.lekcje ||= {};
    const r = st.lekcje[L.key] || { n: 0, best: 0 };
    if (!failed) { r.n++; r.best = Math.max(r.best || 0, pct(acc)); if (perfect) r.idealne = (r.idealne || 0) + 1; }
    st.lekcje[L.key] = r;
    store.markActivity();
    game.award(L.xp, { lekcje: failed ? 0 : 1, poprawne: L.correct, idealne: perfect ? 1 : 0 });
    if (!failed) { game.confetti(); game.sound('win'); }
  }
  document.body.classList.remove('in-lesson');
  const secs = Math.round((Date.now() - L.start) / 1000);
  app.innerHTML = `
    <section class="result lesson-end">
      <div class="result-icon ${failed ? 'sad' : ''}">${failed ? ICONS.heart : ICONS.trophy}</div>
      <h1>${failed ? 'Skończyły się serca' : perfect ? 'Bez ani jednego błędu' : 'Lekcja zaliczona'}</h1>
      <p class="lead">${failed ? 'Spróbuj jeszcze raz — pytania będą podobne.' : esc(L.sc.title)}</p>
      <div class="end-tiles">
        <div class="end-tile t-gold"><span>Zdobyte XP</span><strong>${ICONS.bolt}${L.xp}</strong></div>
        <div class="end-tile t-green"><span>Celność</span><strong>${ICONS.target}${pct(acc)}%</strong></div>
        <div class="end-tile t-blue"><span>Czas</span><strong>${ICONS.clock}${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, '0')}</strong></div>
      </div>
      ${L.maxCombo >= 3 ? `<p class="muted">Najdłuższa seria poprawnych odpowiedzi: <strong>${L.maxCombo}</strong></p>` : ''}
      <div class="actions">
        <a class="btn btn-primary btn-lg btn-cta" href="#/">Kontynuuj</a>
        <button type="button" class="btn btn-ghost btn-lg" id="again">${failed ? 'Spróbuj ponownie' : 'Jeszcze jedna lekcja'}</button>
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
  const training = mode === 'trening';
  const key = `${sid}/${type}/${id}/${mode || ''}`;
  if (!session || session.key !== key) {
    const queue = training
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
    <p class="session-label">${training ? 'Trening swobodny' : isNew ? '<span class="tag tag-new">Nowa fiszka</span>' : '<span class="tag">Powtórka</span>'}
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
        ${training ? `<a class="btn btn-primary btn-lg" href="#/fiszki/${base}/trening" data-restart>Kolejne 50 fiszek</a>` : ''}
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

function startTest(sc) {
  const qs = shuffle(scopeQuestions(sc)).slice(0, TEST_SIZE)
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
      <p class="eyebrow">Pytanie ${i + 1}${sc.type === 'd' ? ` · ${esc(u.nazwa)}` : ''}</p>
      <h2 class="question-text">${esc(q.pytanie)}</h2>
      <div class="options" role="group" aria-label="Odpowiedzi">
        ${order.map((oi, pos) => `<button type="button" class="option" data-oi="${oi}">
            <span class="option-letter">${LITERY[pos]}</span><span class="option-text">${esc(q.odpowiedzi[oi])}</span>
          </button>`).join('')}
      </div>
      <div id="feedback" aria-live="polite"></div>
      ${reportBtn(reportHref(sc.s, u, 'pytanie', q))}
    </section>`;

  app.querySelector('.options').addEventListener('click', (e) => {
    const b = e.target.closest('.option');
    if (b && test.answers[i] === undefined) answer(Number(b.dataset.oi));
  });
  if (test.answers[i] !== undefined) showFeedback();
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
  const { sc, qs, answers } = test;
  const s = sc.s;
  const score = qs.reduce((n, { q }, i) => n + (answers[i] === q.poprawna ? 1 : 0), 0);
  const p = pct(score / qs.length);
  if (!test.saved) {
    store.addTest({ sid: s.id, scope: `${sc.type}:${sc.id}`, name: sc.title, score, total: qs.length, at: Date.now() });
    test.saved = true;
    game.award(5 + (score === qs.length ? 5 : 0));
    if (p >= 70) { game.confetti(); game.sound('win'); }
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

const MATURA_TABS = [['proba', 'Próbna'], ['cke', 'Arkusze CKE'], ['dzialy', 'Działy'], ['autorskie', 'Autorskie']];
const scoreTag = (sc) => (sc.done ? `<span class="score ${sc.pkt / sc.max >= .7 ? 'ok' : sc.pkt / sc.max >= .5 ? 'warn' : 'bad'}">${pct(sc.pkt / sc.max)}%</span>` : '');

function taskRow(href, name, sc, right = '') {
  return `<a class="dzial-row" href="${href}">
    <div class="dzial-row-top"><span class="dzial-name">${esc(name)}</span>${scoreTag(sc)}</div>
    ${progressBar(sc.done / (sc.total || 1), `Rozwiązane zadania: ${name}`)}
    <div class="dzial-meta"><span>${sc.done}/${nZadan(sc.total)} rozwiązanych</span>${right}</div>
  </a>`;
}

function viewMatura(tab) {
  tab = MATURA_TABS.some(([k]) => k === tab) ? tab : 'proba';
  const s = currentSubject();
  if (!s) return notFound();
  let body = '';
  if (tab === 'proba') {
    body = examSection(s);
  } else if (tab === 'cke') {
    body = `<div class="dzial-list">${s.arkusze.map((a) => taskRow(`#/zadania/${enc(s.id)}/a/${enc(a.id)}`, a.nazwa, taskScore(s.id, a.zadania), `<span>${a.punkty} pkt</span>`)).join('')}</div>`
      || '<p class="muted">Brak arkuszy CKE.</p>';
  } else if (tab === 'dzialy') {
    body = `<p class="muted small">Zadania z arkuszy CKE i zadania autorskie z jednego działu.</p>
      <div class="dzial-list">${s.dzialy.map((d) => {
        const cke = tasksOf(s, d.id);
        const own = bankTasks(s, d.id);
        return `<div class="dzial-row dzial-both">
          <span class="dzial-name">${esc(d.nazwa)}</span>
          <div class="pop-row">
            ${cke.length ? `<a class="btn btn-ghost btn-sm" href="#/zadania/${enc(s.id)}/d/${enc(d.id)}">CKE <b>${cke.length}</b></a>` : ''}
            ${own.length ? `<a class="btn btn-ghost btn-sm" href="#/zadania/${enc(s.id)}/b/${enc(d.id)}">Autorskie <b>${own.length}</b></a>` : ''}
          </div>
        </div>`;
      }).join('')}</div>`;
  } else {
    const all = bankTasks(s);
    body = `<p class="muted small">${nZadan(all.length)} w ${s.bank.length} wiązkach — w formacie matury od 2026 r., z kluczem i zasadami oceniania.</p>
      <div class="dzial-list">${s.dzialy.map((d) => ({ d, list: bankTasks(s, d.id) })).filter((x) => x.list.length)
        .map(({ d, list }) => taskRow(`#/zadania/${enc(s.id)}/b/${enc(d.id)}`, d.nazwa, taskScore(s.id, list))).join('')}</div>`;
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

function renderTask() {
  const { s, list, i, title } = zs;
  document.body.classList.add('in-session');
  const z = list[i];
  const w = z.wiazka;
  const a = s.arkusze.find((x) => x.id === z.arkusz) || { nazwa: 'Zadanie autorskie Kolumba', zrodlo: w.zrodlo };
  const k = taskKey(s.id, z);
  const prev = store.get().zadania[k];
  const revealed = zs.revealed[k];

  app.innerHTML = `
    <div class="session-top">
      <a class="icon-btn" href="#/matura/${{ a: 'cke', b: 'autorskie', d: 'dzialy' }[zs.key.split('/')[1]] || 'proba'}" aria-label="Zamknij">${ICONS.close}</a>
      <div class="session-progress">${progressBar((i + 1) / list.length, 'Postęp')}</div>
      <span class="session-count">${i + 1}/${list.length}</span>
    </div>
    <p class="eyebrow">${esc(title)}${title !== a.nazwa ? ` · ${esc(a.nazwa)}` : ''}</p>
    <h1 class="task-title">Zadanie ${esc(z.nr)} <span class="muted">(0–${z.punkty} pkt)</span>${prev ? ` <span class="tag tag-ok">${prev.pkt}/${prev.max} pkt</span>` : ''}</h1>

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
  const btns = Array.from({ length: z.punkty + 1 }, (_, p) =>
    `<button type="button" class="btn btn-score ${prev && prev.pkt === p ? 'active' : ''}" data-pkt="${p}">${p} pkt</button>`).join('');
  return `<section class="card key">
      <h2 class="card-title">${ICONS.check} ${String(z.arkusz).startsWith(BANK_PREFIX) ? 'Przykładowa odpowiedź (klucz Kolumba)' : 'Odpowiedź według klucza CKE'}</h2>
      ${pre(z.odpowiedz || '—')}
      ${z.zasady ? `<details class="rules"><summary>Zasady oceniania</summary>${pre(z.zasady)}</details>` : ''}
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
    <h2 class="card-title">Próbna matura · 180 minut</h2>
    <p class="muted">Arkusz ułożony jak matura od 2026 r.: ok. 50 pkt, kilkanaście wiązek z różnych działów (w proporcjach z arkuszy CKE 2026), na końcu zadanie rozszerzonej odpowiedzi za 7 pkt. Baza: ${nZadan(s.bank.reduce((n, w) => n + w.zadania.length, 0))} autorskich${cke ? ` + ${nZadan(tasksOf(s).length)} CKE` : ''}.</p>
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
        <div class="review-foot"><span class="source">${esc(w.zrodlo)}</span>${reportBtn(mailto(`[Kolumb] Błąd w zadaniu: ${w.id}/${z.nr}`, ['Dzień dobry,', '', `zgłaszam błąd w zadaniu ${w.id}/${z.nr} (${w.zrodlo}).`, '', `Polecenie: ${z.polecenie}`, '', `Klucz: ${z.odpowiedz}`, '', 'Na czym polega błąd:', '']))}</div>
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

// ---------- profil, logowanie i wybór przedmiotu ----------
const initials = (n) => (String(n).trim().split(/\s+/).map((w) => w[0]).join('').slice(0, 2) || '?').toUpperCase();
const avatar = (p, big) => `<span class="avatar ${big ? 'avatar-lg' : ''}" style="--av:${esc(p.color)}" aria-hidden="true">${esc(initials(p.name))}</span>`;
const SUBJECT_ICONS = {
  wos: '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6 6 15v3h36v-3z" fill="currentColor"/><path d="M10 21h4v15h-4zM18 21h4v15h-4zM26 21h4v15h-4zM34 21h4v15h-4z" fill="currentColor" opacity=".85"/><path d="M6 38h36v4H6z" fill="currentColor"/></svg>',
};
const subjectIcon = (s) => SUBJECT_ICONS[s.id] || `<span class="subj-letters">${esc((s.skrot || s.nazwa).slice(0, 3))}</span>`;
let gateMsg = '';

function afterProfileChange() {
  session = test = zs = lesson = null;
  applyTheme();
  updateTopStats();
}

// Ekran logowania: wybór profilu na urządzeniu albo logowanie e-mailem (gdy konta są włączone).
function viewKonto() {
  document.body.classList.add('in-gate');
  const list = store.profileList();
  app.innerHTML = `<section class="gate">
    <img class="gate-logo" src="ikony/ikona.svg" width="76" height="76" alt="Kolumb">
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
    <h1 class="gate-title">Wybierz przedmiot</h1>
    <div class="subj-grid">${subjects.map((s) => `<button type="button" class="subj-tile ${s.id === cur ? 'active' : ''}" data-sid="${esc(s.id)}" aria-label="${esc(s.nazwa)}">
        <span class="subj-icon">${subjectIcon(s)}</span><span class="subj-name">${esc(s.skrot || s.nazwa)}</span></button>`).join('')}</div>
    <button type="button" class="link-btn" data-act="logout">Zmień profil</button>
  </section>`;
  app.querySelector('.subj-grid').addEventListener('click', (e) => {
    const b = e.target.closest('[data-sid]');
    if (!b) return;
    store.get().settings.przedmiot = b.dataset.sid;
    store.save();
    game.sound('tap');
    location.hash = '#/';
  });
  app.querySelector('[data-act="logout"]').addEventListener('click', () => { store.logout(); location.hash = '#/konto'; });
}

function profileHeadHtml(xp, lv) {
  const prof = store.activeProfile();
  const acc = cloud.account();
  return `<section class="profile-head">
    ${avatar(prof, true)}
    <div class="profile-meta"><h1>${esc(prof.name)}</h1><span class="muted">${acc ? esc(acc.email) : 'Profil na tym urządzeniu'}</span>
      <div class="lv-row"><b>Poziom ${lv}</b>${progressBar((xp - game.levelFloor(lv)) / (game.levelFloor(lv + 1) - game.levelFloor(lv)), 'Postęp do następnego poziomu')}<small>${xp} XP</small></div></div>
  </section>`;
}

function connectHtml() {
  if (!cloud.enabled() || cloud.account()) return '';
  return `<details class="card connect"><summary class="card-title">Zapisuj postępy na koncie</summary>
    <form class="gate-form" id="acc-form" novalidate>
      <p class="muted small">Zaloguj się, aby mieć te same postępy na każdym urządzeniu.</p>
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
        viewStats();
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

  const xp = game.xpTotal();
  const lv = game.level(xp);
  const lvA = game.levelFloor(lv), lvB = game.levelFloor(lv + 1);
  const week = [];
  for (let k = 6; k >= 0; k--) {
    const t = store.addDays(store.startOfDay(), -k);
    week.push({ t, xp: state.daily?.[store.dayKey(t)]?.xp || 0 });
  }
  const wMax = Math.max(game.goal(), ...week.map((w) => w.xp));
  const wfmt = new Intl.DateTimeFormat('pl-PL', { weekday: 'short' });
  const got = state.odznaki || {};
  app.innerHTML = `
    ${profileHeadHtml(xp, lv)}
    <section class="card">
      <h2 class="card-title">XP w tym tygodniu</h2>
      <div class="week" role="list">${week.map((w) => `<div class="week-day ${w.xp >= game.goal() ? 'hit' : ''}" role="listitem" aria-label="${wfmt.format(w.t)}: ${w.xp} XP">
        <span class="week-val">${w.xp || ''}</span>
        <div class="week-bar"><span style="height:${Math.round((w.xp / wMax) * 100)}%"></span></div>
        <small>${wfmt.format(w.t).replace('.', '')}</small></div>`).join('')}</div>
      <p class="muted small">Cel dnia: ${game.goal()} XP — dni z osiągniętym celem są wyróżnione.</p>
    </section>
    <section class="card">
      <h2 class="card-title">Odznaki · ${Object.keys(got).length}/${game.BADGES.length}</h2>
      <div class="medals" role="list">${[...game.BADGES].sort((x, y) => (got[y.id] ? 1 : 0) - (got[x.id] ? 1 : 0)).map((b) => `<div role="listitem" class="medal ${got[b.id] ? 'got' : ''}" title="${esc(b.opis)}">
          <span class="badge-medal">${got[b.id] ? ICONS.trophy : ICONS.star}</span><small>${esc(b.name)}</small></div>`).join('')}</div>
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

// ---------- ustawienia ----------
function viewSettings() {
  const settings = store.get().settings;
  const theme = settings.theme;
  const npd = Number(settings.newPerDay) || 20;
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
      <p class="muted">Ile nowych fiszek z każdego przedmiotu dochodzi codziennie do nauki (powtórki są zawsze bez limitu).</p>
      <div class="segmented seg-4" role="radiogroup" aria-label="Nowe fiszki dziennie">
        ${[10, 20, 30, 50].map((v) => `<button type="button" role="radio" aria-checked="${npd === v}" class="${npd === v ? 'active' : ''}" data-npd="${v}">${v}</button>`).join('')}
      </div>
    </section>

    <section class="card">
      <h2 class="card-title">Nazwa profilu</h2>
      <div class="pop-row"><input class="type-input" id="pname" maxlength="30" value="${esc(store.activeProfile().name)}" aria-label="Nazwa profilu"><button type="button" class="btn btn-ghost btn-sm" data-act="rename">Zapisz</button></div>
    </section>

    <section class="card">
      <h2 class="card-title">Dzienny cel XP</h2>
      <p class="muted">Lekcja to ok. 10–15 XP, fiszka 1–2 XP, poprawna odpowiedź w teście 2 XP.</p>
      <div class="segmented seg-4" role="radiogroup" aria-label="Dzienny cel XP">
        ${game.GOALS.map((v) => `<button type="button" role="radio" aria-checked="${game.goal() === v}" class="${game.goal() === v ? 'active' : ''}" data-goal="${v}">${v}</button>`).join('')}
      </div>
    </section>

    <section class="card">
      <h2 class="card-title">Dźwięki</h2>
      <div class="segmented seg-2" role="radiogroup" aria-label="Dźwięki">
        ${[[true, 'Włączone'], [false, 'Wyłączone']].map(([v, l]) => `<button type="button" role="radio" aria-checked="${(settings.sound !== false) === v}" class="${(settings.sound !== false) === v ? 'active' : ''}" data-sound="${v}">${l}</button>`).join('')}
      </div>
    </section>

    ${standalone ? '' : `<section class="card">
      <h2 class="card-title">Aplikacja na ekranie głównym</h2>
      ${installEvent ? '<button type="button" class="btn btn-gold btn-lg" data-act="install">Zainstaluj Kolumba</button>'
        : ios ? '<p>Na iPhonie lub iPadzie otwórz stronę w Safari, stuknij <strong>Udostępnij</strong>, a potem <strong>Do ekranu początkowego</strong>.</p>'
        : '<p>Otwórz menu przeglądarki i wybierz <strong>Zainstaluj aplikację</strong> lub <strong>Dodaj do ekranu głównego</strong>.</p>'}
      <p class="muted">Po instalacji Kolumb działa także bez internetu.</p>
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
      <h2 class="card-title">O aplikacji</h2>
      <p><strong>Kolumb</strong> — fiszki, testy i zadania maturalne. Fiszki wracają według systemu Leitnera: te, których nie znasz, pojawiają się szybko, a opanowane — coraz rzadziej.</p>
      <p class="muted">Zauważyłeś błąd w treści? Użyj przycisku „Zgłoś błąd” albo napisz na <a href="mailto:${REPORT_EMAIL}">${REPORT_EMAIL}</a>.</p>
    </section>`;

  app.querySelectorAll('.segmented').forEach((seg) => seg.addEventListener('click', (e) => {
    const b = e.target.closest('button');
    if (!b) return;
    if (b.dataset.themeSet) {
      settings.theme = b.dataset.themeSet;
      applyTheme();
    }
    if (b.dataset.npd) settings.newPerDay = Number(b.dataset.npd);
    if (b.dataset.goal) settings.dailyGoal = Number(b.dataset.goal);
    if (b.dataset.sound) { settings.sound = b.dataset.sound === 'true'; game.sound('ok'); }
    store.save();
    viewSettings();
  }));
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
    a.download = `kolumb-postepy-${store.dayKey()}.json`;
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
      toast('To nie jest poprawny plik kopii Kolumba.');
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
  document.querySelector('meta[name="theme-color"]').setAttribute('content', dark ? '#0f1a2d' : '#ffffff');
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
  toast('Kolumb zainstalowany!');
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
  [/^#\/fiszki\/([^/]+)\/(d|p)\/([^/]+)(?:\/(trening))?$/, viewFiszki],
  [/^#\/test\/([^/]+)\/(d|p)\/([^/]+)$/, viewTest],
  [/^#\/lekcja\/([^/]+)\/(d|p)\/([^/]+)$/, viewLekcja],
  [/^#\/bledy\/([^/]+)$/, viewBledy],
  [/^#\/szukaj$/, viewSzukaj],
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
];

let lastHash = null;
function route() {
  const hash = location.hash || '#/';
  const changed = hash !== lastHash;
  lastHash = hash;
  keyHandler = null;
  document.body.classList.remove('in-session', 'in-lesson', 'in-gate');
  if (!hash.startsWith('#/lekcja/') && !hash.startsWith('#/bledy/')) lesson = null;
  if (!hash.startsWith('#/fiszki/')) session = null;
  if (!hash.startsWith('#/test/')) test = null;
  if (!hash.startsWith('#/zadania/')) zs = null;
  if (!hash.startsWith('#/egzamin/')) clearInterval(examTimer);

  // bramka: najpierw logowanie (profil), potem wybór przedmiotu
  const gate = !store.loggedIn() ? viewKonto : !store.get().settings.przedmiot && subjects.length && !/^#\/(przedmiot|start)$/.test(hash) ? viewPrzedmiot : null;
  const hit = gate ? null : routes.find(([re]) => re.test(hash));
  if (gate) gate();
  else if (hit) {
    const m = hash.match(hit[0]);
    hit[1](...m.slice(1).map((x) => (x === undefined ? undefined : decodeURIComponent(x))));
  } else notFound();

  const tab = /^#\/(statystyki|profil|ustawienia)/.test(hash) ? 'stats'
    : hash.startsWith('#/matura') || hash.startsWith('#/zadania') || hash.startsWith('#/egzamin') ? 'matura'
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
  if (e.key === 'Escape' && document.body.classList.contains('in-session')) {
    app.querySelector('.session-top .icon-btn')?.click();
    return;
  }
  keyHandler?.(e);
});

// ---------- start ----------
async function init() {
  applyTheme();
  game.onChange(onGameEvents);
  cloud.startAutoSync(() => {});
  updateTopStats();
  try {
    ({ subjects, errors: loadErrors } = await loadSubjects());
  } catch (e) {
    app.innerHTML = `<div class="empty"><div class="empty-icon">${ICONS.compass}</div>
      <h1>Nie udało się wczytać treści</h1>
      <p>Sprawdź połączenie z internetem i spróbuj ponownie.</p>
      <p class="muted"><small>${esc(e.message)}</small></p>
      <button type="button" class="btn btn-primary" onclick="location.reload()">Spróbuj ponownie</button></div>`;
    return;
  }
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
            toast('Dostępna nowa wersja Kolumba.', { label: 'Odśwież', run: () => location.reload() });
          }
        });
      });
    }).catch(() => {});
  });
}

init();
