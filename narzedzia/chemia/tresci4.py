# Treści kursu chemii — porcja 4: Energetyka, kinetyka i równowaga (IV) oraz roztwory (V).

T = {}

T['c-energetyka'] = dict(F=[
 ('Wyjaśnij pojęcie: układ i otoczenie', 'Układ — wyodrębniona część materii, którą badamy (np. reagenty w probówce); otoczenie — wszystko poza układem.'),
 ('Układ otwarty, zamknięty i izolowany', 'Otwarty — wymienia z otoczeniem energię i materię; zamknięty — tylko energię; izolowany — ani energii, ani materii.'),
 ('Wyjaśnij pojęcie: reakcja egzotermiczna', 'Reakcja, w której układ oddaje ciepło do otoczenia; ΔH < 0 (np. spalanie, zobojętnianie).'),
 ('Wyjaśnij pojęcie: reakcja endotermiczna', 'Reakcja, w której układ pobiera ciepło z otoczenia; ΔH > 0 (np. rozkład termiczny CaCO₃, fotosynteza).'),
 ('Wyjaśnij pojęcie: entalpia (ΔH)', 'Ciepło reakcji przebiegającej pod stałym ciśnieniem; ΔH = H(produktów) − H(substratów).'),
 ('Wyjaśnij pojęcie: standardowa entalpia tworzenia', 'Efekt cieplny tworzenia 1 mola związku z pierwiastków w ich trwałych postaciach, w warunkach standardowych. Dla pierwiastków w stanie trwałym = 0.'),
 ('Jak obliczyć ΔH reakcji z entalpii tworzenia?', 'ΔH = Σ ΔH°tw(produktów) − Σ ΔH°tw(substratów), z uwzględnieniem współczynników stechiometrycznych.'),
 ('Prawo Hessa', 'Efekt cieplny reakcji zależy tylko od stanu początkowego i końcowego, a nie od drogi przemiany — można go obliczyć, sumując równania etapów.'),
 ('Jak korzystać z prawa Hessa?', 'Przekształcić podane równania (odwrócić — zmienić znak ΔH; pomnożyć przez liczbę — pomnożyć ΔH), aby ich suma dała szukaną reakcję; zsumować ΔH.'),
 ('Typowy błąd przy prawie Hessa', 'Odwrócenie równania bez zmiany znaku ΔH albo pomnożenie równania bez pomnożenia ΔH.'),
 ('Jak obliczyć ΔH z energii wiązań?', 'ΔH = Σ E(wiązań zrywanych w substratach) − Σ E(wiązań tworzonych w produktach).'),
 ('Wyjaśnij pojęcie: energia aktywacji', 'Minimalna energia, jaką muszą mieć zderzające się drobiny, aby reakcja zaszła (bariera energetyczna).'),
 ('Wykres energetyczny reakcji egzotermicznej', 'Produkty leżą niżej niż substraty; ΔH < 0; garb między nimi to energia aktywacji.'),
 ('Wyjaśnij pojęcie: kompleks aktywny (stan przejściowy)', 'Nietrwały układ atomów o najwyższej energii na drodze reakcji, w którym stare wiązania się rozrywają, a nowe tworzą.'),
 ('Czy katalizator zmienia ΔH reakcji?', 'Nie. Katalizator obniża energię aktywacji, ale ΔH (różnica energii produktów i substratów) zostaje taka sama.'),
], Q=[
 ('Reakcja ma ΔH = −90 kJ. Jest to reakcja:', ['endotermiczna', '*egzotermiczna', 'izotermiczna', 'nie da się ocenić'], 'ΔH < 0 — ciepło oddane do otoczenia.'),
 ('Jeśli dla reakcji A → B ΔH = +50 kJ, to dla B → A:', ['ΔH = +50 kJ', '*ΔH = −50 kJ', 'ΔH = 0', 'ΔH = +100 kJ'], 'Odwrócenie równania zmienia znak ΔH.'),
 ('Katalizator:', ['zmienia ΔH reakcji', '*obniża energię aktywacji', 'przesuwa równowagę', 'zużywa się w reakcji'], 'Działa na kinetykę, nie na termodynamikę.'),
 ('Standardowa entalpia tworzenia O₂(g) wynosi:', ['−286 kJ/mol', '*0', '+498 kJ/mol', 'nie da się określić'], 'Pierwiastek w stanie trwałym.'),
])

