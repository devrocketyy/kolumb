# Schematy chemii — porcja 1: zestawy laboratoryjne, wykresy i ogniwa (rysunki autorskie IndexLab).
# SVG w viewBox 400×300. Klasy jak w biologii: s, s2, f, f2, d, dash, t.
# Znacznik: (x, y elementu, x, y numeru, nazwa, krótki opis).

S = {}


def kolba(cx, y_szyjka, r=40, szyjka=50, w=14, ciecz=True):
    """Kolba okrągłodenna: szyjka od y_szyjka w dół, bańka o promieniu r."""
    cy = y_szyjka + szyjka + r - 4
    out = (f'<path class="s" d="M{cx - w / 2} {y_szyjka} v{szyjka} a{r} {r} 0 1 0 {w} 0 v-{szyjka}"/>')
    if ciecz:
        out += f'<path class="f" d="M{cx - r + 6} {cy + 8} a{r - 6} {r - 6} 0 0 0 {2 * (r - 6)} 0 z"/>'
    return out


def zlewka(x, y, w=80, h=90, poziom=0.55):
    out = f'<path class="s" d="M{x} {y} v{h} h{w} v-{h}"/>'
    hy = y + h * (1 - poziom)
    out += f'<rect class="f" x="{x + 1}" y="{hy}" width="{w - 2}" height="{y + h - hy - 1}"/>'
    return out


def palnik(cx, y):
    return (f'<rect class="f2" x="{cx - 10}" y="{y}" width="20" height="34"/>'
            f'<rect class="f2" x="{cx - 22}" y="{y + 34}" width="44" height="8" rx="2"/>'
            f'<path class="s" d="M{cx} {y - 4} q-9 -14 0 -30 q9 16 0 30"/>')


def osie(x0=50, y0=255, w=320, h=220, ox='', oy=''):
    return (f'<path class="s" d="M{x0} {y0 - h} V{y0} H{x0 + w}"/>'
            f'<path class="d" d="M{x0 - 4} {y0 - h + 6} l4 -8 l4 8 z"/><path class="d" d="M{x0 + w - 6} {y0 - 4} l8 4 l-8 4 z"/>'
            f'<text class="t" x="{x0 + w - 60}" y="{y0 + 18}">{ox}</text><text class="t" x="{x0 - 44}" y="{y0 - h - 6}">{oy}</text>')


# ---------- zestawy laboratoryjne ----------
_destylacja = (
    kolba(90, 70, r=42, szyjka=46)
    + palnik(90, 225)
    + '<path class="s" d="M83 82 h-10 M97 82 h40"/>'  # nasadka
    + '<path class="s2" d="M90 60 v-22"/><rect class="f2" x="86" y="30" width="8" height="12"/>'  # termometr
    + '<path class="f" d="M137 74 L300 150 L294 162 L131 86 z"/>'  # chłodnica
    + '<path class="s" d="M150 78 L290 148"/>'
    + '<path class="s2" d="M180 75 v-18 M265 140 v26"/>'
    + zlewka(285, 175, w=70, h=70, poziom=0.35)
    + '<text class="t" x="168" y="52">woda ↓</text><text class="t" x="252" y="182">↑ woda</text>'
)
_destylacja_zn = [
    (90, 150, 30, 150, 'Kolba z mieszaniną', 'ciecz ogrzewana do wrzenia'),
    (90, 36, 40, 22, 'Termometr', 'zbiornik rtęci na wysokości bocznego odprowadzenia — mierzy temperaturę par'),
    (215, 115, 220, 92, 'Chłodnica', 'pary skraplają się; woda płynie przeciwprądowo (wpływa dołem)'),
    (320, 230, 370, 280, 'Odbieralnik', 'zbiera destylat — składnik o niższej temperaturze wrzenia'),
    (90, 205, 150, 270, 'Źródło ciepła', 'palnik lub czasza grzejna'),
]

_saczenie = (
    '<path class="s" d="M140 60 L260 60 L215 150 L185 150 z"/>'
    '<path class="dash" d="M150 66 L250 66 L210 144 L190 144 z"/>'
    '<path class="s" d="M193 150 v60 M207 150 v60"/>'
    + zlewka(150, 190, w=100, h=80, poziom=0.3)
    + '<path class="f2" d="M155 68 L245 68 L232 92 L168 92 z"/>'
    + '<path class="s2" d="M120 30 l40 30"/><text class="t" x="70" y="26">bagietka</text>'
)
_saczenie_zn = [
    (200, 80, 300, 70, 'Osad na sączku', 'substancja nierozpuszczalna zostaje na bibule'),
    (230, 120, 310, 120, 'Sączek z bibuły', 'złożony i zwilżony, przylega do lejka'),
    (200, 255, 300, 270, 'Przesącz', 'klarowny roztwór substancji rozpuszczonych'),
    (140, 60, 60, 80, 'Lejek', 'nóżka dotyka ścianki zlewki — ciecz spływa bez rozpryskiwania'),
]

