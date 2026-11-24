# Treści kursu chemii — porcja 7: Redoks i elektrochemia (VIII, IX).

T = {}

T['c-stopnie'] = dict(F=[
 ('Wyjaśnij pojęcie: stopień utlenienia', 'Umowny ładunek atomu w związku, obliczony przy założeniu, że wszystkie wiązania są jonowe (elektrony przypisane atomowi bardziej elektroujemnemu).'),
 ('Zasady ustalania stopni utlenienia', 'Pierwiastek wolny — 0; suma w cząsteczce — 0, w jonie — ładunek jonu; F — zawsze −I; metale 1. gr. +I, 2. gr. +II; H zwykle +I (w wodorkach metali −I); O zwykle −II (w nadtlenkach −I, w OF₂ +II).'),
 ('Stopień utlenienia Mn w KMnO₄', '+VII: 1 + x + 4·(−2) = 0.'),
 ('Stopień utlenienia Cr w K₂Cr₂O₇', '+VI: 2·1 + 2x + 7·(−2) = 0.'),
 ('Stopień utlenienia tlenu w H₂O₂', '−I (nadtlenek).'),
 ('Wyjaśnij pojęcie: utlenianie', 'Oddawanie elektronów — wzrost stopnia utlenienia.'),
 ('Wyjaśnij pojęcie: redukcja', 'Przyjmowanie elektronów — spadek stopnia utlenienia.'),
 ('Wyjaśnij pojęcie: utleniacz', 'Substancja, która przyjmuje elektrony (sama się redukuje) i utlenia inną substancję.'),
 ('Wyjaśnij pojęcie: reduktor', 'Substancja, która oddaje elektrony (sama się utlenia) i redukuje inną substancję.'),
 ('Typowe utleniacze', 'KMnO₄, K₂Cr₂O₇, HNO₃, stężony H₂SO₄, Cl₂, O₂, H₂O₂.'),
 ('Typowe reduktory', 'Metale aktywne, H₂, C, CO, H₂S, jony Fe²⁺, I⁻, SO₃²⁻.'),
 ('Wyjaśnij pojęcie: reakcja dysproporcjonowania', 'Reakcja redoks, w której ten sam pierwiastek jednocześnie się utlenia i redukuje, np. Cl₂ + 2NaOH → NaCl + NaClO + H₂O.'),
 ('Wyjaśnij pojęcie: reakcja synproporcjonowania (komproporcjonowania)', 'Reakcja, w której ten sam pierwiastek z dwóch różnych stopni utlenienia przechodzi na jeden pośredni, np. 2H₂S + SO₂ → 3S + 2H₂O.'),
 ('Dlaczego H₂O₂ może być i utleniaczem, i reduktorem?', 'Tlen ma w nim pośredni stopień −I: może zredukować się do −II (H₂O) albo utlenić do 0 (O₂).'),
 ('Typowy błąd: utleniacz a pierwiastek utleniany', 'Mylenie pojęć: utleniacz to substancja, która się REDUKUJE (przyjmuje elektrony), a nie ta, która się utlenia.'),
], Q=[
 ('Stopień utlenienia siarki w H₂SO₄ wynosi:', ['+IV', '*+VI', '−II', '+II'], '2·1 + x + 4·(−2) = 0.'),
 ('W reakcji Zn + Cu²⁺ → Zn²⁺ + Cu reduktorem jest:', ['Cu²⁺', '*Zn', 'Zn²⁺', 'Cu'], 'Cynk oddaje elektrony.'),
 ('Utleniacz w reakcji redoks:', ['oddaje elektrony', '*przyjmuje elektrony i się redukuje', 'zawsze jest metalem', 'zwiększa swój stopień utlenienia'], 'Utleniacz ulega redukcji.'),
 ('Cl₂ + 2NaOH → NaCl + NaClO + H₂O to reakcja:', ['synproporcjonowania', '*dysproporcjonowania', 'zobojętniania', 'wymiany'], 'Chlor z 0 przechodzi na −I i +I.'),
])

