# 🧭 Kolumb — nauka do matury

Kolumb to aplikacja webowa do nauki do matury: **fiszki z powtórkami rozłożonymi w czasie**, **testy ABCD** i **prawdziwe zadania maturalne CKE z kluczem odpowiedzi**.
Działa w przeglądarce na telefonie, tablecie i komputerze, można ją dodać do ekranu głównego i uczyć się **bez internetu**.

- czysty HTML, CSS i JavaScript — bez backendu, bez kosztów utrzymania,
- hosting na GitHub Pages,
- postępy zapisywane w przeglądarce (`localStorage`),
- treści w plikach JSON: przedmiot → dział → poddział → fiszki i pytania.

## Treści — Wiedza o społeczeństwie (matura rozszerzona)

| Dział | Poddziały | Fiszki | Pytania ABCD |
|---|---|---|---|
| Człowiek i społeczeństwo | 7 | 615 | 43 |
| Społeczeństwo obywatelskie i partycypacja | 4 | 276 | 20 |
| Państwo, ideologie i rywalizacja o władzę | 5 | 368 | 30 |
| Ustrój Rzeczypospolitej Polskiej | 10 | 767 | 82 |
| Systemy polityczne państw | 6 | 233 | 31 |
| Prawo w Rzeczypospolitej Polskiej | 7 | 667 | 44 |
| Prawa człowieka i ich ochrona | 3 | 172 | 19 |
| Stosunki międzynarodowe | 6 | 328 | 34 |
| Integracja europejska | 3 | 181 | 24 |
| **Razem** | **51** | **3607** | **327** |

**Zadania maturalne:** arkusze CKE z maja i czerwca 2023 r. (formuła 2023) — 88 zadań (120 pkt) z materiałami źródłowymi, poleceniami, przykładowymi odpowiedziami i zasadami oceniania. Każde zadanie jest przypisane do działów na podstawie wymagań egzaminacyjnych podanych przez CKE.

Podział na działy wynika z wymagań egzaminacyjnych (podstawy programowej). Najwięcej punktów w arkuszach 2023–2024 przypadało na: prawo w RP, organy władzy w RP, człowieka i społeczeństwo, systemy polityczne państw, ład międzynarodowy i społeczeństwo obywatelskie.

Każda fiszka i każde pytanie ma pole `zrodlo` — numer artykułu aktu prawnego (np. „Konstytucja RP, art. 104”, „Kodeks cywilny, art. 158”) albo dział podstawy programowej. Błędy można zgłaszać przyciskiem „Zgłoś błąd”.

## Funkcje

| Ekran | Co robi |
|---|---|
| **Nauka** (ekran główny) | Przedmioty i działy z paskiem opanowania, licznik „dziś do powtórki”, seria dni nauki. |
| **Dział / poddział** | Postęp, liczba powtórek i nowych fiszek, przyciski: fiszki, test, zadania maturalne z działu, przegląd treści. Naukę można prowadzić dla całego działu albo pojedynczego poddziału. |
| **Fiszki** | Pytanie z przodu, odpowiedź po dotknięciu. Oceny **Nie wiem / Trudne / Umiem**. Powtórki według systemu Leitnera. Tryb „trening swobodny” — 50 losowych fiszek bez wpływu na harmonogram. |
| **Test** | 10 losowych pytań ABCD (kolejność odpowiedzi też losowa), od razu informacja o poprawności z wyjaśnieniem i źródłem, na końcu wynik procentowy i lista błędów. |
| **Matura** | Arkusze CKE i zadania według działów. Materiał źródłowy, polecenie, miejsce na własną odpowiedź, klucz CKE z zasadami oceniania i samoocena punktowa. |
| **Statystyki** | Opanowane i poznane fiszki, seria dni nauki, ostatnie 14 dni, wynik zadań maturalnych, opanowanie działów, ostatnie testy. |
| **Ustawienia** | Motyw jasny / ciemny / systemowy, liczba nowych fiszek dziennie (10/20/30/50), instalacja aplikacji, kopia postępów, zerowanie postępów. |
| **Zgłoś błąd** | Przy każdej fiszce, pytaniu i zadaniu. Otwiera e-mail do `roc7et@gmail.com` z pełną treścią. |

Skróty klawiszowe: **spacja** odwraca fiszkę, **1 / 2 / 3** to oceny, w teście **A–D** lub **1–4** wybiera odpowiedź, **Enter** przechodzi dalej, **←/→** przełącza zadania maturalne, **Esc** kończy sesję.

### Jak działają powtórki (system Leitnera)

| Pudełko | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Następna powtórka za | 1 dzień | 2 dni | 4 dni | 8 dni | 16 dni | 32 dni |

