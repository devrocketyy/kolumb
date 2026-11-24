# Treści kursu chemii — porcja 12: dogęszczenie tematów średnich (fiszki).
T = {}

T['c-mol'] = dict(F=[
 ('Mol — definicja', 'Ilość substancji zawierająca 6,02·10²³ drobin (stała Avogadra).'),
 ('Masa molowa', 'Masa 1 mola substancji w g/mol; liczbowo równa masie cząsteczkowej w u.'),
 ('Liczba moli z masy', 'n = m / M.'),
 ('Liczba drobin z liczby moli', 'N = n · Nₐ.'),
 ('Liczba atomów w 1 molu H₂SO₄', '7 · Nₐ ≈ 4,21·10²⁴ atomów (2 H + 1 S + 4 O).'),
 ('Liczba jonów w 1 molu Al₂(SO₄)₃', '5 · Nₐ (2 Al³⁺ + 3 SO₄²⁻).'),
 ('Jednostka masy atomowej u', '1/12 masy atomu ¹²C ≈ 1,66·10⁻²⁴ g.'),
 ('Masa atomowa pierwiastka a izotopy', 'Średnia ważona mas izotopów według ich zawartości procentowej.'),
 ('Jak obliczyć skład izotopowy z masy atomowej?', 'Ułożyć równanie średniej ważonej: A = x·A₁ + (1 − x)·A₂.'),
 ('Najczęstszy błąd z molami', 'Mylenie liczby moli cząsteczek z liczbą moli atomów (np. 1 mol O₂ = 2 mole atomów O).'),
])

T['c-metale'] = dict(F=[
 ('Szereg aktywności metali', 'Metale o ujemnym potencjale (K, Ca, Na, Mg, Al, Zn, Fe, Ni, Sn, Pb) wypierają wodór z kwasów; Cu, Ag, Hg, Au — nie.'),
 ('Wypieranie metali z soli', 'Metal aktywniejszy wypiera mniej aktywny: Zn + Cu²⁺ → Zn²⁺ + Cu.'),
 ('Litowce z wodą', '2Na + 2H₂O → 2NaOH + H₂; aktywność rośnie w dół grupy.'),
 ('Pasywacja', 'Tworzenie szczelnej warstwy tlenku: Al, Fe, Cr w stężonym HNO₃ (i Fe, Al w stężonym H₂SO₄ na zimno).'),
 ('Miedź z kwasami utleniającymi', 'Cu + 4HNO₃(stęż.) → Cu(NO₃)₂ + 2NO₂ + 2H₂O; Cu + 2H₂SO₄(stęż.) → CuSO₄ + SO₂ + 2H₂O.'),
 ('Korozja żelaza', 'Utlenianie Fe w obecności wody i tlenu → rdza (Fe₂O₃·nH₂O); przyspieszają ją sole i kwasy.'),
 ('Ochrona katodowa (protektorowa)', 'Połączenie z metalem aktywniejszym (np. Zn, Mg), który koroduje zamiast chronionego.'),
 ('Ocynkowanie a cynowanie', 'Uszkodzona powłoka cynkowa nadal chroni żelazo (Zn aktywniejszy); cynowa — przyspiesza korozję Fe.'),
 ('Barwa płomienia', 'Li — karminowa, Na — żółta, K — fioletowa, Ca — ceglastoczerwona, Sr — karminowa, Ba — zielona, Cu — zielononiebieska.'),
 ('Metale bloku d — cechy', 'Zmienne stopnie utlenienia, barwne jony, tworzenie związków kompleksowych, właściwości katalityczne.'),
 ('Barwy jonów w roztworze', 'Cu²⁺ niebieski, Fe²⁺ bladozielony, Fe³⁺ żółtobrunatny, Cr³⁺ zielony/fioletowy, Mn²⁺ bladoróżowy, Ni²⁺ zielony, Co²⁺ różowy.'),
 ('Glin — właściwości', 'Amfoteryczny, pasywuje się; aluminotermia: 2Al + Fe₂O₃ → Al₂O₃ + 2Fe.'),
])

