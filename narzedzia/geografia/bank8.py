# Bank zadań autorskich — geografia, część 8: Polska (wody, ludność), rzeźba, lodowce, GIS, świat. Dane autorskie.
BANK = {'polska-gospodarka': [
 B('Ubytek ludności',
   'Tekst autorski. Liczba ludności Polski wynosiła 38,5 mln w 2011 r. i 37,5 mln w 2024 r.',
   T('oblicz', 1, 'Oblicz wskaźnik dynamiki liczby ludności (2011 = 100%). Wynik zaokrąglij do 0,1%.', '97,4%', '37,5 / 38,5 × 100.'),
   T('podaj', 2, 'Podaj dwie przyczyny spadku liczby ludności Polski.', 'Ujemny przyrost naturalny (niska dzietność, starzenie się) oraz emigracja zagraniczna.', 'Po jednej z demografii i migracji.')),
], 'polska-przyroda': [
 B('Spadek Wisły',
   'Tekst autorski. Wisła ma źródła na wysokości ok. 1100 m n.p.m. i długość ok. 1050 km; uchodzi do Bałtyku.',
   T('oblicz', 1, 'Oblicz średni spadek Wisły w promilach. Wynik zaokrąglij do 0,01‰.', 'ok. 1,05‰', '1100 m / 1 050 000 m × 1000.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego spadek Wisły w górnym biegu jest dużo większy niż w dolnym.', 'W górnym biegu rzeka płynie w górach (Beskidy), gdzie różnice wysokości są duże na krótkim odcinku; w dolnym — przez niziny.', 'Profil podłużny.')),
 B('Dorzecze Wisły',
   'Tekst autorski. Powierzchnia Polski: 312,7 tys. km². Powierzchnia dorzecza Wisły w granicach Polski: 168,7 tys. km².',
   T('oblicz', 1, 'Oblicz, jaki odsetek powierzchni Polski zajmuje dorzecze Wisły.', 'ok. 54%', '168,7 / 312,7 × 100 ≈ 53,9.'),
   T('podaj', 1, 'Podaj dwa prawe dopływy Wisły.', 'Np. San, Bug (przez Narew), Dunajec, Wieprz, Narew.', 'Asymetria dorzecza.')),
], 'litosfera': [
 B('Cofający się wodospad',
   'Tekst autorski. Wodospad cofa się w górę doliny średnio o 1 m na rok. Od jego pierwotnego położenia dzieli go obecnie 11 km.',
   T('oblicz', 1, 'Oblicz, ile lat temu wodospad zaczął się cofać.', 'ok. 11 000 lat', '11 000 m / 1 m/rok.'),
   T('podaj', 1, 'Podaj nazwę procesu.', 'erozja wsteczna', 'Np. Niagara.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego wodospad się cofa.', 'Woda podmywa miękkie skały pod twardą warstwą progu; nawis się załamuje i próg przesuwa się w górę rzeki.', 'Podcinanie.')),
], 'hydrosfera': [
 B('Kurczący się lodowiec',
   'Tekst autorski. Długość lodowca alpejskiego zmniejszyła się z 5,2 km w 1974 r. do 4,1 km w 2024 r.',
   T('oblicz', 1, 'Oblicz średnie tempo cofania się czoła lodowca w metrach na rok.', '22 m/rok', '1100 m / 50 lat.'),
   T('podaj', 2, 'Podaj dwa skutki zaniku lodowców górskich.', 'Np. zmniejszenie zasobów wody pitnej i do nawadniania, mniejsze przepływy rzek latem, wzrost poziomu morza, zagrożenie lawinami błotnymi.', 'Wystarczą dwa.')),
], 'mapa': [
 B('Analiza buforowa',
   'Tekst autorski. Planowana droga ekspresowa ma odcinek prosty długości 4 km. W GIS wyznaczono bufor 500 m po obu stronach drogi.',
   T('oblicz', 1, 'Oblicz powierzchnię bufora w hektarach (pomiń zaokrąglenia na końcach odcinka).', '400 ha', '4 km × 1 km = 4 km².'),
   T('podaj', 1, 'Podaj przykład zastosowania takiej analizy.', 'Np. ocena, ile budynków lub obszarów chronionych znajdzie się w strefie hałasu drogi.', 'Planowanie przestrzenne.')),
], 'swiat': [
 B('Polska w Unii Europejskiej',
   'Tekst autorski. Unię Europejską zamieszkuje ok. 450 mln osób, Polskę — 37,5 mln.',
   T('oblicz', 1, 'Oblicz udział ludności Polski w ludności UE. Wynik zaokrąglij do 0,1%.', 'ok. 8,3%', '37,5 / 450 × 100.'),
   T('podaj', 2, 'Podaj dwie korzyści gospodarcze członkostwa Polski w UE.', 'Np. fundusze unijne na infrastrukturę, wspólny rynek i swoboda handlu, napływ inwestycji, swoboda pracy.', 'Wystarczą dwie.')),
 B('Państwa w Arktyce',
   'Tekst autorski. Topnienie lodu morskiego otwiera Północną Drogę Morską wzdłuż wybrzeży Rosji.',
   T('wyjasnij', 2, 'Wyjaśnij, dlaczego Arktyka staje się obszarem rywalizacji państw.', 'Krótsze szlaki żeglugowe między Europą a Azją oraz dostęp do złóż ropy, gazu i surowców pod dnem morskim po ustąpieniu lodu.', 'Geopolityka.'),
   T('podaj', 1, 'Podaj jedno zagrożenie środowiskowe wynikające z tych zmian.', 'Np. ryzyko wycieków ropy w trudnych warunkach, zakłócenie ekosystemów, zanieczyszczenie przez statki.', 'Jedno.')),
], 'umiejetnosci': [
 B('Odczyt z wykresu kołowego',
   'Tekst autorski. Na wykresie kołowym struktury użytkowania ziemi w gminie użytki rolne zajmują wycinek o kącie 216°, a lasy — 90°.',
   T('oblicz', 1, 'Oblicz udział procentowy użytków rolnych i lasów.', 'użytki rolne 60%, lasy 25%', '216/360 i 90/360.'),
   T('oblicz', 1, 'Oblicz powierzchnię lasów, jeśli gmina ma 120 km².', '30 km²', '25% × 120.')),
]}
