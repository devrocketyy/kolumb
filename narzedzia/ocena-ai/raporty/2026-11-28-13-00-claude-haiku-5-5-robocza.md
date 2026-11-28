# Test oceny AI — claude-haiku-5-5 (effort low), część robocza

2026-11-28T13:00:54.197Z · tokeny 169567/27746 · koszt 0.11 zł

| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| **ogółem** | 97 | 93.8% | 0.0% | 2.1% | 4.1% | 0 |

Progi: zgodność ≥ 90%, poważne ≤ 2%, trafność „czego zabrakło” ≥ 85% (przegląd ręczny poniżej).

### Przedmioty
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| biologia | 28 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| chemia | 17 | 82.4% | 0.0% | 5.9% | 11.8% | 0 |
| geografia | 17 | 94.1% | 0.0% | 0.0% | 5.9% | 0 |
| historia | 17 | 88.2% | 0.0% | 5.9% | 5.9% | 0 |
| wos | 18 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |

### Typy zadań
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| oblicz | 10 | 80.0% | 0.0% | 10.0% | 10.0% | 0 |
| okresl | 10 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| podaj | 29 | 93.1% | 0.0% | 3.4% | 3.4% | 0 |
| rozstrzygnij | 18 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| uzasadnij | 11 | 81.8% | 0.0% | 0.0% | 18.2% | 0 |
| wyjasnij | 14 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| wykaz | 5 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |

### Punktacja
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| 1 | 65 | 98.5% | 0.0% | 0.0% | 1.5% | 0 |
| 2 | 32 | 84.4% | 0.0% | 6.3% | 9.4% | 0 |

## Rozbieżności
- **chemia/2026-maj/24#1** wzór 1/1, AI 0/1 — „Projekt 2, bo najpierw wprowadzamy grupę nitrową, a ona kieruje następny podstawnik (chlor) w położenie meta.”
  - AI: Wskazujesz właściwy projekt 2 i poprawnie mówisz, że grupa nitrowa kieruje kolejny podstawnik w położenie meta. Błąd polega na tym, że podstawnikiem kierowanym do położenia meta jest tu chlor, a chlor kieruje w położenie orto i para, więc uzasadnienie jest niepoprawne merytorycznie.
- **chemia/2026-czerwiec/11.2#2** wzór 1/2, AI 0/2 — „Roztwór nasycony. Cp = 70 / 220 · 100% = 31,8%.”
  - AI: Rozstrzygnięcie 'nasycony' jest poprawne, ale obliczenie Cp jest błędne: uczył wziął całą masę CuSO₄ (70 g) zamiast masy substancji rozpuszczonej (20 g) i masę roztworu 220 g zamiast 170 g. Przy nasyconym roztworze z osadem w masie roztworu liczy się tylko rozpuszczona część, więc metoda i wynik są niepoprawne.
- **chemia/2022-grudzien/8#1** wzór 0/2, AI 1/2 — „Około 38% glinu, bo tyle wychodzi z proporcji.”
  - AI: Podajesz poprawny wynik (ok. 38% Al), ale nie pokazujesz metody: brak bilansu moli H2 z Mg i Al oraz zapisu równań i zależności mas. Bez tego nie można przyznać pełnej punktacji.
- **geografia/2024-grudzien/10#3** wzór 1/2, AI 0/2 — „Wiatr wieje od niżu równikowego do wyżów zwrotnikowych, a odchyla go ruch obrotowy Ziemi.”
  - AI: Uczeń odwrócił kierunek wiatru: podał, że wieje od niżu równikowego do wyżów zwrotnikowych, podczas gdy klucz wskazuje odwrotnie (od wyżów zwrotnikowych do niżu równikowego). Element astronomiczny (ruch obrotowy Ziemi odchylający wiatr) jest wskazany poprawnie, ale ogólnie, bez podania kierunku odchylenia na półkulach, więc nie stanowi pełnego elementu.
