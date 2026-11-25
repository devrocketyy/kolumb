# Schematy chemii — porcja 6: wykres dochodzenia do równowagi, chromatografia i procesy z całego zakresu.
S = {}


def osie(x0=50, y0=255, w=320, h=220, ox='', oy=''):
    return (f'<path class="s" d="M{x0} {y0 - h} V{y0} H{x0 + w}"/>'
            f'<text class="t" x="{x0 + w - 60}" y="{y0 + 18}">{ox}</text><text class="t" x="{x0 - 44}" y="{y0 - h - 6}">{oy}</text>')


_rown = (
    osie(ox='czas', oy='stężenie')
    + '<path class="s" d="M50 50 C110 120 150 150 220 160 H370"/>'
    + '<path class="s2" d="M50 255 C110 200 150 185 220 180 H370"/>'
    + '<path class="dash" d="M220 40 V255"/>'
)
_rown_zn = [
    (80, 82, 120, 60, 'Substrat', 'stężenie maleje, coraz wolniej'),
    (80, 225, 120, 240, 'Produkt', 'stężenie rośnie, coraz wolniej'),
    (220, 120, 270, 110, 'Osiągnięcie stanu równowagi', 'od tej chwili stężenia są stałe'),
    (300, 160, 330, 140, 'Stan równowagi dynamicznej', 'v reakcji w prawo = v reakcji w lewo'),
]

_chrom = (
    '<rect class="f" x="140" y="30" width="120" height="230" rx="4"/>'
    '<path class="s2" d="M140 225 H260"/>'
    '<rect class="f2" x="130" y="245" width="140" height="25" rx="3"/>'
    '<circle class="d" cx="170" cy="225" r="5"/><circle class="d" cx="230" cy="225" r="5"/>'
    '<circle class="d" cx="170" cy="90" r="6"/><circle class="d" cx="170" cy="160" r="6"/><circle class="d" cx="230" cy="90" r="6"/>'
    '<path class="dash" d="M140 60 H260"/>'
)
_chrom_zn = [
    (170, 225, 80, 225, 'Linia startu', 'nanosi się krople mieszaniny i wzorców; nad poziomem eluentu'),
    (200, 257, 300, 270, 'Eluent (faza ruchoma)', 'wędruje w górę dzięki zjawiskom kapilarnym'),
    (200, 60, 300, 50, 'Czoło eluentu', 'zaznacza się po wyjęciu płytki'),
    (170, 90, 80, 90, 'Składnik o dużym Rf', 'słabo zatrzymywany przez fazę stacjonarną'),
    (170, 160, 80, 160, 'Składnik o małym Rf', 'silniej oddziałuje z fazą stacjonarną'),
]

S['c-rownowaga'] = [
    dict(typ='rysunek', tytul='Dochodzenie do stanu równowagi', svg=_rown, znaczniki=_rown_zn,
         opis='Zmiany stężeń substratu i produktu w czasie reakcji odwracalnej.',
         uwaga='W stanie równowagi stężenia nie muszą być równe — są tylko stałe w czasie.'),
]
S['c-doswiadczenia'] = [
    dict(typ='rysunek', tytul='Chromatografia cienkowarstwowa', svg=_chrom, znaczniki=_chrom_zn,
         opis='Rozdział mieszaniny dwóch składników; z prawej — wzorzec jednego z nich.',
         uwaga='Rf = droga plamki / droga czoła eluentu. Ta sama wartość Rf co wzorca wskazuje tę samą substancję.'),
]

P = lambda tytul, kroki, opis='', uwaga='': dict(typ='proces', tytul=tytul, kroki=kroki, opis=opis, **({'uwaga': uwaga} if uwaga else {}))

