# Treści kursu chemii — porcja 26: pytania ABCD na poziomie maturalnym (obliczenia, pułapki, rozumowanie).
T = {}

T['c-atom'] = dict(Q=[
 ('Jon ⁵⁶Fe³⁺ zawiera:', ['*26 p, 30 n, 23 e⁻', '26 p, 30 n, 29 e⁻', '26 p, 56 n, 23 e⁻', '23 p, 30 n, 26 e⁻'], 'Z = 26 protonów, 56 − 26 = 30 neutronów, kation 3+ ma o 3 elektrony mniej.'),
 ('Chlor ma średnią masę atomową 35,45 u i izotopy ³⁵Cl i ³⁷Cl. Zawartość ³⁷Cl wynosi ok.:', ['*22,5%', '45,0%', '77,5%', '35,5%'], '35x + 37(1 − x) = 35,45 → x = 0,775, czyli ³⁷Cl stanowi 22,5%.'),
 ('Izotopy tego samego pierwiastka różnią się:', ['*liczbą neutronów', 'liczbą protonów', 'liczbą elektronów', 'ładunkiem jądra'], 'Liczba atomowa jest ta sama, inna liczba masowa.'),
 ('Drobiny izoelektronowe to:', ['*Na⁺, Mg²⁺, F⁻', 'Na, Mg, Al', 'Cl⁻, Br⁻, I⁻', 'Na⁺, K⁺, Rb⁺'], 'Wszystkie mają po 10 elektronów (konfiguracja neonu).'),
])

T['c-konfiguracja'] = dict(Q=[
 ('Liczba niesparowanych elektronów w atomie Fe w stanie podstawowym to:', ['*4', '2', '6', '0'], '3d⁶: jeden orbital podwójnie zajęty, cztery pojedynczo.'),
 ('Elektron opisany liczbami n = 3, l = 2 należy do podpowłoki:', ['*3d', '3p', '2d', '3s'], 'l = 2 oznacza podpowłokę d; podpowłoka 2d nie istnieje.'),
 ('Konfiguracja [Ar] 3d⁵ odpowiada jonowi:', ['*Fe³⁺', 'Fe²⁺', 'Cr³⁺', 'Co²⁺'], 'Fe: [Ar] 4s² 3d⁶ — po oddaniu trzech elektronów zostaje 3d⁵.'),
 ('Maksymalna liczba elektronów na powłoce n = 3 wynosi:', ['*18', '8', '32', '9'], '2n² = 18 (3s, 3p, 3d).'),
 ('Atom w stanie podstawowym ma 3 elektrony na podpowłoce 4p. To:', ['*arsen', 'azot', 'fosfor', 'gal'], '[Ar] 4s² 3d¹⁰ 4p³ — grupa 15, okres 4.'),
])

T['c-okresowosc'] = dict(Q=[
 ('Największy promień spośród podanych ma:', ['*S²⁻', 'Cl⁻', 'K⁺', 'Ca²⁺'], 'Drobiny izoelektronowe: im mniejszy ładunek jądra, tym większy promień.'),
 ('Pierwsza energia jonizacji jest najwyższa dla:', ['*neonu', 'sodu', 'fluoru', 'tlenu'], 'Gaz szlachetny o zamkniętej powłoce i małym promieniu.'),
 ('W okresie 3 od Na do Cl:', ['*rośnie elektroujemność', 'rośnie promień atomu', 'maleje liczba elektronów walencyjnych', 'rośnie charakter metaliczny'], 'Rośnie ładunek jądra przy tej samej liczbie powłok.'),
])

T['c-promieniotworczosc'] = dict(Q=[
 ('W przemianie β⁻ liczba masowa:', ['*nie zmienia się', 'rośnie o 1', 'maleje o 4', 'maleje o 1'], 'Neutron przechodzi w proton — A bez zmian, Z rośnie o 1.'),
 ('²²⁶Ra po przemianie α daje:', ['*²²²Rn', '²²²Po', '²³⁰Th', '²²⁶Ac'], 'A − 4, Z − 2: z radu (88) powstaje radon (86).'),
 ('Promieniowanie najbardziej przenikliwe to:', ['*γ', 'α', 'β⁻', 'β⁺'], 'Fala elektromagnetyczna, zatrzymuje ją dopiero gruba warstwa ołowiu.'),
])

