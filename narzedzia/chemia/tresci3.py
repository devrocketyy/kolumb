# Treści kursu chemii — porcja 3: Wiązania i oddziaływania (III) oraz mol i stechiometria (I).

T = {}

T['c-wiazania'] = dict(F=[
 ('Reguła oktetu (dubletu)', 'Atomy łączą się tak, by uzyskać trwałą konfigurację najbliższego gazu szlachetnego — 8 elektronów na ostatniej powłoce (wodór i lit: 2).'),
 ('Wyjaśnij pojęcie: wiązanie jonowe', 'Wiązanie powstające w wyniku przeniesienia elektronów z atomu metalu na atom niemetalu i elektrostatycznego przyciągania powstałych kationów i anionów.'),
 ('Kiedy powstaje wiązanie jonowe (kryterium elektroujemności)?', 'Gdy różnica elektroujemności łączących się atomów jest duża — umownie ΔE ≥ 1,7.'),
 ('Wyjaśnij pojęcie: wiązanie kowalencyjne (atomowe)', 'Wiązanie utworzone przez wspólną parę (pary) elektronów, do której każdy z atomów wnosi po jednym elektronie.'),
 ('Wiązanie kowalencyjne niespolaryzowane a spolaryzowane', 'Niespolaryzowane — między atomami o tej samej elektroujemności (ΔE ≈ 0, np. H₂, Cl₂); spolaryzowane — wspólna para przesunięta w stronę atomu bardziej elektroujemnego (0 < ΔE < 1,7, np. HCl, H₂O).'),
 ('Wyjaśnij pojęcie: wiązanie koordynacyjne', 'Wiązanie kowalencyjne, w którym oba elektrony wspólnej pary pochodzą od jednego atomu (donora) i trafiają na wolny orbital drugiego (akceptora), np. w NH₄⁺, H₃O⁺, CO.'),
 ('Przykłady drobin z wiązaniem koordynacyjnym', 'NH₄⁺ (N → H⁺), H₃O⁺ (O → H⁺), CO, SO₂, SO₃, HNO₃, H₂SO₄ (w zapisie wzorów elektronowych), związki kompleksowe.'),
 ('Wyjaśnij pojęcie: wiązanie metaliczne', 'Wiązanie w metalach: kationy metalu tworzą sieć krystaliczną, a elektrony walencyjne są zdelokalizowane („gaz elektronowy”).'),
 ('Jak wiązanie metaliczne tłumaczy właściwości metali?', 'Zdelokalizowane elektrony przewodzą prąd i ciepło; warstwy kationów mogą się przesuwać, więc metale są kowalne i ciągliwe; elektrony odbijają światło (połysk).'),
 ('Wyjaśnij pojęcie: wiązanie σ (sigma)', 'Wiązanie powstające przez czołowe nakładanie się orbitali wzdłuż osi łączącej jądra; każde wiązanie pojedyncze jest typu σ.'),
 ('Wyjaśnij pojęcie: wiązanie π (pi)', 'Wiązanie powstające przez boczne nakładanie się orbitali p, nad i pod osią wiązania; występuje w wiązaniach wielokrotnych obok wiązania σ.'),
 ('Ile wiązań σ i π ma wiązanie podwójne i potrójne?', 'Podwójne: 1σ + 1π; potrójne: 1σ + 2π.'),
 ('Właściwości związków jonowych', 'Wysokie temperatury topnienia, w stanie stałym nie przewodzą prądu, przewodzą w stopie i w roztworze; zwykle dobrze rozpuszczalne w wodzie; kruche.'),
 ('Właściwości substancji kowalencyjnych o budowie cząsteczkowej', 'Niskie temperatury topnienia i wrzenia (słabe oddziaływania między cząsteczkami), zwykle nie przewodzą prądu.'),
 ('Wyjaśnij pojęcie: kryształ kowalencyjny', 'Kryształ, w którym atomy połączone są w sieć wiązaniami kowalencyjnymi (np. diament, SiO₂) — bardzo twardy, o bardzo wysokiej temperaturze topnienia.'),
 ('Dlaczego grafit przewodzi prąd, a diament nie?', 'W graficie każdy atom C tworzy 3 wiązania, a czwarty elektron jest zdelokalizowany w warstwie; w diamencie wszystkie 4 elektrony tworzą wiązania σ.'),
 ('Jak zapisać wzór elektronowy kreskowy (Lewisa)?', 'Pokazać wszystkie wiązania (kreski — wspólne pary) i wolne pary elektronowe przy atomach, tak by spełnić regułę oktetu (dubletu).'),
 ('Wyjaśnij pojęcie: wolna (niewiążąca) para elektronowa', 'Para elektronów walencyjnych atomu, która nie bierze udziału w wiązaniu, np. dwie pary przy tlenie w H₂O, jedna przy azocie w NH₃.'),
 ('Wyjaśnij pojęcie: energia wiązania', 'Energia potrzebna do rozerwania wiązania (w 1 molu cząsteczek w stanie gazowym); im krótsze wiązanie, tym zwykle większa energia.'),
], Q=[
 ('W której substancji występuje wiązanie jonowe?', ['HCl', '*KBr', 'CO₂', 'Cl₂'], 'Metal z niemetalem o dużej różnicy elektroujemności.'),
 ('Wiązanie koordynacyjne występuje w:', ['CH₄', '*NH₄⁺', 'H₂', 'NaCl'], 'Azot oddaje wolną parę kationowi H⁺.'),
 ('Ile wiązań σ i π ma cząsteczka N₂?', ['*1σ i 2π', '3σ', '2σ i 1π', '1σ i 1π'], 'Wiązanie potrójne.'),
 ('Dlaczego chlorek sodu w stanie stałym nie przewodzi prądu?', ['nie ma jonów', '*jony nie mogą się swobodnie poruszać w sieci krystalicznej', 'ma wiązania kowalencyjne', 'nie ma elektronów'], 'Przewodzi dopiero w stopie lub roztworze.'),
 ('Dlaczego metale przewodzą prąd elektryczny?', ['mają wiązania jonowe', '*mają zdelokalizowane elektrony walencyjne', 'mają wolne pary elektronowe', 'tworzą kryształy kowalencyjne'], 'Gaz elektronowy w sieci metalicznej.'),
])

