// IndexLab — podcast: lista odcinków powstaje z działów kursu (1 odcinek na temat + 1 powtórka na dział).
// Gotowe nagrania dopisujemy tutaj: klucz = 'przedmiot/p/id-poddziału' albo 'przedmiot/d/id-działu',
// wartość = ścieżka do pliku MP3 (np. w katalogu podcast/mp3/) i długość.
import { NAGRANIA_AUTO } from './nagrania.js';

export const NAGRANIA = {
  ...NAGRANIA_AUTO,
  // 'wos/p/s-socjalizacja': { plik: 'podcast/mp3/wos-01-socjalizacja.mp3', min: 16 },
};

export function odcinki(s) {
  let nr = 0;
  return s.dzialy.map((d) => ({
    d,
    lista: [
      ...d.poddzialy.map((u) => ({ nr: ++nr, klucz: `${s.id}/p/${u.id}`, tytul: u.nazwa, typ: 'temat', min: '8–10' })),
      { nr: ++nr, klucz: `${s.id}/d/${d.id}`, tytul: `Powtórka działu: ${d.nazwa}`, typ: 'powtorka', min: '8–10' },
    ].map((o) => ({ ...o, nagranie: NAGRANIA[o.klucz] || null })),
  }));
}
