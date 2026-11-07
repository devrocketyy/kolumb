#!/usr/bin/env node
// IndexLab — tworzy szkielet nowego kursu (przedmiotu) w przedmioty/.
//
// Użycie:
//   node narzedzia/nowy-przedmiot.mjs <id> "<Nazwa>" <SKRÓT> "<id-działu>:<Nazwa działu>" …
// Przykład:
//   node narzedzia/nowy-przedmiot.mjs historia "Historia" HIS \
//     "starozytnosc:Starożytność" "sredniowiecze:Średniowiecze" "nowozytnosc:Nowożytność"
//
// Powstaje:
//   przedmioty/<id>.json            — opis przedmiotu z listą działów (pola "plik")
//   przedmioty/<id>/<dział>.json    — dział z jednym pustym poddziałem do uzupełnienia
// Potem: uzupełnij fiszki i pytania, uruchom `node narzedzia/zbuduj-indeks.mjs`.
// Nowy kurs ma "szkic": true — jest sprawdzany, ale uczniowie go nie widzą. Usuń to pole, by go opublikować.

import { mkdir, writeFile, access } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const DIR = join(dirname(fileURLToPath(import.meta.url)), '..', 'przedmioty');
const ID = /^[a-z0-9-]+$/;
const [id, nazwa, skrot, ...dzialyArg] = process.argv.slice(2);

const stop = (m) => { console.error('❌ ' + m); process.exit(1); };
if (!id || !nazwa || !skrot || !dzialyArg.length) stop('Użycie: node narzedzia/nowy-przedmiot.mjs <id> "<Nazwa>" <SKRÓT> "<id-działu>:<Nazwa działu>" …');
if (!ID.test(id)) stop(`"${id}": id może zawierać tylko małe litery a–z, cyfry i myślniki`);
const exists = async (p) => access(p).then(() => true, () => false);
if (await exists(join(DIR, id + '.json'))) stop(`przedmioty/${id}.json już istnieje — nic nie nadpisuję`);

const dzialy = dzialyArg.map((a) => {
  const [did, ...rest] = a.split(':');
  const dn = rest.join(':').trim();
  if (!ID.test(did) || !dn) stop(`"${a}": dział podaj jako "id-dzialu:Nazwa działu"`);
  return { id: did, nazwa: dn };
});

const json = (o) => JSON.stringify(o, null, 1) + '\n';
await mkdir(join(DIR, id), { recursive: true });
for (const [i, d] of dzialy.entries()) {
  const nr = String(i + 1).padStart(2, '0');
  await writeFile(join(DIR, id, d.id + '.json'), json({
    id: d.id,
    nazwa: d.nazwa,
    opis: '',
    poddzialy: [{
      id: `${d.id}-${nr}`,
      nazwa: `${d.nazwa} — poddział 1`,
      opis: '',
      fiszki: [{ id: 'f001', przod: 'Pytanie / pojęcie', tyl: 'Odpowiedź / definicja', zrodlo: 'Opracowanie autorskie IndexLab' }],
      pytania: [{
        id: 'p01',
        pytanie: 'Treść pytania:',
        odpowiedzi: ['odpowiedź A', 'odpowiedź B', 'odpowiedź C', 'odpowiedź D'],
        poprawna: 'A',
        wyjasnienie: 'Krótkie uzasadnienie poprawnej odpowiedzi.',
        zrodlo: 'Zadanie autorskie IndexLab',
      }],
    }],
  }));
}
await writeFile(join(DIR, id + '.json'), json({
  id,
  nazwa,
  skrot,
  szkic: true, // usuń, gdy kurs będzie gotowy do publikacji
  opis: 'Matura rozszerzona — kurs autorski IndexLab.',
  dzialy: dzialy.map((d) => ({ id: d.id, plik: `${id}/${d.id}.json` })),
  arkusze: [],
  bank: [],
}));

console.log(`✅ Utworzono przedmioty/${id}.json i ${dzialy.length} plików działów w przedmioty/${id}/`);
console.log('   Dalej: uzupełnij treści i uruchom  node narzedzia/zbuduj-indeks.mjs');