T['c-wiazania'] = dict(Q=[
 ('Wiązanie jonowe tworzą pierwiastki o różnicy elektroujemności zwykle:', ['*powyżej ok. 1,7', 'równej zero', 'od 0,4 do 1,0', 'poniżej 0,4'], 'Duża różnica — przeniesienie elektronów.'),
 ('Liczba wiązań σ i π w cząsteczce C₂H₂ to:', ['*3 σ i 2 π', '2 σ i 3 π', '5 σ i 0 π', '3 σ i 1 π'], 'Dwa wiązania C–H i jedno σ C≡C oraz dwa π.'),
 ('Metale przewodzą prąd, ponieważ:', ['*mają zdelokalizowane elektrony', 'tworzą jony w roztworze', 'mają wiązania kowalencyjne', 'mają małą gęstość'], 'Gaz elektronowy swobodnie przemieszcza się w sieci.'),
])

T['c-geometria'] = dict(Q=[
 ('Cząsteczką niepolarną z wiązaniami polarnymi jest:', ['*CCl₄', 'NH₃', 'H₂O', 'HCl'], 'Tetraedr symetryczny — momenty dipolowe się znoszą.'),
 ('Kształt cząsteczki NH₃ to:', ['*piramida trygonalna', 'tetraedr', 'trójkąt płaski', 'cząsteczka liniowa'], 'Hybrydyzacja sp³, jedna wolna para na azocie.'),
 ('Hybrydyzacja atomu węgla w CO₂ to:', ['*sp', 'sp²', 'sp³', 'brak'], 'Dwa wiązania podwójne, cząsteczka liniowa.'),
 ('Kąt H–O–H w cząsteczce wody jest mniejszy niż w tetraedrze, ponieważ:', ['*wolne pary odpychają silniej', 'tlen ma hybrydyzację sp²', 'wiązania są jonowe', 'wodór jest elektroujemny'], 'Dwie wolne pary ściskają kąt do ok. 104,5°.'),
])

T['c-oddzialywania'] = dict(Q=[
 ('Etanol miesza się z wodą bez ograniczeń, ponieważ:', ['*tworzy z nią wiązania wodorowe', 'jest związkiem jonowym', 'ma większą gęstość', 'jest niepolarny'], 'Grupa –OH oddziałuje z cząsteczkami wody.'),
 ('Jod lepiej rozpuszcza się w heksanie niż w wodzie, ponieważ:', ['*oba są niepolarne', 'jod jest jonowy', 'heksan tworzy wiązania wodorowe', 'woda ma małą gęstość'], 'Podobne rozpuszcza się w podobnym.'),
])

T['c-mol'] = dict(Q=[
 ('Liczba atomów w 0,5 mola H₂O to ok.:', ['*9,03 · 10²³', '3,01 · 10²³', '6,02 · 10²³', '1,81 · 10²⁴'], '0,5 · 3 · 6,02 · 10²³.'),
 ('Objętość 8,8 g CO₂ w warunkach normalnych to:', ['*4,48 dm³', '2,24 dm³', '8,96 dm³', '22,4 dm³'], '8,8/44 = 0,2 mola · 22,4 dm³.'),
 ('Gęstość gazu w warunkach normalnych wynosi 1,25 g/dm³. Jego masa molowa to:', ['*28 g/mol', '32 g/mol', '14 g/mol', '44 g/mol'], 'M = d · 22,4 = 28 g/mol (N₂ lub CO).'),
 ('Masa jednej cząsteczki O₂ to ok.:', ['*5,3 · 10⁻²³ g', '3,2 · 10⁻²³ g', '2,7 · 10⁻²³ g', '1,9 · 10⁻²² g'], '32 g / 6,02 · 10²³.'),
])

T['c-wzory'] = dict(Q=[
 ('Związek zawiera 40% C, 6,7% H i 53,3% O. Wzór empiryczny to:', ['*CH₂O', 'CHO', 'C₂H₄O', 'CH₄O'], 'Stosunek moli 3,33 : 6,7 : 3,33 = 1 : 2 : 1.'),
 ('Zawartość procentowa azotu w NH₄NO₃ wynosi:', ['*35%', '17,5%', '46,7%', '28%'], '28/80 = 0,35.'),
 ('Wzór rzeczywisty związku o wzorze empirycznym CH i M = 78 g/mol:', ['*C₆H₆', 'C₂H₂', 'C₄H₄', 'C₈H₈'], '78 / 13 = 6.'),
])