T['c-geometria'] = dict(F=[
 ('Wyjaśnij pojęcie: hybrydyzacja', 'Model, w którym orbitale atomowe atomu centralnego mieszają się, tworząc nowe, równocenne orbitale zhybrydyzowane o określonym ułożeniu w przestrzeni.'),
 ('Hybrydyzacja sp³ — geometria i kąt', 'Cztery orbitale skierowane do naroży czworościanu, kąt ok. 109,5°, np. CH₄. W NH₃ (1 wolna para) kształt piramidy trygonalnej, ok. 107°; w H₂O (2 wolne pary) kątowy, ok. 104,5°.'),
 ('Hybrydyzacja sp² — geometria i kąt', 'Trzy orbitale w jednej płaszczyźnie, kąt 120° (trójkąt), np. BF₃, C w etenie, C w benzenie.'),
 ('Hybrydyzacja sp — geometria i kąt', 'Dwa orbitale liniowo, kąt 180°, np. BeCl₂, CO₂ (C), C w etynie.'),
 ('Jak ustalić typ hybrydyzacji atomu centralnego?', 'Policzyć liczbę przestrzenną: wiązania σ + wolne pary atomu centralnego. 2 → sp, 3 → sp², 4 → sp³.'),
 ('Hybrydyzacja atomów węgla w etanie, etenie i etynie', 'Etan — sp³, eten — sp², etyn — sp.'),
 ('Model VSEPR — podstawowa zasada', 'Pary elektronowe (wiążące i wolne) wokół atomu centralnego odpychają się i układają jak najdalej od siebie; wolne pary odpychają silniej niż wiążące.'),
 ('Dlaczego kąt H–O–H w wodzie jest mniejszy niż w metanie?', 'Dwie wolne pary elektronowe tlenu odpychają silniej niż pary wiążące i ściskają kąt między wiązaniami O–H (ok. 104,5° zamiast 109,5°).'),
 ('Wyjaśnij pojęcie: moment dipolowy', 'Miara polarności cząsteczki — wynika z rozsunięcia środków ładunku dodatniego i ujemnego.'),
 ('Kiedy cząsteczka jest polarna?', 'Gdy ma wiązania spolaryzowane ułożone niesymetrycznie, więc momenty dipolowe się nie znoszą (np. H₂O, NH₃, HCl).'),
 ('Dlaczego CO₂ jest niepolarny, choć wiązania C=O są spolaryzowane?', 'Cząsteczka jest liniowa i symetryczna — momenty dipolowe obu wiązań znoszą się.'),
 ('Przykłady cząsteczek niepolarnych o wiązaniach spolaryzowanych', 'CO₂ (liniowa), BF₃ (trójkątna płaska), CH₄ i CCl₄ (tetraedryczne).'),
 ('Kształt cząsteczki NH₃', 'Piramida trygonalna — azot sp³ z jedną wolną parą.'),
 ('Kształt cząsteczki H₂O', 'Kątowy (zgięty) — tlen sp³ z dwiema wolnymi parami.'),
 ('Kształt jonu NH₄⁺', 'Tetraedr (czworościan), kąty 109,5° — cztery wiązania N–H, brak wolnej pary.'),
 ('Typowy błąd w określaniu kształtu cząsteczki', 'Mylenie kształtu z rozmieszczeniem par elektronowych: w NH₃ pary są rozmieszczone tetraedrycznie, ale kształt cząsteczki (atomy) to piramida.'),
], Q=[
 ('Atom węgla w etenie ma hybrydyzację:', ['sp', '*sp²', 'sp³', 'nie ulega hybrydyzacji'], 'Trzy wiązania σ, płaski układ, 120°.'),
 ('Która cząsteczka jest niepolarna?', ['H₂O', 'NH₃', '*CCl₄', 'HCl'], 'Tetraedryczna symetria — dipole się znoszą.'),
 ('Kształt cząsteczki amoniaku to:', ['tetraedr', 'trójkąt płaski', '*piramida trygonalna', 'liniowy'], 'sp³ z jedną wolną parą.'),
 ('Kąt między wiązaniami w cząsteczce CO₂ wynosi:', ['104,5°', '109,5°', '120°', '*180°'], 'Cząsteczka liniowa, węgiel sp.'),
 ('Dlaczego kąt w H₂O (104,5°) jest mniejszy od 109,5°?', ['tlen ma hybrydyzację sp²', '*wolne pary elektronowe silniej odpychają pary wiążące', 'wiązania O–H są niespolaryzowane', 'cząsteczka jest liniowa'], 'Model VSEPR.'),
])

