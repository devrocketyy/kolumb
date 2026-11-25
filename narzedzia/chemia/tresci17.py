# Treści kursu chemii — porcja 17: fiszki — wzory, nazwy, reakcje charakterystyczne.
T = {}

T['c-wzory'] = dict(F=[
 ('Wzór kwasu azotowego(III)', 'HNO₂'),
 ('Wzór kwasu chlorowego(VII)', 'HClO₄'),
 ('Wzór siarczanu(IV) sodu', 'Na₂SO₃'),
 ('Wzór tiosiarczanu sodu', 'Na₂S₂O₃'),
 ('Wzór manganianu(VII) potasu', 'KMnO₄'),
 ('Wzór dichromianu(VI) potasu', 'K₂Cr₂O₇'),
 ('Wzór wodorowęglanu wapnia', 'Ca(HCO₃)₂'),
 ('Wzór fosforanu(V) wapnia', 'Ca₃(PO₄)₂'),
 ('Wzór azotku magnezu', 'Mg₃N₂'),
 ('Wzór węgliku wapnia (karbidu)', 'CaC₂'),
 ('Wzór kwasu ortokrzemowego', 'H₄SiO₄'),
 ('Nazwa systematyczna NaClO', 'Chloran(I) sodu.'),
])

T['c-izomeria'] = dict(F=[
 ('Nazwa systematyczna CH₃–CH(CH₃)–CH₂–CH₃', '2-metylobutan.'),
 ('Zasada numeracji łańcucha', 'Najdłuższy łańcuch; numeracja tak, by podstawniki (grupa funkcyjna) miały najniższe lokanty.'),
 ('Kolejność podstawników w nazwie', 'Alfabetyczna (bromo, chloro, etylo, metylo…); przedrostki di-, tri- nie wpływają na kolejność.'),
 ('Liczba izomerów konstytucyjnych C₄H₁₀O (alkohole)', '4: butan-1-ol, butan-2-ol, 2-metylopropan-1-ol, 2-metylopropan-2-ol.'),
 ('Liczba izomerów C₄H₉Cl', '4 izomery konstytucyjne (1- i 2-chlorobutan, 1-chloro-2-metylopropan, 2-chloro-2-metylopropan); 2-chlorobutan ma dodatkowo 2 enancjomery.'),
 ('Konfiguracja R/S — kryterium', 'Priorytety podstawników wg liczby atomowej; patrzymy z najniższym priorytetem z tyłu.'),
 ('Diastereoizomery cis–trans a właściwości', 'Różnią się temperaturą wrzenia i topnienia (enancjomery — nie, tylko skręcalnością).'),
])

T['c-alkany'] = dict(F=[
 ('Rzędowość atomu węgla', 'Liczba atomów węgla połączonych z danym atomem (I–IV).'),
 ('Metan — budowa i występowanie', 'CH₄, tetraedr; główny składnik gazu ziemnego.'),
 ('Gaz LPG', 'Mieszanina propanu i butanu.'),
 ('Destylacja ropy naftowej — frakcje', 'Gazy, benzyna, nafta, olej napędowy, mazut (od najniższej temperatury wrzenia).'),
 ('Halogenoalkany — reakcja z KOH (woda)', 'Substytucja nukleofilowa → alkohol.'),
 ('Halogenoalkany — reakcja z KOH (etanol)', 'Eliminacja → alken.'),
 ('Synteza Wurtza', '2R–X + 2Na → R–R + 2NaX (wydłużenie łańcucha).'),
])

T['c-polecenia'] = dict(F=[
 ('Częsty błąd: „roztwór się rozpuścił”', 'Rozpuszcza się substancja, nie roztwór; metal w kwasie „roztwarza się”.'),
 ('Częsty błąd: obserwacja „wydziela się wodór”', 'To wniosek — obserwacja: „wydziela się bezbarwny, bezwonny gaz”.'),
 ('Częsty błąd w równaniach redoks', 'Strzałka „⇄” zamiast „→” tam, gdzie trzeba wskazać kierunek przemiany.'),
 ('Uzasadnienie musi odnosić się do…', 'Informacji z zadania i budowy/właściwości substancji — ogólnik nie wystarczy.'),
])

T['c-hydroliza'] = dict(F=[
 ('Hydroliza siarczków', 'S²⁻ + H₂O ⇄ HS⁻ + OH⁻ — roztwory siarczków litowców są zasadowe.'),
 ('Hydroliza soli żelaza(III)', 'Roztwór FeCl₃ jest kwasowy; ogrzanie pogłębia hydrolizę (brunatnienie).'),
 ('Wpływ temperatury na hydrolizę', 'Hydroliza jest endotermiczna — ogrzewanie ją nasila.'),
 ('Hamowanie hydrolizy', 'Zakwaszenie (dla hydrolizy kationowej) lub zalkalizowanie (dla anionowej).'),
 ('Sól pochodząca od słabego kwasu i słabej zasady, Ka > Kb', 'Odczyn słabo kwasowy (np. HCOONH₄).'),
])