T['c-szybkosc'] = dict(F=[
 ('Wyjaśnij pojęcie: szybkość reakcji', 'Zmiana stężenia substratu (ubytek) lub produktu (przyrost) w jednostce czasu, np. v = Δc/Δt w mol·dm⁻³·s⁻¹.'),
 ('Czynniki wpływające na szybkość reakcji', 'Stężenie (ciśnienie gazów) reagentów, temperatura, stopień rozdrobnienia (powierzchnia), katalizator, rodzaj reagentów.'),
 ('Jak temperatura wpływa na szybkość reakcji?', 'Wzrost temperatury zwiększa szybkość — więcej drobin ma energię co najmniej równą energii aktywacji i zderzenia są częstsze (reguła van ’t Hoffa: +10°C → ok. 2–4 razy szybciej).'),
 ('Dlaczego rozdrobnienie przyspiesza reakcję?', 'Zwiększa powierzchnię kontaktu reagentów, więc rośnie liczba zderzeń skutecznych (np. pył węglowy spala się wybuchowo).'),
 ('Wyjaśnij pojęcie: równanie kinetyczne', 'Zależność szybkości od stężeń substratów, np. v = k·[A]ᵃ·[B]ᵇ; k — stała szybkości (zależy od temperatury i katalizatora, nie od stężeń).'),
 ('Jak zmieni się szybkość reakcji v = k[A]²[B], gdy [A] wzrośnie 2 razy?', 'Wzrośnie 4 razy (2²).'),
 ('Jak zmiana objętości naczynia wpływa na szybkość reakcji gazów?', 'Zmniejszenie objętości (wzrost ciśnienia) zwiększa stężenia gazów, a więc szybkość; np. dwukrotne zmniejszenie objętości → każde stężenie ×2.'),
 ('Wyjaśnij pojęcie: katalizator', 'Substancja, która zwiększa szybkość reakcji, obniżając energię aktywacji (zmienia mechanizm), i po reakcji pozostaje niezmieniona.'),
 ('Wyjaśnij pojęcie: inhibitor', 'Substancja zmniejszająca szybkość reakcji (np. przeciwutleniacze w żywności).'),
 ('Kataliza homogeniczna i heterogeniczna', 'Homogeniczna — katalizator i reagenty w tej samej fazie (np. H⁺ w roztworze); heterogeniczna — w różnych fazach (np. Pt, Fe w syntezie NH₃).'),
 ('Wyjaśnij pojęcie: okres półtrwania reakcji', 'Czas, po którym stężenie substratu zmniejsza się o połowę.'),
], Q=[
 ('v = k[A][B]. Jak zmieni się szybkość, gdy oba stężenia wzrosną dwukrotnie?', ['2 razy', '*4 razy', '8 razy', 'nie zmieni się'], '2 · 2 = 4.'),
 ('Który czynnik NIE zmienia stałej szybkości k?', ['temperatura', 'katalizator', '*stężenie substratów', 'rodzaj reakcji'], 'k zależy od temperatury i katalizatora.'),
 ('Dlaczego proszek cynku reaguje z kwasem szybciej niż granulka?', ['ma większą masę', '*ma większą powierzchnię kontaktu', 'ma inną entalpię', 'jest katalizatorem'], 'Więcej zderzeń skutecznych.'),
])

