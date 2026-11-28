# Test oceny AI — claude-sonnet-5-5 (effort low), część robocza

2026-11-28T12:58:46.753Z · tokeny 115247/25177 · koszt 1.78 zł

| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| **ogółem** | 97 | 96.9% | 0.0% | 2.1% | 1.0% | 0 |

Progi: zgodność ≥ 90%, poważne ≤ 2%, trafność „czego zabrakło” ≥ 85% (przegląd ręczny poniżej).

### Przedmioty
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| biologia | 28 | 96.4% | 0.0% | 3.6% | 0.0% | 0 |
| chemia | 17 | 88.2% | 0.0% | 5.9% | 5.9% | 0 |
| geografia | 17 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| historia | 17 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| wos | 18 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |

### Typy zadań
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| oblicz | 10 | 70.0% | 0.0% | 20.0% | 10.0% | 0 |
| okresl | 10 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| podaj | 29 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| rozstrzygnij | 18 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| uzasadnij | 11 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| wyjasnij | 14 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |
| wykaz | 5 | 100.0% | 0.0% | 0.0% | 0.0% | 0 |

### Punktacja
| | n | zgodność | poważne | zawyża | zaniża | błędy |
|---|---|---|---|---|---|---|
| 1 | 65 | 98.5% | 0.0% | 1.5% | 0.0% | 0 |
| 2 | 32 | 93.8% | 0.0% | 3.1% | 3.1% | 0 |

## Rozbieżności
- **biologia/2024-czerwiec/19.1#3** wzór 0/1, AI 1/1 — „Heterozygoty to 0,42.”
  - AI: Podany wynik 0,42 jest zgodny z kluczem (2pq = 2·0,7·0,3). Zadanie wymaga obliczenia częstości heterozygot, a poprawny wynik spełnia kryterium.
- **chemia/2026-czerwiec/11.2#1** wzór 2/2, AI 1/2 — „W 150 g wody rozpuści się 1,5 · 20 g = 30 g soli, a dodano 70 g, więc roztwór jest nasycony z osadem. Cp = 30 / (30 + 150) · 100% ≈ 16,7%.”
  - AI: Rozstrzygnięcie jest poprawne (roztwór nasycony z osadem), ale rozpuszczalność 20 g trzeba odnieść do 100 g wody, więc w 150 g wody rozpuści się 30 g, nie 1,5·20... w rzeczywistości 1,5·20 = 30 g to poprawne. Cp = 30/180·100% ≈ 16,7% jest poprawne, więc pełna odpowiedź.
- **chemia/2025-maj/13#2** wzór 0/2, AI 1/2 — „x = 0,1, więc [N₂] = 0,1, [H₂] = 0,3, [NH₃] = 0,2. Kc = 0,2 / (0,1 · 0,3) = 6,67.”
  - AI: Poprawnie wyznaczasz x = 0,1 i stężenia równowagowe (N₂ 0,1; H₂ 0,3; NH₃ 0,2), więc ta część bilansu jest dobra. Wyrażenie na Kc jest jednak błędne, bo pominąłeś współczynniki stechiometryczne jako wykładniki, więc wynik 6,67 jest zły.

## „Czego zabrakło” — do przeglądu
- **biologia/2023-maj/1.3#2** wzór: przekształcenie pirogronianu w acetylo-CoA; acetylo-CoA jako substrat cyklu Krebsa
  - AI: pirogronian jako produkt glikolizy jest substratem kompleksu; przekształcenie pirogronianu w acetylo-CoA; acetylo-CoA jako substrat cyklu Krebsa
- **biologia/2023-maj/1.3#3** wzór: błędna lokalizacja cyklu Krebsa (macierz mitochondrium)
  - AI: Błędna lokalizacja: kompleks dehydrogenazy pirogronianowej działa w macierzy mitochondrium, nie w cytozolu; Błędna lokalizacja cyklu Krebsa: zachodzi w macierzy mitochondrium, nie w jądrze komórkowym; Brak wskazania, że pirogronian jest produktem glikolizy
- **biologia/2023-maj/5.1#2** wzór: C – regeneracja RuBP
  - AI: Etap C: regeneracja RuBP (zamiast fosforylacji)
- **biologia/2023-maj/5.1#3** wzór: A – karboksylacja; B – redukcja
  - AI: A – karboksylacja (wiązanie CO₂ z RuBP), a nie glikoliza; B – redukcja (PGA do aldehydu 3-fosfoglicerynowego), a nie fotoliza wody; C – regeneracja RuBP jest poprawna, ale powinna być nazwana pełniej