T['c-ogniwa'] = dict(F=[
 ('Ogniwo galwaniczne — anoda', 'Elektroda ujemna (−), zachodzi utlenianie; półogniwo o niższym potencjale.'),
 ('Ogniwo galwaniczne — katoda', 'Elektroda dodatnia (+), zachodzi redukcja; półogniwo o wyższym potencjale.'),
 ('SEM ogniwa', 'SEM = E(katody) − E(anody) > 0.'),
 ('Zapis ogniwa (konwencja sztokholmska)', '(−) Zn | Zn²⁺ || Cu²⁺ | Cu (+); | — granica faz, || — klucz elektrolityczny.'),
 ('Klucz elektrolityczny — rola', 'Zamyka obwód i wyrównuje ładunki (aniony płyną do anody, kationy do katody).'),
 ('Standardowa elektroda wodorowa', 'Pt | H₂ (1013 hPa) | H⁺ (1 mol/dm³); E° = 0,00 V z definicji.'),
 ('Równanie Nernsta (metal)', 'E = E° + (0,059/n)·log[Mⁿ⁺] w 25°C.'),
 ('Ogniwo stężeniowe', 'Dwa takie same półogniwa o różnych stężeniach; anodą jest to o mniejszym stężeniu.'),
 ('Ogniwo Daniella', 'Zn | ZnSO₄ || CuSO₄ | Cu; SEM ≈ 1,10 V.'),
 ('Akumulator ołowiowy', 'Pb (−), PbO₂ (+), H₂SO₄; przy rozładowaniu obie elektrody → PbSO₄, maleje stężenie kwasu.'),
 ('Ogniwo Leclanchégo (cynkowo-węglowe)', 'Zn (−), MnO₂ z grafitem (+), elektrolit NH₄Cl — popularna bateria.'),
 ('Pułapka: masa elektrod w ogniwie Cu–Zn', 'Masa cynkowej maleje (roztwarza się), masa miedzianej rośnie (osadza się Cu).'),
])

T['c-elektroliza'] = dict(F=[
 ('Elektroliza — katoda', 'Elektroda ujemna (−) — redukcja (odwrotnie niż w ogniwie!).'),
 ('Elektroliza — anoda', 'Elektroda dodatnia (+) — utlenianie.'),
 ('Co wydziela się na katodzie (roztwór wodny)?', 'Metale mniej aktywne niż wodór (Cu, Ag) się osadzają; dla Na⁺, K⁺, Mg²⁺, Al³⁺ — redukuje się woda (H₂).'),
 ('Co wydziela się na anodzie (elektroda obojętna)?', 'Cl⁻, Br⁻, I⁻ → halogen; SO₄²⁻, NO₃⁻, F⁻ — utlenia się woda (O₂).'),
 ('Elektroliza roztworu NaCl', 'Katoda: H₂; anoda: Cl₂; w roztworze powstaje NaOH.'),
 ('Elektroliza stopionego NaCl', 'Katoda: Na; anoda: Cl₂ — przemysłowe otrzymywanie sodu.'),
 ('Elektroliza CuSO₄ z elektrodą miedzianą', 'Anoda roztwarza się (Cu → Cu²⁺), na katodzie osadza się Cu — rafinacja miedzi.'),
 ('Prawo Faradaya', 'm = M·I·t / (n·F); F = 96 500 C/mol elektronów.'),
 ('Ładunek', 'Q = I · t (A · s = C).'),
 ('Otrzymywanie glinu', 'Elektroliza Al₂O₃ rozpuszczonego w stopionym kriolicie.'),
 ('Galwanizacja', 'Pokrywanie przedmiotu (katoda) warstwą metalu z roztworu jego soli.'),
])

