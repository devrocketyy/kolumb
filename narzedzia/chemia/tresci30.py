# Treści kursu chemii — porcja 30: pytania ABCD — obliczenia i rozumowanie (roztwory, kinetyka, redoks, nieorganiczna).
T = {}

T['c-stezenia'] = dict(Q=[
 ('Ile gramów NaOH potrzeba do sporządzenia 500 cm³ roztworu o stężeniu 0,2 mol/dm³?', ['*4 g', '8 g', '2 g', '40 g'], '0,1 mola · 40 g/mol.'),
 ('Stężenie jonów Cl⁻ w roztworze CaCl₂ o stężeniu 0,15 mol/dm³ wynosi:', ['*0,30 mol/dm³', '0,15 mol/dm³', '0,45 mol/dm³', '0,075 mol/dm³'], 'Każdy mol CaCl₂ daje 2 mole Cl⁻.'),
 ('Ile cm³ roztworu H₂SO₄ o stężeniu 2 mol/dm³ potrzeba do przygotowania 200 cm³ roztworu 0,5 mol/dm³?', ['*50 cm³', '100 cm³', '25 cm³', '80 cm³'], 'c₁V₁ = c₂V₂ → V₁ = 0,5 · 200 / 2.'),
 ('Masa 250 cm³ roztworu o gęstości 1,2 g/cm³ to:', ['*300 g', '208 g', '250 g', '350 g'], 'm = d · V.'),
])

T['c-rozpuszczalnosc'] = dict(Q=[
 ('Ile gramów soli o rozpuszczalności 25 g/100 g wody znajduje się w 250 g roztworu nasyconego?', ['*50 g', '62,5 g', '25 g', '40 g'], '25 g soli na 125 g roztworu → 250 g zawiera 50 g.'),
 ('Kₛ(CaF₂) = [Ca²⁺][F⁻]ⁿ, gdzie n wynosi:', ['*2', '1', '3', '½'], 'CaF₂ ⇄ Ca²⁺ + 2F⁻.'),
 ('Rozpuszczalność AgCl w roztworze NaCl w porównaniu z czystą wodą jest:', ['*mniejsza', 'większa', 'taka sama', 'zerowa'], 'Efekt wspólnego jonu.'),
])

T['c-mieszanie'] = dict(Q=[
 ('W jakim stosunku masowym zmieszać roztwór 40% z wodą, aby otrzymać roztwór 10%?', ['*1 : 3', '1 : 4', '3 : 1', '1 : 2'], 'Reguła krzyżowa: (10 − 0) : (40 − 10).'),
 ('Zmieszano 200 cm³ HCl 0,1 mol/dm³ i 300 cm³ HCl 0,6 mol/dm³. Stężenie wynosi:', ['*0,4 mol/dm³', '0,35 mol/dm³', '0,7 mol/dm³', '0,3 mol/dm³'], '(0,02 + 0,18) / 0,5.'),
 ('Do 100 g roztworu 20% dodano 25 g soli. Stężenie wynosi:', ['*36%', '45%', '25%', '40%'], '45 g / 125 g.'),
])

T['c-ph'] = dict(Q=[
 ('pH roztworu Ba(OH)₂ o stężeniu 0,005 mol/dm³ wynosi:', ['*12', '11,7', '2', '13'], '[OH⁻] = 0,01.'),
 ('Zmieszano równe objętości HCl i NaOH o stężeniach 0,1 mol/dm³. pH wynosi:', ['*7', '1', '13', '3,5'], 'Całkowite zobojętnienie.'),
 ('Iloczyn jonowy wody w 25°C wynosi:', ['*10⁻¹⁴', '10⁻⁷', '7', '14'], 'Kw = [H⁺][OH⁻].'),
 ('Roztwór, w którym [OH⁻] = 10⁻⁴ mol/dm³, ma pH:', ['*10', '4', '−4', '14'], 'pOH = 4.'),
 ('Stopień dysocjacji kwasu HA w roztworze 0,1 mol/dm³ wynosi 1%. Stężenie H⁺ to:', ['*10⁻³ mol/dm³', '10⁻¹ mol/dm³', '10⁻² mol/dm³', '10⁻⁴ mol/dm³'], 'α · c = 0,01 · 0,1.'),
 ('Ka słabego kwasu HA (c = 0,01 mol/dm³, pH = 4) wynosi ok.:', ['*10⁻⁶', '10⁻⁴', '10⁻⁸', '10⁻²'], '[H⁺]² / c = 10⁻⁸ / 10⁻².'),
])