- **historia/2025-maj/4#3** wzór 0/2, AI 1/2 — „A – dominikanie, B – cystersi, C – jezuici.”
  - AI: Poprawnie podano tylko nazwę dla C (jezuici). Dla A uczeń podał dominikanów, a dla B cystersów, zamiast franciszkanów i benedyktynów, więc przyznano 1 pkt za jedną poprawną nazwę zgodnie z zasadami.
- **historia/2026-czerwiec/22#2** wzór 1/2, AI 0/2 — „Wtedy wrócił Piłsudski i Polska odzyskała niepodległość.”
  - AI: Odpowiedź zawiera jedno zdanie, w którym pojawia się powrót Piłsudskiego, ale nie wskazuje on na konkretny fragment ani nie łączy go z datą listopadową. Brak jest też drugiego argumentu, a odniesienie do odzyskania niepodległości jest ogólnikiem bez wiązania z oboma fragmentami.

## „Czego zabrakło” — do przeglądu
- **biologia/2023-maj/1.3#2** wzór: przekształcenie pirogronianu w acetylo-CoA; acetylo-CoA jako substrat cyklu Krebsa
  - AI: Przekształcenie pirogronianu (produktu glikolizy) w acetylo-CoA; Wskazanie, że acetylo-CoA jest substratem cyklu Krebsa
- **biologia/2023-maj/1.3#3** wzór: błędna lokalizacja cyklu Krebsa (macierz mitochondrium)
  - AI: Informacja, że kompleks dehydrogenazy pirogronianowej działa w macierzy mitochondrialnej, a nie w cytozolu.; Poprawne miejsce cyklu Krebsa: macierz mitochondrialna, a nie jądro komórkowe.
- **biologia/2023-maj/4.2#2** wzór: wyrównanie materiału / wykluczenie wpływu innych czynników
  - AI: Wyjaśnienia, że rośliny miały być możliwie podobne na starcie; Wyjaśnienia, że dzięki temu wyeliminowano wpływ innych czynników na wynik doświadczenia
- **biologia/2023-maj/5.1#2** wzór: C – regeneracja RuBP
  - AI: C – poprawnie: regeneracja RuBP (nazwa podana przez ucznia, fosforylacja, jest błędna)
- **biologia/2023-maj/5.1#3** wzór: A – karboksylacja; B – redukcja
  - AI: A – karboksylacja (wiązanie CO₂ z RuBP), zamiast glikolizy; B – redukcja (PGA do aldehydu 3-fosfoglicerynowego), zamiast fotolizy wody
- **biologia/2024-maj/2#2** wzór: funkcja rybonukleazy (rozkład RNA z hybrydy)
  - AI: Funkcja obszaru o aktywności rybonukleazy: rozkład (hydroliza) RNA w hybrydzie RNA-DNA, dzięki czemu może powstać druga nić DNA.
- **biologia/2024-maj/2#3** wzór: rybonukleaza rozkłada RNA, a nie syntetyzuje
  - AI: funkcja rybonukleazy: hydroliza/rozkład RNA z hybrydy RNA-DNA; błędne podanie, że rybonukleaza syntetyzuje RNA wirusa
- **biologia/2024-maj/2#4** wzór: funkcja polimerazy; funkcja rybonukleazy
  - AI: Polimeraza (odwrotnie transkryptaza) syntetyzuje DNA na matrycy RNA oraz drugą nić DNA na matrycy DNA.; Rybonukleaza hydrolizuje (rozkłada) RNA w hybrydzie RNA-DNA, aby umożliwić powstanie drugiej nici DNA.
- **biologia/2024-maj/17.2#3** wzór: funkcja ramienia akceptorowego; funkcja antykodonu
  - AI: Ramię akceptorowe przyłącza aminokwas (koniec 3′).; Antykodon komplementarnie wiąże się z kodonem mRNA, zapewniając wstawienie właściwego aminokwasu.
