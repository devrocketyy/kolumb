# Geografia — porcja 15 (dogęszczanie): umiejętności, mapa, Słońce, klimat i krajobrazy Polski, energetyka.
T = {
'g-polecenia': dict(F=[
 ('Polecenie „Porównaj”', 'Wskaż podobieństwa i/lub różnice, zawsze odnosząc oba obiekty do tej samej cechy.'),
 ('Polecenie „Oceń”', 'Wyraź opinię (np. korzystne/niekorzystne) i podaj argument.'),
 ('Polecenie „Sformułuj wniosek”', 'Uogólnienie wynikające z danych — nie przepisuj samych liczb.'),
 ('Odpowiedź z materiału źródłowego', 'Gdy polecenie mówi „na podstawie mapy/tabeli” — odpowiedź musi wynikać z tego materiału.'),
],
Q=[
 ('Polecenie „Oceń” wymaga:', ['*opinii popartej argumentem', 'samego wypisania danych', 'narysowania wykresu', 'podania definicji pojęcia'], 'Ocena + uzasadnienie.'),
 ('Wniosek z danych to:', ['*uogólnienie wynikające z danych', 'dokładne przepisanie liczb z tabeli', 'pytanie badawcze do tematu', 'definicja pojęcia z podręcznika'], 'Nie przepisuj.'),
 ('Odpowiedź „na podstawie mapy” musi:', ['*wynikać z treści tej mapy', 'pochodzić wyłącznie z pamięci', 'zawierać rysunek', 'mieć co najmniej 5 zdań'], 'Materiał źródłowy.'),
]),
'g-dane': dict(F=[
 ('Wykres liniowy', 'Pokazuje zmiany zjawiska w czasie (np. liczba ludności w latach).'),
 ('Wykres kołowy', 'Pokazuje strukturę — udział części w całości (suma 100%).'),
 ('Kartogram', 'Mapa z polami jednostek zabarwionymi według wartości względnej (np. gęstość zaludnienia).'),
 ('Kartodiagram', 'Mapa z diagramami w jednostkach — pokazuje wartości bezwzględne (np. wielkość produkcji).'),
],
Q=[
 ('Gęstość zaludnienia w województwach najlepiej przedstawić na:', ['*kartogramie', 'kartodiagramie', 'wykresie liniowym', 'mapie izarytmicznej'], 'Wartości względne.'),
 ('Udział sektorów w PKB najlepiej pokazać na wykresie:', ['*kołowym', 'liniowym', 'punktowym', 'klimatogramie'], 'Struktura.'),
 ('Wielkość produkcji w regionach pokazuje się na:', ['*kartodiagramie', 'kartogramie', 'mapie hipsometrycznej', 'profilu terenu'], 'Wartości bezwzględne.'),
]),
'g-obliczenia': dict(F=[
 ('Dynamika zmian (%)', 'Wartość z roku badanego / wartość z roku bazowego × 100%.'),
 ('Średnia roczna temperatura', 'Suma średnich miesięcznych / 12.'),
 ('Amplituda temperatury', 'Różnica między najwyższą a najniższą średnią miesięczną temperaturą.'),
 ('Gęstość zaludnienia', 'Liczba ludności / powierzchnia (os./km²).'),
],
Q=[
 ('Produkcja wzrosła z 200 do 250 tys. t. Wskaźnik dynamiki wynosi:', ['*125%', '25%', '50%', '80%'], '250/200 × 100.'),
 ('Najcieplejszy miesiąc 18°C, najzimniejszy −3°C. Amplituda roczna:', ['*21°C', '15°C', '18°C', '7,5°C'], '18 − (−3).'),
 ('Kraj 2 mln mieszkańców i 40 000 km² ma gęstość:', ['*50 os./km²', '20 os./km²', '200 os./km²', '5 os./km²'], '2 000 000 / 40 000.'),
]),
'g-poziomice': dict(F=[
 ('Cięcie poziomicowe', 'Różnica wysokości między sąsiednimi poziomicami (np. co 10 m na mapie 1:25 000).'),
 ('Punkt wysokościowy', 'Punkt z podaną wysokością bezwzględną (np. szczyt 347,5).'),
 ('Wysokość względna', 'Różnica wysokości między dwoma punktami terenu.'),
 ('Dolina na poziomicach', 'Poziomice tworzą „języki” skierowane w górę doliny (pod prąd rzeki).'),
],
Q=[
 ('Różnica wysokości między sąsiednimi poziomicami to:', ['*cięcie poziomicowe', 'przewyższenie profilu', 'wysokość bezwzględna', 'skala pionowa'], 'Np. 10 m.'),
 ('W dolinie wygięcia poziomic skierowane są:', ['*w górę doliny', 'w dół doliny', 'zawsze na północ', 'prostopadle do rzeki'], 'Pod prąd.'),
 ('Szczyt 520 m i dolina 380 m — wysokość względna szczytu nad doliną:', ['*140 m', '900 m', '380 m', '520 m'], '520 − 380.'),
]),
'g-orientacja': dict(F=[
 ('Azymut magnetyczny i geograficzny', 'Różnią się o deklinację magnetyczną; w Polsce jest ona niewielka (kilka stopni na wschód).'),
 ('Wyznaczanie północy zegarkiem', 'Wskazówkę godzinową kieruje się na Słońce; dwusieczna kąta z „12” (latem z „1”) wskazuje południe.'),
 ('Orientacja w nocy', 'Gwiazda Polarna wskazuje północ; jej wysokość nad horyzontem ≈ szerokość geograficzna.'),
 ('Kierunki pośrednie', 'NE, SE, SW, NW — azymuty 45°, 135°, 225°, 315°.'),
],
Q=[
 ('Azymut 225° to kierunek:', ['*południowo-zachodni', 'północno-wschodni', 'południowo-wschodni', 'zachodni'], 'SW.'),
 ('Wysokość Gwiazdy Polarnej nad horyzontem jest równa w przybliżeniu:', ['*szerokości geograficznej', 'długości geograficznej', 'deklinacji Słońca', 'wysokości n.p.m.'], 'Na biegunie — 90°.'),
 ('Gwiazda Polarna wskazuje kierunek:', ['*północny', 'południowy', 'wschodni', 'zachodni'], 'Półkula N.'),
]),
'g-gis': dict(F=[
 ('Warstwy GIS', 'Dane zapisane w oddzielnych warstwach (drogi, rzeki, budynki), które można nakładać i analizować.'),
 ('Bufor', 'Analiza GIS wyznaczająca strefę w określonej odległości od obiektu (np. 500 m od rzeki).'),
 ('GPS / GNSS', 'Satelitarny system określania położenia; do wyznaczenia pozycji potrzeba sygnału min. 4 satelitów.'),
 ('Ortofotomapa', 'Zdjęcie lotnicze lub satelitarne przekształcone do skali mapy.'),
],
Q=[
 ('Strefa w określonej odległości od obiektu w GIS to:', ['*bufor', 'warstwa rastrowa', 'piksel', 'legenda'], 'Analiza buforowa.'),
 ('Zdjęcie lotnicze przekształcone do skali mapy to:', ['*ortofotomapa', 'kartogram', 'mapa hipsometryczna', 'plan miasta'], 'Geoportal.'),
 ('Do wyznaczenia pozycji 3D w GPS potrzeba sygnału co najmniej:', ['*4 satelitów', '1 satelity', '2 satelitów', '10 satelitów'], 'Trzy współrzędne + czas.'),
]),
'g-slonce': dict(F=[
 ('Wysokość Słońca a nasłonecznienie', 'Im wyżej Słońce, tym mniejsza powierzchnia, na którą pada wiązka, i grubsza warstwa atmosfery mniej je osłabia.'),
 ('Górowanie po stronie północnej', 'Między zwrotnikiem Raka a równikiem w czerwcu Słońce góruje po stronie północnej nieba.'),
 ('Wysokość Słońca na biegunie N 22 VI', 'Ok. 23°27′ — przez całą dobę.'),
 ('Wzór dla półkuli N latem', 'h = 90° − φ + 23°27′ (22 VI); zimą: h = 90° − φ − 23°27′ (22 XII).'),
],
Q=[
 ('22 czerwca na biegunie północnym Słońce znajduje się na wysokości ok.:', ['*23°27′', '0°', '66°33′', '90°'], 'Przez całą dobę.'),
 ('W Krakowie (50°N) w dniu przesilenia zimowego Słońce góruje na wysokości:', ['*16°33′', '40°00′', '63°27′', '26°33′'], '90 − 50 − 23°27′.'),
 ('W czerwcu na 10°N Słońce góruje po stronie:', ['*północnej nieba', 'południowej nieba', 'wschodniej nieba', 'zachodniej nieba'], 'Słońce nad zwrotnikiem Raka.'),
]),
'g-pl-klimat': dict(F=[
 ('Najcieplejszy region Polski', 'Nizina Śląska i zachodnia Polska — najdłuższy okres wegetacyjny (ponad 220 dni).'),
 ('Najzimniejszy region nizinny', 'Pojezierze Mazurskie i Suwalszczyzna — „polski biegun zimna”.'),
 ('Najmniejsze opady w Polsce', 'Kujawy i Wielkopolska — ok. 450–500 mm rocznie (cień opadowy).'),
 ('Najwyższe opady w Polsce', 'Tatry — ponad 1500 mm rocznie (Hala Gąsienicowa, Kasprowy).'),
],
Q=[
 ('Najmniejsze opady w Polsce notuje się na:', ['*Kujawach', 'Podhalu', 'Pojezierzu Kaszubskim', 'Pogórzu Karpackim'], 'Ok. 450–500 mm.'),
 ('„Polskim biegunem zimna” nazywa się:', ['*Suwalszczyznę', 'Nizinę Śląską', 'Żuławy Wiślane', 'Wyżynę Lubelską'], 'Klimat najbardziej kontynentalny.'),
 ('Najdłuższy okres wegetacyjny w Polsce ma:', ['*Nizina Śląska', 'Pojezierze Suwalskie', 'Podhale', 'Pojezierze Mazurskie'], 'Ponad 220 dni.'),
]),
'g-pl-krajobrazy': dict(F=[
 ('Krajobraz młodoglacjalny', 'Pojezierza — świeże formy ostatniego zlodowacenia: jeziora, moreny, sandry, ozy.'),
 ('Krajobraz staroglacjalny', 'Niziny środkowej Polski — formy starszych zlodowaceń, zrównane, bez jezior.'),
 ('Krajobraz wysokogórski', 'Tatry — formy polodowcowe (kotły, żłoby), piętra roślinności, turnie.'),
 ('Krajobraz lessowy', 'Wyżyna Lubelska, Sandomierska — wąwozy, żyzne gleby, rolnictwo.'),
],
Q=[
 ('Liczne jeziora, moreny i sandry to krajobraz:', ['*młodoglacjalny', 'staroglacjalny', 'lessowy', 'krasowy'], 'Pojezierza.'),
 ('Wąwozy i żyzne gleby cechują krajobraz:', ['*lessowy', 'wydmowy', 'młodoglacjalny', 'wysokogórski'], 'Np. Kazimierz Dolny.'),
 ('Krajobraz staroglacjalny występuje głównie na:', ['*nizinach środkowej Polski', 'pojezierzach północy', 'Tatrach i Pieninach', 'wybrzeżu Bałtyku'], 'Starsze zlodowacenia.'),
]),
'g-energetyka': dict(F=[
 ('Elektrownia Bełchatów', 'Największa elektrownia na węgiel brunatny w Europie (woj. łódzkie).'),
 ('Elektrownia szczytowo-pompowa', 'Magazynuje energię: nocą pompuje wodę do górnego zbiornika, w szczycie zapotrzebowania ją spuszcza (Żarnowiec).'),
 ('Offshore na Bałtyku', 'Morskie farmy wiatrowe budowane na Ławicy Słupskiej — wiatr na morzu jest silniejszy i stabilniejszy.'),
 ('Miks energetyczny', 'Struktura źródeł wytwarzania energii w danym kraju.'),
],
Q=[
 ('Największa elektrownia na węgiel brunatny w Europie to:', ['*Bełchatów', 'Opole', 'Kozienice', 'Połaniec'], 'Woj. łódzkie.'),
 ('Elektrownia szczytowo-pompowa służy głównie do:', ['*magazynowania energii', 'spalania biomasy', 'produkcji ciepła', 'wydobycia węgla'], 'Żarnowiec, Porąbka-Żar.'),
 ('Morskie farmy wiatrowe buduje się na Bałtyku, bo wiatr na morzu jest:', ['*silniejszy i stabilniejszy', 'cieplejszy i wilgotniejszy', 'słabszy, ale stały', 'zawsze z południa'], 'Ławica Słupska.'),
]),
}