T['c-bilans'] = dict(F=[
 ('Bilansowanie redoks metodą bilansu elektronowego — kroki', '1) stopnie utlenienia, 2) wskazać pierwiastki zmieniające stopień, 3) zapisać połówkowe równania z elektronami, 4) wyrównać liczbę elektronów (mnożniki), 5) przenieść współczynniki, 6) dobrać resztę (H, O).'),
 ('Metoda jonowo-elektronowa — kroki', '1) zapisać połówkowe reakcje dla utleniacza i reduktora, 2) zbilansować atomy inne niż O i H, 3) tlen — cząsteczkami H₂O, 4) wodór — jonami H⁺ (kwasowe) lub H₂O/OH⁻ (zasadowe), 5) ładunek — elektronami, 6) wyrównać elektrony i zsumować.'),
 ('Połówkowa redukcja MnO₄⁻ w środowisku kwasowym', 'MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O.'),
 ('Połówkowa redukcja MnO₄⁻ w środowisku obojętnym', 'MnO₄⁻ + 2H₂O + 3e⁻ → MnO₂ + 4OH⁻.'),
 ('Połówkowa redukcja MnO₄⁻ w środowisku zasadowym', 'MnO₄⁻ + e⁻ → MnO₄²⁻.'),
 ('Połówkowa redukcja Cr₂O₇²⁻ w środowisku kwasowym', 'Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O.'),
 ('Połówkowe utlenianie Fe²⁺', 'Fe²⁺ → Fe³⁺ + e⁻.'),
 ('Połówkowe utlenianie H₂O₂', 'H₂O₂ → O₂ + 2H⁺ + 2e⁻.'),
 ('Jak sprawdzić zbilansowane równanie redoks?', 'Liczba atomów każdego pierwiastka i suma ładunków muszą być równe po obu stronach; liczba elektronów oddanych = przyjętych.'),
 ('Typowy błąd w bilansowaniu w środowisku zasadowym', 'Dodawanie jonów H⁺ zamiast OH⁻ i H₂O. W środowisku zasadowym nie może być H⁺ w równaniu.'),
 ('KMnO₄ + Na₂SO₃ w środowisku kwasowym (H₂SO₄) — równanie jonowe', '2MnO₄⁻ + 5SO₃²⁻ + 6H⁺ → 2Mn²⁺ + 5SO₄²⁻ + 3H₂O.'),
], Q=[
 ('Ile elektronów przyjmuje jon MnO₄⁻, redukując się do Mn²⁺?', ['3', '*5', '1', '7'], 'Mn: +VII → +II.'),
 ('W metodzie jonowo-elektronowej w środowisku kwasowym niedobór tlenu uzupełnia się:', ['jonami OH⁻', '*cząsteczkami H₂O', 'jonami H⁺', 'tlenem O₂'], 'Tlen — wodą, wodór — jonami H⁺.'),
 ('Ile elektronów przyjmuje jon Cr₂O₇²⁻ przechodząc w 2Cr³⁺?', ['3', '*6', '2', '12'], 'Każdy Cr: +VI → +III, razem 6 e⁻.'),
 ('W równaniu redoks w środowisku zasadowym NIE może wystąpić:', ['OH⁻', 'H₂O', '*H⁺', 'e⁻ w równaniach połówkowych'], 'Środowisko zasadowe.'),
])

T['c-ogniwa'] = dict(F=[
 ('Wyjaśnij pojęcie: ogniwo galwaniczne', 'Układ dwóch półogniw, w którym energia reakcji redoks zamienia się w energię elektryczną; utlenianie i redukcja zachodzą w różnych miejscach.'),
 ('Anoda i katoda w ogniwie galwanicznym', 'Anoda — elektroda, na której zachodzi utlenianie (biegun ujemny); katoda — redukcja (biegun dodatni).'),
 ('Wyjaśnij pojęcie: potencjał standardowy elektrody', 'Potencjał półogniwa względem standardowej elektrody wodorowej (0 V) w warunkach standardowych (stężenie jonów 1 mol/dm³, 25°C).'),
 ('Szereg napięciowy metali', 'Metale uszeregowane według potencjałów standardowych; im niższy potencjał, tym silniejszy reduktor (łatwiej się utlenia).'),
 ('Jak wskazać anodę i katodę z potencjałów?', 'Półogniwo o niższym potencjale jest anodą (−), o wyższym — katodą (+).'),
 ('Siła elektromotoryczna ogniwa (SEM)', 'SEM = E(katody) − E(anody), czyli potencjał wyższy minus niższy.'),
 ('Schemat ogniwa Daniella', '(−) Zn | Zn²⁺ || Cu²⁺ | Cu (+); SEM° = 0,34 − (−0,76) = 1,10 V.'),
 ('Rola klucza elektrolitycznego (mostka solnego)', 'Zamyka obwód wewnętrzny i wyrównuje ładunki w roztworach przez przepływ jonów, nie dopuszczając do mieszania roztworów.'),
 ('Kierunek przepływu elektronów w ogniwie', 'Przewodnikiem zewnętrznym od anody (−) do katody (+).'),
 ('Potencjał standardowy a potencjał elektrody (uwaga CKE 2026)', 'Potencjał standardowy dotyczy stężenia 1 mol/dm³; przy innych stężeniach potencjał elektrody jest inny (równanie Nernsta) — nie wolno ich utożsamiać.'),
 ('Równanie Nernsta dla elektrody metalicznej (25°C)', 'E = E° + (0,059/n) · log[Mⁿ⁺] — wzrost stężenia jonów metalu podwyższa potencjał elektrody.'),
 ('Ogniwo stężeniowe', 'Dwa takie same półogniwa o różnych stężeniach jonów; katodą jest elektroda w roztworze o większym stężeniu.'),
 ('Akumulator ołowiowy — reakcje rozładowania', 'Anoda: Pb + SO₄²⁻ → PbSO₄ + 2e⁻; katoda: PbO₂ + 4H⁺ + SO₄²⁻ + 2e⁻ → PbSO₄ + 2H₂O.'),
], Q=[
 ('W ogniwie Zn–Cu anodą jest:', ['*cynk', 'miedź', 'klucz elektrolityczny', 'roztwór CuSO₄'], 'Zn ma niższy potencjał (−0,76 V).'),
 ('E°(Ag⁺/Ag) = 0,80 V, E°(Cu²⁺/Cu) = 0,34 V. SEM ogniwa wynosi:', ['1,14 V', '*0,46 V', '0,80 V', '0,34 V'], '0,80 − 0,34.'),
 ('Na katodzie ogniwa galwanicznego zachodzi:', ['utlenianie', '*redukcja', 'rozpuszczanie elektrody', 'wydzielanie tlenu zawsze'], 'Katoda (+) — redukcja.'),
 ('Klucz elektrolityczny służy do:', ['przewodzenia elektronów', '*zamknięcia obwodu przez przepływ jonów', 'mieszania roztworów', 'pomiaru napięcia'], 'Wyrównuje ładunki w roztworach.'),
])

