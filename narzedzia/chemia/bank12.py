# Bank zadań autorskich — chemia, część 12.
BANK = {'atom': [
 B('Konfiguracja a położenie w układzie',
   'Tekst autorski. Atom pierwiastka X ma konfigurację [Ar] 4s² 3d¹⁰ 4p³.',
   T('podaj', 2, 'Podaj symbol, numer grupy, okresu i blok pierwiastka X.', 'As; grupa 15; okres 4; blok p', '—'),
   T('podaj', 1, 'Podaj wzór wodorku i najwyższego tlenku X.', 'AsH₃; As₂O₅ (As₄O₁₀)', 'Grupa 15: −III i +V.')),
], 'wiazania': [
 B('Temperatury wrzenia wodorków',
   'Tekst autorski. Temperatury wrzenia: H₂O 100°C, H₂S −60°C, H₂Se −41°C, H₂Te −2°C.',
   T('wyjasnij', 2, 'Wyjaśnij anomalię wody i trend dla H₂S → H₂Te.', 'Woda tworzy wiązania wodorowe (silnie elektroujemny O). Od H₂S do H₂Te rosną masa i rozmiar cząsteczek — silniejsze oddziaływania van der Waalsa.', '—')),
], 'stechiometria': [
 B('Mieszanina gazów — średnia masa molowa',
   'Tekst autorski. Mieszanina N₂ i O₂ ma średnią masę molową 29 g/mol (powietrze uproszczone).',
   T('oblicz', 2, 'Oblicz ułamek molowy tlenu.', '0,25', 'MODEL: średnia ważona mas molowych. RACHUNEK: 28(1 − y) + 32y = 29 → 4y = 1 → y = 0,25. SPRAWDZENIE: 0,75 · 28 + 0,25 · 32 = 21 + 8 = 29.')),
 B('Spalanie siarki w węglu',
   'Tekst autorski. Spalono 1 t węgla zawierającego 1,6% siarki.',
   T('oblicz', 2, 'Oblicz masę powstałego SO₂ (kg).', '32 kg', 'S = 16 kg = 500 mol → SO₂ 500 · 64 g = 32 kg.')),
], 'roztwory': [
 B('Przygotowanie roztworu z kwasu stężonego',
   'Tekst autorski. Stężony H₂SO₄ ma stężenie 96% i gęstość 1,84 g/cm³.',
   T('oblicz', 2, 'Oblicz objętość stężonego kwasu potrzebną do przygotowania 1 dm³ roztworu 1 M.', 'ok. 55,5 cm³', 'm(H₂SO₄) = 98 g → m(roztworu) = 102,1 g → V = 55,5 cm³.')),
], 'roztwory-wodne': [
 B('Reakcja zobojętniania — objętość',
   'Tekst autorski. Ile cm³ 0,25 M H₂SO₄ zobojętni 50 cm³ 0,4 M KOH?',
   T('oblicz', 1, 'Oblicz objętość kwasu.', '40 cm³', 'n(KOH) = 0,02 → n(H₂SO₄) = 0,01 → V = 0,04 dm³.')),
 B('Kolejność pH soli',
   'Tekst autorski. Roztwory 0,1 M: NaCl, NH₄Cl, Na₂CO₃, NaHSO₄.',
   T('podaj', 1, 'Uszereguj według rosnącego pH.', 'NaHSO₄ < NH₄Cl < NaCl < Na₂CO₃', 'HSO₄⁻ jest dość mocnym kwasem.')),
], 'kinetyka': [
 B('Stała równowagi — kierunek reakcji',
   'Tekst autorski. Dla A + B ⇄ C, K = 10. W pewnej chwili [A] = [B] = 0,5, [C] = 1,0 mol·dm⁻³.',
   T('rozstrzygnij', 2, 'Rozstrzygnij, w którą stronę biegnie reakcja. Uzasadnij obliczeniem.', 'W prawo — Q = 1,0/(0,5·0,5) = 4 < K = 10.', 'Porównanie Q i K.')),
 B('Wpływ katalizatora na wykres',
   'Tekst autorski. Reakcję prowadzono z katalizatorem i bez.',
   T('podaj', 2, 'Podaj, które wielkości się zmienią: Ea, ΔH, K, szybkość.', 'Zmieni się Ea (zmaleje) i szybkość (wzrośnie); ΔH i K — bez zmian.', '—')),
], 'redoks': [
 B('Utlenianie szczawianu',
   'Tekst autorski. Jony C₂O₄²⁻ utlenia się zakwaszonym KMnO₄ do CO₂.',
   T('podaj', 2, 'Napisz sumaryczne równanie jonowe.', '2MnO₄⁻ + 5C₂O₄²⁻ + 16H⁺ → 2Mn²⁺ + 10CO₂ + 8H₂O', 'Mn: 5e⁻ × 2; C₂O₄²⁻: 2e⁻ × 5.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego reakcja na początku jest wolna, a potem przyspiesza.', 'Powstające jony Mn²⁺ katalizują reakcję (autokataliza).', '—')),
 B('Elektroliza — porównanie',
   'Tekst autorski. Przez dwa połączone szeregowo elektrolizery z roztworami CuSO₄ i AgNO₃ przepłynął ten sam ładunek; wydzieliło się 2,16 g Ag.',
   T('oblicz', 2, 'Oblicz masę wydzielonej miedzi.', '0,635 g', 'n(e⁻) = 0,02 → n(Cu) = 0,01 → 0,635 g.')),
], 'nieorganiczne': [
 B('Właściwości kwasu siarkowego',
   'Tekst autorski. Na cukier wlano stężony H₂SO₄ — powstała czarna, pęczniejąca masa.',
   T('podaj', 1, 'Podaj, jaką właściwość kwasu ilustruje doświadczenie.', 'Właściwości odwadniające (higroskopijne)', 'C₁₂H₂₂O₁₁ → 12C + 11H₂O.'),
   T('podaj', 1, 'Napisz równanie reakcji miedzi ze stężonym gorącym H₂SO₄.', 'Cu + 2H₂SO₄ → CuSO₄ + SO₂ + 2H₂O', 'Właściwości utleniające.')),
], 'organiczna': [
 B('Nazewnictwo i izomeria halogenopochodnych',
   'Tekst autorski. Wzór C₃H₆Cl₂.',
   T('podaj', 2, 'Podaj nazwy wszystkich izomerów konstytucyjnych.', '1,1-dichloropropan; 1,2-dichloropropan; 1,3-dichloropropan; 2,2-dichloropropan', '4 izomery.'),
   T('podaj', 1, 'Wskaż izomer chiralny.', '1,2-dichloropropan', 'C2 ma cztery różne podstawniki.')),
], 'tlenowe': [
 B('Estry w perfumerii',
   'Tekst autorski. Salicylan metylu (olejek gaultheriowy) to ester kwasu salicylowego i metanolu.',
   T('podaj', 1, 'Napisz wzór salicylanu metylu.', 'HO–C₆H₄–COOCH₃ (o-)', '—'),
   T('podaj', 1, 'Podaj odczynnik, którym wykażesz w nim grupę fenolową.', 'FeCl₃ — fioletowe zabarwienie', '—')),
], 'azotowe-cukry': [
 B('Punkt izoelektryczny i rozpuszczalność',
   'Tekst autorski. Białka najsłabiej rozpuszczają się w roztworze o pH równym ich punktowi izoelektrycznemu.',
   T('wyjasnij', 1, 'Wyjaśnij to zjawisko.', 'Przy pI cząsteczki mają ładunek wypadkowy 0 — nie odpychają się elektrostatycznie i łatwiej się agregują.', '—')),
 B('Nukleotydy — cukry',
   'Tekst autorski. DNA zawiera 2-deoksyrybozę, RNA — rybozę.',
   T('podaj', 1, 'Podaj, czym różnią się te cukry.', 'Deoksyryboza nie ma grupy –OH przy C2.', '—')),
], 'chemia-zycia': [
 B('Polimery biodegradowalne',
   'Tekst autorski. PLA otrzymuje się z kwasu mlekowego.',
   T('podaj', 1, 'Podaj typ polimeryzacji i produkt uboczny.', 'Polikondensacja; woda', '—'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego PLA ulega biodegradacji, a polietylen nie.', 'PLA zawiera wiązania estrowe, które ulegają hydrolizie (także enzymatycznej); PE ma tylko wiązania C–C i C–H.', '—')),
]}
