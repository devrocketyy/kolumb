# Treści kursu chemii — porcja 5: Reakcje w roztworach wodnych (VI).

T = {}

T['c-kwasy-zasady'] = dict(F=[
 ('Wyjaśnij pojęcie: dysocjacja elektrolityczna', 'Rozpad substancji na jony pod wpływem rozpuszczalnika polarnego (wody).'),
 ('Wyjaśnij pojęcie: elektrolit', 'Substancja, której roztwór wodny (lub stop) przewodzi prąd dzięki obecności jonów (kwasy, zasady, sole).'),
 ('Elektrolity mocne i słabe', 'Mocne dysocjują praktycznie całkowicie (HCl, HNO₃, H₂SO₄, NaOH, KOH, większość soli); słabe — częściowo (CH₃COOH, H₂S, H₂CO₃, NH₃·H₂O).'),
 ('Kwas i zasada według Arrheniusa', 'Kwas — substancja, która w wodzie dysocjuje z wytworzeniem jonów H⁺ (H₃O⁺); zasada — z wytworzeniem jonów OH⁻.'),
 ('Kwas i zasada według Brønsteda–Lowry’ego', 'Kwas — donor protonu (H⁺); zasada — akceptor protonu.'),
 ('Wyjaśnij pojęcie: sprzężona para kwas–zasada', 'Kwas i zasada różniące się o jeden proton, np. NH₄⁺/NH₃, H₂O/OH⁻, HCO₃⁻/CO₃²⁻.'),
 ('Jak wskazać kwas i zasadę Brønsteda w równaniu NH₃ + H₂O ⇄ NH₄⁺ + OH⁻?', 'H₂O oddaje proton — kwas; NH₃ go przyjmuje — zasada. Sprzężone pary: NH₄⁺/NH₃ oraz H₂O/OH⁻.'),
 ('Wyjaśnij pojęcie: amfolit (substancja amfiprotyczna)', 'Drobina, która może być i kwasem, i zasadą Brønsteda, np. H₂O, HCO₃⁻, HSO₄⁻, H₂PO₄⁻.'),
 ('Zależność mocy kwasu i sprzężonej z nim zasady', 'Im mocniejszy kwas, tym słabsza sprzężona z nim zasada (np. HCl — mocny kwas, Cl⁻ — bardzo słaba zasada).'),
 ('Dysocjacja wielostopniowa kwasu wieloprotonowego', 'Zachodzi etapami, a każdy kolejny stopień w mniejszym stopniu, np. H₃PO₄ ⇄ H⁺ + H₂PO₄⁻; H₂PO₄⁻ ⇄ H⁺ + HPO₄²⁻; HPO₄²⁻ ⇄ H⁺ + PO₄³⁻.'),
 ('Zapis jonu oksoniowego', 'H₃O⁺ — proton związany z cząsteczką wody (wiązaniem koordynacyjnym); w uproszczeniu zapisuje się H⁺.'),
 ('Autodysocjacja (autoprotoliza) wody', 'H₂O + H₂O ⇄ H₃O⁺ + OH⁻; iloczyn jonowy wody Kw = [H⁺][OH⁻] = 10⁻¹⁴ (w 25°C).'),
], Q=[
 ('W równaniu HCO₃⁻ + H₂O ⇄ CO₃²⁻ + H₃O⁺ jon HCO₃⁻ jest:', ['zasadą', '*kwasem Brønsteda', 'solą', 'nie bierze udziału w przemianie'], 'Oddaje proton.'),
 ('Sprzężoną zasadą kwasu H₂SO₄ jest:', ['SO₄²⁻', '*HSO₄⁻', 'H₃SO₄⁺', 'H₂O'], 'Różnią się o jeden proton.'),
 ('Który kwas jest słabym elektrolitem?', ['HCl', 'HNO₃', '*CH₃COOH', 'HBr'], 'Dysocjuje częściowo.'),
 ('Amfolitem jest:', ['Cl⁻', '*H₂O', 'Na⁺', 'NH₄⁺'], 'Woda może oddać i przyjąć proton.'),
])

