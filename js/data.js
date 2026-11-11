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

// Źródło plików: domyślnie katalog przedmioty/, w trybie premium — treści z bazy (null = brak dostępu).
let pobierz = (plik) => fetchJSON(`przedmioty/${plik}`);

async function resolve(item) {
  if (!item || !item.plik) return item;
  const { zarys, ...ref } = item;
  const ext = await pobierz(item.plik);
  // treść premium bez dostępu: zostaje sam zarys (nazwy działów i tematów), oznaczony jako zablokowany
  if (ext == null) return { ...(zarys || {}), ...ref, zablokowany: true };
  return { ...ext, ...ref, plik: item.plik };
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

function normalizeUnit(u, i, dzialId, zablokowany) {
  return {
    id: String(u.id || `${dzialId}-${i + 1}`),
    dzialId,
    zablokowany: !!zablokowany,
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
    zablokowany: !!d.zablokowany,
    poddzialy: raw.map((u, j) => normalizeUnit(u, j, id, d.zablokowany)),
  };
}

function normalizeArkusz(a, i) {
  const id = String(a.id || `arkusz-${i + 1}`);
  const wiazki = (a.wiazki || []).map((w) => ({
    nr: String(w.nr ?? ''),
    tytul: w.tytul || '',
    material: w.material || '',
    uwaga: w.uwaga || '',
    // arkusz „link + omówienie”: materiał źródłowy zostaje w oryginalnym PDF CKE (strona w arkuszu)
    link: a.link ? `${a.link}#page=${Number(w.strona) || 1}` : '',
    strona: Number(w.strona) || 0,
    zadania: (w.zadania || []).map((z) => ({
      nr: String(z.nr),
      polecenie: z.polecenie || '',
      odpowiedz: z.odpowiedz || '',
      zasady: z.zasady || '',
      omowienie: z.omowienie || '',
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
    link: a.link || '',
    linkZasady: a.linkZasady || '',
    zablokowany: !!a.zablokowany,
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

// Brak jednego pliku (np. arkusza) nie może wyłączyć całego przedmiotu — pomijamy go i zgłaszamy.
let bledyPlikow = [];
const resolveSafe = (item) => resolve(item).catch((e) => { bledyPlikow.push(e.message); return null; });

async function normalizeSubject(raw, file) {
  const id = String(raw.id || file.replace(/\.json$/, ''));
  const dzialyRaw = (await Promise.all((raw.dzialy || []).map(resolveSafe))).filter(Boolean);
  const arkuszeRaw = (await Promise.all((raw.arkusze || []).map(resolveSafe))).filter(Boolean);
  const bankRaw = await Promise.all((raw.bank || []).map(resolveSafe));
  const akt = raw.aktualnosci ? await resolveSafe(raw.aktualnosci) : null;
  const aktualnosci = akt && !akt.zablokowany ? akt : null;
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
    egzamin: raw.egzamin || null, // data matury (RRRR-MM-DD) — podstawa planu nauki
  };
}

// Wczytywanie dwuetapowe (szybki start): najpierw spis i „szkielety” przedmiotów (kilka KB),
// potem pełne treści — w kolejności, od przedmiotu, którego uczeń teraz się uczy.
export async function loadIndex(zrodlo) {
  bledyPlikow = [];
  if (zrodlo) pobierz = async (plik) => (zrodlo.has(plik) ? zrodlo.get(plik) : null);
  const idx = await pobierz('index.json');
  if (!idx) throw new Error('Brak spisu przedmiotów.');
  const files = Array.isArray(idx) ? idx : idx.przedmioty || [];
  const raws = await Promise.all(files.map((f) => pobierz(f).catch((e) => { bledyPlikow.push(`${f}: ${e.message}`); return null; })));
  return files.map((f, i) => ({ file: f, raw: raws[i] })).filter((x) => x.raw)
    .map(({ file, raw }) => ({ file, raw, stub: { ...stubSubject(raw, file), _raw: raw } }));
}

// Przedmiot bez treści — wystarcza do ekranów wyboru profilu i kursu.
function stubSubject(raw, file) {
  const id = String(raw.id || file.replace(/\.json$/, ''));
  return { id, plik: file, nazwa: raw.nazwa || id, skrot: raw.skrot || raw.nazwa || id, ikona: raw.ikona || '📘', opis: raw.opis || '',
    dzialy: [], units: new Map(), arkusze: [], bank: [], aktualnosci: null, wagi: null, srednia: raw.srednia || null, egzamin: raw.egzamin || null, szkielet: true };
}

export async function loadFull(entry) {
  return normalizeSubject(entry.raw, entry.file);
}

export const takeErrors = () => { const e = bledyPlikow; bledyPlikow = []; return e; };

// zrodlo (opcjonalnie): Map plik → dane, np. treści z bazy; brak pliku w mapie = brak dostępu.
export async function loadSubjects(zrodlo) {
  bledyPlikow = [];
  if (zrodlo) pobierz = async (plik) => (zrodlo.has(plik) ? zrodlo.get(plik) : null);
  const idx = await pobierz('index.json');
  if (!idx) throw new Error('Brak spisu przedmiotów.');
  const files = Array.isArray(idx) ? idx : idx.przedmioty || [];
  const results = await Promise.allSettled(
    files.map(async (f) => {
      const raw = await pobierz(f);
      if (!raw) throw new Error('brak dostępu');
      return normalizeSubject(raw, f);
    })
  );
  const subjects = [];
  const errors = bledyPlikow;
  bledyPlikow = [];
  results.forEach((r, i) => {
    if (r.status === 'fulfilled') subjects.push(r.value);
    else errors.push(`${files[i]}: ${r.reason?.message || r.reason}`);
  });
  subjects.sort((a, b) => a.nazwa.localeCompare(b.nazwa, 'pl'));
  return { subjects, errors };
}
