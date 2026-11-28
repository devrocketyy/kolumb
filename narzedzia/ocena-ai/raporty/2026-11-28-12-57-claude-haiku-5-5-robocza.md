# Test oceny AI — claude-haiku-5-5 (effort low), część robocza

2026-11-28T12:57:32.548Z · tokeny 115247/28182 · koszt 0.09 zł

| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| **ogółem** | 97 | 92.8% | 0.0% | 3.1% | 4.1% | 0 |

Progi: zgodność ≥ 90%, poważne ≤ 2%, trafność „czego zabrakło” ≥ 85% (przegląd ręczny poniżej).

### Przedmioty
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| biologia | 28 | 96.4% | 0.0% | 3.6% | 0.0% | 0 |
| chemia | 17 | 82.4% | 0.0% | 5.9% | 11.8% | 0 |
| geografia | 17 | 94.1% | 0.0% | 0.0% | 5.9% | 0 |
| historia | 17 | 88.2% | 0.0% | 5.9% | 5.9% | 0 |
| wos | 18 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |

### Typy zadań
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| oblicz | 10 | 70.0% | 0.0% | 20.0% | 10.0% | 0 |
| okresl | 10 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| podaj | 29 | 93.1% | 0.0% | 3.4% | 3.4% | 0 |
| rozstrzygnij | 18 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| uzasadnij | 11 | 81.8% | 0.0% | 0.0% | 18.2% | 0 |
| wyjasnij | 14 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| wykaz | 5 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |

### Punktacja
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| 1 | 65 | 96.9% | 0.0% | 1.5% | 1.5% | 0 |
| 2 | 32 | 84.4% | 0.0% | 6.3% | 9.4% | 0 |

## Rozbieżności
- **biologia/2024-czerwiec/19.1#3** wzór 0/1, AI 1/1 — „Heterozygoty to 0,42.”
  - AI: Podano poprawną częstość heterozygot 0,42, zgodną z kluczem (2pq = 2·0,7·0,3). Odpowiedź jest poprawna i nie zawiera błędnych elementów.
- **chemia/2026-maj/24#1** wzór 1/1, AI 0/1 — „Projekt 2, bo najpierw wprowadzamy grupę nitrową, a ona kieruje następny podstawnik (chlor) w położenie meta.”
  - AI: Wskazanie projektu 2 jest poprawne, ale uczeń błędnie uzasadnia kierowanie: grupa –NO₂ kieruje chlor w położenie meta, a nie wprowadza go do meta, jak sugeruje zdanie. Sformułowanie „grupa nitrowa kieruje następny podstawnik (chlor) w położenie meta” jest mylące, bo nie wskazuje, że chlor wchodzi w meta względem –NO₂ i że to właśnie ta orientacja daje produkt meta; uzasadnienie jest więc niepełne. Dodatkowo nie uwzględniono, że –Cl kierowałby w orto/para, co jest istotą porównania projektów.
- **chemia/2026-czerwiec/11.2#2** wzór 1/2, AI 0/2 — „Roztwór nasycony. Cp = 70 / 220 · 100% = 31,8%.”
  - AI: Poprawnie rozpoznasz roztwór jako nasycony, ale obliczenie Cp jest błędne: przyjąłeś za masę roztworu 70 g + 150 g = 220 g, pomijając, że w roztworze rozpuści się tylko 20 g CuSO₄ na 150 g wody (reszta, 50 g, tworzy osad). Wynik 31,8% jest więc niepoprawny.
- **chemia/2025-maj/13#2** wzór 0/2, AI 1/2 — „x = 0,1, więc [N₂] = 0,1, [H₂] = 0,3, [NH₃] = 0,2. Kc = 0,2 / (0,1 · 0,3) = 6,67.”
  - AI: Poprawnie wyznaczyłeś x = 0,1 i stężenia równowagowe [N₂] = 0,1, [H₂] = 0,3, [NH₃] = 0,2 mol·dm⁻³, więc część za bilans jest przyznana. Wyrażenie na Kc jest jednak błędne: brakuje potęg zgodnych ze współczynnikami reakcji N₂ + 3H₂ ⇌ 2NH₃, czyli [NH₃]² i [H₂]³. Wynik 6,67 jest zatem błędny, a jednostka nie jest podana.
