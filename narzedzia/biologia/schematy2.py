# Schematy biologii — porcja 2: procesy i cykle (umiejętności, biochemia, metabolizm, podziały, genetyka molekularna).
S = {}

S['b-metodologia'] = [
    dict(typ='proces', tytul='Etapy metody naukowej',
         kroki=[('Obserwacja', 'zauważenie zjawiska'), ('Problem badawczy', 'pytanie, na które szukamy odpowiedzi'),
                ('Hipoteza', 'przypuszczalna odpowiedź, którą da się sprawdzić'), ('Planowanie doświadczenia', 'próba badawcza i kontrolna, jedna zmienna'),
                ('Przeprowadzenie doświadczenia i zebranie wyników'), ('Analiza wyników'), ('Wniosek', 'potwierdzenie lub odrzucenie hipotezy')],
         uwaga='Problem badawczy zapisuje się jako pytanie, hipotezę — jako zdanie oznajmujące. Wniosek musi odnosić się do hipotezy i wynikać z wyników.'),
    dict(typ='proces', tytul='Planowanie doświadczenia — krok po kroku',
         kroki=[('Ustal zmienną niezależną', 'to, co badacz zmienia'), ('Ustal zmienną zależną', 'to, co mierzymy'),
                ('Ustal zmienne kontrolowane', 'warunki jednakowe we wszystkich próbach'), ('Zaplanuj próbę kontrolną', 'bez działania badanego czynnika'),
                ('Zaplanuj powtórzenia', 'kilka prób w każdym wariancie'), ('Określ sposób pomiaru i zapisu wyników')],
         uwaga='Najczęstszy błąd na maturze: próba kontrolna różni się od badawczej więcej niż jednym czynnikiem.'),
]

S['b-wykresy'] = [
    dict(typ='proces', tytul='Rysowanie wykresu na maturze',
         kroki=[('Wybierz typ wykresu', 'liniowy — zmienna ciągła, słupkowy — kategorie'), ('Zmienna niezależna na osi X'),
                ('Zmienna zależna na osi Y'), ('Opisz osie z jednostkami'), ('Dobierz skalę', 'równe odstępy, cały zakres danych'),
                ('Nanieś punkty lub słupki'), ('Dodaj legendę, jeśli jest kilka serii')],
         uwaga='Brak jednostek lub nierówna skala to najczęstsze powody utraty punktu za wykres.'),
]

S['b-enzymy'] = [
    dict(typ='cykl', tytul='Cykl katalityczny enzymu',
         kroki=[('Wolny enzym z centrum aktywnym'), ('Przyłączenie substratu', 'powstaje kompleks enzym–substrat'),
                ('Dopasowanie indukowane', 'enzym zmienia nieco kształt'), ('Przekształcenie substratu w produkt'),
                ('Uwolnienie produktu', 'enzym jest gotowy do kolejnej reakcji')],
         uwaga='Enzym nie zużywa się w reakcji. Model „ręki i rękawiczki” (dopasowanie indukowane) jest dokładniejszy niż model „klucza i zamka”.'),
]

S['b-atp'] = [
    dict(typ='cykl', tytul='Cykl ATP–ADP',
         kroki=[('ATP', 'nośnik energii w komórce'), ('Hydroliza ATP', 'uwolnienie energii do pracy komórki'),
                ('ADP + fosforan'), ('Fosforylacja ADP', 'energia z oddychania lub fotosyntezy')],
         uwaga='Fosforylacja substratowa (glikoliza, cykl Krebsa) i oksydacyjna (łańcuch oddechowy) to dwa sposoby odtwarzania ATP.'),
]