_rozdzielacz = (
    '<path class="s" d="M170 40 h60 M175 40 C160 120 160 170 196 205 h8 C240 170 240 120 225 40"/>'
    '<path class="f" d="M168 120 C168 165 175 185 196 203 h8 C225 185 232 165 232 120 z"/>'
    '<path class="f2" d="M166 82 C164 100 165 112 168 120 h64 C235 112 236 100 234 82 z"/>'
    '<path class="s" d="M197 205 v40 M203 205 v40"/><rect class="d" x="186" y="220" width="28" height="6" rx="2"/>'
    '<rect class="f2" x="187" y="30" width="26" height="10" rx="2"/>'
)
_rozdzielacz_zn = [
    (200, 100, 300, 90, 'Warstwa górna', 'ciecz o mniejszej gęstości, np. benzyna lub eter'),
    (200, 160, 300, 160, 'Warstwa dolna', 'ciecz o większej gęstości, np. woda lub CCl₄'),
    (200, 223, 300, 230, 'Kran', 'spuszcza się nim dolną warstwę'),
    (200, 35, 300, 30, 'Korek', 'zdejmuje się go przed otwarciem kranu'),
]

_gaz = (
    '<path class="s" d="M60 60 h40 M65 60 v120 a15 15 0 0 0 30 0 v-120"/>'  # probówka
    '<path class="f" d="M66 140 v40 a14 14 0 0 0 28 0 v-40 z"/>'
    '<path class="s" d="M80 60 v-20 h150 v170"/>'  # rurka
    + zlewka(180, 160, w=140, h=100, poziom=0.7)
    + '<path class="s" d="M215 120 v110 a8 8 0 0 0 16 0 v-110"/>'  # odwrócona probówka
    + '<path class="f" d="M216 170 v60 a7 7 0 0 0 14 0 v-60 z"/>'
    + palnik(80, 220)
)
_gaz_zn = [
    (80, 160, 20, 150, 'Probówka z substratami', 'ogrzewana mieszanina, np. KMnO₄ lub KClO₃ z MnO₂'),
    (223, 140, 300, 110, 'Gaz zebrany nad wodą', 'metoda dla gazów słabo rozpuszczalnych w wodzie (O₂, H₂, N₂)'),
    (260, 230, 360, 280, 'Wanna z wodą', 'gaz wypiera wodę z odwróconej probówki'),
    (155, 40, 150, 20, 'Rurka odprowadzająca', 'po zakończeniu najpierw wyjmuje się ją z wody, potem gasi palnik'),
]

_miareczkowanie = (
    '<path class="s" d="M190 20 v170 M210 20 v170"/>'
    '<rect class="f" x="191" y="60" width="18" height="130"/>'
    + ''.join(f'<path class="s2" d="M191 {y} h8"/>' for y in range(70, 190, 12))
    + '<path class="s" d="M195 190 v20 h10 v-20"/><rect class="d" x="183" y="196" width="34" height="5" rx="2"/>'
    '<path class="s" d="M196 210 l2 14 h4 l2 -14"/>'
    '<path class="s" d="M185 232 h30 M188 232 v10 L150 285 h100 L212 242 v-10"/>'
    '<path class="f" d="M162 272 L238 272 L250 285 L150 285 z"/>'
    '<path class="s" d="M100 290 h200 M120 20 v270 M120 40 h70"/><rect class="f2" x="100" y="286" width="60" height="6"/>'
)
_miareczkowanie_zn = [
    (200, 120, 290, 100, 'Biureta z titrantem', 'roztwór o znanym stężeniu; odczyt z dokładnością do 0,05 cm³'),
    (200, 198, 290, 190, 'Kranik', 'pozwala dodawać titrant kroplami'),
    (200, 278, 300, 270, 'Kolba stożkowa z analitem', 'odmierzona pipetą objętość i kilka kropli wskaźnika'),
    (120, 160, 50, 150, 'Statyw', 'utrzymuje biuretę w pionie'),
]

