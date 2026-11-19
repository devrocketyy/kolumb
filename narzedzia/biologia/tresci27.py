# Treści kursu biologii — porcja 27: duża partia fiszek i pytań ABCD (wszystkie działy).
T = {}

# ---------- Umiejętności ----------
T['b-dane'] = dict(F=[
 ('Odchylenie standardowe', 'Miara rozrzutu wyników wokół średniej — im większe, tym bardziej zróżnicowane pomiary.'),
 ('Mediana', 'Wartość środkowa uporządkowanego zbioru wyników — mniej wrażliwa na wartości skrajne niż średnia.'),
 ('Korelacja a związek przyczynowy', 'Współwystępowanie dwóch zmiennych nie dowodzi, że jedna jest przyczyną drugiej — może działać trzeci czynnik.'),
 ('Wartość procentowa a bezwzględna', 'Wzrost z 2 do 4 to +100%, ale tylko +2 jednostki — przy interpretacji danych trzeba rozróżniać oba ujęcia.'),
], Q=[
 ('Wyniki: 3, 5, 5, 7, 30. Mediana wynosi:', ['10', '*5', '7', '6'], 'Wartość środkowa.'),
 ('Jeśli odchylenia standardowe dwóch prób się nakładają, to:', ['różnica jest na pewno istotna', '*różnica może nie być istotna', 'pomiary były błędne', 'próba kontrolna była zbędna'], 'Ostrożność we wnioskach.'),
 ('Korelacja dwóch zmiennych oznacza, że:', ['jedna jest przyczyną drugiej', '*zmieniają się one współzależnie', 'nie mają ze sobą związku', 'badanie było błędne'], 'Nie dowodzi przyczynowości.'),
])

T['b-wykresy'] = dict(F=[
 ('Skala logarytmiczna na wykresie', 'Kolejne podziałki rosną wielokrotnie (1, 10, 100…) — pozwala przedstawić dane obejmujące wiele rzędów wielkości.'),
 ('Słupki błędów na wykresie', 'Pokazują rozrzut (np. odchylenie standardowe) wokół średniej — ułatwiają ocenę wiarygodności różnic.'),
], Q=[
 ('Na skali logarytmicznej odległość od 1 do 10 jest taka sama jak od:', ['10 do 20', '*10 do 100', '10 do 50', '1 do 2'], 'Kolejne rzędy wielkości.'),
])

# ---------- Biochemia ----------
T['b-woda'] = dict(F=[
 ('Woda jako rozpuszczalnik', 'Polarne cząsteczki wody otaczają jony i związki polarne (hydratacja) — dlatego jest środowiskiem reakcji w komórce.'),
 ('Napięcie powierzchniowe wody — znaczenie', 'Umożliwia np. poruszanie się nartników po powierzchni i udział w podsiąkaniu wody w naczyniach.'),
 ('Ciepło parowania wody', 'Duże — parowanie potu i transpiracja skutecznie chłodzą organizm.'),
], Q=[
 ('Pocenie chłodzi organizm dzięki dużemu:', ['napięciu powierzchniowemu', '*ciepłu parowania wody', 'ciężarowi wody', 'pH potu'], 'Parowanie pobiera ciepło.'),
 ('Substancje hydrofilowe:', ['nie rozpuszczają się w wodzie', '*dobrze rozpuszczają się w wodzie', 'tworzą dwuwarstwy', 'są zawsze lipidami'], 'Polarne.'),
])

T['b-bialka'] = dict(F=[
 ('Wiązanie peptydowe', 'Wiązanie między grupą karboksylową jednego aminokwasu a aminową drugiego, powstające z wydzieleniem wody (kondensacja).'),
 ('Punkt izoelektryczny białka', 'pH, przy którym białko ma ładunek całkowity równy zero — wtedy najsłabiej się rozpuszcza.'),
 ('Funkcje białek — przykłady', 'Enzymatyczna (amylaza), transportowa (hemoglobina), budulcowa (kolagen), obronna (przeciwciała), regulacyjna (insulina), ruchowa (aktyna, miozyna).'),
], Q=[
 ('Przy powstawaniu wiązania peptydowego wydziela się:', ['CO₂', '*woda', 'amoniak', 'ATP'], 'Kondensacja.'),
 ('Białkiem transportowym jest:', ['kolagen', '*hemoglobina', 'keratyna', 'pepsyna'], 'Transport O₂.'),
 ('Ile wiązań peptydowych ma tripeptyd?', ['1', '*2', '3', '4'], 'n − 1.'),
])