S['b-fotosynteza'] = [
    dict(typ='proces', tytul='Faza zależna od światła',
         kroki=[('Absorpcja światła przez barwniki fotosystemów'), ('Wzbudzenie elektronu w centrum reakcji'),
                ('Fotoliza wody', 'w fotosystemie II: powstają O₂, H⁺ i elektrony'), ('Transport elektronów w błonie tylakoidu', 'przez przenośniki do fotosystemu I'),
                ('Gradient protonów i synteza ATP', 'fotofosforylacja'), ('Redukcja NADP⁺ do NADPH')],
         uwaga='Tlen z fotosyntezy pochodzi z wody, nie z CO₂ — dowodzą tego badania z izotopem ¹⁸O.'),
    dict(typ='cykl', tytul='Cykl Calvina',
         kroki=[('Karboksylacja', 'RuBisCO przyłącza CO₂ do RuBP'), ('Powstaje 3-fosfoglicerynian (PGA)'),
                ('Redukcja do aldehydu 3-fosfoglicerynowego', 'zużycie ATP i NADPH'), ('Część aldehydu — na syntezę glukozy'),
                ('Regeneracja RuBP', 'zużycie ATP')],
         uwaga='Cykl Calvina nie wymaga bezpośrednio światła, ale zatrzymuje się w ciemności, bo brakuje ATP i NADPH z fazy jasnej.'),
]

S['b-oddychanie'] = [
    dict(typ='proces', tytul='Oddychanie tlenowe — etapy',
         kroki=[('Glikoliza', 'cytozol: glukoza → 2 pirogroniany, 2 ATP netto'), ('Reakcja pomostowa', 'macierz: pirogronian → acetylo-CoA + CO₂'),
                ('Cykl Krebsa', 'macierz: CO₂, NADH, FADH₂, ATP'), ('Łańcuch oddechowy', 'błona wewnętrzna: transport elektronów na O₂'),
                ('Fosforylacja oksydacyjna', 'syntaza ATP, większość ATP')],
         uwaga='CO₂ powstaje w reakcji pomostowej i cyklu Krebsa, woda — na końcu łańcucha oddechowego.'),
    dict(typ='proces', tytul='Glikoliza — najważniejsze etapy',
         kroki=[('Glukoza'), ('Fosforylacja glukozy', 'zużycie 2 ATP'), ('Rozpad na dwie cząsteczki aldehydu 3-fosfoglicerynowego'),
                ('Utlenienie i redukcja NAD⁺ do NADH'), ('Fosforylacja substratowa', 'powstają 4 ATP'), ('2 cząsteczki pirogronianu')],
         uwaga='Bilans glikolizy: 2 ATP netto i 2 NADH. Zachodzi u wszystkich organizmów — także w warunkach beztlenowych.'),
    dict(typ='cykl', tytul='Cykl Krebsa',
         kroki=[('Acetylo-CoA łączy się ze szczawiooctanem'), ('Powstaje cytrynian (6C)'),
                ('Dekarboksylacje oksydacyjne', 'uwolnienie 2 CO₂, powstaje NADH'), ('Fosforylacja substratowa', '1 ATP (GTP)'),
                ('Utlenienie z redukcją FAD i NAD⁺'), ('Odtworzenie szczawiooctanu')],
         uwaga='Na jedną glukozę przypadają dwa obroty cyklu Krebsa.'),
    dict(typ='proces', tytul='Łańcuch oddechowy i fosforylacja oksydacyjna',
         kroki=[('NADH i FADH₂ oddają elektrony przenośnikom'), ('Elektrony przechodzą przez kompleksy w błonie wewnętrznej'),
                ('Pompowanie H⁺ do przestrzeni międzybłonowej'), ('Tlen przyjmuje elektrony i H⁺ — powstaje woda'),
                ('Powrót H⁺ przez syntazę ATP do macierzy'), ('Synteza ATP z ADP i fosforanu')],
         uwaga='Cyjanek blokuje przekazanie elektronów na tlen — staje cały łańcuch i synteza ATP.'),
]

S['b-fermentacje'] = [
    dict(typ='proces', tytul='Fermentacja alkoholowa',
         kroki=[('Glikoliza', 'glukoza → 2 pirogroniany, 2 ATP, 2 NADH'), ('Dekarboksylacja pirogronianu', 'uwolnienie CO₂, powstaje aldehyd octowy'),
                ('Redukcja aldehydu octowego do etanolu', 'NADH oddaje wodór'), ('Odtworzenie NAD⁺ dla glikolizy')],
         uwaga='Celem etapów po glikolizie jest odzyskanie NAD⁺ — bez tego glikoliza by się zatrzymała.'),
    dict(typ='proces', tytul='Fermentacja mleczanowa',
         kroki=[('Glikoliza', 'glukoza → 2 pirogroniany, 2 ATP, 2 NADH'), ('Redukcja pirogronianu do mleczanu', 'NADH oddaje wodór'),
                ('Odtworzenie NAD⁺ dla glikolizy'), ('Mleczan transportowany do wątroby', 'u człowieka — przekształcany w glukozę')],
         uwaga='W fermentacji mleczanowej nie powstaje CO₂ — tym różni się od alkoholowej.'),
]

