# Schematy biologii — porcja 4: procesy i cykle (mikroorganizmy, rośliny, zwierzęta, genetyka, biotechnologia, ewolucja, ekologia).
S = {}

S['b-wirusy'] = [
    dict(typ='proces', tytul='Cykl lityczny bakteriofaga',
         kroki=[('Adsorpcja', 'przyczepienie do receptorów bakterii'), ('Wstrzyknięcie DNA faga'), ('Rozkład DNA bakterii'),
                ('Replikacja DNA faga i synteza białek kapsydu'), ('Składanie nowych wirionów'), ('Liza komórki i uwolnienie fagów')],
         uwaga='Bakteriofagi wykorzystuje się w terapii fagowej przeciw bakteriom opornym na antybiotyki.'),
    dict(typ='proces', tytul='Cykl lizogeniczny bakteriofaga',
         kroki=[('Adsorpcja i wstrzyknięcie DNA faga'), ('Włączenie DNA faga do chromosomu bakterii', 'profag'),
                ('Podziały bakterii z kopiowaniem profagu'), ('Czynnik stresowy, np. promieniowanie UV'), ('Wycięcie profagu'),
                ('Przejście w cykl lityczny')],
         uwaga='W cyklu lizogenicznym bakteria nie ginie — przekazuje profag komórkom potomnym.'),
    dict(typ='proces', tytul='Namnażanie HIV',
         kroki=[('Przyłączenie do receptora CD4 limfocytu Th'), ('Fuzja osłonki z błoną i wniknięcie kapsydu'),
                ('Odwrotna transkrypcja', 'RNA wirusa → DNA'), ('Integracja DNA wirusa z genomem gospodarza', 'integraza'),
                ('Transkrypcja i translacja białek wirusa'), ('Składanie wirionów i pączkowanie', 'otoczka z błony komórki')],
         uwaga='Leki przeciw HIV hamują m.in. odwrotną transkryptazę, integrazę i proteazę wirusa.'),
]

S['b-bakterie'] = [
    dict(typ='proces', tytul='Barwienie metodą Grama',
         kroki=[('Utrwalenie bakterii na szkiełku'), ('Fiolet krystaliczny', 'wszystkie komórki fioletowe'), ('Płyn Lugola', 'utrwala barwnik'),
                ('Odbarwienie alkoholem', 'Gram-ujemne tracą fiolet'), ('Barwienie safraniną lub fuksyną', 'Gram-ujemne — różowe')],
         uwaga='Gruba warstwa mureiny Gram-dodatnich zatrzymuje fiolet — one pozostają fioletowe.'),
    dict(typ='proces', tytul='Powstawanie oporności bakterii na antybiotyk',
         kroki=[('Populacja bakterii — część z mutacją oporności'), ('Kontakt z antybiotykiem'), ('Śmierć bakterii wrażliwych'),
                ('Przeżycie i namnażanie bakterii opornych'), ('Przekazywanie genów oporności', 'także koniugacja plazmidów'),
                ('Populacja w większości oporna')],
         uwaga='Antybiotyk nie wywołuje mutacji — selekcjonuje bakterie, które już były oporne.'),
]

S['b-protisty'] = [
    dict(typ='cykl', tytul='Cykl rozwojowy zarodźca malarii',
         kroki=[('Ukłucie przez samicę widliszka', 'sporozoity do krwi'), ('Namnażanie w komórkach wątroby'),
                ('Wniknięcie merozoitów do erytrocytów'), ('Rozpad erytrocytów — napady gorączki'), ('Powstawanie gametocytów we krwi'),
                ('Pobranie gametocytów przez komara'), ('Rozmnażanie płciowe w komarze', 'żywiciel ostateczny')],
         uwaga='Żywicielem ostatecznym jest komar (rozmnażanie płciowe), człowiek — żywicielem pośrednim.'),
]

S['b-grzyby'] = [
    dict(typ='cykl', tytul='Cykl rozwojowy grzyba podstawkowego',
         kroki=[('Zarodnik (n)'), ('Grzybnia pierwotna (n)'), ('Połączenie dwóch grzybni — plazmogamia'),
                ('Grzybnia wtórna dwujądrowa (n + n)'), ('Owocnik'), ('Kariogamia w podstawce', 'jądro 2n'),
                ('Mejoza i powstanie zarodników podstawkowych')],
         uwaga='U grzybów plazmogamia i kariogamia są rozdzielone w czasie — przez długi czas grzybnia ma po dwa jądra w komórce.'),
]

