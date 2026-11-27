# Ocena AI — szkolenie Haiku do oceniania zadań otwartych

Dokument przekazania dla nowej sesji. Zawiera stan funkcji oceniania AI, decyzje właściciela i plan „szkolenia” tańszego modelu (Claude Haiku 5.5), tak aby oceniał prawie wszystkie zadania otwarte na poziomie dobrego korepetytora, a Sonnet zostawał tylko do trudnych przypadków.

Rozmowy z właścicielem prowadź po polsku.

## Cel

Haiku ocenia prawie wszystkie zadania otwarte z biologii, chemii, geografii, historii i WOS według zasad CKE. Wyjątki dla Sonneta: dłuższe wypowiedzi z historii i WOS oraz przypadki, które Haiku oznaczy jako niepewne. Dokładną granicę ustala wynik testu.

Model nie jest dotrenowywany (fine-tuning). „Szkolenie” = instrukcja oceniania + biblioteka przykładów + pętla poprawek mierzona na stałym zbiorze testowym.

## Stan obecny (już w repozytorium)

- `supabase/functions/ocen/index.ts` — funkcja Edge oceniająca odpowiedź. SDK `@anthropic-ai/sdk`, ustrukturyzowane wyjście (`output_config.format`, JSON: `pkt`, `uzasadnienie`, `brakuje[]`, `wskazowka`), `effort: low`, `max_tokens: 1500`, przycinanie wejścia (polecenie 3000, materiał 4000, klucz 3000, zasady 2000, odpowiedź 3000 znaków).
- Wybór modelu: zadania poniżej `OCENA_PROG_PKT` (domyślnie 2) → `OCENA_MODEL_PROSTE` (`claude-haiku-5-5`), od progu → `OCENA_MODEL_TRUDNE` (`claude-sonnet-5-5`). `OCENA_TRUDNE_PRZEDMIOTY` (np. `historia,wos`) wymusza Sonnet dla całego przedmiotu.
- `supabase/do-przegladarki/ocen.ts` — kopia jednoplikowa do wklejenia w edytorze Supabase (generuj ją ponownie po każdej zmianie funkcji).
- Migracje: `supabase/migrations/008_ocena_ai.sql` (tabela `ocena_ai`), `009_ocena_ai_limity.sql` (kolumny `darmowa`, `model`, `sesja`).
- Front: `js/app.js` (przycisk „Oceń moją odpowiedź (AI)”, karta wyniku, sugerowany wynik na przyciskach punktów), `js/dostep.js` (`ocen()`), `css/style.css` (`.ai-ocena`, `.ai-sugg`), wyłącznik `AI.ocena` w `js/config.js`.
- Dane zadań: `przedmioty/<przedmiot>/*.json` — arkusze CKE i zadania autorskie; pola `polecenie`, `odpowiedz` (klucz), `zasady`, `omowienie`, `punkty`, a w arkuszach `linkZasady` (link do oficjalnych zasad oceniania CKE).

## Limity (decyzja właściciela, liczone na najgorszy przypadek)

Wspólne na konto, działają tylko w przedmiotach z planu. Zadania — limit tygodniowy (ostatnie 7 dni), próbne matury AI — miesięczny (miesiąc kalendarzowy), maks. 30 ocen w jednej maturze.

| Plan | Cena | Oceny zadań | Matury AI |
|---|---|---|---|
| Darmowy | 0 zł | 3 łącznie | — |
| 1 przedmiot | 35 zł/mies. · 179 zł do matury | 12 / tydzień | 1 / miesiąc |
| 2 przedmioty | 55 zł/mies. · 289 zł | 18 / tydzień | 2 / miesiąc |
| Wszystkie | 70 zł/mies. · 369 zł | 20 / tydzień | 3 / miesiąc |

Najgorszy koszt oceny: Sonnet ok. 11 gr, Haiku ok. 0,5 gr. Limity są w sekrecie `OCENA_LIMITY` (JSON, opis w nagłówku funkcji). Jeśli Haiku przejdzie test, limity można podnieść — decyzja należy do właściciela.

## Progi jakości („ocenia jak korepetytor”)

- zgodność punktów z oceną wzorcową ≥ 90%,
- poważne pomyłki (różnica ≥ 2 pkt albo 0 zamiast pełnej/odwrotnie) ≤ 2%,
- trafność „czego zabrakło” ≥ 85%.