T['c-rownowaga'] = dict(F=[
 ('Wyjaśnij pojęcie: reakcja odwracalna', 'Reakcja, która może przebiegać w obu kierunkach; zapis ⇄.'),
 ('Wyjaśnij pojęcie: stan równowagi dynamicznej', 'Stan, w którym szybkości reakcji w obu kierunkach są równe, więc stężenia reagentów się nie zmieniają, choć obie reakcje wciąż zachodzą.'),
 ('Wyrażenie na stałą równowagi K', 'Dla aA + bB ⇄ cC + dD: K = [C]ᶜ[D]ᵈ / ([A]ᵃ[B]ᵇ) — stężenia równowagowe, wykładniki = współczynniki.'),
 ('Czego nie wpisuje się do wyrażenia na stałą równowagi?', 'Substancji stałych i czystych cieczy (np. C(s), CaCO₃(s), H₂O jako rozpuszczalnika).'),
 ('Od czego zależy wartość stałej równowagi?', 'Tylko od temperatury (i rodzaju reakcji). Nie zależy od stężeń, ciśnienia ani katalizatora.'),
 ('Co mówi duża wartość K (K ≫ 1)?', 'Że w stanie równowagi przeważają produkty — reakcja przebiega prawie do końca.'),
 ('Reguła przekory (Le Chateliera–Brauna)', 'Układ w równowadze, poddany zewnętrznemu działaniu, reaguje tak, by to działanie zmniejszyć — równowaga przesuwa się w stronę przeciwdziałającą zmianie.'),
 ('Jak zwiększenie stężenia substratu wpływa na równowagę?', 'Przesuwa ją w prawo (w stronę produktów); K się nie zmienia.'),
 ('Jak usunięcie produktu wpływa na równowagę?', 'Przesuwa ją w prawo — układ odtwarza usunięty produkt (sposób zwiększenia wydajności).'),
 ('Jak wzrost ciśnienia wpływa na równowagę reakcji gazowej?', 'Przesuwa ją w stronę mniejszej liczby moli gazów; gdy liczba moli gazów po obu stronach jest równa — brak wpływu.'),
 ('Jak wzrost temperatury wpływa na równowagę?', 'Przesuwa ją w stronę reakcji endotermicznej; dla reakcji egzotermicznej (ΔH < 0) — w lewo, a K maleje.'),
 ('Czy katalizator przesuwa równowagę?', 'Nie. Przyspiesza obie reakcje jednakowo, więc tylko skraca czas dojścia do równowagi.'),
 ('Typowy błąd według CKE 2026 w zadaniach z równowagą', 'Zastosowanie niewłaściwej stałej równowagi (np. wyrażenia dla innej reakcji lub z pominiętymi współczynnikami) albo podstawienie stężeń początkowych zamiast równowagowych.'),
 ('Jak liczyć stężenia równowagowe — tabela „start–zmiana–równowaga”?', 'Zapisać stężenia początkowe, zmianę wynikającą ze stechiometrii (x, 2x…) i stężenia równowagowe; podstawić do K i rozwiązać.'),
 ('Synteza amoniaku N₂ + 3H₂ ⇄ 2NH₃, ΔH < 0 — warunki korzystne dla wydajności', 'Wysokie ciśnienie (mniej moli gazów po prawej), niska temperatura (reakcja egzotermiczna) i usuwanie NH₃; w praktyce umiarkowana temperatura i katalizator (Fe) dla szybkości.'),
], Q=[
 ('Stała równowagi zależy od:', ['stężeń reagentów', 'ciśnienia', '*temperatury', 'katalizatora'], 'Tylko od temperatury.'),
 ('Dla reakcji 2SO₂ + O₂ ⇄ 2SO₃ (gazy) wzrost ciśnienia przesuwa równowagę:', ['w lewo', '*w prawo', 'nie wpływa', 'zależy od katalizatora'], '3 mole gazów → 2 mole gazów.'),
 ('Reakcja egzotermiczna w równowadze. Po podgrzaniu:', ['równowaga przesunie się w prawo', '*równowaga przesunie się w lewo, K zmaleje', 'K wzrośnie', 'nic się nie zmieni'], 'Ogrzewanie sprzyja reakcji endotermicznej (odwrotnej).'),
 ('Wyrażenie na stałą równowagi CaCO₃(s) ⇄ CaO(s) + CO₂(g) to:', ['K = [CaO][CO₂]/[CaCO₃]', '*K = [CO₂]', 'K = 1/[CO₂]', 'K = [CaO]/[CaCO₃]'], 'Ciał stałych nie wpisujemy.'),
 ('Dla H₂ + I₂ ⇄ 2HI (gazy) wzrost ciśnienia:', ['przesuwa równowagę w prawo', 'przesuwa w lewo', '*nie przesuwa równowagi', 'zmienia K'], 'Po obu stronach 2 mole gazów.'),
])