S['b-przeglad-roslin'] = [
    dict(typ='cykl', tytul='Cykl rozwojowy mchu',
         kroki=[('Zarodnik (n)'), ('Splątek'), ('Gametofit — ulistniona łodyżka (n)', 'pokolenie dominujące'),
                ('Plemnie i rodnie — gamety'), ('Zapłodnienie w wodzie', 'zygota 2n'), ('Sporofit — seta z puszką (2n)', 'żyje na gametoficie'),
                ('Mejoza w puszce zarodni')],
         uwaga='U mchów dominuje gametofit, a sporofit jest od niego zależny. Do zapłodnienia potrzebna jest woda.'),
    dict(typ='cykl', tytul='Cykl rozwojowy paproci',
         kroki=[('Sporofit — roślina z liśćmi (2n)', 'pokolenie dominujące'), ('Mejoza w zarodniach na spodzie liści'),
                ('Zarodnik (n)'), ('Przedrośle — gametofit (n)'), ('Plemnie i rodnie na przedroślu'), ('Zapłodnienie w wodzie'),
                ('Zygota i młody sporofit')],
         uwaga='U paproci oba pokolenia są samodzielne, ale dominuje sporofit.'),
    dict(typ='cykl', tytul='Cykl rozwojowy rośliny okrytonasiennej',
         kroki=[('Sporofit — roślina kwiatowa (2n)'), ('Mejoza w pylnikach i zalążkach'), ('Ziarno pyłku (gametofit męski)'),
                ('Woreczek zalążkowy (gametofit żeński)'), ('Zapylenie'), ('Podwójne zapłodnienie'), ('Nasienie z zarodkiem w owocu'),
                ('Kiełkowanie')],
         uwaga='Gametofity okrytonasiennych są skrajnie zredukowane: ziarno pyłku ma 2–3 komórki, woreczek zalążkowy — zwykle 7 komórek.'),
    dict(typ='cykl', tytul='Cykl rozwojowy sosny',
         kroki=[('Sporofit — drzewo (2n)'), ('Szyszki męskie — mikrospory i ziarna pyłku'), ('Szyszki żeńskie — zalążki na łuskach'),
                ('Zapylenie przez wiatr'), ('Zapłodnienie', 'ok. rok po zapyleniu'), ('Nasiono ze skrzydełkiem'), ('Kiełkowanie')],
         uwaga='Nagonasienne nie mają owoców — zalążki leżą odkryte na łuskach szyszek.'),
]

S['b-gospodarka-wodna'] = [
    dict(typ='proces', tytul='Transport wody w roślinie',
         kroki=[('Pobieranie wody przez włośniki', 'osmoza'), ('Przechodzenie przez korę korzenia', 'apoplast i symplast'),
                ('Śródskórnia z pasemkami Caspary’ego', 'kontrola przepływu'), ('Naczynia i cewki drewna'),
                ('Transport w górę łodygi', 'siła ssąca transpiracji, kohezja, parcie korzeniowe'), ('Miękisz liścia'),
                ('Parowanie przez aparaty szparkowe')],
         uwaga='Pasemka Caspary’ego zatrzymują drogę apoplastyczną — woda musi przejść przez błony komórek śródskórni.'),
    dict(typ='proces', tytul='Otwieranie aparatu szparkowego',
         kroki=[('Światło pobudza pompy protonowe komórek szparkowych'), ('Aktywny napływ K⁺ do komórek szparkowych'),
                ('Spadek potencjału wody w komórkach'), ('Napływ wody — wzrost turgoru'), ('Wygięcie komórek szparkowych', 'cieńsze ściany zewnętrzne rozciągają się'),
                ('Otwarcie szparki')],
         uwaga='Kwas abscysynowy (ABA) przy niedoborze wody powoduje zamykanie aparatów szparkowych.'),
]

