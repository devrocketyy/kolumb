// Kolumb — aplikacja do nauki do matury.
import * as store from './store.js';
import { loadSubjects } from './data.js';
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
    <h1>Zboczyliśmy z kursu</h1>
    <p>Nie znaleziono tej strony. Być może treści zostały zmienione.</p>
    <a class="btn btn-primary" href="#/">Wróć na start</a></div>`;
}

// ---------- ekran główny ----------
function greeting() {
  const h = new Date().getHours();
  if (h < 5) return 'Nocna wachta';
  if (h < 12) return 'Dzień dobry';
  if (h < 18) return 'Cześć';
  return 'Dobry wieczór';
}

function viewHome() {
  let todo = 0;
  const cardsHtml = subjects.map((s) => {
    const allowance = newAllowance(s.id);
    todo += summary(s.id, allUnits(s), allowance).todo;
    const rows = s.dzialy.map((d) => unitRow(hrefDzial(s.id, d.id), d.nazwa, summary(s.id, d.poddzialy, allowance)));
    const nTasks = tasksOf(s).length;
    return `<section class="subject-card">
      <div class="subject-head">
        <span class="subject-icon" aria-hidden="true">${esc(s.ikona)}</span>
        <div><h2>${esc(s.nazwa)}</h2>${s.opis ? `<p>${esc(s.opis)}</p>` : ''}</div>
      </div>
      <div class="dzial-list">${rows.join('')}</div>
      ${nTasks ? `<a class="btn btn-ghost btn-lg subject-exam" href="#/matura">${ICONS.exam}<span>Zadania maturalne · ${nZadan(nTasks)}</span></a>` : ''}
    </section>`;
  });

  const st = store.streak();
  const showInstall = installEvent && !store.get().settings.installDismissed;

  app.innerHTML = `
    <section class="hero">
      <div class="hero-bg" aria-hidden="true">${ICONS.compass}</div>
      <p class="eyebrow">${greeting()}!</p>
      <h1>Wyznacz dziś kurs na maturę</h1>
      <div class="hero-stats">
        <div class="hero-stat"><strong>${todo}</strong><span>dziś do powtórki</span></div>
        <a class="hero-stat" href="#/statystyki">
          <strong>${ICONS.flame}${st.current}</strong>
          <span>${plural(st.current, 'dzień', 'dni', 'dni')} serii${st.current && !st.today ? ' — ucz się dziś, by ją utrzymać' : ''}</span>
        </a>
      </div>
    </section>
    ${showInstall ? `<div class="install-banner">
        <div><strong>Zainstaluj Kolumba</strong><span>Ikona na ekranie głównym i nauka bez internetu.</span></div>
        <div class="install-actions">
          <button type="button" class="btn btn-gold btn-sm" data-act="install">Zainstaluj</button>
          <button type="button" class="icon-btn" data-act="dismiss" aria-label="Nie teraz">${ICONS.close}</button>
        </div></div>` : ''}
    ${loadErrors.length ? `<div class="alert">Nie udało się wczytać: ${esc(loadErrors.join('; '))}</div>` : ''}
    <h2 class="section-title">Przedmioty</h2>
    <div class="subjects">${cardsHtml.join('') || '<p class="muted">Brak przedmiotów. Dodaj plik JSON do katalogu <code>przedmioty/</code>.</p>'}</div>
  `;

  app.querySelector('[data-act="install"]')?.addEventListener('click', promptInstall);
  app.querySelector('[data-act="dismiss"]')?.addEventListener('click', () => {
    store.get().settings.installDismissed = true;
    store.save();
    viewHome();
  });
}

// ---------- dział i poddział ----------
function learnActions(sc, sm) {
  const base = scopePath(sc);
  const nQ = Math.min(TEST_SIZE, scopeQuestions(sc).length);
  const total = sc.units.reduce((n, u) => n + u.fiszki.length, 0);
  let fiszki = '';
  if (total) {
    fiszki = sm.todo
      ? `<a class="btn btn-primary btn-xl" href="#/fiszki/${base}">${ICONS.cards}<span>Fiszki<small>${nFiszek(sm.todo)} na dziś</small></span></a>`
      : `<div class="done-note">${ICONS.check}<span>${sm.fresh ? 'Dzienny limit nowych fiszek wykorzystany. Wróć jutro albo poćwicz swobodnie.' : 'Na dziś wszystko powtórzone! Wróć jutro albo poćwicz swobodnie.'}</span></div>`;
    fiszki += `<a class="btn ${sm.todo ? 'btn-ghost' : 'btn-primary'} btn-xl" href="#/fiszki/${base}/trening">${ICONS.cards}<span>Trening swobodny<small>losowe fiszki, bez wpływu na harmonogram</small></span></a>`;
  }
  return `${fiszki}
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
    ${pageHead(d.nazwa, '#/', s.nazwa)}
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
  store.save();
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
      <h1>${reviewed ? 'Ziemia na horyzoncie!' : 'Na dziś wszystko!'}</h1>
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
  store.save();
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
    store.save();
    test.saved = true;
  }
  const msg = p >= 90 ? 'Mistrzowska nawigacja!' : p >= 70 ? 'Dobry kurs — tak trzymaj!' : p >= 50 ? 'Połowa drogi za Tobą.' : 'Sztorm — powtórz fiszki i spróbuj ponownie.';
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