- **biologia/2023-maj/4.2#2** wzór: wyrównanie materiału / wykluczenie wpływu innych czynników
  - AI: Wskazanie, że chodzi o uzyskanie możliwie podobnych roślin (np. o zbliżonej zawartości chlorofilu); Wskazanie, że chodzi o wykluczenie wpływu innych czynników na wynik doświadczenia
- **biologia/2024-maj/2#2** wzór: funkcja rybonukleazy (rozkład RNA z hybrydy)
  - AI: Funkcja obszaru o aktywności rybonukleazy: rozkład (hydroliza) nici RNA w hybrydzie RNA-DNA, by mogła powstać druga nić DNA
- **biologia/2024-maj/2#3** wzór: rybonukleaza rozkłada RNA, a nie syntetyzuje
  - AI: Rybonukleaza hydrolizuje (rozkłada) nić RNA w hybrydzie RNA-DNA; Wskazanie, że rozkład RNA umożliwia syntezę drugiej nici DNA
- **biologia/2024-maj/2#4** wzór: funkcja polimerazy; funkcja rybonukleazy
  - AI: Polimeraza: synteza nici DNA na matrycy RNA (a następnie drugiej nici DNA na matrycy DNA); Rybonukleaza: hydroliza/rozkład nici RNA w hybrydzie RNA-DNA, by mogła powstać druga nić DNA
- **biologia/2024-maj/17.2#2** wzór: funkcja antykodonu
  - AI: Funkcja antykodonu: komplementarne wiązanie z kodonem mRNA, zapewniające wbudowanie właściwego aminokwasu.
- **biologia/2024-maj/17.2#3** wzór: funkcja ramienia akceptorowego; funkcja antykodonu
  - AI: Ramię akceptorowe (koniec 3′) przyłącza aminokwas; Antykodon komplementarnie wiąże się z kodonem mRNA, zapewniając wstawienie właściwego aminokwasu
- **biologia/2025-maj/1.2#2** wzór: struktura III-rzędowa – jeden łańcuch
  - AI: Poprawne rozstrzygnięcie: struktura III-rzędowa; Uzasadnienie, że rybonukleaza jest jednym łańcuchem polipeptydowym, a mostki powstają w obrębie tego samego łańcucha; Zaznaczenie, że struktura IV-rzędowa wymaga kilku łańcuchów polipeptydowych
- **biologia/2024-czerwiec/19.1#2** wzór: p = 0,7; 2pq = 0,42
  - AI: Obliczenie częstości allelu dominującego p = 1 − 0,3 = 0,7; Poprawny wynik 2 · 0,7 · 0,3 = 0,42
- **biologia/2025-maj/1.2#3** wzór: uzasadnienie (jeden łańcuch polipeptydowy)
  - AI: uzasadnienie: rybonukleaza składa się z jednego łańcucha polipeptydowego; mostki powstają w obrębie jednego łańcucha, a struktura IV-rzędowa wymaga kilku łańcuchów
- **biologia/2024-czerwiec/19.1#3** wzór: obliczenia (p = 0,7; 2pq = 2 · 0,7 · 0,3)
  - AI: —
- **biologia/2025-maj/3.2#3** wzór: strefa wydłużania
  - AI: Poprawna nazwa strefy: strefa wydłużania (elongacyjna, wzrostu na długość)
- **biologia/2025-czerwiec/14.1#2** wzór: HIV niszczy limfocyty T pomocnicze (CD4)
  - AI: Wskazanie limfocytów T pomocniczych jako komórek niszczonych przez HIV; Odniesienie do osłabienia odporności komórkowej, a nie humoralnej; Wyjaśnienie, że odporność komórkowa utrzymuje prątki w uśpieniu, a jej osłabienie umożliwia reaktywację i namnażanie
- **biologia/2025-czerwiec/14.1#3** wzór: zniszczenie limfocytów T pomocniczych
  - AI: wskazanie, że HIV niszczy limfocyty T pomocnicze (CD4+); osłabienie odporności komórkowej; brak kontroli nad prątkami i ich namnażanie (reaktywacja gruźlicy)
- **chemia/2026-maj/24#3** wzór: uzasadnienie (kierujący wpływ grupy –NO₂)
  - AI: uzasadnienie: grupa –NO₂ jest podstawnikiem II rzędu i kieruje kolejny podstawnik (Cl) w położenie meta; wskazanie, że –Cl kieruje w orto/para, więc projekt 1 nie daje produktu meta
