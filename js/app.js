// Kolumb — aplikacja do nauki do matury.
import * as store from './store.js';
import { loadSubjects } from './data.js';
import { cardKey, nextState, intervalLabel, dzialSummary, buildQueue, MASTERED_BOX } from './srs.js';

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

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

const pct = (x) => Math.round(x * 100);
const findSubject = (sid) => subjects.find((s) => s.id === sid);
const findDzial = (s, did) => s?.dzialy.find((d) => d.id === did);
const dHref = (sid, did) => `#/d/${encodeURIComponent(sid)}/${encodeURIComponent(did)}`;

const ICONS = {
  compass: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.25" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 8.2 13.4 13.4 8.2 15.8 10.6 10.6Z" fill="currentColor"/></svg>',
  chart: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
  gear: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.5 5.5l1.7 1.7M16.8 16.8l1.7 1.7M5.5 18.5l1.7-1.7M16.8 7.2l1.7-1.7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
  back: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>',
  flag: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 21V4m0 0h11l-2 4 2 4H5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  cards: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="14" height="14" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M7 3h11.5A2.5 2.5 0 0 1 21 5.5V17" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
  quiz: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.25" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M9.5 9.3a2.6 2.6 0 1 1 3.6 2.4c-.7.3-1.1.9-1.1 1.6v.4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="12" cy="17" r="1.1" fill="currentColor"/></svg>',
  book: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5zM4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
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
function reportHref(subject, dzial, kind, item) {
  const lines = [
    'Dzień dobry,',
    '',
    `zgłaszam błąd w ${kind === 'fiszka' ? 'fiszce' : 'pytaniu testowym'} w aplikacji Kolumb.`,
    '',
    `Przedmiot: ${subject.nazwa}`,
    `Dział: ${dzial.nazwa}`,
    `ID: ${subject.id}/${dzial.id}/${item.id}`,
    '',
  ];
  if (kind === 'fiszka') {
    lines.push(`Pytanie: ${item.przod}`, `Odpowiedź: ${item.tyl}`);
  } else {
    lines.push(`Pytanie: ${item.pytanie}`);
    item.odpowiedzi.forEach((o, i) => lines.push(`${LITERY[i]}) ${o}${i === item.poprawna ? '  ← oznaczona jako poprawna' : ''}`));
    if (item.wyjasnienie) lines.push(`Wyjaśnienie: ${item.wyjasnienie}`);
  }
  lines.push(`Źródło: ${item.zrodlo || '—'}`, '', 'Na czym polega błąd:', '', '');
  const subj = `[Kolumb] Błąd: ${subject.skrot} — ${kind} ${item.id}`;
  return `mailto:${REPORT_EMAIL}?subject=${encodeURIComponent(subj)}&body=${encodeURIComponent(lines.join('\n'))}`;
}

const reportBtn = (href) =>
  `<a class="btn-report" href="${esc(href)}">${ICONS.flag}<span>Zgłoś błąd</span></a>`;

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

function notFound() {
  app.innerHTML = `<div class="empty">
    <div class="empty-icon">${ICONS.compass}</div>
    <h1>Zboczyliśmy z kursu</h1>
    <p>Nie znaleziono tego działu. Być może treści zostały zmienione.</p>
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
  const rows = subjects.map((s) => {
    const items = s.dzialy.map((d) => {
      const sm = dzialSummary(s.id, d);
      todo += sm.todo;
      return `<a class="dzial-row" href="${dHref(s.id, d.id)}">
        <div class="dzial-row-top">
          <span class="dzial-name">${esc(d.nazwa)}</span>
          ${sm.todo ? `<span class="badge">${sm.todo}</span>` : `<span class="badge badge-ok" aria-label="Na dziś gotowe">${ICONS.check}</span>`}
        </div>
        ${progressBar(sm.progress, `Opanowanie działu ${d.nazwa}`)}
        <div class="dzial-meta">
          <span>${pct(sm.progress)}% opanowania</span>
          <span>${sm.mastered}/${sm.total} ${plural(sm.total, 'fiszka', 'fiszki', 'fiszek')}</span>
        </div>
      </a>`;
    });
    return `<section class="subject-card">
      <div class="subject-head">
        <span class="subject-icon" aria-hidden="true">${esc(s.ikona)}</span>
        <div><h2>${esc(s.nazwa)}</h2>${s.opis ? `<p>${esc(s.opis)}</p>` : ''}</div>
      </div>
      <div class="dzial-list">${items.join('')}</div>
    </section>`;
  });

  const st = store.streak();
  const settings = store.get().settings;
  const showInstall = installEvent && !settings.installDismissed;

  app.innerHTML = `
    <section class="hero">
      <div class="hero-bg" aria-hidden="true">${ICONS.compass}</div>
      <p class="eyebrow">${greeting()}!</p>
      <h1>Wyznacz dziś kurs na maturę</h1>
      <div class="hero-stats">
        <div class="hero-stat">
          <strong>${todo}</strong>
          <span>dziś do powtórki</span>
        </div>
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
    <div class="subjects">${rows.join('') || '<p class="muted">Brak przedmiotów. Dodaj plik JSON do katalogu <code>przedmioty/</code>.</p>'}</div>
  `;

  app.querySelector('[data-act="install"]')?.addEventListener('click', promptInstall);
  app.querySelector('[data-act="dismiss"]')?.addEventListener('click', () => {
    store.get().settings.installDismissed = true;
    store.save();
    viewHome();
  });
}

// ---------- ekran działu ----------
function viewDzial(sid, did) {
  const s = findSubject(sid);
  const d = findDzial(s, did);
  if (!d) return notFound();
  const sm = dzialSummary(s.id, d);
  const tests = store.get().tests.filter((t) => t.sid === s.id && t.did === d.id);
  const last = tests[tests.length - 1];
  const best = tests.reduce((m, t) => Math.max(m, t.score / t.total), 0);
  const base = `${encodeURIComponent(s.id)}/${encodeURIComponent(d.id)}`;
  const nQ = Math.min(TEST_SIZE, d.pytania.length);

  app.innerHTML = `
    ${pageHead(d.nazwa, '#/', s.nazwa)}
    ${d.opis ? `<p class="lead">${esc(d.opis)}</p>` : ''}
    <section class="card">
      <div class="ring-row">
        <div class="ring" style="--p:${pct(sm.progress)}"><span>${pct(sm.progress)}%</span></div>
        <div class="ring-text"><strong>Opanowanie działu</strong>
          <span>${sm.mastered} z ${sm.total} ${plural(sm.total, 'fiszki', 'fiszek', 'fiszek')} opanowanych na dłużej</span></div>
      </div>
      <div class="mini-stats">
        <div><strong>${sm.due}</strong><span>do powtórki</span></div>
        <div><strong>${sm.newToday}</strong><span>nowe na dziś</span></div>
        <div><strong>${sm.fresh}</strong><span>jeszcze nieznane</span></div>
      </div>
    </section>

    <div class="actions">
      ${d.fiszki.length ? (sm.todo
        ? `<a class="btn btn-primary btn-xl" href="#/fiszki/${base}">${ICONS.cards}<span>Fiszki<small>${sm.todo} ${plural(sm.todo, 'fiszka', 'fiszki', 'fiszek')} na dziś</small></span></a>`
        : `<div class="done-note">${ICONS.check}<span>Na dziś wszystko powtórzone! Wróć jutro albo poćwicz swobodnie.</span></div>
           <a class="btn btn-primary btn-xl" href="#/fiszki/${base}/trening">${ICONS.cards}<span>Trening swobodny<small>wszystkie fiszki, bez wpływu na harmonogram</small></span></a>`) : ''}
      ${nQ ? `<a class="btn btn-gold btn-xl" href="#/test/${base}">${ICONS.quiz}<span>Test<small>${nQ} ${plural(nQ, 'losowe pytanie', 'losowe pytania', 'losowych pytań')} ABCD</small></span></a>` : ''}
      <a class="btn btn-ghost btn-xl" href="#/lista/${base}">${ICONS.book}<span>Przeglądaj treści<small>wszystkie fiszki i pytania ze źródłami</small></span></a>
    </div>

    ${last ? `<p class="muted center">Ostatni test: <strong>${pct(last.score / last.total)}%</strong> · najlepszy: <strong>${pct(best)}%</strong></p>` : ''}
  `;
}

// ---------- fiszki ----------
let session = null;

function viewFiszki(sid, did, mode) {
  const s = findSubject(sid);
  const d = findDzial(s, did);
  if (!d) return notFound();
  const training = mode === 'trening';
  if (!session || session.key !== `${sid}/${did}/${mode || ''}`) {
    const queue = training ? shuffle(d.fiszki) : buildQueue(s.id, d);
    session = { key: `${sid}/${did}/${mode || ''}`, s, d, queue, done: 0, training, counts: { nie: 0, trudne: 0, umiem: 0 } };
  }
  renderCard();
}

function renderCard() {
  const { s, d, queue, training } = session;
  document.body.classList.add('in-session');
  const back = dHref(s.id, d.id);
  if (!queue.length) return renderSessionEnd();

  const f = queue[0];
  const st = store.get().cards[cardKey(s.id, d.id, f.id)];
  const total = session.done + queue.length;
  const isNew = !st || !st.reps;

  app.innerHTML = `
    <div class="session-top">
      <a class="icon-btn" href="${back}" aria-label="Zakończ sesję">${ICONS.close}</a>
      <div class="session-progress">${progressBar(session.done / total, 'Postęp sesji')}</div>
      <span class="session-count">${session.done + 1}/${total}</span>
    </div>
    <p class="session-label">${training ? 'Trening swobodny' : isNew ? '<span class="tag tag-new">Nowa fiszka</span>' : '<span class="tag">Powtórka</span>'}</p>

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
          ${f.zrodlo ? `<span class="source">Konstytucja RP: ${esc(f.zrodlo)}</span>` : ''}
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
      ${reportBtn(reportHref(s, d, 'fiszka', f))}
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
  const { s, d, queue, training } = session;
  const f = queue.shift();
  session.counts[r]++;
  if (!training) {
    const key = cardKey(s.id, d.id, f.id);
    const cards = store.get().cards;
    cards[key] = nextState(cards[key], r);
  }
  store.markActivity();
  store.save();
  if (r === 'nie') queue.splice(Math.min(3, queue.length), 0, f); // wróci za kilka fiszek
  else session.done++;
  renderCard();
  window.scrollTo({ top: 0 });
}

function renderSessionEnd() {
  const { s, d, counts, training } = session;
  const sm = dzialSummary(s.id, d);
  const reviewed = counts.nie + counts.trudne + counts.umiem;
  const base = `${encodeURIComponent(s.id)}/${encodeURIComponent(d.id)}`;
  app.innerHTML = `
    <div class="session-top">
      <a class="icon-btn" href="${dHref(s.id, d.id)}" aria-label="Zamknij">${ICONS.close}</a>
    </div>
    <section class="result">
      <div class="result-icon">${ICONS.compass}</div>
      <h1>${reviewed ? 'Ziemia na horyzoncie!' : 'Na dziś wszystko!'}</h1>
      <p class="lead">${reviewed
        ? `Przejrzane oceny: ${reviewed}. ${training ? 'Trening nie zmienia harmonogramu powtórek.' : 'Kolejne powtórki zaplanowane.'}`
        : 'W tym dziale nie ma teraz fiszek do powtórki. Wróć jutro albo poćwicz swobodnie.'}</p>
      ${reviewed ? `<div class="mini-stats">
        <div class="c-bad"><strong>${counts.nie}</strong><span>Nie wiem</span></div>
        <div class="c-warn"><strong>${counts.trudne}</strong><span>Trudne</span></div>
        <div class="c-ok"><strong>${counts.umiem}</strong><span>Umiem</span></div>
      </div>` : ''}
      <p class="muted">Opanowanie działu: <strong>${pct(sm.progress)}%</strong></p>
      <div class="actions">
        ${sm.todo ? `<a class="btn btn-primary btn-lg" href="#/fiszki/${base}" data-restart>Kontynuuj (${sm.todo})</a>` : ''}
        <a class="btn btn-gold btn-lg" href="#/test/${base}">Sprawdź się w teście</a>
        <a class="btn btn-ghost btn-lg" href="${dHref(s.id, d.id)}">Wróć do działu</a>
      </div>
    </section>`;
  app.querySelector('[data-restart]')?.addEventListener('click', () => (session = null));
  keyHandler = null;
}

// ---------- test ----------
let test = null;

function viewTest(sid, did) {
  const s = findSubject(sid);
  const d = findDzial(s, did);
  if (!d) return notFound();
  if (!test || test.key !== `${sid}/${did}`) startTest(s, d);
  renderQuestion();
}

function startTest(s, d) {
  const qs = shuffle(d.pytania).slice(0, TEST_SIZE).map((q) => ({ q, order: shuffle(q.odpowiedzi.map((_, i) => i)) }));
  test = { key: `${s.id}/${d.id}`, s, d, qs, i: 0, answers: [], saved: false };
}

function renderQuestion() {
  const { s, d, qs, i } = test;
  document.body.classList.add('in-session');
  if (i >= qs.length) return renderTestEnd();
  const { q, order } = qs[i];
  const answered = test.answers[i];

  app.innerHTML = `
    <div class="session-top">
      <a class="icon-btn" href="${dHref(s.id, d.id)}" aria-label="Przerwij test">${ICONS.close}</a>
      <div class="session-progress">${progressBar(i / qs.length, 'Postęp testu')}</div>
      <span class="session-count">${i + 1}/${qs.length}</span>
    </div>
    <section class="question">
      <p class="eyebrow">Pytanie ${i + 1}</p>
      <h2 class="question-text">${esc(q.pytanie)}</h2>
      <div class="options" role="group" aria-label="Odpowiedzi">
        ${order.map((oi, pos) => `<button type="button" class="option" data-oi="${oi}">
            <span class="option-letter">${LITERY[pos]}</span><span class="option-text">${esc(q.odpowiedzi[oi])}</span>
          </button>`).join('')}
      </div>
      <div id="feedback" aria-live="polite"></div>
      ${reportBtn(reportHref(s, d, 'pytanie', q))}
    </section>`;

  const opts = app.querySelector('.options');
  opts.addEventListener('click', (e) => {
    const b = e.target.closest('.option');
    if (b && test.answers[i] === undefined) answer(Number(b.dataset.oi));
  });
  if (answered !== undefined) showFeedback();
  keyHandler = (e) => {
    const pos = ['1', '2', '3', '4'].indexOf(e.key) >= 0 ? Number(e.key) - 1 : LITERY.indexOf(e.key.toUpperCase());
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
      ${q.zrodlo ? `<span class="source">Konstytucja RP: ${esc(q.zrodlo)}</span>` : ''}
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
  const { s, d, qs, answers } = test;
  const score = qs.reduce((n, { q }, i) => n + (answers[i] === q.poprawna ? 1 : 0), 0);
  const p = pct(score / qs.length);
  if (!test.saved) {
    store.addTest({ sid: s.id, did: d.id, score, total: qs.length, at: Date.now() });
    store.save();
    test.saved = true;
  }
  const msg = p >= 90 ? 'Mistrzowska nawigacja!' : p >= 70 ? 'Dobry kurs — tak trzymaj!' : p >= 50 ? 'Połowa drogi za Tobą.' : 'Sztorm — powtórz fiszki i spróbuj ponownie.';
  const wrong = qs.map((x, i) => ({ ...x, a: answers[i] })).filter((x) => x.a !== x.q.poprawna);
  const base = `${encodeURIComponent(s.id)}/${encodeURIComponent(d.id)}`;

  app.innerHTML = `
    <div class="session-top"><a class="icon-btn" href="${dHref(s.id, d.id)}" aria-label="Zamknij">${ICONS.close}</a></div>
    <section class="result">
      <div class="ring ring-xl ${p >= 70 ? 'ring-ok' : p >= 50 ? 'ring-warn' : 'ring-bad'}" style="--p:${p}"><span>${p}%</span></div>
      <h1>${msg}</h1>
      <p class="lead">Poprawne odpowiedzi: <strong>${score} z ${qs.length}</strong></p>
      <div class="actions">
        <button type="button" class="btn btn-gold btn-lg" id="again">Nowy test</button>
        <a class="btn btn-ghost btn-lg" href="${dHref(s.id, d.id)}">Wróć do działu</a>
      </div>
    </section>
    ${wrong.length ? `<h2 class="section-title">Do poprawki</h2>
      <div class="review-list">${wrong.map(({ q, a }) => `<article class="card review">
        <h3>${esc(q.pytanie)}</h3>
        <p class="ans bad">${ICONS.close}<span>Twoja odpowiedź: ${esc(q.odpowiedzi[a])}</span></p>
        <p class="ans ok">${ICONS.check}<span>Poprawna: ${esc(q.odpowiedzi[q.poprawna])}</span></p>
        ${q.wyjasnienie ? `<p class="muted">${esc(q.wyjasnienie)}</p>` : ''}
        <div class="review-foot">${q.zrodlo ? `<span class="source">Konstytucja RP: ${esc(q.zrodlo)}</span>` : '<span></span>'}${reportBtn(reportHref(s, d, 'pytanie', q))}</div>
      </article>`).join('')}</div>` : ''}`;

  app.querySelector('#again').addEventListener('click', () => {
    startTest(s, d);
    location.hash = `#/test/${base}`;
    renderQuestion();
    window.scrollTo({ top: 0 });
  });
  keyHandler = null;
}

// ---------- przegląd treści ----------
function viewLista(sid, did) {
  const s = findSubject(sid);
  const d = findDzial(s, did);
  if (!d) return notFound();
  const cards = store.get().cards;
  const boxLabel = (c) => (!c || !c.reps ? 'nowa' : c.box >= MASTERED_BOX ? 'opanowana' : `poziom ${c.box}/6`);
  app.innerHTML = `
    ${pageHead('Treści działu', dHref(s.id, d.id), d.nazwa)}
    <div class="tabs" role="tablist">
      <button type="button" role="tab" class="tab active" aria-selected="true" data-tab="f">Fiszki (${d.fiszki.length})</button>
      <button type="button" role="tab" class="tab" aria-selected="false" data-tab="p">Pytania (${d.pytania.length})</button>
    </div>
    <div data-panel="f" class="review-list">${d.fiszki.map((f, i) => {
      const c = cards[cardKey(s.id, d.id, f.id)];
      return `<article class="card review">
        <div class="review-head"><span class="muted">${i + 1}.</span><span class="tag ${c && c.box >= MASTERED_BOX ? 'tag-ok' : ''}">${boxLabel(c)}</span></div>
        <h3>${esc(f.przod)}</h3><p>${esc(f.tyl)}</p>
        <div class="review-foot">${f.zrodlo ? `<span class="source">Konstytucja RP: ${esc(f.zrodlo)}</span>` : '<span></span>'}${reportBtn(reportHref(s, d, 'fiszka', f))}</div>
      </article>`;
    }).join('')}</div>
    <div data-panel="p" class="review-list" hidden>${d.pytania.map((q, i) => `<article class="card review">
        <div class="review-head"><span class="muted">${i + 1}.</span></div>
        <h3>${esc(q.pytanie)}</h3>
        <ol class="abcd">${q.odpowiedzi.map((o, j) => `<li class="${j === q.poprawna ? 'ok' : ''}"><b>${LITERY[j]}</b> ${esc(o)}${j === q.poprawna ? ` ${ICONS.check}` : ''}</li>`).join('')}</ol>
        ${q.wyjasnienie ? `<p class="muted">${esc(q.wyjasnienie)}</p>` : ''}
        <div class="review-foot">${q.zrodlo ? `<span class="source">Konstytucja RP: ${esc(q.zrodlo)}</span>` : '<span></span>'}${reportBtn(reportHref(s, d, 'pytanie', q))}</div>
      </article>`).join('')}</div>`;

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

// ---------- statystyki ----------
function viewStats() {
  const st = store.streak();
  const state = store.get();
  let mastered = 0, total = 0, seen = 0;
  const per = [];
  subjects.forEach((s) => s.dzialy.forEach((d) => {
    const sm = dzialSummary(s.id, d);
    mastered += sm.mastered;
    total += sm.total;
    seen += sm.total - sm.fresh;
    per.push({ s, d, sm });
  }));
  const activity = Object.values(state.days).reduce((a, b) => a + b, 0);
  const tests = state.tests.slice(-10).reverse();
  const avg = state.tests.length ? state.tests.reduce((a, t) => a + t.score / t.total, 0) / state.tests.length : null;
  const fmt = new Intl.DateTimeFormat('pl-PL', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' });

  // ostatnie 14 dni nauki
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
    </div>

    <section class="card">
      <h2 class="card-title">Ostatnie 14 dni</h2>
      <div class="days" role="list">${days.map((x) => `<div role="listitem" class="day ${x.on ? 'on' : ''}" title="${store.dayKey(x.t)}"><span class="dot">${x.on ? ICONS.check : ''}</span><small>${dfmt.format(x.t)}</small></div>`).join('')}</div>
    </section>

    <section class="card">
      <h2 class="card-title">Opanowanie działów</h2>
      ${per.map(({ s, d, sm }) => `<a class="stat-row" href="${dHref(s.id, d.id)}">
        <div class="stat-row-top"><span>${esc(s.skrot)} · ${esc(d.nazwa)}</span><strong>${pct(sm.progress)}%</strong></div>
        ${progressBar(sm.progress, d.nazwa)}
      </a>`).join('') || '<p class="muted">Brak działów.</p>'}
    </section>

    <section class="card">
      <h2 class="card-title">Ostatnie testy</h2>
      ${tests.length ? `<ul class="test-list">${tests.map((t) => {
        const s = findSubject(t.sid);
        const d = findDzial(s, t.did);
        const p = pct(t.score / t.total);
        return `<li><div><strong>${esc(d ? d.nazwa : t.did)}</strong><span>${fmt.format(t.at)} · ${t.score}/${t.total}</span></div>
          <span class="score ${p >= 70 ? 'ok' : p >= 50 ? 'warn' : 'bad'}">${p}%</span></li>`;
      }).join('')}</ul>` : '<p class="muted">Nie masz jeszcze żadnego testu. Rozwiąż pierwszy w wybranym dziale!</p>'}
    </section>`;
}

// ---------- ustawienia ----------
function viewSettings() {
  const theme = store.get().settings.theme;
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
      <p><strong>Kolumb</strong> — fiszki i testy do matury. Fiszki wracają według systemu Leitnera: te, których nie znasz, pojawiają się szybko, a opanowane — coraz rzadziej.</p>
      <p class="muted">Zauważyłeś błąd w treści? Użyj przycisku „Zgłoś błąd” przy fiszce lub pytaniu albo napisz na <a href="mailto:${REPORT_EMAIL}">${REPORT_EMAIL}</a>.</p>
    </section>`;

  app.querySelector('.segmented').addEventListener('click', (e) => {
    const b = e.target.closest('[data-theme-set]');
    if (!b) return;
    store.get().settings.theme = b.dataset.themeSet;
    store.save();
    applyTheme();
    viewSettings();
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
    if (!confirm('Na pewno usunąć wszystkie postępy, serię i wyniki testów? Tej operacji nie można cofnąć.')) return;
    store.reset();
    session = test = null;
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
  [/^#\/fiszki\/([^/]+)\/([^/]+)(?:\/(trening))?$/, viewFiszki],
  [/^#\/test\/([^/]+)\/([^/]+)$/, viewTest],
  [/^#\/lista\/([^/]+)\/([^/]+)$/, viewLista],
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

  for (const [re, view] of routes) {
    const m = hash.match(re);
    if (m) {
      view(...m.slice(1).map((x) => (x === undefined ? undefined : decodeURIComponent(x))));
      break;
    }
    if (re === routes[routes.length - 1][0]) notFound();
  }

  const tab = hash.startsWith('#/statystyki') ? 'stats' : hash.startsWith('#/ustawienia') ? 'settings' : 'home';
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
