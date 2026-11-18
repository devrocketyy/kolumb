# Treści kursu biologii — porcja 14: Genetyka klasyczna.
T = {}

T['b-krzyzowki'] = dict(F=[
 ('Wyjaśnij pojęcie: allel dominujący i recesywny', 'Dominujący (A) ujawnia się w fenotypie także u heterozygoty; recesywny (a) — tylko u homozygoty recesywnej (aa).'),
 ('Wyjaśnij pojęcie: homozygota i heterozygota', 'Homozygota — dwa jednakowe allele danego genu (AA, aa); heterozygota — dwa różne (Aa).'),
 ('I prawo Mendla (czystości gamet)', 'Każda gameta zawiera tylko jeden allel z danej pary — allele rozdzielają się podczas tworzenia gamet (anafaza I mejozy).'),
 ('II prawo Mendla (niezależnej segregacji)', 'Allele różnych genów dziedziczą się niezależnie od siebie — dotyczy genów leżących na różnych parach chromosomów.'),
 ('Stosunek fenotypów w F2 krzyżówki jednogenowej z dominacją zupełną', '3 : 1 (genotypy 1 AA : 2 Aa : 1 aa).'),
 ('Stosunek fenotypów w F2 krzyżówki dwugenowej (AaBb × AaBb)', '9 : 3 : 3 : 1 (geny niesprzężone, dominacja zupełna).'),
 ('Wyjaśnij pojęcie: krzyżówka testowa', 'Krzyżowanie osobnika o fenotypie dominującym z homozygotą recesywną, aby ustalić jego genotyp: brak potomstwa recesywnego → AA; 1:1 → Aa.'),
 ('Wynik krzyżówki testowej AaBb × aabb', '1 : 1 : 1 : 1 (AaBb, Aabb, aaBb, aabb) — przy genach niesprzężonych.'),
 ('Wyjaśnij pojęcie: dominacja niezupełna', 'Heterozygota ma fenotyp pośredni (np. różowe kwiaty lwiej paszczy z czerwonych i białych); w F2 stosunek 1 : 2 : 1.'),
 ('Wyjaśnij pojęcie: kodominacja', 'W heterozygocie ujawniają się oba allele w pełni (np. grupa krwi AB — obecne oba antygeny).'),
 ('Wyjaśnij pojęcie: allele letalne', 'Allele powodujące śmierć osobnika (zwykle w stanie homozygotycznym) — np. przy żółtym umaszczeniu myszy w F2 stosunek 2 : 1 zamiast 3 : 1.'),
 ('Jak obliczyć liczbę typów gamet osobnika?', '2ⁿ, gdzie n — liczba genów w stanie heterozygotycznym (niesprzężonych); np. AaBbCC → 2² = 4 typy gamet.'),
 ('Jak obliczać prawdopodobieństwo w krzyżówkach wielogenowych?', 'Rozpatrzyć każdy gen osobno i pomnożyć prawdopodobieństwa (reguła iloczynu) — np. P(aabb) z AaBb × AaBb = 1/4 × 1/4 = 1/16.'),
 ('Jak zapisać krzyżówkę na maturze?', 'Podać genotypy rodziców (P), ich gamety, szachownicę Punnetta (lub krzyżówkę), genotypy i fenotypy potomstwa z proporcjami; objaśnić oznaczenia alleli.'),
 ('Wyjaśnij pojęcie: pokolenie P, F1, F2', 'P — rodzicielskie; F1 — pierwsze pokolenie potomne; F2 — potomstwo osobników F1.'),
 ('Dlaczego Mendel wybrał groch?', 'Łatwa uprawa, krótki cykl, dużo potomstwa, wyraźne cechy alternatywne, możliwość samozapylenia (linie czyste) i kontrolowanego krzyżowania.'),
], Q=[
 ('Stosunek fenotypów 9:3:3:1 dotyczy krzyżówki:', ['Aa × aa (jeden gen)', '*AaBb × AaBb (geny niesprzężone)', 'AaBb × aabb (testowej)', 'AABB × aabb (pokolenie P)'], 'F2 dwugenowa.'),
 ('Krzyżówka testowa polega na skrzyżowaniu z:', ['homozygotą dominującą', '*homozygotą recesywną', 'heterozygotą', 'osobnikiem F1'], 'Ujawnia genotyp.'),
 ('Ile typów gamet wytwarza osobnik AaBbCc (geny niesprzężone)?', ['3', '6', '*8', '9'], '2³.'),
 ('Grupa krwi AB jest przykładem:', ['dominacji niezupełnej', '*kodominacji', 'epistazy', 'sprzężenia z płcią'], 'Oba antygeny.'),
 ('Stosunek 2:1 w potomstwie dwóch heterozygot wskazuje na:', ['kodominację alleli', '*allel letalny w homozygocie', 'sprzężenie genów', 'polimerię genów'], 'Homozygoty giną.'),
], pp='XIV.1.1')