T['c-stezenia'] = dict(F=[
 ('Wyjaśnij pojęcie: roztwór', 'Jednorodna mieszanina rozpuszczalnika i substancji rozpuszczonej.'),
 ('Wyjaśnij pojęcie: stężenie procentowe (masowe)', 'Masa substancji rozpuszczonej w 100 g roztworu: Cp = (ms/mr) · 100%.'),
 ('Wyjaśnij pojęcie: stężenie molowe', 'Liczba moli substancji rozpuszczonej w 1 dm³ roztworu: Cm = n/V [mol/dm³].'),
 ('Masa roztworu', 'mr = ms + mrozp (masa substancji + masa rozpuszczalnika) albo mr = d · V.'),
 ('Typowy błąd: objętość roztworu a objętość wody', 'Do wzoru na Cm podstawia się objętość ROZTWORU, a nie użytej wody.'),
 ('Wzór na przeliczanie Cp na Cm', 'Cm = (Cp · d) / (M · 100%), d w g/dm³.'),
 ('Jak przygotować roztwór o określonym Cm?', 'Obliczyć n = Cm·V i m = n·M, odważyć substancję, rozpuścić w części wody w kolbie miarowej i uzupełnić wodą do kreski.'),
 ('Jak liczyć stężenie, gdy rozpuszczasz hydrat (np. CuSO₄·5H₂O)?', 'Masa substancji (ms) to tylko masa soli bezwodnej zawarta w hydracie; woda krystalizacyjna wchodzi do rozpuszczalnika.'),
 ('Typowy błąd przy rozpuszczaniu hydratu', 'Przyjęcie całej masy hydratu jako masy substancji rozpuszczonej.'),
 ('Stężenie jonów w roztworze soli', 'Zależy od wzoru soli, np. 0,1 mol/dm³ Na₂SO₄: [Na⁺] = 0,2 mol/dm³, [SO₄²⁻] = 0,1 mol/dm³.'),
 ('Wyjaśnij pojęcie: stężenie ppm', 'Liczba części masowych substancji na milion części roztworu (1 ppm = 1 mg/kg); używane przy bardzo małych stężeniach, np. zanieczyszczeń.'),
], Q=[
 ('W 200 g roztworu jest 30 g soli. Cp wynosi:', ['30%', '*15%', '20%', '17,6%'], '30/200 · 100%.'),
 ('W 500 cm³ roztworu jest 0,2 mola NaCl. Cm wynosi:', ['0,1 mol/dm³', '*0,4 mol/dm³', '0,2 mol/dm³', '2,5 mol/dm³'], '0,2 mol / 0,5 dm³.'),
 ('Jakie jest stężenie jonów Cl⁻ w 0,1 M CaCl₂?', ['0,1 mol/dm³', '*0,2 mol/dm³', '0,05 mol/dm³', '0,3 mol/dm³'], 'Każdy CaCl₂ daje 2 Cl⁻.'),
 ('Rozpuszczając hydrat, jako ms we wzorze na Cp przyjmujemy:', ['masę hydratu', '*masę soli bezwodnej w hydracie', 'masę wody krystalizacyjnej', 'masę rozpuszczalnika'], 'Woda krystalizacyjna dołącza do rozpuszczalnika.'),
])