T['c-oddzialywania'] = dict(F=[
 ('Wyjaśnij pojęcie: wiązanie wodorowe', 'Oddziaływanie między atomem wodoru związanym z silnie elektroujemnym atomem (F, O, N) a wolną parą elektronową innego atomu F, O lub N.'),
 ('Jak wiązania wodorowe wpływają na temperaturę wrzenia?', 'Podnoszą ją — trzeba dostarczyć dodatkowej energii, by je zerwać (np. H₂O wrze w 100°C, a cięższy H₂S w ok. −60°C).'),
 ('Dlaczego etanol wrze w wyższej temperaturze niż eter dimetylowy o tej samej masie molowej?', 'Etanol ma grupę –OH i tworzy wiązania wodorowe między cząsteczkami, eter dimetylowy nie ma wodoru przy tlenie i ich nie tworzy.'),
 ('Wyjaśnij pojęcie: oddziaływania van der Waalsa (dyspersyjne)', 'Słabe oddziaływania między cząsteczkami wynikające z chwilowych dipoli; rosną z wielkością cząsteczki i jej powierzchnią kontaktu.'),
 ('Jak długość łańcucha alkanu wpływa na temperaturę wrzenia?', 'Im dłuższy łańcuch, tym silniejsze oddziaływania van der Waalsa i wyższa temperatura wrzenia.'),
 ('Jak rozgałęzienie łańcucha wpływa na temperaturę wrzenia izomerów?', 'Rozgałęzione izomery wrą niżej — mają mniejszą powierzchnię kontaktu, więc słabsze oddziaływania międzycząsteczkowe.'),
 ('Oddziaływania dipol–dipol', 'Przyciąganie między cząsteczkami polarnymi (np. HCl) — silniejsze niż dyspersyjne przy podobnej masie, słabsze niż wiązania wodorowe.'),
 ('Zasada „podobne rozpuszcza podobne”', 'Substancje polarne i jonowe dobrze rozpuszczają się w rozpuszczalnikach polarnych (woda), niepolarne — w niepolarnych (np. heksan).'),
 ('Dlaczego alkohole o krótkim łańcuchu mieszają się z wodą, a o długim nie?', 'Grupa –OH tworzy wiązania wodorowe z wodą, ale długi niepolarny łańcuch węglowy (hydrofobowy) przeważa i utrudnia rozpuszczanie.'),
 ('Wyjaśnij pojęcie: hydratacja (solwatacja)', 'Otaczanie jonów lub cząsteczek substancji rozpuszczonej przez cząsteczki wody (rozpuszczalnika) — dodatnie jony przez atomy O, ujemne przez atomy H wody.'),
 ('Dlaczego lód ma mniejszą gęstość niż woda?', 'W lodzie cząsteczki wody połączone są wiązaniami wodorowymi w ażurową sieć z dużą ilością pustej przestrzeni.'),
 ('Uszereguj oddziaływania według siły', 'Wiązanie kowalencyjne i jonowe (najsilniejsze) > wiązanie wodorowe > oddziaływania dipol–dipol > oddziaływania dyspersyjne.'),
], Q=[
 ('Która substancja tworzy wiązania wodorowe między cząsteczkami?', ['CH₄', '*NH₃', 'H₂S', 'CH₃–O–CH₃'], 'Wodór przy azocie i wolna para na azocie.'),
 ('Która substancja ma najwyższą temperaturę wrzenia?', ['metan', 'propan', '*butan', 'etan'], 'Najdłuższy łańcuch — najsilniejsze oddziaływania dyspersyjne.'),
 ('Dlaczego H₂O wrze w wyższej temperaturze niż H₂S?', ['H₂O ma większą masę', '*między cząsteczkami wody tworzą się wiązania wodorowe', 'H₂S jest jonowy', 'H₂O jest niepolarna'], 'S jest za mało elektroujemna.'),
 ('Która substancja najlepiej rozpuszcza się w heksanie?', ['NaCl', 'etanol', '*jod I₂', 'cukier'], 'Niepolarny I₂ w niepolarnym rozpuszczalniku.'),
])