- **chemia/2026-maj/24#2** wzór: projekt 2: –NO₂ kieruje w meta, –Cl w orto/para
  - AI: Wskazanie projektu 2 jako prowadzącego do produktu meta; Informacja, że grupa –NO₂ kieruje kolejny podstawnik w położenie meta; Informacja, że –Cl kieruje w położenie orto/para, więc chlorowanie jako pierwszy etap nie da produktu meta
- **chemia/2015-maj-f2015/5.1#2** wzór: hybrydyzacja sp²
  - AI: Poprawna hybrydyzacja atomu siarki: sp² (trzy wiązania σ, brak wolnej pary elektronowej na S)
- **chemia/2016-maj-f2015/24.2#2** wzór: A – kwas propanowy
  - AI: Poprawna nazwa produktu A: kwas propanowy (uczeń podał propanal, który jest substratem lub produktem pośrednim, a nie produktem utleniania)
- **chemia/2017-maj-f2015/1.3#2** wzór: tlenek na maksymalnym stopniu utlenienia: CrO₃
  - AI: Poprawny wzór tlenku Z na maksymalnym stopniu utlenienia: CrO₃ (zamiast Cr₂O₃)
- **chemia/2026-czerwiec/11.2#2** wzór: Cp liczone tylko z rozpuszczonej soli (30 g) – ok. 16,7%
  - AI: Obliczenie masy soli rozpuszczonej w 150 g wody: 30 g (reszta 40 g to osad); Poprawna masa roztworu: 180 g; Poprawny wynik Cp ≈ 16,7%
- **chemia/2026-czerwiec/11.2#3** wzór: roztwór nasycony; Cp ≈ 16,7%
  - AI: Wniosek: roztwór nasycony z osadem (w 150 g wody rozpuszcza się tylko 30 g soli); Poprawna masa substancji rozpuszczonej: 30 g; Poprawna masa roztworu: 180 g; Wynik Cp ≈ 16,7%
- **chemia/2025-maj/13#3** wzór: metoda: bilans stężeń z warunku spadku ciśnienia; Kc ≈ 14,8
  - AI: równanie reakcji N₂ + 3H₂ ⇌ 2NH₃; bilans stężeń w stanie równowagi z użyciem x (spadek liczby moli/ciśnienia do 75%); wyznaczenie stężeń równowagowych N₂, H₂, NH₃; wyrażenie na Kc i poprawne podstawienie; wynik ok. 14,8 (z uwzględnieniem jednostki wg zasad)
- **chemia/2025-maj/13#2** wzór: błędne wyrażenie na Kc (brak potęg) – błąd metody, wynik ok. 14,8
  - AI: Poprawne wyrażenie na stałą równowagi: Kc = [NH₃]² / ([N₂]·[H₂]³); Prawidłowy wynik liczbowy Kc ≈ 14,8
- **chemia/2022-grudzien/8#1** wzór: obliczenia (metoda)
  - AI: równania reakcji Mg i Al z HCl; obliczenie ilości wodoru z mieszaniny Mg i Cu (Cu nie reaguje); obliczenie masy mieszaniny Mg + Cu; zapisanie, że masa Al + Ag jest taka sama i ilość H2 jest równa; obliczenie masy Al i jej procentu w mieszaninie z Ag
- **geografia/2026-maj/6.1#2** wzór: naprzemianległe piaskowce i łupki; łupki nasiąknięte wodą jako powierzchnia poślizgu
  - AI: Wskazanie naprzemianległego układu piaskowców i łupków; Rola łupków: nasiąkają wodą i tworzą śliską powierzchnię poślizgu; Nachylenie warstw sprzyjające zsuwaniu się po stoku
- **geografia/2026-maj/10.1#2** wzór: wyjaśnienie dla stacji B (strefa zbieżności, deszcze zenitalne)
  - AI: Wyjaśnienie większych opadów na stacji B: położenie w głębi lądu i latem dotarcie strefy zbieżności z deszczami zenitalnymi; Mechanizm działania zimnego prądu: chłodzi powietrze, stabilizuje je i hamuje parowanie oraz konwekcję; Nazwa prądu (Benguelski) – nieobowiązkowa, ale wzmacnia odpowiedź
- **geografia/2026-maj/6.1#3** wzór: rola łupków / wody jako powierzchni poślizgu
  - AI: wskazanie naprzemianległości przepuszczalnych piaskowców i nieprzepuszczalnych łupków; wyjaśnienie, że łupki nasiąkają wodą i tworzą śliską powierzchnię poślizgu; wskazanie, że nachylone warstwy mogą zsuwać się po stoku
