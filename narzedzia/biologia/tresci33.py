# Treści kursu biologii — porcja 33: genetyka, genetyka molekularna, biotechnologia, ewolucja i ekologia.
T = {}

T['b-gen'] = dict(F=[
 ('Geny nakładające się', 'U niektórych organizmów (np. wirusów) ten sam fragment DNA koduje różne białka w różnych ramkach odczytu — oszczędność genomu.'),
 ('Rodzina genów', 'Grupa podobnych genów powstałych przez duplikację genu wyjściowego (np. geny globin).'),
], Q=[
 ('Rodziny genów (np. globin) powstały głównie przez:', ['delecje', '*duplikacje genów', 'translokacje', 'transkrypcję odwrotną'], 'Powielenie i zróżnicowanie.'),
])

T['b-transkrypcja'] = dict(F=[
 ('Rybozymy', 'Cząsteczki RNA o aktywności katalitycznej (np. rRNA w rybosomie, RNA spliceosomu) — argument za hipotezą świata RNA.'),
 ('Transkrypcja a rozmiar genu', 'U eukariontów pre-mRNA może być wielokrotnie dłuższy od dojrzałego mRNA — introny stanowią często większość genu.'),
], Q=[
 ('Rybozym to:', ['białkowy enzym zawarty w rybosomie', '*cząsteczka RNA o właściwościach katalitycznych', 'rodzaj tRNA przenoszący aminokwasy', 'białkowy enzym trawiący cząsteczki RNA'], 'Kataliza przez RNA.'),
])

T['b-regulacja'] = dict(F=[
 ('Regulacja ekspresji a środowisko', 'Ekspresję genów zmieniają czynniki zewnętrzne — np. światło włącza geny białek fotosyntezy, temperatura — geny białek szoku cieplnego.'),
 ('Komórki macierzyste a ekspresja genów', 'W miarę różnicowania komórki trwale wyciszają część genów (zmiany epigenetyczne) i tracą wszechstronność.'),
], Q=[
 ('Wyciszenie genów w trakcie różnicowania komórek wynika głównie ze zmian:', ['sekwencji DNA', '*epigenetycznych', 'liczby chromosomów', 'kodu genetycznego'], 'Metylacja, histony.'),
])

T['b-krzyzowki'] = dict(F=[
 ('Jak odróżnić 9:3:3:1 od sprzężenia w zadaniu?', 'Przy genach niesprzężonych w krzyżówce testowej klasy są równe (1:1:1:1); przy sprzężeniu dwie klasy rodzicielskie wyraźnie przeważają.'),
 ('Wynik krzyżówki dwóch heterozygot przy dominacji niezupełnej w obu genach', '9 klas fenotypowych w F2 (każdy genotyp ma odrębny fenotyp).'),
], Q=[
 ('Ile klas fenotypów powstaje w F2 krzyżówki AaBb × AaBb, gdy oba geny wykazują dominację niezupełną?', ['4', '6', '*9', '16'], 'Każdy genotyp to fenotyp.'),
])

T['b-plec'] = dict(F=[
 ('Gen SRY', 'Gen na chromosomie Y uruchamiający rozwój jąder; jego brak (lub przeniesienie na X) zmienia rozwój płci.'),
 ('Dlaczego mężczyźni częściej są daltonistami?', 'Allel daltonizmu leży na X; mężczyzna ma jeden X, więc jeden allel recesywny wystarcza — kobieta potrzebuje dwóch.'),
], Q=[
 ('Częstość daltonizmu u mężczyzn wynosi ok. 8%. U kobiet jest:', ['taka sama', '*znacznie mniejsza (ok. 0,64%)', 'dwa razy większa', 'zawsze zerowa'], 'q² = 0,08².'),
])

T['b-rodowody'] = dict(F=[
 ('Krok po kroku — analiza rodowodu', '1) Recesywna czy dominująca? (zdrowi rodzice, chore dziecko → recesywna). 2) Sprzężona z X? (sprawdź ojców i synów, matki i córki). 3) Zapisz genotypy pewne, potem prawdopodobne.'),
], Q=[
 ('Pierwszym krokiem w analizie rodowodu jest zwykle ustalenie, czy cecha jest:', ['sprzężona z Y', '*dominująca czy recesywna', 'mitochondrialna', 'wielogenowa'], 'Podstawowa decyzja.'),
])

T['b-mutacje'] = dict(F=[
 ('Mutacje dynamiczne', 'Powiększanie się liczby powtórzeń trójek nukleotydów w kolejnych pokoleniach (np. pląsawica Huntingtona, zespół łamliwego X) — objawy wcześniejsze i silniejsze.'),
 ('Duplikacja genów a ewolucja', 'Kopia genu może mutować bez utraty pierwotnej funkcji — źródło nowych genów i funkcji.'),
], Q=[
 ('Wzrost liczby powtórzeń CAG w kolejnych pokoleniach to mutacja:', ['cicha', '*dynamiczna', 'liczbowa', 'translokacja'], 'Pląsawica Huntingtona.'),
])

T['b-choroby-genetyczne'] = dict(F=[
 ('Zespół łamliwego chromosomu X', 'Najczęstsza dziedziczna przyczyna niepełnosprawności intelektualnej; mutacja dynamiczna (powtórzenia CGG) w genie na chromosomie X.'),
 ('Choroby wieloczynnikowe', 'Warunkowane wieloma genami i środowiskiem — np. cukrzyca typu 2, nadciśnienie, rozszczep wargi, wiele nowotworów.'),
 ('Geny BRCA1 i BRCA2', 'Geny supresorowe naprawy DNA; ich mutacje znacznie zwiększają ryzyko raka piersi i jajnika.'),
], Q=[
 ('Cukrzyca typu 2 jest chorobą:', ['jednogenową recesywną', '*wieloczynnikową (geny i środowisko)', 'chromosomową', 'mitochondrialną'], 'Styl życia + predyspozycje.'),
 ('Mutacje genów BRCA1/BRCA2 zwiększają ryzyko:', ['hemofilii', '*raka piersi i jajnika', 'zespołu Downa', 'daltonizmu'], 'Geny supresorowe.'),
])