T['c-stechiometria'] = dict(Q=[
 ('Ile gramów CaO powstaje z rozkładu 50 g CaCO₃?', ['*28 g', '56 g', '22 g', '14 g'], '0,5 mola CaCO₃ → 0,5 mola CaO · 56 g/mol.'),
 ('Zmieszano 2 mole H₂ i 2 mole O₂. Po reakcji pozostaje:', ['*1 mol O₂', '1 mol H₂', '0,5 mola O₂', 'nic'], '2H₂ + O₂ → 2H₂O — tlen w nadmiarze.'),
 ('Z 10 g H₂ otrzymano 34 g NH₃. Wydajność wynosi ok.:', ['*60%', '50%', '85%', '30%'], 'Teoretycznie 5 mol H₂ → 3,33 mol NH₃ = 56,7 g; 34/56,7 = 0,6.'),
 ('Ile dm³ O₂ (w. n.) potrzeba do spalenia 1 mola CH₄?', ['*44,8 dm³', '22,4 dm³', '67,2 dm³', '11,2 dm³'], 'CH₄ + 2O₂ → CO₂ + 2H₂O.'),
])

T['c-energetyka'] = dict(Q=[
 ('Prawo Hessa mówi, że ΔH reakcji:', ['*nie zależy od drogi przemiany', 'zależy od katalizatora', 'rośnie z czasem', 'równa się Eₐ'], 'Entalpia jest funkcją stanu.'),
 ('Rozpuszczaniu NH₄NO₃ w wodzie towarzyszy ochłodzenie roztworu. Proces jest:', ['*endotermiczny', 'egzotermiczny', 'termoneutralny', 'jądrowy'], 'Układ pobiera ciepło z otoczenia.'),
])

T['c-szybkosc'] = dict(Q=[
 ('Dla v = k[A]²[B] dwukrotny wzrost [A] przy stałym [B] zwiększa szybkość:', ['*4 razy', '2 razy', '8 razy', '6 razy'], '2² = 4.'),
 ('Rozdrobnienie ciała stałego przyspiesza reakcję, ponieważ:', ['*zwiększa powierzchnię kontaktu', 'obniża ΔH', 'podnosi temperaturę', 'zmienia stałą K'], 'Więcej zderzeń na powierzchni.'),
])

T['c-rownowaga'] = dict(Q=[
 ('Dla N₂ + 3H₂ ⇄ 2NH₃ (ΔH < 0) wydajność NH₃ zwiększy:', ['*wzrost ciśnienia', 'wzrost temperatury', 'dodanie katalizatora', 'usunięcie N₂'], 'Mniej moli gazów po stronie produktów.'),
 ('W wyrażeniu na stałą równowagi CaCO₃(s) ⇄ CaO(s) + CO₂(g) występuje tylko:', ['*[CO₂]', '[CaO]/[CaCO₃]', '[CaO][CO₂]', '[CaCO₃]'], 'Stężeń ciał stałych nie wpisuje się do K.'),
 ('Dla H₂ + I₂ ⇄ 2HI wzrost ciśnienia:', ['*nie przesuwa równowagi', 'przesuwa ją w prawo', 'przesuwa ją w lewo', 'zmienia wartość K'], 'Po obu stronach 2 mole gazów.'),
])

T['c-stezenia'] = dict(Q=[
 ('Stężenie procentowe roztworu: 20 g soli w 180 g wody:', ['*10%', '11,1%', '20%', '9%'], '20 / 200 · 100%.'),
 ('Stężenie molowe roztworu: 4 g NaOH w 250 cm³ roztworu:', ['*0,4 mol/dm³', '0,1 mol/dm³', '1,6 mol/dm³', '0,25 mol/dm³'], '0,1 mola / 0,25 dm³.'),
 ('Stężenie molowe 36,5% HCl o gęstości 1,18 g/cm³ to ok.:', ['*11,8 mol/dm³', '10,0 mol/dm³', '36,5 mol/dm³', '1,18 mol/dm³'], 'c = cₚ · d · 10 / M = 36,5 · 1,18 · 10 / 36,5.'),
])

T['c-rozpuszczalnosc'] = dict(Q=[
 ('Rozpuszczalność soli wynosi 40 g/100 g wody. Stężenie roztworu nasyconego to:', ['*28,6%', '40%', '33,3%', '25%'], '40 / 140.'),
 ('Roztwór, w którym w danej temperaturze można jeszcze rozpuścić substancję, jest:', ['*nienasycony', 'nasycony', 'przesycony', 'koloidalny'], 'Stężenie poniżej rozpuszczalności.'),
])