- **geografia/2024-grudzien/10#3** wzór 1/2, AI 0/2 — „Wiatr wieje od niżu równikowego do wyżów zwrotnikowych, a odchyla go ruch obrotowy Ziemi.”
  - AI: Uczeń odwrócił kierunek ruchu powietrza: wiatr wieje od wyżów zwrotnikowych do niżu równikowego, a nie odwrotnie. Element astronomiczny jest ogólnikowy (brak wskazania, że siła Coriolisa odchyla wiatr w prawo na półkuli północnej i w lewo na południowej), a część barycznej odpowiedzi jest błędna, więc punktów nie przyznaję.
- **historia/2025-maj/4#3** wzór 0/2, AI 1/2 — „A – dominikanie, B – cystersi, C – jezuici.”
  - AI: Poprawnie wskazano tylko zakon C (jezuici). Zakon A to franciszkanie, a nie dominikanie, zaś zakon B to benedyktyni, a nie cystersi, więc przyznano jeden punkt zgodnie z zasadą dla dwóch poprawnych nazw.
- **historia/2026-czerwiec/22#2** wzór 1/2, AI 0/2 — „Wtedy wrócił Piłsudski i Polska odzyskała niepodległość.”
  - AI: Odpowiedź zawiera jedno ogólnikowe zdanie, bez wskazania konkretnych argumentów odnoszących się do fragmentów. Powrót Piłsudskiego (10 XI 1918) wspomniany jest bez daty i bez wiązania z fragmentem, a odzyskanie niepodległości nie jest argumentem uzasadniającym datę listopadową dla obu źródeł.

## „Czego zabrakło” — do przeglądu
- **biologia/2023-maj/1.3#2** wzór: przekształcenie pirogronianu w acetylo-CoA; acetylo-CoA jako substrat cyklu Krebsa
  - AI: produkt glikolizy (pirogronian) jako substrat kompleksu; powstawanie acetylo-CoA; acetylo-CoA jako substrat cyklu Krebsa
- **biologia/2023-maj/1.3#3** wzór: błędna lokalizacja cyklu Krebsa (macierz mitochondrium)
  - AI: Informacja, że kompleks dehydrogenazy pirogronianowej działa w mitochondriach (macierz mitochondrialna), a nie w cytozolu.; Poprawna lokalizacja cyklu Krebsa: macierz mitochondrialna, a nie jądro komórkowe.; Wyraźne wskazanie, że acetylo-CoA jest substratem cyklu Krebsa.
- **biologia/2023-maj/4.2#2** wzór: wyrównanie materiału / wykluczenie wpływu innych czynników
  - AI: Informacji, że warunki mają być takie same, by rośliny były możliwie podobne na starcie.; Informacji, że dzięki temu wyłączasz wpływ innych czynników i wynik zależy tylko od badanego czynnika.
- **biologia/2023-maj/5.1#2** wzór: C – regeneracja RuBP
  - AI: C – poprawna nazwa to regeneracja RuBP (akceptator CO₂), a nie fosforylacja
- **biologia/2023-maj/5.1#3** wzór: A – karboksylacja; B – redukcja
  - AI: A: karboksylacja (wiązanie CO₂ z RuBP) – podano glikolizę, która nie jest etapem cyklu Calvina; B: redukcja (PGA do aldehydu 3-fosfoglicerynowego) – podano fotolizę wody, proces fazy jasnej
- **biologia/2024-maj/2#2** wzór: funkcja rybonukleazy (rozkład RNA z hybrydy)
  - AI: Funkcja obszaru o aktywności rybonukleazy: rozkład (hydroliza) RNA w hybrydzie RNA-DNA, aby umożliwić syntezę drugiej nici DNA.
- **biologia/2024-maj/2#3** wzór: rybonukleaza rozkłada RNA, a nie syntetyzuje
  - AI: Rybonukleaza nie syntetyzuje RNA wirusa, tylko rozkłada nić RNA w hybrydzie RNA-DNA.; Brak wskazania, że rozkład RNA umożliwia powstanie drugiej nici DNA.
