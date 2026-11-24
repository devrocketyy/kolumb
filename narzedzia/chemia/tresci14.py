# Treści kursu chemii — porcja 14: fiszki do pozostałych tematów.
T = {}

T['c-atom'] = dict(F=[
 ('Liczba atomowa Z', 'Liczba protonów w jądrze (= liczba elektronów w obojętnym atomie).'),
 ('Liczba masowa A', 'Suma protonów i neutronów (nukleonów) w jądrze.'),
 ('Nuklid', 'Atom o określonej liczbie protonów i neutronów, zapis ᴬ_Z E.'),
 ('Izobary', 'Nuklidy o tej samej liczbie masowej, różnej liczbie atomowej (np. ⁴⁰Ar i ⁴⁰Ca).'),
 ('Masa protonu i neutronu', 'Ok. 1 u każda; elektron ok. 1/1840 u.'),
 ('Ładunek jonu a liczba elektronów', 'Kation Xⁿ⁺ ma o n elektronów mniej niż atom, anion Xⁿ⁻ — o n więcej.'),
 ('Drobiny izoelektronowe', 'Mają tę samą liczbę elektronów, np. Na⁺, Mg²⁺, F⁻, O²⁻, Ne (10 e⁻).'),
 ('Promień w szeregu izoelektronowym', 'Maleje ze wzrostem Z: O²⁻ > F⁻ > Na⁺ > Mg²⁺ > Al³⁺.'),
 ('Model atomu — orbital', 'Obszar przestrzeni, w którym prawdopodobieństwo znalezienia elektronu jest największe.'),
 ('Kształty orbitali', 's — kula, p — „ósemka” (3 orientacje), d — 5 orbitali o złożonych kształtach.'),
])

T['c-konfiguracja'] = dict(F=[
 ('Liczby kwantowe — zestaw', 'n (główna, powłoka), l (poboczna, podpowłoka: 0 s, 1 p, 2 d, 3 f), m (magnetyczna, orbital), mₛ (spinowa, ±½).'),
 ('Zakaz Pauliego', 'W atomie nie ma dwóch elektronów o identycznych czterech liczbach kwantowych → max 2 e⁻ na orbitalu, o przeciwnych spinach.'),
 ('Reguła Hunda', 'Elektrony zajmują orbitale tej samej podpowłoki najpierw pojedynczo, ze zgodnymi spinami.'),
 ('Kolejność zapełniania podpowłok', '1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p …'),
 ('Wartości m dla l = 2', '−2, −1, 0, 1, 2 (5 orbitali d).'),
 ('Zapis skrócony konfiguracji', 'Rdzeń gazu szlachetnego w nawiasie: Fe [Ar] 3d⁶ 4s².'),
 ('Elektrony walencyjne pierwiastków bloku d', 'Elektrony ns i (n−1)d, np. Mn: 4s² 3d⁵ — 7 elektronów walencyjnych.'),
 ('Stan wzbudzony', 'Elektron przeniesiony na wyższą (pustą) podpowłokę, np. C*: 2s¹ 2p³ — tłumaczy czterowartościowość węgla.'),
 ('Konfiguracja jonu Fe²⁺', '[Ar] 3d⁶ (usuwamy 2 elektrony 4s).'),
 ('Pułapka: schemat klatkowy', 'Trzeba podpisać powłoki i podpowłoki; elektrony niesparowane — zgodne spiny.'),
])