T['c-mol'] = dict(F=[
 ('Wyjaśnij pojęcie: mol', 'Jednostka liczności materii: 1 mol zawiera 6,02 · 10²³ drobin (liczba Avogadra).'),
 ('Wyjaśnij pojęcie: masa molowa', 'Masa 1 mola substancji w g/mol; liczbowo równa masie cząsteczkowej (atomowej) w u.'),
 ('Jak obliczyć masę molową H₂SO₄?', '2·1 + 32 + 4·16 = 98 g/mol.'),
 ('Wyjaśnij pojęcie: objętość molowa gazu', 'Objętość 1 mola gazu; w warunkach normalnych (0°C, 1013 hPa) wynosi 22,4 dm³/mol i jest taka sama dla wszystkich gazów doskonałych.'),
 ('Prawo Avogadra', 'Równe objętości różnych gazów w tych samych warunkach ciśnienia i temperatury zawierają tę samą liczbę cząsteczek.'),
 ('Wzory łączące n, m, V i N', 'n = m/M; n = V/Vmol (gazy, war. normalne); n = N/NA.'),
 ('Gęstość gazu w warunkach normalnych', 'd = M / 22,4 dm³/mol (g/dm³).'),
 ('Ile atomów jest w 1 molu H₂O?', '3 mole atomów, czyli 3 · 6,02 · 10²³ ≈ 1,81 · 10²⁴ atomów.'),
 ('Typowy błąd: liczba cząsteczek a liczba atomów', 'Pominięcie, że jedna cząsteczka zawiera kilka atomów (np. w 1 molu O₂ jest 2 mole atomów tlenu).'),
 ('Równanie Clapeyrona i jednostki', 'pV = nRT; R = 83,14 hPa·dm³·mol⁻¹·K⁻¹ (p w hPa, V w dm³) lub 8,314 J·mol⁻¹·K⁻¹ (p w Pa, V w m³); T w kelwinach.'),
], Q=[
 ('Masa molowa CaCO₃ wynosi (Ca = 40, C = 12, O = 16):', ['68 g/mol', '*100 g/mol', '84 g/mol', '116 g/mol'], '40 + 12 + 48 = 100 g/mol.'),
 ('Ile cząsteczek zawiera 0,5 mola wody?', ['6,02·10²³', '*3,01·10²³', '1,2·10²⁴', '9,03·10²³'], 'N = n · NA.'),
 ('Jaka jest gęstość CO₂ (M = 44 g/mol) w warunkach normalnych?', ['1,25 g/dm³', '*1,96 g/dm³', '0,51 g/dm³', '44 g/dm³'], 'd = 44/22,4 ≈ 1,96 g/dm³.'),
 ('Ile moli atomów tlenu jest w 2 molach CO₂?', ['2', '*4', '6', '1'], 'Każda cząsteczka CO₂ ma 2 atomy O.'),
])

