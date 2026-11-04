#!/usr/bin/env node
// Kolumb — sprawdza pliki przedmiotów i buduje przedmioty/index.json.
// Użycie:  node narzedzia/zbuduj-indeks.mjs
// Skrypt uruchamia się automatycznie w GitHub Actions przy każdym wdrożeniu.

import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const DIR = join(ROOT, 'przedmioty');
const LITERY = ['A', 'B', 'C', 'D'];

const bledy = [];
const ostrzezenia = [];

function sprawdzPrzedmiot(plik, p) {
  const gdzie = (s) => `${plik}: ${s}`;
  if (!p || typeof p !== 'object') return bledy.push(gdzie('plik nie zawiera obiektu JSON'));
  if (!p.nazwa) bledy.push(gdzie('brak pola "nazwa"'));
  if (!Array.isArray(p.dzialy) || !p.dzialy.length) return bledy.push(gdzie('brak działów ("dzialy")'));
  const idDzialow = new Set();
  p.dzialy.forEach((d, i) => {
    const dz = `dział ${d.id || '#' + (i + 1)}`;
    if (!d.id) bledy.push(gdzie(`${dz}: brak pola "id"`));
    else if (!/^[a-z0-9-]+$/.test(d.id)) bledy.push(gdzie(`${dz}: "id" może zawierać tylko małe litery a–z, cyfry i myślniki`));
    if (idDzialow.has(d.id)) bledy.push(gdzie(`${dz}: powtórzone "id"`));
    idDzialow.add(d.id);
    if (!d.nazwa) bledy.push(gdzie(`${dz}: brak pola "nazwa"`));
    const ids = new Set();
    (d.fiszki || []).forEach((f, j) => {
      const w = `${dz}, fiszka ${f.id || '#' + (j + 1)}`;
      if (!f.id) bledy.push(gdzie(`${w}: brak "id"`));
      if (ids.has(f.id)) bledy.push(gdzie(`${w}: powtórzone "id"`));
      ids.add(f.id);
      if (!f.przod || !f.tyl) bledy.push(gdzie(`${w}: brak "przod" lub "tyl"`));
      if (!f.zrodlo) ostrzezenia.push(gdzie(`${w}: brak "zrodlo"`));
    });
    (d.pytania || []).forEach((q, j) => {
      const w = `${dz}, pytanie ${q.id || '#' + (j + 1)}`;
      if (!q.id) bledy.push(gdzie(`${w}: brak "id"`));
      if (ids.has(q.id)) bledy.push(gdzie(`${w}: powtórzone "id"`));
      ids.add(q.id);
      if (!q.pytanie) bledy.push(gdzie(`${w}: brak "pytanie"`));
      if (!Array.isArray(q.odpowiedzi) || q.odpowiedzi.length !== 4) bledy.push(gdzie(`${w}: "odpowiedzi" musi mieć dokładnie 4 elementy`));
      const ok = typeof q.poprawna === 'number' ? q.poprawna >= 0 && q.poprawna < 4 : LITERY.includes(String(q.poprawna).toUpperCase());
      if (!ok) bledy.push(gdzie(`${w}: "poprawna" musi być literą A–D`));
      if (!q.wyjasnienie) ostrzezenia.push(gdzie(`${w}: brak "wyjasnienie"`));
      if (!q.zrodlo) ostrzezenia.push(gdzie(`${w}: brak "zrodlo"`));
    });
    if (!(d.fiszki || []).length && !(d.pytania || []).length) ostrzezenia.push(gdzie(`${dz}: dział jest pusty`));
  });
}

const pliki = (await readdir(DIR))
  .filter((f) => f.endsWith('.json') && f !== 'index.json')
  .sort((a, b) => a.localeCompare(b, 'pl'));

for (const plik of pliki) {
  try {
    sprawdzPrzedmiot(plik, JSON.parse(await readFile(join(DIR, plik), 'utf8')));
  } catch (e) {
    bledy.push(`${plik}: niepoprawny JSON — ${e.message}`);
  }
}

ostrzezenia.forEach((o) => console.warn('⚠️  ' + o));
if (bledy.length) {
  bledy.forEach((b) => console.error('❌ ' + b));
  process.exit(1);
}

await writeFile(join(DIR, 'index.json'), JSON.stringify({ przedmioty: pliki }, null, 2) + '\n');
console.log(`✅ Zapisano przedmioty/index.json (${pliki.length}): ${pliki.join(', ')}`);
