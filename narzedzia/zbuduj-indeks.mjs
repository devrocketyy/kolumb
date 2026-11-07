#!/usr/bin/env node
// Kolumb — sprawdza pliki przedmiotów i buduje przedmioty/index.json.
// Użycie:  node narzedzia/zbuduj-indeks.mjs
// Skrypt uruchamia się automatycznie w GitHub Actions przy każdym wdrożeniu.
//
// Przedmiot = plik JSON bezpośrednio w katalogu przedmioty/ (np. przedmioty/historia.json).
// Pliki w podkatalogach (np. przedmioty/wos/prawo.json) to działy i arkusze wskazywane polem "plik".

import { readdir, readFile, writeFile, access } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const DIR = join(ROOT, 'przedmioty');
const LITERY = ['A', 'B', 'C', 'D'];
const ID = /^[a-z0-9-]+$/;

const bledy = [];
const ostrzezenia = [];
const staty = [];
const dlugosc = { abcd: 0, najdluzsza: 0 }; // czy poprawna odpowiedź nie jest regularnie najdłuższa

async function wczytaj(plik) {
  return JSON.parse(await readFile(join(DIR, plik), 'utf8'));
}

async function rozwin(item, gdzie) {
  if (!item || !item.plik) return item;
  try {
    await access(join(DIR, item.plik));
  } catch {
    bledy.push(gdzie(`brak pliku "${item.plik}"`));
    return null;
  }
  try {
    return { ...(await wczytaj(item.plik)), ...item };
  } catch (e) {
    bledy.push(gdzie(`${item.plik}: niepoprawny JSON — ${e.message}`));
    return null;
  }
}

function sprawdzPoddzial(u, w, gdzie) {
  const ids = new Set();
  let nf = 0, nq = 0;
  (u.fiszki || []).forEach((f, j) => {
    const x = `${w}, fiszka ${f.id || '#' + (j + 1)}`;
    if (!f.id) bledy.push(gdzie(`${x}: brak "id"`));
    if (ids.has(f.id)) bledy.push(gdzie(`${x}: powtórzone "id"`));
    ids.add(f.id);
    if (!f.przod || !f.tyl) bledy.push(gdzie(`${x}: brak "przod" lub "tyl"`));
    if (!f.zrodlo) ostrzezenia.push(gdzie(`${x}: brak "zrodlo"`));
    nf++;
  });
  (u.pytania || []).forEach((q, j) => {
    const x = `${w}, pytanie ${q.id || '#' + (j + 1)}`;
    if (!q.id) bledy.push(gdzie(`${x}: brak "id"`));
    if (ids.has(q.id)) bledy.push(gdzie(`${x}: powtórzone "id"`));
    ids.add(q.id);
    if (!q.pytanie) bledy.push(gdzie(`${x}: brak "pytanie"`));
    if (!Array.isArray(q.odpowiedzi) || q.odpowiedzi.length !== 4) bledy.push(gdzie(`${x}: "odpowiedzi" musi mieć dokładnie 4 elementy`));
    const ok = typeof q.poprawna === 'number' ? q.poprawna >= 0 && q.poprawna < 4 : LITERY.includes(String(q.poprawna).toUpperCase());
    if (!ok) bledy.push(gdzie(`${x}: "poprawna" musi być literą A–D`));
    if (ok && Array.isArray(q.odpowiedzi) && q.odpowiedzi.length === 4) {
      const ci = typeof q.poprawna === 'number' ? q.poprawna : LITERY.indexOf(String(q.poprawna).toUpperCase());
      const dl = q.odpowiedzi.map((o) => String(o).length);
      const inne = Math.max(...dl.filter((_, k) => k !== ci));
      dlugosc.abcd++;
      if (dl[ci] > inne) dlugosc.najdluzsza++;
      if (dl[ci] >= 1.6 * inne && dl[ci] - inne >= 15) ostrzezenia.push(gdzie(`${x}: poprawna odpowiedź jest wyraźnie dłuższa od pozostałych — zdradza się długością`));
    }
    if (!q.wyjasnienie) ostrzezenia.push(gdzie(`${x}: brak "wyjasnienie"`));
    if (!q.zrodlo) ostrzezenia.push(gdzie(`${x}: brak "zrodlo"`));
    nq++;
  });
  return [nf, nq];
}