T['b-wspoldzialanie'] = dict(F=[
 ('Wyjaśnij pojęcie: allele wielokrotne', 'Więcej niż dwa allele danego genu w populacji (osobnik ma maksymalnie dwa) — np. grupy krwi: Iᴬ, Iᴮ, i.'),
 ('Genotypy grup krwi AB0', 'A: IᴬIᴬ lub Iᴬi; B: IᴮIᴮ lub Iᴮi; AB: IᴬIᴮ; 0: ii.'),
 ('Czy rodzice z grupami A i B mogą mieć dziecko z grupą 0?', 'Tak — jeśli oboje są heterozygotami (Iᴬi × Iᴮi); prawdopodobieństwo 1/4.'),
 ('Wyjaśnij pojęcie: epistaza', 'Allel jednego genu maskuje (hamuje) ekspresję alleli innego genu — np. albinizm maskuje geny barwy sierści.'),
 ('Stosunek fenotypów przy epistazie recesywnej', '9 : 3 : 4 (np. barwa sierści myszy: aa maskuje gen B).'),
 ('Stosunek fenotypów przy epistazie dominującej', '12 : 3 : 1 (np. barwa owoców dyni).'),
 ('Wyjaśnij pojęcie: geny komplementarne', 'Dwa geny, których dominujące allele muszą wystąpić razem, aby ujawniła się cecha — stosunek 9 : 7 (np. purpurowe kwiaty groszku pachnącego).'),
 ('Wyjaśnij pojęcie: polimeria (dziedziczenie wielogenowe)', 'Cecha warunkowana addytywnym działaniem wielu genów — im więcej alleli dominujących, tym silniej wyrażona (wzrost, kolor skóry); rozkład ciągły.'),
 ('Wyjaśnij pojęcie: cechy ilościowe i jakościowe', 'Ilościowe — zmienność ciągła, wiele genów i wpływ środowiska (masa, wzrost); jakościowe — kilka wyraźnych klas (grupa krwi, barwa kwiatu).'),
 ('Wyjaśnij pojęcie: plejotropia', 'Jeden gen wpływa na wiele cech (np. mukowiscydoza — układ oddechowy, trawienny i rozrodczy; fenyloketonuria).'),
 ('Wyjaśnij pojęcie: norma reakcji', 'Zakres fenotypów, jakie może wytworzyć dany genotyp w różnych warunkach środowiska (np. umaszczenie kota syjamskiego zależne od temperatury).'),
 ('Jak rozpoznać współdziałanie genów w zadaniu?', 'Stosunek fenotypów w F2 jest modyfikacją 9:3:3:1 (np. 9:7, 9:3:4, 12:3:1, 15:1), a liczba klas fenotypowych jest mniejsza niż 4.'),
], Q=[
 ('Osoba z grupą krwi 0 ma genotyp:', ['IᴬIᴮ', 'Iᴬi', '*ii', 'IᴮIᴮ'], 'Homozygota recesywna.'),
 ('Stosunek 9:7 w F2 wskazuje na:', ['epistazę dominującą', '*geny komplementarne', 'polimerię', 'kodominację'], 'Dwa allele dominujące potrzebne.'),
 ('Kolor skóry człowieka jest przykładem:', ['allelu letalnego w homozygocie', '*dziedziczenia wielogenowego (polimerii)', 'dominacji zupełnej jednego genu', 'sprzężenia z chromosomem X'], 'Zmienność ciągła.'),
 ('Wpływ jednego genu na wiele cech to:', ['epistaza', '*plejotropia', 'polimeria', 'kodominacja'], 'Np. mukowiscydoza.'),
], pp='XIV.1.2')

