# Bank zadań autorskich — geografia, część 14: skala i azymut, lesistość, uprawy, Żuławy, klimat Polski, konurbacja. Dane autorskie.
BANK = {'mapa': [
 B('Skala z odległości',
   'Tekst autorski. Odległość 15 km między dwiema miejscowościami odpowiada na mapie 3 cm.',
   T('oblicz', 1, 'Oblicz skalę liczbową mapy.', '1:500 000', '1 500 000 cm / 3.'),
   T('oblicz', 1, 'Oblicz odległość w terenie odpowiadającą na tej mapie odcinkowi 7 cm.', '35 km', '7 × 5 km.')),
 B('Marsz na azymut',
   'Tekst autorski. Turysta przeszedł z punktu A do B w kierunku azymutu 60°, a następnie z B do C w kierunku azymutu 150°.',
   T('podaj', 1, 'Podaj kierunki geograficzne obu odcinków marszu.', 'A–B: północny wschód (ENE); B–C: południowy wschód (SSE)', '60° i 150°.'),
   T('oblicz', 1, 'Oblicz azymut drogi powrotnej z B do A.', '240°', '60° + 180°.')),
], 'umiejetnosci': [
 B('Lesistość województwa',
   'Tekst autorski. Województwo ma 18 000 km², z czego lasy zajmują 9000 km². Lesistość Polski wynosi ok. 31%.',
   T('oblicz', 1, 'Oblicz lesistość województwa.', '50%', '9000 / 18 000 × 100.'),
   T('podaj', 1, 'Podaj przyczynę przyrodniczą dużej lesistości takiego regionu.', 'Np. słabe gleby piaszczyste nieprzydatne dla rolnictwa, górzysta rzeźba.', 'Lubuskie, Podkarpackie.')),
], 'rolnictwo': [
 B('Kawa z Brazylii',
   'Tekst autorski. Światowa produkcja kawy wynosi ok. 10,5 mln t, a Brazylii ok. 3,4 mln t.',
   T('oblicz', 1, 'Oblicz udział Brazylii w produkcji kawy. Wynik zaokrąglij do 1%.', 'ok. 32%', '3,4 / 10,5 × 100 ≈ 32,4.'),
   T('podaj', 2, 'Podaj dwa przyrodnicze warunki uprawy kawy.', 'Ciepły klimat bez przymrozków (ok. 18–24°C), opady ok. 1500–2000 mm, żyzne gleby (np. terra roxa), wyżynne położenie.', 'Wystarczą dwa.')),
], 'polska-przyroda': [
 B('Depresja na Żuławach',
   'Tekst autorski. Najniżej położony punkt Polski leży na ok. 1,8 m p.p.m., a korona wału przeciwpowodziowego obok — na 6 m n.p.m.',
   T('oblicz', 1, 'Oblicz różnicę wysokości między punktem a koroną wału.', '7,8 m', '6 − (−1,8).'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego Żuławy trzeba stale odwadniać.', 'Teren leży poniżej poziomu morza i rzek — woda sama nie odpłynie, więc pompownie przepompowują ją z polderów do rzek.', 'Poldery.')),
 B('Zimy na zachodzie i wschodzie',
   'Tekst autorski. Średnia temperatura stycznia w Świnoujściu wynosi ok. 0°C, a w Suwałkach ok. −4°C. Odległość między miastami to ok. 640 km.',
   T('oblicz', 1, 'Oblicz średni spadek temperatury stycznia na każde 100 km.', 'ok. 0,6°C/100 km', '4°C / 6,4.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego zimą izotermy w Polsce biegną z północy na południe.', 'Zimą o temperaturze decyduje odległość od Atlantyku — im dalej na wschód, tym słabszy wpływ ciepłych mas oceanicznych i silniejszy kontynentalnych.', 'Kontynentalizm.')),
], 'ludnosc': [
 B('Konurbacja górnośląska',
   'Tekst autorski. Metropolia górnośląska liczy ok. 2,2 mln mieszkańców na powierzchni ok. 2500 km².',
   T('oblicz', 1, 'Oblicz gęstość zaludnienia metropolii.', 'ok. 880 os./km²', '2 200 000 / 2500.'),
   T('wyjasnij', 2, 'Wyjaśnij, dlaczego na Górnym Śląsku powstała konurbacja, a nie aglomeracja z jednym centrum.', 'Wiele miast rozwijało się równolegle wokół kopalń i hut w XIX–XX w.; z czasem zrosły się w policentryczny zespół bez jednego dominującego ośrodka.', 'Industrializacja.')),
 B('Mediana wieku',
   'Tekst autorski. Mediana wieku ludności: Niger 15 lat, Polska 42 lata, Japonia 49 lat.',
   T('podaj', 1, 'Podaj, które z państw ma najstarsze społeczeństwo.', 'Japonia', 'Najwyższa mediana.'),
   T('wyjasnij', 1, 'Wyjaśnij, co oznacza mediana wieku 15 lat w Nigrze.', 'Połowa mieszkańców ma mniej niż 15 lat — bardzo wysoka dzietność i młoda struktura wieku.', 'Mediana.')),
]}