- **biologia/2024-maj/2#4** wzór: funkcja polimerazy; funkcja rybonukleazy
  - AI: Polimeraza (odwrotna transkryptaza) syntetyzuje DNA na matrycy RNA wirusa (a potem drugą nić na matrycy DNA).; Rybonukleaza rozkłada (hydrolizuje) RNA w hybrydzie RNA-DNA, umożliwiając powstanie drugiej nici DNA.
- **biologia/2024-maj/17.2#2** wzór: funkcja antykodonu
  - AI: funkcja antykodonu: komplementarne wiązanie się z kodonem mRNA; wskazanie, że dzięki temu wstawiany jest właściwy aminokwas
- **biologia/2024-maj/17.2#3** wzór: funkcja ramienia akceptorowego; funkcja antykodonu
  - AI: Ramię akceptorowe: przyłączanie aminokwasu (koniec 3′); Antykodon: komplementarne wiązanie się z kodonem mRNA
- **biologia/2025-maj/1.2#3** wzór: uzasadnienie (jeden łańcuch polipeptydowy)
  - AI: Uzasadnienia, że rybonukleaza to jeden łańcuch polipeptydowy, więc mostki powstają w obrębie tego samego łańcucha.; Wyjaśnienia, że struktura IV-rzędowa wymagałaby co najmniej dwóch łańcuchów.
- **biologia/2025-maj/1.2#2** wzór: struktura III-rzędowa – jeden łańcuch
  - AI: Wskazanie poprawnej struktury: III-rzędowej.; Poprawne uzasadnienie: rybonukleaza to pojedynczy łańcuch polipeptydowy, więc mostki tworzą się wewnątrz niego.; Wyjaśnienie, że struktura IV-rzędowa wymaga co najmniej dwóch łańcuchów.
- **biologia/2025-maj/3.2#3** wzór: strefa wydłużania
  - AI: Nazwa strefy wydłużania (elongacyjna, wzrostu na długość) jako strefy, w której zachodzi wzrost prowadzący do wygięcia wierzchołka
- **biologia/2024-czerwiec/19.1#2** wzór: p = 0,7; 2pq = 0,42
  - AI: Obliczenie częstości allelu B (p = 1 − 0,3 = 0,7).; Poprawny wynik częstości heterozygot: 2pq = 2 · 0,7 · 0,3 = 0,42.
- **biologia/2024-czerwiec/19.1#3** wzór: obliczenia (p = 0,7; 2pq = 2 · 0,7 · 0,3)
  - AI: —
- **biologia/2025-czerwiec/14.1#2** wzór: HIV niszczy limfocyty T pomocnicze (CD4)
  - AI: Wskazanie limfocytów T pomocniczych (CD4+) jako komórek niszczonych przez HIV; Wyjaśnienie, że osłabiona odporność komórkowa nie utrzymuje prątków w stanie uśpienia
- **biologia/2025-czerwiec/14.1#3** wzór: zniszczenie limfocytów T pomocniczych
  - AI: wskazanie, że HIV niszczy limfocyty T pomocnicze (komórki Th); wyjaśnienie, że bez nich organizm nie utrzymuje prątków w stanie uśpienia; informacja, że prątki zaczynają się wtedy namnażać
- **chemia/2026-maj/24#3** wzór: uzasadnienie (kierujący wpływ grupy –NO₂)
  - AI: Uzasadnienie, że grupa –NO₂ kieruje kolejny podstawnik w położenie meta; Informacja, że –Cl kieruje w położenie orto/para, więc w projekcie 1 powstałby produkt orto/para
- **chemia/2026-maj/24#2** wzór: projekt 2: –NO₂ kieruje w meta, –Cl w orto/para
  - AI: Wskazanie właściwego projektu 2 (nitrowanie → chlorowanie → redukcja).; Poprawne uzasadnienie: –NO₂ jest kierownikiem II rodzaju i w pierwszym etapie kieruje kolejny podstawnik w położenie meta.; Poprawny kierunek działania chloru: –Cl kieruje w położenia orto i para.
- **chemia/2016-maj-f2015/24.2#2** wzór: A – kwas propanowy
  - AI: Produkt utleniania A: kwas propanowy (zamiast propanalu)
- **chemia/2015-maj-f2015/5.1#2** wzór: hybrydyzacja sp²
  - AI: Poprawna hybrydyzacja atomu S: sp² (zamiast sp³)