T['c-mieszanie'] = dict(Q=[
 ('Zmieszano 100 g 10% i 300 g 30% roztworu tej samej soli. Stężenie to:', ['*25%', '20%', '40%', '22,5%'], '(10 + 90) / 400.'),
 ('Do 200 g 15% roztworu dodano 100 g wody. Stężenie to:', ['*10%', '7,5%', '15%', '5%'], '30 g / 300 g.'),
 ('Ile wody trzeba odparować z 500 g 8% roztworu, aby otrzymać 10%?', ['*100 g', '50 g', '40 g', '125 g'], '40 g soli w 400 g roztworu.'),
])

T['c-kwasy-zasady'] = dict(Q=[
 ('Zasadą sprzężoną z HSO₄⁻ jest:', ['*SO₄²⁻', 'H₂SO₄', 'H₃O⁺', 'OH⁻'], 'Kwas oddaje proton — powstaje zasada sprzężona.'),
 ('Amfolitem Brønsteda jest:', ['*HCO₃⁻', 'CO₃²⁻', 'NH₄⁺', 'Cl⁻'], 'Może oddać lub przyjąć proton.'),
 ('Najsłabszym kwasem spośród podanych jest (największe pKa):', ['*HCN', 'HF', 'CH₃COOH', 'HNO₂'], 'pKa HCN ≈ 9,2.'),
])

T['c-ph'] = dict(Q=[
 ('pH roztworu HCl o stężeniu 0,01 mol/dm³ wynosi:', ['*2', '1', '12', '0,01'], '[H⁺] = 10⁻².'),
 ('Roztwór HCl o pH = 3 rozcieńczono 10 razy. pH wynosi:', ['*4', '2', '3', '30'], 'Stężenie H⁺ spada 10-krotnie.'),
 ('Stopień dysocjacji słabego kwasu po rozcieńczeniu roztworu:', ['*rośnie', 'maleje', 'nie zmienia się', 'spada do zera'], 'Prawo rozcieńczeń Ostwalda: α ≈ √(K/c).'),
 ('pH kwasu octowego 0,1 mol/dm³ (Ka = 1,8 · 10⁻⁵) wynosi ok.:', ['*2,9', '1,0', '4,7', '3,9'], '[H⁺] = √(1,8 · 10⁻⁶) ≈ 1,34 · 10⁻³.'),
])

T['c-hydroliza'] = dict(Q=[
])

T['c-jonowe'] = dict(Q=[
 ('Osad nie powstanie po zmieszaniu roztworów:', ['*KCl i NaNO₃', 'AgNO₃ i NaCl', 'BaCl₂ i Na₂SO₄', 'CuSO₄ i NaOH'], 'Wszystkie możliwe produkty są rozpuszczalne.'),
 ('Równanie jonowe skrócone zobojętniania HCl przez NaOH:', ['*H⁺ + OH⁻ → H₂O', 'Na⁺ + Cl⁻ → NaCl', 'HCl + OH⁻ → Cl⁻ + H₂O', 'H⁺ + NaOH → Na⁺ + H₂O'], 'Jony Na⁺ i Cl⁻ są jonami obojętnymi.'),
 ('Biały osad, który ciemnieje na świetle, tworzą:', ['*Ag⁺ i Cl⁻', 'Ba²⁺ i SO₄²⁻', 'Cu²⁺ i OH⁻', 'Fe³⁺ i OH⁻'], 'AgCl rozkłada się pod wpływem światła.'),
])

T['c-tlenki'] = dict(Q=[
 ('Tlenek kwasowy reaguje z:', ['*zasadami', 'kwasami', 'tylko z wodą', 'metalami szlachetnymi'], 'Powstaje sól i woda.'),
 ('Charakter tlenków chromu zmienia się od CrO do CrO₃:', ['*z zasadowego na kwasowy', 'z kwasowego na zasadowy', 'pozostaje amfoteryczny', 'pozostaje obojętny'], 'Wyższy stopień utlenienia — bardziej kwasowy.'),
])