T['c-hydroliza'] = dict(Q=[
 ('Spośród roztworów o tym samym stężeniu najwyższe pH ma:', ['*Na₂CO₃', 'NaHCO₃', 'NaCl', 'NH₄Cl'], 'CO₃²⁻ jest mocniejszą zasadą niż HCO₃⁻.'),
 ('Wodny roztwór CH₃COONH₄ ma odczyn zbliżony do obojętnego, ponieważ:', ['*Ka i Kb jonów są podobne', 'sól nie hydrolizuje', 'jest to sól mocnego kwasu', 'octan nie dysocjuje'], 'Hydrolizują oba jony w podobnym stopniu.'),
 ('Hydroliza Al³⁺ w wodzie powoduje, że roztwór AlCl₃ ma odczyn:', ['*kwasowy', 'zasadowy', 'obojętny', 'zależny od ilości soli'], '[Al(H₂O)₆]³⁺ oddaje proton.'),
])

T['c-jonowe'] = dict(Q=[
 ('Po zmieszaniu roztworów Pb(NO₃)₂ i KI powstaje:', ['*żółty osad PbI₂', 'biały osad KNO₃', 'czarny osad Pb', 'brak zmian'], 'Pb²⁺ + 2I⁻ → PbI₂↓.'),
 ('Jonem obojętnym w reakcji BaCl₂ + Na₂SO₄ jest:', ['*Na⁺', 'Ba²⁺', 'SO₄²⁻', 'żaden'], 'Na⁺ i Cl⁻ nie biorą udziału w strąceniu.'),
 ('Czarny osad z roztworu soli miedzi(II) powstaje po dodaniu:', ['*Na₂S', 'NaOH', 'NaCl', 'Na₂SO₄'], 'CuS.'),
 ('Odczynnikiem na jony SO₄²⁻ jest roztwór:', ['*BaCl₂', 'AgNO₃', 'NaOH', 'KMnO₄'], 'Biały osad BaSO₄ nierozpuszczalny w kwasach.'),
])

T['c-szybkosc'] = dict(Q=[
 ('Podwyższenie temperatury o 20 K przy współczynniku temperaturowym 3 zwiększa szybkość:', ['*9 razy', '6 razy', '3 razy', '20 razy'], '3² = 9.'),
 ('Szybkość reakcji A + B → C nie zależy od [B]. Rząd względem B wynosi:', ['*0', '1', '2', '−1'], 'Wykładnik zero.'),
 ('Reakcja 2NO + O₂ → 2NO₂ ma v = k[NO]²[O₂]. Trzykrotny wzrost [NO] zwiększa szybkość:', ['*9 razy', '3 razy', '6 razy', '27 razy'], '3².'),
 ('Szybkość reakcji cynku z HCl nie zależy od:', ['*objętości kwasu (przy stałym stężeniu)', 'stężenia użytego kwasu solnego', 'temperatury mieszaniny reakcyjnej', 'stopnia rozdrobnienia cynku'], 'Liczy się stężenie, nie objętość.'),
])

T['c-rownowaga'] = dict(Q=[
 ('Dla 2SO₂ + O₂ ⇄ 2SO₃ wyrażenie na K to:', ['*[SO₃]² / ([SO₂]²[O₂])', '[SO₃] / ([SO₂][O₂])', '[SO₂]²[O₂] / [SO₃]²', '2[SO₃] / (2[SO₂][O₂])'], 'Potęgi = współczynniki.'),
 ('Jeśli Q > K, układ:', ['*reaguje w lewo', 'reaguje w prawo', 'jest w równowadze', 'nie reaguje'], 'Za dużo produktów.'),
 ('Dla A ⇄ B: K = 4. Stężenie równowagowe B przy [A] = 0,5 mol/dm³ wynosi:', ['*2 mol/dm³', '0,125 mol/dm³', '8 mol/dm³', '4,5 mol/dm³'], '[B] = K · [A].'),
 ('Usunięcie CO₂ z układu CaCO₃ ⇄ CaO + CO₂ powoduje:', ['*rozkład większej ilości CaCO₃', 'powstawanie CaCO₃', 'brak zmian', 'zmianę wartości K'], 'Reguła przekory.'),
])

T['c-energetyka'] = dict(Q=[
 ('ΔHₜ(CO₂) = −394 kJ/mol, ΔHₜ(H₂O) = −286 kJ/mol, ΔHₜ(CH₄) = −75 kJ/mol. ΔH spalania CH₄ to:', ['*−891 kJ/mol', '−605 kJ/mol', '−755 kJ/mol', '+891 kJ/mol'], '(−394 − 572) − (−75).'),
 ('Energia wiązań: H–H 436, Cl–Cl 243, H–Cl 432 kJ/mol. ΔH reakcji H₂ + Cl₂ → 2HCl to:', ['*−185 kJ', '+185 kJ', '−247 kJ', '+247 kJ'], '(436 + 243) − 2 · 432.'),
])