# ---------- wykresy ----------
_krzywa = (
    osie(ox='V titranta', oy='pH')
    + '<path class="s" d="M50 210 C120 205 175 200 195 190 C205 185 208 170 210 130 C212 90 215 75 225 70 C260 62 320 60 370 58"/>'
    + '<path class="dash" d="M210 130 V255 M50 130 H210"/>'
    + '<text class="t" x="20" y="134">7</text><text class="t" x="200" y="270">Vₑ</text>'
    + '<text class="t" x="20" y="214">1</text><text class="t" x="20" y="62">13</text>'
)
_krzywa_zn = [
    (90, 208, 90, 250, 'Nadmiar kwasu', 'pH rośnie powoli'),
    (210, 130, 280, 140, 'Punkt równoważnikowy', 'mocny kwas + mocna zasada: pH = 7'),
    (209, 170, 150, 110, 'Skok pH', 'wskaźnik musi zmieniać barwę w tym zakresie (np. fenoloftaleina)'),
    (320, 60, 340, 100, 'Nadmiar zasady', 'pH dąży do pH titranta'),
]

_krzywa_slaby = (
    osie(ox='V NaOH', oy='pH')
    + '<path class="s" d="M50 190 C70 160 90 150 130 145 C170 140 200 130 215 115 C222 100 224 80 230 70 C260 62 320 60 370 58"/>'
    + '<path class="dash" d="M130 145 V255 M50 145 H130 M220 92 V255"/>'
    + '<text class="t" x="16" y="149">pKa</text><text class="t" x="118" y="270">½Vₑ</text><text class="t" x="212" y="270">Vₑ</text>'
)
_krzywa_slaby_zn = [
    (130, 145, 100, 110, 'Obszar buforowy', 'mieszanina CH₃COOH/CH₃COO⁻ — pH zmienia się wolno'),
    (130, 145, 150, 200, 'Połowa zobojętnienia', 'pH = pKa'),
    (220, 92, 290, 120, 'Punkt równoważnikowy', 'pH > 7 — hydroliza anionu słabego kwasu'),
    (50, 190, 70, 230, 'Początek', 'pH słabego kwasu wyższe niż mocnego o tym samym stężeniu'),
]

_energ_egzo = (
    osie(ox='przebieg reakcji', oy='energia')
    + '<path class="s" d="M60 110 H110 C150 110 160 50 190 50 C220 50 230 170 270 170 H360"/>'
    + '<path class="s2" d="M85 110 V50 M85 54 l-3 6 h6 z"/>'
    + '<path class="s2" d="M330 110 V170 M330 166 l-3 -6 h6 z"/><path class="dash" d="M110 110 H340"/>'
)
_energ_egzo_zn = [
    (80, 110, 60, 140, 'Substraty', 'wyższa entalpia'),
    (190, 50, 190, 25, 'Kompleks aktywny', 'stan przejściowy na szczycie bariery'),
    (85, 80, 30, 80, 'Energia aktywacji Eₐ', 'katalizator ją obniża, ΔH się nie zmienia'),
    (300, 170, 300, 205, 'Produkty', 'niższa entalpia'),
    (330, 140, 375, 140, 'ΔH < 0', 'reakcja egzotermiczna — ciepło oddawane do otoczenia'),
]

_energ_endo = (
    osie(ox='przebieg reakcji', oy='energia')
    + '<path class="s" d="M60 190 H110 C150 190 160 60 190 60 C220 60 230 120 270 120 H360"/>'
    + '<path class="dash" d="M60 190 C150 190 170 110 190 110 C215 110 235 120 270 120"/>'
    + '<path class="dash" d="M110 190 H340"/><path class="s2" d="M330 190 V120 M330 124 l-3 6 h6 z"/>'
)
_energ_endo_zn = [
    (80, 190, 60, 220, 'Substraty', 'niższa entalpia'),
    (190, 60, 190, 30, 'Bariera bez katalizatora', 'wyższa energia aktywacji'),
    (190, 110, 130, 95, 'Bariera z katalizatorem', 'niższa energia aktywacji, inna droga reakcji'),
    (300, 120, 300, 100, 'Produkty', 'wyższa entalpia'),
    (330, 155, 375, 165, 'ΔH > 0', 'reakcja endotermiczna — ciepło pobierane'),
]

