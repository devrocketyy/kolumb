// IndexLab — test jakości oceniania AI na stałym zbiorze (zbior.jsonl). Wewnętrzne, nie trafia do aplikacji.
// Używa TEJ SAMEJ instrukcji co funkcja „ocen” (supabase/functions/_shared/ocena-instrukcja.ts).
//
//   node narzedzia/ocena-ai/test.mjs --szacuj [--model haiku|sonnet] [--czesc robocza|kontrolna|wszystko]
//       → tylko szacunek kosztu, BEZ wywołań API
//   node narzedzia/ocena-ai/test.mjs --model haiku --czesc robocza --tak
//       → płatny przebieg (wymaga klucza w INDEXLAB_KLUCZ_TESTOWY lub ANTHROPIC_API_KEY i flagi --tak = zgoda właściciela na koszt)
//   Opcje: --limit N (pierwsze N pozycji), --przedmiot biologia, --effort low|medium|high, --rownolegle 4
//
// Raport: narzedzia/ocena-ai/raporty/<data>-<model>-<czesc>.{json,md}
// Metryki: zgodność punktów (cel ≥ 90%), poważne pomyłki (|różnica| ≥ 2 albo 0↔pełna; cel ≤ 2%),
// „czego zabrakło” — do przeglądu ręcznego (lista w raporcie; cel trafności ≥ 85%).
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { instrukcja, SCHEMAT } from '../../supabase/functions/_shared/ocena-instrukcja.ts';

const arg = (n, d) => { const i = process.argv.indexOf(`--${n}`); return i < 0 ? d : (process.argv[i + 1] ?? true); };
const jest = (n) => process.argv.includes(`--${n}`);
const MODELE = { haiku: 'claude-haiku-5-5', sonnet: 'claude-sonnet-5-5' };
const CENY = { 'claude-haiku-5-5': [0.10, 0.50], 'claude-sonnet-5-5': [2.00, 10.00] }; // $ / 1M tokenów (wej., wyj.)
const KURS = 3.7; // zł za $, przybliżenie
const model = MODELE[arg('model', 'haiku')] ?? arg('model');
const czesc = arg('czesc', 'robocza');
const effort = arg('effort', 'low');
const katalog = new URL('.', import.meta.url);
const korzen = new URL('../../', import.meta.url);

// --- zbiór i zadania ---
const zbior = readFileSync(new URL('zbior.jsonl', katalog), 'utf8').split('\n').filter((l) => l.trim() && !l.startsWith('//')).map((l) => JSON.parse(l));
const arkusze = new Map();
function zadanie(ref) { // „biologia/2024-maj/17.2”
  const [p, a, nr] = ref.split('/');
  const k = `${p}/${a}`;
  if (!arkusze.has(k)) arkusze.set(k, JSON.parse(readFileSync(new URL(`przedmioty/${p}/arkusze/${a}.json`, korzen), 'utf8')));
  for (const w of arkusze.get(k).wiazki) for (const z of w.zadania ?? []) if (String(z.nr) === nr) return z;
  throw new Error(`Brak zadania ${ref}`);
}
let lista = zbior.filter((x) => (czesc === 'wszystko' || x.czesc === czesc) && (!x.przeglad || process.argv.includes('--z-spornymi'))); // pozycje „do przeglądu” (sporny wzorzec) pomijamy
if (arg('przedmiot')) lista = lista.filter((x) => x.przedmiot === arg('przedmiot'));
if (arg('limit')) lista = lista.slice(0, Number(arg('limit')));
const pozycje = lista.map((x) => {
  const z = zadanie(x.ref);
  const max = Number(z.punkty) || 1;
  return { ...x, max, ...instrukcja(x.przedmiot, { polecenie: z.polecenie, material: z.material, klucz: z.odpowiedz, zasady: z.zasady }, max, x.odpowiedz) };
});

// --- szacunek (bez API): ~3 znaki/token dla polskiego tekstu, wyjście ~350 tokenów z rozumowaniem ---
const zl = (usd) => `${(usd * KURS).toFixed(2)} zł`;
function szacuj(m) {
  const [ci, co] = CENY[m];
  const wej = pozycje.reduce((s, x) => s + (x.system.length + x.tresc.length) / 3 + 250, 0);
  const wyj = pozycje.length * 350;
  const typ = (wej * ci + wyj * co) / 1e6;
  const max = (wej * ci + pozycje.length * 1500 * co) / 1e6; // sufit: max_tokens 1500
  return { wej: Math.round(wej), typ, max };
}
console.log(`Zbiór: ${pozycje.length} pozycji (część: ${czesc}${arg('przedmiot') ? `, ${arg('przedmiot')}` : ''})`);
for (const m of jest('szacuj') ? Object.values(MODELE) : [model]) {
  const s = szacuj(m);
  console.log(`  ${m}: ~${s.wej} tok. wejścia → szacunkowo ${zl(s.typ)} (najgorszy przypadek ${zl(s.max)})`);
}
if (jest('szacuj')) process.exit(0);
if (!jest('tak')) { console.log('\nPłatny przebieg wymaga flagi --tak (po zgodzie właściciela na powyższy koszt).'); process.exit(1); }

