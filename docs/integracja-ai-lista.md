# Lista zadań integracji AI

Dokument startowy dla osobnej rozmowy „Lista zadań integracji AI”. Opisuje, jak ma wyglądać nauka z AI w IndexLab, co już jest w kodzie, co musi zrobić właściciel i co trzeba zbudować. Rozmowy z właścicielem prowadź po polsku.

Powiązany dokument: `docs/ocena-ai-szkolenie.md` (szkolenie Haiku — zbiór testowy, progi jakości, pętla poprawek).

## Cel właściciela

- **Wysokie limity** i **dobre sprawdzanie** za **niewielką cenę**.
- Uczeń w jednym, przyjemnym miejscu ma zadania **ABCD**, **otwarte** i **zadania z oceną AI**.

## Pomysł: „Sesja dnia” (zamknięte + otwarte + AI)

Zasada kosztowa: **ABCD i zadania otwarte z kluczem nic nie kosztują i nie mają limitu.** AI ocenia tylko to, co najbardziej się opłaca — dlatego limity mogą być wysokie.

Jedna sesja ok. 15–20 min, układana automatycznie z mapy luk ucznia (najsłabsze poddziały):

1. **Rozgrzewka — 8–10 pytań ABCD** z najsłabszego działu. Natychmiastowa informacja zwrotna, bez AI.
2. **Fiszki do powtórki** (z kolejki SRS), jeśli są zaległe.
3. **2 zadania otwarte z kluczem** — uczeń pisze odpowiedź, porównuje z kluczem, sam zaznacza punkty (bez AI).
4. **1 „Zadanie z oceną AI”** — zadanie otwarte za 2–3 pkt typu „wyjaśnij / uzasadnij” z najsłabszego działu. AI ocenia jak egzaminator: punkty, czego zabrakło, wskazówka. To jedyny krok, który zużywa limit.
5. **Podsumowanie** — wynik sesji, zmiana opanowania poddziałów, prognoza matury, „jutro: …”.

Dodatkowo, poza sesją:
- Przy każdym zadaniu otwartym przycisk **„Oceń moją odpowiedź (AI)”** (już jest) — zużywa ten sam limit.
- **Próbna matura AI** — pełny arkusz na czas, zamknięte sprawdzane automatycznie, otwarte oceniane przez AI, wynik w % i przelicznik na punkty rekrutacyjne. Osobny limit miesięczny.

Dlaczego to dobrze działa:
- Uczeń ma codzienny, gotowy plan zamiast wybierania z listy.
- Większość ćwiczeń (ABCD, klucz) jest darmowa, więc limit AI wystarcza na długo.
- AI trafia tam, gdzie daje najwięcej: zadania „wyjaśnij/uzasadnij”, których uczeń sam nie oceni dobrze.

## Jak uzyskać wysokie limity przy niskiej cenie

1. **Haiku do prawie wszystkiego** (po szkoleniu z `docs/ocena-ai-szkolenie.md`), Sonnet tylko do dłuższych wypowiedzi z historii/WOS i przypadków oznaczonych jako niepewne. Najgorszy koszt oceny: Haiku ok. 0,5 gr, Sonnet ok. 11 gr.
2. **Bez płacenia dwa razy** — ta sama odpowiedź na to samo zadanie zwraca zapisany wynik.
3. **Ocena tylko po wpisaniu odpowiedzi** (min. kilka słów) i tylko dla zadań z kluczem.
4. **Przycinanie wejścia i `max_tokens: 1500`** — już w funkcji `ocen`, twardy sufit kosztu jednej oceny.
5. **Limit wydatków w console.anthropic.com** — ostateczne zabezpieczenie.

Limity dziś (najgorszy przypadek, wszystko na Sonnecie od 2 pkt):

| Plan | Cena | Oceny AI zadań | Matury AI |
|---|---|---|---|
| Darmowy | 0 zł | 3 łącznie | — |
| 1 przedmiot | 35 zł/mies. · 179 zł do matury | 12 / tydzień | 1 / miesiąc |
| 2 przedmioty | 55 zł/mies. · 289 zł | 18 / tydzień | 2 / miesiąc |
| Wszystkie | 70 zł/mies. · 369 zł | 20 / tydzień | 3 / miesiąc |

