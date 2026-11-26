# Treści kursu chemii — porcja 11: dogęszczenie najsłabszych tematów (fiszki + pytania).
T = {}

T['c-wzory'] = dict(F=[
 ('Wzór empiryczny (elementarny)', 'Najprostszy stosunek liczb atomów pierwiastków w związku, np. CH₂O dla glukozy.'),
 ('Wzór rzeczywisty (sumaryczny)', 'Rzeczywista liczba atomów w cząsteczce; = n × wzór empiryczny, n = M(związku) / M(wzoru empirycznego).'),
 ('Jak ustalić wzór empiryczny z % masowych?', 'Założyć 100 g związku → masy pierwiastków w g → podzielić przez masy molowe → podzielić przez najmniejszą liczbę moli → doprowadzić do liczb całkowitych.'),
 ('Stosunek 1 : 1,5 w obliczeniach wzoru', 'Pomnożyć przez 2 → 2 : 3 (nie zaokrąglać do 1 : 2!).'),
 ('Stosunek 1 : 1,33 w obliczeniach wzoru', 'Pomnożyć przez 3 → 3 : 4 (np. Fe₃O₄).'),
 ('Jak wyznaczyć wzór związku organicznego ze spalania?', 'm(C) z CO₂ (12/44), m(H) z H₂O (2/18), m(O) = m(próbki) − m(C) − m(H); dalej stosunek moli.'),
 ('Gęstość względna gazu D względem H₂', 'M = D · 2 g/mol (względem powietrza: M = D · 29 g/mol).'),
 ('Hydrat — jak ustalić liczbę cząsteczek wody?', 'm(wody) = m(hydratu) − m(soli bezwodnej); n(H₂O) : n(soli) = x.'),
 ('Wzór CuSO₄·5H₂O — co oznacza kropka?', 'Woda krystalizacyjna: 5 moli H₂O na 1 mol CuSO₄ w krysztale.'),
 ('Masa molowa CuSO₄·5H₂O', '160 + 5·18 = 250 g/mol (najczęstszy błąd: liczenie tylko soli bezwodnej).'),
 ('Zawartość % pierwiastka w związku', '%E = (liczba atomów E · M(E) / M(związku)) · 100%.'),
 ('Pułapka: wynik 2,98 : 1 w obliczeniach wzoru', 'To błąd zaokrągleń — przyjmij 3 : 1; ale 2,5 : 1 to 5 : 2, nie 3 : 1.'),
], Q=[
 ('Związek zawiera 40% C, 6,7% H i 53,3% O, M = 180 g/mol. Jego wzór rzeczywisty to:', ['*C₆H₁₂O₆', 'CH₂O', 'C₃H₆O₃', 'C₆H₆O₆'], 'Empiryczny CH₂O (30 g/mol), 180/30 = 6.'),
 ('Stosunek molowy Fe : O = 1 : 1,5 oznacza wzór:', ['*Fe₂O₃', 'FeO', 'Fe₃O₄', 'FeO₂'], '1 : 1,5 = 2 : 3.'),
])

T['c-stechiometria'] = dict(F=[
 ('Substrat w niedomiarze', 'Ten, który przereaguje całkowicie — on wyznacza ilość produktu.'),
 ('Jak wskazać substrat w nadmiarze?', 'Podzielić liczby moli substratów przez ich współczynniki stechiometryczne — mniejszy iloraz = niedomiar.'),
 ('Wydajność reakcji', 'W = (ilość otrzymana / ilość teoretyczna) · 100%; ilość teoretyczna z substratu w niedomiarze.'),
 ('Wydajność procesu wieloetapowego', 'Iloczyn wydajności etapów: W = W₁ · W₂ · W₃.'),
 ('Masa substratu przy wydajności W', 'm(rzeczywista) = m(teoretyczna) / W — dzielimy, bo trzeba użyć więcej substratu.'),
 ('Czystość substratu (np. 80% CaCO₃)', 'Do obliczeń bierzemy tylko masę czystego składnika: m · 0,80.'),
 ('Objętość molowa gazu w warunkach normalnych', '22,4 dm³/mol (0°C, 1013 hPa).'),
 ('Objętość gazu w innych warunkach', 'Z równania Clapeyrona: pV = nRT, R = 83,14 hPa·dm³·mol⁻¹·K⁻¹.'),
 ('Prawo Avogadra', 'Równe objętości gazów w tych samych warunkach zawierają tyle samo cząsteczek → stosunek objętości = stosunek moli.'),
 ('Liczba Avogadra', 'Nₐ = 6,02·10²³ mol⁻¹ — liczba drobin w 1 molu.'),
 ('Typowy błąd: mieszanina dwóch substancji reagujących', 'Trzeba ułożyć układ dwóch równań (masa mieszaniny + ilość produktu), a nie liczyć jak dla jednej substancji.'),
 ('Analiza miareczkowa — kolejność rozumowania', 'n(titranta) = c·V → z równania n(analitu) → przeliczenie na całą próbkę (np. 25 cm³ z 500 cm³ → × 20).'),
], Q=[
 ('Z 10 g H₂ i 64 g O₂ powstaje woda. W nadmiarze jest:', ['*wodór', 'tlen', 'żaden', 'nie da się ustalić'], 'n(H₂) = 5, n(O₂) = 2; do 2 mol O₂ potrzeba 4 mol H₂.'),
 ('Dwa etapy o wydajnościach 80% i 50% dają łączną wydajność:', ['*40%', '65%', '130%', '30%'], '0,8 · 0,5 = 0,4.'),
])

