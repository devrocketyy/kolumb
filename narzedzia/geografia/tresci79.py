# Geografia — porcja 79 (obliczenia krok po kroku w stylu CKE — nowe liczby).
T = {
'g-obrotowy': dict(F=[
 ('Oblicz: na 20°E jest 12:00 czasu słonecznego — która na 35°E?', 'Różnica 15° × 4 min = 60 min; na wschodzie później → 13:00.'),
 ('Oblicz: na 10°W jest 9:00 czasu słonecznego — która na 25°E?', 'Różnica 35° × 4 min = 140 min = 2 h 20 min; na wschodzie później → 11:20.'),
 ('Oblicz: w Warszawie zimą 18:00 — która w Pekinie (UTC+8)?', 'Różnica 7 h → 1:00 następnego dnia.'),
 ('Oblicz: start z Tokio (UTC+9) o 10:00, lot 11 h — o której lądowanie w Warszawie zimą?', 'W Tokio będzie 21:00 → w Warszawie (UTC+1) 13:00 tego samego dnia.'),
 ('Oblicz: różnica czasu słonecznego między Szczecinem (14,5°E) a Białymstokiem (23,2°E)', 'Ok. 8,7° × 4 min ≈ 35 min; w Białymstoku Słońce góruje wcześniej.'),
],
Q=[
 ('Na południku 10°W jest 9:00 czasu słonecznego. Na południku 25°E jest wtedy:', ['*11:20', '6:40', '11:00', '7:20'], '35° × 4 min.'),
]),
'g-obiegowy': dict(F=[
 ('Oblicz: wysokość górowania Słońca 22 VI na 50°N', '90° − 50° + 23°26′ = 63°26′ (nad południowym horyzontem).'),
 ('Oblicz: wysokość górowania Słońca 22 XII na 30°S', '90° − 30° + 23°26′ = 83°26′ (lato na półkuli S; nad północnym horyzontem).'),
 ('Oblicz: wysokość górowania Słońca 21 III na 60°N', '90° − 60° = 30°.'),
 ('Oblicz: wysokość górowania Słońca 22 VI na 10°N', 'Słońce nad zwrotnikiem Raka, czyli na północ od miejsca: 90° − (23°26′ − 10°) = 76°34′ nad północnym horyzontem.'),
 ('Oblicz szerokość: 22 VI Słońce górowało 70° nad południowym horyzontem (półkula N)', 'φ = 90° − 70° + 23°26′ = 43°26′N.'),
],
Q=[
 ('Wysokość górowania Słońca 22 czerwca na 50°N wynosi:', ['*63°26′', '40°', '16°34′', '73°26′'], '90 − 50 + 23°26′.'),
]),
'g-wspolrzedne': dict(F=[
 ('Oblicz: odległość wzdłuż południka między 45°N a 52°N', '7° × 111,2 km ≈ 778 km.'),
 ('Oblicz: odległość wzdłuż równika między 10°E a 40°E', '30° × 111,3 km ≈ 3339 km.'),
 ('Oblicz: odległość wzdłuż południka między 10°S a 20°N', 'Punkty po obu stronach równika: 10° + 20° = 30° × 111,2 km ≈ 3336 km.'),
 ('Oblicz szerokość: Gwiazda Polarna 38° nad horyzontem', '38°N.'),
],
Q=[]),
'g-skala': dict(F=[
 ('Oblicz: 6 cm na mapie 1:25 000', '6 × 250 m = 1,5 km.'),
 ('Oblicz: 3,5 km w terenie na mapie 1:50 000', '3,5 km ÷ 0,5 km = 7 cm.'),
 ('Oblicz: prostokąt 2 × 3 cm na mapie 1:25 000', '0,5 km × 0,75 km = 0,375 km² (37,5 ha).'),
 ('Oblicz skalę: 15 km w terenie to 3 cm na mapie', '1 cm – 5 km → 1:500 000.'),
],
Q=[]),
'g-obliczenia': dict(F=[
 ('Oblicz: spadek rzeki — 450 m różnicy wysokości na 90 km', '450 m ÷ 90 km = 5 m/km = 5‰.'),
 ('Oblicz: gęstość zaludnienia — 2,4 mln osób na 12 000 km²', '200 os./km².'),
 ('Oblicz: temperatura na 1800 m przy 16°C na 300 m (0,6°C/100 m)', 'Różnica 1500 m → 9°C mniej → 7°C.'),
 ('Oblicz: amplituda roczna — lipiec 21,5°C, styczeń −6,5°C', '21,5 − (−6,5) = 28°C.'),
],
Q=[]),
}