- **geografia/2026-maj/10.1#3** wzór: zimny prąd przy A; deszcze zenitalne przy B
  - AI: wpływ zimnego prądu Benguelskiego na stacji A (chłodzenie powietrza, hamowanie parowania, mało opadów); wyjaśnienie wysokich opadów na stacji B: latem dociera strefa zbieżności z deszczami zenitalnymi; poprawne określenie, że na stacji A opadów jest mniej niż na B; usunięcie błędnego uogólnienia, że wysokość n.p.m. zawsze zmniejsza opady
- **geografia/2024-grudzien/10#2** wzór: uwarunkowanie astronomiczne – siła Coriolisa
  - AI: uwarunkowanie astronomiczne: ruch obrotowy Ziemi / siła Coriolisa; odchylenie wiatru w prawo na półkuli północnej i w lewo na południowej (pasaty NE i SE)
- **geografia/2023-czerwiec/1.2#2** wzór: wyrównywanie brzegu przez fale i prąd przybrzeżny (pływy na Bałtyku są znikome)
  - AI: Błędny czynnik: pływy zamiast falowania i prądu przybrzeżnego wyrównujących brzeg od strony morza; Brak wskazania prądu przybrzeżnego (wzdłużbrzegowego)
- **geografia/2024-grudzien/10#3** wzór: kierunek: od wyżu do niżu
  - AI: Poprawny kierunek barycznego przemieszczania powietrza: od wyżów zwrotnikowych do niżu równikowego; Wskazanie odchylenia: na półkuli północnej w prawo, na południowej w lewo (siła Coriolisa)
- **geografia/2024-czerwiec/28#2** wzór: druga cecha (np. wysokie opady, duże spadki rzek)
  - AI: druga cecha środowiska (np. wysokie opady lub duże spadki rzek na krawędziach wyżyn); doprecyzowanie, że rzeki mają duże przepływy i są zasobne w wodę
- **geografia/2024-grudzien/30#2** wzór: szybki rozwój gospodarek wschodzących
  - AI: Wskazanie szybkiego rozwoju gospodarczego krajów wschodzących (Chiny, Indie); Wskazanie przenoszenia produkcji do tych krajów; Odniesienie do wolniejszego wzrostu PKB w G7
- **historia/2025-maj/4#2** wzór: B – benedyktyni
  - AI: B – benedyktyni (podano błędnie cystersów)
- **historia/2025-maj/4#3** wzór: A – franciszkanie; B – benedyktyni
  - AI: A – franciszkanie (zamiast dominikanów); B – benedyktyni (zamiast cystersów)
- **geografia/2026-styczen/24#2** wzór: Australia: suchy klimat → przewaga pastwisk
  - AI: Australia: suchy klimat w większości kraju, który ogranicza uprawy; Australia: dominacja pastwisk (np. wypas owiec), a uprawy tylko na SE/w strefach z większą ilością opadów
- **historia/2026-maj/18.2#2** wzór: uzasadnienie: Wersal 1919 vs Poczdam 1945
  - AI: wskazanie, że znaczek upamiętnia traktat wersalski (1919); wskazanie, że dokument pochodzi z konferencji poczdamskiej (1945); odwołanie do treści dokumentu, np. granica na Odrze, Gdańsk, część Prus Wschodnich pod administracją Polski
- **historia/2026-maj/18.2#3** wzór: dokument dotyczy konferencji poczdamskiej
  - AI: Poprawne wskazanie konferencji poczdamskiej (1945) zamiast jałtańskiej; Odwołanie do treści dokumentu (granica na Odrze, Gdańsk, część Prus Wschodnich pod administracją Polski)
- **historia/2024-maj/24#2** wzór: mapa: Czechosłowacja 1968, tekst: Węgry 1956
  - AI: Poprawne rozstrzygnięcie: mapa i tekst NIE dotyczą tych samych wydarzeń; Wskazanie, że mapa przedstawia inwazję Układu Warszawskiego na Czechosłowację w 1968 r.; Wskazanie, że tekst dotyczy powstania węgierskiego z 1956 r. (Nagy, wystąpienie z Układu Warszawskiego)
- **historia/2024-grudzien/5.1#2** wzór: ekskomunika Henryka IV i Canossa
  - AI: wskazanie, że Dictatus papae głosił wyższość papieża nad władzą świecką/cesarzem; wskazanie sprzeciwu Henryka IV i jego ekskomuniki; powiązanie z wydarzeniem ze źródła 2 – upokorzeniem Henryka IV w Canossie (1077)