T['c-okresowosc'] = dict(F=[
 ('Prawo okresowości', 'Właściwości pierwiastków są okresową funkcją liczby atomowej.'),
 ('Numer okresu', 'Liczba powłok elektronowych w atomie.'),
 ('Numer grupy (bloki s i p)', 'Grupy 1–2: liczba elektronów walencyjnych; 13–18: liczba elektronów walencyjnych + 10.'),
 ('Energia jonizacji w okresie', 'Rośnie od lewej do prawej (z wyjątkami: grupa 13 < 2, grupa 16 < 15).'),
 ('Elektroujemność — trend', 'Rośnie w okresie w prawo, maleje w grupie w dół.'),
 ('Charakter tlenków w okresie 3', 'Na₂O, MgO — zasadowe; Al₂O₃ — amfoteryczny; SiO₂, P₄O₁₀, SO₃, Cl₂O₇ — kwasowe.'),
 ('Wodorki w okresie 2', 'LiH (jonowy, zasadowy) … CH₄ (obojętny) … HF (kwasowy w wodzie).'),
 ('Metaloidy (półmetale)', 'B, Si, Ge, As, Sb, Te — pośrednie właściwości.'),
 ('Maksymalny stopień utlenienia', 'Zwykle równy liczbie elektronów walencyjnych (S: +VI, Cl: +VII, Mn: +VII).'),
 ('Promień atomowy w okresie', 'Maleje od lewej do prawej (rośnie ładunek jądra, ta sama liczba powłok).'),
])

T['c-promieniotworczosc'] = dict(F=[
 ('Promieniowanie α', 'Jądra helu ⁴₂He; małą przenikliwość (zatrzymuje je kartka papieru).'),
 ('Promieniowanie β⁻', 'Elektrony z jądra (n → p + e⁻); zatrzymuje je cienka blacha aluminiowa.'),
 ('Promieniowanie β⁺', 'Pozytony (p → n + e⁺); Z maleje o 1.'),
 ('Promieniowanie γ', 'Fale elektromagnetyczne o dużej energii; bardzo przenikliwe (ołów, beton).'),
 ('Wychwyt elektronu (K)', 'Jądro pochłania elektron z powłoki K: p + e⁻ → n; Z maleje o 1.'),
 ('Okres półtrwania T½', 'Czas, po którym rozpada się połowa jąder; nie zależy od masy próbki ani warunków.'),
 ('Masa po n okresach półtrwania', 'm = m₀ · (½)ⁿ.'),
 ('Szereg promieniotwórczy', 'Ciąg przemian α i β kończący się trwałym izotopem (zwykle ołowiu).'),
 ('Datowanie radiowęglowe', '¹⁴C (T½ ≈ 5730 lat) — określanie wieku szczątków organicznych.'),
 ('Reakcja rozszczepienia', 'Ciężkie jądro (²³⁵U) po pochłonięciu neutronu dzieli się na dwa lżejsze i 2–3 neutrony (reakcja łańcuchowa).'),
 ('Zastosowania izotopów', 'Medycyna (¹³¹I — tarczyca, ⁶⁰Co — radioterapia), znaczniki, energetyka jądrowa.'),
])

T['c-wiazania'] = dict(F=[
 ('Wiązanie kowalencyjne spolaryzowane', 'Wspólna para elektronów przesunięta w stronę atomu bardziej elektroujemnego (H–Cl, H–O).'),
 ('Wiązanie σ', 'Powstaje przez czołowe nakładanie orbitali; każde wiązanie pojedyncze to σ.'),
 ('Wiązanie π', 'Boczne nakładanie orbitali p; występuje w wiązaniach podwójnych (1π) i potrójnych (2π).'),
 ('Wiązanie koordynacyjne (donorowo-akceptorowe)', 'Para elektronów pochodzi od jednego atomu (donora), np. NH₄⁺, H₃O⁺, kompleksy.'),
 ('Związki jonowe — właściwości', 'Wysokie temperatury topnienia, kruche, przewodzą w stopie i roztworze, często dobrze rozpuszczalne w wodzie.'),
 ('Związki kowalencyjne — właściwości', 'Często niskie temperatury topnienia i wrzenia, nie przewodzą prądu (wyjątek: grafit).'),
 ('Energia wiązania', 'Energia potrzebna do rozerwania 1 mola wiązań; rośnie z krotnością: C–C < C=C < C≡C.'),
 ('Długość wiązania', 'Maleje z krotnością: C–C 154 pm, C=C 134 pm, C≡C 120 pm.'),
 ('Reguła oktetu i wyjątki', 'Atomy dążą do 8 elektronów walencyjnych; wyjątki: BF₃, AlCl₃ (sekstet), PCl₅, SF₆ (rozszerzony oktet).'),
 ('Wzór elektronowy kreskowy', 'Kreska = para elektronowa (wiążąca lub wolna); zaznaczyć wszystkie wolne pary!'),
])

