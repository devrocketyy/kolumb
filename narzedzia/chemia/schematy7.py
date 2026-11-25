# Schematy chemii — porcja 7: procesy i algorytmy — domknięcie wszystkich poddziałów.
S = {}
P = lambda tytul, kroki, opis='', uwaga='': dict(typ='proces', tytul=tytul, kroki=kroki, opis=opis, **({'uwaga': uwaga} if uwaga else {}))

S['c-atom'] = [
    P('Obliczanie średniej masy atomowej i składu izotopowego', [
        ('Średnia masa z udziałów', 'A = Σ (masa izotopu · udział)'),
        ('Skład z masy średniej (2 izotopy)', 'A = m₁x + m₂(1 − x) — rozwiąż względem x'),
        ('Sprawdzenie', 'masa średnia leży bliżej izotopu o większym udziale'),
    ]),
]
S['c-stopnie'] = [
    P('Ustalanie stopnia utlenienia', [
        ('Pierwiastki w stanie wolnym', '0'),
        ('Pewne stopnie', 'F: −I; litowce +I; berylowce +II; H zwykle +I; O zwykle −II'),
        ('Suma w cząsteczce', 'równa 0'),
        ('Suma w jonie', 'równa ładunkowi jonu'),
        ('Wylicz niewiadomą', 'z równania sumy'),
    ]),
    P('Rozpoznawanie reakcji redoks', [
        ('Ustal stopnie utlenienia wszystkich pierwiastków', 'po obu stronach'),
        ('Czy któryś się zmienił?', 'jeśli nie — to nie jest redoks'),
        ('Wzrost stopnia', 'utlenianie — ta drobina to reduktor'),
        ('Spadek stopnia', 'redukcja — ta drobina to utleniacz'),
    ]),
]
S['c-oddzialywania'] = [
    P('Przewidywanie temperatury wrzenia', [
        ('Rodzaj kryształu', 'kowalencyjny > jonowy > metaliczny (zwykle) > molekularny'),
        ('Wiązania wodorowe', 'znacznie podwyższają temperaturę wrzenia'),
        ('Polarność', 'cząsteczki polarne wrzą wyżej niż niepolarne o podobnej masie'),
        ('Masa cząsteczkowa', 'większa masa — silniejsze siły van der Waalsa'),
        ('Kształt', 'łańcuchy proste wrzą wyżej niż rozgałęzione'),
    ]),
]
S['c-mieszanie'] = [
    P('Reguła krzyżowa (mieszanie roztworów)', [
        ('Wpisz stężenia', 'c₁ i c₂ roztworów wyjściowych, c — docelowe'),
        ('Odejmij po przekątnych', '|c₂ − c| i |c − c₁|'),
        ('Stosunek mas', 'm₁ : m₂ = |c₂ − c| : |c − c₁|'),
        ('Woda i czysta substancja', '0% i 100%'),
    ]),
]
S['c-jonowe'] = [
    P('Przewidywanie, czy powstanie osad', [
        ('Wypisz możliwe produkty wymiany', 'pary kation–anion z obu roztworów'),
        ('Sprawdź w tabeli rozpuszczalności', 'czy któryś produkt jest trudno rozpuszczalny'),
        ('Jeśli tak', 'powstaje osad — zapisz równanie jonowe'),
        ('Jeśli nie', 'brak reakcji (wszystkie jony zostają w roztworze)'),
    ]),
]
S['c-tlenki'] = [
    P('Reakcje tlenków — przegląd', [
        ('Tlenek zasadowy + woda', 'wodorotlenek (tylko tlenki litowców i cięższych berylowców)'),
        ('Tlenek kwasowy + woda', 'kwas tlenowy (poza SiO₂)'),
        ('Tlenek zasadowy + kwas', 'sól + woda'),
        ('Tlenek kwasowy + zasada', 'sól + woda'),
        ('Tlenek amfoteryczny', 'reaguje z kwasami i mocnymi zasadami'),
    ]),
]
S['c-niemetale'] = [
    P('Właściwości halogenów w grupie', [
        ('Fluor', 'najsilniejszy utleniacz, gaz jasnożółty'),
        ('Chlor', 'gaz żółtozielony, wypiera Br₂ i I₂'),
        ('Brom', 'ciecz brunatnoczerwona, wypiera I₂'),
        ('Jod', 'ciało stałe fioletowoczarne, sublimuje'),
        ('Trend w dół grupy', 'maleje elektroujemność i aktywność utleniająca'),
    ]),
]
S['c-wzory'] = [
    P('Ustalanie wzoru z procentowego składu', [
        ('Przyjmij 100 g związku', 'procenty = masy w gramach'),
        ('Podziel przez masy molowe', 'liczby moli pierwiastków'),
        ('Podziel przez najmniejszą', 'stosunek liczb całkowitych (ew. pomnóż)'),
        ('Wzór rzeczywisty', 'porównaj z masą molową'),
    ]),
]
S['c-sole'] = [
    P('Nazewnictwo soli', [
        ('Nazwa anionu', 'od kwasu: -ek (beztlenowe), -an (tlenowe)'),
        ('Stopień utlenienia', 'w nawiasie, gdy pierwiastek ma kilka, np. siarczan(IV)'),
        ('Nazwa kationu', 'w dopełniaczu, z wartościowością metalu, np. żelaza(III)'),
        ('Wodorosole', 'przedrostek wodoro-/diwodoro-'),
        ('Hydraty', 'woda krystalizacyjna, np. „—woda(1/5)”'),
    ]),
]
S['c-estry'] = [
    P('Nazewnictwo estrów', [
        ('Rozpoznaj część kwasową', 'R–COO– (z atomem C grupy karbonylowej)'),
        ('Rozpoznaj część alkoholową', 'grupa alkilowa przy tlenie'),
        ('Nazwa', 'anion kwasu + nazwa grupy alkilowej, np. etanian propylu'),
        ('Nazwy zwyczajowe', 'octan, mrówczan, maślan'),
    ]),
]
S['c-chemia-zycia'] = [
    P('Tworzywa sztuczne — klasyfikacja', [
        ('Polimeryzacja (addycyjna)', 'PE, PP, PCW, PS, teflon'),
        ('Polikondensacja', 'poliestry (PET), poliamidy (nylon), żywice fenolowo-formaldehydowe'),
        ('Termoplasty', 'miękną po ogrzaniu, można je przetwarzać ponownie'),
        ('Duroplasty', 'po utwardzeniu nie miękną'),
        ('Recykling', 'oznaczenia 1–7 na opakowaniach'),
    ]),
]
S['c-rozpuszczalnosc'] = [
    P('Iloczyn rozpuszczalności — obliczenia', [
        ('Zapisz równanie dysocjacji', 'np. MₐXᵦ ⇄ aMⁿ⁺ + bXᵐ⁻'),
        ('Wyraź stężenia przez s', '[M] = a·s, [X] = b·s'),
        ('Wstaw do Kₛ', 'Kₛ = (as)ᵃ(bs)ᵇ'),
        ('Rozwiąż względem s', 'rozpuszczalność molowa'),
        ('Ze wspólnym jonem', 's = Kₛ / stężenie wspólnego jonu (dla soli typu MX)'),
    ]),
]
S['c-promieniotworczosc'] = [
    P('Uzupełnianie równań reakcji jądrowych', [
        ('Suma liczb masowych', 'po obu stronach równa'),
        ('Suma liczb atomowych', 'po obu stronach równa'),
        ('Cząstka α', '⁴₂He'),
        ('Cząstka β⁻', '⁰₋₁e'),
        ('Neutron i proton', '¹₀n i ¹₁p'),
    ]),
]
S['c-kwasy-zasady'] = [
    P('Porównywanie mocy kwasów', [
        ('Ka lub pKa', 'większe Ka (mniejsze pKa) — mocniejszy kwas'),
        ('Kwasy tlenowe tego samego pierwiastka', 'więcej atomów O — mocniejszy'),
        ('Kwasy beztlenowe w grupie', 'moc rośnie w dół (HF < HCl < HBr < HI)'),
        ('Doświadczenie', 'mocniejszy kwas wypiera słabszy z jego soli'),
    ]),
]
S['c-alkany'] = [
    P('Nazewnictwo alkanów rozgałęzionych', [
        ('Najdłuższy łańcuch', 'nazwa podstawowa'),
        ('Numeracja', 'od końca bliższego rozgałęzieniu'),
        ('Podstawniki', 'lokant + nazwa (metylo-, etylo-), alfabetycznie'),
        ('Takie same podstawniki', 'przedrostki di-, tri-, tetra-'),
    ]),
]
S['c-karbonylowe'] = [
    P('Otrzymywanie i reakcje związków karbonylowych', [
        ('Alkohol I-rzędowy → aldehyd', 'CuO lub K₂Cr₂O₇ (łagodnie)'),
        ('Alkohol II-rzędowy → keton', 'CuO lub K₂Cr₂O₇'),
        ('Aldehyd → kwas', 'utlenianie (Tollens, Trommer, KMnO₄)'),
        ('Aldehyd/keton → alkohol', 'redukcja wodorem (kat.)'),
    ]),
]
S['c-cukry'] = [
    P('Hydroliza cukrów złożonych', [
        ('Sacharoza', 'glukoza + fruktoza'),
        ('Maltoza', '2 glukoza'),
        ('Laktoza', 'galaktoza + glukoza'),
        ('Skrobia (etapami)', 'dekstryny → maltoza → glukoza'),
        ('Celuloza', 'celobioza → glukoza'),
    ]),
]
S['c-energetyka'] = [
    P('Obliczanie ΔH z energii wiązań', [
        ('Narysuj wzory strukturalne', 'policz wiązania w substratach i produktach'),
        ('Energia wiązań zrywanych', 'suma dla substratów'),
        ('Energia wiązań tworzonych', 'suma dla produktów'),
        ('ΔH = Σ zrywane − Σ tworzone', 'ujemne — reakcja egzotermiczna'),
    ]),
]