T['c-sole'] = dict(F=[
 ('Metody otrzymywania soli (najważniejsze)', 'Kwas + zasada, kwas + metal, kwas + tlenek metalu, zasada + tlenek niemetalu, metal + niemetal, sól + sól (osad).'),
 ('Wodorosole', 'Zawierają H w anionie: NaHCO₃, KHSO₄, NaH₂PO₄ — z kwasów wieloprotonowych.'),
 ('Hydroksosole', 'Zawierają OH⁻: Mg(OH)Cl, (CuOH)₂CO₃ (malachit).'),
 ('Sole uwodnione (hydraty)', 'Zawierają wodę krystalizacyjną: CuSO₄·5H₂O (niebieski), CaSO₄·2H₂O (gips).'),
 ('Odwodnienie CuSO₄·5H₂O', 'Niebieski → biały; biały CuSO₄ służy do wykrywania wody.'),
 ('Gips palony', 'CaSO₄·½H₂O; po zarobieniu wodą twardnieje (przechodzi w CaSO₄·2H₂O).'),
 ('Rozkład termiczny węglanów', 'CaCO₃ → CaO + CO₂ (wapno palone); węglany litowców (poza Li) są trwałe.'),
 ('Rozkład azotanów(V)', 'Litowce: 2NaNO₃ → 2NaNO₂ + O₂; metale ciężkie: 2Cu(NO₃)₂ → 2CuO + 4NO₂ + O₂.'),
 ('Sole amonowe z zasadą', 'NH₄Cl + NaOH → NaCl + NH₃ + H₂O (wykrywanie NH₄⁺ — zapach, wilgotny papierek zasinia).'),
 ('Tablica rozpuszczalności — reguły', 'Rozpuszczalne: wszystkie sole Na⁺, K⁺, NH₄⁺, wszystkie azotany(V) i octany; trudno: większość węglanów, fosforanów, siarczków.'),
 ('Twardość wody a mydło', 'Ca²⁺ + 2RCOO⁻ → (RCOO)₂Ca↓.'),
])

T['c-rownowaga'] = dict(F=[
 ('Stan równowagi dynamicznej', 'Szybkości reakcji w obu kierunkach są równe; stężenia się nie zmieniają (ale reakcje zachodzą).'),
 ('Wyrażenie na stałą równowagi', 'K = [produkty]^współczynniki / [substraty]^współczynniki; nie wpisujemy ciał stałych ani czystych cieczy.'),
 ('Co zmienia wartość K?', 'Tylko temperatura (nie stężenia, ciśnienie ani katalizator).'),
 ('Katalizator a równowaga', 'Przyspiesza ustalenie równowagi, ale nie przesuwa jej i nie zmienia K ani wydajności.'),
 ('Reguła przekory (Le Chateliera)', 'Układ przeciwdziała zmianie warunków: dodanie substratu → przesunięcie w prawo.'),
 ('Wpływ ciśnienia', 'Wzrost ciśnienia przesuwa równowagę w stronę mniejszej liczby moli GAZÓW; brak wpływu, gdy Δn(gazów) = 0.'),
 ('Wpływ temperatury', 'Wzrost T przesuwa równowagę w stronę reakcji endotermicznej.'),
 ('Iloraz reakcji Q', 'Q < K — reakcja biegnie w prawo; Q > K — w lewo; Q = K — równowaga.'),
 ('Tabelka do zadań z K', 'Wiersze: początek / zmiana (zgodnie ze współczynnikami!) / równowaga; stężenia = mole / objętość.'),
 ('Synteza amoniaku — optymalne warunki', 'Wysokie ciśnienie, umiarkowana temperatura (~450°C — kompromis szybkość/wydajność), katalizator Fe, usuwanie NH₃.'),
 ('Duże K (np. 10¹⁰)', 'Równowaga silnie przesunięta w stronę produktów — reakcja praktycznie nieodwracalna.'),
])