T['c-wodorotlenki-kwasy'] = dict(Q=[
 ('Wodorotlenek amfoteryczny to:', ['*Al(OH)₃', 'NaOH', 'Mg(OH)₂', 'Ca(OH)₂'], 'Roztwarza się w kwasach i w mocnych zasadach.'),
 ('W szeregu HF, HCl, HBr, HI moc kwasów:', ['*rośnie', 'maleje', 'nie zmienia się', 'jest równa dla wszystkich'], 'Rośnie długość i maleje energia wiązania H–X.'),
])

T['c-sole'] = dict(Q=[
 ('Soli nie można otrzymać w reakcji:', ['*Cu + HCl', 'Zn + HCl', 'CaO + HCl', 'NaOH + HCl'], 'Miedź nie wypiera wodoru z kwasów nieutleniających.'),
 ('Hydratem jest:', ['*CuSO₄·5H₂O', 'CuSO₄', 'NaHSO₄', 'CaCO₃'], 'Sól zawierająca wodę krystalizacyjną.'),
])

T['c-metale'] = dict(Q=[
 ('Glin nie reaguje ze stężonym HNO₃ na zimno, ponieważ:', ['*ulega pasywacji', 'jest szlachetny', 'tworzy amalgamat', 'jest niemetalem'], 'Powierzchnię pokrywa szczelna warstwa tlenku.'),
 ('Metal, który wypiera miedź z roztworu CuSO₄, to:', ['*żelazo', 'srebro', 'złoto', 'platyna'], 'Fe jest aktywniejsze od Cu.'),
 ('Wapń reaguje z wodą, tworząc:', ['*Ca(OH)₂ i H₂', 'CaO i H₂', 'CaH₂ i O₂', 'Ca(OH)₂ i O₂'], 'Metal aktywny wypiera wodór z wody.'),
])

T['c-niemetale'] = dict(Q=[
 ('Brom wypiera z roztworu soli:', ['*jod', 'chlor', 'fluor', 'tlen'], 'Halogen aktywniejszy wypiera mniej aktywny.'),
 ('Stężony H₂SO₄ zwęgla cukier, ponieważ:', ['*silnie odwadnia', 'jest reduktorem', 'jest zasadą', 'jest lotny'], 'Odciąga wodę z cząsteczek cukru.'),
 ('Amoniak można wykryć:', ['*wilgotnym papierkiem wskaźnikowym', 'wodą wapienną (mętnienie)', 'wodą bromową (odbarwienie)', 'płynem Lugola (granat)'], 'Papierek barwi się na niebiesko.'),
])

T['c-stopnie'] = dict(Q=[
 ('Stopień utlenienia chromu w K₂Cr₂O₇:', ['*+VI', '+III', '+VII', '+II'], '2 · 1 + 2x − 14 = 0.'),
 ('Dysproporcjonowanie to reakcja, w której:', ['*ten sam pierwiastek utlenia się i redukuje', 'dwa metale wymieniają się', 'nie zmieniają się stopnie utlenienia', 'tlen się redukuje'], 'Np. Cl₂ + 2OH⁻ → Cl⁻ + ClO⁻ + H₂O.'),
])

T['c-bilans'] = dict(Q=[
 ('W równaniu MnO₄⁻ + 8H⁺ + ne⁻ → Mn²⁺ + 4H₂O liczba n wynosi:', ['*5', '3', '7', '2'], 'Mn: z +VII na +II.'),
 ('W środowisku obojętnym MnO₄⁻ redukuje się do:', ['*MnO₂', 'Mn²⁺', 'MnO₄²⁻', 'Mn'], 'Brunatny osad.'),
 ('W środowisku silnie zasadowym MnO₄⁻ redukuje się do:', ['*MnO₄²⁻', 'Mn²⁺', 'MnO₂', 'Mn(OH)₂'], 'Zielony manganian(VI).'),
])

T['c-ogniwa'] = dict(Q=[
 ('SEM ogniwa Zn | Zn²⁺ || Ag⁺ | Ag (E°: −0,76 V i +0,80 V) wynosi:', ['*1,56 V', '0,04 V', '0,76 V', '2,36 V'], '0,80 − (−0,76).'),
 ('W ogniwie elektrony płyną:', ['*od anody do katody', 'od katody do anody', 'przez klucz elektrolityczny', 'w obie strony'], 'Przewodnikiem zewnętrznym od elektrody ujemnej.'),
 ('Katodą w ogniwie Zn–Cu jest:', ['*miedź', 'cynk', 'klucz elektrolityczny', 'woltomierz'], 'Na miedzi zachodzi redukcja Cu²⁺.'),
])