_rozp = (
    osie(ox='temperatura, °C', oy='g/100 g wody')
    + '<path class="s" d="M50 200 C150 185 250 120 370 40"/>'
    + '<path class="s" d="M50 150 C150 148 250 146 370 144"/>'
    + '<path class="s2" d="M50 120 C150 170 250 205 370 225"/>'
    + '<circle class="d" cx="250" cy="120" r="4"/><circle class="d" cx="250" cy="180" r="3"/>'
    + '<path class="dash" d="M250 120 V255"/>'
)
_rozp_zn = [
    (330, 70, 330, 30, 'KNO₃', 'rozpuszczalność silnie rośnie z temperaturą'),
    (330, 145, 340, 165, 'NaCl', 'rozpuszczalność prawie stała'),
    (330, 221, 330, 245, 'Gaz (np. CO₂)', 'rozpuszczalność gazów maleje z temperaturą'),
    (250, 120, 200, 70, 'Punkt na krzywej', 'roztwór nasycony'),
    (250, 180, 200, 200, 'Punkt pod krzywą', 'roztwór nienasycony'),
]

_ogniwo = (
    zlewka(40, 140, w=110, h=100, poziom=0.7) + zlewka(250, 140, w=110, h=100, poziom=0.7)
    + '<rect class="f2" x="80" y="100" width="18" height="120"/><rect class="f" x="300" y="100" width="18" height="120"/>'
    + '<path class="s" d="M89 100 V40 H309 V100"/><circle class="f" cx="199" cy="40" r="16"/>'
    + '<text class="t" x="193" y="44">V</text>'
    + '<path class="s" d="M120 175 V120 H280 V175 M135 175 V135 H265 V175"/>'
    + '<text class="t" x="60" y="90">anoda (−)</text><text class="t" x="300" y="90">katoda (+)</text>'
    + '<text class="t" x="130" y="28">e⁻ →</text>'
)
_ogniwo_zn = [
    (89, 190, 30, 270, 'Anoda: Zn', 'utlenianie: Zn → Zn²⁺ + 2e⁻; masa maleje'),
    (95, 230, 120, 280, 'Roztwór ZnSO₄', 'rośnie stężenie Zn²⁺'),
    (309, 190, 370, 270, 'Katoda: Cu', 'redukcja: Cu²⁺ + 2e⁻ → Cu; masa rośnie'),
    (305, 230, 280, 280, 'Roztwór CuSO₄', 'maleje stężenie Cu²⁺, barwa słabnie'),
    (200, 125, 200, 160, 'Klucz elektrolityczny', 'np. KNO₃ — zamyka obwód, wyrównuje ładunki'),
    (199, 40, 250, 18, 'Woltomierz', 'SEM = E°(katody) − E°(anody) = 0,34 − (−0,76) = 1,10 V'),
]

_elektroliza = (
    zlewka(90, 120, w=220, h=140, poziom=0.75)
    + '<rect class="f2" x="140" y="80" width="14" height="150"/><rect class="f2" x="246" y="80" width="14" height="150"/>'
    + '<path class="s" d="M147 80 V40 H175 M225 40 H253 V80"/><path class="s" d="M175 30 v20 M185 36 v8 M215 30 v20 M225 36 v8"/>'
    + '<path class="s" d="M185 40 H215"/>'
    + '<text class="t" x="164" y="24">−</text><text class="t" x="218" y="24">+</text>'
    + ''.join(f'<circle class="s2" cx="{x}" cy="{y}" r="3"/>' for x, y in ((136, 200), (159, 180), (138, 160), (241, 205), (264, 175), (243, 150)))
)
_elektroliza_zn = [
    (147, 190, 50, 190, 'Katoda (−)', 'redukcja; w roztworze NaCl: 2H₂O + 2e⁻ → H₂ + 2OH⁻'),
    (253, 190, 350, 190, 'Anoda (+)', 'utlenianie; 2Cl⁻ → Cl₂ + 2e⁻'),
    (200, 230, 200, 285, 'Elektrolit', 'wodny roztwór NaCl; przy katodzie odczyn zasadowy'),
    (200, 35, 280, 18, 'Źródło prądu stałego', 'wymusza reakcję niesamorzutną'),
]