T['c-szybkosc'] = dict(F=[
 ('Szybkość reakcji', 'Zmiana stężenia w jednostce czasu: v = Δc/Δt (mol·dm⁻³·s⁻¹).'),
 ('Czynniki zwiększające szybkość', 'Wzrost stężenia, temperatury, rozdrobnienia (powierzchni), katalizator, mieszanie.'),
 ('Równanie kinetyczne', 'v = k·[A]ᵃ·[B]ᵇ; wykładniki wyznacza się DOŚWIADCZALNIE (nie ze współczynników!).'),
 ('Rząd reakcji', 'Suma wykładników w równaniu kinetycznym.'),
 ('Jak wyznaczyć rząd względem A?', 'Porównać doświadczenia, w których zmienia się tylko [A]: podwojenie [A] → v × 2 (rząd 1), × 4 (rząd 2), bez zmian (rząd 0).'),
 ('Jednostka stałej szybkości', 'Rząd 1: s⁻¹; rząd 2: dm³·mol⁻¹·s⁻¹; rząd 3: dm⁶·mol⁻²·s⁻¹.'),
 ('Energia aktywacji', 'Minimalna energia, jaką muszą mieć zderzające się drobiny, aby zaszła reakcja.'),
 ('Katalizator — działanie', 'Obniża energię aktywacji (inna droga reakcji); nie zmienia ΔH.'),
 ('Reguła van ’t Hoffa', 'Wzrost temperatury o 10°C zwiększa szybkość reakcji 2–4 razy.'),
 ('Etap decydujący o szybkości', 'Najwolniejszy etap mechanizmu (o najwyższej energii aktywacji).'),
 ('Inhibitor', 'Substancja spowalniająca reakcję (np. konserwanty, antyoksydanty).'),
])

T['c-energetyka'] = dict(F=[
 ('Reakcja egzotermiczna', 'ΔH < 0 — układ oddaje ciepło do otoczenia (spalanie, zobojętnianie).'),
 ('Reakcja endotermiczna', 'ΔH > 0 — układ pobiera ciepło (rozkład CaCO₃, fotosynteza, rozpuszczanie NH₄NO₃).'),
 ('Prawo Hessa', 'Efekt cieplny zależy tylko od stanu początkowego i końcowego — można sumować równania i ich ΔH.'),
 ('Przekształcanie równań w prawie Hessa', 'Odwrócenie równania → zmiana znaku ΔH; pomnożenie przez liczbę → pomnożenie ΔH.'),
 ('Entalpia tworzenia', 'ΔH powstania 1 mola związku z pierwiastków w stanie standardowym; dla pierwiastków = 0.'),
 ('ΔH reakcji z entalpii tworzenia', 'ΔH = ΣΔHf(produktów) − ΣΔHf(substratów).'),
 ('ΔH z energii wiązań', 'ΔH = ΣE(wiązań zerwanych) − ΣE(wiązań utworzonych).'),
 ('Entalpia spalania', 'ΔH spalenia 1 mola substancji do CO₂ i H₂O (zawsze ujemna).'),
 ('Wykres energetyczny reakcji egzotermicznej', 'Produkty niżej niż substraty; garb = energia aktywacji.'),
 ('Pułapka w zadaniach z ciepłem', 'Q dla podanej masy ≠ ΔH na mol — trzeba przeliczyć na liczbę moli.'),
])

