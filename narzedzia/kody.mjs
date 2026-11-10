#!/usr/bin/env node
// IndexLab — generuje kody dostępu (np. do sprzedaży na Naffy) i zapisuje ich skróty w tabeli „kody”.
//
//   SUPABASE_URL=… SUPABASE_SERVICE_ROLE_KEY=… node narzedzia/kody.mjs --ile 100 --do 2027-05-31 --partia naffy-2026-11
//   SUPABASE_URL=… SUPABASE_SERVICE_ROLE_KEY=… node narzedzia/kody.mjs --ile 50 --dni 30 --partia naffy-miesiac
//
// Kody trafiają do pliku CSV (wypisanego na końcu) — wgraj go do sklepu. W bazie zostaje tylko SHA-256 kodu,
// więc wyciek bazy nie ujawnia kodów. Pliku CSV nie dodawaj do repozytorium.
import { createHash, randomInt } from 'node:crypto';
import { writeFileSync } from 'node:fs';

const arg = (n, d) => { const i = process.argv.indexOf(`--${n}`); return i > 0 ? process.argv[i + 1] : d; };
const ile = Number(arg('ile', 10));
const dni = arg('dni') ? Number(arg('dni')) : null;
const doDnia = arg('do') ? new Date(`${arg('do')}T23:59:59+02:00`).toISOString() : null;
const partia = arg('partia', `partia-${new Date().toISOString().slice(0, 10)}`);
const plan = arg('plan', doDnia ? 'matura' : 'kod');
if (!dni && !doDnia) { console.error('Podaj --dni N albo --do RRRR-MM-DD.'); process.exit(1); }

const ALFABET = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // bez 0/O i 1/I
const kod = () => Array.from({ length: 3 }, () => Array.from({ length: 4 }, () => ALFABET[randomInt(ALFABET.length)]).join('')).join('-');
const hash = (k) => createHash('sha256').update(k.replace(/[^A-Z0-9]/g, '')).digest('hex');

const kody = Array.from({ length: ile }, kod);
const URL_ = (process.env.SUPABASE_URL || '').replace(/\/+$/, '');
const KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || '';
if (!URL_ || !KEY) { console.error('Ustaw SUPABASE_URL i SUPABASE_SERVICE_ROLE_KEY.'); process.exit(1); }

const res = await fetch(`${URL_}/rest/v1/kody`, {
  method: 'POST',
  headers: { apikey: KEY, Authorization: `Bearer ${KEY}`, 'Content-Type': 'application/json', Prefer: 'return=minimal' },
  body: JSON.stringify(kody.map((k) => ({ kod_hash: hash(k), plan, dni, do_dnia: doDnia, partia }))),
});
if (!res.ok) { console.error(`Błąd ${res.status}: ${await res.text()}`); process.exit(1); }
const plik = `kody-${partia}.csv`;
writeFileSync(plik, 'kod\n' + kody.join('\n') + '\n');
console.log(`Zapisano ${ile} kodów (${doDnia ? `ważne do ${arg('do')}` : `${dni} dni`}) → ${plik}`);