T['c-stezenia'] = dict(F=[
 ('Stężenie procentowe', 'Cp = ms / mr · 100%; mr = ms + m(rozpuszczalnika).'),
 ('Stężenie molowe', 'Cm = n / V (V w dm³!).'),
 ('Przeliczanie Cp → Cm', 'Cm = Cp · d / (M · 100%), d w g/dm³ (1 g/cm³ = 1000 g/dm³).'),
 ('Rozcieńczanie — co się nie zmienia?', 'Masa (liczba moli) substancji rozpuszczonej: Cp₁·mr₁ = Cp₂·mr₂; Cm₁·V₁ = Cm₂·V₂.'),
 ('Zatężanie przez odparowanie wody', 'ms stała, mr maleje → Cp rośnie.'),
 ('Stężenie jonów w roztworze soli', 'Mnożymy przez liczbę jonów: 0,1 M Na₂SO₄ → [Na⁺] = 0,2 M, [SO₄²⁻] = 0,1 M.'),
 ('Ppm', 'Części na milion: 1 ppm = 1 mg/kg (≈ 1 mg/dm³ dla wody).'),
 ('Roztwór z hydratu — pułapka', 'Masa soli bezwodnej = m(hydratu) · M(soli)/M(hydratu); woda krystalizacyjna dołącza do rozpuszczalnika.'),
 ('Gęstość a objętość roztworu', 'mr = d · V; objętości roztworów przy mieszaniu zwykle się NIE sumują dokładnie (zadanie mówi, czy przyjąć sumowanie).'),
 ('Najczęstszy błąd w Cm', 'Objętość w cm³ zamiast dm³ (wynik 1000 razy za duży lub za mały).'),
 ('Ułamek molowy', 'x = n(składnika) / n(wszystkich składników).'),
], Q=[
 ('Ile gramów NaOH jest w 200 cm³ roztworu 0,5 M? (M = 40 g/mol)', ['*4 g', '40 g', '0,4 g', '10 g'], 'n = 0,5 · 0,2 = 0,1 mol → 4 g.'),
 ('Stężenie jonów Cl⁻ w 0,2 M CaCl₂ wynosi:', ['*0,4 mol/dm³', '0,2 mol/dm³', '0,1 mol/dm³', '0,6 mol/dm³'], 'Dwa jony Cl⁻ na jedną formułę.'),
])

T['c-rozpuszczalnosc'] = dict(F=[
 ('Rozpuszczalność', 'Maksymalna masa substancji, która rozpuszcza się w 100 g rozpuszczalnika w danej temperaturze (roztwór nasycony).'),
 ('Roztwór nasycony', 'W danej temperaturze nie rozpuści już więcej substancji; jest w równowadze z osadem.'),
 ('Roztwór przesycony', 'Zawiera więcej substancji niż nasycony — nietrwały, krystalizuje po wstrząśnięciu lub dodaniu kryształka.'),
 ('Rozpuszczalność gazów a temperatura', 'Maleje ze wzrostem temperatury (np. NH₃, CO₂, O₂).'),
 ('Rozpuszczalność gazów a ciśnienie', 'Rośnie ze wzrostem ciśnienia (prawo Henry’ego) — np. napoje gazowane.'),
 ('Rozpuszczalność większości ciał stałych a temperatura', 'Rośnie (wyjątki: np. Ca(OH)₂, Li₂CO₃, Ce₂(SO₄)₃ — maleje).'),
 ('Cp roztworu nasyconego z rozpuszczalności R', 'Cp = R / (100 + R) · 100% — dzielimy przez masę ROZTWORU.'),
 ('Krystalizacja przez chłodzenie', 'Masa kryształów = R(T₁) − R(T₂) na 100 g wody (przeliczyć na faktyczną masę wody).'),
 ('Iloczyn rozpuszczalności Ks', 'Dla AₓBᵧ: Ks = [A]ˣ[B]ʸ w roztworze nasyconym; stały w danej temperaturze.'),
 ('Rozpuszczalność molowa z Ks dla AB', 's = √Ks.'),
 ('Rozpuszczalność molowa z Ks dla AB₂ (np. Mg(OH)₂)', 'Ks = s(2s)² = 4s³ → s = ∛(Ks/4).'),
 ('Kiedy wytrąci się osad?', 'Gdy iloczyn stężeń jonów (z wykładnikami) > Ks. Pamiętaj o rozcieńczeniu po zmieszaniu roztworów!'),
 ('Efekt wspólnego jonu', 'Dodanie jonu obecnego w osadzie (np. Cl⁻ do AgCl) zmniejsza jego rozpuszczalność.'),
], Q=[
 ('Ks soli AB₂ = 4·10⁻¹². Rozpuszczalność molowa s wynosi:', ['*10⁻⁴ mol/dm³', '2·10⁻⁶ mol/dm³', '10⁻⁶ mol/dm³', '2·10⁻⁴ mol/dm³'], '4s³ = 4·10⁻¹² → s = 10⁻⁴.'),
])