T['c-kwasy-zasady'] = dict(F=[
 ('Kwas wg Brønsteda', 'Donor protonu (H⁺).'),
 ('Zasada wg Brønsteda', 'Akceptor protonu.'),
 ('Sprzężona para kwas–zasada', 'Różnią się jednym protonem: CH₃COOH / CH₃COO⁻; NH₄⁺ / NH₃.'),
 ('Amfiprotyczność', 'Drobina może być kwasem i zasadą: H₂O, HCO₃⁻, HSO₃⁻, H₂PO₄⁻, HPO₄²⁻.'),
 ('Kwas wg Lewisa', 'Akceptor pary elektronowej (np. BF₃, AlCl₃, Fe³⁺).'),
 ('Zasada wg Lewisa', 'Donor pary elektronowej (np. NH₃, H₂O, Cl⁻).'),
 ('Moc kwasu a sprzężona zasada', 'Im mocniejszy kwas, tym słabsza sprzężona z nim zasada.'),
 ('Moc kwasów beztlenowych w grupie 17', 'HF < HCl < HBr < HI (rośnie promień, słabnie wiązanie H–X).'),
 ('Moc kwasów tlenowych chloru', 'HClO < HClO₂ < HClO₃ < HClO₄ (więcej atomów O).'),
 ('Stała dysocjacji Ka', 'Ka = [H⁺][A⁻]/[HA]; większa Ka → mocniejszy kwas; pKa = −log Ka.'),
 ('Ka·Kb dla pary sprzężonej', 'Ka·Kb = Kw = 10⁻¹⁴ (25°C).'),
])

T['c-hydroliza'] = dict(F=[
 ('Hydroliza soli — istota', 'Reakcja jonów słabego kwasu lub słabej zasady z wodą, zmieniająca odczyn.'),
 ('Sól mocnego kwasu i mocnej zasady (NaCl, KNO₃)', 'Nie hydrolizuje — odczyn obojętny.'),
 ('Sól słabego kwasu i mocnej zasady (Na₂CO₃, CH₃COONa)', 'Hydroliza anionowa — odczyn zasadowy.'),
 ('Sól mocnego kwasu i słabej zasady (NH₄Cl, ZnCl₂, AlCl₃)', 'Hydroliza kationowa — odczyn kwasowy.'),
 ('Sól słabego kwasu i słabej zasady (CH₃COONH₄)', 'Hydrolizują oba jony; odczyn zależy od Ka i Kb (dla octanu amonu ≈ obojętny).'),
 ('Hydroliza jonu Al³⁺', '[Al(H₂O)₆]³⁺ + H₂O ⇄ [Al(OH)(H₂O)₅]²⁺ + H₃O⁺.'),
 ('Hydroliza wodorosoli', 'NaHCO₃ — słabo zasadowy; NaHSO₄ — kwasowy (HSO₄⁻ dysocjuje).'),
 ('Kb anionu z Ka kwasu', 'Kb = Kw / Ka; pH roztworu soli: [OH⁻] ≈ √(Kb·c).'),
 ('Zapis hydrolizy — zasada', 'Tylko jon, który hydrolizuje, + H₂O ⇄ … (jon widz pomijamy).'),
 ('Pułapka: Na₂CO₃ — który Ka?', 'Dla CO₃²⁻ używamy Ka2 kwasu węglowego (sprzężona para HCO₃⁻/CO₃²⁻).'),
])

T['c-ph'] = dict(F=[
 ('pH i pOH', 'pH = −log[H⁺]; pOH = −log[OH⁻]; pH + pOH = 14 (25°C).'),
 ('pH mocnego kwasu', '[H⁺] = c·(liczba protonów); np. 0,01 M HCl → pH 2.'),
 ('pH mocnej zasady', '[OH⁻] = c·(liczba OH⁻); 0,01 M NaOH → pOH 2 → pH 12; 0,01 M Ba(OH)₂ → pH 12,3.'),
 ('pH słabego kwasu (warunek c/Ka > 400)', '[H⁺] = √(Ka·c).'),
 ('Zmiana pH przy rozcieńczeniu mocnego kwasu 10 razy', 'pH rośnie o 1.'),
 ('Rozcieńczanie bardzo rozcieńczonego kwasu', 'pH nigdy nie przekroczy 7 — trzeba uwzględnić autodysocjację wody.'),
 ('Iloczyn jonowy wody', 'Kw = [H⁺][OH⁻] = 10⁻¹⁴ w 25°C; rośnie z temperaturą (pH wody obojętnej w 60°C < 7).'),
 ('Wskaźniki: fenoloftaleina', 'Bezbarwna w kwasowym i obojętnym, malinowa w zasadowym (pH > 8,2).'),
 ('Wskaźniki: oranż metylowy', 'Czerwony w kwasowym (pH < 3,1), żółty powyżej 4,4.'),
 ('Wskaźniki: błękit bromotymolowy', 'Żółty — kwasowy, zielony — obojętny, niebieski — zasadowy.'),
 ('Wskaźnik uniwersalny', 'Czerwony (silnie kwasowy) → żółty → zielony (obojętny) → niebieski → fioletowy (silnie zasadowy).'),
])

