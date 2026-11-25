# Schematy chemii — porcja 2: procesy i algorytmy (kroki z krótkim opisem).
S = {}

P = lambda tytul, kroki, opis='', uwaga='': dict(typ='proces', tytul=tytul, kroki=kroki, opis=opis, **({'uwaga': uwaga} if uwaga else {}))

S['c-obliczenia'] = [
    P('Model rozwiązania zadania obliczeniowego', [
        ('Równanie reakcji', 'zapisz i uzgodnij — bez tego proporcja jest błędna'),
        ('Dane i szukane', 'z jednostkami; przelicz cm³ na dm³, mg na g'),
        ('Liczba moli', 'n = m/M, n = V/22,4 dm³ (w. n.), n = c · V'),
        ('Proporcja ze stosunku molowego', 'współczynniki równania'),
        ('Wynik i jednostka', 'zaokrąglenie wg polecenia; sprawdź sens (czy masa nie większa od substratu)'),
    ], 'Schemat punktowany przez CKE: metoda + obliczenia + wynik z jednostką.'),
    P('Obliczenia z nadmiarem', [
        ('Liczby moli obu substratów', ''),
        ('Podziel przez współczynniki', 'mniejszy iloraz = substrat w niedomiarze'),
        ('Licz produkt z niedomiaru', 'substrat w nadmiarze zostaje częściowo nieprzereagowany'),
        ('Skład mieszaniny końcowej', 'produkty + pozostały nadmiar'),
    ]),
    P('Wydajność reakcji', [
        ('Ilość teoretyczna', 'z równania, przy 100% przereagowania'),
        ('Ilość praktyczna', 'otrzymana w doświadczeniu'),
        ('W = praktyczna / teoretyczna · 100%', ''),
        ('Proces wieloetapowy', 'wydajność całkowita = iloczyn wydajności etapów'),
    ]),
]
S['c-konfiguracja'] = [
    P('Kolejność zapełniania podpowłok', [
        ('1s', ''), ('2s → 2p', ''), ('3s → 3p', ''), ('4s → 3d → 4p', 'reguła n + l: 4s ma niższą energię niż 3d'),
        ('5s → 4d → 5p', ''), ('Wyjątki: Cr, Cu', '4s¹ 3d⁵ i 4s¹ 3d¹⁰ — trwała podpowłoka półzapełniona lub zapełniona'),
        ('Jony bloku d', 'najpierw usuwa się elektrony 4s, potem 3d'),
    ], 'Reguła Hunda: elektrony najpierw pojedynczo, o równoległych spinach.'),
]
S['c-promieniotworczosc'] = [
    P('Ustalanie liczby przemian α i β⁻ w szeregu', [
        ('Różnica liczb masowych', 'liczba przemian α = ΔA / 4'),
        ('Spadek Z po przemianach α', '2 · liczba α'),
        ('Porównaj z Z produktu', 'każda β⁻ zwiększa Z o 1'),
        ('Liczba β⁻', '= Z(produkt) − (Z(substrat) − 2α)'),
    ]),
]
S['c-geometria'] = [
    P('Ustalanie kształtu cząsteczki (VSEPR)', [
        ('Atom centralny', 'zwykle najmniej elektroujemny (nie H)'),
        ('Liczba przestrzenna', 'atomy przyłączone + wolne pary atomu centralnego'),
        ('Hybrydyzacja', '2 → sp, 3 → sp², 4 → sp³'),
        ('Kształt', 'liczą się tylko atomy: NH₃ — piramida, H₂O — kątowa'),
        ('Polarność', 'polarne wiązania + niesymetryczny kształt = cząsteczka polarna'),
    ], uwaga='CO₂ ma wiązania polarne, ale jest liniowa, więc niepolarna.'),
]
S['c-bilans'] = [
    P('Bilansowanie równania redoks metodą jonowo-elektronową', [
        ('Stopnie utlenienia', 'wskaż, co się utlenia, a co redukuje'),
        ('Równania połówkowe', 'osobno utlenianie i redukcja'),
        ('Bilans atomów O i H', 'środowisko kwasowe: H₂O i H⁺; zasadowe: H₂O i OH⁻'),
        ('Bilans ładunku', 'dopisz elektrony'),
        ('Wspólna wielokrotność elektronów', 'pomnóż równania'),
        ('Dodaj i skróć', 'sprawdź atomy i ładunki po obu stronach'),
    ]),
]
S['c-rownowaga'] = [
    P('Obliczanie stałej równowagi (tabela „początek–zmiana–równowaga”)', [
        ('Stężenia początkowe', 'n/V'),
        ('Zmiana', 'x pomnożone przez współczynniki'),
        ('Stężenia równowagowe', 'początek ± zmiana'),
        ('Wyrażenie na K', 'produkty / substraty w potęgach współczynników; bez ciał stałych i wody-rozpuszczalnika'),
        ('Rozwiąż i sprawdź', 'stężenia nie mogą wyjść ujemne'),
    ]),
    P('Reguła przekory — szybka analiza', [
        ('Dodanie substratu', 'równowaga w prawo'),
        ('Usunięcie produktu', 'równowaga w prawo'),
        ('Wzrost ciśnienia', 'w stronę mniejszej liczby moli gazów'),
        ('Wzrost temperatury', 'w stronę reakcji endotermicznej; zmienia się K'),
        ('Katalizator', 'brak przesunięcia, szybciej osiągnięta równowaga'),
    ]),
]
S['c-mieszanie'] = [
    P('Mieszanie i rozcieńczanie roztworów', [
        ('Masa substancji przed', 'mₛ = cₚ · m_r / 100%'),
        ('Masa substancji po', 'suma mas substancji z obu roztworów'),
        ('Masa roztworu po', 'suma mas roztworów (+ dodana woda)'),
        ('Nowe stężenie', 'cₚ = mₛ / m_r · 100%'),
    ], uwaga='Stężenia molowe przy mieszaniu: sumuj liczby moli i objętości (jeśli polecenie pozwala).'),
]
S['c-jonowe'] = [
    P('Zapis równania jonowego skróconego', [
        ('Równanie cząsteczkowe', 'uzgodnione'),
        ('Rozpisz na jony', 'tylko mocne elektrolity rozpuszczalne w wodzie'),
        ('Nie rozpisuj', 'osadów, gazów, wody, słabych elektrolitów'),
        ('Skreśl jony obojętne', 'występujące po obu stronach'),
        ('Sprawdź ładunki', 'suma po lewej = suma po prawej'),
    ]),
]
S['c-izomeria'] = [
    P('Nazewnictwo systematyczne związku organicznego', [
        ('Najdłuższy łańcuch', 'zawierający grupę funkcyjną i wiązania wielokrotne'),
        ('Numeracja', 'najniższy lokant dla grupy głównej, potem wiązań wielokrotnych, potem podstawników'),
        ('Podstawniki', 'alfabetycznie, z przedrostkami di-, tri-'),
        ('Końcówka', '-an, -en, -yn, -ol, -al, -on, kwas -owy'),
    ]),
    P('Sprawdzanie izomerii cis–trans', [
        ('Wiązanie C=C lub pierścień', 'brak swobodnej rotacji'),
        ('Każdy atom C wiązania', 'musi mieć dwa różne podstawniki'),
        ('Jeśli przy jednym C dwa jednakowe', 'izomeria geometryczna nie występuje'),
    ]),
]
S['c-alkany'] = [
    P('Mechanizm chlorowania alkanu (rodnikowy)', [
        ('Inicjacja', 'Cl₂ → 2Cl· pod wpływem światła'),
        ('Propagacja I', 'Cl· + RH → HCl + R·'),
        ('Propagacja II', 'R· + Cl₂ → RCl + Cl·'),
        ('Terminacja', 'łączenie dwóch rodników'),
    ], uwaga='Najłatwiej podstawiany jest H przy węglu III-rzędowym (najtrwalszy rodnik).'),
]
S['c-alkeny'] = [
    P('Addycja elektrofilowa HX do alkenu', [
        ('Atak H⁺ na wiązanie π', 'powstaje karbokation'),
        ('Trwalszy karbokation', 'na atomie C o większej liczbie podstawników'),
        ('Przyłączenie X⁻', 'reguła Markownikowa'),
        ('Nadtlenki (tylko HBr)', 'mechanizm rodnikowy — produkt antymarkownikowski'),
    ]),
]
S['c-alkohole'] = [
    P('Utlenianie alkoholi', [
        ('Alkohol I-rzędowy', '→ aldehyd → kwas karboksylowy'),
        ('Alkohol II-rzędowy', '→ keton'),
        ('Alkohol III-rzędowy', 'nie utlenia się w łagodnych warunkach'),
        ('Utleniacze', 'CuO (T), K₂Cr₂O₇/H⁺ (pomarańczowy → zielony), KMnO₄/H⁺'),
    ]),
]
S['c-cukry'] = [
    P('Identyfikacja cukrów — kolejność prób', [
        ('Cu(OH)₂ na zimno', 'szafirowy roztwór — wiele grup –OH przy sąsiednich C'),
        ('Próba Trommera / Tollensa', 'cukry redukujące (glukoza, fruktoza, maltoza, laktoza)'),
        ('Woda bromowa + NaHCO₃', 'odbarwia tylko aldozy — odróżnia glukozę od fruktozy'),
        ('Jod (płyn Lugola)', 'skrobia — granatowe zabarwienie'),
        ('Sacharoza', 'nieredukująca; po hydrolizie daje pozytywny wynik'),
    ]),
]
S['c-aminokwasy'] = [
    P('Wykrywanie białek', [
        ('Reakcja biuretowa', 'Cu²⁺ w środowisku zasadowym — fioletowe; min. 2 wiązania peptydowe'),
        ('Reakcja ksantoproteinowa', 'stężony HNO₃ — żółte; aminokwasy z pierścieniem aromatycznym'),
        ('Denaturacja', 'sole metali ciężkich, etanol, temperatura — nieodwracalna'),
        ('Wysalanie', 'roztwory soli lekkich metali — odwracalne'),
    ]),
]
S['c-estry'] = [
    P('Estryfikacja i hydroliza estrów', [
        ('Kwas + alkohol', 'stężony H₂SO₄, ogrzewanie — reakcja odwracalna'),
        ('Pochodzenie atomów O', 'woda powstaje z –OH kwasu i H alkoholu'),
        ('Hydroliza kwasowa', 'odwracalna: ester + woda ⇄ kwas + alkohol'),
        ('Hydroliza zasadowa (zmydlanie)', 'nieodwracalna: powstaje sól kwasu i alkohol'),
    ]),
]