T['b-weglowodany'] = dict(F=[
 ('Wiązanie glikozydowe', 'Wiązanie łączące cukry, powstające w reakcji kondensacji; rozrywane podczas hydrolizy (trawienia).'),
 ('Laktoza', 'Disacharyd mleka zbudowany z glukozy i galaktozy; trawiony przez laktazę.'),
 ('Maltoza', 'Disacharyd z dwóch cząsteczek glukozy — produkt trawienia skrobi przez amylazę.'),
], Q=[
 ('Produktem trawienia skrobi przez amylazę ślinową jest głównie:', ['sacharoza', '*maltoza', 'laktoza', 'fruktoza'], 'Dwie glukozy.'),
 ('Laktoza zbudowana jest z:', ['dwóch glukoz', '*glukozy i galaktozy', 'glukozy i fruktozy', 'dwóch galaktoz'], 'Cukier mleczny.'),
])

T['b-lipidy'] = dict(F=[
 ('Woski — funkcje', 'Estry kwasów tłuszczowych i alkoholi długołańcuchowych; tworzą warstwy ochronne (kutykula, pióra ptaków, plaster miodu).'),
 ('Hormony steroidowe — przykłady', 'Testosteron, estrogeny, progesteron, kortyzol, aldosteron — pochodne cholesterolu.'),
 ('Tłuszcze roślinne a zwierzęce', 'Roślinne zwykle ciekłe (więcej kwasów nienasyconych), zwierzęce zwykle stałe (więcej nasyconych).'),
], Q=[
 ('Hormonem steroidowym jest:', ['insulina', 'adrenalina', '*kortyzol', 'tyroksyna'], 'Pochodna cholesterolu.'),
 ('Oleje roślinne są ciekłe, ponieważ zawierają dużo kwasów tłuszczowych:', ['nasyconych', '*nienasyconych', 'krótkich i nasyconych', 'aromatycznych'], 'Wiązania podwójne.'),
])

T['b-kwasy'] = dict(F=[
 ('Reguła Chargaffa', 'W DNA ilość A = T i G = C, więc puryny = pirymidyny.'),
 ('Puryny i pirymidyny', 'Puryny (dwupierścieniowe): adenina, guanina; pirymidyny (jednopierścieniowe): cytozyna, tymina, uracyl.'),
 ('Wiązanie fosfodiestrowe', 'Łączy nukleotydy w łańcuchu — między resztą fosforanową a cukrem sąsiedniego nukleotydu (3′–5′).'),
], Q=[
 ('Do puryn należy:', ['cytozyna', 'tymina', '*guanina', 'uracyl'], 'Dwa pierścienie.'),
 ('Jeśli w DNA jest 22% guaniny, to tyminy jest:', ['22%', '*28%', '56%', '44%'], '(100 − 44)/2.'),
])

# ---------- Komórka ----------
T['b-blony'] = dict(F=[
 ('Akwaporyny', 'Białkowe kanały w błonie ułatwiające szybki przepływ wody (dyfuzja wspomagana); np. w kanalikach nerkowych.'),
 ('Transport wtórnie aktywny (symport)', 'Transport substancji wbrew gradientowi z wykorzystaniem gradientu innego jonu (np. glukoza razem z Na⁺ w jelicie).'),
 ('Pinocytoza', 'Pobieranie przez komórkę kropli płynu w pęcherzykach („picie komórkowe”).'),
], Q=[
 ('Glukoza jest wchłaniana do enterocytów razem z jonami Na⁺. To przykład:', ['dyfuzji prostej', '*transportu wtórnie aktywnego', 'osmozy', 'pinocytozy'], 'Symport.'),
 ('Akwaporyny umożliwiają transport:', ['glukozy', '*wody', 'jonów Na⁺', 'białek'], 'Kanały wodne.'),
])