S['c-energetyka'] = [
    P('Obliczanie ΔH z prawa Hessa', [
        ('Zapisz reakcję docelową', 'z właściwymi współczynnikami'),
        ('Dobierz reakcje dane', 'tak, aby po dodaniu dały reakcję docelową'),
        ('Odwróć, jeśli trzeba', 'zmień znak ΔH'),
        ('Pomnóż, jeśli trzeba', 'pomnóż też ΔH'),
        ('Dodaj równania i ΔH', 'skróć substancje po obu stronach'),
    ]),
]
S['c-szybkosc'] = [
    P('Czynniki wpływające na szybkość reakcji', [
        ('Stężenie substratów', 'więcej zderzeń w jednostce czasu'),
        ('Temperatura', 'więcej cząsteczek o energii ≥ Eₐ'),
        ('Rozdrobnienie', 'większa powierzchnia kontaktu'),
        ('Katalizator', 'niższa energia aktywacji'),
        ('Ciśnienie (gazy)', 'wzrost stężenia reagentów gazowych'),
        ('Rodzaj substratów', 'np. aktywność metalu'),
    ]),
]
S['c-konfiguracja'] = [
    P('Zapis konfiguracji elektronowej jonu', [
        ('Ustal Z i ładunek', 'liczba elektronów = Z − ładunek'),
        ('Zapisz konfigurację atomu', 'kolejność zapełniania podpowłok'),
        ('Kation bloku s, p', 'usuń elektrony z najwyższej powłoki'),
        ('Kation bloku d', 'najpierw usuń elektrony 4s, potem 3d'),
        ('Anion', 'dodaj elektrony do najbliższej podpowłoki — zwykle konfiguracja gazu szlachetnego'),
    ]),
]
S['c-wiazania'] = [
    P('Rysowanie wzoru elektronowego', [
        ('Policz elektrony walencyjne', 'suma dla wszystkich atomów ± ładunek jonu'),
        ('Ustal szkielet', 'atom centralny, wokół ligandy'),
        ('Wiązania pojedyncze', 'po jednej kresce między atomami'),
        ('Uzupełnij oktety', 'wolne pary — najpierw na atomach zewnętrznych'),
        ('Wiązania wielokrotne', 'jeśli atom centralny nie ma oktetu'),
    ]),
]
S['c-wodorotlenki-kwasy'] = [
    P('Otrzymywanie wodorotlenków i kwasów', [
        ('Metal aktywny + woda', 'wodorotlenek + H₂ (np. Na, Ca)'),
        ('Tlenek zasadowy + woda', 'wodorotlenek (np. CaO)'),
        ('Sól + mocna zasada', 'wodorotlenek trudno rozpuszczalny (strącanie)'),
        ('Tlenek kwasowy + woda', 'kwas tlenowy (np. SO₃ → H₂SO₄)'),
        ('Niemetal + wodór, potem woda', 'kwas beztlenowy (np. HCl)'),
        ('Sól + mocniejszy kwas', 'słabszy kwas (wypieranie)'),
    ]),
]
S['c-metale'] = [
    P('Korozja żelaza i ochrona', [
        ('Utlenianie żelaza (anoda)', 'Fe → Fe²⁺ + 2e⁻'),
        ('Redukcja tlenu (katoda)', 'O₂ + 2H₂O + 4e⁻ → 4OH⁻'),
        ('Powstanie rdzy', 'Fe(OH)₂ → Fe(OH)₃ → Fe₂O₃·nH₂O'),
        ('Ochrona bierna', 'farby, lakiery, warstwa cynku lub chromu'),
        ('Ochrona czynna', 'protektor (Zn, Mg) lub ochrona katodowa'),
    ]),
]
S['c-promieniotworczosc'] = [
    P('Obliczenia z okresem półtrwania', [
        ('Liczba okresów półtrwania', 'n = t / T½'),
        ('Pozostała ilość', 'm = m₀ · (1/2)ⁿ'),
        ('Ilość rozpadnięta', 'm₀ − m'),
        ('Wiek próbki', 'z ilości pozostałej odczytaj n, potem t = n · T½'),
    ]),
]
S['c-izomeria'] = [
    P('Rozpoznawanie rodzaju izomerii', [
        ('Ten sam wzór sumaryczny?', 'jeśli nie — to nie są izomery'),
        ('Inny szkielet węglowy', 'izomeria łańcuchowa'),
        ('Inne położenie grupy lub wiązania', 'izomeria położeniowa'),
        ('Inna grupa funkcyjna', 'izomeria funkcyjna'),
        ('Inne rozmieszczenie w przestrzeni', 'stereoizomeria: cis–trans lub optyczna'),
    ]),
]
S['c-aminy'] = [
    P('Porównywanie mocy zasad azotowych', [
        ('Amoniak', 'punkt odniesienia'),
        ('Aminy alifatyczne', 'mocniejsze — grupy alkilowe zwiększają gęstość elektronową na N'),
        ('Aminy aromatyczne', 'słabsze — wolna para N sprzężona z pierścieniem'),
        ('Amidy', 'praktycznie bez właściwości zasadowych — sąsiedztwo C=O'),
    ]),
]
S['c-srodowisko'] = [
    P('Uzdatnianie wody pitnej', [
        ('Cedzenie i sedymentacja', 'usunięcie większych zanieczyszczeń'),
        ('Koagulacja', 'np. siarczan glinu — łączenie zawiesin w kłaczki'),
        ('Filtracja', 'filtry piaskowe i z węgla aktywnego'),
        ('Dezynfekcja', 'chlor, ozon lub promieniowanie UV'),
    ]),
]
