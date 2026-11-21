// IndexLab — „Moje talie”: talie i fiszki tworzone przez ucznia.
//
// Talie leżą w zapisie profilu (store.talie), więc działają offline, mają osobne postępy w każdym profilu
// i synchronizują się z kontem w chmurze. Postępy fiszek są w store.cards pod kluczem
// „moje/<idTalii>/<idFiszki>” — tym samym silnikiem powtórek (Leitner, js/srs.js) co fiszki z kursów.
//
// Usunięta talia zostaje jako „nagrobek” { id, usunieta: true, updated }, żeby scalanie z drugim
// urządzeniem jej nie przywróciło.

import { get, save } from './store.js';

export const SID = 'moje';
export const MAX_PRZOD = 500;
export const MAX_TYL = 1000;
export const MAX_NAZWA = 60;

const uid = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
const clean = (s, max) => String(s ?? '').replace(/\s+/g, ' ').trim().slice(0, max);
const all = () => (get().talie ||= {});

export function list() {
  return Object.values(all()).filter((t) => t && !t.usunieta).sort((a, b) => (b.updated || 0) - (a.updated || 0));
}
export function find(id) {
  const t = all()[id];
  return t && !t.usunieta ? t : null;
}

export function create(nazwa, opis = '') {
  const now = Date.now();
  const t = { id: uid(), nazwa: clean(nazwa, MAX_NAZWA) || 'Nowa talia', opis: clean(opis, 200), fiszki: [], created: now, updated: now };
  all()[t.id] = t;
  save();
  return t;
}

export function update(id, { nazwa, opis }) {
  const t = find(id);
  if (!t) return null;
  if (nazwa !== undefined) t.nazwa = clean(nazwa, MAX_NAZWA) || t.nazwa;
  if (opis !== undefined) t.opis = clean(opis, 200);
  t.updated = Date.now();
  save();
  return t;
}

function forgetProgress(deckId, cardId) {
  const cards = get().cards;
  const prefix = `${SID}/${deckId}/`;
  for (const k of Object.keys(cards)) if (cardId ? k === prefix + cardId : k.startsWith(prefix)) delete cards[k];
}

export function remove(id) {
  if (!find(id)) return false;
  all()[id] = { id, usunieta: true, updated: Date.now() };
  forgetProgress(id);
  save();
  return true;
}

export function addCards(id, pary) {
  const t = find(id);
  if (!t) return 0;
  let n = 0;
  for (const p of pary) {
    const przod = clean(p.przod, MAX_PRZOD);
    const tyl = clean(p.tyl, MAX_TYL);
    if (!przod || !tyl) continue;
    t.fiszki.push({ id: uid() + n, przod, tyl });
    n++;
  }
  if (n) { t.updated = Date.now(); save(); }
  return n;
}
export const addCard = (id, przod, tyl) => addCards(id, [{ przod, tyl }]) === 1;

export function editCard(id, cardId, przod, tyl) {
  const t = find(id);
  const f = t?.fiszki.find((x) => x.id === cardId);
  if (!f) return false;
  const p = clean(przod, MAX_PRZOD), b = clean(tyl, MAX_TYL);
  if (!p || !b) return false;
  f.przod = p; f.tyl = b;
  t.updated = Date.now();
  save();
  return true;
}

export function removeCard(id, cardId) {
  const t = find(id);
  if (!t) return false;
  const before = t.fiszki.length;
  t.fiszki = t.fiszki.filter((x) => x.id !== cardId);
  if (t.fiszki.length === before) return false;
  forgetProgress(id, cardId);
  t.updated = Date.now();
  save();
  return true;
}

// Talia jako „poddział” — ten sam kształt, którego używają fiszki, lekcje i podsumowania z kursów.
export const asUnit = (t) => ({ id: t.id, nazwa: t.nazwa, fiszki: t.fiszki, pytania: [], schematy: [] });

// ---------- import i eksport tekstu ----------
// Jedna fiszka w linii: „przód<separator>tył”. Separator wykrywamy raz dla całego tekstu,
// w kolejności: tabulator (kopiowanie z arkusza, eksport z Quizletu/Anki), „ - ” / „ – ” / „ — ”, „;”, „ = ”, „:”.
const SEPARATORY = [
  { nazwa: 'tabulator', re: /\t/ },
  { nazwa: 'myślnik', re: /\s+[-–—]\s+/ },
  { nazwa: 'średnik', re: /;/ },
  { nazwa: 'znak =', re: /\s*=\s*/ },
  { nazwa: 'dwukropek', re: /:\s*/ },
];

export function parseText(text) {
  const lines = String(text || '').split(/\r?\n/).map((l) => l.trim()).filter(Boolean);
  if (!lines.length) return { karty: [], pominiete: [], separator: null };
  // wybieramy separator, który dzieli najwięcej linii
  let best = SEPARATORY[0], bestN = -1;
  for (const s of SEPARATORY) {
    const n = lines.filter((l) => s.re.test(l)).length;
    if (n > bestN) { best = s; bestN = n; }
  }
  const karty = [], pominiete = [];
  for (const l of lines) {
    const m = l.match(best.re);
    if (!m) { pominiete.push(l); continue; }
    const przod = l.slice(0, m.index).trim();
    const tyl = l.slice(m.index + m[0].length).trim();
    if (!przod || !tyl) { pominiete.push(l); continue; }
    karty.push({ przod, tyl });
  }
  return { karty, pominiete, separator: bestN > 0 ? best.nazwa : null };
}

export const exportText = (t) => t.fiszki.map((f) => `${f.przod}\t${f.tyl}`).join('\n');

// ---------- scalanie z chmurą ----------
// Z każdej talii bierzemy nowszą wersję (także nagrobek, jeśli usunięcie było późniejsze niż ostatnia zmiana).
export function merge(a = {}, b = {}) {
  const out = { ...a };
  for (const [k, t] of Object.entries(b || {})) {
    const x = out[k];
    if (!x || (t.updated || 0) > (x.updated || 0)) out[k] = t;
  }
  return out;
}