T['b-mitochondria'] = dict(F=[
 ('Chromoplasty', 'Plastydy z karotenoidami — nadają barwę kwiatom i owocom (np. pomidor, marchew).'),
 ('Macierz mitochondrialna', 'Wnętrze mitochondrium: zachodzi reakcja pomostowa, cykl Krebsa, β-oksydacja; zawiera mtDNA i rybosomy.'),
 ('Stroma chloroplastu', 'Wnętrze chloroplastu poza tylakoidami — zachodzi cykl Calvina; zawiera DNA i rybosomy 70S.'),
], Q=[
 ('Czerwony kolor dojrzałego pomidora nadają:', ['chloroplasty', '*chromoplasty', 'leukoplasty', 'wakuole z antocyjanami'], 'Karotenoidy.'),
 ('Cykl Krebsa zachodzi w:', ['cytozolu', '*macierzy mitochondrium', 'stromie chloroplastu', 'błonie zewnętrznej mitochondrium'], 'Matrix.'),
])

# ---------- Metabolizm ----------
T['b-enzymy'] = dict(F=[
 ('Model indukowanego dopasowania', 'Centrum aktywne zmienia nieco kształt po związaniu substratu, dopasowując się do niego.'),
 ('Swoistość substratowa enzymu', 'Enzym katalizuje reakcję tylko określonego substratu (lub grupy podobnych) dzięki kształtowi centrum aktywnego.'),
 ('Proenzymy (zymogeny)', 'Nieaktywne formy enzymów (np. pepsynogen, trypsynogen) aktywowane w miejscu działania — chronią komórki przed samostrawieniem.'),
], Q=[
 ('Trypsynogen jest przykładem:', ['koenzymu', '*proenzymu', 'inhibitora', 'hormonu'], 'Nieaktywna forma.'),
 ('Wraz ze wzrostem stężenia substratu szybkość reakcji enzymatycznej:', ['rośnie bez końca', '*rośnie do osiągnięcia maksimum', 'spada', 'nie zmienia się'], 'Wysycenie enzymu.'),
])

T['b-oddychanie'] = dict(F=[
 ('Gdzie powstaje woda w oddychaniu tlenowym?', 'W łańcuchu oddechowym — tlen przyjmuje elektrony i protony (kompleks IV).'),
 ('Oddychanie a spalanie', 'Oddychanie zachodzi etapami, z udziałem enzymów, a energia jest częściowo magazynowana w ATP; spalanie — gwałtownie, energia jako ciepło i światło.'),
], Q=[
 ('Woda w oddychaniu tlenowym powstaje w:', ['glikolizie', 'cyklu Krebsa', '*łańcuchu oddechowym', 'reakcji pomostowej'], 'Redukcja tlenu.'),
])

T['b-fotosynteza'] = dict(F=[
 ('Fotofosforylacja', 'Synteza ATP w fazie zależnej od światła dzięki gradientowi protonów w poprzek błony tylakoidu.'),
 ('Fotoliza wody', 'Rozkład wody przy PS II: 2 H₂O → 4 H⁺ + 4 e⁻ + O₂ — źródło elektronów i tlenu.'),
], Q=[
 ('Fotoliza wody zachodzi przy fotosystemie:', ['I', '*II', 'I i II jednocześnie', 'w stromie'], 'P680.'),
 ('Gradient protonów w chloroplaście powstaje w poprzek błony:', ['zewnętrznej otoczki', '*tylakoidu', 'wewnętrznej otoczki', 'komórkowej'], 'Wnętrze tylakoidu kwaśne.'),
])

# ---------- Podziały ----------
T['b-replikacja'] = dict(F=[
 ('Topoizomeraza', 'Enzym usuwający superskręty DNA przed widełkami replikacyjnymi przez nacinanie i ponowne łączenie nici.'),
 ('Widełki replikacyjne', 'Miejsce rozplatania DNA, w którym zachodzi synteza nowych nici; z jednego ori wychodzą dwa widełki.'),
], Q=[
 ('Superskręty DNA przed widełkami usuwa:', ['helikaza', '*topoizomeraza', 'prymaza', 'ligaza'], 'Napięcia.'),
])

T['b-apoptoza'] = dict(F=[
 ('Ciałka apoptotyczne', 'Fragmenty komórki otoczone błoną, powstające podczas apoptozy i pochłaniane przez makrofagi.'),
 ('Apoptoza a rozwój układu nerwowego', 'Nadmiar neuronów, które nie nawiązały połączeń, ulega apoptozie — kształtowanie sieci nerwowej.'),
], Q=[
 ('Ciałka apoptotyczne są usuwane przez:', ['limfocyty B', '*makrofagi', 'erytrocyty', 'płytki krwi'], 'Fagocytoza.'),
])