- **Nie wiem** — fiszka wraca do pudełka 1 i pojawia się jeszcze w tej samej sesji.
- **Trudne** — fiszka nie awansuje (z pudełka 3 lub wyższego spada o jedno) i wraca jutro.
- **Umiem** — fiszka przechodzi do wyższego pudełka.

Fiszka jest **opanowana** od pudełka 4. Nowe fiszki dochodzą w dziennym limicie na przedmiot (domyślnie 20 — zmiana w Ustawieniach), powtórki są bez limitu. Parametry: `js/srs.js`.

## Struktura projektu

```
index.html, manifest.webmanifest, sw.js    strona, PWA, działanie offline
css/style.css                              wygląd
js/app.js  js/srs.js  js/store.js  js/data.js
ikony/                                     ikony aplikacji
przedmioty/
  index.json                               lista przedmiotów (budowana automatycznie)
  wos.json                                 przedmiot WOS — lista działów i arkuszy
  wos/<dział>.json                         działy z poddziałami, fiszkami i pytaniami
  wos/arkusze/<arkusz>.json                zadania maturalne
narzedzia/zbuduj-indeks.mjs                sprawdza treści i buduje przedmioty/index.json
narzedzia/dopisz-z-tekstu.py               szybkie dopisywanie fiszek z pliku tekstowego
.github/workflows/pages.yml                automatyczne wdrożenie na GitHub Pages
```

## Jak dodać nowy przedmiot

1. Utwórz plik `przedmioty/<id>.json`, np. `przedmioty/historia.json`. Najprostsza wersja — wszystko w jednym pliku:

```json
{
  "id": "historia",
  "nazwa": "Historia",
  "skrot": "HIS",
  "ikona": "🏛️",
  "opis": "Matura rozszerzona.",
  "dzialy": [
    {
      "id": "polska-piastow",
      "nazwa": "Polska Piastów",
      "poddzialy": [
        {
          "id": "his-mieszko",
          "nazwa": "Państwo Mieszka I",
          "fiszki": [
            { "id": "f001", "przod": "W którym roku odbył się chrzest Mieszka I?", "tyl": "W 966 roku.", "zrodlo": "Podręcznik, rozdz. 1" }
          ],
          "pytania": [
            {
              "id": "p01",
              "pytanie": "Kto został pierwszym królem Polski?",
              "odpowiedzi": ["Mieszko I", "Bolesław Chrobry", "Mieszko II", "Kazimierz Odnowiciel"],
              "poprawna": "B",
              "wyjasnienie": "Bolesław Chrobry koronował się w 1025 roku.",
              "zrodlo": "Podręcznik, rozdz. 2"
            }
          ]
        }
      ]
    }
  ]
}
```

2. Zapisz zmiany w gałęzi `main` (commit + push). Przy wdrożeniu przez GitHub Actions lista `przedmioty/index.json` zbuduje się **sama**.

Przy dużym przedmiocie każdy dział warto trzymać w osobnym pliku (telefon ładuje mniejsze pliki szybciej). W pliku przedmiotu wpisujesz wtedy tylko odnośnik:

```json
"dzialy": [
  { "id": "polska-piastow", "plik": "historia/polska-piastow.json" }
]
```

a plik `przedmioty/historia/polska-piastow.json` zawiera `id`, `nazwa`, `opis` i `poddzialy`. Tak zbudowany jest WOS.

> Bez GitHub Actions (opcja „Deploy from a branch”) albo lokalnie zaktualizuj listę przedmiotów poleceniem `node narzedzia/zbuduj-indeks.mjs`.

### Jak dodać nowy dział lub poddział

- **Dział** — dopisz obiekt do listy `"dzialy"` w pliku przedmiotu (inline albo z polem `"plik"`).
- **Poddział** — dopisz obiekt do listy `"poddzialy"` działu.
- Dział może też mieć `fiszki` i `pytania` bezpośrednio, bez poddziałów — aplikacja potraktuje go jak jeden poddział.

### Zasady pól

| Element | Pola |
|---|---|
| Przedmiot | `id`, `nazwa`, `skrot`, `ikona`, `opis`, `dzialy`, `arkusze` (opcjonalnie) |
| Dział | `id`, `nazwa`, `opis`, `poddzialy` albo `fiszki`/`pytania`, albo `plik` |
| Poddział | `id` (unikalne w całym przedmiocie), `nazwa`, `opis`, `fiszki`, `pytania` |
| Fiszka | `id`, `przod`, `tyl`, `zrodlo` |
| Pytanie ABCD | `id`, `pytanie`, `odpowiedzi` (dokładnie 4), `poprawna` (`"A"`–`"D"`), `wyjasnienie`, `zrodlo` |