T['c-ph'] = dict(F=[
 ('Definicja pH', 'pH = −log[H⁺] (stężenie jonów wodorowych w mol/dm³).'),
 ('Definicja pOH i związek z pH', 'pOH = −log[OH⁻]; w 25°C pH + pOH = 14.'),
 ('Odczyn roztworu a pH (25°C)', 'pH < 7 — kwasowy, pH = 7 — obojętny, pH > 7 — zasadowy.'),
 ('pH roztworu mocnego kwasu jednoprotonowego', '[H⁺] = Cm kwasu, np. 0,01 mol/dm³ HCl → pH = 2.'),
 ('pH roztworu mocnej zasady', '[OH⁻] = Cm (dla NaOH) lub 2·Cm (dla Ba(OH)₂); pOH = −log[OH⁻]; pH = 14 − pOH.'),
 ('Jak zmienia się pH przy rozcieńczeniu mocnego kwasu 10 razy?', 'Wzrasta o 1 (np. z 2 do 3).'),
 ('Wyjaśnij pojęcie: stała dysocjacji (Ka, Kb)', 'Stała równowagi dysocjacji słabego elektrolitu, np. dla HA ⇄ H⁺ + A⁻: Ka = [H⁺][A⁻]/[HA]. Im większa, tym mocniejszy elektrolit; zależy tylko od temperatury.'),
 ('Wyjaśnij pojęcie: stopień dysocjacji α', 'Stosunek liczby cząsteczek, które zdysocjowały, do całkowitej liczby cząsteczek elektrolitu: α = Czdys / C₀ (często w %).'),
 ('Prawo rozcieńczeń Ostwalda', 'K = α²·C₀ / (1 − α); dla słabych elektrolitów (α < 5%) w przybliżeniu K ≈ α²·C₀.'),
 ('Jak stopień dysocjacji zależy od stężenia?', 'Rośnie przy rozcieńczaniu (maleje C₀), choć stała dysocjacji się nie zmienia.'),
 ('pH słabego kwasu — przybliżenie', '[H⁺] ≈ √(Ka·C₀), gdy C₀/Ka ≥ 400 (α < 5%).'),
 ('Typowy błąd przy pH słabego kwasu', 'Przyjęcie [H⁺] = C₀, jakby kwas był mocny, albo użycie przybliżenia √(Ka·C₀), gdy warunek C₀/Ka ≥ 400 nie jest spełniony.'),
 ('Jak obliczyć [H⁺] z pH?', '[H⁺] = 10⁻ᵖᴴ, np. pH = 3,5 → [H⁺] ≈ 3,16 · 10⁻⁴ mol/dm³.'),
 ('Jak obliczyć pH po zmieszaniu mocnego kwasu z mocną zasadą?', 'Obliczyć mole H⁺ i OH⁻, odjąć (zobojętnienie), nadmiar podzielić przez łączną objętość, policzyć pH lub pOH.'),
 ('Typowy błąd: kwas wieloprotonowy', 'Dla 0,01 M H₂SO₄ (mocny w 1. stopniu) w zadaniach często przyjmuje się [H⁺] = 0,02 mol/dm³ — trzeba czytać, co zakłada polecenie.'),
], Q=[
 ('pH roztworu HCl o stężeniu 0,001 mol/dm³ wynosi:', ['1', '2', '*3', '11'], '[H⁺] = 10⁻³.'),
 ('pH roztworu NaOH o stężeniu 0,01 mol/dm³ wynosi:', ['2', '10', '*12', '14'], 'pOH = 2, pH = 14 − 2.'),
 ('Stopień dysocjacji słabego kwasu przy rozcieńczaniu:', ['maleje', '*rośnie', 'nie zmienia się', 'spada do zera'], 'Prawo rozcieńczeń Ostwalda.'),
 ('Stała dysocjacji zależy od:', ['stężenia', '*temperatury', 'objętości', 'stopnia dysocjacji'], 'Jak każda stała równowagi.'),
 ('Ka kwasu wynosi 10⁻⁵, C₀ = 0,1 mol/dm³. pH wynosi około:', ['1', '*3', '5', '2'], '[H⁺] = √(10⁻⁶) = 10⁻³.'),
])

