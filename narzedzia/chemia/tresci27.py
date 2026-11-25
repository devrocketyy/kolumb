# Treści kursu chemii — porcja 27: fiszki do najsłabiej obsadzonych poddziałów (obliczenia, roztwory, równowaga).
T = {}

T['c-mol'] = dict(F=[
 ('Liczba Avogadra', '6,02 · 10²³ drobin w 1 molu.'),
 ('Objętość molowa gazu (warunki normalne)', '22,4 dm³/mol przy 0°C i 1013 hPa.'),
 ('Równanie Clapeyrona', 'pV = nRT; R = 83,1 hPa·dm³/(mol·K).'),
 ('Gęstość gazu a masa molowa', 'd = M / Vₘ — w warunkach normalnych M = d · 22,4.'),
 ('Gęstość względna gazu', 'D = M₁/M₂ — np. gaz 2 razy cięższy od powietrza ma M ≈ 58 g/mol.'),
 ('Średnia masa molowa powietrza', 'ok. 29 g/mol — gazy o M < 29 są lżejsze od powietrza.'),
 ('Liczba moli z liczby drobin', 'n = N / Nₐ.'),
 ('Masa atomowa a masa molowa', 'Liczbowo równe: 1 u ↔ 1 g/mol.'),
 ('Prawo Avogadra', 'Równe objętości gazów w tych samych warunkach zawierają tyle samo cząsteczek.'),
 ('Przeliczanie temperatury na kelwiny', 'T = t + 273 (np. 25°C = 298 K).'),
 ('Mieszanina gazów — skład objętościowy', 'Procent objętościowy = procent molowy (dla gazów doskonałych).'),
 ('Typowy błąd: objętość molowa', '22,4 dm³/mol stosujesz tylko do gazów i tylko w warunkach normalnych.'),
])

T['c-stechiometria'] = dict(F=[
 ('Substrat w niedomiarze', 'Ten, który przereaguje całkowicie i wyznacza ilość produktu.'),
 ('Jak wyznaczyć niedomiar', 'Podziel liczby moli substratów przez ich współczynniki — mniejszy iloraz to niedomiar.'),
 ('Wydajność reakcji', 'W = (ilość otrzymana / ilość teoretyczna) · 100%.'),
 ('Wydajność procesu wieloetapowego', 'Iloczyn wydajności etapów, np. 0,9 · 0,8 = 72%.'),
 ('Prawo zachowania masy', 'Masa substratów = masa produktów (w układzie zamkniętym).'),
 ('Prawo stałości składu', 'Związek chemiczny ma stały stosunek masowy pierwiastków.'),
 ('Stosunek objętościowy gazów w reakcji', 'Równy stosunkowi współczynników (prawo Gay-Lussaca).'),
 ('Czystość substratu w obliczeniach', 'Do równania bierz tylko masę czystej substancji: m · (% czystości).'),
 ('Mieszanina dwóch substancji — metoda', 'Oznacz liczby moli x i y, ułóż dwa równania (masa i produkt).'),
 ('Ubytek masy przy prażeniu', 'Masa gazu, który uleciał (np. CO₂ z CaCO₃, H₂O z hydratu).'),
 ('Hydrat — wyznaczanie wzoru', 'Stosunek moli soli bezwodnej i wody, np. CuSO₄ : H₂O = 1 : 5.'),
 ('Sprawdzenie sensu wyniku', 'Produkt nie może ważyć więcej niż substraty; wydajność ≤ 100%.'),
])

T['c-rozpuszczalnosc'] = dict(F=[
 ('Rozpuszczalność', 'Maksymalna masa substancji, którą można rozpuścić w 100 g rozpuszczalnika w danej temperaturze.'),
 ('Roztwór nasycony', 'Nie można w nim rozpuścić więcej substancji w danej temperaturze.'),
 ('Roztwór przesycony', 'Zawiera więcej substancji niż wynosi rozpuszczalność; nietrwały — po dodaniu kryształka krystalizuje.'),
 ('Stężenie roztworu nasyconego', 'cₚ = R / (100 + R) · 100%.'),
 ('Krystalizacja przez ochłodzenie', 'Masa wydzielonych kryształów = różnica rozpuszczalności (przeliczona na masę roztworu).'),
 ('Wpływ temperatury na rozpuszczalność ciał stałych', 'Zwykle rośnie (wyjątki: np. Ca(OH)₂, Li₂CO₃ — maleje).'),
 ('Wpływ ciśnienia na rozpuszczalność gazów', 'Wzrost ciśnienia zwiększa rozpuszczalność gazu (napoje gazowane).'),
 ('Iloczyn rozpuszczalności Kₛ', 'Iloczyn stężeń jonów w roztworze nasyconym trudno rozpuszczalnej soli, np. Kₛ(AgCl) = [Ag⁺][Cl⁻].'),
 ('Warunek strącenia osadu', 'Iloczyn jonowy > Kₛ.'),
 ('Efekt wspólnego jonu', 'Dodatek jonu obecnego w osadzie zmniejsza jego rozpuszczalność.'),
 ('Odczyt z wykresu rozpuszczalności', 'Wartość na osi Y dotyczy 100 g wody, nie 100 g roztworu.'),
 ('Hydrat a rozpuszczalność', 'Przy rozpuszczaniu hydratu woda krystalizacyjna dołącza do rozpuszczalnika.'),
])