T['c-geometria'] = dict(F=[
 ('Metoda VSEPR — zasada', 'Pary elektronowe (wiążące i wolne) wokół atomu centralnego odpychają się i rozmieszczają jak najdalej od siebie.'),
 ('Liczba przestrzenna Lp', 'Lp = liczba atomów związanych z atomem centralnym + liczba jego wolnych par.'),
 ('Lp = 2', 'Hybrydyzacja sp, kształt liniowy (CO₂, BeCl₂, HCN).'),
 ('Lp = 3', 'sp², trygonalny płaski (BF₃, SO₃) lub kątowy przy 1 wolnej parze (SO₂).'),
 ('Lp = 4', 'sp³: tetraedr (CH₄), piramida trygonalna (NH₃, 1 wolna para), kątowy (H₂O, 2 wolne pary).'),
 ('Kąty: CH₄, NH₃, H₂O', '109,5°, 107°, 104,5° — wolne pary odpychają silniej.'),
 ('Lp = 5 i 6', 'Bipiramida trygonalna (PCl₅) i oktaedr (SF₆).'),
 ('Hybrydyzacja w CO₃²⁻ i NO₃⁻', 'sp², płaski trójkąt; ładunek zdelokalizowany.'),
 ('Hybrydyzacja w NH₄⁺', 'sp³, tetraedr.'),
 ('Liczba wiązań σ i π w HC≡N', '2σ i 2π.'),
])

T['c-izomeria'] = dict(F=[
 ('Izomeria konstytucyjna', 'Różna kolejność łączenia atomów: łańcuchowa, położenia, funkcyjna.'),
 ('Izomeria łańcuchowa', 'Różny szkielet węglowy: butan i 2-metylopropan.'),
 ('Izomeria położenia', 'Różne położenie grupy funkcyjnej lub wiązania wielokrotnego: propan-1-ol i propan-2-ol.'),
 ('Izomeria funkcyjna', 'Różne grupy funkcyjne: etanol i eter dimetylowy; aldehyd i keton; kwas i ester.'),
 ('Stereoizomeria', 'Ta sama kolejność atomów, inne rozmieszczenie w przestrzeni: geometryczna (cis–trans) i optyczna.'),
 ('Warunek izomerii cis–trans', 'Wiązanie podwójne (lub pierścień), a przy każdym atomie węgla wiązania — dwa różne podstawniki.'),
 ('Enancjomery', 'Stereoizomery będące swoimi lustrzanymi odbiciami; skręcają płaszczyznę światła spolaryzowanego w przeciwne strony.'),
 ('Diastereoizomery', 'Stereoizomery, które nie są enancjomerami (np. D-glukoza i D-galaktoza).'),
 ('Mieszanina racemiczna', 'Równomolowa mieszanina enancjomerów — optycznie nieczynna.'),
 ('Forma mezo', 'Ma asymetryczne atomy węgla, ale i płaszczyznę symetrii — achiralna (kwas mezo-winowy).'),
 ('Maksymalna liczba stereoizomerów optycznych', '2ⁿ, gdzie n — liczba asymetrycznych atomów węgla (mniej, gdy istnieje forma mezo).'),
])

T['c-alkohole'] = dict(F=[
 ('Rzędowość alkoholu', 'Liczba atomów węgla połączonych z węglem niosącym –OH: I, II, III.'),
 ('Alkohole a sód', '2ROH + 2Na → 2RONa + H₂ (alkoholan).'),
 ('Odczyn wodnego roztworu alkoholu', 'Obojętny (alkohole są słabszymi kwasami niż woda).'),
 ('Dehydratacja alkoholi', 'Stęż. H₂SO₄ lub Al₂O₃, wysoka temperatura → alken (wewnątrzcząsteczkowa) lub eter (międzycząsteczkowa).'),
 ('Utlenianie alkoholi I-rzędowych', 'Aldehyd → kwas karboksylowy.'),
 ('Etanol — otrzymywanie', 'Fermentacja alkoholowa glukozy: C₆H₁₂O₆ → 2C₂H₅OH + 2CO₂; hydratacja etenu.'),
 ('Metanol', 'Silnie trujący (ślepota); otrzymywany z CO i H₂.'),
 ('Glikol etylenowy', 'Etano-1,2-diol — płyn do chłodnic, substrat do PET.'),
 ('Glicerol', 'Propano-1,2,3-triol — z Cu(OH)₂ szafirowy roztwór; składnik tłuszczów.'),
 ('Fenole a alkohole', 'Fenole mają –OH przy pierścieniu, są słabymi kwasami (reagują z NaOH), dają barwne związki z FeCl₃.'),
 ('Rozpuszczalność alkoholi', 'Metanol, etanol, propanol mieszają się z wodą; dłuższe łańcuchy — coraz gorzej.'),
])