T['c-hydroliza'] = dict(F=[
 ('Wyjaśnij pojęcie: hydroliza soli', 'Reakcja jonów soli z wodą, w której powstaje słaby elektrolit, a roztwór zmienia odczyn.'),
 ('Odczyn soli mocnego kwasu i mocnej zasady', 'Obojętny — sól nie ulega hydrolizie (np. NaCl, KNO₃, Na₂SO₄).'),
 ('Odczyn soli słabego kwasu i mocnej zasady', 'Zasadowy — hydrolizie ulega anion, np. CH₃COO⁻ + H₂O ⇄ CH₃COOH + OH⁻ (CH₃COONa, Na₂CO₃, K₂S).'),
 ('Odczyn soli mocnego kwasu i słabej zasady', 'Kwasowy — hydrolizie ulega kation, np. NH₄⁺ + H₂O ⇄ NH₃ + H₃O⁺ (NH₄Cl), także sole Al³⁺, Fe³⁺, Cu²⁺, Zn²⁺.'),
 ('Hydroliza kationów metali (np. Al³⁺)', 'Uwodniony kation działa jak kwas: [Al(H₂O)₆]³⁺ + H₂O ⇄ [Al(H₂O)₅OH]²⁺ + H₃O⁺ — roztwór jest kwasowy.'),
 ('Jak zapisać równanie hydrolizy w formie jonowej skróconej?', 'Tylko jon ulegający hydrolizie + H₂O ⇄ słaby elektrolit + H⁺ (lub H₃O⁺) albo OH⁻; jony „widzowie” pomijamy.'),
 ('Typowy błąd w równaniu hydrolizy', 'Zapisanie hydrolizy jonu mocnego elektrolitu (np. Cl⁻ czy Na⁺) albo strzałki jednokierunkowej zamiast ⇄.'),
 ('Wyjaśnij pojęcie: roztwór buforowy', 'Roztwór, który utrzymuje prawie stałe pH po dodaniu niewielkich ilości kwasu lub zasady albo po rozcieńczeniu.'),
 ('Skład roztworu buforowego', 'Słaby kwas i jego sól z mocną zasadą (np. CH₃COOH/CH₃COONa) albo słaba zasada i jej sól z mocnym kwasem (np. NH₃/NH₄Cl).'),
 ('Jak działa bufor octanowy po dodaniu kwasu?', 'Jony CH₃COO⁻ wiążą dodane H⁺: CH₃COO⁻ + H⁺ → CH₃COOH, więc pH prawie się nie zmienia.'),
 ('Jak działa bufor octanowy po dodaniu zasady?', 'Kwas octowy zobojętnia dodane OH⁻: CH₃COOH + OH⁻ → CH₃COO⁻ + H₂O.'),
 ('pH buforu (równanie Hendersona–Hasselbalcha)', 'pH = pKa + log([sól]/[kwas]); gdy stężenia są równe, pH = pKa.'),
 ('Bufory w organizmie człowieka', 'Wodorowęglanowy (H₂CO₃/HCO₃⁻) we krwi utrzymuje pH ok. 7,4; fosforanowy i białczanowy w komórkach.'),
], Q=[
 ('Który roztwór ma odczyn zasadowy?', ['NaCl', 'NH₄Cl', '*K₂CO₃', 'KNO₃'], 'Sól słabego kwasu i mocnej zasady — hydroliza anionu.'),
 ('Odczyn wodnego roztworu NH₄Cl jest:', ['zasadowy', '*kwasowy', 'obojętny', 'zależy od stężenia'], 'Hydroliza kationu NH₄⁺.'),
 ('Roztworem buforowym jest mieszanina:', ['HCl i NaCl', '*CH₃COOH i CH₃COONa', 'NaOH i NaCl', 'HNO₃ i KNO₃'], 'Słaby kwas + jego sól.'),
 ('Poprawne równanie hydrolizy octanu sodu w formie jonowej skróconej:', ['*CH₃COO⁻ + H₂O ⇄ CH₃COOH + OH⁻', 'Na⁺ + H₂O ⇄ NaOH + H⁺', 'CH₃COONa + H₂O → CH₃COOH + NaOH', 'CH₃COO⁻ + H⁺ → CH₃COOH'], 'Hydrolizuje tylko anion słabego kwasu.'),
])