T['b-techniki'] = dict(F=[
 ('Edycja genów CRISPR — zastosowania', 'Badania funkcji genów, terapie chorób genetycznych (np. anemii sierpowatej), tworzenie odmian roślin.'),
 ('Biblioteka cDNA', 'Zbiór kopii cDNA wszystkich mRNA danej tkanki — pokazuje, które geny są w niej aktywne.'),
], Q=[
 ('Biblioteka cDNA zawiera geny:', ['całego genomu wraz z intronami', '*ulegające ekspresji w danej tkance (bez intronów)', 'wyłącznie z genomu mitochondrialnego', 'wyłącznie sekwencje niekodujące DNA'], 'Z mRNA.'),
])

T['b-gmo'] = dict(F=[
 ('Rośliny odporne na herbicydy — ryzyko', 'Nadmierne stosowanie herbicydu może prowadzić do powstania odpornych chwastów (dobór naturalny).'),
], Q=[
 ('Długotrwałe stosowanie jednego herbicydu na uprawach GMO sprzyja:', ['wyginięciu wszystkich chwastów', '*selekcji chwastów odpornych na herbicyd', 'wzrostowi plonów bez końca', 'zanikowi mutacji'], 'Dobór.'),
])

T['b-biotech-medycyna'] = dict(F=[
 ('Terapia CAR-T', 'Limfocyty T pacjenta modyfikuje się genetycznie, by rozpoznawały komórki nowotworowe, i podaje z powrotem — terapia białaczek.'),
], Q=[
 ('W terapii CAR-T modyfikuje się genetycznie:', ['erytrocyty', '*limfocyty T pacjenta', 'komórki nowotworowe', 'bakterie jelitowe'], 'Immunoterapia.'),
])

T['b-dobor'] = dict(F=[
 ('Biogeograficzne dowody ewolucji', 'Rozmieszczenie gatunków odzwierciedla historię ich powstawania — np. torbacze w Australii, endemity wysp.'),
 ('Ewolucja oporności — tempo', 'U organizmów o krótkim pokoleniu i dużej liczebności (bakterie, owady) dobór działa szybko — oporność pojawia się w latach.'),
], Q=[
 ('Występowanie torbaczy głównie w Australii to dowód ewolucji:', ['embriologiczny', '*biogeograficzny', 'molekularny', 'anatomiczny'], 'Izolacja kontynentu.'),
])

T['b-populacje-genetyka'] = dict(Q=[
 ('Jeśli 36% osobników ma fenotyp recesywny, częstość allelu dominującego wynosi:', ['0,6', '*0,4', '0,64', '0,36'], 'q = 0,6; p = 0,4.'),
 ('Przy p = 0,7 odsetek osobników o fenotypie dominującym wynosi:', ['49%', '*91%', '42%', '70%'], 'p² + 2pq = 1 − 0,09.'),
])

T['b-specjacja'] = dict(F=[
 ('Radiacja ssaków po wymarciu dinozaurów', 'Po wymarciu dinozaurów (66 mln lat temu) ssaki zajęły zwolnione nisze — szybkie powstanie wielu nowych grup.'),
 ('Pierścień gatunków', 'Szereg populacji wokół bariery, w którym sąsiednie się krzyżują, a skrajne już nie — ilustracja stopniowej specjacji.'),
], Q=[
 ('Szybkie różnicowanie się ssaków po wymarciu dinozaurów to przykład:', ['konwergencji', '*radiacji adaptacyjnej', 'dryfu', 'koewolucji'], 'Wolne nisze.'),
])

T['b-ekosystem'] = dict(F=[
 ('Las tropikalny — cechy', 'Największa różnorodność gatunkowa, piętrowa struktura, szybki obieg materii, uboga gleba (pierwiastki głównie w biomasie).'),
 ('Tundra — cechy', 'Wieczna zmarzlina, krótki okres wegetacji, mchy, porosty, karłowate krzewinki.'),
], Q=[
 ('Wieczna zmarzlina jest cechą:', ['tajgi', '*tundry', 'stepu', 'lasu liściastego'], 'Biom arktyczny.'),
])

T['b-populacje'] = dict(F=[
 ('Cykle liczebności lemingów', 'Regularne wahania (co 3–4 lata) związane z dostępnością pokarmu i presją drapieżników (np. lisy polarne, sowy śnieżne).'),
], Q=[
 ('Sowa śnieżna i leming to para:', ['konkurentów', '*drapieżnik–ofiara', 'pasożyt–żywiciel', 'mutualistów'], 'Cykle liczebności.'),
])

T['b-ochrona'] = dict(F=[
 ('Zmiany klimatu a gatunki', 'Przesuwanie się zasięgów na północ i w górę, zaburzenie terminów kwitnienia i migracji, zagrożenie gatunków o wąskich niszach.'),
], Q=[
 ('Skutkiem ocieplenia klimatu dla gatunków górskich jest:', ['poszerzanie zasięgu w dół gór', '*przesuwanie zasięgu w górę i jego kurczenie', 'brak zmian', 'wzrost liczby gatunków arktycznych'], 'Ucieczka w chłodniejsze strefy.'),
])