Te progi to propozycja, a nie standard CKE.

## Plan pracy

1. **Zbiór testowy** (`narzedzia/ocena-ai/zbior.jsonl`, wewnętrzny, nie trafia do aplikacji). Ok. 200 pozycji: ~40 na przedmiot, różne typy poleceń (podaj, wymień, wyjaśnij, uzasadnij, oblicz, porównaj, praca z materiałem). Do każdego zadania 3–4 odpowiedzi: pełna, częściowa, błędna, poprawna innymi słowami, „poprawna + błędna informacja”. Każda z oceną wzorcową (punkty + co brakuje) ustaloną wg zasad CKE; niejasne przypadki oznacz do przeglądu właściciela. Podział na część roboczą i kontrolną (kontrolnej nie używaj do poprawiania instrukcji).
2. **Skrypt testu** (`narzedzia/ocena-ai/test.mjs`): ocenia zbiór wybranym modelem tą samą instrukcją co funkcja `ocen` (wspólny moduł z promptem), liczy metryki ogółem, per przedmiot, per typ zadania i per punktacja, zapisuje raport. Przed każdym płatnym przebiegiem podaj szacowany koszt i poproś o zgodę.
3. **Test bazowy**: obecna instrukcja, Haiku i Sonnet.
4. **Ulepszanie instrukcji**: rozbicie klucza na elementy (model najpierw zaznacza „element jest / nie ma”, potem liczy punkty), reguły CKE wprost (sens zamiast dosłowności, błędna informacja obok poprawnej zeruje punkt, ogólniki nie dają punktu, odpowiedź musi wynikać z materiału), biblioteka przykładów dobieranych do typu zadania i przedmiotu, pole „niepewne” → eskalacja do Sonneta. Po każdej zmianie test na części roboczej, na koniec na kontrolnej.
5. **Wdrożenie**: przenieś ulepszoną instrukcję do `supabase/functions/ocen/index.ts`, ustaw podział Haiku/Sonnet (próg, przedmioty, eskalacja) i wygeneruj `do-przegladarki/ocen.ts`. Zbiór i skrypt zostają w repozytorium — przy nowej wersji Haiku wystarczy powtórzyć test.

Szacowany koszt API całego procesu: ok. 10–20 zł.

## Źródła materiałów

- **Zasady oceniania rozwiązań zadań** do każdego arkusza (cke.gov.pl → Egzamin maturalny → arkusze z danego roku): klucz, punktacja, często przykłady odpowiedzi uznanych i nieuznanych.
- **Informatory o egzaminie maturalnym** (cke.gov.pl → Informatory): przykładowe zadania z zasadami punktowania.
- **Sprawozdania z egzaminu** (cke.gov.pl): typowe błędy uczniów.
- **Aplikacja**: 10 arkuszy na przedmiot z kluczem, omówieniem i `linkZasady`; zadania autorskie IndexLab.
- Później: zgłoszenia „ocena AI się myli” od uczniów (za zgodą) jako nowe pozycje zbioru.

## Zasady i ograniczenia

- Nie kopiujemy materiałów CKE do aplikacji ani do zbioru — piszemy własne odpowiedzi testowe i własne opisy kryteriów na podstawie zasad CKE. W aplikacji: link do zasad + nasze omówienie.
- Klucz API tylko w sekretach (środowisko sesji / Supabase), nigdy w kodzie, repozytorium ani na czacie.
- Każdy płatny przebieg testu: najpierw szacunek kosztu i zgoda właściciela.
- Zmiany wypychaj na `main` i na gałąź roboczą sesji; commity kończ stopką podaną przez środowisko.

## Do zrobienia po stronie właściciela (jeśli jeszcze nie)

1. Supabase → SQL Editor: migracje `008_ocena_ai.sql` i `009_ocena_ai_limity.sql`.
2. console.anthropic.com: klucz API i miesięczny limit wydatków z powiadomieniami.
3. Supabase → Edge Functions → Secrets: `ANTHROPIC_API_KEY`; wdrożenie funkcji `ocen`.
4. Klucz API w środowisku nowej sesji (bezpieczny formularz), aby uruchamiać testy.