T['c-elektroliza'] = dict(Q=[
 ('Podczas elektrolizy wodnego roztworu CuSO₄ na katodzie wydziela się:', ['*miedź', 'wodór', 'tlen', 'siarka'], 'Cu²⁺ łatwiej się redukuje niż woda.'),
 ('Podczas elektrolizy wodnego Na₂SO₄ na anodzie wydziela się:', ['*tlen', 'siarka', 'wodór', 'sód'], 'Aniony tlenowe nie utleniają się — utlenia się woda.'),
 ('Ochrona protektorowa stali polega na połączeniu jej z:', ['*cynkiem lub magnezem', 'miedzią', 'srebrem', 'grafitem'], 'Metal aktywniejszy koroduje zamiast żelaza.'),
])

T['c-izomeria'] = dict(Q=[
 ('Liczba izomerów konstytucyjnych C₅H₁₂ to:', ['*3', '2', '4', '5'], 'Pentan, 2-metylobutan, 2,2-dimetylopropan.'),
 ('Izomerię cis–trans wykazuje:', ['*but-2-en', 'but-1-en', 'propen', '2-metylopropen'], 'Każdy atom C=C ma dwa różne podstawniki.'),
 ('Atom węgla asymetryczny występuje w:', ['*butan-2-olu', 'propan-2-olu', 'etanolu', 'propan-1-olu'], 'C2 ma cztery różne podstawniki: H, OH, CH₃, C₂H₅.'),
])

T['c-alkany'] = dict(Q=[
 ('Produktem głównym monochlorowania 2-metylopropanu jest:', ['*2-chloro-2-metylopropan', '1-chlorobutan', '2-chlorobutan', '1-chloro-2-metylopropan'], 'Najtrwalszy rodnik trzeciorzędowy (przy większym udziale światła i wyższej T selektywność maleje).'),
 ('Alkany są mało reaktywne, ponieważ:', ['*mają tylko wiązania σ', 'mają wiązania π', 'są polarne', 'są jonowe'], 'Wiązania C–C i C–H są trwałe i słabo spolaryzowane.'),
])

T['c-alkeny'] = dict(Q=[
 ('Alken odbarwia wodę bromową w wyniku reakcji:', ['*addycji', 'substytucji', 'eliminacji', 'kondensacji'], 'Brom przyłącza się do wiązania podwójnego.'),
 ('Produkt główny addycji HCl do propenu:', ['*2-chloropropan', '1-chloropropan', '1,2-dichloropropan', 'chloropropen'], 'Reguła Markownikowa.'),
 ('Etyn powstaje w reakcji:', ['*karbidu z wodą', 'etanolu z H₂SO₄', 'etenu z H₂', 'metanu z Cl₂'], 'CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂.'),
 ('Hydratacja etynu (kat. Hg²⁺) daje:', ['*etanal', 'etanol', 'kwas octowy', 'eten'], 'Enol przechodzi w aldehyd.'),
])

T['c-areny'] = dict(Q=[
 ('Benzen nie odbarwia wody bromowej, ponieważ:', ['*ma zdelokalizowany układ π', 'jest nasycony', 'jest polarny', 'nie ma wiązań C–H'], 'Aromatyczność — trwały sekstet elektronowy.'),
 ('Nitrowanie benzenu to substytucja:', ['*elektrofilowa', 'nukleofilowa', 'rodnikowa', 'eliminacyjna'], 'Czynnikiem atakującym jest NO₂⁺.'),
 ('Chlorowanie toluenu na świetle zachodzi:', ['*w łańcuchu bocznym', 'w pierścieniu', 'nie zachodzi', 'tylko w pozycji meta'], 'Mechanizm rodnikowy.'),
])

T['c-alkohole'] = dict(Q=[
 ('Fenol w odróżnieniu od etanolu reaguje z:', ['*NaOH', 'Na', 'O₂', 'HCl'], 'Fenol ma odczyn słabo kwasowy.'),
 ('Glicerol wykryjesz za pomocą:', ['*Cu(OH)₂', 'wody bromowej', 'FeCl₃', 'płynu Lugola'], 'Szafirowy roztwór — sąsiednie grupy –OH.'),
 ('Fenol z FeCl₃ daje zabarwienie:', ['*fioletowe', 'ceglaste', 'szafirowe', 'żółte'], 'Charakterystyczna reakcja fenoli.'),
 ('Odwodnienie etanolu w 170°C (H₂SO₄) daje:', ['*eten', 'etanal', 'eter dietylowy', 'etyn'], 'W niższej temperaturze (ok. 140°C) przeważa eter.'),
])