T['c-aminokwasy'] = dict(F=[
 ('Budowa α-aminokwasu', 'Grupa –NH₂ i –COOH przy tym samym (α) atomie węgla, plus łańcuch boczny R.'),
 ('Jon obojnaczy', '⁺H₃N–CHR–COO⁻ — forma aminokwasu w roztworze o pH bliskim pI i w stanie stałym.'),
 ('Właściwości amfoteryczne aminokwasów', 'Reagują z kwasami (grupa –NH₂) i z zasadami (grupa –COOH).'),
 ('Punkt izoelektryczny (pI)', 'pH, w którym aminokwas nie wędruje w polu elektrycznym (ładunek wypadkowy 0).'),
 ('Aminokwasy białkowe — konfiguracja', 'Szereg L (wszystkie oprócz achiralnej glicyny).'),
 ('Aminokwasy kwasowe', 'Kwas asparaginowy i glutaminowy (dodatkowa –COOH) — pI ok. 3.'),
 ('Aminokwasy zasadowe', 'Lizyna, arginina, histydyna (dodatkowa grupa aminowa) — pI wysokie.'),
 ('Aminokwasy siarkowe', 'Cysteina (–SH, tworzy mostki disiarczkowe) i metionina.'),
 ('Liczba dipeptydów z dwóch różnych aminokwasów', '4 (A-A, B-B, A-B, B-A); bez powtórzeń — 2.'),
 ('Hydroliza peptydów', 'Rozpad wiązań peptydowych (kwas, zasada lub enzymy) → aminokwasy.'),
 ('Masa peptydu', 'Suma mas aminokwasów − (n − 1)·18 g/mol (woda z każdego wiązania).'),
])

T['c-stopnie'] = dict(F=[
 ('Reguły ustalania stopnia utlenienia', 'Pierwiastki = 0; F zawsze −I; O zwykle −II (nadtlenki −I, OF₂ +II); H zwykle +I (wodorki metali −I); suma = ładunek drobiny.'),
 ('Stopień utlenienia w jonie', 'Suma stopni = ładunek jonu: w SO₄²⁻ siarka +VI.'),
 ('Stopień utlenienia chromu w K₂Cr₂O₇', '+VI.'),
 ('Stopień utlenienia azotu: NH₃, N₂, NO, NO₂, HNO₃', '−III, 0, +II, +IV, +V.'),
 ('Stopień utlenienia wodoru w NaH', '−I (wodorek metalu).'),
 ('Stopień utlenienia węgla w CH₃OH', '−II.'),
 ('Średni stopień utlenienia', 'Może być ułamkowy, np. Fe w Fe₃O₄: +8/3; S w S₄O₆²⁻: +2,5.'),
 ('Utlenianie i redukcja', 'Utlenianie — wzrost stopnia utlenienia (oddanie e⁻); redukcja — spadek (przyjęcie e⁻).'),
 ('Utleniacz a reduktor', 'Utleniacz się redukuje, reduktor się utlenia.'),
 ('Substancje, które mogą być i utleniaczem, i reduktorem', 'Na pośrednim stopniu utlenienia: H₂O₂, SO₂, NO₂⁻, Fe²⁺.'),
])