# ---------- Genetyka molekularna ----------
T['b-gen'] = dict(F=[
 ('Rama odczytu', 'Sposób podziału sekwencji na kolejne trójki od kodonu START; przesunięcie o 1–2 nukleotydy zmienia wszystkie dalsze kodony.'),
 ('Region nieulegający translacji (UTR)', 'Fragmenty mRNA przed kodonem START (5′UTR) i za kodonem STOP (3′UTR) — wpływają na stabilność i wydajność translacji.'),
], Q=[
 ('5′UTR to fragment mRNA:', ['za kodonem STOP', '*przed kodonem START', 'kodujący pierwszy aminokwas', 'usuwany w splicingu'], 'Niekodujący.'),
])

T['b-transkrypcja'] = dict(F=[
 ('Alternatywny splicing — znaczenie', 'Z jednego genu powstaje kilka białek — zwiększa różnorodność białek przy ograniczonej liczbie genów.'),
 ('Odwrotna transkrypcja w telomerazie', 'Telomeraza zawiera własny RNA, na którego matrycy dobudowuje DNA telomerów.'),
], Q=[
 ('Alternatywny splicing pozwala na:', ['powielenie genu w genomie', '*powstanie kilku białek z jednego genu', 'replikację RNA w jądrze', 'usunięcie promotora genu'], 'Różne zestawy eksonów.'),
])

# ---------- Genetyka ----------
T['b-krzyzowki'] = dict(Q=[
 ('Z krzyżówki AaBb × Aabb (geny niesprzężone) potomstwa o fenotypie dominującym w obu cechach jest:', ['9/16', '*3/8', '1/4', '1/2'], '3/4 × 1/2.'),
 ('Osobnik AaBbCc wytwarza gametę ABC z prawdopodobieństwem:', ['1/4', '*1/8', '1/16', '1/2'], '(1/2)³.'),
 ('W krzyżówce Aa × Aa prawdopodobieństwo, że osobnik o fenotypie dominującym jest heterozygotą, wynosi:', ['1/2', '*2/3', '3/4', '1/4'], 'AA : 2Aa.'),
])

T['b-wspoldzialanie'] = dict(F=[
 ('Geny kumulatywne (polimeryczne)', 'Kilka genów o działaniu addytywnym — im więcej alleli dominujących, tym silniej wyrażona cecha (np. kolor ziarna pszenicy).'),
 ('Penetracja niepełna', 'Nie wszyscy nosiciele danego genotypu wykazują odpowiadający mu fenotyp.'),
], Q=[
 ('Nie każdy nosiciel allelu dominującego choroby wykazuje objawy. Zjawisko to:', ['kodominacja', '*niepełna penetracja', 'epistaza', 'sprzężenie'], 'Penetracja.'),
])

T['b-rodowody'] = dict(F=[
 ('Jak wykluczyć dziedziczenie dominujące sprzężone z X?', 'Jeśli chory ojciec ma zdrową córkę (dominujący allel na X zawsze trafia do córki).'),
 ('Proband', 'Osoba, od której rozpoczęto badanie rodowodu (zwykle pierwsza zdiagnozowana w rodzinie).'),
], Q=[
 ('Chory ojciec ma zdrową córkę. Wykluczono dziedziczenie:', ['autosomalne recesywne', '*dominujące sprzężone z X', 'autosomalne dominujące', 'mitochondrialne'], 'Córka dostaje X ojca.'),
])

T['b-choroby-genetyczne'] = dict(F=[
 ('Hemofilia A', 'Recesywna choroba sprzężona z X — brak czynnika krzepnięcia VIII; przedłużone krwawienia.'),
 ('Dystrofia mięśniowa Duchenne’a', 'Recesywna sprzężona z X — brak dystrofiny, postępujący zanik mięśni u chłopców.'),
 ('Albinizm', 'Autosomalny recesywny brak melaniny (niedobór tyrozynazy) — jasna skóra, włosy, wrażliwość na UV.'),
], Q=[
 ('Albinizm u człowieka dziedziczy się:', ['dominująco autosomalnie', '*recesywnie autosomalnie', 'recesywnie z X', 'mitochondrialnie'], 'Brak melaniny.'),
 ('Dystrofia mięśniowa Duchenne’a dotyczy głównie:', ['dziewczynek', '*chłopców', 'obu płci równo', 'tylko dorosłych'], 'Sprzężona z X.'),
])

