# Bank zadań autorskich — chemia, część 14.
BANK = {'atom': [
 B('Liczby kwantowe',
   'Tekst autorski. Elektron opisują liczby: n = 3, l = 2, m = −1.',
   T('podaj', 1, 'Podaj symbol podpowłoki.', '3d', '—'),
   T('podaj', 1, 'Podaj maksymalną liczbę elektronów o n = 3.', '18', '2n².')),
], 'wiazania': [
 B('Hybrydyzacja w związkach organicznych',
   'Tekst autorski. Cząsteczka: CH₂=CH–C≡N (akrylonitryl).',
   T('podaj', 2, 'Podaj hybrydyzację każdego atomu węgla (od lewej) i liczbę wiązań σ i π.', 'sp², sp², sp; 6σ, 3π', 'C=C: 1π, C≡N: 2π.')),
], 'stechiometria': [
 B('Odczynnik ograniczający — trzy substraty',
   'Tekst autorski. N₂ + 3H₂ → 2NH₃. Zmieszano 14 g N₂ i 4 g H₂.',
   T('oblicz', 2, 'Oblicz maksymalną masę NH₃.', '17 g', 'n(N₂) = 0,5, n(H₂) = 2 (potrzeba 1,5) → N₂ ogranicza → 1 mol NH₃.')),
 B('Analiza spalania związku z azotem',
   'Tekst autorski. Spalono 0,1 mola aminy CₓHᵧN, otrzymując 8,8 g CO₂ i 6,3 g H₂O.',
   T('oblicz', 2, 'Ustal wzór aminy.', 'C₂H₇N (np. etyloamina)', 'C: 0,2 mol → x = 2; H: 0,7 mol → y = 7.')),
], 'roztwory': [
 B('Mieszanie roztworów o różnych Cm',
   'Tekst autorski. Ile cm³ 2 M i ile 0,5 M roztworu HCl należy zmieszać, aby otrzymać 300 cm³ roztworu 1 M?',
   T('oblicz', 2, 'Oblicz objętości.', '100 cm³ roztworu 2 M i 200 cm³ roztworu 0,5 M', '2x + 0,5(300 − x) = 300 → 1,5x = 150 → x = 100.')),
], 'roztwory-wodne': [
 B('Ka z pH buforu',
   'Tekst autorski. Bufor zawiera 0,1 mol HA i 0,2 mol NaA w 1 dm³; pH = 5,0.',
   T('oblicz', 2, 'Oblicz pKa i Ka kwasu HA.', 'pKa = 4,7; Ka = 2·10⁻⁵', '5,0 = pKa + log 2 → pKa = 4,7.')),
], 'kinetyka': [
 B('Równowaga a ciśnienie i temperatura',
   'Tekst autorski. CO(g) + 2H₂(g) ⇄ CH₃OH(g), ΔH < 0.',
   T('podaj', 2, 'Podaj warunki (ciśnienie, temperatura) sprzyjające dużej wydajności metanolu.', 'Wysokie ciśnienie, niska temperatura (w praktyce kompromis z szybkością + katalizator).', '3 mole gazów → 1 mol; reakcja egzotermiczna.')),
], 'redoks': [
 B('Bilans z nadtlenkiem w zasadzie',
   'Tekst autorski. Mn²⁺ w środowisku zasadowym utlenia się H₂O₂ do MnO₂.',
   T('podaj', 2, 'Napisz równanie jonowe.', 'Mn²⁺ + H₂O₂ + 2OH⁻ → MnO₂ + 2H₂O', 'Mn +II → +IV (2e⁻), O −I → −II (2 × 1e⁻).')),
 B('Ogniwo — kierunek reakcji',
   'Tekst autorski. E°: Cu²⁺/Cu = +0,34 V; Fe³⁺/Fe²⁺ = +0,77 V.',
   T('podaj', 2, 'Napisz równanie reakcji zachodzącej samorzutnie i oblicz SEM.', 'Cu + 2Fe³⁺ → Cu²⁺ + 2Fe²⁺; SEM = 0,43 V', 'Tak trawi się miedź roztworem FeCl₃ (płytki drukowane).')),
], 'nieorganiczne': [
 B('Sole amonowe — rozkład',
   'Tekst autorski. Ogrzewano: NH₄Cl, NH₄NO₂, (NH₄)₂CO₃.',
   T('podaj', 2, 'Napisz równania rozkładu termicznego.', 'NH₄Cl → NH₃ + HCl; NH₄NO₂ → N₂ + 2H₂O; (NH₄)₂CO₃ → 2NH₃ + CO₂ + H₂O', 'NH₄NO₂ — reakcja redoks (synproporcjonowanie azotu).')),
], 'organiczna': [
 B('Substytucja w toluenie — warunki',
   'Tekst autorski. Toluen bromowano: I — w świetle, II — z FeBr₃.',
   T('podaj', 2, 'Podaj nazwy głównych produktów obu reakcji.', 'I: bromek benzylu (bromofenylometan); II: 2- i 4-bromotoluen', 'Mechanizm rodnikowy vs elektrofilowy.')),
 B('Polimeryzacja — fragment łańcucha',
   'Tekst autorski. Fragment polimeru: –CH₂–CH(CN)–CH₂–CH(CN)–.',
   T('podaj', 1, 'Podaj wzór i nazwę monomeru.', 'CH₂=CH–CN — akrylonitryl (propenonitryl)', '—')),
], 'tlenowe': [
 B('Reakcje fenolu',
   'Tekst autorski. Fenol poddano reakcjom z: Na, NaOH, wodą bromową, FeCl₃.',
   T('podaj', 2, 'Napisz równania reakcji z Na i z wodą bromową.', '2C₆H₅OH + 2Na → 2C₆H₅ONa + H₂; C₆H₅OH + 3Br₂ → C₆H₂Br₃OH + 3HBr', '—')),
 B('Glicerol — estry',
   'Tekst autorski. Glicerol zestryfikowano kwasem azotowym(V).',
   T('podaj', 1, 'Napisz równanie (wzory półstrukturalne).', 'C₃H₅(OH)₃ + 3HNO₃ → C₃H₅(ONO₂)₃ + 3H₂O', 'Nitrogliceryna — ester, nie związek nitrowy.')),
], 'azotowe-cukry': [
 B('Hydroliza dipeptydu — masa',
   'Tekst autorski. Zhydrolizowano 14,6 g dipeptydu Gly-Ala (M = 146 g/mol).',
   T('oblicz', 2, 'Oblicz łączną masę otrzymanych aminokwasów.', '16,4 g', '0,1 mol + 0,1 mol H₂O → 7,5 g Gly + 8,9 g Ala.')),
 B('Szereg D i L',
   'Tekst autorski. Aldehyd glicerynowy jest najprostszym cukrem chiralnym.',
   T('podaj', 1, 'Podaj, od czego zależy przynależność cukru do szeregu D lub L.', 'Od położenia –OH przy asymetrycznym atomie C najdalszym od grupy karbonylowej (w projekcji Fischera: prawo — D).', '—'),
   T('podaj', 1, 'Rozstrzygnij, czy D-cukry zawsze są prawoskrętne.', 'Nie — konfiguracja D/L nie określa kierunku skręcania światła (np. D-fruktoza jest lewoskrętna).', '—')),
], 'chemia-zycia': [
 B('Mydła i detergenty — budowa',
   'Tekst autorski. Porównaj stearynian sodu i dodecylosiarczan sodu.',
   T('podaj', 1, 'Podaj, który z nich nie tworzy osadu w twardej wodzie.', 'Dodecylosiarczan sodu (detergent)', 'Sole wapnia siarczanów alkilowych są rozpuszczalne.')),
]}