T['c-polecenia'] = dict(F=[
 ('Polecenie „Oceń prawdziwość”', 'Każde zdanie osobno P/F; punkt zwykle za wszystkie poprawne.'),
 ('Polecenie „Wyjaśnij”', 'Mechanizm/przyczyna zjawiska — łańcuch: budowa → właściwość → obserwacja.'),
 ('Polecenie „Rozstrzygnij”', 'Jednoznaczna odpowiedź (tak/nie, I/II) + uzasadnienie, jeśli polecenie go wymaga.'),
 ('Polecenie „Zaprojektuj doświadczenie”', 'Wybrać odczynniki z listy, opisać czynności i spodziewane obserwacje dla każdej substancji.'),
 ('„Napisz wzór półstrukturalny (grupowy)”', 'Wszystkie grupy w poprawnej kolejności; zapis –COH zamiast –CHO = błąd.'),
 ('„Napisz w formie jonowej z uwzględnieniem liczby elektronów”', 'Równanie połówkowe z e⁻, w formie jonowej, ze środowiskiem.'),
 ('Zaznaczanie odpowiedzi w nawiasach', 'Podkreślić/zakreślić dokładnie jedną opcję w KAŻDYM nawiasie.'),
 ('Wynik z dokładnością', 'Zaokrąglaj dopiero na końcu; wynik podaj z żądaną dokładnością i jednostką.'),
])

T['c-obliczenia'] = dict(F=[
 ('Cyfry znaczące — zasada', 'Wynik podaje się z taką dokładnością jak najmniej dokładna dana (lub jak każe polecenie).'),
 ('Przeliczenia objętości', '1 dm³ = 1000 cm³ = 1 L; 1 m³ = 1000 dm³.'),
 ('Przeliczenia ciśnienia', '1013 hPa = 1 atm = 101,3 kPa.'),
 ('Logarytmy w pH', 'log(a·10ⁿ) = log a + n; np. −log(2·10⁻³) = 2,7.'),
 ('Proporcja vs wzór', 'Obie metody są poprawne, ale tok rozumowania musi być widoczny — sam wynik = 0 pkt.'),
 ('Sprawdzenie sensu wyniku', 'Stężenie % < 100, wydajność ≤ 100%, pH 0–14, masa produktu realna.'),
 ('Błąd metody vs błąd rachunkowy', 'Zła zależność (np. pominięcie współczynnika) = 0 pkt; pomyłka w działaniu = zwykle −1 pkt.'),
 ('Stałe z karty wzorów', 'Nₐ = 6,02·10²³, R = 8,314 J·mol⁻¹·K⁻¹ (83,14 hPa·dm³·mol⁻¹·K⁻¹), F = 96 500 C·mol⁻¹, Vm = 22,4 dm³·mol⁻¹.'),
])

T['c-doswiadczenia'] = dict(F=[
 ('Sączenie', 'Oddzielenie osadu od cieczy przez lejek z sączkiem; ilościowe wyodrębnianie osadu.'),
 ('Dekantacja', 'Zlewanie cieczy znad osadu po jego opadnięciu (nie jest ilościowa).'),
 ('Destylacja', 'Rozdzielanie cieczy o różnych temperaturach wrzenia.'),
 ('Ekstrakcja', 'Przeniesienie substancji do rozpuszczalnika, w którym lepiej się rozpuszcza (rozdzielacz).'),
 ('Krystalizacja', 'Wydzielanie kryształów z roztworu przez odparowanie lub ochłodzenie.'),
 ('Chromatografia', 'Rozdział składników na podstawie różnej szybkości wędrówki w fazie stacjonarnej.'),
 ('Miareczkowanie — sprzęt', 'Biureta (titrant), kolba stożkowa (analit), pipeta, wskaźnik.'),
 ('Wykrywanie CO₂', 'Woda wapienna mętnieje: Ca(OH)₂ + CO₂ → CaCO₃↓ + H₂O.'),
 ('Wykrywanie H₂', 'Zapalone łuczywko — charakterystyczny „szczek” (próba wybuchowa).'),
 ('Wykrywanie O₂', 'Tlące się łuczywko rozżarza się.'),
 ('Wykrywanie NH₃', 'Zapach; wilgotny uniwersalny papierek zabarwia się na niebiesko.'),
])