# ---------- Biotechnologia ----------
T['b-techniki'] = dict(F=[
 ('Metoda Sangera — zasada', 'Synteza DNA z dodatkiem dideoksynukleotydów kończących łańcuch — fragmenty różnej długości odczytuje się po rozdziale.'),
 ('Marker wielkości DNA (drabinka)', 'Mieszanina fragmentów o znanej długości nakładana obok prób w elektroforezie — wzorzec do odczytu wielkości.'),
], Q=[
 ('W metodzie Sangera synteza łańcucha kończy się po wbudowaniu:', ['rybonukleotydu', '*dideoksynukleotydu', 'aminokwasu', 'startera'], 'Brak 3′-OH.'),
])

T['b-biotech-medycyna'] = dict(F=[
 ('Medycyna sądowa a DNA', 'Profil STR z niewielkiej ilości materiału (krew, ślina, włos z cebulką) pozwala z dużym prawdopodobieństwem zidentyfikować osobę.'),
 ('Testy genetyczne a etyka', 'Ochrona danych genetycznych, prawo do niewiedzy, ryzyko dyskryminacji (ubezpieczenia, praca), świadoma zgoda.'),
], Q=[
 ('Do analizy DNA nie nadaje się:', ['krew z miejsca zdarzenia', 'ślina na niedopałku papierosa', '*włos ścięty bez cebulki', 'włos wyrwany z cebulką'], 'Cebulka zawiera komórki.'),
])

# ---------- Mikroorganizmy ----------
T['b-wirusy'] = dict(F=[
 ('Szczepionki przeciw wirusom — przykłady', 'Odra, świnka, różyczka, polio, WZW B, HPV, grypa, COVID-19.'),
 ('Leki przeciwwirusowe — zasada', 'Hamują etapy specyficzne dla wirusa (np. odwrotną transkryptazę HIV, uwalnianie wirusa grypy).'),
], Q=[
 ('Przeciw której chorobie istnieje szczepionka?', ['AIDS', '*WZW typu B', 'przeziębienie (wszystkie typy)', 'opryszczka'], 'Szczepienie obowiązkowe.'),
])

T['b-bakterie'] = dict(F=[
 ('Antybiotyk bakteriobójczy a bakteriostatyczny', 'Bakteriobójczy zabija bakterie (np. penicylina — ściana); bakteriostatyczny hamuje ich namnażanie (np. tetracyklina — rybosomy).'),
 ('Penicylina — mechanizm', 'Hamuje syntezę mureiny — bakterie mają uszkodzoną ścianę i pękają (działa na dzielące się bakterie).'),
], Q=[
 ('Penicylina hamuje:', ['syntezę białek', '*syntezę ściany komórkowej', 'replikację DNA', 'oddychanie'], 'Mureina.'),
 ('Na komórki człowieka penicylina nie działa, ponieważ nie mają one:', ['rybosomów', '*ściany z mureiny', 'błony komórkowej', 'mitochondriów'], 'Selektywność.'),
])

T['b-protisty'] = dict(F=[
 ('Rzęsistek pochwowy', 'Pasożytniczy wiciowiec przenoszony drogą płciową — wywołuje rzęsistkowicę.'),
 ('Lamblia (giardia)', 'Wiciowiec pasożytujący w jelicie cienkim — biegunki; zarażenie przez cysty w wodzie.'),
], Q=[
 ('Lamblioza przenosi się głównie przez:', ['ukłucie zakażonego owada', '*cysty w zanieczyszczonej wodzie', 'kontakt skórny z chorym', 'drogę kropelkową w powietrzu'], 'Droga pokarmowa.'),
])

T['b-grzyby'] = dict(F=[
 ('Konidia', 'Bezpłciowe zarodniki grzybów workowych (np. pędzlaka, kropidlaka) odcinane na końcach strzępek.'),
 ('Grzyby a obieg węgla', 'Rozkładając materię organiczną, uwalniają CO₂ do atmosfery w oddychaniu.'),
], Q=[
 ('Konidia to:', ['zarodniki płciowe', '*bezpłciowe zarodniki grzybów', 'komórki drożdży', 'owocniki'], 'Rozmnażanie bezpłciowe.'),
])

