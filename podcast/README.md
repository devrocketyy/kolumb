# Podcast IndexLab

Format: **jeden narrator**, spokojny ton, opowieść (styl podcastu reportażowego), nie lista faktów.
Każdy odcinek: scena otwierająca → opowieść z pojęciami wplecionymi w historię → „Co z tego będzie na maturze” → spokojne podsumowanie i trzy pytania do przemyślenia.

- Odcinki tematyczne: ok. 13–18 min (ok. 1 700–2 400 słów).
- Odcinki działowe (powtórka przed arkuszem): ok. 25–30 min.

Wskazówki dla lektora (Azure SSML) w nawiasach kwadratowych, np. [pauza], [wolniej] — generator zamieni je na znaczniki.

## Tryb aktywny (pytania w trakcie odcinka)

- W scenariuszu `[pytanie: id]` oznacza miejsce zatrzymania w trybie aktywnym (lektor go nie czyta).
- `[odpowiedź]` … `[koniec odpowiedzi]` to fragment pomijany w trybie aktywnym, bo uczeń widzi odpowiedź na karcie.
- Pytania do odcinka: `podcast/pytania/<odcinek>.json` (typy: `abcd`, `laczenie`). Poprawna odpowiedź jest pierwsza, a odtwarzacz losuje kolejność.
- Tryb pasywny odtwarza całe nagranie bez zatrzymań.
- Pilot: `biologia-06-woda`.