S['b-odzywianie-roslin'] = [
    dict(typ='proces', tytul='Transport asymilatów (hipoteza przepływu masowego)',
         kroki=[('Synteza sacharozy w liściu (źródło)'), ('Aktywny załadunek sacharozy do rurek sitowych'), ('Napływ wody z drewna — wzrost ciśnienia'),
                ('Przepływ roztworu łykiem'), ('Rozładunek w organach odbierających', 'korzenie, owoce, bulwy'), ('Odpływ wody do drewna')],
         uwaga='Łyko transportuje w obu kierunkach — od źródła do miejsca wykorzystania lub magazynowania.'),
]

S['b-rozmnazanie-roslin'] = [
    dict(typ='proces', tytul='Podwójne zapłodnienie',
         kroki=[('Zapylenie — pyłek na znamieniu słupka'), ('Kiełkowanie łagiewki pyłkowej'), ('Wzrost łagiewki przez szyjkę słupka'),
                ('Wniknięcie do zalążka przez okienko'), ('Komórka plemnikowa + komórka jajowa → zygota (2n)'),
                ('Komórka plemnikowa + komórka centralna → bielmo (3n)')],
         uwaga='Podwójne zapłodnienie występuje tylko u roślin okrytonasiennych.'),
    dict(typ='proces', tytul='Powstawanie nasienia i owocu',
         kroki=[('Zapłodnienie w zalążku'), ('Zygota → zarodek'), ('Komórka centralna → bielmo'), ('Osłonki zalążka → łupina nasienna'),
                ('Zalążek → nasienie'), ('Zalążnia → owoc')],
         uwaga='Owoc powstaje ze ściany zalążni, a nasienie — z zalążka.'),
    dict(typ='proces', tytul='Kiełkowanie nasienia',
         kroki=[('Pęcznienie — pobranie wody'), ('Aktywacja enzymów', 'gibereliny pobudzają amylazy'), ('Rozkład materiałów zapasowych'),
                ('Wydostanie się korzenia zarodkowego'), ('Wzrost hipokotylu i wydostanie się pędu'), ('Rozpoczęcie fotosyntezy')],
         uwaga='Do kiełkowania potrzebne są woda, tlen i odpowiednia temperatura; części nasion potrzebne jest też światło.'),
]

S['b-rozwoj-roslin'] = [
    dict(typ='proces', tytul='Fototropizm dodatni pędu',
         kroki=[('Jednostronne oświetlenie wierzchołka'), ('Przemieszczenie auksyny na stronę zacienioną'),
                ('Wyższe stężenie auksyny po stronie zacienionej'), ('Silniejsze wydłużanie komórek po stronie zacienionej'),
                ('Wygięcie pędu w stronę światła')],
         uwaga='Klasyczne doświadczenia z koleoptylami (Darwin, Went) wykazały, że bodziec odbiera wierzchołek, a reaguje strefa poniżej.'),
]

S['b-bezkregowce'] = [
    dict(typ='cykl', tytul='Cykl rozwojowy tasiemca uzbrojonego',
         kroki=[('Tasiemiec w jelicie człowieka', 'żywiciel ostateczny'), ('Człony z jajami wydalane z kałem'), ('Zjedzenie jaj przez świnię'),
                ('Onkosfera przechodzi do krwi'), ('Wągier w mięśniach świni', 'żywiciel pośredni'),
                ('Zjedzenie surowego lub niedogotowanego mięsa przez człowieka')],
         uwaga='Jeśli człowiek połknie jaja tasiemca uzbrojonego, sam staje się żywicielem pośrednim — wągry mogą powstać np. w mózgu (wągrzyca).'),
    dict(typ='cykl', tytul='Cykl rozwojowy glisty ludzkiej',
         kroki=[('Jaja w kale człowieka'), ('Dojrzewanie jaj w glebie'), ('Połknięcie jaj z niemytymi warzywami'),
                ('Larwy w jelicie przechodzą do krwi'), ('Wędrówka przez wątrobę i płuca'), ('Odkrztuszenie i połknięcie larw'),
                ('Dojrzałe glisty w jelicie cienkim')],
         uwaga='Glista ma jednego żywiciela — człowieka; profilaktyka to mycie rąk i warzyw.'),
    dict(typ='proces', tytul='Przeobrażenie zupełne owada',
         kroki=[('Jajo'), ('Larwa', 'odżywianie i wzrost, linienie'), ('Poczwarka', 'przebudowa ciała'), ('Postać dorosła (imago)', 'rozmnażanie')],
         uwaga='Przeobrażenie zupełne mają m.in. motyle, chrząszcze, muchówki i błonkówki; niezupełne — ważki, prostoskrzydłe, pluskwiaki.'),
]