- **biologia/2024-maj/17.2#2** wzór: funkcja antykodonu
  - AI: funkcja antykodonu: komplementarne wiązanie się z kodonem mRNA, zapewniające wstawienie właściwego aminokwasu
- **biologia/2025-maj/1.2#2** wzór: struktura III-rzędowa – jeden łańcuch
  - AI: Poprawne rozstrzygnięcie: struktura III-rzędowa; Poprawne uzasadnienie: rybonukleaza jest jednym łańcuchem polipeptydowym, więc mostki tworzą się w obrębie jednego łańcucha
- **biologia/2025-maj/1.2#3** wzór: uzasadnienie (jeden łańcuch polipeptydowy)
  - AI: uzasadnienie, że rybonukleaza składa się z jednego łańcucha polipeptydowego; wyjaśnienie, że mostki powstają wewnątrz tego samego łańcucha, a struktura IV-rzędowa wymagałaby kilku łańcuchów
- **biologia/2025-maj/3.2#3** wzór: strefa wydłużania
  - AI: Wskazanie strefy wydłużania (elongacyjnej) jako strefy, w której zachodzi wzrost prowadzący do wygięcia korzenia w dół.
- **biologia/2024-czerwiec/19.1#2** wzór: p = 0,7; 2pq = 0,42
  - AI: Wyliczenie częstości allelu A: p = 1 − 0,3 = 0,7; Poprawne podstawienie do wzoru: 2 · 0,7 · 0,3 = 0,42
- **biologia/2025-czerwiec/14.1#2** wzór: HIV niszczy limfocyty T pomocnicze (CD4)
  - AI: HIV niszczy limfocyty T pomocnicze (Th, CD4+), a nie limfocyty B; Brak wyjaśnienia roli osłabionej odporności komórkowej w utrzymywaniu prątków w uśpieniu
- **biologia/2025-czerwiec/14.1#3** wzór: zniszczenie limfocytów T pomocniczych
  - AI: wskazanie, że HIV niszczy limfocyty T pomocnicze; powiązanie osłabienia odporności komórkowej z brakiem utrzymywania prątków w stanie uśpienia
- **chemia/2026-maj/24#2** wzór: projekt 2: –NO₂ kieruje w meta, –Cl w orto/para
  - AI: Wskazanie właściwego projektu 2 (nitrowanie → chlorowanie → redukcja); Poprawne uzasadnienie: grupa –NO₂ jest podstawnikiem II rodzaju i kieruje kolejny podstawnik w położenie meta
- **chemia/2026-maj/24#3** wzór: uzasadnienie (kierujący wpływ grupy –NO₂)
  - AI: uzasadnienie, że grupa –NO₂ kieruje kolejny podstawnik w położenie meta; informacja, że –Cl kieruje w położenie orto/para
- **chemia/2015-maj-f2015/5.1#2** wzór: hybrydyzacja sp²
  - AI: Poprawna hybrydyzacja S: sp² (podano sp³)
- **chemia/2016-maj-f2015/24.2#2** wzór: A – kwas propanowy
  - AI: produkt A: kwas propanowy (zamiast propanalu)
- **chemia/2017-maj-f2015/1.3#2** wzór: tlenek na maksymalnym stopniu utlenienia: CrO₃
  - AI: wzór tlenku Z na maksymalnym stopniu utlenienia: CrO₃ (chrom(VI)) zamiast Cr₂O₃
- **chemia/2026-czerwiec/11.2#3** wzór: roztwór nasycony; Cp ≈ 16,7%
  - AI: Poprawne rozstrzygnięcie: roztwór nasycony (z osadem); Poprawna masa substancji rozpuszczonej: 30 g CuSO₄ przy rozpuszczalności 20 g/100 g wody; Poprawna masa roztworu: 150 g + 30 g = 180 g; Poprawny wynik: Cp ≈ 16,7%
