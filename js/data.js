// Kolumb — wczytywanie treści z plików JSON w katalogu przedmioty/.
const LITERY = ['A', 'B', 'C', 'D'];

async function fetchJSON(url) {
  const res = await fetch(url, { cache: 'no-cache' });
  if (!res.ok) throw new Error(`${url}: HTTP ${res.status}`);
  return res.json();
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

function normalizeSubject(raw, file) {
  const id = String(raw.id || file.replace(/\.json$/, ''));
  return {
    id,
    plik: file,
    nazwa: raw.nazwa || id,
    skrot: raw.skrot || raw.nazwa || id,
    ikona: raw.ikona || '📘',
    opis: raw.opis || '',
    dzialy: (raw.dzialy || []).map((d, i) => ({
      id: String(d.id || `dzial-${i + 1}`),
      nazwa: d.nazwa || `Dział ${i + 1}`,
      opis: d.opis || '',
      fiszki: (d.fiszki || []).map((f, j) => ({
        id: String(f.id ?? `f${j + 1}`),
        przod: f.przod || '',
        tyl: f.tyl || '',
        zrodlo: f.zrodlo || '',
      })),
      pytania: (d.pytania || [])
        .map(normalizeQuestion)
        .filter((q) => q.odpowiedzi.length >= 2),
    })),
  };
}

export async function loadSubjects() {
  const idx = await fetchJSON('przedmioty/index.json');
  const files = Array.isArray(idx) ? idx : idx.przedmioty || [];
  const results = await Promise.allSettled(files.map((f) => fetchJSON(`przedmioty/${f}`)));
  const subjects = [];
  const errors = [];
  results.forEach((r, i) => {
    if (r.status === 'fulfilled') subjects.push(normalizeSubject(r.value, files[i]));
    else errors.push(`${files[i]}: ${r.reason?.message || r.reason}`);
  });
  subjects.sort((a, b) => a.nazwa.localeCompare(b.nazwa, 'pl'));
  return { subjects, errors };
}