function viewMatura() {
  const withTasks = subjects.filter((s) => s.arkusze.length);
  app.innerHTML = `
    ${pageHead('Zadania maturalne', null, 'Arkusze CKE')}
    <p class="lead">Próbne matury na czas oraz prawdziwe zadania z arkuszy CKE z kluczem odpowiedzi.</p>
    ${subjects.filter((s) => s.bank.length || s.arkusze.length).map(examSection).join('')}
    ${subjects.filter((s) => s.bank.length).map((s) => {
      const byD = s.dzialy.map((d) => ({ d, list: bankTasks(s, d.id) })).filter((x) => x.list.length);
      return `<section class="card"><h2 class="card-title">Trening: zadania autorskie</h2>
        <p class="muted">Ćwicz wiązki zadań z jednego działu bez limitu czasu — od razu z kluczem i samooceną.</p>
        <div class="dzial-list">${byD.map(({ d, list }) => {
          const sc = taskScore(s.id, list);
          return `<a class="dzial-row" href="#/zadania/${enc(s.id)}/b/${enc(d.id)}">
            <div class="dzial-row-top"><span class="dzial-name">${esc(d.nazwa)}</span>${sc.done ? `<span class="score ${sc.pkt / sc.max >= .7 ? 'ok' : sc.pkt / sc.max >= .5 ? 'warn' : 'bad'}">${pct(sc.pkt / sc.max)}%</span>` : ''}</div>
            ${progressBar(sc.done / (sc.total || 1), `Rozwiązane zadania autorskie: ${d.nazwa}`)}
            <div class="dzial-meta"><span>${sc.done}/${nZadan(sc.total)} rozwiązanych</span></div>
          </a>`;
        }).join('')}</div></section>`;
    }).join('')}
    <h2 class="section-title">Arkusze CKE</h2>
    ${withTasks.map((s) => {
      const byDzial = s.dzialy.map((d) => ({ d, n: tasksOf(s, d.id).length })).filter((x) => x.n);
      return `<section class="card">
        <h2 class="card-title">${esc(s.ikona)} ${esc(s.nazwa)}</h2>
        <div class="dzial-list">${s.arkusze.map((a) => {
          const sc = taskScore(s.id, a.zadania);
          return `<a class="dzial-row" href="#/zadania/${enc(s.id)}/a/${enc(a.id)}">
            <div class="dzial-row-top"><span class="dzial-name">${esc(a.nazwa)}</span>${sc.done ? `<span class="score ${sc.pkt / sc.max >= .7 ? 'ok' : sc.pkt / sc.max >= .5 ? 'warn' : 'bad'}">${pct(sc.pkt / sc.max)}%</span>` : ''}</div>
            ${progressBar(sc.done / (sc.total || 1), `Rozwiązane zadania: ${a.nazwa}`)}
            <div class="dzial-meta"><span>${sc.done}/${nZadan(sc.total)} rozwiązanych</span><span>${a.punkty} pkt</span></div>
          </a>`;
        }).join('')}</div>
        ${byDzial.length ? `<h3 class="sub-title">Według działów</h3>
          <div class="chips">${byDzial.map(({ d, n }) => `<a class="chip" href="#/zadania/${enc(s.id)}/d/${enc(d.id)}">${esc(d.nazwa)} <b>${n}</b></a>`).join('')}</div>` : ''}
      </section>`;
    }).join('') || '<p class="muted">Brak zadań maturalnych w treściach.</p>'}`;
  subjects.filter((s) => s.bank.length || s.arkusze.length).forEach(bindExamSection);
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
      <a class="icon-btn" href="#/matura" aria-label="Zamknij">${ICONS.close}</a>
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
    store.get().zadania[k] = { pkt: Number(b.dataset.pkt), max: z.punkty, at: Date.now() };
    store.markActivity();
    store.save();
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
const DEFAULT_WAGI = { spoleczenstwo: 10, obywatel: 5, polityka: 4, 'ustroj-rp': 7, 'systemy-panstw': 6, prawo: 7, 'prawa-czlowieka': 3, miedzynarodowe: 5, ue: 3 };

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

// Układa arkusz: ok. 48 pkt w krótkich wiązkach (proporcje działów jak na maturze) + zadania za 5 i 7 pkt.
function buildExam(s, seed, cke) {
  const r = rng(seed);
  const pool = examPool(s, cke);
  const shortW = pool.filter((w) => !isExt(w));
  const ext5 = seededShuffle(pool.filter((w) => isExt(w) && wPts(w) === 5), r);
  const ext7 = seededShuffle(pool.filter((w) => isExt(w) && wPts(w) >= 6), r);
  const wagi = s.wagi || DEFAULT_WAGI;
  const sum = Object.values(wagi).reduce((a, b) => a + b, 0);
  const byD = {};
  seededShuffle(shortW, r).forEach((w) => (byD[w.dzial] ||= []).push(w));
  const quota = {};
  Object.keys(wagi).forEach((d) => (quota[d] = (wagi[d] / sum) * 48));
  const picked = [];
  let total = 0;
  let progress = true;
  while (total < 47 && progress) {
    progress = false;
    for (const d of seededShuffle(Object.keys(wagi), r)) {
      if (total >= 48) break;
      const list = byD[d] || [];
      if (!list.length || quota[d] <= 0.5) continue;
      const w = list.shift();
      picked.push(w); total += wPts(w); quota[d] -= wPts(w); progress = true;
    }
  }
  if (total < 47) { // brak zadań w części działów — dobierz z dowolnych
    const rest = Object.values(byD).flat();
    while (total < 47 && rest.length) { const w = rest.shift(); picked.push(w); total += wPts(w); }
  }
  const order = s.dzialy.map((d) => d.id);
  picked.sort((a, b) => order.indexOf(a.dzial) - order.indexOf(b.dzial));
  const ext = [ext5[0], ext7[0]].filter(Boolean);
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
    <p class="muted">Arkusz ułożony jak prawdziwa matura: ok. 20 wiązek z różnych działów (w proporcjach z egzaminów CKE), na końcu zadania za 5 i 7 pkt. Baza: ${nZadan(s.bank.reduce((n, w) => n + w.zadania.length, 0))} autorskich${cke ? ` + ${nZadan(tasksOf(s).length)} CKE` : ''}.</p>
    <label class="switch"><input type="checkbox" id="exam-cke" ${cke ? 'checked' : ''}> <span>Dobieraj też zadania z arkuszy CKE</span></label>
    <button type="button" class="btn btn-gold btn-lg" id="exam-random">Losowa próbna matura</button>
    <h3 class="sub-title">Ponumerowane próbne matury</h3>
    <div class="exam-grid">${numbered.map((n) => {
      const e = st[`${s.id}-nr${n}-${cke ? 'c' : 'a'}`];
      return `<a class="exam-tile ${e?.koniec ? 'done' : e ? 'open' : ''}" href="#/egzamin/${enc(s.id)}/${enc(`nr${n}-${cke ? 'c' : 'a'}`)}"><strong>${n}</strong><span>${res(e) || 'rozpocznij'}</span></a>`;
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
    const m = key.match(/^nr(\d+)-(c|a)$/);
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
  store.save();
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

  app.innerHTML = `
    ${pageHead('Statystyki', null, 'Dziennik pokładowy')}
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
      }).join('')}</ul>` : '<p class="muted">Nie masz jeszcze żadnego testu. Rozwiąż pierwszy w wybranym dziale!</p>'}
    </section>`;
}

// ---------- ustawienia ----------
function viewSettings() {
  const settings = store.get().settings;
  const theme = settings.theme;
  const npd = Number(settings.newPerDay) || 20;
  const ios = /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  const standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  app.innerHTML = `
    ${pageHead('Ustawienia', null, 'Kajuta kapitana')}
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
      <button type="button" class="btn btn-danger btn-lg" data-act="reset">Wyzeruj wszystkie postępy</button>
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
    store.save();
    viewSettings();
  }));
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
  document.querySelector('meta[name="theme-color"]').setAttribute('content', dark ? '#0a1428' : '#13274d');
  const btn = document.getElementById('theme-toggle');
  btn.setAttribute('aria-label', dark ? 'Włącz jasny motyw' : 'Włącz ciemny motyw');
  btn.dataset.dark = String(dark);
}