- **chemia/2026-czerwiec/11.2#2** wzór: Cp liczone tylko z rozpuszczonej soli (30 g) – ok. 16,7%
  - AI: Masa substancji rozpuszczonej w roztworze to 20 g (rozpuszczalność), a nie 70 g – reszta tworzy osad.; Masa roztworu to 150 g wody + 20 g CuSO₄ = 170 g, a nie 220 g.; Poprawny wynik: Cp = 20/170 · 100% ≈ 11,8%, a nie ok. 16,7% z kluczem – trzeba jednak uwzględnić, że klucz podaje Cp ok. 16,7% (np. 20/120), więc należy sprawdzić przyjętą masę roztworu zgodnie z kluczem.
- **chemia/2025-maj/13#3** wzór: metoda: bilans stężeń z warunku spadku ciśnienia; Kc ≈ 14,8
  - AI: Zapis reakcji N₂ + 3H₂ ⇌ 2NH₃ i bilans stężeń (zmiana x, stężenia równowagowe); Wyrażenie na Kc = [NH₃]²/([N₂]·[H₂]³); Poprawny wynik Kc ≈ 14,8 z jednostką (dm⁶·mol⁻²)
- **chemia/2025-maj/13#2** wzór: błędne wyrażenie na Kc (brak potęg) – błąd metody, wynik ok. 14,8
  - AI: Potęga 2 przy [NH₃] w liczniku, zgodnie ze współczynnikiem 2 w równaniu; Potęga 3 przy [H₂] w mianowniku, zgodnie ze współczynnikiem 3 w równaniu; Poprawny wynik Kc ≈ 14,8 (bez jednostki, bo dla tej reakcji Kc ma jednostkę dm⁶·mol⁻²)
- **chemia/2022-grudzien/8#1** wzór: obliczenia (metoda)
  - AI: Równania reakcji Mg i Al z HCl oraz zależności między ilością wydzielonego H2 a masą metalu.; Ułożenia równania z niewiadomą masą (np. m_Al) i wyliczenia masy Al i mieszaniny.; Obliczenia procentu masowego Al z jednostką (%).
- **geografia/2026-maj/6.1#2** wzór: naprzemianległe piaskowce i łupki; łupki nasiąknięte wodą jako powierzchnia poślizgu
  - AI: naprzemianległe warstwy piaskowców i łupków jako budowa fliszu; chłonięcie wody przez łupki i powstanie śliskiej powierzchni poślizgu; zsuwanie się nachylonych warstw po stoku
- **geografia/2026-maj/6.1#3** wzór: rola łupków / wody jako powierzchni poślizgu
  - AI: wskazanie naprzemianległych piaskowców i łupków; wyjaśnienie, że łupki chłoną wodę i stają się śliską powierzchnią poślizgu; wskazanie, że nachylone warstwy zsuwają się po stoku
- **geografia/2026-maj/10.1#2** wzór: wyjaśnienie dla stacji B (strefa zbieżności, deszcze zenitalne)
  - AI: Wyjaśnienia, dlaczego stacja B ma dużo opadów (w głębi lądu latem dociera strefa zbieżności z deszczami zenitalnymi).; Mechanizmu dla stacji A: zimny prąd chłodzi powietrze i hamuje parowanie.
- **geografia/2026-maj/10.1#3** wzór: zimny prąd przy A; deszcze zenitalne przy B
  - AI: Wyjaśnienia niskich opadów na stacji A: zimny prąd Benguelski chłodzi powietrze i hamuje parowanie; Wskazania, że stacja B leży w głębi lądu, gdzie latem dociera strefa zbieżności z deszczami zenitalnymi; Poprawnego uzasadnienia różnicy opadów (uczeń błędnie twierdzi, że na wybrzeżu pada dużo)