S['c-doswiadczenia'] = [
    dict(typ='rysunek', tytul='Destylacja prosta', svg=_destylacja, znaczniki=_destylacja_zn,
         opis='Zestaw do rozdzielania cieczy o różnych temperaturach wrzenia.',
         uwaga='Typowe pytania: gdzie umieścić termometr, którędy wpływa woda do chłodnicy, który składnik jest w destylacie.'),
    dict(typ='rysunek', tytul='Sączenie', svg=_saczenie, znaczniki=_saczenie_zn,
         opis='Oddzielanie osadu od roztworu.',
         uwaga='Sączenie rozdziela mieszaninę niejednorodną ciało stałe–ciecz. Roztwór nie da się „przesączyć” na składniki.'),
    dict(typ='rysunek', tytul='Rozdzielacz', svg=_rozdzielacz, znaczniki=_rozdzielacz_zn,
         opis='Rozdzielanie dwóch niemieszających się cieczy.',
         uwaga='O tym, która warstwa jest na dole, decyduje gęstość, a nie polarność.'),
    dict(typ='rysunek', tytul='Zbieranie gazu nad wodą', svg=_gaz, znaczniki=_gaz_zn,
         opis='Otrzymywanie i zbieranie gazu słabo rozpuszczalnego w wodzie.',
         uwaga='NH₃ i HCl zbiera się wyłącznie „na sucho” (bardzo dobrze rozpuszczalne). Przy wypieraniu powietrza naczynie trzyma się wylotem w dół dla gazów lżejszych od powietrza (H₂, NH₃), a wylotem w górę dla cięższych (CO₂, Cl₂).'),
    dict(typ='rysunek', tytul='Zestaw do miareczkowania', svg=_miareczkowanie, znaczniki=_miareczkowanie_zn,
         opis='Oznaczanie stężenia analitu titrantem o znanym stężeniu.'),
]
S['c-ph'] = [
    dict(typ='rysunek', tytul='Krzywa miareczkowania mocnego kwasu mocną zasadą', svg=_krzywa, znaczniki=_krzywa_zn,
         opis='pH roztworu HCl w zależności od objętości dodanego NaOH.',
         uwaga='Objętość w punkcie równoważnikowym: n(HCl) = n(NaOH). Szeroki skok pH — pasuje zarówno oranż metylowy, jak i fenoloftaleina.'),
    dict(typ='rysunek', tytul='Krzywa miareczkowania słabego kwasu mocną zasadą', svg=_krzywa_slaby, znaczniki=_krzywa_slaby_zn,
         opis='pH roztworu CH₃COOH w zależności od objętości dodanego NaOH.',
         uwaga='Punkt równoważnikowy przy pH > 7 — wskaźnikiem jest fenoloftaleina, nie oranż metylowy.'),
]
S['c-energetyka'] = [
    dict(typ='rysunek', tytul='Wykres energetyczny reakcji egzotermicznej', svg=_energ_egzo, znaczniki=_energ_egzo_zn,
         opis='Zmiana energii układu w trakcie reakcji.'),
]
S['c-szybkosc'] = [
    dict(typ='rysunek', tytul='Działanie katalizatora na wykresie energetycznym', svg=_energ_endo, znaczniki=_energ_endo_zn,
         opis='Reakcja endotermiczna z katalizatorem i bez niego.',
         uwaga='Katalizator nie zmienia ΔH ani stałej równowagi — przyspiesza osiągnięcie stanu równowagi.'),
]
S['c-rozpuszczalnosc'] = [
    dict(typ='rysunek', tytul='Krzywe rozpuszczalności', svg=_rozp, znaczniki=_rozp_zn,
         opis='Rozpuszczalność substancji w wodzie w zależności od temperatury (przebieg poglądowy).',
         uwaga='Z krzywej odczytujesz masę substancji w 100 g wody. Masa roztworu nasyconego = 100 g + rozpuszczalność.'),
]
S['c-ogniwa'] = [
    dict(typ='rysunek', tytul='Ogniwo Daniella', svg=_ogniwo, znaczniki=_ogniwo_zn,
         opis='Ogniwo cynkowo-miedziowe: Zn | Zn²⁺ || Cu²⁺ | Cu.',
         uwaga='W ogniwie anoda jest ujemna, w elektrolizerze — dodatnia. W obu przypadkach na anodzie zachodzi utlenianie.'),
]
S['c-elektroliza'] = [
    dict(typ='rysunek', tytul='Elektroliza wodnego roztworu NaCl', svg=_elektroliza, znaczniki=_elektroliza_zn,
         opis='Elektrolizer z elektrodami grafitowymi.',
         uwaga='Kationy Na⁺ (metale aktywne) nie redukują się w roztworze wodnym — zamiast nich redukuje się woda.'),
]