async function sprawdzPrzedmiot(plik, p) {
  const gdzie = (s) => `${plik}: ${s}`;
  if (!p || typeof p !== 'object') return bledy.push(gdzie('plik nie zawiera obiektu JSON'));
  if (!p.nazwa) bledy.push(gdzie('brak pola "nazwa"'));
  if (!Array.isArray(p.dzialy) || !p.dzialy.length) return bledy.push(gdzie('brak działów ("dzialy")'));
  const idDzialow = new Set();
  const idPoddzialow = new Set();
  let nf = 0, nq = 0, nu = 0, nz = 0;
  for (const [i, raw] of p.dzialy.entries()) {
    const d = await rozwin(raw, gdzie);
    if (!d) continue;
    const dz = `dział ${d.id || '#' + (i + 1)}`;
    if (!d.id) bledy.push(gdzie(`${dz}: brak pola "id"`));
    else if (!ID.test(d.id)) bledy.push(gdzie(`${dz}: "id" może zawierać tylko małe litery a–z, cyfry i myślniki`));
    if (idDzialow.has(d.id)) bledy.push(gdzie(`${dz}: powtórzone "id"`));
    idDzialow.add(d.id);
    if (!d.nazwa) bledy.push(gdzie(`${dz}: brak pola "nazwa"`));
    const units = Array.isArray(d.poddzialy) && d.poddzialy.length ? d.poddzialy : [{ ...d, id: d.id }];
    for (const [j, u] of units.entries()) {
      const w = `${dz}, poddział ${u.id || '#' + (j + 1)}`;
      if (!u.id) bledy.push(gdzie(`${w}: brak "id"`));
      else if (!ID.test(u.id)) bledy.push(gdzie(`${w}: "id" może zawierać tylko małe litery a–z, cyfry i myślniki`));
      if (idPoddzialow.has(u.id)) bledy.push(gdzie(`${w}: "id" poddziału musi być unikalne w całym przedmiocie`));
      idPoddzialow.add(u.id);
      if (!u.nazwa) bledy.push(gdzie(`${w}: brak "nazwa"`));
      const [a, b] = sprawdzPoddzial(u, w, gdzie);
      if (!a && !b) ostrzezenia.push(gdzie(`${w}: poddział jest pusty`));
      nf += a; nq += b; nu++;
    }
  }
  for (const [i, raw] of (p.arkusze || []).entries()) {
    const a = await rozwin(raw, gdzie);
    if (!a) continue;
    const w = `arkusz ${a.id || '#' + (i + 1)}`;
    if (!a.id) bledy.push(gdzie(`${w}: brak "id"`));
    if (!Array.isArray(a.wiazki)) { bledy.push(gdzie(`${w}: brak "wiazki"`)); continue; }
    const nry = new Set();
    for (const wz of a.wiazki) {
      for (const z of wz.zadania || []) {
        if (nry.has(z.nr)) bledy.push(gdzie(`${w}: powtórzony numer zadania ${z.nr}`));
        nry.add(z.nr);
        if (!z.polecenie) bledy.push(gdzie(`${w}, zadanie ${z.nr}: brak "polecenie"`));
        if (!z.odpowiedz) ostrzezenia.push(gdzie(`${w}, zadanie ${z.nr}: brak "odpowiedz"`));
        for (const dz of z.dzialy || []) if (!idDzialow.has(dz)) ostrzezenia.push(gdzie(`${w}, zadanie ${z.nr}: nieznany dział "${dz}"`));
        nz++;
      }
    }
  }
  const idWiazek = new Set();
  let nb = 0;
  for (const raw of p.bank || []) {
    const b = await rozwin(raw, gdzie);
    if (!b) continue;
    for (const wz of b.wiazki || []) {
      const w = `bank, wiązka ${wz.id}`;
      if (!wz.id) bledy.push(gdzie('bank: wiązka bez "id"'));
      if (idWiazek.has(wz.id)) bledy.push(gdzie(`${w}: powtórzone id`));
      idWiazek.add(wz.id);
      if (!idDzialow.has(wz.dzial || b.dzial)) ostrzezenia.push(gdzie(`${w}: nieznany dział "${wz.dzial || b.dzial}"`));
      const otw = (wz.material.match(/\[\[(wykres|linia|tabela|rysunek|mapa)/g) || []).length;
      const zam = (wz.material.match(/\[\[\/\]\]/g) || []).length;
      if (otw !== zam) bledy.push(gdzie(`${w}: niedomknięty blok [[…]] w materiale`));
      if (!(wz.zadania || []).length) bledy.push(gdzie(`${w}: brak zadań`));
      for (const z of wz.zadania || []) {
        if (!z.polecenie) bledy.push(gdzie(`${w}, zadanie ${z.nr}: brak "polecenie"`));
        if (!z.odpowiedz) bledy.push(gdzie(`${w}, zadanie ${z.nr}: brak "odpowiedz"`));
        if (!(z.punkty >= 1)) bledy.push(gdzie(`${w}, zadanie ${z.nr}: zła liczba punktów`));
        nb++;
      }
    }
  }
  staty.push(`${plik}: ${idWiazek.size} wiązek autorskich (${nb} zadań)`);
  staty.push(`${plik}: ${idDzialow.size} działów, ${nu} poddziałów, ${nf} fiszek, ${nq} pytań ABCD, ${nz} zadań maturalnych`);
}

const pliki = (await readdir(DIR, { withFileTypes: true }))
  .filter((f) => f.isFile() && f.name.endsWith('.json') && f.name !== 'index.json')
  .map((f) => f.name)
  .sort((a, b) => a.localeCompare(b, 'pl'));

const szkice = []; // przedmioty z "szkic": true — sprawdzane, ale niewidoczne w aplikacji
for (const plik of pliki) {
  try {
    const p = await wczytaj(plik);
    if (p && p.szkic) szkice.push(plik);
    await sprawdzPrzedmiot(plik, p);
  } catch (e) {
    bledy.push(`${plik}: niepoprawny JSON — ${e.message}`);
  }
}

if (dlugosc.abcd >= 40 && dlugosc.najdluzsza / dlugosc.abcd > 0.33) {
  ostrzezenia.push(`pytania ABCD: poprawna jest najdłuższą odpowiedzią w ${Math.round((100 * dlugosc.najdluzsza) / dlugosc.abcd)}% pytań (losowo ~25%) — wyrównaj długości odpowiedzi`);
}
if (ostrzezenia.length > 20) {
  ostrzezenia.slice(0, 20).forEach((o) => console.warn('⚠️  ' + o));
  console.warn(`⚠️  …i ${ostrzezenia.length - 20} kolejnych ostrzeżeń`);
} else ostrzezenia.forEach((o) => console.warn('⚠️  ' + o));
if (bledy.length) {
  bledy.forEach((b) => console.error('❌ ' + b));
  process.exit(1);
}

const widoczne = pliki.filter((f) => !szkice.includes(f));
await writeFile(join(DIR, 'index.json'), JSON.stringify({ przedmioty: widoczne }, null, 2) + '\n');
staty.forEach((s) => console.log('📚 ' + s));
if (dlugosc.abcd) console.log(`📏 Poprawna = najdłuższa odpowiedź: ${Math.round((100 * dlugosc.najdluzsza) / dlugosc.abcd)}% pytań ABCD (poziom losowy ~25%)`);
console.log(`✅ Zapisano przedmioty/index.json (${widoczne.length}): ${widoczne.join(', ')}`);
if (szkice.length) console.log(`📝 Szkice (niewidoczne dla uczniów, usuń "szkic": true, by opublikować): ${szkice.join(', ')}`);