- **geografia/2023-czerwiec/1.2#2** wzór: wyrównywanie brzegu przez fale i prąd przybrzeżny (pływy na Bałtyku są znikome)
  - AI: Wskazanie prądu przybrzeżnego jako czynnika wyrównującego brzeg od strony morza; Poprawne określenie roli falowania od strony morza (zamiast pływów); Wyjaśnienie, że w zatoce prądy są słabe, więc brzeg pozostaje urozmaicony
- **geografia/2024-grudzien/10#2** wzór: uwarunkowanie astronomiczne – siła Coriolisa
  - AI: uwarunkowanie astronomiczne: ruch obrotowy Ziemi (siła Coriolisa) i odchylenie wiatru w prawo na półkuli północnej, w lewo na południowej
- **geografia/2024-grudzien/10#3** wzór: kierunek: od wyżu do niżu
  - AI: Poprawny kierunek barycznego uwarunkowania: od wyżów zwrotnikowych do niżu równikowego; Wyjaśnienie, że siła Coriolisa odchyla wiatr na półkuli północnej w prawo, a na południowej w lewo (stąd pasaty NE i SE)
- **geografia/2024-czerwiec/28#2** wzór: druga cecha (np. wysokie opady, duże spadki rzek)
  - AI: druga cecha środowiska sprzyjająca energetyce wodnej (np. wysokie opady, duże spadki rzek na krawędziach wyżyn); doprecyzowanie, że chodzi o rzeki o dużych przepływach
- **geografia/2024-grudzien/30#2** wzór: szybki rozwój gospodarek wschodzących
  - AI: szybki rozwój gospodarczy krajów wschodzących, np. Chin i Indii; przeniesienie produkcji z krajów G7 do krajów wschodzących; wolny wzrost PKB w krajach G7
- **historia/2025-maj/4#2** wzór: B – benedyktyni
  - AI: B – benedyktyni (uczeń podał cystersi)
- **historia/2025-maj/4#3** wzór: A – franciszkanie; B – benedyktyni
  - AI: A: franciszkanie (podano dominikanów); B: benedyktyni (podano cystersów)
- **geografia/2026-styczen/24#2** wzór: Australia: suchy klimat → przewaga pastwisk
  - AI: Australia: suchy klimat w większości kraju; Australia: dominacja pastwisk i wypasu owiec; Australia: uprawy ograniczone do płd.-wsch. części kraju; Dania: umiarkowany klimat jako czynnik przyrodniczy
- **historia/2026-maj/18.2#3** wzór: dokument dotyczy konferencji poczdamskiej
  - AI: Wskazania, że dokument pochodzi z konferencji poczdamskiej (1945), a nie z Jałty.; Odwołania do treści dokumentu, np. ustaleń o granicy na Odrze, Gdańsku lub administracji Polski nad częścią Prus Wschodnich.
- **historia/2026-maj/18.2#2** wzór: uzasadnienie: Wersal 1919 vs Poczdam 1945
  - AI: nazwa traktatu wersalskiego (1919) z znaczka; nazwa postanowień konferencji poczdamskiej (1945) jako źródła fragmentu; konkretne treści wskazujące na różnicę, np. granica na Odrze, Gdańsk, Prusy Wschodnie
- **historia/2024-maj/24#2** wzór: mapa: Czechosłowacja 1968, tekst: Węgry 1956
  - AI: Rozstrzygnięcie „nie” - wydarzenia w mapie i tekście są różne; Odwołanie do źródeł: mapy (inwazja na Czechosłowację 1968) i tekstu (powstanie węgierskie 1956, Nagy)
- **historia/2024-grudzien/5.1#2** wzór: ekskomunika Henryka IV i Canossa
  - AI: treść dokumentu: ogłoszenie wyższości papieża nad cesarzem (Dictatus papae); reakcja Henryka IV i jej skutek w postaci ekskomuniki; upokorzenie cesarza w Canossie (1077) jako konkretny skutek