T['b-sprzezenia'] = dict(F=[
 ('Wyjaśnij pojęcie: geny sprzężone', 'Geny leżące na tym samym chromosomie, dziedziczone najczęściej razem (nie podlegają II prawu Mendla).'),
 ('Wyjaśnij pojęcie: teoria chromosomowa Morgana', 'Geny leżą w chromosomach liniowo; geny jednego chromosomu tworzą grupę sprzężeń; sprzężenie może być przerwane przez crossing-over z częstością zależną od odległości między genami.'),
 ('Wyjaśnij pojęcie: rekombinanty', 'Osobniki (gamety) z nowymi kombinacjami alleli, niewystępującymi u rodziców — powstają w wyniku crossing-over.'),
 ('Jak obliczyć częstość crossing-over?', 'Liczba rekombinantów / liczba wszystkich potomków × 100%.'),
 ('Wyjaśnij pojęcie: centymorgan (cM)', 'Jednostka odległości na mapie genowej — 1% rekombinantów = 1 cM.'),
 ('Jak rozpoznać sprzężenie w krzyżówce testowej?', 'Zamiast stosunku 1:1:1:1 przeważają dwie klasy fenotypów rodzicielskich, a dwie klasy rekombinantów są nieliczne.'),
 ('Dlaczego częstość rekombinacji nie przekracza 50%?', 'Przy 50% wynik jest taki jak dla genów niesprzężonych — geny bardzo odległe zachowują się jak niezależne.'),
 ('Jak ustalić kolejność genów na mapie?', 'Na podstawie odległości (procentu rekombinacji) między parami genów — np. A–B 10 cM, B–C 4 cM, A–C 14 cM → kolejność A–B–C.'),
 ('Dlaczego Morgan prowadził badania na muszce owocowej?', 'Krótki cykl rozwojowy, liczne potomstwo, mała liczba chromosomów (4 pary), łatwa hodowla, wiele widocznych mutacji.'),
 ('Wyjaśnij pojęcie: układ cis i trans', 'Cis (sprzężenie) — allele dominujące na jednym chromosomie (AB/ab); trans (odpychanie) — na różnych (Ab/aB); ważne dla przewidywania gamet rodzicielskich.'),
], Q=[
 ('W krzyżówce testowej AaBb × aabb uzyskano: 45% AaBb, 45% aabb, 5% Aabb, 5% aaBb. Odległość genów wynosi:', ['5 cM', '*10 cM', '45 cM', '90 cM'], '10% rekombinantów.'),
 ('Przy genach sprzężonych w krzyżówce testowej przeważają:', ['rekombinanty', '*klasy rodzicielskie', 'wszystkie po równo', 'homozygoty dominujące'], 'Brak crossing-over w większości gamet.'),
 ('Odległość A–B = 12 cM, B–C = 5 cM, A–C = 7 cM. Kolejność genów to:', ['A–B–C', '*A–C–B', 'B–A–C', 'C–A–B'], 'C leży między A i B.'),
], pp='XIV.1.3–4')