- **chemia/2017-maj-f2015/1.3#2** wzór: tlenek na maksymalnym stopniu utlenienia: CrO₃
  - AI: Poprawny wzór tlenku Z na maksymalnym stopniu utlenienia chromu: CrO₃ (zamiast Cr₂O₃)
- **chemia/2026-czerwiec/11.2#2** wzór: Cp liczone tylko z rozpuszczonej soli (30 g) – ok. 16,7%
  - AI: Uwzględnienia, że rozpuszcza się tylko 30 g CuSO₄ (20 g na 100 g wody · 150 g wody = 30 g), a nie 70 g.; Masy roztworu nasyconego: 30 g + 150 g = 180 g.; Poprawnego wyniku Cp ≈ 16,7% (30/180 · 100%).
- **chemia/2026-czerwiec/11.2#3** wzór: roztwór nasycony; Cp ≈ 16,7%
  - AI: Poprawne rozstrzygnięcie: roztwór nasycony z osadem (rozpuszczone jest tylko 30 g CuSO₄).; Poprawna metoda obliczenia Cp: masa substancji w roztworze to 30 g, masa roztworu to 180 g.; Poprawny wynik: Cp ≈ 16,7%.
- **chemia/2025-maj/13#3** wzór: metoda: bilans stężeń z warunku spadku ciśnienia; Kc ≈ 14,8
  - AI: Bilans stężeń w stanie równowagi (zmiana liczby moli/stężeń N₂, H₂, NH₃) wynikający ze spadku ciśnienia do 75%; Obliczenie stężeń równowagowych [N₂], [H₂], [NH₃]; Zastosowanie wyrażenia Kc = [NH₃]²/([N₂]·[H₂]³) i podanie wyniku; Poprawny wynik Kc ≈ 14,8
- **chemia/2022-grudzien/8#1** wzór: obliczenia (metoda)
  - AI: Zapisu reakcji Mg, Al z HCl i stosunku moli wodoru; Obliczeń mas Mg i Cu oraz Al i Ag z zachowaniem warunku tej samej masy i tej samej ilości wodoru; Obliczenia procentu masowego glinu w mieszaninie z wynikiem
- **chemia/2025-maj/13#2** wzór: błędne wyrażenie na Kc (brak potęg) – błąd metody, wynik ok. 14,8
  - AI: Poprawna postać Kc = [NH₃]² / ([N₂]·[H₂]³); Poprawny wynik Kc ≈ 14,8 (dm⁶·mol⁻²); Jednostka wyniku
- **geografia/2026-maj/6.1#2** wzór: naprzemianległe piaskowce i łupki; łupki nasiąknięte wodą jako powierzchnia poślizgu
  - AI: wskazanie naprzemianległych warstw piaskowców i łupków; informacja, że łupki chłoną wodę i stają się śliską powierzchnią poślizgu; związek z nachyleniem warstw, po których zsuwa się materiał
- **geografia/2026-maj/6.1#3** wzór: rola łupków / wody jako powierzchni poślizgu
  - AI: wskazanie naprzemianległych piaskowców i łupków; wyjaśnienie, że łupki chłoną wodę i tworzą śliską powierzchnię poślizgu; wskazanie, że nachylone warstwy zsuwają się po stoku
- **geografia/2026-maj/10.1#2** wzór: wyjaśnienie dla stacji B (strefa zbieżności, deszcze zenitalne)
  - AI: Wyjaśnienia wysokich opadów na stacji B (916 m n.p.m., w głębi lądu).; Odniesienia do strefy zbieżności zwrotnikowej i deszczów zenitalnych dochodzących latem.; Porównania obu przyczyn jako różnicy między stacjami.
- **geografia/2026-maj/10.1#3** wzór: zimny prąd przy A; deszcze zenitalne przy B
  - AI: Wyjaśnienia dla stacji A: zimny prąd Benguelski chłodzi powietrze i hamuje parowanie, stąd mało opadów.; Wyjaśnienia dla stacji B: w głębi lądu latem dociera strefa zbieżności z deszczami zenitalnymi.; Poprawnej przyczyny różnicy – uczeń opiera się na wysokości n.p.m. i bliskości morza, a pomija czynniki klimatyczne.