T['c-elektroliza'] = dict(F=[
 ('Wyjaśnij pojęcie: elektroliza', 'Proces redoks wymuszony przepływem prądu stałego przez elektrolit (roztwór lub stop).'),
 ('Katoda i anoda w elektrolizie', 'Katoda (−) — redukcja; anoda (+) — utlenianie. Znaki biegunów odwrotne niż w ogniwie, ale nazwy procesów te same.'),
 ('Elektroliza stopionego NaCl', 'Katoda: Na⁺ + e⁻ → Na; anoda: 2Cl⁻ → Cl₂ + 2e⁻.'),
 ('Elektroliza wodnego roztworu NaCl', 'Katoda: 2H₂O + 2e⁻ → H₂ + 2OH⁻; anoda: 2Cl⁻ → Cl₂ + 2e⁻ — w roztworze powstaje NaOH.'),
 ('Co redukuje się na katodzie w roztworze wodnym?', 'Kationy metali mniej aktywnych (Cu²⁺, Ag⁺) — wydziela się metal; przy kationach metali aktywnych (Na⁺, K⁺, Ca²⁺, Al³⁺) redukuje się woda (H₂).'),
 ('Co utlenia się na anodzie obojętnej w roztworze wodnym?', 'Aniony beztlenowe (Cl⁻, Br⁻, I⁻) — wydziela się fluorowiec; przy anionach tlenowych (SO₄²⁻, NO₃⁻) utlenia się woda (O₂).'),
 ('Elektroliza roztworu CuSO₄ (elektrody obojętne)', 'Katoda: Cu²⁺ + 2e⁻ → Cu; anoda: 2H₂O → O₂ + 4H⁺ + 4e⁻; roztwór się zakwasza.'),
 ('Elektroliza z anodą rozpuszczalną (miedzianą)', 'Anoda Cu utlenia się: Cu → Cu²⁺ + 2e⁻ (rafinacja elektrolityczna miedzi).'),
 ('I prawo Faradaya', 'Masa substancji wydzielonej na elektrodzie jest proporcjonalna do ładunku: m = (M · I · t) / (n · F); F = 96500 C/mol.'),
 ('Wyjaśnij pojęcie: korozja elektrochemiczna', 'Niszczenie metalu w wyniku działania mikroogniw powstających na styku metalu z innym metalem lub zanieczyszczeniami w obecności wilgoci (elektrolitu).'),
 ('Ochrona protektorowa', 'Połączenie chronionego metalu z metalem aktywniejszym (np. cynkiem lub magnezem), który utlenia się zamiast niego.'),
 ('Dlaczego porysowana blacha ocynkowana nie rdzewieje, a pobielana (cynowana) rdzewieje szybciej?', 'Cynk jest aktywniejszy od żelaza i utlenia się zamiast niego; cyna jest mniej aktywna, więc w mikroogniwie anodą staje się żelazo.'),
], Q=[
 ('W elektrolizie wodnego roztworu KNO₃ na katodzie wydziela się:', ['K', '*H₂', 'O₂', 'N₂'], 'K⁺ jest za aktywny — redukuje się woda.'),
 ('Na anodzie obojętnej w elektrolizie roztworu CuCl₂ wydziela się:', ['O₂', 'H₂', '*Cl₂', 'Cu'], 'Anion beztlenowy utlenia się.'),
 ('W elektrolizie katoda jest biegunem:', ['dodatnim', '*ujemnym', 'obojętnym', 'zależnym od elektrolitu'], 'Katoda (−) — redukcja.'),
 ('Ochrona protektorowa stalowego kadłuba statku polega na przymocowaniu:', ['płyt miedzianych', '*płyt cynkowych', 'płyt srebrnych', 'płyt cynowych'], 'Zn jest aktywniejszy od Fe.'),
])