T['c-mieszanie'] = dict(F=[
 ('Mieszanie dwóch roztworów tej samej substancji', 'ms = ms₁ + ms₂; mr = mr₁ + mr₂; Cp = ms/mr · 100%.'),
 ('Reguła krzyża (metoda mieszania)', 'Stosunek mas roztworów = (Cp₂ − Cp) : (Cp − Cp₁) — działa dla stężeń procentowych.'),
 ('Woda w regule krzyża', 'Woda ma Cp = 0%; czysta substancja Cp = 100%.'),
 ('Mieszanie roztworów reagujących (np. kwas + zasada)', 'Najpierw policz mole każdego reagenta, ustal nadmiar, potem stężenie nadmiaru w ŁĄCZNEJ objętości.'),
 ('pH po zmieszaniu mocnego kwasu i mocnej zasady', 'n(nadmiaru H⁺ lub OH⁻) / (V₁ + V₂) → pH lub pOH.'),
 ('Zmieszanie równych objętości dwóch roztworów', 'Stężenie każdego składnika spada o połowę (przed ewentualną reakcją).'),
 ('Pułapka przy Cm i mieszaniu', 'Nie wolno sumować stężeń — sumujemy MOLE i dzielimy przez sumę objętości.'),
 ('Rozpuszczanie stałej substancji w gotowym roztworze', 'ms = ms₁ + m(dodanej); mr = mr₁ + m(dodanej).'),
 ('Dodanie hydratu do roztworu', 'Do ms dolicz tylko część bezwodną; do mr całą masę hydratu.'),
 ('Roztwór buforowy z mieszania', 'Słaby kwas + jego sól (lub słaba zasada + jej sól); pH = pKa + log(c_soli/c_kwasu).'),
], Q=[
 ('Zmieszano 100 g roztworu 10% i 100 g roztworu 30%. Cp mieszaniny:', ['*20%', '40%', '15%', '25%'], '(10 + 30)/200 · 100%.'),
 ('Zmieszano 50 cm³ 0,2 M HCl i 50 cm³ 0,2 M NaOH. pH:', ['*7', '1', '13', '0,7'], 'Zobojętnienie stechiometryczne.'),
])

T['c-tlenki'] = dict(F=[
 ('Tlenki kwasowe', 'Reagują z zasadami (i często z wodą → kwas), np. CO₂, SO₂, SO₃, P₄O₁₀, N₂O₅, CrO₃, Mn₂O₇.'),
 ('Tlenki zasadowe', 'Reagują z kwasami, np. Na₂O, CaO, MgO, CuO, FeO.'),
 ('Tlenki amfoteryczne', 'Reagują i z kwasami, i z mocnymi zasadami: ZnO, Al₂O₃, Cr₂O₃, BeO, PbO, SnO.'),
 ('Tlenki obojętne', 'Nie reagują ani z kwasami, ani z zasadami: CO, NO, N₂O (uwaga: SiO₂ NIE jest obojętny — to tlenek kwasowy).'),
 ('Charakter tlenku a stopień utlenienia metalu', 'Im wyższy stopień utlenienia, tym bardziej kwasowy: CrO (zasadowy), Cr₂O₃ (amfoteryczny), CrO₃ (kwasowy).'),
 ('SiO₂ — charakter i reakcja', 'Tlenek kwasowy, nie reaguje z wodą; reaguje ze stopionymi zasadami i z HF: SiO₂ + 4HF → SiF₄ + 2H₂O.'),
 ('Reakcja ZnO z NaOH (roztwór)', 'ZnO + 2NaOH + H₂O → Na₂[Zn(OH)₄].'),
 ('Reakcja Al₂O₃ z kwasem', 'Al₂O₃ + 6H⁺ → 2Al³⁺ + 3H₂O.'),
 ('Tlenek + woda → zasada', 'Tylko tlenki metali aktywnych (1. i 2. grupa od Ca): CaO + H₂O → Ca(OH)₂.'),
 ('Nadtlenki', 'Zawierają anion O₂²⁻ (tlen na −I), np. Na₂O₂, H₂O₂.'),
 ('Tlenek mieszany Fe₃O₄', 'FeO·Fe₂O₃ — żelazo na +II i +III.'),
 ('Typowy błąd: CO₂ + NaOH', 'Przy nadmiarze NaOH → Na₂CO₃ + H₂O; przy nadmiarze CO₂ → NaHCO₃.'),
], Q=[
 ('Tlenkiem amfoterycznym jest:', ['*Al₂O₃', 'CaO', 'SO₃', 'CO'], 'Reaguje z kwasami i zasadami.'),
 ('Który tlenek NIE reaguje z wodą, ale jest kwasowy?', ['*SiO₂', 'SO₃', 'CO₂', 'P₄O₁₀'], 'SiO₂ reaguje dopiero ze stopionymi zasadami.'),
])