- **geografia/2023-czerwiec/1.2#2** wzór: wyrównywanie brzegu przez fale i prąd przybrzeżny (pływy na Bałtyku są znikome)
  - AI: wskazanie prądu przybrzeżnego jako czynnika wyrównującego brzeg od strony morza; poprawne przypisanie wyrównywania brzegu falowaniu (nie pływom); wzmianka o słabych prądach w zatoce
- **geografia/2024-grudzien/10#2** wzór: uwarunkowanie astronomiczne – siła Coriolisa
  - AI: uwarunkowanie astronomiczne: ruch obrotowy Ziemi / siła Coriolisa; wyjaśnienie odchylenia wiatru w prawo na N i w lewo na S (kierunki NE i SE)
- **geografia/2024-grudzien/10#3** wzór: kierunek: od wyżu do niżu
  - AI: Poprawny kierunek: od wyżów zwrotnikowych do niżu równikowego; Wskazanie siły Coriolisa jako przyczyny odchylenia; Kierunek odchylenia: w prawo na półkuli północnej, w lewo na południowej; Związek z pasatami NE i SE
- **geografia/2024-czerwiec/28#2** wzór: druga cecha (np. wysokie opady, duże spadki rzek)
  - AI: druga cecha środowiska (np. wysokie opady lub duże spadki rzek); doprecyzowanie, że rzeki mają duże przepływy (zasobność w wodę)
- **geografia/2024-grudzien/30#2** wzór: szybki rozwój gospodarek wschodzących
  - AI: szybki rozwój gospodarczy krajów wschodzących (Chiny, Indie); wolniejszy wzrost PKB w krajach G7; przeniesienie produkcji do krajów wschodzących
- **geografia/2026-styczen/24#2** wzór: Australia: suchy klimat → przewaga pastwisk
  - AI: Australia: suchy klimat w większości kraju; Australia: dominacja pastwisk (wypas owiec); Australia: uprawy ograniczone do południowo-wschodniej części kraju; Dania: umiarkowany klimat jako czynnik wpływający na użytkowanie
- **historia/2025-maj/4#2** wzór: B – benedyktyni
  - AI: B – benedyktyni (klasztor Monte Cassino założył Benedykt z Nursji; cystersi to odrębny zakon powstały w XI w.)
- **historia/2025-maj/4#3** wzór: A – franciszkanie; B – benedyktyni
  - AI: A: franciszkanie (podano dominikanie); B: benedyktyni (podano cystersi)
- **historia/2026-maj/18.2#2** wzór: uzasadnienie: Wersal 1919 vs Poczdam 1945
  - AI: Nazwa traktatu upamiętnionego na znaczku (traktat wersalski, 1919).; Nazwa dokumentu, z którego pochodzi fragment (postanowienia konferencji poczdamskiej, 1945).; Konkretne treści fragmentu, np. granica na Odrze, Gdańsk czy administracja polska w Prusach Wschodnich, jako dowód przynależności do innego dokumentu.
- **historia/2024-maj/24#2** wzór: mapa: Czechosłowacja 1968, tekst: Węgry 1956
  - AI: Rozstrzygnięcia „Nie” – wydarzenia są różne; Identyfikacji wydarzenia z mapy (inwazja Układu Warszawskiego na Czechosłowację, 1968); Identyfikacji wydarzenia z tekstu (stłumienie powstania węgierskiego, 1956); Uzasadnienia opartego na źródłach
- **historia/2026-maj/18.2#3** wzór: dokument dotyczy konferencji poczdamskiej
  - AI: Poprawna nazwa konferencji: poczdamska (1945), a nie jałtańska.; Odwołanie do treści dokumentu, np. ustalenia granicy na Odrze i Nysie Łużyckiej, przyznania Gdańska czy administracji Polski na części Prus Wschodnich.
- **historia/2024-grudzien/5.1#2** wzór: ekskomunika Henryka IV i Canossa
  - AI: treść dokumentu: Dictatus papae ogłasza wyższość papieża nad cesarzem; reakcja Henryka IV: sprzeciw wobec papieskich postanowień; skutki: ekskomunika cesarza i upokorzenie w Canossie w 1077 r.