T['b-plec'] = dict(F=[
 ('Chromosomowa determinacja płci u człowieka', 'XX — kobieta, XY — mężczyzna; płeć dziecka zależy od plemnika (X lub Y); gen SRY na chromosomie Y uruchamia rozwój jąder.'),
 ('Typy determinacji płci u zwierząt', 'XX/XY (ssaki, muszka), ZW/ZZ (ptaki, motyle — samica ZW heterogametyczna), X0 (niektóre owady), haplodiploidalność (pszczoły — samce n), temperaturowa (wiele gadów).'),
 ('Wyjaśnij pojęcie: cechy sprzężone z płcią', 'Cechy warunkowane genami leżącymi na chromosomie X (w odcinku niehomologicznym do Y) — inaczej dziedziczone u obu płci.'),
 ('Dlaczego choroby recesywne sprzężone z X częściej występują u mężczyzn?', 'Mężczyźni mają jeden chromosom X (hemizygoty) — jeden allel recesywny wystarcza do ujawnienia cechy; kobieta musi mieć dwa.'),
 ('Przykłady chorób recesywnych sprzężonych z chromosomem X', 'Hemofilia A, daltonizm (ślepota na barwy czerwoną i zieloną), dystrofia mięśniowa Duchenne’a.'),
 ('Po kim syn dziedziczy allel sprzężony z X?', 'Zawsze po matce (od ojca otrzymuje chromosom Y).'),
 ('Wyjaśnij pojęcie: nosicielka', 'Kobieta heterozygotyczna (XᴴXʰ) — zdrowa fenotypowo, ale może przekazać allel choroby; połowa jej synów może być chora.'),
 ('Potomstwo nosicielki daltonizmu i zdrowego mężczyzny (XᴰXᵈ × XᴰY)', 'Córki: 50% zdrowe, 50% nosicielki; synowie: 50% zdrowi, 50% chorzy.'),
 ('Czy chory na hemofilię ojciec może przekazać chorobę synowi?', 'Nie — synowi przekazuje chromosom Y; wszystkie jego córki będą nosicielkami.'),
 ('Wyjaśnij pojęcie: cechy związane z chromosomem Y (holandryczne)', 'Warunkowane genami tylko na chromosomie Y — przekazywane z ojca na wszystkich synów (np. SRY).'),
 ('Wyjaśnij pojęcie: cechy związane z płcią (ograniczone płcią)', 'Cechy warunkowane genami autosomalnymi, ale ujawniające się zależnie od płci, pod wpływem hormonów (np. łysienie androgenowe, rogi u owiec).'),
 ('Wyjaśnij pojęcie: dziedziczenie pozajądrowe (cytoplazmatyczne)', 'Dziedziczenie genów zawartych w mitochondriach i plastydach — zwykle wyłącznie po matce (komórka jajowa przekazuje cytoplazmę).'),
 ('Jak rozpoznać chorobę mitochondrialną w rodowodzie?', 'Chora matka przekazuje ją wszystkim dzieciom (obu płci); chory ojciec nie przekazuje jej nikomu.'),
 ('Zapis genotypów cech sprzężonych z X', 'Allel zapisuje się jako indeks przy X: kobieta XᴬXᵃ, mężczyzna XᵃY (Y bez allelu).'),
], Q=[
 ('Syn otrzymuje chromosom X od:', ['ojca', '*matki', 'obojga rodziców', 'losowo od jednego z rodziców'], 'Od ojca — Y.'),
 ('U ptaków płeć heterogametyczną (ZW) mają:', ['samce', '*samice', 'obie płcie', 'żadna'], 'Odwrotnie niż u ssaków.'),
 ('Dziecko chorej matki z chorobą mitochondrialną i zdrowego ojca:', ['zachoruje tylko syn', 'zachoruje tylko córka', '*może zachorować bez względu na płeć', 'nie zachoruje'], 'Mitochondria od matki.'),
 ('Chory na hemofilię mężczyzna i zdrowa (nienosicielka) kobieta. Ich córki będą:', ['chore', '*nosicielkami', 'zdrowe bez allelu', 'w połowie chore'], 'XᴴXʰ.'),
], pp='XIV.1.5–7')