T['c-mieszanie'] = dict(F=[
 ('Reguła mieszania (krzyżowa)', 'm₁ : m₂ = (c₂ − c) : (c − c₁).'),
 ('Woda w regule krzyżowej', 'Ma stężenie 0%.'),
 ('Czysta substancja w regule krzyżowej', 'Ma stężenie 100%.'),
 ('Zatężanie przez odparowanie', 'Masa substancji stała, masa roztworu maleje o masę odparowanej wody.'),
 ('Rozcieńczanie roztworu molowego', 'c₁V₁ = c₂V₂.'),
 ('Mieszanie roztworów molowych', 'c = (c₁V₁ + c₂V₂) / (V₁ + V₂) — przy założeniu addytywności objętości.'),
 ('Przeliczanie cₚ na c (mol/dm³)', 'c = cₚ · d · 10 / M (d w g/cm³).'),
 ('Przeliczanie c na cₚ', 'cₚ = c · M / (10 · d).'),
 ('Dodanie substancji do roztworu', 'Rośnie i masa substancji, i masa roztworu.'),
 ('Typowy błąd przy rozcieńczaniu', 'Masa roztworu po dodaniu wody = masa roztworu + masa wody (nie samej wody).'),
])

T['c-stezenia'] = dict(F=[
 ('Stężenie procentowe', 'cₚ = mₛ / m_r · 100%.'),
 ('Stężenie molowe', 'c = n / V (mol/dm³).'),
 ('Masa roztworu z objętości', 'm = d · V.'),
 ('Ppm', 'Liczba części na milion — 1 ppm = 1 mg substancji na 1 kg roztworu.'),
 ('Stężenie jonów z dysocjacji', 'Pomnóż stężenie soli przez liczbę jonów danego rodzaju, np. 0,1 M Na₂SO₄ → [Na⁺] = 0,2 M.'),
 ('Sporządzanie roztworu o danym stężeniu molowym', 'Odważ substancję, rozpuść, uzupełnij wodą w kolbie miarowej do kreski.'),
])

T['c-rownowaga'] = dict(F=[
 ('Stan równowagi dynamicznej', 'Szybkości reakcji w obu kierunkach są równe, stężenia się nie zmieniają.'),
 ('Stała równowagi Kc', 'Iloczyn stężeń produktów / iloczyn stężeń substratów, w potęgach współczynników.'),
 ('Duża wartość K', 'W stanie równowagi przeważają produkty.'),
 ('Iloraz reakcji Q', 'Wyrażenie jak K, ale dla dowolnej chwili; Q < K — reakcja biegnie w prawo.'),
 ('Stała dla reakcji odwrotnej', 'K′ = 1 / K.'),
 ('Stała dla reakcji pomnożonej przez 2', 'K′ = K².'),
 ('Wpływ gazu obojętnego (V = const)', 'Nie przesuwa równowagi.'),
 ('Reakcja egzotermiczna a temperatura', 'Wzrost T przesuwa równowagę w lewo i zmniejsza K.'),
 ('Reakcja endotermiczna a temperatura', 'Wzrost T przesuwa równowagę w prawo i zwiększa K.'),
 ('Synteza amoniaku — warunki przemysłowe', 'Ok. 450°C, 20–30 MPa, katalizator żelazowy — kompromis między wydajnością a szybkością.'),
 ('Wydajność w stanie równowagi', 'Liczba moli produktu w równowadze / teoretyczna liczba moli · 100%.'),
 ('Stopień przereagowania', 'Część substratu, która przereagowała do chwili osiągnięcia równowagi.'),
])

