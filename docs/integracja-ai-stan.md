# Integracja AI — stan prac (28.11.2026)

Notatka przekazania po sesji „Lista zadań integracji AI”. Plan całości: `docs/integracja-ai-lista.md`, szkolenie Haiku: `docs/ocena-ai-szkolenie.md`.

## Zrobione dziś

### Kroki właściciela
- [x] Migracje `008_ocena_ai.sql`, `009_ocena_ai_limity.sql` i nowa `010_ocena_ai_pamiec.sql` uruchomione w Supabase.
- [x] Konto API w console.anthropic.com (osobna organizacja IndexLab), doładowanie $20, **auto-reload wyłączony**.
- [x] Limit wydatków organizacji **$25/mies.**, powiadomienia e-mail przy $10 i $18.
- [x] Konto serwisowe `indexlab-ocen` (rola Developer, workspace Default).
- [x] Klucz `IndexLab-produkcja` → Supabase → Edge Functions → Secrets → `ANTHROPIC_API_KEY`.
- [x] Funkcja `ocen` wdrożona w Supabase (Verify JWT: włączone — tak ma zostać).
- [x] Klucz testowy `IndexLab-testy` (30 dni) → zmienna `ANTHROPIC_API_KEY` w środowisku chmurowym „apliakcja” (działa tylko w NOWYCH sesjach).

### Zadanie 1 — sprawdzenie `ocen` ✅
Test w aplikacji (biologia): maj 2024 zad. 17.2 → Sonnet, 2/2, trafne uzasadnienie; maj 2025 zad. 1.2 → Haiku, 1/1 i 0/1 poprawnie. Zapisy w tabeli `ocena_ai` z modelem, licznik limitu działa (plan „Wszystkie”: 20/tydz.).

### Zadanie 2 — „bez płacenia dwa razy” ✅ (na `main`)
- Identyczna odpowiedź (bez różnic w spacjach/wielkości liter) na to samo zadanie → zapisany wynik, 0 zł, bez zużycia limitu.
- Kolumny `skrot` (SHA-256) i `wynik` (jsonb) w `ocena_ai`; zmiana instrukcji → podbić `WERSJA_INSTRUKCJI`.
- Sprawdzone w Supabase: 2. kliknięcie nie dodało wiersza.
- Aplikacja pokazuje dopisek „Ta odpowiedź była już oceniona…”.

### Zadanie 3 — szkolenie Haiku: część bezpłatna ✅ (gałąź `claude/sharp-edison-dj5q65`, jeszcze NIE na `main`)
- `supabase/functions/_shared/ocena-instrukcja.ts` — wspólna instrukcja oceniania (funkcja i test używają tego samego tekstu). Działanie funkcji bez zmian — ponowne wdrożenie niepotrzebne.
- `narzedzia/ocena-ai/przegladarka.mjs` — generuje `supabase/do-przegladarki/ocen.ts` (uruchamiać po każdej zmianie funkcji lub instrukcji).
- `narzedzia/ocena-ai/test.mjs` — test jakości: `--szacuj` (bez API), płatny przebieg tylko z `--tak`; raporty w `narzedzia/ocena-ai/raporty/`.
- Zbiór testowy `narzedzia/ocena-ai/zbior.jsonl` (z plików `zbior_<przedmiot>.py`, składa `zbuduj-zbior.py`): **154 autorskie odpowiedzi** — biologia 41, chemia 29, geografia 28, historia 28, WOS 28; część robocza 97, kontrolna 57. Niejasne przypadki rozstrzygnięte wg zasad CKE (np. wynik bez obliczeń = 0, ogólnik = 0, błędny wzór na Kc = 0).

## Do zrobienia — następna sesja

**Otwórz NOWĄ sesję** (claude.ai/code → New session → repo `devrocketyy/kolumb` → środowisko **apliakcja**) i wklej:

```
Przeczytaj docs/integracja-ai-stan.md, docs/integracja-ai-lista.md i docs/ocena-ai-szkolenie.md. Kontynuuj zadanie 3 (szkolenie Haiku) z gałęzi claude/sharp-edison-dj5q65: zbiór (154 pozycje) i skrypt są w narzedzia/ocena-ai. Klucz testowy jest w zmiennej ANTHROPIC_API_KEY. Mam zgodę na test bazowy: Haiku i Sonnet na części roboczej (ok. 1,80 zł, maks. ok. 6 zł). Najpierw npm install w narzedzia/ocena-ai i --szacuj, potem uruchom oba przebiegi z --tak i omów wyniki po polsku.
```

Kolejne kroki:
1. **Test bazowy** (zgoda jest): Haiku + Sonnet, część robocza — ok. 1,80 zł (maks. ok. 6 zł).
2. **Ulepszanie instrukcji** pod Haiku (rozbicie klucza na elementy, reguły CKE wprost, pole „niepewne” → Sonnet, zabezpieczenia dla niepełnoletnich: tylko ocena zadania, bez rozmów na inne tematy). Każdy przebieg Haiku ok. 0,10 zł — przed każdym szacunek i zgoda.
3. **Sprawdzian końcowy** na części kontrolnej (Haiku + Sonnet, ok. 1,20 zł).
4. **Wdrożenie**: podbić `WERSJA_INSTRUKCJI`, ustawić podział Haiku/Sonnet, `node narzedzia/ocena-ai/przegladarka.mjs`, wkleić nowe `do-przegladarki/ocen.ts` w Supabase, wypchnąć na `main`.
5. Decyzje właściciela po teście: czy historia/WOS zawsze na Sonnecie; nowe limity (`OCENA_LIMITY`).

Cały proces szkolenia: szacunkowo **ok. 6 zł** (najgorzej ok. 15 zł) z doładowanych $20.

Dalej wg listy: 4. Sesja dnia → 5. Próbna matura AI → 6. Limity na ekranie Plany → 7. Licznik kosztów w panelu (+ ostrzeżenie o niedziałającym kluczu) → 8. Podniesienie limitów.

## Do pamiętania
- **Klucz testowy** wygasa po 30 dniach (ok. 28.12.2026) — po testach usuń go w console.anthropic.com → Keys i usuń zmienną ze środowiska „apliakcja”.
- **Klucz produkcyjny**: wymiana = nowy klucz → podmiana sekretu w Supabase → test oceny → usunięcie starego.
- **Auto-reload** włączyć dopiero przy płacących uczniach (np. przy $10 doładuj do $30); limit wtedy ok. $50–100.
- **Gemini (darmowy)**: odrzucony — oszczędność kilku zł, a ryzyko danych niepełnoletnich (RODO) i limitów.
- Ankieta Anthropic: zadeklarowano użytkowników < 18 lat i brak porad medycznych/prawnych/finansowych — przy ewentualnym czacie z AI dodać przekierowanie pytań osobistych („zapytaj lekarza / rodzica”).
- Uwaga do danych WOS: w niektórych kluczach (`odpowiedz`) są stopki „Egzamin maturalny z wiedzy o społeczeństwie…” skopiowane z PDF CKE — do wyczyszczenia przy okazji.
- Ceny (listopad 2026): Haiku 5.5 $0,10 / $0,50, Sonnet 5.5 $2 / $10 za 1M tokenów (wej./wyj.).