T['b-rodowody'] = dict(F=[
 ('Oznaczenia w rodowodach', 'Kwadrat — mężczyzna, koło — kobieta; zamalowany — chory; pozioma linia — związek; pionowa — potomstwo; cyfry rzymskie — pokolenia.'),
 ('Cechy dziedziczenia autosomalnego dominującego w rodowodzie', 'Cecha w każdym pokoleniu, chory ma co najmniej jednego chorego rodzica, obie płcie jednakowo; dwoje chorych rodziców może mieć zdrowe dziecko.'),
 ('Cechy dziedziczenia autosomalnego recesywnego w rodowodzie', 'Cecha może przeskakiwać pokolenia, zdrowi rodzice (nosiciele) mogą mieć chore dziecko, obie płcie jednakowo.'),
 ('Cechy dziedziczenia recesywnego sprzężonego z X w rodowodzie', 'Chorują głównie mężczyźni; chory syn zwykle ma zdrową matkę-nosicielkę; chory ojciec nie przekazuje choroby synom; córki chorego ojca to nosicielki.'),
 ('Cechy dziedziczenia dominującego sprzężonego z X w rodowodzie', 'Chory ojciec przekazuje cechę wszystkim córkom i żadnemu synowi.'),
 ('Jak wykluczyć dziedziczenie dominujące?', 'Jeśli dwoje zdrowych rodziców ma chore dziecko — cecha jest recesywna.'),
 ('Jak wykluczyć dziedziczenie recesywne sprzężone z X?', 'Jeśli chora kobieta ma zdrowego syna albo zdrowy ojciec ma chorą córkę.'),
 ('Jak wykluczyć dziedziczenie autosomalne recesywne?', 'Jeśli dwoje chorych rodziców ma zdrowe dziecko (dla recesywnej oboje to aa, więc dzieci muszą być aa).'),
 ('Jak obliczyć ryzyko, że zdrowe rodzeństwo chorego (AR) jest nosicielem?', '2/3 — wśród zdrowych dzieci dwóch heterozygot (AA : 2 Aa) dwie trzecie to Aa.'),
 ('Dlaczego małżeństwa krewniacze zwiększają ryzyko chorób recesywnych?', 'Krewni częściej mają te same allele recesywne odziedziczone po wspólnym przodku — rośnie szansa homozygoty aa u dziecka.'),
], Q=[
 ('Dwoje zdrowych rodziców ma chore dziecko. Cecha jest:', ['dominująca', '*recesywna', 'mitochondrialna', 'holandryczna'], 'Rodzice nosicielami.'),
 ('Zdrowy ojciec ma chorą córkę. Wykluczono dziedziczenie:', ['autosomalne recesywne', '*recesywne sprzężone z X', 'autosomalne dominujące', 'mitochondrialne'], 'Córka otrzymała zdrowe X ojca.'),
 ('Prawdopodobieństwo, że zdrowy brat chorego na mukowiscydozę jest nosicielem:', ['1/4', '1/2', '*2/3', '3/4'], 'AA : 2Aa.'),
], pp='XIV.1.8')