T['c-bilans'] = dict(F=[
 ('Metoda bilansu elektronowego — kroki', '1) stopnie utlenienia, 2) równania połówkowe, 3) wyrównanie liczby elektronów, 4) współczynniki, 5) bilans O i H, 6) sprawdzenie ładunku.'),
 ('Równanie połówkowe w środowisku kwasowym', 'Brakujący tlen uzupełniamy H₂O, wodór — jonami H⁺.'),
 ('Równanie połówkowe w środowisku zasadowym', 'Brakujący tlen — jonami OH⁻ (po stronie z nadmiarem H dopisujemy H₂O).'),
 ('Sprawdzenie równania jonowego', 'Suma ładunków po obu stronach musi być równa.'),
 ('KMnO₄ — produkty redukcji', 'Kwasowe: Mn²⁺ (bezbarwny); obojętne: MnO₂ (brunatny osad); zasadowe: MnO₄²⁻ (zielony).'),
 ('K₂Cr₂O₇ w środowisku kwasowym', 'Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O (pomarańczowy → zielony).'),
 ('Dysproporcjonowanie', 'Ten sam pierwiastek jednocześnie się utlenia i redukuje, np. Cl₂ + 2OH⁻ → Cl⁻ + ClO⁻ + H₂O.'),
 ('Synproporcjonowanie (komproporcjonowanie)', 'Ten sam pierwiastek z dwóch stopni utlenienia przechodzi na stopień pośredni, np. IO₃⁻ + 5I⁻ + 6H⁺ → 3I₂ + 3H₂O.'),
 ('H₂O₂ jako utleniacz', 'H₂O₂ + 2H⁺ + 2e⁻ → 2H₂O (tlen −I → −II).'),
 ('H₂O₂ jako reduktor', 'H₂O₂ → O₂ + 2H⁺ + 2e⁻ (np. z KMnO₄).'),
 ('Pułapka: „uwzględnij środowisko”', 'Równanie z H⁺ dla reakcji w zasadzie (lub OH⁻ w kwasie) = 0 pkt, nawet przy dobrym bilansie.'),
], Q=[
 ('W reakcji Cl₂ + 2OH⁻ → Cl⁻ + ClO⁻ + H₂O chlor:', ['*ulega dysproporcjonowaniu', 'tylko się utlenia', 'tylko się redukuje', 'nie zmienia stopnia utlenienia'], '0 → −I i +I.'),
 ('KMnO₄ w środowisku obojętnym redukuje się do:', ['*MnO₂', 'Mn²⁺', 'MnO₄²⁻', 'Mn'], 'Brunatny osad.'),
])

T['c-jonowe'] = dict(F=[
 ('Czego NIE rozpisujemy na jony w równaniu jonowym?', 'Osadów, gazów, wody, słabych elektrolitów (CH₃COOH, NH₃, H₂S, HF), tlenków, substancji prostych.'),
 ('Jony widzowie', 'Jony, które nie biorą udziału w reakcji — pomijamy je w zapisie skróconym.'),
 ('Mocne kwasy (dysocjują całkowicie)', 'HCl, HBr, HI, HNO₃, H₂SO₄ (1. etap), HClO₄.'),
 ('Mocne zasady', 'Wodorotlenki litowców i Ca(OH)₂, Sr(OH)₂, Ba(OH)₂.'),
 ('Reakcja zobojętniania (jonowo skrócona)', 'H⁺ + OH⁻ → H₂O (dla mocnego kwasu i mocnej zasady).'),
 ('Wypieranie słabego kwasu z soli', 'Mocny kwas wypiera słabszy/lotny: CO₃²⁻ + 2H⁺ → CO₂ + H₂O; S²⁻ + 2H⁺ → H₂S.'),
 ('Wypieranie słabej zasady', 'NH₄⁺ + OH⁻ → NH₃ + H₂O (ogrzewanie — zapach amoniaku).'),
 ('Białe osady do zapamiętania', 'AgCl, BaSO₄, BaCO₃, CaCO₃, PbCl₂, PbSO₄, Mg(OH)₂, Al(OH)₃, Zn(OH)₂.'),
 ('Barwne osady do zapamiętania', 'AgBr (żółtawy), AgI (żółty), PbI₂ (żółty), Ag₂CrO₄ (ceglasty), Cu(OH)₂ (niebieski), Fe(OH)₃ (brunatny), Fe(OH)₂ (zielonkawy), CuS, PbS, Ag₂S (czarne).'),
 ('Wykrywanie jonów SO₄²⁻', 'Ba²⁺ → biały BaSO₄, nierozpuszczalny w HCl (BaCO₃ się roztwarza).'),
 ('Wykrywanie jonów Cl⁻', 'Ag⁺ (w obecności HNO₃) → biały, serowaty AgCl, ciemnieje na świetle.'),
], Q=[
 ('Osad żółty, który wytrąca się z Ag⁺ i nie roztwarza się w amoniaku, to:', ['*AgI', 'AgCl', 'Ag₂O', 'AgNO₃'], 'AgCl roztwarza się w NH₃, AgI — nie.'),
])

