# 18. Audyt merytoryczny kursu chemii

Audyt niezależny, wykonany na gałęzi `claude/audyt-chemii`. Pliki z treściami nie były zmieniane — raport zawiera wyłącznie uwagi i propozycje poprawek.

**Zakres i metoda.** Treści wczytano tak, jak robi to `narzedzia/zbuduj-chemie.py` (runpy), i przeczytano w całości. Każde równanie zapisane w treściach przepuszczono przez automatyczny bilans atomów i ładunków (parser wzorów z indeksami i ładunkami Unicode); wszystkie zgłoszone niezgodności sprawdzono ręcznie. Liczby w pytaniach i zadaniach przeliczono ręcznie. Kryterium „poza podstawą” to wymagania egzaminacyjne z chemii (zakres rozszerzony) obowiązujące od 2025 r.

**Stan prac:** w toku — przejrzane `tresci1–53.py`.


## Podsumowanie liczbowe

| Waga | Liczba |
|---|---|
| krytyczny | 1 |
| średni | 2 |
| drobny | 14 |
| **razem** | **17** |


| Grupa plików | Liczba uwag |
|---|---|
| tresci | 17 |


## Lista uwag

Kolejność: najpierw krytyczne, potem średnie i drobne. Kolumna „miejsce” podaje klucz działu i numer fiszki (F) lub pytania (Q) liczony od 0 w obrębie działu w danym pliku; dla banku — tytuł wiązki i numer zadania; dla podcastu — id pytania lub nagłówek sekcji.