T['c-jonowe'] = dict(F=[
 ('Reakcja zobojętniania — równanie jonowe skrócone', 'H⁺ + OH⁻ → H₂O (dla mocnego kwasu i mocnej zasady).'),
 ('Wyjaśnij pojęcie: reakcja strąceniowa', 'Reakcja jonów w roztworze, w której powstaje trudno rozpuszczalny związek (osad), np. Ag⁺ + Cl⁻ → AgCl↓.'),
 ('Jak przewidzieć, czy wytrąci się osad?', 'Sprawdzić w tabeli rozpuszczalności, czy produkt wymiany jonów jest trudno rozpuszczalny w wodzie.'),
 ('Wyjaśnij pojęcie: iloczyn rozpuszczalności (Ks)', 'Iloczyn stężeń jonów trudno rozpuszczalnej soli w roztworze nasyconym, w potęgach równych współczynnikom, np. Ks(AgCl) = [Ag⁺][Cl⁻].'),
 ('Kiedy wytrąca się osad (z Ks)?', 'Gdy iloczyn stężeń jonów w roztworze przekroczy wartość Ks.'),
 ('Wyrażenie na Ks dla Ca₃(PO₄)₂', 'Ks = [Ca²⁺]³[PO₄³⁻]².'),
 ('Wyjaśnij pojęcie: efekt wspólnego jonu', 'Dodanie jonu wspólnego z trudno rozpuszczalną solą zmniejsza jej rozpuszczalność (przesuwa równowagę w stronę osadu).'),
 ('Reakcja kwasu z solą słabszego kwasu', 'Mocniejszy kwas wypiera słabszy z jego soli, np. CaCO₃ + 2H⁺ → Ca²⁺ + CO₂↑ + H₂O.'),
 ('Typowe gazy powstające w reakcjach jonowych', 'CO₂ (węglany + kwas), H₂S (siarczki + kwas), SO₂ (siarczany(IV) + kwas), NH₃ (sole amonowe + zasada, ogrzewanie).'),
 ('Jak zapisać równanie jonowe skrócone krok po kroku?', '1) równanie cząsteczkowe, 2) rozpisać na jony mocne elektrolity rozpuszczalne, 3) skreślić jony, które się nie zmieniają, 4) sprawdzić atomy i ładunki.'),
 ('Jakich substancji nie rozpisuje się na jony?', 'Osadów, gazów, wody, tlenków, słabych elektrolitów (słabe kwasy i zasady), substancji niezdysocjowanych.'),
 ('Wyjaśnij pojęcie: miareczkowanie alkacymetryczne', 'Oznaczanie stężenia kwasu (zasady) przez stopniowe dodawanie zasady (kwasu) o znanym stężeniu do punktu równoważnikowego, wskazanego np. zmianą barwy wskaźnika.'),
], Q=[
 ('Które jony utworzą osad w roztworze?', ['Na⁺ i Cl⁻', '*Ba²⁺ i SO₄²⁻', 'K⁺ i NO₃⁻', 'NH₄⁺ i Cl⁻'], 'BaSO₄ jest trudno rozpuszczalny.'),
 ('Wyrażenie na iloczyn rozpuszczalności PbI₂ to:', ['[Pb²⁺][I⁻]', '*[Pb²⁺][I⁻]²', '[Pb²⁺]²[I⁻]', '2[Pb²⁺][I⁻]'], 'Wykładniki = współczynniki.'),
 ('Równanie jonowe skrócone reakcji Na₂CO₃ z HCl:', ['*CO₃²⁻ + 2H⁺ → CO₂ + H₂O', 'Na⁺ + Cl⁻ → NaCl', 'Na₂CO₃ + 2H⁺ → 2Na⁺ + H₂CO₃', 'H⁺ + OH⁻ → H₂O'], 'Kwas węglowy rozkłada się na CO₂ i wodę.'),
 ('Dodanie NaCl do nasyconego roztworu AgCl spowoduje:', ['rozpuszczenie osadu', '*wytrącenie dodatkowej ilości AgCl', 'brak zmian', 'powstanie gazu'], 'Efekt wspólnego jonu Cl⁻.'),
])