S['b-cykl'] = [
    dict(typ='cykl', tytul='Cykl komórkowy',
         kroki=[('Faza G₁', 'wzrost komórki, synteza białek'), ('Punkt kontrolny G₁/S'), ('Faza S', 'replikacja DNA'),
                ('Faza G₂', 'przygotowanie do podziału'), ('Punkt kontrolny G₂/M'), ('Mitoza'), ('Cytokineza')],
         uwaga='Ilość DNA podwaja się w fazie S (z 2c do 4c), ale liczba chromosomów (2n) się nie zmienia.'),
]

S['b-replikacja'] = [
    dict(typ='proces', tytul='Replikacja DNA',
         kroki=[('Rozpoznanie miejsca startu (ori)'), ('Rozplecenie helisy przez helikazę'), ('Stabilizacja nici przez białka SSB'),
                ('Synteza starterów RNA przez prymazę'), ('Wydłużanie nici przez polimerazę DNA', 'w kierunku 5′→3′'),
                ('Usunięcie starterów i uzupełnienie luk'), ('Łączenie fragmentów Okazakiego przez ligazę')],
         uwaga='Polimeraza DNA dobudowuje nukleotydy tylko do końca 3′ — stąd nić opóźniona i fragmenty Okazakiego.'),
]

S['b-mitoza-mejoza'] = [
    dict(typ='proces', tytul='Fazy mitozy',
         kroki=[('Profaza', 'kondensacja chromosomów, zanik jąderka, tworzenie wrzeciona'), ('Prometafaza', 'rozpad otoczki jądrowej, przyłączanie włókien do kinetochorów'),
                ('Metafaza', 'chromosomy w płaszczyźnie równikowej'), ('Anafaza', 'rozejście chromatyd siostrzanych do biegunów'),
                ('Telofaza', 'despiralizacja chromosomów, odtworzenie otoczek jądrowych')],
         uwaga='Liczbę chromosomów najłatwiej policzyć w metafazie. W anafazie chromatydy stają się chromosomami potomnymi.'),
    dict(typ='proces', tytul='Mejoza — przebieg',
         kroki=[('Profaza I', 'koniugacja homologów, biwalenty, crossing-over'), ('Metafaza I', 'biwalenty w płaszczyźnie równikowej'),
                ('Anafaza I', 'rozejście chromosomów homologicznych — redukcja liczby'), ('Telofaza I i cytokineza', '2 komórki haploidalne'),
                ('Profaza II i metafaza II', 'bez replikacji DNA'), ('Anafaza II', 'rozejście chromatyd siostrzanych'),
                ('Telofaza II', '4 komórki haploidalne, zróżnicowane genetycznie')],
         uwaga='Źródła zmienności w mejozie: crossing-over (profaza I) i niezależna segregacja chromosomów (anafaza I).'),
    dict(typ='proces', tytul='Spermatogeneza',
         kroki=[('Spermatogonium (2n)', 'podziały mitotyczne'), ('Spermatocyt I rzędu (2n)'), ('Mejoza I'),
                ('2 spermatocyty II rzędu (n)'), ('Mejoza II'), ('4 spermatydy (n)'), ('Spermiogeneza', 'dojrzewanie w plemniki')],
         uwaga='Z jednego spermatocytu I rzędu powstają 4 plemniki, a z oocytu I rzędu — 1 komórka jajowa i ciałka kierunkowe.'),
    dict(typ='proces', tytul='Oogeneza',
         kroki=[('Oogonium (2n)', 'podziały mitotyczne przed urodzeniem'), ('Oocyt I rzędu', 'zatrzymany w profazie I do dojrzewania płciowego'),
                ('Mejoza I przed owulacją', 'oocyt II rzędu + I ciałko kierunkowe'), ('Owulacja', 'oocyt II zatrzymany w metafazie II'),
                ('Zapłodnienie uruchamia mejozę II'), ('Komórka jajowa i II ciałko kierunkowe')],
         uwaga='Nierówny podział cytoplazmy zapewnia komórce jajowej zapas substancji odżywczych dla zarodka.'),
]