- **historia/2026-maj/22#2** wzór: Polska odrzuciła udział pod presją ZSRS
  - AI: Błędna informacja, że Polska nie została zaproszona (w rzeczywistości odrzuciła plan pod presją ZSRS); Brak wskazania Czechosłowacji, która również odrzuciła plan; Brak odwołania do krajów pozaeuropejskich z wykresu (Chiny, Filipiny, Etiopia); Brak informacji, że plan Marshalla dotyczył tylko Europy
- **historia/2024-grudzien/4#2** wzór: oba – Bolesław Chrobry
  - AI: Poprawne rozstrzygnięcie: oba źródła dotyczą tego samego władcy, Bolesława Chrobrego; Uzasadnienie z odwołaniem do źródła 1: syn poganina i chrześcijanki, wyniesiony przez cesarza; Uzasadnienie z odwołaniem do źródła 2: zjazd gnieźnieński, arcybiskupstwo dla Radzima, korona od Ottona III
- **historia/2026-czerwiec/22#2** wzór: argument dotyczący drugiego fragmentu (abdykacja Wilhelma II / rewolucja w Niemczech)
  - AI: Drugi argument: abdykacja Wilhelma II i rewolucja w Niemczech (9 XI 1918) lub zakończenie wojny; Konkretne wydarzenie zamiast ogólnika o odzyskaniu niepodległości (np. Rząd Tymczasowy w Lublinie); Odniesienie do treści obu fragmentów źródłowych
- **wos/2024-maj/17.4#3** wzór: wskazanie ETPC (Rada Europy)
  - AI: Wskazanie właściwej instytucji spoza systemu UE (Europejski Trybunał Praw Człowieka); Uzasadnienie, że ETPC należy do systemu Rady Europy; Usunięcie błędnego twierdzenia o TSUE
- **wos/2026-maj/16.2#2** wzór: pełna nazwa (polecenie wymaga pełnej nazwy)
  - AI: Pełna nazwa: Organizacja Narodów Zjednoczonych (zamiast samego skrótu ONZ)
- **wos/2024-maj/17.4#2** wzór: ETPC – Rada Europy
  - AI: Wskazanie, że ETPC (Europejski Trybunał Praw Człowieka) jest instytucją Rady Europy; Poprawne uzasadnienie – błędnie przypisano ETPC do ONZ
- **wos/2024-maj/14.2#2** wzór: Kodeks cywilny
  - AI: Poprawna nazwa kodeksu: Kodeks cywilny
- **wos/2026-maj/16.2#3** wzór: Organizacja Narodów Zjednoczonych
  - AI: Poprawna organizacja: Organizacja Narodów Zjednoczonych; Pełna polska nazwa zamiast skrótu
- **wos/2026-czerwiec/13.2#2** wzór: uzasadnienie z nazwą organu (NIK)
  - AI: nazwa organu: Najwyższa Izba Kontroli; odwołanie do przepisu Konstytucji (np. sposób powołania Prezesa NIK); odwołanie do tekstu opisującego działania NIK; wskazanie, że przepis dotyczy Prezesa NIK jako osoby stojącej na czele organu
- **wos/2024-maj/16.2#2** wzór: tak – rezolucja RB ONZ
  - AI: Poprawne rozstrzygnięcie: Tak, operacja miała mandat ONZ; Uzasadnienie odwołujące się do rezolucji Rady Bezpieczeństwa ONZ
- **wos/2023-maj/12.2#2** wzór: wydatki > dochody → deficyt
  - AI: Poprawne rozstrzygnięcie: Tak, deficyt jest założony; Uzasadnienie odwołujące się do dokumentu: planowane wydatki są wyższe niż dochody budżetowe
- **wos/2023-maj/10.1#2** wzór: 2. USA
  - AI: Poprawna nazwa państwa 2: Stany Zjednoczone (Ameryki) / USA; Wielka Brytania jest błędną odpowiedzią
- **wos/2025-czerwiec/3.2#2** wzór: uzasadnienie: mała grupa pierwotna, nacisk na zgodność z normami
  - AI: Wyjaśnienie, że wpływ normatywny polega na skłanianiu jednostki do zachowań zgodnych z oczekiwaniami grupy; Wskazanie, że rodzina jest małą grupą pierwotną, w której presja na zgodność jest silna; Odniesienie do obu tekstów źródłowych