// --- przebieg ---
const { default: Anthropic } = await import('@anthropic-ai/sdk');
// Klucz: INDEXLAB_KLUCZ_TESTOWY (środowisko sesji nie przekazuje zmiennej o nazwie ANTHROPIC_API_KEY), albo ANTHROPIC_API_KEY lokalnie.
const apiKey = process.env.INDEXLAB_KLUCZ_TESTOWY || process.env.ANTHROPIC_API_KEY;
if (!apiKey) { console.error('Brak klucza: ustaw INDEXLAB_KLUCZ_TESTOWY lub ANTHROPIC_API_KEY.'); process.exit(1); }
const client = new Anthropic({ apiKey });
const wyniki = [];
let wejT = 0, wyjT = 0, i = 0;
async function ocen(x) {
  try {
    const out = await client.messages.create({
      model, max_tokens: 1500, system: x.system,
      output_config: { effort, format: { type: 'json_schema', schema: SCHEMAT } },
      messages: [{ role: 'user', content: x.tresc }],
    });
    wejT += out.usage.input_tokens; wyjT += out.usage.output_tokens;
    if (out.stop_reason === 'refusal') return { blad: 'refusal' };
    const t = out.content.find((c) => c.type === 'text');
    const r = JSON.parse(t.text);
    return { pkt: Math.max(0, Math.min(x.max, Math.round(Number(r.pkt) || 0))), brakuje: r.brakuje, uzasadnienie: r.uzasadnienie };
  } catch (e) { return { blad: String(e.message || e) }; }
}
const rownolegle = Number(arg('rownolegle', 4));
await Promise.all(Array.from({ length: rownolegle }, async () => {
  while (i < pozycje.length) {
    const x = pozycje[i++];
    const r = await ocen(x);
    wyniki.push({ id: x.id, przedmiot: x.przedmiot, typ: x.typ, max: x.max, wzor_pkt: x.wzor_pkt, wzor_brakuje: x.wzor_brakuje, odpowiedz: x.odpowiedz, ...r });
    process.stdout.write(r.blad ? 'E' : r.pkt === x.wzor_pkt ? '.' : 'x');
  }
}));
console.log();

// --- metryki ---
const powazna = (w) => Math.abs(w.pkt - w.wzor_pkt) >= 2 || (w.max > 1 && ((w.pkt === 0 && w.wzor_pkt === w.max) || (w.pkt === w.max && w.wzor_pkt === 0)));
function metryki(ws) {
  const ok = ws.filter((w) => !w.blad);
  const n = ok.length || 1;
  return { n: ws.length, bledy: ws.length - ok.length, zgodnosc: ok.filter((w) => w.pkt === w.wzor_pkt).length / n,
    powazne: ok.filter(powazna).length / n, zawyza: ok.filter((w) => w.pkt > w.wzor_pkt).length / n, zaniza: ok.filter((w) => w.pkt < w.wzor_pkt).length / n };
}
const grupuj = (klucz) => Object.fromEntries([...new Set(wyniki.map((w) => w[klucz]))].sort().map((k) => [k, metryki(wyniki.filter((w) => w[klucz] === k))]));
const koszt = (wejT * CENY[model][0] + wyjT * CENY[model][1]) / 1e6;
const raport = { data: new Date().toISOString(), model, effort, czesc, tokeny: { wej: wejT, wyj: wyjT }, koszt_usd: koszt,
  ogolem: metryki(wyniki), przedmiot: grupuj('przedmiot'), typ: grupuj('typ'), punkty: grupuj('max'), wyniki };
const proc = (v) => `${(v * 100).toFixed(1)}%`;
const wiersz = (k, m) => `| ${k} | ${m.n} | ${proc(m.zgodnosc)} | ${proc(m.powazne)} | ${proc(m.zawyza)} | ${proc(m.zaniza)} | ${m.bledy} |`;
const tab = (t, o) => [`### ${t}`, '| | n | zgodność | poważne | zawyża | zaniża | błędy |', '|---|---|---|---|---|---|---|', ...Object.entries(o).map(([k, m]) => wiersz(k, m)), ''].join('\n');
const md = [`# Test oceny AI — ${model} (effort ${effort}), część ${czesc}`, '', `${raport.data} · tokeny ${wejT}/${wyjT} · koszt ${zl(koszt)}`, '',
  '| | n | zgodność | poważne | zawyża | zaniża | błędy |', '|---|---|---|---|---|---|---|', wiersz('**ogółem**', raport.ogolem), '',
  'Progi: zgodność ≥ 90%, poważne ≤ 2%, trafność „czego zabrakło” ≥ 85% (przegląd ręczny poniżej).', '',
  tab('Przedmioty', raport.przedmiot), tab('Typy zadań', raport.typ), tab('Punktacja', raport.punkty),
  '## Rozbieżności', ...wyniki.filter((w) => w.blad || w.pkt !== w.wzor_pkt).map((w) => `- **${w.id}** wzór ${w.wzor_pkt}/${w.max}, AI ${w.blad ? `BŁĄD ${w.blad}` : `${w.pkt}/${w.max}`} — „${w.odpowiedz.slice(0, 160)}”${w.uzasadnienie ? `\n  - AI: ${w.uzasadnienie}` : ''}`),
  '', '## „Czego zabrakło” — do przeglądu', ...wyniki.filter((w) => !w.blad && w.wzor_brakuje?.length).map((w) => `- **${w.id}** wzór: ${w.wzor_brakuje.join('; ')}\n  - AI: ${(w.brakuje || []).join('; ') || '—'}`),
].join('\n');
mkdirSync(new URL('raporty/', katalog), { recursive: true });
const nazwa = `${raport.data.slice(0, 16).replace(/[:T]/g, '-')}-${model}-${czesc}`;
writeFileSync(new URL(`raporty/${nazwa}.json`, katalog), JSON.stringify(raport, null, 1));
writeFileSync(new URL(`raporty/${nazwa}.md`, katalog), md);
console.log(md.split('\n').slice(0, 8).join('\n'));
console.log(`\nRaport: narzedzia/ocena-ai/raporty/${nazwa}.md`);