T['c-alkany'] = dict(F=[
 ('Wzór ogólny alkanów', 'CₙH₂ₙ₊₂; cykloalkany CₙH₂ₙ.'),
 ('Hybrydyzacja węgla w alkanach', 'sp³, kąty ok. 109,5° (tetraedr).'),
 ('Typowa reakcja alkanów', 'Substytucja rodnikowa z halogenami (światło): CH₄ + Cl₂ → CH₃Cl + HCl.'),
 ('Etapy substytucji rodnikowej', 'Inicjacja (Cl₂ → 2Cl•), propagacja (powstawanie rodników), terminacja (łączenie rodników).'),
 ('Selektywność bromowania', 'Brom podstawia głównie wodór przy węglu o najwyższej rzędowości (III > II > I); chlor jest mało selektywny.'),
 ('Temperatura wrzenia alkanów', 'Rośnie z długością łańcucha; maleje z rozgałęzieniem (mniejsza powierzchnia kontaktu).'),
 ('Rozpuszczalność alkanów', 'Nie rozpuszczają się w wodzie (niepolarne); rozpuszczają się w rozpuszczalnikach niepolarnych.'),
 ('Spalanie całkowite alkanu', 'CₙH₂ₙ₊₂ + (3n+1)/2 O₂ → nCO₂ + (n+1)H₂O.'),
 ('Spalanie niecałkowite', 'Przy niedoborze tlenu powstaje CO lub C (sadza).'),
 ('Kraking', 'Rozkład długich łańcuchów na krótsze alkany i alkeny (wysoka temperatura, katalizator).'),
 ('Reforming', 'Przekształcanie alkanów prostych w rozgałęzione i aromatyczne — podnosi liczbę oktanową.'),
 ('Liczba oktanowa', 'Odporność paliwa na spalanie stukowe; izooktan = 100, n-heptan = 0.'),
], Q=[
 ('Ile monochloropochodnych (izomerów konstytucyjnych) daje propan?', ['*2', '1', '3', '4'], '1-chloro- i 2-chloropropan.'),
 ('Najwyższą temperaturę wrzenia ma:', ['*n-pentan', '2-metylobutan', '2,2-dimetylopropan', 'butan'], 'Nierozgałęziony, najdłuższy.'),
])

T['c-areny'] = dict(F=[
 ('Warunki aromatyczności (reguła Hückla)', 'Pierścień płaski, sprzężony, z 4n + 2 elektronami π (benzen: 6).'),
 ('Hybrydyzacja węgla w benzenie', 'sp²; wszystkie wiązania C–C jednakowej długości (139 pm).'),
 ('Typowa reakcja benzenu', 'Substytucja elektrofilowa (nitrowanie, halogenowanie z FeBr₃/FeCl₃, sulfonowanie, alkilowanie).'),
 ('Nitrowanie benzenu', 'C₆H₆ + HNO₃ → C₆H₅NO₂ + H₂O (stęż. H₂SO₄); elektrofil NO₂⁺.'),
 ('Podstawniki kierujące w orto/para', '–OH, –NH₂, –CH₃ (alkile), –OCH₃, halogeny (halogeny dezaktywują, ale kierują o/p).'),
 ('Podstawniki kierujące w meta', '–NO₂, –COOH, –CHO, –CN, –SO₃H, –COR (dezaktywujące).'),
 ('Toluen + Cl₂ w świetle', 'Substytucja rodnikowa w grupie CH₃: C₆H₅CH₂Cl.'),
 ('Toluen + Cl₂ z FeCl₃', 'Substytucja elektrofilowa w pierścieniu: o- i p-chlorotoluen.'),
 ('Utlenianie toluenu KMnO₄', 'Łańcuch boczny → –COOH: kwas benzoesowy.'),
 ('Czy benzen odbarwia wodę bromową?', 'Nie — nie ulega łatwo addycji (trwały układ aromatyczny).'),
 ('Naftalen', 'C₁₀H₈ — dwa skondensowane pierścienie, aromatyczny, sublimuje.'),
 ('Fenol a benzen w bromowaniu', 'Fenol reaguje z wodą bromową bez katalizatora → 2,4,6-tribromofenol (biały osad).'),
], Q=[
 ('Grupa kierująca kolejny podstawnik w położenie meta to:', ['*–NO₂', '–OH', '–CH₃', '–Cl'], 'Grupy dezaktywujące z wiązaniem wielokrotnym.'),
 ('Produktem reakcji toluenu z Br₂ w świetle jest:', ['*bromek benzylu (C₆H₅CH₂Br)', 'o-bromotoluen', 'p-bromotoluen', 'bromobenzen'], 'Substytucja rodnikowa w łańcuchu bocznym.'),
])