T['c-alkeny'] = dict(F=[
 ('Wzór ogólny alkenów', 'CₙH₂ₙ; hybrydyzacja węgli przy C=C: sp² (kąt 120°).'),
 ('Wiązanie podwójne C=C', 'Jedno σ + jedno π; brak swobodnej rotacji → izomeria cis–trans.'),
 ('Typowa reakcja alkenów', 'Addycja elektrofilowa (H₂, X₂, HX, H₂O).'),
 ('Reguła Markownikowa', 'Przy addycji HX do niesymetrycznego alkenu H przyłącza się do węgla bogatszego w wodór.'),
 ('Odbarwienie wody bromowej', 'Wykrywanie wiązań wielokrotnych (addycja Br₂).'),
 ('Alken + KMnO₄ (obojętne)', 'Diol (glikol) + brunatny MnO₂ — odbarwienie fioletowego roztworu.'),
 ('Otrzymywanie alkenów', 'Dehydratacja alkoholi (stęż. H₂SO₄, Al₂O₃, T) lub eliminacja HX z halogenoalkanów (KOH/etanol).'),
 ('Reguła Zajcewa', 'W eliminacji powstaje głównie alken bardziej podstawiony (z mniejszą liczbą H przy C=C).'),
 ('Polimeryzacja', 'n CH₂=CH₂ → [–CH₂–CH₂–]ₙ (polietylen); PVC z chlorku winylu, PS ze styrenu.'),
 ('Dieny sprzężone', 'Np. buta-1,3-dien — monomer kauczuku syntetycznego.'),
 ('Alkiny', 'CₙH₂ₙ₋₂; wiązanie potrójne (σ + 2π), węgle sp (180°); etyn z karbidu: CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂.'),
])

T['c-estry'] = dict(F=[
 ('Estryfikacja', 'Kwas + alkohol ⇄ ester + woda (katalizator H⁺, reakcja odwracalna).'),
 ('Skąd pochodzi tlen w wodzie przy estryfikacji?', 'Z grupy –OH kwasu (badania izotopem ¹⁸O w alkoholu).'),
 ('Nazewnictwo estrów', 'Nazwa anionu kwasu + nazwa grupy alkilowej alkoholu: CH₃COOC₂H₅ — octan etylu (etanian etylu).'),
 ('Hydroliza kwasowa estru', 'Odwracalna: ester + H₂O ⇄ kwas + alkohol.'),
 ('Hydroliza zasadowa (zmydlanie)', 'Nieodwracalna: ester + OH⁻ → anion kwasu + alkohol.'),
 ('Estry — właściwości fizyczne', 'Lotne, o owocowych zapachach, słabo rozpuszczalne w wodzie, temperatura wrzenia niższa niż kwasów (brak wiązań wodorowych między cząsteczkami).'),
 ('Estry kwasów nieorganicznych', 'Np. azotan(V) glicerolu (nitrogliceryna), estry kwasu fosforowego w DNA i lecytynach.'),
 ('Woski', 'Estry wyższych kwasów tłuszczowych i wyższych alkoholi monohydroksylowych.'),
 ('Poliestry', 'Polikondensacja kwasu dikarboksylowego i diolu, np. PET (kwas tereftalowy + glikol etylenowy).'),
 ('Ester izomeryczny z kwasem', 'CH₃COOCH₃ i CH₃CH₂COOH — ten sam wzór C₃H₆O₂ (izomeria funkcyjna).'),
])