T['c-wzory'] = dict(F=[
 ('Wyjaśnij pojęcie: wzór empiryczny (elementarny)', 'Wzór podający najprostszy stosunek liczby atomów pierwiastków w związku, np. CH₂O dla glukozy.'),
 ('Wyjaśnij pojęcie: wzór rzeczywisty (sumaryczny)', 'Wzór podający rzeczywistą liczbę atomów w cząsteczce, np. C₆H₁₂O₆; jest wielokrotnością wzoru empirycznego.'),
 ('Jak wyznaczyć wzór empiryczny z procentowego składu?', 'Przyjąć 100 g związku → masy pierwiastków = ich procenty; podzielić przez masy molowe → mole; podzielić przez najmniejszą liczbę moli → stosunek; ewentualnie pomnożyć do liczb całkowitych.'),
 ('Jak przejść od wzoru empirycznego do rzeczywistego?', 'Podzielić masę molową związku przez masę molową wzoru empirycznego — wynik (liczba całkowita) mnoży indeksy.'),
 ('Jak obliczyć skład procentowy pierwiastka w związku?', '%E = (liczba atomów E · masa atomowa E / masa molowa związku) · 100%.'),
 ('Typowy błąd przy wyznaczaniu wzoru empirycznego', 'Zaokrąglanie stosunków typu 1,5 lub 1,33 do liczb całkowitych zamiast pomnożenia przez 2 lub 3.'),
 ('Wyjaśnij pojęcie: hydrat (sól uwodniona)', 'Sól zawierająca w sieci krystalicznej określoną liczbę cząsteczek wody, np. CuSO₄·5H₂O.'),
 ('Jak obliczyć liczbę cząsteczek wody w hydracie?', 'Z ubytku masy przy prażeniu: n(H₂O) / n(soli bezwodnej) = x we wzorze sól·xH₂O.'),
], Q=[
 ('Wzór empiryczny związku o wzorze rzeczywistym C₆H₆ to:', ['C₆H₆', '*CH', 'C₂H₂', 'C₃H₃'], 'Stosunek 1 : 1.'),
 ('Zawartość procentowa tlenu w H₂O (H = 1, O = 16) wynosi około:', ['11,1%', '50%', '*88,9%', '94,1%'], '16/18 · 100%.'),
 ('Stosunek molowy C : H wyszedł 1 : 2,5. Wzór empiryczny to:', ['CH₂', 'CH₃', '*C₂H₅', 'C₅H₂'], 'Mnożymy przez 2.'),
])