# ---------- Rośliny ----------
T['b-przeglad-roslin'] = dict(F=[
 ('Wątrobowce', 'Mszaki o plesze lub ulistnionej łodyżce (np. porostnica) — rozmnażanie także rozmnóżkami w koszyczkach.'),
 ('Widłaki', 'Paprotniki o drobnych liściach i kłosach zarodnionośnych; w Polsce wszystkie gatunki chronione.'),
 ('Jednoliścienne a dwuliścienne — liście i kwiaty', 'Jednoliścienne: liście równowąskie, nerwacja równoległa, kwiaty trójkrotne; dwuliścienne: nerwacja siatkowata, kwiaty cztero- lub pięciokrotne.'),
], Q=[
 ('Nerwacja równoległa liści jest typowa dla:', ['dwuliściennych', '*jednoliściennych', 'paproci', 'mchów'], 'Trawy, lilie.'),
 ('Kwiaty trójkrotne mają zwykle rośliny:', ['dwuliścienne', '*jednoliścienne', 'nagonasienne', 'paprotniki'], 'Tulipan.'),
])

T['b-odzywianie-roslin'] = dict(F=[
 ('Nawozy zielone', 'Rośliny (zwykle bobowate) przyorywane w celu wzbogacenia gleby w materię organiczną i azot.'),
 ('Płodozmian', 'Następowanie po sobie różnych roślin na polu — poprawia żyzność gleby i ogranicza choroby i szkodniki.'),
], Q=[
 ('Bobowate w płodozmianie wzbogacają glebę głównie w:', ['fosfor', '*azot', 'potas', 'wapń'], 'Bakterie brodawkowe.'),
])

T['b-rozmnazanie-roslin'] = dict(F=[
 ('Szczepienie roślin', 'Łączenie fragmentu pędu jednej rośliny (zraz) z podkładką drugiej — utrwalenie cech odmiany (np. jabłonie).'),
 ('Kultury in vitro — zastosowanie', 'Szybkie namnażanie roślin (np. storczyków), uzyskiwanie roślin bez wirusów, ochrona gatunków zagrożonych.'),
], Q=[
 ('Szczepienie drzew owocowych to rozmnażanie:', ['płciowe', '*wegetatywne (sztuczne)', 'przez apomiksję', 'przez zarodniki'], 'Zraz i podkładka.'),
])

T['b-tkanki-roslinne'] = dict(F=[
 ('Miękisz spichrzowy', 'Gromadzi materiały zapasowe (skrobia w bulwie ziemniaka, cukry w korzeniu buraka).'),
 ('Tkanki wydzielnicze', 'Gruczoły nektarowe, kanały żywiczne, rurki mleczne (np. mniszek) — wydzielanie substancji.'),
], Q=[
 ('Kanały żywiczne występują w drewnie:', ['dębu', '*sosny', 'lipy', 'brzozy'], 'Nagonasienne.'),
])

# ---------- Zwierzęta ----------
T['b-bezkregowce'] = dict(F=[
 ('Skorupiaki — znaczenie', 'Kryl i widłonogi to podstawa sieci pokarmowych mórz; rozwielitki filtrują wodę w jeziorach.'),
 ('Pająki — trawienie', 'Trawienie pozajelitowe: wstrzykują enzymy do ofiary, a następnie wysysają płynną treść.'),
], Q=[
 ('Pająki trawią pokarm:', ['wyłącznie w jelicie', '*częściowo poza organizmem (pozajelitowo)', 'w żołądku wielokomorowym', 'przy pomocy symbiotycznych bakterii'], 'Enzymy wstrzykiwane.'),
])

T['b-kregowce'] = dict(F=[
 ('Płazy ogoniaste i bezogonowe', 'Ogoniaste (traszki, salamandry) — ogon przez całe życie; bezogonowe (żaby, ropuchy) — tracą ogon w przeobrażeniu.'),
 ('Gady — skóra', 'Sucha, z rogowymi łuskami (lub tarczkami), bez gruczołów śluzowych — chroni przed wysychaniem; linienie.'),
], Q=[
 ('Traszka należy do płazów:', ['bezogonowych', '*ogoniastych', 'beznogich', 'gadów'], 'Ogon zachowany.'),
])