| # | Plik | Miejsce / id | Problem | Dowód / obliczenie | Proponowana poprawka | Waga |
|---|---|---|---|---|---|---|
| 1 | `narzedzia/chemia/tresci26.py` | c-alkany, pytanie Q0 (monochlorowanie 2-metylopropanu) | Zły klucz: dla chlorowania produktem głównym jest 1-chloro-2-metylopropan, nie 2-chloro-2-metylopropan. | 2-metylopropan ma 9 atomów H I-rzędowych i 1 atom H III-rzędowy. Przy względnej reaktywności Cl• ok. 1 : 5 (I : III) udział produktów ≈ 9 : 5 → ok. 64% 1-chloro-2-metylopropanu i 36% 2-chloro-2-metylopropanu. Sam kurs (tresci11, c-alkany F4) pisze, że „chlor jest mało selektywny”, a selektywny jest brom. | Zmienić reagent na brom: „Produktem głównym monobromowania 2-metylopropanu (Br₂, hν) jest: *2-bromo-2-metylopropan”. Usunąć asekuracyjny dopisek z wyjaśnienia. | krytyczny |
| 2 | `narzedzia/chemia/tresci12.py` | c-ph, fiszka F10 (wskaźnik uniwersalny) vs tresci1.py c-doswiadczenia F11 | Niespójność w kursie: barwa wskaźnika uniwersalnego w roztworze obojętnym. | tresci1 F11: „obojętny — żółty (żółtopomarańczowy)”; tresci12 F10: „żółty → zielony (obojętny)”. Uczeń dostaje dwie różne odpowiedzi na to samo pytanie. | Ujednolicić, np. „papierek uniwersalny: obojętny — żółty/żółtozielony (zależnie od producenta); roztwór wskaźnika uniwersalnego: zielony” albo trzymać się jednej konwencji z podręcznika. | średni |
| 3 | `narzedzia/chemia/tresci16.py` | c-metale, pytanie Q1: „Z roztworu CuSO₄ miedź wypiera:” | Niejednoznaczne sformułowanie — przy szyku przestawnym zdanie czyta się „miedź wypiera żelazo”, czyli odwrotnie do prawdy. | „miedź” i „żelazo” mają tę samą formę w mianowniku i bierniku, więc nie wiadomo, który metal jest podmiotem. Kluczowana odpowiedź (żelazo) jest poprawna tylko przy lekturze „miedź wypiera [je] żelazo”. | „Który metal wypiera miedź z roztworu CuSO₄?” — odp. żelazo. | średni |
| 4 | `narzedzia/chemia/tresci10.py` | c-aminokwasy, fiszka F10 (wysalanie) | Nieścisłość: (NH₄)₂SO₄ podano jako przykład „soli metali lekkich”. | Siarczan(VI) amonu nie jest solą metalu. | „po dodaniu stężonych roztworów soli metali lekkich lub soli amonowych (np. NaCl, (NH₄)₂SO₄)”. | drobny |
| 5 | `narzedzia/chemia/tresci11.py` | c-chemia-zycia, fiszka F7 (wysalanie) | To samo co w tresci10: (NH₄)₂SO₄ jako przykład soli „lekkich metali”. | Jon amonowy nie jest metalem. | „solami metali lekkich lub amonowymi (np. NaCl, (NH₄)₂SO₄)”. | drobny |
| 6 | `narzedzia/chemia/tresci15.py` | c-karbonylowe F2–F3 (kondensacja aldolowa, reakcja Cannizzaro), c-aminy F4 (sole diazoniowe), c-aminokwasy F0–F1 (HNO₂/van Slyke, ninhydryna), c-alkeny F3, F5 (katalizator Lindlara, acetylenki), c-areny F1 (alkilowanie Friedla–Craftsa); tresci16 c-karbonylowe Q1 (próba jodoformowa) | Treści wykraczające poza wymagania egzaminacyjne 2027 (podstawa programowa, zakres rozszerzony). | Podstawa (XIII–XIX) nie wymaga tych reakcji; mogą pojawić się tylko jako informacja wprowadzająca w zadaniu. Fiszki i pytania ABCD sugerują, że trzeba je znać. | Oznaczyć jako „poszerzenie (poza podstawą)” albo przenieść do materiałów dodatkowych; nie umieszczać w puli pytań sprawdzających. | drobny |
| 7 | `narzedzia/chemia/tresci17.py` | c-energetyka, fiszka F1 (proces samorzutny) | Błędna definicja: „zachodzi bez dostarczania energii z zewnątrz”. | Samorzutne procesy endotermiczne (np. rozpuszczanie NH₄NO₃, podane w kursie jako przykład endotermiczny) pobierają ciepło z otoczenia. Samorzutność oznacza przebieg bez wykonywania pracy z zewnątrz (dla matury: „zachodzi sam, bez ingerencji z zewnątrz”), a nie brak wymiany energii. | „Proces samorzutny — przebiega sam, bez stałej ingerencji z zewnątrz (może pobierać ciepło z otoczenia, np. rozpuszczanie NH₄NO₃)”. | drobny |
| 8 | `narzedzia/chemia/tresci17.py` | c-izomeria F5 (konfiguracja R/S), c-alkany F6 (synteza Wurtza), c-rownowaga F1 (Kp a Kc) | Treści poza wymaganiami egzaminacyjnymi 2027. | Podstawa wymaga konfiguracji D/L (projekcja Fischera), nie R/S; synteza Wurtza i Kp nie występują w wymaganiach. | Oznaczyć jako poszerzenie albo usunąć z fiszek obowiązkowych. | drobny |
| 9 | `narzedzia/chemia/tresci2.py` | c-atom, fiszka F11 (masa atomowa chloru) | Wynik obliczenia nie zgadza się z podanym działaniem. | (35·75,8 + 37·24,2)/100 = (2653 + 895,4)/100 = 35,48 u, a nie 35,45 u (35,45 wychodzi dopiero z dokładnych mas izotopów 34,97 i 36,97 u). | Zapisać „≈ 35,48 u (przy dokładnych masach izotopów 34,97 i 36,97 u: 35,45 u)” albo podstawić dokładne masy. | drobny |
| 10 | `narzedzia/chemia/tresci21.py` | c-izomeria, pytanie Q1 („Izomerem propan-1-olu NIE jest”) | Dwa dystraktory to ten sam związek. | „eter etylowo-metylowy” i „metoksyetan” to dwie nazwy CH₃–O–C₂H₅. Uczeń, który to zauważy, odrzuca obie bez wiedzy o izomerii — pytanie ma realnie 3 opcje. | Zastąpić jeden z nich innym izomerem C₃H₈O, np. „propan-2-ol” zostaje, a „metoksyetan” → „2-metylo... (niemożliwe)”; prościej: „cyklopropanol” jako dodatkowy NIE-izomer nie pasuje — dać np. „eter metylowo-etylowy” i „propan-2-ol” oraz „1-metoksyetan” zamienić na „propan-1,2-diol” (C₃H₈O₂, też nie-izomer) i przekluczyć na dwie poprawne? Najprościej: zamienić „metoksyetan” na „propan-2-ol” w innym brzmieniu nie wolno — zalecenie: zastąpić „metoksyetan” odpowiedzią „żaden z wymienionych”. | drobny |
| 11 | `narzedzia/chemia/tresci22.py` | c-sole, fiszka F4 (rozpływanie się soli) | NaOH podany jako przykład soli. | NaOH jest wodorotlenkiem, nie solą. | „Rozpływanie się substancji (np. CaCl₂, a także NaOH)”. | drobny |
| 12 | `narzedzia/chemia/tresci26.py` | c-atom Q1 vs tresci2.py c-atom F11 | Niespójne dane o składzie izotopowym chloru. | tresci2: 75,8% ³⁵Cl / 24,2% ³⁷Cl (dane rzeczywiste); tresci26: 22,5% ³⁷Cl (wynik z całkowitych liczb masowych 35 i 37). Uczeń dostaje dwie różne „zawartości ³⁷Cl”. | W tresci26 dopisać „przyjmij masy izotopów 35 u i 37 u (wynik przybliżony)” albo podać masy 34,97 u i 36,97 u (wtedy wychodzi ok. 24%). | drobny |
| 13 | `narzedzia/chemia/tresci26.py` | c-jonowe Q1 (wyjaśnienie); także tresci59.py c-jonowe Q1 | Mylący termin: „jony obojętne” zamiast „jony widzowie”. | Na⁺, Cl⁻ (K⁺, NO₃⁻) mają ładunek — nie są obojętne; nie biorą udziału w reakcji. | „Jony Na⁺ i Cl⁻ to jony widzowie (nie biorą udziału w reakcji)”. | drobny |
| 14 | `narzedzia/chemia/tresci28.py` | c-alkeny Q3 (ozonoliza but-2-enu) | Treść poza wymaganiami egzaminacyjnymi. | Ozonoliza nie występuje w podstawie programowej (XIII); bez informacji wprowadzającej uczeń nie ma podstaw do odpowiedzi. | Usunąć z puli ABCD albo poprzedzić pytanie krótką informacją o przebiegu ozonolizy. | drobny |
| 15 | `narzedzia/chemia/tresci3.py` | c-wiazania, fiszka F5 | Błąd językowy: „obie elektrony”. | Elektron jest rodzaju męskiego. | „oba elektrony wspólnej pary”. | drobny |
| 16 | `narzedzia/chemia/tresci30.py` | c-ogniwa F3 (potencjał standardowy) | Nieprecyzyjna definicja: „SEM ogniwa złożonego z danego półogniwa i elektrody wodorowej”. | SEM jest zawsze dodatnia, a potencjały standardowe bywają ujemne (Zn: −0,76 V). Z tej definicji uczeń nie wyprowadzi znaku E°. | „Potencjał półogniwa w warunkach standardowych względem standardowej elektrody wodorowej (ze znakiem: ujemny, gdy półogniwo jest anodą w ogniwie z elektrodą wodorową)”. | drobny |
| 17 | `narzedzia/chemia/tresci46.py` | c-energetyka F3 („Warunki standardowe: 25°C i 1013 hPa”) vs tresci23.py c-energetyka F5 („Stan standardowy — 1000 hPa”) | Niespójna wartość ciśnienia standardowego w kursie. | Jedna fiszka podaje 1013 hPa, druga 1000 hPa. Obie wartości funkcjonują (dawna konwencja 1 atm, obecna IUPAC 1 bar), ale uczeń powinien dostać jedną, zgodną z kartą CKE, z ewentualnym przypisem. | Ujednolicić do wartości z karty „Wybrane wzory i stałe fizykochemiczne” i dodać uwagę o drugiej konwencji. | drobny |