document.getElementById('theme-toggle').addEventListener('click', () => {
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
  [/^#\/lista\/([^/]+)\/([^/]+)$/, viewLista],
  [/^#\/matura$/, viewMatura],
  [/^#\/zadania\/([^/]+)\/(a|d|b)\/([^/]+)$/, viewZadania],
  [/^#\/egzamin\/([^/]+)\/([^/]+)$/, viewEgzamin],
  [/^#\/statystyki$/, viewStats],
  [/^#\/ustawienia$/, viewSettings],
];

let lastHash = null;
function route() {
  const hash = location.hash || '#/';
  const changed = hash !== lastHash;
  lastHash = hash;
  keyHandler = null;
  document.body.classList.remove('in-session');
  if (!hash.startsWith('#/fiszki/')) session = null;
  if (!hash.startsWith('#/test/')) test = null;
  if (!hash.startsWith('#/zadania/')) zs = null;
  if (!hash.startsWith('#/egzamin/')) clearInterval(examTimer);

  const hit = routes.find(([re]) => re.test(hash));
  if (hit) {
    const m = hash.match(hit[0]);
    hit[1](...m.slice(1).map((x) => (x === undefined ? undefined : decodeURIComponent(x))));
  } else notFound();

  const tab = hash.startsWith('#/statystyki') ? 'stats'
    : hash.startsWith('#/ustawienia') ? 'settings'
    : hash.startsWith('#/matura') || hash.startsWith('#/zadania') || hash.startsWith('#/egzamin') ? 'matura' : 'home';
  document.querySelectorAll('.tabbar a').forEach((a) => {
    const on = a.dataset.tab === tab;
    a.classList.toggle('active', on);
    if (on) a.setAttribute('aria-current', 'page');
    else a.removeAttribute('aria-current');
  });
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