S['b-kregowce'] = [
    dict(typ='proces', tytul='Rozwój żaby',
         kroki=[('Skrzek — jaja w wodzie'), ('Kijanka ze skrzelami zewnętrznymi'), ('Kijanka ze skrzelami wewnętrznymi'),
                ('Wykształcenie kończyn tylnych'), ('Wykształcenie kończyn przednich, rozwój płuc'), ('Zanik ogona', 'pod wpływem tyroksyny'),
                ('Dorosła żaba')],
         uwaga='Przeobrażenie płazów jest sterowane hormonami tarczycy.'),
]

S['b-krzyzowki'] = [
    dict(typ='proces', tytul='Rozwiązywanie zadania z krzyżówką',
         kroki=[('Ustal, które allele są dominujące'), ('Wprowadź oznaczenia alleli'), ('Zapisz genotypy rodziców'), ('Wypisz możliwe gamety'),
                ('Narysuj szachownicę Punnetta'), ('Odczytaj genotypy i fenotypy potomstwa'), ('Podaj stosunek lub prawdopodobieństwo')],
         uwaga='Zawsze sprawdź, o co pyta polecenie: o genotyp, fenotyp, prawdopodobieństwo czy stosunek liczbowy.'),
]

S['b-sprzezenia'] = [
    dict(typ='proces', tytul='Crossing-over',
         kroki=[('Koniugacja chromosomów homologicznych w profazie I'), ('Powstanie biwalentu (tetrady)'),
                ('Pęknięcie chromatyd niesiostrzanych w tym samym miejscu'), ('Wymiana odcinków'), ('Chiazma — miejsce wymiany'),
                ('Chromatydy z nowymi układami alleli', 'gamety rekombinowane')],
         uwaga='Im dalej od siebie leżą geny, tym częściej zachodzi między nimi crossing-over — 1% rekombinantów = 1 cM.'),
]

S['b-rodowody'] = [
    dict(typ='proces', tytul='Analiza rodowodu — kolejność rozumowania',
         kroki=[('Czy chore dziecko ma zdrowych rodziców?', 'tak → cecha recesywna'), ('Czy chorzy są w każdym pokoleniu?', 'sugeruje dominację'),
                ('Czy chorują głównie mężczyźni?', 'sugeruje sprzężenie z X'), ('Czy chora córka ma zdrowego ojca albo chora matka — zdrowego syna?', 'tak → wyklucza recesywne sprzężenie z X'),
                ('Ustal genotypy osób pewnych'), ('Oblicz prawdopodobieństwo dla wskazanej osoby')],
         uwaga='Do wykluczenia sposobu dziedziczenia wystarczy jeden przypadek, który mu przeczy — wskaż go w uzasadnieniu.'),
]

S['b-mutacje'] = [
    dict(typ='proces', tytul='Nondysjunkcja — powstawanie trisomii',
         kroki=[('Mejoza u rodzica'), ('Nierozejście się chromosomów homologicznych w anafazie I lub chromatyd w anafazie II'),
                ('Gameta z dodatkowym chromosomem (n + 1)'), ('Zapłodnienie przez prawidłową gametę (n)'), ('Zygota z trisomią (2n + 1)', 'np. zespół Downa')],
         uwaga='Ryzyko nondysjunkcji rośnie z wiekiem matki — oocyty są długo zatrzymane w profazie I.'),
]