T['c-karbonylowe'] = dict(F=[
 ('Aldehyd — grupa funkcyjna', '–CHO (zapis –COH jest błędny!).'),
 ('Keton — grupa funkcyjna', '>C=O między dwoma atomami węgla.'),
 ('Otrzymywanie aldehydu', 'Utlenianie alkoholu I-rzędowego (np. CuO, ogrzewanie).'),
 ('Otrzymywanie ketonu', 'Utlenianie alkoholu II-rzędowego.'),
 ('Próba Tollensa', 'Aldehyd + [Ag(NH₃)₂]⁺ → lustro srebrne; ketony nie reagują.'),
 ('Próba Trommera', 'Aldehyd + Cu(OH)₂ (zasadowe, ogrzewanie) → ceglastoczerwony Cu₂O.'),
 ('Redukcja aldehydu', 'Do alkoholu I-rzędowego (H₂/Ni, NaBH₄).'),
 ('Redukcja ketonu', 'Do alkoholu II-rzędowego.'),
 ('Metanal — właściwości', 'Gaz, roztwór 40% to formalina; w próbie Tollensa daje 4 Ag na cząsteczkę.'),
 ('Propanon (aceton)', 'Najprostszy keton, rozpuszczalnik, miesza się z wodą.'),
 ('Hybrydyzacja węgla karbonylowego', 'sp², geometria płaska trygonalna.'),
 ('Reakcja haloformowa', 'Metyloketony (CH₃–CO–R) z I₂/NaOH → CHI₃ (żółty osad jodoformu) + RCOO⁻.'),
], Q=[
 ('Który związek daje próbę Tollensa?', ['*propanal', 'propanon', 'propan-2-ol', 'kwas propanowy'], 'Aldehyd.'),
 ('Utlenienie butan-2-olu prowadzi do:', ['*butanonu', 'butanalu', 'kwasu butanowego', 'but-2-enu'], 'Alkohol II-rzędowy → keton.'),
])

T['c-karboksylowe'] = dict(F=[
 ('Grupa karboksylowa', '–COOH; kwasy karboksylowe są słabymi kwasami.'),
 ('Moc kwasów karboksylowych', 'HCOOH > CH₃COOH > C₂H₅COOH; podstawniki elektroujemne (Cl) przy C-α zwiększają moc.'),
 ('Kwas mrówkowy — wyjątkowa właściwość', 'Ma grupę aldehydową — daje próbę Tollensa i odbarwia KMnO₄.'),
 ('Reakcja kwasu z metalem aktywnym', '2CH₃COOH + Mg → (CH₃COO)₂Mg + H₂.'),
 ('Reakcja kwasu z węglanem', '2CH₃COOH + Na₂CO₃ → 2CH₃COONa + CO₂ + H₂O — dowód, że kwas octowy jest mocniejszy od węglowego.'),
 ('Wyższe kwasy tłuszczowe', 'Palmitynowy C₁₅H₃₁COOH, stearynowy C₁₇H₃₅COOH (nasycone), oleinowy C₁₇H₃₃COOH (1 C=C).'),
 ('Mydła', 'Sole sodowe/potasowe wyższych kwasów tłuszczowych; w twardej wodzie tworzą osady z Ca²⁺/Mg²⁺.'),
 ('Odczyn roztworu mydła', 'Zasadowy — hydroliza anionu RCOO⁻.'),
 ('Temperatura wrzenia kwasów', 'Wysoka — tworzą dimery przez wiązania wodorowe.'),
 ('Hydroksykwasy', 'Mają –OH i –COOH, np. kwas mlekowy CH₃CH(OH)COOH (chiralny).'),
 ('Kwas szczawiowy', 'HOOC–COOH — najprostszy dikarboksylowy, reduktor (z KMnO₄ → CO₂).'),
 ('Bezwodniki i chlorki kwasowe', 'Pochodne kwasów reagujące z alkoholami nieodwracalnie (większa wydajność niż estryfikacja).'),
], Q=[
 ('Który kwas daje próbę Tollensa?', ['*mrówkowy', 'octowy', 'propanowy', 'benzoesowy'], 'Ma fragment aldehydowy.'),
])