T['c-stechiometria'] = dict(F=[
 ('Prawo zachowania masy', 'Masa substratów równa jest masie produktów reakcji chemicznej.'),
 ('Prawo stałości składu', 'Związek chemiczny ma zawsze ten sam skład jakościowy i ilościowy, niezależnie od sposobu otrzymania.'),
 ('Jak ułożyć proporcję z równania reakcji?', 'Nad wzorami zapisać dane i szukane, pod wzorami — ilości wynikające z równania (mole × masa molowa lub objętość molowa), potem ułożyć proporcję.'),
 ('Obliczenia z wydajnością — schemat', 'Obliczyć ilość teoretyczną z równania, potem pomnożyć przez wydajność (W/100%); przy szukaniu substratów — podzielić przez wydajność.'),
 ('Typowy błąd w zadaniach z wydajnością', 'Mnożenie przez wydajność, gdy trzeba dzielić (szukanie potrzebnej ilości substratu przy wydajności < 100%).'),
 ('Obliczenia z nadmiarem — schemat', 'Policzyć mole obu substratów, porównać ze stosunkiem z równania, obliczyć produkt z substratu w niedomiarze; ewentualnie policzyć, ile zostało nadmiaru.'),
 ('Jak liczyć skład mieszaniny dwóch substancji reagujących z tym samym odczynnikiem?', 'Oznaczyć niewiadome (np. x i y — mole lub masy składników), ułożyć dwa równania: na masę mieszaniny i na ilość odczynnika lub produktu, rozwiązać układ.'),
 ('Typowy błąd w zadaniach z mieszaniną według CKE', 'Niewłaściwa interpretacja składu mieszaniny — np. przyjęcie, że reaguje tylko jeden składnik, albo pomylenie masy mieszaniny z masą składnika.'),
 ('Obliczenia z udziałem gazów w warunkach innych niż normalne', 'Liczbę moli gazu obliczyć z równania Clapeyrona n = pV/(RT), a dopiero potem stosować stosunek molowy.'),
 ('Jak sprawdzić wynik obliczeń stechiometrycznych?', 'Czy masa produktu nie przekracza możliwej z prawa zachowania masy? Czy stosunek molowy zgadza się ze współczynnikami? Czy jednostka pasuje do szukanej?'),
 ('Wyjaśnij pojęcie: stechiometria', 'Dział chemii zajmujący się ilościowymi zależnościami między reagentami w reakcjach chemicznych i składem związków.'),
], Q=[
 ('Ile gramów wody powstanie z 4 g wodoru w reakcji 2H₂ + O₂ → 2H₂O (H = 1, O = 16)?', ['18 g', '*36 g', '72 g', '9 g'], '4 g H₂ = 2 mol → 2 mol H₂O = 36 g.'),
 ('Teoretycznie powinno powstać 50 g produktu, wydajność wynosi 80%. Ile otrzymano?', ['62,5 g', '*40 g', '50 g', '30 g'], '50 · 0,8 = 40 g.'),
 ('Aby otrzymać 40 g produktu przy wydajności 80%, trzeba teoretycznie przygotować substraty na:', ['32 g produktu', '40 g produktu', '*50 g produktu', '48 g produktu'], 'Dzielimy przez wydajność: 40/0,8.'),
 ('Do reakcji Zn + 2HCl → ZnCl₂ + H₂ użyto 1 mol Zn i 1 mol HCl. Ile moli H₂ powstanie?', ['1 mol', '*0,5 mol', '2 mol', '0,25 mol'], 'HCl jest w niedomiarze: 1 mol HCl → 0,5 mol H₂.'),
])
