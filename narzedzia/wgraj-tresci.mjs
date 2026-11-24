#!/usr/bin/env node
// IndexLab — wgrywa treści z katalogu przedmioty/ do tabeli „tresci” w Supabase (tryb premium).
//
//   node narzedzia/wgraj-tresci.mjs --sprawdz      # tylko pokaż, co jest demo, a co premium
//   SUPABASE_URL=https://xxx.supabase.co SUPABASE_SERVICE_ROLE_KEY=… node narzedzia/wgraj-tresci.mjs
//
// Klucz serwisowy (service_role) omija RLS — podawaj go tylko w zmiennej środowiskowej,
// nigdy nie zapisuj go w repozytorium ani w js/config.js.
//
// Darmowe demo (demo = true): spis przedmiotów, szkielet każdego przedmiotu (z nazwami wszystkich działów
// i tematów — żeby uczeń widział, co odblokuje), działy z listy DEMO (domyślnie pierwszy z treścią),
// najnowszy arkusz CKE, bank zadań z działów demo i aktualności / chronologia.
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = new URL('../przedmioty/', import.meta.url).pathname;
// Darmowa część: ok. 30% fiszek (pierwsze działy po kolei, aż suma przekroczy 30%) i ok. 30% arkuszy CKE (najnowsze).
const CZESC_DARMOWA = 0.3;
const DEMO = {}; // opcjonalnie: ręczna lista działów demo dla przedmiotu, np. { historia: ['umiejetnosci', 'starozytnosc'] }
const czytaj = (plik) => JSON.parse(readFileSync(join(ROOT, plik), 'utf8'));

const rows = [];
const add = (plik, przedmiot, dane, demo) => rows.push({ plik, przedmiot, dane, demo });

const idx = czytaj('index.json');
const pliki = Array.isArray(idx) ? idx : idx.przedmioty;
add('index.json', '*', idx, true);

for (const f of pliki) {
  const s = czytaj(f);
  const sid = s.id || f.replace(/\.json$/, '');
  const liczFiszki = (d) => (Array.isArray(d.poddzialy) && d.poddzialy.length ? d.poddzialy : [d]).reduce((n, u) => n + (u.fiszki?.length || 0), 0);
  const zDzialow = s.dzialy.filter((r) => r.plik).map((r) => ({ id: r.id, n: liczFiszki(czytaj(r.plik)) }));
  const wszystkie = zDzialow.reduce((n, d) => n + d.n, 0);
  const auto = [];
  // dokładamy kolejne działy, dopóki suma jest bliżej 30% z danym działem niż bez niego
  for (let suma = 0, i = 0; i < zDzialow.length; i++) {
    const cel = wszystkie * CZESC_DARMOWA;
    if (auto.length && Math.abs(suma + zDzialow[i].n - cel) >= Math.abs(suma - cel)) break;
    auto.push(zDzialow[i].id); suma += zDzialow[i].n;
  }
  const demoDzialy = new Set(DEMO[sid] || auto);
  const ileArkuszy = Math.max(1, Math.round((s.arkusze || []).length * CZESC_DARMOWA));
  const szkielet = structuredClone(s);

  szkielet.dzialy = s.dzialy.map((ref) => {
    if (!ref.plik) return ref;
    const d = czytaj(ref.plik);
    add(ref.plik, sid, d, demoDzialy.has(ref.id));
    const pod = Array.isArray(d.poddzialy) && d.poddzialy.length ? d.poddzialy : [{ id: d.id || ref.id, nazwa: d.nazwa }];
    return { ...ref, zarys: { nazwa: d.nazwa, opis: d.opis || '', poddzialy: pod.map((u) => ({ id: u.id, nazwa: u.nazwa, liczbaFiszek: u.fiszki?.length || 0 })) } };
  });

  szkielet.arkusze = (s.arkusze || []).map((ref, i) => {
    if (!ref.plik) return ref;
    const a = czytaj(ref.plik);
    add(ref.plik, sid, a, i < ileArkuszy);
    const zad = (a.wiazki || []).flatMap((w) => w.zadania || []);
    return { ...ref, zarys: { nazwa: a.nazwa, opis: a.opis || '', liczbaZadan: zad.length, punkty: zad.reduce((n, z) => n + (Number(z.punkty) || 1), 0) } };
  });

  szkielet.bank = (s.bank || []).map((ref) => {
    if (!ref.plik) return ref;
    const b = czytaj(ref.plik);
    const dz = b.dzial || b.wiazki?.[0]?.dzial;
    add(ref.plik, sid, b, demoDzialy.has(dz));
    return { ...ref, zarys: { dzial: dz, liczbaZadan: (b.wiazki || []).reduce((n, w) => n + (w.zadania?.length || 0), 0) } };
  });

  if (s.aktualnosci?.plik) add(s.aktualnosci.plik, sid, czytaj(s.aktualnosci.plik), true);
  add(f, sid, szkielet, true);
}

const kb = (x) => Math.round(Buffer.byteLength(JSON.stringify(x)) / 1024);
for (const r of rows) console.log(`${r.demo ? 'DEMO   ' : 'premium'}  ${r.plik.padEnd(42)} ${String(kb(r.dane)).padStart(5)} KB`);
console.log(`\nRazem: ${rows.length} plików, demo: ${rows.filter((r) => r.demo).length}, premium: ${rows.filter((r) => !r.demo).length}`);

if (process.argv.includes('--sprawdz')) process.exit(0);

const URL_ = (process.env.SUPABASE_URL || '').replace(/\/+$/, '');
const KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || '';
if (!URL_ || !KEY) {
  console.error('\nUstaw SUPABASE_URL i SUPABASE_SERVICE_ROLE_KEY (albo użyj --sprawdz).');
  process.exit(1);
}
const now = new Date().toISOString();
for (let i = 0; i < rows.length; i += 5) { // małe porcje — pojedyncze pliki mają do ~1 MB
  const part = rows.slice(i, i + 5).map((r) => ({ ...r, updated_at: now }));
  const res = await fetch(`${URL_}/rest/v1/tresci`, {
    method: 'POST',
    headers: { apikey: KEY, Authorization: `Bearer ${KEY}`, 'Content-Type': 'application/json', Prefer: 'resolution=merge-duplicates,return=minimal' },
    body: JSON.stringify(part),
  });
  if (!res.ok) { console.error(`Błąd ${res.status}: ${await res.text()}`); process.exit(1); }
  process.stdout.write('.');
}
// pliki usunięte z repozytorium znikają też z bazy
const aktualne = rows.map((r) => `"${r.plik}"`).join(',');
const del = await fetch(`${URL_}/rest/v1/tresci?plik=not.in.(${encodeURIComponent(aktualne)})`, {
  method: 'DELETE', headers: { apikey: KEY, Authorization: `Bearer ${KEY}` },
});
console.log(del.ok ? '\nGotowe — treści w bazie są aktualne.' : `\nWgrano, ale nie usunięto starych plików (${del.status}).`);