T['c-cukry'] = dict(F=[
 ('Monosacharydy — podział', 'Aldozy (grupa –CHO) i ketozy (grupa C=O); triozy, tetrozy, pentozy, heksozy.'),
 ('Glukoza', 'Aldoheksoza C₆H₁₂O₆; redukująca; w roztworze głównie forma pierścieniowa (piranoza).'),
 ('Fruktoza', 'Ketoheksoza; daje próby Tollensa i Trommera (w środowisku zasadowym przechodzi w aldozę), ale NIE odbarwia wody bromowej.'),
 ('Odróżnienie glukozy od fruktozy', 'Woda bromowa — odbarwia tylko glukoza.'),
 ('Anomery α i β', 'Różnią się położeniem –OH przy węglu anomerycznym (C1 aldozy); szereg D: α — pod płaszczyzną w Haworthcie.'),
 ('Mutarotacja', 'Przechodzenie α ⇄ β w roztworze przez formę łańcuchową.'),
 ('Szereg D/L', 'Według położenia –OH przy przedostatnim atomie węgla w projekcji Fischera (D — po prawej).'),
 ('Sacharoza', 'Glukoza + fruktoza, wiązanie α,β-1,2-glikozydowe; nieredukująca.'),
 ('Maltoza i laktoza', 'Disacharydy redukujące (wolna grupa półacetalowa).'),
 ('Skrobia', 'Amyloza (α-1,4) + amylopektyna (α-1,4 i α-1,6); z jodem — granatowe zabarwienie.'),
 ('Celuloza', 'β-1,4-glukoza; łańcuchy proste, wiązania wodorowe → włókna; nie barwi się jodem.'),
 ('Hydroliza sacharozy', 'Daje cukier inwertowany (glukoza + fruktoza) — redukujący.'),
 ('Wielohydroksylowość cukrów — próba', 'Cu(OH)₂ na zimno → szafirowy roztwór (–OH przy sąsiednich atomach C).'),
], Q=[
 ('Cukrem nieredukującym jest:', ['*sacharoza', 'maltoza', 'glukoza', 'laktoza'], 'Brak wolnej grupy półacetalowej.'),
 ('Wodą bromową odróżnisz:', ['*glukozę od fruktozy', 'skrobię od celulozy', 'maltozę od laktozy', 'sacharozę od skrobi'], 'Tylko aldoza się utlenia.'),
])

T['c-aminy'] = dict(F=[
 ('Rzędowość amin', 'I: R–NH₂, II: R₂NH, III: R₃N — liczba grup węglowodorowych przy azocie (inaczej niż w alkoholach!).'),
 ('Charakter chemiczny amin', 'Zasadowy — wolna para elektronowa na N przyłącza H⁺.'),
 ('Zasadowość: metyloamina vs anilina', 'Metyloamina silniejsza (grupa alkilowa zwiększa gęstość elektronową na N); anilina słabsza (para N sprzężona z pierścieniem).'),
 ('Reakcja aminy z kwasem', 'CH₃NH₂ + HCl → CH₃NH₃⁺Cl⁻ (chlorek metyloamoniowy) — sól dobrze rozpuszczalna.'),
 ('Odczyn wodnego roztworu metyloaminy', 'Zasadowy: CH₃NH₂ + H₂O ⇄ CH₃NH₃⁺ + OH⁻.'),
 ('Anilina z wodą bromową', '2,4,6-tribromoanilina (biały osad) — –NH₂ silnie aktywuje pierścień.'),
 ('Otrzymywanie aniliny', 'Redukcja nitrobenzenu (Fe/HCl lub H₂/Ni).'),
 ('Amina I-rzędowa + HNO₂', 'Alkohol + N₂ (dla alifatycznych); wydziela się bezbarwny gaz.'),
 ('Amidy', 'R–CONH₂; wiązanie amidowe; mocznik (NH₂)₂CO — diamid kwasu węglowego.'),
 ('Hydroliza amidu', 'W kwasie → kwas + sól amonowa; w zasadzie → sól kwasu + NH₃.'),
 ('Temperatura wrzenia amin', 'Niższa niż alkoholi o podobnej masie (słabsze wiązania wodorowe N–H···N).'),
], Q=[
 ('Najsilniejszą zasadą jest:', ['*dimetyloamina', 'anilina', 'amoniak', 'acetamid'], 'Dwie grupy alkilowe; amidy są praktycznie obojętne.'),
 ('Produkt reakcji aniliny z HCl to:', ['*chlorek aniliniowy', 'chlorobenzen', 'p-chloroanilina', 'nitrobenzen'], 'Sól — reakcja kwas–zasada.'),
])

T['c-chemia-zycia'] = dict(F=[
 ('Tłuszcze — budowa', 'Estry glicerolu i wyższych kwasów tłuszczowych (triacyloglicerole).'),
 ('Tłuszcze ciekłe vs stałe', 'Ciekłe (oleje) — przewaga reszt nienasyconych; stałe — nasyconych.'),
 ('Utwardzanie tłuszczów', 'Uwodornienie wiązań C=C (H₂, Ni) — margaryna.'),
 ('Zmydlanie', 'Hydroliza zasadowa tłuszczu → glicerol + mydło.'),
 ('Wykrywanie nienasycenia tłuszczu', 'Odbarwienie wody bromowej (lub KMnO₄).'),
 ('Białka — wykrywanie', 'Reakcja biuretowa (Cu(OH)₂ → fioletowe), ksantoproteinowa (HNO₃ → żółte, pierścienie aromatyczne).'),
 ('Denaturacja białek', 'Nieodwracalna utrata struktury: wysoka temperatura, sole metali ciężkich, alkohol, stężone kwasy.'),
 ('Wysalanie białek', 'Odwracalne wytrącenie solami metali lekkich lub solami amonowymi (np. NaCl, (NH₄)₂SO₄).'),
 ('Detergenty a mydła', 'Detergenty (np. alkilobenzenosulfoniany) nie tworzą osadów w twardej wodzie.'),
 ('Budowa cząsteczki substancji powierzchniowo czynnej', 'Część hydrofilowa (głowa jonowa) + hydrofobowa (łańcuch węglowodorowy) — micele.'),
 ('Konserwanty', 'Np. kwas benzoesowy (E210), sorbowy (E200) i ich sole — hamują rozwój drobnoustrojów.'),
], Q=[
 ('Reakcja ksantoproteinowa wykrywa w białkach:', ['*pierścienie aromatyczne', 'wiązania peptydowe', 'grupy –SH', 'wiązania wodorowe'], 'Nitrowanie pierścieni (Tyr, Phe, Trp).'),
 ('Produktem zmydlania tłuszczu jest:', ['*glicerol i mydło', 'glicerol i kwas tłuszczowy', 'etanol i mydło', 'tylko mydło'], 'Hydroliza zasadowa.'),
])