# ---------- Fizjologia ----------
T['b-odpornosc'] = dict(Q=[
 ('Przeszczep jest odrzucany głównie przez:', ['erytrocyty biorcy', '*limfocyty T rozpoznające obce MHC', 'płytki krwi biorcy', 'przeciwciała IgE na komórkach tucznych'], 'Odpowiedź komórkowa.'),
 ('Gorączka w infekcji:', ['zawsze szkodzi organizmowi', '*hamuje namnażanie patogenów i wspiera odporność', 'nie ma żadnego związku z infekcją', 'niszczy wytworzone przeciwciała'], 'Mechanizm obronny.'),
])

T['b-hormony'] = dict(Q=[
 ('Erytropoetynę wytwarzają głównie:', ['wątroba', '*nerki', 'szpik', 'płuca'], 'Niedotlenienie.'),
 ('Hormon wzrostu wydziela:', ['tarczyca', '*przedni płat przysadki', 'grasica', 'nadnercza'], 'GH.'),
])

T['b-nerwy'] = dict(Q=[
 ('Ośrodek mowy ruchowej (Broki) leży w płacie:', ['potylicznym', '*czołowym', 'skroniowym', 'ciemieniowym'], 'Lewa półkula.'),
 ('Plamka żółta zawiera głównie:', ['pręciki', '*czopki', 'komórki zwojowe', 'brak fotoreceptorów'], 'Ostre widzenie.'),
])

T['b-krazenie'] = dict(Q=[
 ('Pierwszy ton serca powstaje przy zamknięciu zastawek:', ['półksiężycowatych', '*przedsionkowo-komorowych', 'żylnych', 'aorty i pnia płucnego'], 'Początek skurczu komór.'),
])

T['b-wydalanie'] = dict(Q=[
 ('Glukoza nie występuje w moczu ostatecznym zdrowego człowieka, ponieważ:', ['nie przechodzi przez filtr kłębuszka', '*jest całkowicie resorbowana', 'jest rozkładana w pęcherzu', 'jest wydalana z potem'], 'Kanalik I rzędu.'),
])

# ---------- Ewolucja i ekologia ----------
T['b-dobor'] = dict(F=[
 ('Dryf a dobór — różnica', 'Dobór zmienia częstości alleli w sposób ukierunkowany (przystosowawczy), dryf — losowo.'),
 ('Paleontologia — metody datowania', 'Datowanie względne (warstwy skalne) i bezwzględne (izotopy promieniotwórcze, np. ¹⁴C dla młodszych szczątków).'),
], Q=[
 ('Losowe zmiany częstości alleli to:', ['dobór naturalny', '*dryf genetyczny', 'przepływ genów', 'mutacja'], 'Małe populacje.'),
])

T['b-populacje'] = dict(F=[
 ('Opór środowiska', 'Czynniki ograniczające wzrost populacji (brak pokarmu, choroby, drapieżnictwo, konkurencja) — przyczyna krzywej S.'),
 ('Pojemność środowiska a gęstość populacji', 'Przy zagęszczeniu bliskim K rośnie śmiertelność i spada rozrodczość — liczebność się stabilizuje.'),
], Q=[
 ('Wzrost populacji zgodny z krzywą J następuje, gdy:', ['zasoby są ograniczone', '*zasoby są praktycznie nieograniczone', 'działa silna konkurencja', 'populacja osiągnęła K'], 'Wykładniczy.'),
])

T['b-ekosystem'] = dict(Q=[
 ('Nitryfikację przeprowadzają bakterie:', ['brodawkowe w korzeniach', '*nitryfikacyjne (chemoautotrofy)', 'gnilne (amonifikacyjne)', 'denitryfikacyjne w glebie'], 'NH₄⁺ → NO₃⁻.'),
 ('Najwięcej energii zgromadzone jest na poziomie:', ['drapieżników', 'roślinożerców', '*producentów', 'destruentów'], 'Piramida energii.'),
])

T['b-ochrona'] = dict(F=[
 ('Restytucja a reintrodukcja', 'Restytucja — odtworzenie populacji gatunku (np. z hodowli); reintrodukcja — ponowne wprowadzenie na obszar, gdzie wyginął.'),
 ('Fragmentacja siedlisk — przykłady', 'Drogi, linie kolejowe, osiedla dzielące lasy i łąki na małe, izolowane płaty.'),
], Q=[
 ('Przejścia dla zwierząt nad autostradą ograniczają skutki:', ['eutrofizacji', '*fragmentacji siedlisk', 'kwaśnych deszczy', 'dryfu w dużych populacjach'], 'Korytarze ekologiczne.'),
])