T['c-oddzialywania'] = dict(F=[
 ('Wiązanie wodorowe', 'Oddziaływanie atomu H związanego z F, O lub N z wolną parą innego atomu F, O lub N.'),
 ('Siły van der Waalsa', 'Słabe oddziaływania między cząsteczkami; rosną z masą i powierzchnią cząsteczki.'),
 ('Oddziaływanie dipol–dipol', 'Przyciąganie przeciwnych biegunów cząsteczek polarnych.'),
 ('Temperatura wrzenia alkanów rozgałęzionych', 'Niższa niż izomerów prostołańcuchowych — mniejsza powierzchnia kontaktu.'),
 ('Anomalna gęstość wody', 'Największa w 4°C; lód jest lżejszy od wody (ażurowa sieć wiązań wodorowych).'),
 ('HF a HCl — temperatura wrzenia', 'HF wrze wyżej mimo mniejszej masy — wiązania wodorowe.'),
 ('Kryształ kowalencyjny', 'Np. diament, SiO₂ — bardzo twardy, bardzo wysoka temperatura topnienia, nie przewodzi.'),
 ('Kryształ molekularny', 'Np. I₂, lód, CO₂(s) — niska temperatura topnienia, miękki.'),
 ('Kryształ jonowy', 'Np. NaCl — wysoka temperatura topnienia, przewodzi w stopie i roztworze.'),
 ('Grafit przewodzi prąd', 'Każdy atom C ma jeden zdelokalizowany elektron między warstwami.'),
 ('Rozpuszczalność alkoholi w wodzie', 'Maleje ze wzrostem łańcucha — rośnie część hydrofobowa.'),
 ('Etery a alkohole — lotność', 'Etery bardziej lotne — nie tworzą wiązań wodorowych między sobą.'),
])

T['c-bilans'] = dict(F=[
 ('Równanie połówkowe w środowisku kwasowym', 'Brakujący tlen uzupełniasz H₂O, wodór — jonami H⁺.'),
 ('Równanie połówkowe w środowisku zasadowym', 'Brakujący tlen uzupełniasz OH⁻ (2OH⁻ → H₂O + „O”), nadmiar wodoru — przez H₂O i OH⁻.'),
 ('Dichromian(VI) w środowisku kwasowym', 'Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O (pomarańczowy → zielony).'),
 ('Nadtlenek wodoru jako utleniacz', 'H₂O₂ + 2H⁺ + 2e⁻ → 2H₂O.'),
 ('Nadtlenek wodoru jako reduktor', 'H₂O₂ → O₂ + 2H⁺ + 2e⁻.'),
 ('Kwas azotowy(V) stężony z miedzią', 'Cu + 4HNO₃ → Cu(NO₃)₂ + 2NO₂ + 2H₂O (brunatny gaz).'),
 ('Kwas azotowy(V) rozcieńczony z miedzią', '3Cu + 8HNO₃ → 3Cu(NO₃)₂ + 2NO + 4H₂O (bezbarwny NO).'),
 ('Sprawdzenie równania redoks', 'Liczba atomów każdego pierwiastka i suma ładunków po obu stronach równe.'),
 ('Stosunek molowy utleniacza do reduktora', 'Odwrotny do stosunku liczby elektronów wymienianych w równaniach połówkowych.'),
 ('Dysproporcjonowanie chloru w zasadzie na zimno', 'Cl₂ + 2OH⁻ → Cl⁻ + ClO⁻ + H₂O.'),
 ('Dysproporcjonowanie chloru w zasadzie na gorąco', '3Cl₂ + 6OH⁻ → 5Cl⁻ + ClO₃⁻ + 3H₂O.'),
])

