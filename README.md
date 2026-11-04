# 🧭 Kolumb — nauka do matury

Kolumb to aplikacja webowa do nauki do matury: **fiszki z powtórkami rozłożonymi w czasie** i **testy ABCD**.
Działa w przeglądarce na telefonie, tablecie i komputerze, można ją dodać do ekranu głównego i uczyć się **bez internetu**.

- czysty HTML, CSS i JavaScript — bez backendu, bez kosztów utrzymania,
- hosting na GitHub Pages,
- postępy zapisywane w przeglądarce (`localStorage`),
- treści w plikach JSON — nowy przedmiot to nowy plik.

## Funkcje

| Ekran | Co robi |
|---|---|
| **Nauka** (ekran główny) | Przedmioty i działy, pasek opanowania każdego działu, licznik „dziś do powtórki”, seria dni nauki. |
| **Fiszki** | Pytanie z przodu, odpowiedź po dotknięciu. Oceny **Nie wiem / Trudne / Umiem**. Powtórki według systemu Leitnera (opis niżej). Tryb „trening swobodny”, gdy na dziś wszystko powtórzone. |
| **Test** | 10 losowych pytań ABCD z działu (kolejność odpowiedzi też losowa), natychmiastowa informacja o poprawności z wyjaśnieniem i źródłem, na końcu wynik procentowy i lista błędów. |
| **Przegląd treści** | Wszystkie fiszki i pytania działu razem ze źródłami — do sprawdzania. |
| **Statystyki** | Opanowane fiszki, seria dni nauki (obecna i najdłuższa), ostatnie 14 dni, opanowanie działów, wyniki ostatnich testów. |
| **Ustawienia** | Motyw jasny / ciemny / systemowy, instalacja aplikacji, kopia postępów (pobierz / wczytaj), zerowanie postępów. |
| **Zgłoś błąd** | Przy każdej fiszce i każdym pytaniu. Otwiera e-mail do `roc7et@gmail.com` z pełną treścią fiszki lub pytania. |

Skróty klawiszowe (tablet z klawiaturą, komputer): **spacja** odwraca fiszkę, **1 / 2 / 3** to oceny, w teście **A–D** lub **1–4** wybiera odpowiedź, **Enter** przechodzi dalej, **Esc** kończy sesję.

### Jak działają powtórki (system Leitnera)

Każda fiszka leży w jednym z 6 „pudełek”. Im wyższe pudełko, tym dłuższa przerwa do następnej powtórki:

| Pudełko | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Następna powtórka za | 1 dzień | 2 dni | 4 dni | 8 dni | 16 dni | 32 dni |

- **Nie wiem** — fiszka wraca do pudełka 1 i pojawia się ponownie jeszcze w tej samej sesji (po kilku innych fiszkach).
- **Trudne** — fiszka nie awansuje (z pudełka 3 lub wyższego spada o jedno) i wraca jutro.
- **Umiem** — fiszka przechodzi do wyższego pudełka, więc wraca coraz rzadziej.

Fiszka jest **opanowana** od pudełka 4. Codziennie dochodzi maksymalnie **10 nowych fiszek** na dział, żeby nie zasypać się powtórkami.
Parametry można zmienić w pliku `js/srs.js` (`INTERVALS`, `MASTERED_BOX`, `NEW_PER_DAY`).

## Struktura projektu

```
index.html              strona aplikacji
manifest.webmanifest    manifest PWA (nazwa, ikony, kolory)
sw.js                   service worker — działanie offline
css/style.css           wygląd (tryb jasny i ciemny)
js/app.js               ekrany aplikacji
js/srs.js               powtórki rozłożone w czasie
js/store.js             zapis postępów w localStorage
js/data.js              wczytywanie plików z treściami
ikony/                  ikony aplikacji
przedmioty/             TREŚCI: jeden plik JSON = jeden przedmiot
  index.json            lista plików przedmiotów (budowana automatycznie)
  wos.json              Wiedza o społeczeństwie
narzedzia/zbuduj-indeks.mjs   sprawdza treści i buduje przedmioty/index.json
.github/workflows/pages.yml   automatyczne wdrożenie na GitHub Pages
```

## Jak dodać nowy przedmiot

