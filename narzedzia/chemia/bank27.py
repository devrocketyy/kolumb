# Bank zadań autorskich — chemia, część 27: wiązki CKE 2023+ — roztwory wodne, kinetyka, organiczna, nieorganiczne, redoks.
BANK = {'roztwory-wodne': [
 B('Moc kwasów z wartości Ka',
   'Tekst autorski. Ka (25°C): HF 6,3 · 10⁻⁴; HCOOH 1,8 · 10⁻⁴; CH₃COOH 1,8 · 10⁻⁵; HCN 6,2 · 10⁻¹⁰.',
   T('podaj', 1, 'Uszereguj kwasy według rosnącej mocy.', 'HCN < CH₃COOH < HCOOH < HF', '—'),
   T('podaj', 1, 'Wskaż zasadę sprzężoną, która jest najmocniejsza.', 'CN⁻', 'Najsłabszy kwas → najmocniejsza zasada sprzężona.'),
   T('oblicz', 1, 'Oblicz pH roztworu HCOOH o stężeniu 0,18 mol/dm³ (α < 5%).', 'pH ≈ 2,24', '[H⁺] = √(1,8 · 10⁻⁴ · 0,18) = √(3,24 · 10⁻⁵) = 5,7 · 10⁻³.')),
 B('Hydroliza a pH soli amonowej',
   'Tekst autorski. Roztwór NH₄Cl ma stężenie 0,1 mol/dm³. Kb(NH₃) = 1,8 · 10⁻⁵.',
   T('podaj', 1, 'Napisz równanie hydrolizy.', 'NH₄⁺ + H₂O ⇄ NH₃ + H₃O⁺', '—'),
   T('oblicz', 2, 'Oblicz pH roztworu.', 'pH ≈ 5,1', 'Ka = Kw/Kb = 5,6 · 10⁻¹⁰; [H⁺] = √(5,6 · 10⁻¹¹) = 7,5 · 10⁻⁶.')),
], 'kinetyka': [
 B('Wpływ katalizatora na równowagę',
   'Tekst autorski. Dwie identyczne mieszaniny N₂ i H₂ ogrzano do tej samej temperatury: jedną z katalizatorem żelazowym, drugą bez.',
   T('podaj', 2, 'Porównaj czas osiągnięcia równowagi i skład mieszanin w stanie równowagi.', 'Z katalizatorem równowaga ustala się szybciej; skład w równowadze jest taki sam.', 'Katalizator nie zmienia K.'),
   T('podaj', 1, 'Narysuj (opisz) różnicę na wykresie energetycznym.', 'Z katalizatorem niższa bariera (Eₐ), poziomy substratów i produktów bez zmian.', '—')),
], 'organiczna': [
 B('Węglowodory C₅H₁₀',
   'Tekst autorski. Związki A, B i C mają wzór C₅H₁₀. A odbarwia wodę bromową i ma izomery cis–trans. B odbarwia wodę bromową, nie ma izomerów cis–trans i ma łańcuch nierozgałęziony. C nie odbarwia wody bromowej.',
   T('podaj', 2, 'Podaj wzory i nazwy A, B i C.', 'A: pent-2-en; B: pent-1-en; C: cyklopentan (lub metylocyklobutan)', 'C₅H₁₀ to alkeny lub cykloalkany.'),
   T('podaj', 1, 'Napisz równanie reakcji B z HCl i podaj nazwę produktu głównego.', 'CH₂=CHCH₂CH₂CH₃ + HCl → CH₃CHClCH₂CH₂CH₃; 2-chloropentan', 'Reguła Markownikowa.')),
 B('Polimer kondensacyjny',
   'Tekst autorski. PET otrzymuje się z kwasu tereftalowego (kwasu benzeno-1,4-dikarboksylowego) i glikolu etylenowego.',
   T('podaj', 1, 'Podaj nazwę grupy łączącej mery w PET.', 'estrowa', 'Poliester.'),
   T('podaj', 1, 'Napisz, jaki produkt uboczny powstaje w każdym akcie kondensacji.', 'woda', '—'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego PET można przetopić i ponownie uformować.', 'Jest termoplastem — ma łańcuchy liniowe bez usieciowania.', '—')),
], 'nieorganiczne': [
 B('Cykl miedzi',
   'Tekst autorski. Przeprowadzono przemiany: Cu → CuO → CuSO₄ → Cu(OH)₂ → CuO → Cu.',
   T('podaj', 2, 'Napisz równania przemian 1, 2 i 5 w formie cząsteczkowej.', '2Cu + O₂ → 2CuO; CuO + H₂SO₄ → CuSO₄ + H₂O; CuO + H₂ → Cu + H₂O', '—'),
   T('podaj', 1, 'Napisz równanie jonowe przemiany 3 i obserwację.', 'Cu²⁺ + 2OH⁻ → Cu(OH)₂↓; niebieski galaretowaty osad', '—')),
], 'redoks': [
 B('Bilans manganianu w środowisku obojętnym',
   'Tekst autorski. Fioletowy roztwór KMnO₄ zmieszano z roztworem Na₂SO₃ w środowisku obojętnym. Wytrącił się brunatny osad.',
   T('podaj', 2, 'Napisz równanie jonowe reakcji (metodą jonowo-elektronową).', '2MnO₄⁻ + 3SO₃²⁻ + H₂O → 2MnO₂ + 3SO₄²⁻ + 2OH⁻', 'Mn: +VII → +IV (3e⁻ · 2); S: +IV → +VI (2e⁻ · 3).'),
   T('podaj', 1, 'Podaj, jak zmieni się odczyn roztworu.', 'stanie się zasadowy (powstają OH⁻)', '—')),
]}