`id` działów i poddziałów: małe litery a–z, cyfry i myślniki. **Nie zmieniaj `id`** po publikacji — po nich aplikacja pamięta postępy. Treść fiszek możesz poprawiać dowolnie.

### Szybkie dopisywanie fiszek z pliku tekstowego

Zamiast pisać JSON ręcznie, możesz przygotować plik tekstowy:

```
# prawo | Prawo w Rzeczypospolitej Polskiej | opis działu
## prawo-karne | Prawo karne i wykroczeń | opis poddziału
Q Od ilu lat odpowiada się karnie? :: Co do zasady od 17 lat. :: KK 10
T zbrodnia :: Czyn zagrożony karą co najmniej 3 lat pozbawienia wolności. :: KK 7 § 2
P Monteskiusz :: Autor „O duchu praw”, trójpodział władzy. :: PP ZR V
? Zbrodnią jest czyn zagrożony karą od: :: *3 lat :: 1 roku :: 5 lat :: 8 lat :: Wyjaśnienie. :: KK 7 § 2
```

- `Q` — zwykła fiszka; `T` — pojęcie (powstają 2 fiszki: pojęcie → definicja i definicja → pojęcie); `P` — postać (2 fiszki); `?` — pytanie ABCD (poprawna odpowiedź z `*`).
- Źródła można skracać: `K 104` → „Konstytucja RP, art. 104”, `KC`, `KK`, `KP`, `KRO`, `KPA`, `KPK`, `KPC`, `KW`, `TUE`, `TFUE`, `KNZ`, `EKPC`, `PP ZR VIII` (podstawa programowa) i inne (lista w skrypcie).

```bash
python3 narzedzia/dopisz-z-tekstu.py wos moje-fiszki.txt
```

Skrypt tylko **dopisuje** — niczego nie usuwa, a fiszki o tym samym przodzie aktualizuje (zachowując `id` i postępy).

### Zadania maturalne (arkusze)

W pliku przedmiotu: `"arkusze": [{ "id": "2023-maj", "plik": "wos/arkusze/2023-maj.json" }]`. Arkusz składa się z wiązek (`wiazki`): `nr`, `tytul`, `material`, `uwaga` oraz `zadania` z polami `nr`, `punkty`, `polecenie`, `odpowiedz`, `zasady`, `dzialy` (lista `id` działów).

### Sprawdzanie treści

```bash
node narzedzia/zbuduj-indeks.mjs
```

Skrypt wykrywa błędy (zły JSON, brak pól, powtórzone `id`, brak 4 odpowiedzi, zła litera w `poprawna`, brak pliku działu) i ostrzega o brakującym `zrodlo` lub `wyjasnienie`. To samo sprawdzenie wykonuje się przy każdym wdrożeniu — jeśli treść ma błąd, nowa wersja się nie opublikuje.

## Jak włączyć GitHub Pages

1. Repozytorium na GitHubie → **Settings** → **Pages**.
2. W sekcji **Build and deployment** ustaw **Source: GitHub Actions**.
3. Zrób push do `main` (albo **Actions** → „Wdrożenie na GitHub Pages” → **Run workflow**).
4. Po minucie–dwóch strona będzie pod adresem `https://<twoja-nazwa>.github.io/kolumb/`.

Każdy push do `main` publikuje nową wersję; zainstalowana aplikacja pokaże komunikat „Dostępna nowa wersja”.

## Instalacja na telefonie i tablecie

- **Android (Chrome):** przycisk „Zainstaluj” w aplikacji albo menu ⋮ → **Zainstaluj aplikację**.
- **iPhone / iPad (Safari):** **Udostępnij** → **Do ekranu początkowego**.

Po pierwszym otwarciu wszystkie treści są zapisywane w pamięci urządzenia — nauka działa w trybie samolotowym.

## Uruchomienie lokalne

```bash
python3 -m http.server 8000
```

Następnie otwórz `http://localhost:8000`.

## Postępy i prywatność

Postępy są zapisane wyłącznie w przeglądarce na danym urządzeniu — nic nie jest wysyłane na serwer. W **Ustawieniach** można pobrać kopię i wczytać ją na innym urządzeniu.

## Źródła zadań

Zadania maturalne pochodzą z arkuszy egzaminacyjnych i zasad oceniania Centralnej Komisji Egzaminacyjnej (cke.gov.pl). Materiały graficzne (rysunki, wykresy, mapy) nie są w aplikacji odtwarzane — przy takich zadaniach jest odpowiednia uwaga i odesłanie do oryginalnego arkusza.
