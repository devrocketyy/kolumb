# Schematy chemii — porcja 5: procesy i algorytmy z całego zakresu (rozwiązywanie typowych zadań CKE).
S = {}
P = lambda tytul, kroki, opis='', uwaga='': dict(typ='proces', tytul=tytul, kroki=kroki, opis=opis, **({'uwaga': uwaga} if uwaga else {}))

S['c-polecenia'] = [
    P('Jak odpowiadać na polecenia „wyjaśnij” i „uzasadnij”', [
        ('Przeczytaj, czego dotyczy pytanie', 'zjawisko, wybór czy wynik doświadczenia'),
        ('Wskaż przyczynę', 'odwołaj się do budowy, właściwości lub danych z informacji'),
        ('Połącz przyczynę ze skutkiem', '„ponieważ…, więc…”'),
        ('Użyj terminologii', 'np. hydroliza anionowa, efekt wspólnego jonu'),
        ('Sprawdź zgodność z poleceniem', 'nie dopisuj sprzecznych informacji'),
    ]),
]
S['c-doswiadczenia'] = [
    P('Projektowanie doświadczenia — krok po kroku', [
        ('Cel', 'co ma zostać wykazane lub odróżnione'),
        ('Wybór odczynnika', 'taki, który da różne obserwacje dla badanych substancji'),
        ('Schemat', 'odczynnik → probówki z badanymi substancjami'),
        ('Obserwacje', 'zmiany barwy, osad, gaz, zapach — bez nazw produktów'),
        ('Wniosek', 'nazwy substancji lub równania reakcji'),
    ], uwaga='Obserwacja to to, co widzisz; wniosek to to, co z tego wynika.'),
    P('Identyfikacja jonów w roztworze', [
        ('Cl⁻', 'AgNO₃ — biały osad AgCl'),
        ('SO₄²⁻', 'BaCl₂ — biały osad nierozpuszczalny w HCl'),
        ('CO₃²⁻', 'HCl — gaz mętniejący wodę wapienną'),
        ('NH₄⁺', 'NaOH, ogrzewanie — zapach NH₃, papierek niebieszczeje'),
        ('Fe³⁺', 'NaOH — brunatny osad; KSCN — krwistoczerwone zabarwienie'),
        ('Cu²⁺', 'NaOH — niebieski osad Cu(OH)₂'),
    ]),
]
S['c-mol'] = [
    P('Przeliczanie wielkości chemicznych', [
        ('Masa → mole', 'n = m / M'),
        ('Objętość gazu (w. n.) → mole', 'n = V / 22,4 dm³'),
        ('Liczba drobin → mole', 'n = N / 6,02 · 10²³'),
        ('Inne warunki', 'n = pV / RT'),
        ('Roztwór', 'n = c · V'),
    ]),
]
S['c-stechiometria'] = [
    P('Analiza mieszaniny dwóch substancji', [
        ('Oznacz niewiadome', 'x i y — liczby moli składników'),
        ('Równanie masy', 'Mₐx + M_by = masa mieszaniny'),
        ('Równanie produktu', 'z równań reakcji, np. objętość gazu'),
        ('Rozwiąż układ', 'sprawdź, czy x i y są dodatnie'),
        ('Odpowiedź', 'masa lub procent składnika'),
    ]),
]
S['c-rozpuszczalnosc'] = [
    P('Krystalizacja przez ochłodzenie — obliczenia', [
        ('Skład roztworu nasyconego w T₁', 'masa wody i soli z rozpuszczalności'),
        ('Ile soli pozostanie w T₂', 'rozpuszczalność w T₂ · masa wody / 100'),
        ('Masa kryształów', 'różnica mas soli'),
        ('Hydrat', 'kryształy zabierają wodę — przelicz masę soli bezwodnej i wody'),
    ]),
]
S['c-kwasy-zasady'] = [
    P('Wskazywanie sprzężonych par kwas–zasada', [
        ('Znajdź drobinę, która oddaje H⁺', 'to kwas'),
        ('Drobina po oddaniu H⁺', 'to zasada sprzężona'),
        ('Znajdź drobinę, która przyjmuje H⁺', 'to zasada'),
        ('Drobina po przyjęciu H⁺', 'to kwas sprzężony'),
    ], uwaga='Para sprzężona różni się dokładnie jednym protonem, np. H₂O / OH⁻, H₃O⁺ / H₂O.'),
]
S['c-tlenki'] = [
    P('Ustalanie charakteru tlenku', [
        ('Reaguje z kwasem, nie z zasadą', 'zasadowy'),
        ('Reaguje z zasadą, nie z kwasem', 'kwasowy'),
        ('Reaguje z kwasem i z zasadą', 'amfoteryczny'),
        ('Nie reaguje z żadnym', 'obojętny'),
    ]),
]
S['c-sole'] = [
    P('Metody otrzymywania soli', [
        ('Metal + kwas', 'np. Zn + 2HCl → ZnCl₂ + H₂'),
        ('Tlenek metalu + kwas', 'np. CuO + H₂SO₄ → CuSO₄ + H₂O'),
        ('Wodorotlenek + kwas', 'zobojętnianie'),
        ('Tlenek kwasowy + zasada', 'np. CO₂ + 2NaOH → Na₂CO₃ + H₂O'),
        ('Tlenek zasadowy + tlenek kwasowy', 'np. CaO + CO₂ → CaCO₃'),
        ('Sól + sól (strącanie)', 'np. AgNO₃ + NaCl → AgCl↓ + NaNO₃'),
        ('Metal + niemetal', 'np. 2Na + Cl₂ → 2NaCl'),
    ]),
]
S['c-elektroliza'] = [
    P('Przewidywanie produktów elektrolizy roztworu wodnego', [
        ('Katoda — kation metalu mało aktywnego', 'wydziela się metal (Cu, Ag)'),
        ('Katoda — kation metalu aktywnego', 'redukuje się woda — wodór'),
        ('Anoda — Cl⁻, Br⁻, I⁻', 'wydziela się halogen'),
        ('Anoda — aniony tlenowe, F⁻', 'utlenia się woda — tlen'),
        ('Anoda roztwarzalna', 'metal anody przechodzi do roztworu'),
    ]),
]
S['c-karboksylowe'] = [
    P('Otrzymywanie kwasów karboksylowych', [
        ('Utlenianie alkoholi I-rzędowych', 'np. KMnO₄ lub K₂Cr₂O₇ w H⁺'),
        ('Utlenianie aldehydów', 'nawet łagodnymi utleniaczami'),
        ('Fermentacja octowa', 'C₂H₅OH + O₂ → CH₃COOH + H₂O (bakterie)'),
        ('Hydroliza estrów', 'w środowisku kwasowym'),
        ('Wypieranie z soli', 'mocniejszy kwas + sól kwasu karboksylowego'),
    ]),
]
S['c-estry'] = [
    P('Otrzymywanie mydła', [
        ('Tłuszcz + NaOH(aq)', 'ogrzewanie (zmydlanie)'),
        ('Produkty', 'glicerol i sole sodowe kwasów tłuszczowych'),
        ('Wysalanie', 'dodatek NaCl wydziela mydło z roztworu'),
        ('Działanie myjące', 'część hydrofobowa wiąże brud, hydrofilowa — wodę (micele)'),
    ]),
]
S['c-chemia-zycia'] = [
    P('Cykl wapniowy w budownictwie', [
        ('Prażenie wapienia', 'CaCO₃ → CaO + CO₂'),
        ('Gaszenie wapna', 'CaO + H₂O → Ca(OH)₂'),
        ('Zaprawa wapienna', 'Ca(OH)₂ + piasek + woda'),
        ('Twardnienie', 'Ca(OH)₂ + CO₂ → CaCO₃ + H₂O'),
    ]),
]