S['b-techniki'] = [
    dict(typ='cykl', tytul='Cykl PCR',
         kroki=[('Denaturacja', 'ok. 95°C — rozdzielenie nici'), ('Przyłączenie starterów', 'ok. 50–65°C'),
                ('Wydłużanie', 'ok. 72°C — polimeraza Taq'), ('Podwojenie liczby kopii')],
         uwaga='Po n cyklach powstaje do 2ⁿ kopii fragmentu. Polimeraza Taq pochodzi z bakterii z gorących źródeł — nie ulega denaturacji.'),
    dict(typ='proces', tytul='Klonowanie genu w bakteriach',
         kroki=[('Wycięcie genu restryktazą'), ('Przecięcie plazmidu tą samą restryktazą', 'lepkie końce'), ('Połączenie genu z plazmidem ligazą'),
                ('Transformacja bakterii'), ('Selekcja na pożywce z antybiotykiem', 'gen oporności w plazmidzie'), ('Namnażanie bakterii i ekspresja genu')],
         uwaga='Ta sama restryktaza daje komplementarne lepkie końce — dzięki temu gen i plazmid mogą się połączyć.'),
    dict(typ='proces', tytul='Elektroforeza DNA',
         kroki=[('Cięcie DNA restryktazami'), ('Nałożenie próbek do studzienek w żelu'), ('Włączenie prądu', 'DNA wędruje do bieguna dodatniego'),
                ('Rozdział fragmentów według długości', 'krótsze szybciej'), ('Wybarwienie i odczyt prążków', 'porównanie ze wzorcem')],
         uwaga='DNA ma ładunek ujemny dzięki resztom fosforanowym — dlatego wędruje do anody (+).'),
    dict(typ='proces', tytul='Klonowanie owcy Dolly',
         kroki=[('Pobranie komórki somatycznej z wymienia owcy A'), ('Pobranie komórki jajowej owcy B'), ('Usunięcie jądra z komórki jajowej'),
                ('Połączenie jądra komórki somatycznej z komórką jajową', 'impuls elektryczny'), ('Rozwój zarodka in vitro'),
                ('Wszczepienie zarodka matce zastępczej C'), ('Narodziny klonu owcy A')],
         uwaga='Klon jest genetycznie identyczny z dawcą jądra — z wyjątkiem DNA mitochondrialnego, pochodzącego z komórki jajowej.'),
    dict(typ='proces', tytul='Edycja genu metodą CRISPR-Cas9',
         kroki=[('Zaprojektowanie RNA prowadzącego (gRNA)'), ('Połączenie gRNA z białkiem Cas9'), ('Rozpoznanie docelowej sekwencji DNA'),
                ('Przecięcie obu nici DNA'), ('Naprawa DNA przez komórkę', 'wyłączenie genu lub wstawienie nowej sekwencji')],
         uwaga='CRISPR pochodzi z układu odpornościowego bakterii, który niszczy DNA bakteriofagów.'),
]

S['b-gmo'] = [
    dict(typ='proces', tytul='Otrzymywanie rośliny transgenicznej',
         kroki=[('Wybór genu o pożądanej cesze'), ('Wstawienie genu do plazmidu Ti bakterii Agrobacterium'), ('Zakażenie komórek roślinnych bakterią'),
                ('Selekcja komórek, które przyjęły gen'), ('Hodowla tkankowa — regeneracja całej rośliny'), ('Sprawdzenie ekspresji genu i badania bezpieczeństwa')],
         uwaga='Komórki roślinne są totipotentne — z jednej komórki można odtworzyć całą roślinę.'),
]

S['b-biotech-medycyna'] = [
    dict(typ='proces', tytul='Produkcja insuliny przez bakterie',
         kroki=[('Wyizolowanie mRNA insuliny z komórek trzustki'), ('Odwrotna transkrypcja — cDNA bez intronów'), ('Wstawienie cDNA do plazmidu'),
                ('Transformacja bakterii E. coli'), ('Hodowla bakterii w bioreaktorze'), ('Oczyszczenie insuliny')],
         uwaga='Bakterie nie mają splicingu — dlatego wprowadza się cDNA, a nie gen z intronami.'),
    dict(typ='proces', tytul='Terapia genowa ex vivo',
         kroki=[('Pobranie komórek pacjenta', 'np. komórek macierzystych szpiku'), ('Wprowadzenie prawidłowego genu wektorem wirusowym'),
                ('Namnożenie zmodyfikowanych komórek'), ('Podanie komórek pacjentowi'), ('Synteza brakującego białka')],
         uwaga='W terapii ex vivo komórki modyfikuje się poza organizmem, w in vivo — wektor podaje się bezpośrednio pacjentowi.'),
]