T['c-rozpuszczalnosc'] = dict(F=[
 ('Wyjaśnij pojęcie: rozpuszczalność', 'Maksymalna masa substancji, jaką można rozpuścić w 100 g rozpuszczalnika w danej temperaturze, otrzymując roztwór nasycony.'),
 ('Wyjaśnij pojęcie: roztwór nasycony', 'Roztwór, w którym w danej temperaturze nie można już rozpuścić więcej substancji (pozostaje w równowadze z nierozpuszczonym osadem).'),
 ('Wyjaśnij pojęcie: roztwór nienasycony', 'Roztwór, w którym można jeszcze rozpuścić dodatkową porcję substancji w danej temperaturze.'),
 ('Wyjaśnij pojęcie: roztwór przesycony', 'Nietrwały roztwór zawierający więcej substancji niż roztwór nasycony; drobny kryształek wywołuje krystalizację nadmiaru.'),
 ('Jak temperatura wpływa na rozpuszczalność ciał stałych i gazów?', 'Rozpuszczalność większości ciał stałych rośnie ze wzrostem temperatury; rozpuszczalność gazów maleje (a rośnie ze wzrostem ciśnienia).'),
 ('Jak obliczyć Cp roztworu nasyconego z rozpuszczalności R?', 'Cp = R / (100 + R) · 100% (R — g substancji na 100 g wody).'),
 ('Typowy błąd: rozpuszczalność a stężenie procentowe', 'Utożsamianie rozpuszczalności (g na 100 g WODY) ze stężeniem procentowym (g na 100 g ROZTWORU).'),
 ('Jak obliczyć masę kryształów wydzielonych po ochłodzeniu roztworu nasyconego?', 'Policzyć masę substancji w roztworze w wyższej temperaturze i masę, która zostaje rozpuszczona w niższej (przy tej samej masie wody); różnica to masa kryształów.'),
 ('Wyjaśnij pojęcie: krystalizacja', 'Wydzielanie się substancji z roztworu w postaci kryształów, np. po ochłodzeniu roztworu nasyconego lub odparowaniu rozpuszczalnika.'),
 ('Jak odczytać rozpuszczalność z krzywej rozpuszczalności?', 'Znaleźć temperaturę na osi poziomej i odczytać z krzywej masę substancji na 100 g wody na osi pionowej.'),
], Q=[
 ('Rozpuszczalność soli w 20°C wynosi 25 g/100 g wody. Cp roztworu nasyconego to:', ['25%', '*20%', '33,3%', '12,5%'], '25/125 · 100%.'),
 ('Jak zmienia się rozpuszczalność gazów ze wzrostem temperatury?', ['rośnie', '*maleje', 'nie zmienia się', 'najpierw rośnie, potem maleje'], 'Dlatego ciepła woda zawiera mniej tlenu.'),
 ('Roztwór, w którym można jeszcze rozpuścić substancję, to roztwór:', ['nasycony', '*nienasycony', 'przesycony', 'koloidalny'], 'Nie osiągnięto rozpuszczalności.'),
])

T['c-mieszanie'] = dict(F=[
 ('Wyjaśnij pojęcie: rozcieńczanie roztworu', 'Dodawanie rozpuszczalnika — masa (liczba moli) substancji się nie zmienia, rośnie masa (objętość) roztworu, więc stężenie maleje.'),
 ('Wzór dla rozcieńczania (stężenie molowe)', 'C₁·V₁ = C₂·V₂ — liczba moli substancji przed i po rozcieńczeniu jest taka sama.'),
 ('Wzór dla rozcieńczania (stężenie procentowe)', 'Cp₁·m₁ = Cp₂·m₂ (masa substancji się nie zmienia).'),
 ('Wyjaśnij pojęcie: zatężanie roztworu', 'Zwiększanie stężenia przez odparowanie rozpuszczalnika albo dodanie substancji.'),
 ('Jak obliczyć Cp po zmieszaniu dwóch roztworów tej samej substancji?', 'Cp = (ms₁ + ms₂) / (mr₁ + mr₂) · 100% — sumuje się masy substancji i masy roztworów.'),
 ('Reguła krzyżowa (metoda krzyża)', 'Przy mieszaniu roztworów o stężeniach C₁ i C₂, by otrzymać C: masy roztworów mają się jak (C₂ − C) : (C − C₁). Woda = roztwór 0%, czysta substancja = 100%.'),
 ('Typowy błąd przy mieszaniu roztworów', 'Uśrednianie stężeń (np. (10% + 30%)/2 = 20%) bez uwzględnienia mas mieszanych roztworów.'),
 ('Czy objętości roztworów się sumują przy mieszaniu?', 'Nie zawsze dokładnie (kontrakcja objętości); w zadaniach z Cm przyjmuje się sumowanie objętości tylko wtedy, gdy polecenie na to pozwala.'),
 ('Jak liczyć stężenie po zmieszaniu roztworów, które ze sobą reagują?', 'Najpierw obliczyć mole reagentów i ustalić, co przereagowało (stechiometria, nadmiar), a dopiero potem stężenia pozostałych substancji w łącznej objętości.'),
], Q=[
 ('Do 100 g 20% roztworu dodano 100 g wody. Cp wynosi:', ['20%', '*10%', '40%', '15%'], '20 g / 200 g.'),
 ('50 cm³ roztworu 2 mol/dm³ rozcieńczono do 200 cm³. Cm wynosi:', ['1 mol/dm³', '*0,5 mol/dm³', '0,25 mol/dm³', '4 mol/dm³'], 'C₁V₁ = C₂V₂: 2·50 = C·200.'),
 ('Zmieszano 100 g 10% i 300 g 30% roztworu. Cp mieszaniny:', ['20%', '*25%', '40%', '15%'], '(10 + 90)/400 · 100%.'),
])