S['b-apoptoza'] = [
    dict(typ='proces', tytul='Apoptoza — przebieg',
         kroki=[('Sygnał śmierci', 'zewnętrzny (receptory) lub wewnętrzny (uszkodzenie DNA)'), ('Uwolnienie cytochromu c z mitochondriów'),
                ('Aktywacja kaspaz'), ('Fragmentacja DNA i kondensacja chromatyny'), ('Obkurczanie komórki i pączkowanie błony'),
                ('Powstanie ciałek apoptotycznych'), ('Fagocytoza bez stanu zapalnego')],
         uwaga='Apoptoza nie wywołuje stanu zapalnego — w przeciwieństwie do martwicy (nekrozy), w której komórka pęka.'),
]

S['b-transkrypcja'] = [
    dict(typ='proces', tytul='Transkrypcja u eukariontów',
         kroki=[('Przyłączenie czynników transkrypcyjnych do promotora'), ('Przyłączenie polimerazy RNA'),
                ('Rozplecenie fragmentu DNA'), ('Synteza pre-mRNA na nici matrycowej', 'w kierunku 5′→3′'),
                ('Terminacja i odłączenie polimerazy')],
         uwaga='Polimeraza RNA nie potrzebuje startera — w przeciwieństwie do polimerazy DNA.'),
    dict(typ='proces', tytul='Obróbka pre-mRNA',
         kroki=[('Dodanie czapeczki na końcu 5′', 'ochrona i rozpoznanie przez rybosom'), ('Dodanie ogona poli-A na końcu 3′', 'ochrona przed degradacją'),
                ('Splicing — wycięcie intronów', 'spliceosom'), ('Łączenie eksonów', 'możliwy alternatywny splicing'),
                ('Transport dojrzałego mRNA do cytoplazmy')],
         uwaga='Dzięki alternatywnemu splicingowi jeden gen może kodować kilka różnych białek.'),
]

S['b-translacja'] = [
    dict(typ='proces', tytul='Translacja — etapy',
         kroki=[('Aktywacja aminokwasów', 'przyłączenie do tRNA, zużycie ATP'), ('Inicjacja', 'mała podjednostka + mRNA + tRNA z metioniną na kodonie AUG'),
                ('Przyłączenie dużej podjednostki rybosomu'), ('Elongacja', 'kolejne aminoacylo-tRNA, wiązania peptydowe'),
                ('Translokacja rybosomu o jeden kodon'), ('Terminacja na kodonie STOP', 'czynniki uwalniające'), ('Uwolnienie polipeptydu')],
         uwaga='Kodony STOP: UAA, UAG, UGA — nie mają odpowiadającego im tRNA.'),
]

S['b-regulacja'] = [
    dict(typ='proces', tytul='Operon laktozowy — indukcja',
         kroki=[('Brak laktozy: represor związany z operatorem', 'geny nieaktywne'), ('Pojawienie się laktozy w środowisku'),
                ('Allolaktoza wiąże się z represorem'), ('Represor odłącza się od operatora'),
                ('Polimeraza RNA transkrybuje geny struktury'), ('Synteza enzymów rozkładających laktozę')],
         uwaga='Operon lac jest indukowany (włączany substratem), operon tryptofanowy — represjonowany (wyłączany produktem).'),
]

S['b-gen'] = [
    dict(typ='proces', tytul='Od genu do cechy',
         kroki=[('Gen w DNA'), ('Transkrypcja', 'pre-mRNA'), ('Obróbka', 'dojrzałe mRNA'), ('Translacja', 'łańcuch polipeptydowy'),
                ('Fałdowanie i modyfikacje białka'), ('Funkcja białka', 'np. enzym'), ('Cecha organizmu')],
         uwaga='Mutacja w genie może zmienić białko, a przez to cechę — to typowy łańcuch przyczynowy w zadaniach z genetyki.'),
]