- **historia/2026-maj/22#2** wzór: Polska odrzuciła udział pod presją ZSRS
  - AI: Odwołanie do wykresu: obecność krajów spoza Europy (Chiny, Filipiny, Etiopia); Wskazanie, że plan Marshalla był skierowany do Europy; Poprawna przyczyna nieudziału Polski: odrzucenie pomocy pod presją ZSRS, a nie brak zaproszenia
- **historia/2024-grudzien/4#2** wzór: oba – Bolesław Chrobry
  - AI: Poprawne rozstrzygnięcie: oba źródła dotyczą Bolesława Chrobrego.; Uzasadnienie odwołujące się do źródeł (syn poganina i chrześcijanki, wyniesienie przez cesarza; zjazd gnieźnieński, korona od Ottona III).
- **historia/2026-czerwiec/22#2** wzór: argument dotyczący drugiego fragmentu (abdykacja Wilhelma II / rewolucja w Niemczech)
  - AI: Brak wskazania, że powrót Piłsudskiego (10 XI 1918) dotyczy ziem polskich i Rządu Tymczasowego w Lublinie; Brak drugiego argumentu: abdykacji Wilhelma II i rewolucji w Niemczech (9 XI 1918) jako wydarzeń z końca wojny
- **wos/2024-maj/17.4#2** wzór: ETPC – Rada Europy
  - AI: Poprawne wskazanie, że ETPC należy do systemu ochrony praw człowieka Rady Europy; Poprawna przynależność organizacyjna (Rada Europy zamiast ONZ)
- **wos/2026-maj/16.2#2** wzór: pełna nazwa (polecenie wymaga pełnej nazwy)
  - AI: Pełna polska nazwa organizacji: Organizacja Narodów Zjednoczonych
- **wos/2024-maj/17.4#3** wzór: wskazanie ETPC (Rada Europy)
  - AI: Poprawnie wskazanej instytucji spoza systemu instytucjonalnego UE, np. Europejskiego Trybunału Praw Człowieka; Uzasadnienia, że dana instytucja należy do innego systemu (np. Rady Europy)
- **wos/2024-maj/14.2#2** wzór: Kodeks cywilny
  - AI: Poprawna nazwa kodeksu: Kodeks cywilny
- **wos/2026-maj/16.2#3** wzór: Organizacja Narodów Zjednoczonych
  - AI: Pełna polska nazwa: Organizacja Narodów Zjednoczonych
- **wos/2026-czerwiec/13.2#2** wzór: uzasadnienie z nazwą organu (NIK)
  - AI: nazwa Najwyższej Izby Kontroli w uzasadnieniu; odwołanie do treści przepisu Konstytucji (np. sposób powołania Prezesa NIK); odwołanie do treści tekstu źródłowego
- **wos/2024-maj/16.2#2** wzór: tak – rezolucja RB ONZ
  - AI: Poprawne rozstrzygnięcie: operacja była prowadzona na podstawie mandatu ONZ (Tak).; Uzasadnienie wskazujące rezolucję Rady Bezpieczeństwa ONZ jako podstawę operacji.
- **wos/2023-maj/12.2#2** wzór: wydatki > dochody → deficyt
  - AI: Rozstrzygnięcie 'Tak' - w uchwale planowane wydatki są wyższe od dochodów.; Odwołanie do konkretnych danych z przytoczonego fragmentu uchwały.
- **wos/2023-maj/10.1#2** wzór: 2. USA
  - AI: Stany Zjednoczone (USA) jako drugie państwo – uczeń podał Wielką Brytanię, która nie jest prawidłową odpowiedzią
- **wos/2025-czerwiec/3.2#2** wzór: uzasadnienie: mała grupa pierwotna, nacisk na zgodność z normami
  - AI: Uzasadnienia opartego na tym, że rodzina jest grupą małą i pierwotną, w której łatwiej skłonić jednostkę do zachowania zgodnego z oczekiwaniami grupy.