T['c-wodorotlenki-kwasy'] = dict(F=[
 ('Wodorotlenki rozpuszczalne (zasady)', 'Litowców, Ca(OH)₂ (słabo), Sr(OH)₂, Ba(OH)₂.'),
 ('Otrzymywanie wodorotlenków nierozpuszczalnych', 'Sól + zasada: CuSO₄ + 2NaOH → Cu(OH)₂↓ + Na₂SO₄.'),
 ('Wodorotlenki amfoteryczne', 'Zn(OH)₂, Al(OH)₃, Cr(OH)₃, Pb(OH)₂, Sn(OH)₂, Be(OH)₂.'),
 ('Rozkład termiczny wodorotlenków', 'Cu(OH)₂ → CuO + H₂O (niebieski → czarny); wodorotlenki litowców się nie rozkładają.'),
 ('Kwasy beztlenowe', 'HCl, HBr, HI, HF, H₂S — roztwory wodorków w wodzie.'),
 ('Kwasy tlenowe — otrzymywanie', 'Tlenek kwasowy + woda: SO₃ + H₂O → H₂SO₄.'),
 ('Kwas węglowy i siarkowy(IV)', 'Nietrwałe: rozkładają się na CO₂/SO₂ i wodę.'),
 ('Stężony H₂SO₄ — właściwości', 'Higroskopijny, odwadniający (zwęgla cukier), utleniający (na gorąco z Cu → SO₂).'),
 ('Stężony HNO₃ — właściwości', 'Silny utleniacz; z białkami daje żółte zabarwienie; rozkłada się na świetle (NO₂).'),
 ('Woda królewska', 'HCl + HNO₃ (3 : 1) — roztwarza złoto i platynę.'),
 ('Kwas fosforowy(V)', 'H₃PO₄ — średniej mocy, trójprotonowy, tworzy trzy szeregi soli.'),
])

T['c-niemetale'] = dict(F=[
 ('Chlor — otrzymywanie w laboratorium', 'MnO₂ + 4HCl → MnCl₂ + Cl₂ + 2H₂O (lub KMnO₄ + HCl).'),
 ('Aktywność halogenów', 'F₂ > Cl₂ > Br₂ > I₂ — halogen aktywniejszy wypiera słabszy z soli.'),
 ('Wykrywanie jodu', 'Skrobia — granatowe zabarwienie; w chloroformie fioletowa warstwa.'),
 ('Tlen — otrzymywanie', 'Rozkład H₂O₂ (MnO₂), KMnO₄, KClO₃; przemysłowo — destylacja skroplonego powietrza.'),
 ('Ozon', 'O₃ — odmiana alotropowa tlenu, silny utleniacz, chroni przed UV.'),
 ('Siarka — odmiany', 'Rombowa, jednoskośna, plastyczna; cząsteczki S₈.'),
 ('Amoniak — otrzymywanie laboratoryjne', '2NH₄Cl + Ca(OH)₂ → CaCl₂ + 2NH₃ + 2H₂O (ogrzewanie).'),
 ('Tlenki azotu', 'NO — bezbarwny; NO₂ — brunatny; 2NO₂ ⇄ N₂O₄ (bezbarwny).'),
 ('Węgiel — odmiany alotropowe', 'Diament (sp³), grafit (sp², przewodzi), fulereny, grafen.'),
 ('Krzem', 'Półprzewodnik; SiO₂ — kwarc, piasek; krzemiany — szkło.'),
 ('Gazy szlachetne', 'Konfiguracja s²p⁶ (He: s²), bardzo mało reaktywne; Xe tworzy fluorki.'),
])