Cel po szkoleniu Haiku (jeśli przejdzie progi jakości): **ok. 5× wyższe limity** przy podobnym koszcie, np. 60 / 90 / 100 ocen tygodniowo. Ostateczne liczby ustala właściciel po teście; zmiana przez sekret `OCENA_LIMITY`, bez zmian w kodzie.

## Co już jest w kodzie

- Funkcja Edge `supabase/functions/ocen/index.ts` (+ kopia `supabase/do-przegladarki/ocen.ts`): ocena wg klucza CKE, ustrukturyzowane wyjście JSON, `effort: low`, Haiku dla zadań < 2 pkt i Sonnet od 2 pkt, limity tygodniowe i miesięczne (sesje matur), darmowa pula, zapis do tabeli `ocena_ai`.
- Migracje `supabase/migrations/008_ocena_ai.sql`, `009_ocena_ai_limity.sql`.
- Przycisk „Oceń moją odpowiedź (AI)” i karta wyniku w ekranie zadania (`js/app.js`, `js/dostep.js`, `css/style.css`), wyłącznik `AI.ocena` w `js/config.js`.
- Istniejące elementy do wykorzystania w „Sesji dnia”: fiszki SRS (`js/srs.js`), pytania ABCD, zadania otwarte z kluczem, plan nauki i prognoza wyniku w `js/app.js`.

## Kroki właściciela (bez nich AI nie ruszy)

1. **Supabase → SQL Editor**: uruchom `supabase/migrations/008_ocena_ai.sql`, potem `009_ocena_ai_limity.sql`.
2. **console.anthropic.com**: utwórz osobny klucz API dla IndexLab; ustaw miesięczny limit wydatków (np. 200 zł) i powiadomienia przy 50% i 80%.
3. **Supabase → Edge Functions → Secrets**: dodaj `ANTHROPIC_API_KEY` (nigdy w kodzie ani na czacie).
4. **Wdróż funkcję `ocen`**: `supabase functions deploy ocen` albo wklej `supabase/do-przegladarki/ocen.ts` w edytorze funkcji pod nazwą `ocen`.
5. **Klucz API w środowisku sesji Claude** (bezpieczny formularz) — potrzebny do testów jakości.
6. **Decyzje**: zgoda na koszt testów (ok. 10–20 zł), ostateczne limity po teście Haiku, czy historia/WOS zawsze na Sonnecie.

## Zadania do zbudowania (kolejność)

| # | Zadanie | Szac. czas |
|---|---|---|
| 1 | Sprawdzenie działania `ocen` na prawdziwych zadaniach po krokach właściciela | 1–2 h |
| 2 | „Bez płacenia dwa razy” — zapamiętanie wyniku dla identycznej odpowiedzi | 0,5 h |
| 3 | Szkolenie Haiku wg `docs/ocena-ai-szkolenie.md` (zbiór, test, instrukcja, wdrożenie) | 10–14 h |
| 4 | „Sesja dnia”: generator sesji z mapy luk (ABCD → fiszki → 2 otwarte z kluczem → 1 z AI → podsumowanie) | 6–8 h |
| 5 | Próbna matura AI: arkusz na czas, sesja `matura` w `ocen`, wynik w % i przelicznik na punkty rekrutacyjne | 6–10 h |
| 6 | Limity AI na ekranie „Plany” i licznik „Oceny AI w tym tygodniu” w profilu | 1–2 h |
| 7 | Licznik kosztów AI w panelu właściciela (oceny dziś/miesiąc, model, szacowany koszt) | 1–2 h |
| 8 | Podniesienie limitów po teście Haiku (sekret `OCENA_LIMITY`) i aktualizacja oferty | 0,5 h |

Razem ok. 26–40 h pracy w sesjach.

## Zasady

- Klucze API tylko w sekretach — nigdy w kodzie, repozytorium ani na czacie.
- Każdy płatny test: najpierw szacunek kosztu i zgoda właściciela.
- Nie kopiujemy materiałów CKE do aplikacji — link do zasad + własne omówienie.
- Zmiany wypychaj na `main` i gałąź roboczą sesji; commity kończ stopką podaną przez środowisko.
- Aplikacja: https://app.indexlab.pl
