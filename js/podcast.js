// IndexLab — podcast: lista odcinków powstaje z działów kursu (1 odcinek na temat + 1 powtórka na dział).
// Gotowe nagrania dopisujemy tutaj: klucz = 'przedmiot/p/id-poddziału' albo 'przedmiot/d/id-działu',
// wartość = ścieżka do pliku MP3 (np. w katalogu podcast/mp3/) i długość.
export const NAGRANIA = {
  'biologia/p/b-woda': { plik: 'podcast/mp3/biologia-06-woda.mp3', min: 8, pytania: 'podcast/pytania/biologia-06-woda.json', czasy: 'podcast/mp3/biologia-06-woda.json' },
  // 'wos/p/s-socjalizacja': { plik: 'podcast/mp3/wos-01-socjalizacja.mp3', min: 16 },
};

export function odcinki(s) {
  let nr = 0;
  return s.dzialy.map((d) => ({
    d,
    lista: [
      ...d.poddzialy.map((u) => ({ nr: ++nr, klucz: `${s.id}/p/${u.id}`, tytul: u.nazwa, typ: 'temat', min: '13–18' })),
      { nr: ++nr, klucz: `${s.id}/d/${d.id}`, tytul: `Powtórka działu: ${d.nazwa}`, typ: 'powtorka', min: '25–30' },
    ].map((o) => ({ ...o, nagranie: NAGRANIA[o.klucz] || null })),
  }));
}