T['c-wodorotlenki-kwasy'] = dict(F=[
 ('Wodorotlenki rozpuszczalne w wodzie', 'Litowców oraz Ca(OH)₂ (słabo), Sr(OH)₂, Ba(OH)₂.'),
 ('Otrzymywanie wodorotlenku trudno rozpuszczalnego', 'Sól + mocna zasada → osad, np. CuSO₄ + 2NaOH → Cu(OH)₂↓ + Na₂SO₄.'),
 ('Barwa Cu(OH)₂', 'Niebieski galaretowaty osad; po ogrzaniu czernieje (CuO).'),
 ('Barwa Fe(OH)₃', 'Brunatnoczerwony osad.'),
 ('Barwa Fe(OH)₂', 'Zielonkawy osad, na powietrzu brunatnieje (utlenia się).'),
 ('Kwasy beztlenowe', 'HF, HCl, HBr, HI, H₂S — roztwory wodorków w wodzie.'),
 ('Kwas fluorowodorowy', 'Słaby kwas, trawi szkło (reaguje z SiO₂).'),
 ('Kwas węglowy', 'Nietrwały: H₂CO₃ ⇄ CO₂ + H₂O; słaby, dwuprotonowy.'),
 ('Kwas siarkowy(IV)', 'Nietrwały, słaby; powstaje z SO₂ i wody.'),
 ('Moc kwasów tlenowych tego samego pierwiastka', 'Rośnie z liczbą atomów tlenu (stopniem utlenienia).'),
 ('Amfoteryczność Zn(OH)₂', 'Zn(OH)₂ + 2OH⁻ → [Zn(OH)₄]²⁻; Zn(OH)₂ + 2H⁺ → Zn²⁺ + 2H₂O.'),
])

T['c-energetyka'] = dict(F=[
 ('Entalpia tworzenia', 'ΔH reakcji otrzymywania 1 mola związku z pierwiastków w stanie standardowym.'),
 ('Entalpia tworzenia pierwiastka', 'Równa zero (dla postaci trwałej w warunkach standardowych).'),
 ('ΔH z entalpii tworzenia', 'ΔH = Σ ΔHₜ(produktów) − Σ ΔHₜ(substratów).'),
 ('ΔH z energii wiązań', 'ΔH = Σ E(wiązań zrywanych) − Σ E(wiązań tworzonych).'),
 ('Entalpia spalania', 'ΔH spalenia 1 mola substancji do CO₂ i H₂O.'),
 ('Energia aktywacji a ΔH', 'Niezależne: katalizator zmienia Eₐ, nie zmienia ΔH.'),
 ('Zmiana znaku ΔH', 'Reakcja odwrotna ma ΔH o przeciwnym znaku.'),
 ('Ciepło z masy substancji', 'Q = n · |ΔH| — najpierw policz liczbę moli.'),
])

T['c-szybkosc'] = dict(F=[
 ('Szybkość reakcji', 'Zmiana stężenia reagenta w jednostce czasu (mol · dm⁻³ · s⁻¹).'),
 ('Równanie kinetyczne', 'v = k[A]ᵃ[B]ᵇ — wykładniki wyznacza się doświadczalnie.'),
 ('Reguła van ’t Hoffa', 'Wzrost temperatury o 10 K zwiększa szybkość 2–4 razy.'),
 ('Stała szybkości k', 'Zależy od temperatury i katalizatora, nie od stężeń.'),
 ('Inhibitor', 'Substancja spowalniająca reakcję.'),
 ('Kataliza homogeniczna', 'Katalizator w tej samej fazie co reagenty.'),
 ('Kataliza heterogeniczna', 'Katalizator w innej fazie (np. Pt w katalizatorze samochodowym).'),
 ('Enzym', 'Katalizator biologiczny — białko, działa wybiórczo i w łagodnych warunkach.'),
 ('Okres półtrwania reakcji', 'Czas, po którym stężenie substratu maleje o połowę.'),
 ('Szybkość z wykresu c(t)', 'Nachylenie krzywej; maleje w miarę zużywania substratu.'),
])

T['c-elektroliza'] = dict(F=[
 ('Prawo Faradaya', 'm = M · I · t / (z · F); F = 96 500 C/mol.'),
 ('Ładunek elektryczny', 'Q = I · t (A · s = C).'),
 ('Elektroliza stopionego NaCl', 'Katoda: Na⁺ + e⁻ → Na; anoda: 2Cl⁻ → Cl₂ + 2e⁻.'),
 ('Elektroliza wody (H₂SO₄ lub NaOH)', 'Katoda: H₂, anoda: O₂ w stosunku objętości 2 : 1.'),
 ('Rafinacja miedzi', 'Anoda z surowej miedzi roztwarza się, na katodzie osadza się czysta Cu.'),
 ('Galwanizacja', 'Pokrywanie przedmiotu (katody) warstwą metalu z roztworu jego soli.'),
 ('Korozja elektrochemiczna', 'Mikroogniwa na powierzchni metalu: metal aktywniejszy się utlenia.'),
 ('Ochrona katodowa', 'Połączenie z ujemnym biegunem źródła prądu.'),
])
