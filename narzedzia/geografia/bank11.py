# Bank zadań autorskich — geografia, część 11: surowce, energia, transport, klimat Polski, gleby, rozwój. Dane autorskie.
BANK = {'polska-gospodarka': [
 B('Miedź z Zagłębia Legnicko-Głogowskiego',
   'Tekst autorski. W ciągu roku wydobyto 30 mln t rudy o średniej zawartości miedzi 1,5%.',
   T('oblicz', 1, 'Oblicz masę miedzi zawartej w wydobytej rudzie.', '450 tys. t', '30 000 000 t × 0,015.'),
   T('podaj', 1, 'Podaj nazwę drugiego cennego metalu pozyskiwanego z tych rud.', 'srebro', 'Polska — czołowy producent srebra.')),
 B('Fotowoltaika na dachu',
   'Tekst autorski. Instalacja o mocy 10 kW produkuje w Polsce ok. 1000 kWh z każdego kW mocy rocznie. Dom zużywa 4000 kWh energii rocznie.',
   T('oblicz', 1, 'Oblicz roczną produkcję energii i jej nadwyżkę ponad zużycie.', '10 000 kWh; nadwyżka 6000 kWh', '10 × 1000; 10 000 − 4000.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego produkcja z paneli w Polsce jest najmniejsza w grudniu.', 'Słońce góruje nisko, dzień jest krótki, a zachmurzenie duże — dociera mało promieniowania.', 'Wysokość Słońca, długość dnia.')),
], 'przemysl': [
 B('Kanał Sueski',
   'Tekst autorski. Droga morska Rotterdam–Singapur przez Kanał Sueski ma ok. 15 300 km, a wokół Afryki ok. 21 700 km.',
   T('oblicz', 1, 'Oblicz, o ile kilometrów i o ile procent kanał skraca drogę.', 'o 6400 km, czyli ok. 29%', '6400 / 21 700 × 100 ≈ 29,5.'),
   T('podaj', 1, 'Podaj jeden skutek gospodarczy zablokowania kanału.', 'Np. opóźnienia dostaw, wzrost kosztów frachtu i cen towarów, statki kierowane wokół Afryki.', 'Np. 2021, 2024.')),
], 'polska-przyroda': [
 B('Okres wegetacyjny',
   'Tekst autorski. Okres wegetacyjny trwa we Wrocławiu ok. 225 dni, a w Suwałkach ok. 185 dni.',
   T('oblicz', 1, 'Oblicz różnicę długości okresu wegetacyjnego.', '40 dni', '225 − 185.'),
   T('wyjasnij', 2, 'Wyjaśnij przyczyny tej różnicy.', 'Suwałki leżą dalej na północnym wschodzie — silniejszy wpływ mas kontynentalnych i dłuższa, mroźniejsza zima; Wrocław jest pod wpływem łagodnych mas oceanicznych i leży niżej, na południowym zachodzie.', 'Kontynentalizm, szerokość.')),
], 'atmosfera': [
 B('Inwersja nad miastem',
   'Tekst autorski. Mroźnego zimowego poranka przy ziemi zmierzono −8°C, a na wysokości 300 m −2°C.',
   T('oblicz', 1, 'Oblicz zmianę temperatury na 100 m wysokości.', 'wzrost o 2°C na 100 m', '+6°C / 300 m.'),
   T('wyjasnij', 2, 'Wyjaśnij, dlaczego taka sytuacja sprzyja smogowi.', 'To inwersja temperatury — cieplejsza warstwa powietrza nad zimną blokuje ruchy pionowe, więc zanieczyszczenia z kominów i samochodów zalegają przy ziemi.', 'Brak konwekcji.')),
], 'pedosfera': [
 B('Erozja gleby na stoku',
   'Tekst autorski. Na zaoranym wzdłuż stoku polu gleba traci przez erozję 20 t/ha rocznie, a w tym samym czasie powstaje 1 t/ha nowej gleby.',
   T('oblicz', 1, 'Oblicz ubytek gleby po 50 latach.', '950 t/ha', '(20 − 1) × 50.'),
   T('podaj', 2, 'Podaj dwa sposoby ograniczenia erozji gleb na stokach.', 'Orka w poprzek stoku, tarasowanie, zadrzewienia śródpolne, utrzymywanie okrywy roślinnej (międzyplony), zalesianie stromych stoków.', 'Wystarczą dwa.')),
], 'swiat': [
 B('BRICS',
   'Tekst autorski. Kraje BRICS (pierwotne pięć) zamieszkuje ok. 3,3 mld ludzi, a cały świat — ok. 8,1 mld.',
   T('oblicz', 1, 'Oblicz udział ludności BRICS w ludności świata.', 'ok. 41%', '3,3 / 8,1 × 100 ≈ 40,7.'),
   T('podaj', 1, 'Podaj nazwy dwóch państw BRICS położonych w Azji.', 'Chiny i Indie (także Rosja w części)', 'Pierwotne BRICS.')),
], 'ziemia': [
 B('Dzień polarny',
   'Tekst autorski. Miasto Tromsø leży na ok. 69°40′N.',
   T('rozstrzygnij', 1, 'Rozstrzygnij, czy w Tromsø występuje dzień polarny. Uzasadnij.', 'Tak — miasto leży na północ od koła podbiegunowego (66°33′N).', 'Za kołem podbiegunowym.'),
   T('oblicz', 1, 'Oblicz wysokość Słońca w momencie górowania 22 czerwca w Tromsø.', '43°47′', '90° − 69°40′ + 23°27′.')),
]}
