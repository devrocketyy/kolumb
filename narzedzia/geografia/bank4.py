# Bank zadań autorskich — geografia, część 4: mapa szczegółowa, czas, klimat, świat. Dane autorskie.
BANK = {'mapa': [
 B('Wycieczka na wieżę widokową',
   'Tekst autorski. Na mapie w skali 1:25 000 kościół leży na wysokości 212 m n.p.m., a wieża widokowa na wzgórzu — 347 m n.p.m. Odległość między nimi na mapie: 8 cm. Wieża leży od kościoła w kierunku azymutu 135°.',
   T('oblicz', 1, 'Oblicz odległość w terenie między kościołem a wieżą.', '2 km', '8 cm × 250 m.'),
   T('oblicz', 1, 'Oblicz średni spadek terenu między obiektami w procentach.', '6,75%', '135 m / 2000 m × 100%.'),
   T('podaj', 1, 'Podaj kierunek geograficzny od kościoła do wieży oraz azymut drogi powrotnej.', 'południowy wschód (SE); 315°', '135° + 180°.')),
 B('Las na mapie',
   'Tekst autorski. Na mapie w skali 1:25 000 kompleks leśny ma kształt prostokąta o bokach 4 cm i 3 cm.',
   T('oblicz', 2, 'Oblicz powierzchnię lasu w terenie w hektarach.', '75 ha', 'Boki 1 km i 0,75 km → 0,75 km² = 75 ha (lub 12 cm² × 6,25 ha).')),
], 'ziemia': [
 B('Słońce nad Zgorzelcem i Terespolem',
   'Tekst autorski. Zgorzelec leży na ok. 15°00′E, Terespol na ok. 23°40′E. Jest zima (obowiązuje czas UTC+1).',
   T('oblicz', 2, 'Oblicz, o której godzinie czasu urzędowego Słońce góruje w Terespolu.', 'ok. 11:25:20', 'Różnica długości 8°40′ = 520′ × 4 s = 34 min 40 s; Słońce góruje wcześniej niż na 15°E.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego w Zgorzelcu Słońce góruje około 12:00 czasu urzędowego.', 'Zgorzelec leży prawie na południku 15°E — środkowym południku strefy UTC+1.', 'Czas strefowy = czas słoneczny południka środkowego.')),
 B('Lot przez linię zmiany daty',
   'Tekst autorski. Samolot wylatuje z Tokio (UTC+9) 1 lipca o 22:00 czasu lokalnego. Lot do Honolulu (UTC−10) trwa 7 godzin.',
   T('oblicz', 2, 'Podaj datę i godzinę lądowania w czasie lokalnym Honolulu.', '1 lipca, 10:00', 'Wylot 13:00 UTC; lądowanie 20:00 UTC; −10 h → 10:00 1 lipca.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego samolot ląduje „wcześniej”, niż wystartował.', 'Przekroczył linię zmiany daty z zachodu na wschód — data cofa się o dobę.', 'Różnica stref 19 h.')),
], 'atmosfera': [
 B('Temperatura na szczycie',
   'Tekst autorski. U podnóża gór, na wysokości 900 m n.p.m., temperatura wynosi 8°C. Szczyt ma wysokość 1987 m n.p.m. Przyjmij spadek temperatury 0,6°C/100 m.',
   T('oblicz', 2, 'Oblicz temperaturę na szczycie. Wynik zaokrąglij do 0,1°C.', 'ok. 1,5°C', '1087 m × 0,006 = 6,52°C; 8 − 6,52 ≈ 1,5.')),
], 'ludnosc': [
 B('Ludność Nigerii',
   'Tekst autorski. Kraj liczy ok. 230 mln mieszkańców, a współczynnik przyrostu naturalnego wynosi ok. 25‰.',
   T('oblicz', 1, 'Oblicz roczny przyrost naturalny w milionach osób.', 'ok. 5,75 mln', '230 mln × 0,025.'),
   T('oblicz', 1, 'Oszacuj, po ilu latach liczba ludności się podwoi (reguła 70).', 'ok. 28 lat', '70 / 2,5 (% rocznie).'),
   T('podaj', 1, 'Podaj fazę przejścia demograficznego, w której jest ten kraj.', 'faza II–III — eksplozja demograficzna', 'Spadek zgonów, wysokie urodzenia.')),
 B('Starzejąca się Japonia',
   'Tekst autorski. Struktura wieku ludności Japonii: 0–14 lat — 11%, 15–64 lata — 59%, 65 lat i więcej — 30%.',
   T('oblicz', 2, 'Oblicz współczynnik obciążenia demograficznego (liczba osób w wieku 0–14 i 65+ na 100 osób w wieku 15–64).', 'ok. 69', '(11 + 30) / 59 × 100 ≈ 69,5.'),
   T('podaj', 1, 'Podaj dwa skutki gospodarcze starzenia się społeczeństwa.', 'Np. wzrost wydatków na emerytury i opiekę zdrowotną, niedobór rąk do pracy.', 'Japonia — robotyzacja, imigracja.')),
]}