S['b-dobor'] = [
    dict(typ='proces', tytul='Dobór naturalny według Darwina',
         kroki=[('Nadprodukcja potomstwa'), ('Zmienność osobników'), ('Walka o byt — ograniczone zasoby'),
                ('Przeżywają osobniki lepiej przystosowane'), ('Przekazanie korzystnych cech potomstwu'), ('Zmiana częstości cech w populacji')],
         uwaga='Dobór działa na fenotypy, a zmienia częstość alleli w populacji. Osobnik nie ewoluuje — ewoluuje populacja.'),
]

S['b-specjacja'] = [
    dict(typ='proces', tytul='Specjacja allopatryczna',
         kroki=[('Jedna populacja wyjściowa'), ('Powstanie bariery geograficznej', 'np. rzeka, góry, morze'), ('Brak przepływu genów'),
                ('Różne mutacje, dryf i dobór w obu populacjach'), ('Narastanie różnic genetycznych'), ('Izolacja rozrodcza — dwa gatunki')],
         uwaga='O powstaniu nowego gatunku świadczy izolacja rozrodcza, a nie same różnice w wyglądzie.'),
]

S['b-ekosystem'] = [
    dict(typ='cykl', tytul='Obieg węgla',
         kroki=[('CO₂ w atmosferze'), ('Fotosynteza producentów'), ('Związki organiczne w łańcuchach pokarmowych'),
                ('Oddychanie organizmów'), ('Rozkład martwej materii przez destruentów'), ('Spalanie paliw kopalnych', 'działalność człowieka')],
         uwaga='Paliwa kopalne to węgiel wyłączony z obiegu na miliony lat — ich spalanie zwiększa stężenie CO₂.'),
    dict(typ='cykl', tytul='Obieg azotu',
         kroki=[('N₂ w atmosferze'), ('Wiązanie azotu', 'bakterie brodawkowe, sinice'), ('Amonifikacja', 'rozkład białek do NH₃'),
                ('Nitryfikacja', 'NH₄⁺ → NO₂⁻ → NO₃⁻'), ('Pobieranie azotanów przez rośliny'), ('Denitryfikacja', 'NO₃⁻ → N₂')],
         uwaga='Rośliny nie wiążą N₂ samodzielnie — pobierają jony NH₄⁺ i NO₃⁻ z gleby.'),
    dict(typ='proces', tytul='Sukcesja pierwotna',
         kroki=[('Naga skała'), ('Porosty', 'organizmy pionierskie'), ('Mchy'), ('Rośliny zielne'), ('Krzewy'), ('Las — zbiorowisko klimaksowe')],
         uwaga='Sukcesja pierwotna zaczyna się bez gleby, wtórna — na podłożu z glebą (np. porzucone pole, pogorzelisko).'),
    dict(typ='proces', tytul='Eutrofizacja jeziora',
         kroki=[('Spływ nawozów i ścieków', 'azot i fosfor'), ('Zakwit glonów i sinic'), ('Zacienienie i zamieranie roślin dna'),
                ('Rozkład martwej materii przez bakterie'), ('Spadek stężenia tlenu w wodzie'), ('Śnięcie ryb, procesy beztlenowe')],
         uwaga='W eutrofizacji tlenu brakuje nie z powodu glonów, ale przez bakterie rozkładające ich martwe szczątki.'),
]

S['b-ochrona'] = [
    dict(typ='proces', tytul='Reintrodukcja gatunku',
         kroki=[('Ustalenie przyczyn wymarcia i ich usunięcie'), ('Hodowla zachowawcza w niewoli'), ('Wybór i przygotowanie siedliska'),
                ('Wypuszczenie osobników', 'często stopniowo, z adaptacją'), ('Monitorowanie populacji')],
         uwaga='Reintrodukcja ma sens tylko wtedy, gdy usunięto przyczynę wymarcia — inaczej populacja ponownie zginie.'),
]

S['b-populacje'] = [
    dict(typ='proces', tytul='Wzrost logistyczny populacji',
         kroki=[('Mała liczebność — wolny wzrost'), ('Faza wykładnicza — szybki wzrost'), ('Narastanie oporu środowiska', 'konkurencja, choroby'),
                ('Spowolnienie wzrostu'), ('Stabilizacja przy pojemności środowiska (K)')],
         uwaga='Krzywa wzrostu logistycznego ma kształt litery S, wykładniczego — litery J.'),
]