T['b-mutacje'] = dict(F=[
 ('Wyjaśnij pojęcie: zmienność genetyczna i środowiskowa', 'Genetyczna (dziedziczna) — rekombinacyjna i mutacyjna; środowiskowa (fluktuacyjna) — zmiany fenotypu pod wpływem środowiska, niedziedziczne.'),
 ('Źródła zmienności rekombinacyjnej', 'Crossing-over, niezależna segregacja chromosomów w mejozie, losowe łączenie się gamet.'),
 ('Wyjaśnij pojęcie: mutacja', 'Nagła, trwała zmiana materiału genetycznego — genowa (punktowa), chromosomowa strukturalna lub liczbowa.'),
 ('Rodzaje mutacji punktowych', 'Substytucja (tranzycja, transwersja), delecja i insercja nukleotydów (przesunięcie ramki odczytu, jeśli nie o wielokrotność 3).'),
 ('Skutki substytucji', 'Cicha (bez zmiany aminokwasu), zmiany sensu (missens — inny aminokwas, np. anemia sierpowata), nonsens (kodon STOP — skrócone białko).'),
 ('Wyjaśnij pojęcie: mutacje chromosomowe strukturalne', 'Delecja (utrata fragmentu), duplikacja (podwojenie), inwersja (odwrócenie o 180°), translokacja (przeniesienie na inny chromosom).'),
 ('Wyjaśnij pojęcie: mutacje liczbowe — aneuploidie', 'Brak lub nadmiar pojedynczych chromosomów (2n−1 monosomia, 2n+1 trisomia) — skutek nondysjunkcji.'),
 ('Wyjaśnij pojęcie: euploidia (poliploidia)', 'Zmiana liczby całych zestawów chromosomów (3n, 4n) — autopoliploidy (zestawy tego samego gatunku) i allopoliploidy (różnych gatunków, np. pszenica).'),
 ('Dlaczego mieszańce międzygatunkowe są często bezpłodne, a allopoliploidy płodne?', 'U mieszańca chromosomy różnych gatunków nie tworzą par homologicznych w mejozie; po podwojeniu liczby chromosomów każdy ma parę — mejoza przebiega prawidłowo.'),
 ('Wyjaśnij pojęcie: mutacje somatyczne i generatywne', 'Somatyczne — w komórkach ciała, nie są dziedziczone (mogą prowadzić do nowotworu); generatywne — w komórkach płciowych, przekazywane potomstwu.'),
 ('Wyjaśnij pojęcie: mutacje spontaniczne i indukowane', 'Spontaniczne — błędy replikacji, naturalne uszkodzenia; indukowane — wywołane mutagenami.'),
 ('Znaczenie mutacji w ewolucji', 'Są pierwotnym źródłem nowych alleli (zmienności genetycznej), na które działa dobór naturalny.'),
], Q=[
 ('Zamiana kodonu na kodon STOP to mutacja:', ['cicha', 'zmiany sensu', '*nonsens', 'inwersja'], 'Skrócone białko.'),
 ('Trisomia jest przykładem:', ['poliploidii', '*aneuploidii', 'translokacji', 'mutacji punktowej'], '2n+1.'),
 ('Odwrócenie fragmentu chromosomu o 180° to:', ['delecja', 'duplikacja', '*inwersja', 'translokacja'], 'Mutacja strukturalna.'),
 ('Mutacje dziedziczone przez potomstwo zachodzą w komórkach:', ['somatycznych skóry', '*płciowych (linii generatywnej)', 'nowotworowych guza', 'mięśniowych serca'], 'Generatywne.'),
], pp='XIV.2.1–6')