1. Utwórz w katalogu `przedmioty/` nowy plik, np. `przedmioty/historia.json`.
2. Wklej do niego szablon i uzupełnij treści:

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
      "opis": "Od chrztu Polski do 1370 roku.",
      "fiszki": [
        {
          "id": "f01",
          "przod": "W którym roku odbył się chrzest Mieszka I?",
          "tyl": "W 966 roku.",
          "zrodlo": "Podręcznik, rozdz. 1"
        }
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
```

3. Zapisz zmiany w gałęzi `main` (commit + push). Przy wdrożeniu przez GitHub Actions lista przedmiotów `przedmioty/index.json` zbuduje się **sama** — nie trzeba niczego więcej edytować.

> Jeśli wdrażasz stronę bez GitHub Actions (opcja „Deploy from a branch”) albo testujesz lokalnie, zaktualizuj listę jednym poleceniem:
> ```bash
> node narzedzia/zbuduj-indeks.mjs
> ```
> albo dopisz ręcznie nazwę pliku do `przedmioty/index.json`, np. `{ "przedmioty": ["historia.json", "wos.json"] }`.

### Pola w pliku przedmiotu

| Pole | Wymagane | Opis |
|---|---|---|
| `id` | tak | Krótki identyfikator przedmiotu (małe litery, bez spacji). Postępy są do niego przypisane — **nie zmieniaj go później**. |
| `nazwa` | tak | Pełna nazwa przedmiotu. |
| `skrot` | nie | Krótka nazwa (np. w statystykach i temacie zgłoszenia błędu). |
| `ikona` | nie | Emoji wyświetlane przy przedmiocie. |
| `opis` | nie | Jedno zdanie pod nazwą. |
| `dzialy` | tak | Lista działów. |

Fiszka: `id`, `przod` (pytanie), `tyl` (odpowiedź), `zrodlo` (np. numer artykułu, strona podręcznika).

Pytanie testowe: `id`, `pytanie`, `odpowiedzi` (dokładnie 4), `poprawna` (litera `"A"`–`"D"` według kolejności w pliku — w aplikacji odpowiedzi i tak są tasowane), `wyjasnienie`, `zrodlo`.

**Ważne:** `id` fiszek i pytań musi być unikalne w obrębie działu i nie powinno się zmieniać — po nim aplikacja pamięta postępy. Treść fiszki możesz poprawiać dowolnie, postęp zostanie zachowany.

## Jak dodać nowy dział

Otwórz plik przedmiotu (np. `przedmioty/wos.json`) i dopisz nowy obiekt do listy `"dzialy"` — po przecinku za poprzednim działem:

```json
"dzialy": [
  { "id": "konstytucja-zasady-organy", "nazwa": "...", "fiszki": [ ... ], "pytania": [ ... ] },
  {
    "id": "prawa-czlowieka",
    "nazwa": "Prawa i wolności człowieka",
    "opis": "Rozdział II Konstytucji RP.",
    "fiszki": [ ... ],
    "pytania": [ ... ]
  }
]
```

`id` działu: małe litery a–z, cyfry i myślniki (bez polskich znaków i spacji). Test losuje 10 pytań — jeśli dział ma ich mniej, test obejmie wszystkie.

### Sprawdzanie treści

Przed wysłaniem zmian warto uruchomić:

```bash
node narzedzia/zbuduj-indeks.mjs
```

Skrypt wykrywa błędy (zły JSON, brak pól, powtórzone `id`, brak 4 odpowiedzi, zła litera w `poprawna`) i ostrzega o brakującym `zrodlo` lub `wyjasnienie`. To samo sprawdzenie wykonuje się przy każdym wdrożeniu — jeśli treść ma błąd, nowa wersja się nie opublikuje, a w zakładce **Actions** zobaczysz, co poprawić.

## Jak włączyć GitHub Pages

1. Wejdź w repozytorium na GitHubie → **Settings** → **Pages**.
2. W sekcji **Build and deployment** ustaw **Source: GitHub Actions**.
3. Zrób dowolny push do gałęzi `main` (albo w zakładce **Actions** wybierz „Wdrożenie na GitHub Pages” → **Run workflow**).
4. Po minucie–dwóch strona będzie dostępna pod adresem `https://<twoja-nazwa>.github.io/kolumb/` (adres pokazuje się też w **Settings → Pages**).

Każdy kolejny push do `main` automatycznie publikuje nową wersję. Zainstalowana aplikacja pobierze aktualizację przy następnym uruchomieniu i pokaże komunikat „Dostępna nowa wersja”.

**Alternatywa bez Actions:** Settings → Pages → Source: **Deploy from a branch** → gałąź `main`, katalog `/ (root)`. Wtedy pamiętaj o aktualizacji `przedmioty/index.json` przy dodawaniu przedmiotu (patrz wyżej).

## Instalacja na telefonie i tablecie

- **Android (Chrome):** otwórz stronę → przycisk „Zainstaluj” na ekranie głównym aplikacji albo menu ⋮ → **Zainstaluj aplikację**.
- **iPhone / iPad (Safari):** przycisk **Udostępnij** → **Do ekranu początkowego**.

Po pierwszym otwarciu wszystkie treści są zapisywane w pamięci urządzenia, więc nauka działa także w trybie samolotowym.

## Uruchomienie lokalne

Aplikacja wczytuje pliki JSON, więc potrzebuje prostego serwera (otwarcie `index.html` bezpośrednio z dysku nie zadziała):

```bash
python3 -m http.server 8000
```

Następnie otwórz `http://localhost:8000`.

## Postępy i prywatność

Postępy (stan fiszek, seria dni, wyniki testów) są zapisane wyłącznie w przeglądarce na danym urządzeniu — nic nie jest wysyłane na serwer. Wyczyszczenie danych przeglądarki usuwa postępy, dlatego w **Ustawieniach** można pobrać kopię i wczytać ją na innym urządzeniu.

## Treści na start

**Wiedza o społeczeństwie → Konstytucja RP — zasady ustroju i organy władzy**: 40 fiszek i 20 pytań testowych na poziomie matury rozszerzonej. Każda fiszka i każde pytanie ma pole `zrodlo` z numerem artykułu Konstytucji RP z 2 kwietnia 1997 r. Błędy można zgłaszać przyciskiem „Zgłoś błąd”.