- **historia/2026-maj/22#2** wzór: Polska odrzuciła udział pod presją ZSRS
  - AI: Informacja, że Polska i Czechosłowacja odrzuciły plan pod presją ZSRS (zamiast twierdzenia o braku zaproszenia); Odwołanie do krajów z wykresu spoza Europy (Chiny, Filipiny, Etiopia) jako dowodu; Wskazanie, że plan Marshalla był skierowany do Europy
- **historia/2024-grudzien/4#2** wzór: oba – Bolesław Chrobry
  - AI: Poprawne rozstrzygnięcie: oba źródła dotyczą Bolesława Chrobrego.; Uzasadnienie odwołujące się do treści źródeł: w napisie nagrobnym syn poganina i chrześcijanki wyniesiony przez cesarza oraz w źródle 2 zjazd gnieźnieński, arcybiskupstwo dla Radzima i korona nałożona przez Ottona III.
- **historia/2026-czerwiec/22#2** wzór: argument dotyczący drugiego fragmentu (abdykacja Wilhelma II / rewolucja w Niemczech)
  - AI: Brak wskazania argumentu dotyczącego fragmentu o ziemiach polskich (np. Rząd Tymczasowy w Lublinie lub powrót Piłsudskiego 10 XI 1918 r.).; Brak wskazania argumentu dotyczącego fragmentu europejskiego (abdykacja Wilhelma II i rewolucja w Niemczech 9 XI 1918 r. lub koniec wojny).; Brak daty ani jednoznacznego powiązania z listopadem 1918 r.
- **wos/2024-maj/17.4#2** wzór: ETPC – Rada Europy
  - AI: Wskazanie, że ETPC jest instytucją Rady Europy (systemu ochrony praw człowieka), a nie ONZ
- **wos/2024-maj/17.4#3** wzór: wskazanie ETPC (Rada Europy)
  - AI: Wskazania instytucji niebędącej częścią systemu instytucjonalnego UE (np. Europejskiego Trybunału Praw Człowieka, należącego do Rady Europy).; Uzasadnienia, dlaczego wskazana instytucja nie należy do systemu UE.
- **wos/2026-maj/16.2#2** wzór: pełna nazwa (polecenie wymaga pełnej nazwy)
  - AI: Pełna polska nazwa: Organizacja Narodów Zjednoczonych
- **wos/2026-maj/16.2#3** wzór: Organizacja Narodów Zjednoczonych
  - AI: Pełna polska nazwa: Organizacja Narodów Zjednoczonych
- **wos/2024-maj/14.2#2** wzór: Kodeks cywilny
  - AI: Poprawna nazwa kodeksu: Kodeks cywilny
- **wos/2026-czerwiec/13.2#2** wzór: uzasadnienie z nazwą organu (NIK)
  - AI: Nazwa organu konstytucyjnego (Najwyższa Izba Kontroli) w uzasadnieniu; Odwołanie do treści przepisu Konstytucji (np. sposób powołania Prezesa NIK); Odwołanie do treści tekstu źródłowego
- **wos/2024-maj/16.2#2** wzór: tak – rezolucja RB ONZ
  - AI: Poprawne rozstrzygnięcie: tak, operacja była przeprowadzona na podstawie mandatu ONZ.; Uzasadnienie wskazujące na rezolucję Rady Bezpieczeństwa ONZ jako podstawę operacji.
- **wos/2023-maj/12.2#2** wzór: wydatki > dochody → deficyt
  - AI: Poprawne rozstrzygnięcie: tak, w uchwale założony jest deficyt.; Odwołanie do danych z fragmentu uchwały: planowane wydatki są wyższe niż dochody budżetowe.
- **wos/2023-maj/10.1#2** wzór: 2. USA
  - AI: Państwo 2 powinno być Stanami Zjednoczonymi (USA), a nie Wielką Brytanią
- **wos/2025-czerwiec/3.2#2** wzór: uzasadnienie: mała grupa pierwotna, nacisk na zgodność z normami
  - AI: Wskazania, że rodzina jest grupą małą i pierwotną; Wyjaśnienia, że w takiej grupie łatwiej skłonić jednostkę do zachowania zgodnego z oczekiwaniami grupy (wpływ normatywny); Odniesienia do obu tekstów