T['b-choroby-genetyczne'] = dict(F=[
 ('Mukowiscydoza — dziedziczenie i przyczyna', 'Autosomalna recesywna; mutacja genu CFTR (kanał chlorkowy) — gęsty śluz w płucach, trzustce, przewodach — infekcje, zaburzenia trawienia.'),
 ('Fenyloketonuria — dziedziczenie i przyczyna', 'Autosomalna recesywna; brak enzymu przekształcającego fenyloalaninę w tyrozynę — fenyloalanina gromadzi się i uszkadza mózg; leczenie: dieta ubogofenyloalaninowa, badanie przesiewowe noworodków.'),
 ('Anemia sierpowata — przyczyna', 'Autosomalna recesywna; substytucja w genie β-globiny (Glu → Val) — hemoglobina S krystalizuje przy niskim O₂, erytrocyty sierpowate; heterozygoty odporniejsze na malarię.'),
 ('Pląsawica Huntingtona — dziedziczenie', 'Autosomalna dominująca; ekspansja powtórzeń CAG — zwyrodnienie neuronów, objawy zwykle po 35.–40. roku życia (po okresie rozrodczym).'),
 ('Achondroplazja — dziedziczenie', 'Autosomalna dominująca; zaburzenie wzrostu kości długich (karłowatość); homozygota dominująca letalna.'),
 ('Zespół Downa — przyczyna', 'Trisomia chromosomu 21 (47,XX+21 lub 47,XY+21) — najczęściej nondysjunkcja w oogenezie; ryzyko rośnie z wiekiem matki.'),
 ('Zespół Turnera — przyczyna i objawy', 'Monosomia X (45,X0) — kobieta niskiego wzrostu, niedorozwój jajników, bezpłodność.'),
 ('Zespół Klinefeltera — przyczyna i objawy', '47,XXY — mężczyzna wysoki, niedorozwój jąder, bezpłodność, czasem cechy żeńskie.'),
 ('Zespół Patau i Edwardsa', 'Trisomia 13 (Patau) i 18 (Edwardsa) — ciężkie wady, zwykle śmierć w pierwszym roku życia.'),
 ('Zespół „miauczenia kota” (cri du chat)', 'Delecja fragmentu krótkiego ramienia chromosomu 5 — niepełnosprawność intelektualna, charakterystyczny płacz.'),
 ('Wyjaśnij pojęcie: mutageny fizyczne, chemiczne i biologiczne', 'Fizyczne — promieniowanie UV, X, γ, wysoka temperatura; chemiczne — benzopiren (dym tytoniowy), azbest, barwniki, kolchicyna; biologiczne — niektóre wirusy (HPV, HBV), aflatoksyny.'),
 ('Jak promieniowanie UV uszkadza DNA?', 'Powoduje powstawanie dimerów tyminy (wiązania między sąsiednimi tyminami), zaburzających replikację i transkrypcję.'),
 ('Wyjaśnij pojęcie: nowotwór — przyczyna genetyczna', 'Nagromadzenie mutacji w protoonkogenach (→ onkogeny) i genach supresorowych — niekontrolowane podziały, unikanie apoptozy, zdolność do przerzutów.'),
 ('Wyjaśnij pojęcie: nowotwór łagodny i złośliwy', 'Łagodny — rośnie powoli, otoczony torebką, nie daje przerzutów; złośliwy — nacieka tkanki, tworzy przerzuty.'),
 ('Metody diagnostyki prenatalnej', 'Nieinwazyjne: USG, testy z krwi matki (wolne DNA płodu); inwazyjne: amniopunkcja, biopsja kosmówki — badanie kariotypu i DNA.'),
 ('Wyjaśnij pojęcie: poradnictwo genetyczne', 'Ocena ryzyka chorób genetycznych w rodzinie na podstawie rodowodu i badań, informowanie o możliwościach diagnostyki i profilaktyki.'),
], Q=[
 ('Zespół Downa to:', ['monosomia X', '*trisomia 21', 'delecja chromosomu 5', 'trisomia 13'], '47,+21.'),
 ('Fenyloketonurię leczy się:', ['insuliną', '*dietą ubogą w fenyloalaninę', 'przetaczaniem krwi', 'antybiotykami'], 'Brak enzymu.'),
 ('Pląsawica Huntingtona dziedziczy się w sposób:', ['autosomalny recesywny', '*autosomalny dominujący', 'recesywny sprzężony z X', 'mitochondrialny'], 'Objawy późno.'),
 ('Kariotyp 47,XXY to zespół:', ['Turnera', 'Downa', '*Klinefeltera', 'Patau'], 'Mężczyzna z dodatkowym X.'),
 ('Promieniowanie UV wywołuje w DNA powstawanie:', ['delecji chromosomu', '*dimerów tyminy', 'trisomii', 'inwersji'], 'Mutagen fizyczny.'),
], pp='XIV.2.7–9')
