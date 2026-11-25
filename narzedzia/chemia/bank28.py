# Bank zadań autorskich — chemia, część 28: wiązki CKE 2023+ — przekrój działów (paczka podwójna).
BANK = {'atom': [
 B('Promieniotwórczość w medycynie i datowaniu',
   'Tekst autorski. Technet-99m (T½ = 6 h) stosuje się w diagnostyce. Pacjentowi podano preparat o aktywności 800 MBq.',
   T('oblicz', 1, 'Oblicz aktywność preparatu po 24 h.', '50 MBq', '4 okresy półtrwania: 800/16.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego krótki okres półtrwania jest zaletą w diagnostyce.', 'Izotop szybko traci aktywność — pacjent otrzymuje małą dawkę promieniowania.', '—')),
 B('Energia jonizacji magnezu',
   'Tekst autorski. Kolejne energie jonizacji Mg (kJ/mol): 738, 1451, 7733, 10 540.',
   T('wyjasnij', 1, 'Wyjaśnij duży skok między drugą a trzecią energią jonizacji.', 'Trzeci elektron pochodzi z zamkniętej powłoki 2p⁶, bliżej jądra — trudniej go oderwać.', '—'),
   T('podaj', 1, 'Podaj wzór jonu, który tworzy Mg w związkach.', 'Mg²⁺', '—')),
], 'wiazania': [
 B('Budowa CO₂ i SO₂',
   'Tekst autorski. CO₂ i SO₂ to tlenki o wzorze typu XO₂, ale tylko jeden z nich jest cząsteczką polarną.',
   T('podaj', 2, 'Podaj hybrydyzację atomu centralnego, kształt i polarność każdej cząsteczki.', 'CO₂: sp, liniowa, niepolarna; SO₂: sp², kątowa, polarna', 'Wolna para na S.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego SO₂ lepiej rozpuszcza się w wodzie niż CO₂.', 'SO₂ jest polarny i silniej oddziałuje z polarnymi cząsteczkami wody (oraz z nią reaguje).', '—')),
], 'stechiometria': [
 B('Utlenianie amoniaku — nadmiar',
   'Tekst autorski. Zmieszano 6,8 g NH₃ i 12,8 g O₂. Zachodzi reakcja 4NH₃ + 5O₂ → 4NO + 6H₂O.',
   T('oblicz', 2, 'Wskaż substrat w niedomiarze i oblicz masę NO.', 'O₂ w niedomiarze; 9,6 g NO', 'n(NH₃) = 0,4 → 0,4/4 = 0,1; n(O₂) = 0,4 → 0,4/5 = 0,08 (mniej). n(NO) = 0,4 · 4/5 = 0,32 mol · 30 g/mol.'),
   T('oblicz', 1, 'Oblicz masę wody.', 'ok. 8,6 g', 'n(H₂O) = 0,4 · 6/5 = 0,48 mol · 18 = 8,64 g.')),
 B('Wzór soli z analizy',
   'Tekst autorski. Sól zawiera 32,4% Na, 22,5% S i 45,1% O.',
   T('oblicz', 2, 'Ustal wzór empiryczny soli i podaj jej nazwę.', 'Na₂SO₄ — siarczan(VI) sodu', 'Na : S : O = 1,41 : 0,70 : 2,82 = 2 : 1 : 4.')),
], 'roztwory': [
 B('Roztwór cukru',
   'Tekst autorski. Rozpuszczono 34,2 g sacharozy w wodzie i otrzymano 250 cm³ roztworu o gęstości 1,04 g/cm³.',
   T('oblicz', 1, 'Oblicz stężenie molowe roztworu.', '0,4 mol/dm³', '0,1 mol / 0,25 dm³.'),
   T('oblicz', 1, 'Oblicz stężenie procentowe roztworu.', 'ok. 13,2%', '34,2 / 260.')),
], 'kinetyka': [
 B('Rozkład N₂O₅',
   'Tekst autorski. Rozkład 2N₂O₅ → 4NO₂ + O₂ jest reakcją pierwszego rzędu. Okres półtrwania w danej temperaturze wynosi 20 min. Początkowe stężenie N₂O₅ wynosiło 0,8 mol/dm³.',
   T('oblicz', 1, 'Oblicz stężenie N₂O₅ po 60 min.', '0,1 mol/dm³', 'Trzy okresy półtrwania.'),
   T('oblicz', 1, 'Oblicz stężenie NO₂ po 60 min (V = const).', '1,4 mol/dm³', 'Przereagowało 0,7 mol/dm³ N₂O₅ → 2 · 0,7.')),
], 'roztwory-wodne': [
 B('Zobojętnianie kwasu dwuprotonowego',
   'Tekst autorski. Do 20 cm³ roztworu H₂SO₄ o stężeniu 0,1 mol/dm³ dodawano roztwór NaOH o stężeniu 0,2 mol/dm³.',
   T('oblicz', 1, 'Oblicz objętość NaOH potrzebną do całkowitego zobojętnienia.', '20 cm³', 'n(H₂SO₄) = 0,002 mol → 0,004 mol NaOH / 0,2.'),
   T('podaj', 1, 'Podaj odczyn roztworu po dodaniu 10 cm³ NaOH i wzór soli, która wtedy powstaje.', 'kwasowy; NaHSO₄', 'Pierwszy etap zobojętnienia.')),
], 'redoks': [
 B('Aktywność metali — doświadczenie',
   'Tekst autorski. Płytkę cynkową zanurzono w roztworze Pb(NO₃)₂, a płytkę miedzianą w roztworze ZnSO₄.',
   T('podaj', 1, 'Wskaż probówkę, w której zaszła reakcja, i napisz równanie jonowe.', 'Zn w Pb(NO₃)₂: Zn + Pb²⁺ → Zn²⁺ + Pb', '—'),
   T('podaj', 1, 'Uszereguj Zn, Pb, Cu według malejącej aktywności.', 'Zn > Pb > Cu', '—')),
], 'tlenowe': [
 B('Utlenianie glicerolu i etanolu',
   'Tekst autorski. Do dwóch probówek z Cu(OH)₂ dodano etanol i glicerol.',
   T('podaj', 1, 'Opisz obserwacje w obu probówkach.', 'etanol: brak zmian (niebieski osad); glicerol: szafirowy roztwór', '—'),
   T('wyjasnij', 1, 'Wyjaśnij przyczynę różnicy.', 'Glicerol ma grupy –OH przy sąsiednich atomach węgla, które tworzą kompleks z Cu²⁺.', '—')),
], 'azotowe-cukry': [
 B('Hydroliza skrobi — doświadczenie',
   'Tekst autorski. Kleik skrobiowy ogrzewano z rozcieńczonym HCl. Co kilka minut pobierano próbki i badano płynem Lugola i próbą Trommera (po zobojętnieniu).',
   T('podaj', 2, 'Opisz wyniki obu prób na początku i na końcu doświadczenia.', 'Początek: Lugol — granatowy, Trommer — negatywna; koniec: Lugol — brak zabarwienia, Trommer — ceglasty osad', 'Skrobia hydrolizuje do glukozy.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego przed próbą Trommera trzeba zobojętnić próbkę.', 'Próba wymaga środowiska zasadowego — kwas zobojętniłby NaOH i rozpuścił Cu(OH)₂.', '—')),
], 'nieorganiczne': [
 B('Otrzymywanie siarczanu miedzi(II)',
   'Tekst autorski. Uczeń chce otrzymać CuSO₄ trzema metodami.',
   T('podaj', 2, 'Napisz równania trzech reakcji prowadzących do CuSO₄.', 'CuO + H₂SO₄ → CuSO₄ + H₂O; Cu(OH)₂ + H₂SO₄ → CuSO₄ + 2H₂O; Cu + 2H₂SO₄(stęż.) → CuSO₄ + SO₂ + 2H₂O', 'Miedź nie reaguje z rozcieńczonym H₂SO₄.')),
]}