T['c-ph'] = dict(F=[
 ('pH roztworu buforowego (wzór)', 'pH = pKa + log(c_soli / c_kwasu) — Henderson–Hasselbalch.'),
 ('Pojemność buforowa', 'Ilość kwasu/zasady, którą bufor zneutralizuje bez znacznej zmiany pH; największa przy c_soli = c_kwasu.'),
 ('Bufory w organizmie', 'Wodorowęglanowy (krew, pH 7,4), fosforanowy (komórki), białczanowy.'),
 ('pH krwi', 'Ok. 7,35–7,45.'),
 ('pH soku żołądkowego', 'Ok. 1–2 (HCl).'),
])

T['c-energetyka'] = dict(F=[
 ('Układ otwarty, zamknięty, izolowany', 'Otwarty — wymienia masę i energię; zamknięty — tylko energię; izolowany — nic.'),
 ('Proces samorzutny', 'Zachodzi bez dostarczania energii z zewnątrz (np. rozpuszczanie soli, spalanie po zainicjowaniu).'),
 ('Ciepło właściwe wody', 'ok. 4,18 J/(g·K) — do obliczeń kalorymetrycznych: Q = m·c·ΔT.'),
 ('Kalorymetria — zasada', 'Ciepło reakcji = ciepło pochłonięte przez wodę (Q = m·c·ΔT); znak ΔH przeciwny.'),
])

T['c-rownowaga'] = dict(F=[
 ('Stała dysocjacji jako stała równowagi', 'Ka i Kb są stałymi równowagi — zależą tylko od temperatury.'),
 ('Kp a Kc', 'Kp wyrażona ciśnieniami cząstkowymi; dla Δn = 0 Kp = Kc.'),
 ('Wpływ gazu obojętnego (V = const)', 'Nie przesuwa równowagi (stężenia reagentów bez zmian).'),
 ('Wydajność a stała równowagi', 'Duże K → duża wydajność równowagowa (w danych warunkach).'),
])

T['c-szybkosc'] = dict(F=[
 ('Kataliza homogeniczna', 'Katalizator w tej samej fazie co reagenty (np. H⁺ w estryfikacji).'),
 ('Kataliza heterogeniczna', 'Katalizator w innej fazie — reakcja na powierzchni (Fe w syntezie NH₃, Pt w katalizatorach).'),
 ('Enzymy', 'Biokatalizatory białkowe — specyficzne, działają w łagodnych warunkach (temperatura, pH).'),
 ('Autokataliza', 'Produkt reakcji jest jej katalizatorem (np. Mn²⁺ w reakcji MnO₄⁻ ze szczawianami).'),
 ('Okres półtrwania reakcji I rzędu', 'Stały, niezależny od stężenia początkowego: t½ = 0,693/k.'),
])

T['c-cukry'] = dict(F=[
 ('Glikogen', 'Zapasowy polisacharyd zwierząt; silnie rozgałęziony (α-1,4 i α-1,6).'),
 ('Chityna', 'Polisacharyd z N-acetyloglukozaminy — pancerze stawonogów, ściany grzybów.'),
 ('Laktoza', 'Galaktoza + glukoza (β-1,4); cukier mleczny, redukujący.'),
 ('Maltoza', 'Dwie glukozy (α-1,4); powstaje przy hydrolizie skrobi.'),
 ('Wzór Hawortha — zasada', 'Pierścień płaski; grupy po prawej w projekcji Fischera — pod płaszczyzną.'),
])

T['c-aminokwasy'] = dict(F=[
 ('Elektroforeza aminokwasów', 'Przy pH > pI — anion, wędruje do anody; pH < pI — kation, do katody.'),
 ('Białka proste i złożone', 'Proste — tylko aminokwasy; złożone — z częścią niebiałkową (np. hemoglobina z hemem).'),
 ('Funkcje białek', 'Enzymatyczna, budulcowa (kolagen), transportowa (hemoglobina), regulacyjna (hormony), obronna (przeciwciała).'),
 ('Wiązanie peptydowe — cechy', 'Płaskie (częściowo podwójne), sztywne; atomy C, O, N, H w jednej płaszczyźnie.'),
])

T['c-tlenki'] = dict(F=[
 ('Tlenek azotu(V)', 'N₂O₅ — bezwodnik kwasu azotowego(V).'),
 ('Tlenek fosforu(V)', 'P₄O₁₀ — silnie higroskopijny, środek suszący.'),
 ('Tlenek węgla(IV) w wodzie', 'CO₂ + H₂O ⇄ H₂CO₃ — odczyn słabo kwasowy.'),
 ('Tlenek siarki(IV) — właściwości', 'Gaz o ostrym zapachu, reduktor (odbarwia KMnO₄), z wodą — H₂SO₃.'),
 ('Tlenki metali przejściowych — barwy', 'CuO czarny, Cu₂O czerwony, Fe₂O₃ czerwonobrunatny, Cr₂O₃ zielony, MnO₂ brunatnoczarny.'),
])