T['c-karbonylowe'] = dict(Q=[
 ('Próbę Tollensa daje:', ['*etanal', 'propanon', 'etanol', 'kwas octowy'], 'Grupa aldehydowa redukuje Ag⁺ do srebra.'),
 ('Redukcja propanonu daje:', ['*propan-2-ol', 'propan-1-ol', 'propanal', 'kwas propanowy'], 'Keton → alkohol II-rzędowy.'),
 ('Próba jodoformowa jest pozytywna dla:', ['*propanonu', 'propanalu', 'metanalu', 'pentan-3-onu'], 'Wymaga grupy CH₃–CO–.'),
])

T['c-karboksylowe'] = dict(Q=[
 ('Najmocniejszym kwasem karboksylowym jest:', ['*kwas trichlorooctowy', 'kwas octowy', 'kwas propanowy', 'kwas chlorooctowy'], 'Trzy atomy Cl silnie przyciągają elektrony.'),
 ('Kwas mrówkowy różni się od octowego tym, że:', ['*odbarwia KMnO₄', 'reaguje z NaOH', 'barwi lakmus', 'tworzy estry'], 'Ma charakter redukujący (ugrupowanie aldehydowe).'),
 ('Kwas octowy reaguje z NaHCO₃, wydzielając:', ['*CO₂', 'H₂', 'O₂', 'CH₄'], 'Mocniejszy kwas wypiera słabszy kwas węglowy.'),
])

T['c-estry'] = dict(Q=[
 ('Ester o zapachu bananów to:', ['*octan izopentylu', 'mrówczan etylu', 'octan metylu', 'maślan etylu'], 'Klasyczny przykład estru zapachowego.'),
 ('Zmydlanie tłuszczu to hydroliza:', ['*zasadowa', 'kwasowa', 'enzymatyczna', 'utleniająca'], 'Powstaje glicerol i mydło.'),
 ('Tłuszcz ciekły różni się od stałego tym, że ma:', ['*więcej wiązań C=C', 'więcej grup –OH', 'krótszy glicerol', 'więcej atomów N'], 'Reszty kwasów nienasyconych.'),
])

T['c-aminy'] = dict(Q=[
 ('Najmocniejszą zasadą jest:', ['*dimetyloamina', 'amoniak', 'anilina', 'acetamid'], 'Grupy alkilowe zwiększają gęstość elektronową na N.'),
 ('Anilina jest słabszą zasadą niż amoniak, ponieważ:', ['*para N sprzęga się z pierścieniem', 'nie ma wolnej pary elektronów', 'jest związkiem o budowie jonowej', 'ma w cząsteczce grupę –COOH'], 'Delokalizacja zmniejsza dostępność pary elektronowej.'),
 ('Hydroliza acetamidu w NaOH daje:', ['*octan sodu i NH₃', 'kwas octowy i NH₄⁺', 'etanol i NH₃', 'etanal i N₂'], 'W środowisku zasadowym powstaje sól i amoniak.'),
])

T['c-aminokwasy'] = dict(Q=[
 ('Glicyna w roztworze o pH równym punktowi izoelektrycznemu występuje głównie jako:', ['*jon obojnaczy', 'kation', 'anion', 'cząsteczka niezjonizowana'], 'Ładunek wypadkowy równy zero.'),
 ('Liczba dipeptydów z glicyny i alaniny (bez powtórzeń reszt) to:', ['*2', '1', '4', '3'], 'Gly-Ala i Ala-Gly.'),
 ('Jedynym aminokwasem białkowym bez asymetrycznego atomu C jest:', ['*glicyna', 'alanina', 'seryna', 'cysteina'], 'Atom Cα ma dwa atomy wodoru.'),
])

T['c-cukry'] = dict(Q=[
 ('Skrobia z płynem Lugola daje zabarwienie:', ['*granatowe', 'ceglaste', 'fioletowe', 'żółte'], 'Kompleks jodu z amylozą.'),
 ('Glukozę od fruktozy odróżnisz:', ['*wodą bromową z NaHCO₃', 'próbą Trommera', 'próbą Tollensa', 'Cu(OH)₂ na zimno'], 'Fruktoza w środowisku zasadowym też redukuje Cu²⁺ i Ag⁺.'),
])