T['c-bilans'] = dict(Q=[
 ('Współczynnik przy H⁺ w równaniu Cr₂O₇²⁻ + Fe²⁺ + H⁺ → Cr³⁺ + Fe³⁺ + H₂O to:', ['*14', '7', '8', '6'], 'Cr₂O₇²⁻ + 6Fe²⁺ + 14H⁺ → 2Cr³⁺ + 6Fe³⁺ + 7H₂O.'),
 ('Liczba elektronów oddana przez 1 mol (COOH)₂ przy utlenianiu do CO₂:', ['*2', '1', '4', '8'], 'C z +III na +IV, dwa atomy C.'),
 ('W reakcji 3Cu + 8HNO₃ → … stosunek moli reduktora do utleniacza (azotu, który się redukuje) to:', ['*3 : 2', '3 : 8', '1 : 1', '8 : 3'], 'Tylko 2 z 8 cząsteczek HNO₃ redukują się do NO.'),
])

T['c-stopnie'] = dict(Q=[
 ('Stopień utlenienia siarki w Na₂S₂O₃ (średni):', ['*+II', '+IV', '+VI', '−II'], '2 + 2x − 6 = 0.'),
 ('Stopień utlenienia azotu w NH₄⁺:', ['*−III', '+III', '+V', '0'], 'x + 4 = +1.'),
 ('W reakcji 2H₂O₂ → 2H₂O + O₂ nadtlenek wodoru jest:', ['*utleniaczem i reduktorem jednocześnie', 'wyłącznie utleniaczem w tej reakcji', 'wyłącznie reduktorem w tej reakcji', 'katalizatorem rozkładu wody'], 'Dysproporcjonowanie tlenu z −I.'),
])

T['c-ogniwa'] = dict(Q=[
 ('W ogniwie Mg | Mg²⁺ || Cu²⁺ | Cu masa elektrody magnezowej:', ['*maleje', 'rośnie', 'nie zmienia się', 'najpierw rośnie, potem maleje'], 'Magnez utlenia się i przechodzi do roztworu.'),
 ('Które metale wyprą srebro z roztworu AgNO₃?', ['*Cu i Zn', 'tylko Au', 'Pt i Au', 'żaden metal'], 'Oba mają niższy potencjał niż Ag.'),
 ('Klucz elektrolityczny zawiera zwykle:', ['*KNO₃ lub KCl', 'stężony H₂SO₄', 'czystą wodę', 'rtęć'], 'Jony, które nie reagują z elektrodami.'),
])

T['c-sole'] = dict(Q=[
 ('Sól powstaje w reakcji metalu z niemetalem, np.:', ['*2Na + Cl₂ → 2NaCl', 'CaO + H₂O → Ca(OH)₂', 'SO₃ + H₂O → H₂SO₄', 'H₂ + Cl₂ → 2HCl'], 'Synteza z pierwiastków.'),
 ('Ałun glinowo-potasowy to przykład soli:', ['*podwójnej', 'kwaśnej', 'zasadowej', 'kompleksowej'], 'KAl(SO₄)₂·12H₂O.'),
])

T['c-metale'] = dict(Q=[
 ('Glin roztwarza się w NaOH(aq), tworząc:', ['*Na[Al(OH)₄] i H₂', 'Al(OH)₃ i O₂', 'Al₂O₃ i Na', 'NaAlO₂ i H₂O₂'], '2Al + 2NaOH + 6H₂O → 2Na[Al(OH)₄] + 3H₂.'),
 ('Żelazo rdzewieje szybciej w obecności:', ['*wody i soli', 'suchego powietrza', 'oleju', 'azotu'], 'Elektrolit przyspiesza korozję elektrochemiczną.'),
 ('Najsilniejszym reduktorem spośród metali jest:', ['*lit', 'miedź', 'srebro', 'żelazo'], 'Najniższy potencjał standardowy.'),
])

T['c-niemetale'] = dict(Q=[
 ('Chlor w laboratorium otrzymuje się z:', ['*KMnO₄ i stężonego HCl', 'NaCl i wody', 'HCl i Cu', 'KCl i O₂'], 'Mangan(VII) utlenia chlorki.'),
 ('Najsilniejszym utleniaczem wśród fluorowców jest:', ['*fluor', 'chlor', 'brom', 'jod'], 'Największa elektroujemność.'),
 ('Siarkowodór z roztworem Pb(NO₃)₂ daje:', ['*czarny osad PbS', 'biały osad PbSO₄', 'żółty osad S', 'brak zmian'], 'Wykrywanie H₂S.'),
])

T['c-wiazania'] = dict(Q=[
 ('Wiązanie metaliczne występuje w:', ['*miedzi', 'diamencie', 'NaCl', 'I₂'], 'Kationy w gazie elektronowym.'),
 ('Wiązanie σ powstaje przez:', ['*czołowe nakładanie orbitali', 'boczne nakładanie orbitali p', 'przeniesienie elektronu', 'oddziaływanie dipoli'], 'Wiązanie π powstaje przez nakładanie boczne.'),
])

T['c-geometria'] = dict(Q=[
 ('Polarna cząsteczka to:', ['*SO₂', 'CO₂', 'BF₃', 'CH₄'], 'Cząsteczka kątowa.'),
 ('Hybrydyzacja azotu w NO₃⁻:', ['*sp²', 'sp³', 'sp', 'brak'], 'Jon płaski trójkątny.'),
])
