# IndexLab — stan projektu i lista dalszych prac

Stan na 20 listopada 2026. Aplikacja działa w trybie prywatnym.
Link właściciela: https://app.indexlab.pl/?klucz=ni-D4DOaRe8m (publikacja: `docs/06`).

## 1. Co jest zrobione

### Aplikacja (wszystkie przedmioty)
- Logowanie przez Supabase: imię, e-mail, hasło (podgląd hasła), magic link.
  - Na komputerze ekran logowania przy każdej nowej wizycie, z przyciskiem „Kontynuuj jako…”.
  - Usuwanie konta (migracja `002_usun_konto.sql`).
- Regulamin i polityka prywatności (`prawne/`), zgody przy rejestracji i zakupie.
  - Dane usługodawcy uzupełnione (23.11.2026). Adres do korespondencji do podmiany na wirtualne biuro po pierwszych przychodach.
- Program poleceń (`?ref=`, migracja `003_polecenia.sql`).
- Prognoza wyniku:
  - punkty na 60 i realny cel na maj;
  - wykres postępu;
  - sekcja „Gdzie zyskasz najwięcej”;
  - test diagnostyczny z 20 pytań.
- Podcast (`#/podcast`, plan odcinków w `docs/05`).
- Gra „Oś czasu” z historii.
- Chronologia: 245 dat z omówieniami, okienko po kliknięciu daty.
- Nowy ekran ładowania i ładniejszy ekran logowania.
- Tryb prywatny: strona „Już wkrótce”, noindex, robots.txt.

### Historia i WOS
- Pełne kursy: fiszki, ABCD, zadania autorskie (około 330 zadań dopisanych w tej serii).
- Omówienia arkuszy CKE.

### Biologia (przedmiot flagowy)

| | Zrobione | Plan |
|---|---|---|
| Działy / podrozdziały | 13 / **71 z 71** | 13 / 71 |
| Fiszki | 3618 unikalnych (+ 823 odwrócone) | ~3620 ✅ |
| Pytania ABCD | 1492 | ~1500 ✅ |
| Zadania autorskie | 903 (467 wiązek) | ~920 |
| Omówienia matur CKE | 6 arkuszy, 295 zadań (wszystkie z omówieniem) | ~11 arkuszy |
| Schematy | 171 (43 rysunki, 128 procesów i cykli) | ~170 ✅ |

- Arkusze z omówieniem: maj i czerwiec 2024, 2025 i 2026.
- Audyt z 20 listopada 2026 (`narzedzia/biologia/usuniete.py`, `omowienia_ark.py`):
  - usunięte powtórzenia: 156 fiszek, 25 pytań ABCD, 4 wiązki zadań (to samo pojęcie lub zadanie w dwóch miejscach);
  - uzupełnione 103 brakujące omówienia zadań z arkuszy CKE;
  - fiszki odwrócone („Rozpoznaj…”) tylko z pojęć — bez zgadywania tytułów zestawień;
  - dopisane nowe fiszki i pytania z pojęć, których brakowało (sprawdzone pod kątem powtórzeń);
  - licznik fiszek liczy tylko fiszki rzeczywiście trafiające do aplikacji.
- Kurs przechodzi automatyczną kontrolę bez błędów i ostrzeżeń:
  - brak powtórzeń;
  - poprawna odpowiedź ABCD nie zdradza się długością.

## 2. Co jeszcze trzeba zrobić

### Biologia — treści
1. Pytania ABCD: plan osiągnięty (1492).
2. Fiszki: plan osiągnięty ✅.
3. Zadania autorskie: plan praktycznie osiągnięty (903).
   - Najwięcej brakuje w: mikroorganizmach, zwierzętach, ewolucji i ekologii, biotechnologii.
4. Arkusze CKE:
   - matura maj 2023 (brak na Drive — trzeba dograć);
   - próbna z stycznia 2026 (do decyzji, czy to arkusz CKE);
   - bank zadań ze starej formuły 2015–2022, filtrowany do obecnej podstawy.
5. Schematy: plan osiągnięty ✅ (171).
   - Rysunki do podpisania (tryb „Podpisz”) i procesy do ułożenia (tryb „Ułóż etapy”); wejście: Nauka → Schematy oraz z poddziału.
   - Źródła w `narzedzia/biologia/schematy*.py`; builder sprawdza znaczniki, powtórzenia i długość list.
6. Data matury z biologii 2027 — potrzebna do odliczania i prognozy.
   - Strona CKE jest zablokowana w moim środowisku.

### Biologia — sprawdzenie (lista w `docs/08`)
- Merytoryczne przeczytanie wszystkich działów przez nauczyciela lub dobrego ucznia.
- Linki do PDF-ów CKE (zbudowane według wzoru, niesprawdzone).
- Zadania z arkuszy oparte na rysunkach — porównać numery i litery z oryginałem.

### Funkcje aplikacji
- Sprawdzanie wypracowań i zadań otwartych przez AI.
  - Limity: Pro — 40 zadań krótkich i 3 wypracowania tygodniowo; darmowe — 3 + 1 na próbę.
  - Wymaga klucza API wpisanego w ustawieniach Supabase (nie w czacie ani repozytorium).
- Płatności (webhook z nagrodą za polecenie jest gotowy, brakuje podpięcia bramki).

### Formalności przed publikacją
- Uzupełnić dane w regulaminie i polityce prywatności.
- Wyłączyć tryb prywatny (instrukcja w `docs/06`).
- Fiszki na fiszki.indexlab.pl/prawa-czlowieka — nie ruszać do końca sezonu olimpijskiego.

## Docelowy model sprzedaży (ustalenie właściciela)
- **Matura** (dostęp do przedmiotów) — sprzedawana w aplikacji app.indexlab.pl (Stripe Checkout → webhook → `dostep_przedmiot`).
- **Kursy** — w przyszłości sprzedawane przez stronę internetową indexlab.pl (osobny produkt w Stripe, ta sama zasada `metadata.app` do rozróżniania płatności na wspólnym koncie).