T['c-oddzialywania'] = dict(F=[
 ('Wiązanie wodorowe — warunek', 'H połączony z F, O lub N oddziałuje z wolną parą innego F, O, N.'),
 ('Wpływ wiązań wodorowych na temperaturę wrzenia', 'Podwyższają ją: H₂O (100°C) vs H₂S (−60°C); etanol (78°C) vs etanotiol (35°C).'),
 ('Oddziaływania dipol–dipol', 'Między cząsteczkami polarnymi (np. HCl, aceton).'),
 ('Siły dyspersyjne (van der Waalsa)', 'Między wszystkimi cząsteczkami; rosną z masą i powierzchnią cząsteczki.'),
 ('Dlaczego lód pływa po wodzie?', 'Wiązania wodorowe tworzą w lodzie ażurową sieć — gęstość lodu mniejsza niż wody.'),
 ('„Podobne rozpuszcza podobne”', 'Substancje polarne rozpuszczają się w polarnych (woda), niepolarne w niepolarnych (heksan).'),
 ('Rozpuszczalność alkoholi w wodzie', 'Maleje ze wzrostem łańcucha (rośnie część hydrofobowa).'),
 ('Kryształ molekularny', 'Cząsteczki połączone słabymi oddziaływaniami — niska temperatura topnienia (I₂, lód, CO₂).'),
 ('Kryształ kowalencyjny', 'Sieć wiązań kowalencyjnych — bardzo twardy, wysoka temperatura topnienia (diament, SiO₂).'),
 ('Kryształ jonowy', 'Wysoka temperatura topnienia, przewodzi po stopieniu i w roztworze (NaCl, MgO).'),
 ('Kryształ metaliczny', 'Kationy w „gazie elektronowym” — przewodzi w stanie stałym, kowalny.'),
], Q=[
 ('Najwyższą temperaturę wrzenia ma:', ['*H₂O', 'H₂S', 'H₂Se', 'CH₄'], 'Wiązania wodorowe.'),
 ('Kryształ, który przewodzi prąd w stanie stałym, to:', ['*metaliczny', 'jonowy', 'molekularny', 'kowalencyjny'], 'Swobodne elektrony.'),
])

T['c-srodowisko'] = dict(F=[
 ('Efekt cieplarniany — główne gazy', 'CO₂, CH₄, N₂O, para wodna, freony.'),
 ('Kwaśne deszcze — przyczyny', 'Tlenki siarki (spalanie węgla) i azotu (silniki, energetyka) → H₂SO₄, HNO₃.'),
 ('Dziura ozonowa', 'Rozkład O₃ w stratosferze katalizowany przez rodniki Cl• z freonów (CFC).'),
 ('Smog fotochemiczny', 'NOₓ + węglowodory + światło → ozon troposferyczny, PAN (lato, ruch samochodowy).'),
 ('Smog londyński (kwaśny)', 'SO₂ + pyły + mgła (zima, spalanie węgla).'),
 ('Katalizator samochodowy', 'Pt, Pd, Rh: utlenia CO i węglowodory do CO₂, redukuje NOₓ do N₂.'),
 ('Odsiarczanie spalin', 'CaCO₃ lub Ca(OH)₂ wiąże SO₂ → CaSO₃ → CaSO₄ (gips).'),
 ('Eutrofizacja', 'Nadmiar azotanów i fosforanów w wodach → zakwity glonów, deficyt tlenu.'),
 ('Twardość wody — rodzaje', 'Przemijająca (wodorowęglany, usuwalna gotowaniem) i trwała (siarczany, chlorki Ca i Mg).'),
 ('Zmiękczanie wody trwałej', 'Na₂CO₃ lub wymieniacze jonowe (jony Ca²⁺, Mg²⁺ wymieniane na Na⁺ lub H⁺).'),
], Q=[
 ('Za niszczenie warstwy ozonowej odpowiadają głównie:', ['*freony', 'tlenki siarki', 'CO₂', 'metan'], 'Rodniki chloru.'),
 ('Twardość przemijającą wody powodują:', ['*wodorowęglany wapnia i magnezu', 'siarczany wapnia', 'chlorki sodu', 'azotany potasu'], 'Rozkładają się przy gotowaniu.'),
])
