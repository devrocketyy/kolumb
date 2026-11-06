// IndexLab — wczytywanie treści z plików JSON w katalogu przedmioty/.
//
// Przedmiot (przedmioty/<id>.json) zawiera listę działów. Dział może:
//  • mieć fiszki i pytania bezpośrednio (jeden poddział),
//  • mieć listę "poddzialy",
//  • wskazywać osobny plik: { "plik": "wos/prawo.json" } (ścieżka względem przedmioty/).
// Przedmiot może też mieć "arkusze" — zadania maturalne (również w osobnych plikach).

const LITERY = ['A', 'B', 'C', 'D'];

async function fetchJSON(url) {
  const res = await fetch(url, { cache: 'no-cache' });
  if (!res.ok) throw new Error(`${url}: HTTP ${res.status}`);
  return res.json();
}

async function resolve(item) {
  if (!item || !item.plik) return item;
  const ext = await fetchJSON(`przedmioty/${item.plik}`);
  return { ...ext, ...item, plik: item.plik };
}

function normalizeQuestion(q, i) {
  let correct = q.poprawna;
  if (typeof correct === 'string') correct = LITERY.indexOf(correct.trim().toUpperCase());
  return {
    id: String(q.id ?? `p${i + 1}`),
    pytanie: q.pytanie || '',
    odpowiedzi: Array.isArray(q.odpowiedzi) ? q.odpowiedzi.map(String) : [],
    poprawna: Number.isInteger(correct) ? correct : 0,
    wyjasnienie: q.wyjasnienie || '',
    zrodlo: q.zrodlo || '',
  };
}

function normalizeUnit(u, i, dzialId) {
  return {
    id: String(u.id || `${dzialId}-${i + 1}`),
    dzialId,
    nazwa: u.nazwa || `Część ${i + 1}`,
    opis: u.opis || '',
    fiszki: (u.fiszki || []).map((f, j) => ({
      id: String(f.id ?? `f${j + 1}`),
      przod: f.przod || '',
      tyl: f.tyl || '',
      zrodlo: f.zrodlo || '',
    })),
    pytania: (u.pytania || []).map(normalizeQuestion).filter((q) => q.odpowiedzi.length >= 2),
  };
}

function normalizeDzial(d, i) {
  const id = String(d.id || `dzial-${i + 1}`);
  const raw = Array.isArray(d.poddzialy) && d.poddzialy.length
    ? d.poddzialy
    : [{ id, nazwa: d.nazwa, opis: d.opis, fiszki: d.fiszki, pytania: d.pytania }];
  return {
    id,
    nazwa: d.nazwa || `Dział ${i + 1}`,
    opis: d.opis || '',
    poddzialy: raw.map((u, j) => normalizeUnit(u, j, id)),
  };
}

function normalizeArkusz(a, i) {
  const id = String(a.id || `arkusz-${i + 1}`);
  const wiazki = (a.wiazki || []).map((w) => ({
    nr: String(w.nr ?? ''),
    tytul: w.tytul || '',
    material: w.material || '',
    uwaga: w.uwaga || '',
    zadania: (w.zadania || []).map((z) => ({
      nr: String(z.nr),
      polecenie: z.polecenie || '',
      odpowiedz: z.odpowiedz || '',
      zasady: z.zasady || '',
      punkty: Number(z.punkty) || 1,
      dzialy: Array.isArray(z.dzialy) ? z.dzialy.map(String) : [],
    })),
  }));
  const zadania = [];
  wiazki.forEach((w) => w.zadania.forEach((z) => zadania.push({ ...z, arkusz: id, wiazka: w })));
  return {
    id,
    nazwa: a.nazwa || id,
    opis: a.opis || '',
    zrodlo: a.zrodlo || '',
    wiazki,
    zadania,
    punkty: zadania.reduce((n, z) => n + z.punkty, 0),
  };
}

// Bank zadań autorskich: wiązki przypisane do działów, z typem każdego zadania.
function normalizeBank(b) {
  return (b.wiazki || []).map((w) => ({
    id: String(w.id),
    dzial: String(w.dzial || b.dzial || ''),
    tytul: w.tytul || '',
    material: w.material || '',
    uwaga: w.uwaga || '',
    zrodlo: w.zrodlo || 'Zadanie autorskie IndexLab',
    autorskie: true,
    zadania: (w.zadania || []).map((z, i) => ({
      nr: String(z.nr ?? i + 1),
      typ: z.typ || 'otwarte',
      punkty: Number(z.punkty) || 1,
      polecenie: z.polecenie || '',
      odpowiedz: z.odpowiedz || '',
      zasady: z.zasady || '',
      dzialy: [String(w.dzial || b.dzial || '')],
    })),
  }));
}

async function normalizeSubject(raw, file) {
  const id = String(raw.id || file.replace(/\.json$/, ''));
  const dzialyRaw = await Promise.all((raw.dzialy || []).map(resolve));
  const arkuszeRaw = await Promise.all((raw.arkusze || []).map(resolve));
  const bankRaw = await Promise.all((raw.bank || []).map(resolve));
  const aktualnosci = raw.aktualnosci ? await resolve(raw.aktualnosci) : null;
  const dzialy = dzialyRaw.map(normalizeDzial);
  const units = new Map();
  dzialy.forEach((d) => d.poddzialy.forEach((u) => units.set(u.id, u)));
  return {
    id,
    plik: file,
    nazwa: raw.nazwa || id,
    skrot: raw.skrot || raw.nazwa || id,
    ikona: raw.ikona || '📘',
    opis: raw.opis || '',
    dzialy,
    units,
    arkusze: arkuszeRaw.map(normalizeArkusz),
    bank: bankRaw.filter(Boolean).flatMap(normalizeBank),
    aktualnosci,
    wagi: raw.wagi || null,
    srednia: raw.srednia || null,
  };
}

export async function loadSubjects() {
  const idx = await fetchJSON('przedmioty/index.json');
  const files = Array.isArray(idx) ? idx : idx.przedmioty || [];
  const results = await Promise.allSettled(
    files.map(async (f) => normalizeSubject(await fetchJSON(`przedmioty/${f}`), f))
  );
  const subjects = [];
  const errors = [];
  results.forEach((r, i) => {
    if (r.status === 'fulfilled') subjects.push(r.value);
    else errors.push(`${files[i]}: ${r.reason?.message || r.reason}`);
  });
  subjects.sort((a, b) => a.nazwa.localeCompare(b.nazwa, 'pl'));
  return { subjects, errors };
}
