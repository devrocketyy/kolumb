# Schematy chemii — porcja 3: budowa atomu i cząsteczek, diagram fazowy, ogrzewanie wody (rysunki autorskie).
S = {}


def atom(x, y, r=7, cls='f2'):
    return f'<circle class="{cls}" cx="{x}" cy="{y}" r="{r}"/>'


def wiaz(x1, y1, x2, y2, cls='s'):
    return f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'


# ---------- orbitale ----------
def plat(cx, cy, dx, dy, rx=26, ry=11, rot=0):
    return f'<ellipse class="f" cx="{cx + dx}" cy="{cy + dy}" rx="{rx}" ry="{ry}" transform="rotate({rot} {cx + dx} {cy + dy})"/>'


_orb = (
    '<circle class="f" cx="70" cy="150" r="34"/>'
    + plat(200, 150, 0, -30, rx=11, ry=28) + plat(200, 150, 0, 30, rx=11, ry=28)
    + plat(330, 150, 24, -24, rx=26, ry=10, rot=-45) + plat(330, 150, -24, 24, rx=26, ry=10, rot=-45)
    + plat(330, 150, -24, -24, rx=26, ry=10, rot=45) + plat(330, 150, 24, 24, rx=26, ry=10, rot=45)
    + ''.join(atom(x, 150, 2.5, 'd') for x in (70, 200, 330))
    + '<path class="dash" d="M200 90 V210 M140 150 H260"/>'
    + '<text class="t" x="196" y="84">z</text>'
)
_orb_zn = [
    (70, 150, 70, 240, 'Orbital s', 'kulisty; l = 0, jeden na powłokę'),
    (200, 120, 200, 240, 'Orbital p', 'dwa „płaty”; l = 1, trzy orbitale px, py, pz'),
    (330, 150, 330, 240, 'Orbital d', 'cztery płaty (większość); l = 2, pięć orbitali'),
    (200, 150, 260, 60, 'Płaszczyzna węzłowa', 'prawdopodobieństwo znalezienia elektronu równe zeru'),
]

# ---------- kształty cząsteczek ----------
_ksz = (
    # liniowa CO2
    atom(30, 70) + atom(60, 70, 9, 'f') + atom(90, 70) + wiaz(37, 67, 51, 67) + wiaz(37, 73, 51, 73) + wiaz(69, 67, 83, 67) + wiaz(69, 73, 83, 73)
    # trójkątna BF3
    + atom(200, 70, 9, 'f') + wiaz(200, 61, 200, 32) + wiaz(192, 75, 166, 92) + wiaz(208, 75, 234, 92)
    + atom(200, 28) + atom(162, 94) + atom(238, 94)
    # tetraedr CH4
    + atom(330, 70, 9, 'f') + wiaz(330, 61, 330, 30) + wiaz(322, 74, 298, 92) + wiaz(338, 74, 362, 92)
    + '<path class="dash" d="M330 79 L340 108"/>' + atom(330, 26, 5) + atom(295, 94, 5) + atom(365, 94, 5) + atom(342, 112, 5)
    # piramida NH3
    + atom(90, 200, 9, 'f') + wiaz(83, 206, 60, 230) + wiaz(97, 206, 120, 230) + '<path class="dash" d="M90 209 L95 240"/>'
    + atom(57, 233, 5) + atom(123, 233, 5) + atom(96, 244, 5)
    + '<ellipse class="s2" cx="90" cy="176" rx="7" ry="12"/>'
    # kątowa H2O
    + atom(280, 200, 9, 'f') + wiaz(273, 206, 250, 230) + wiaz(287, 206, 310, 230) + atom(247, 233, 5) + atom(313, 233, 5)
    + '<ellipse class="s2" cx="270" cy="178" rx="6" ry="11" transform="rotate(-20 270 178)"/>'
    + '<ellipse class="s2" cx="290" cy="178" rx="6" ry="11" transform="rotate(20 290 178)"/>'
)
_ksz_zn = [
    (60, 70, 60, 120, 'Liniowa (CO₂)', 'sp, kąt 180°, 2 obszary elektronowe'),
    (200, 70, 200, 130, 'Trójkątna płaska (BF₃)', 'sp², kąt 120°'),
    (330, 70, 330, 140, 'Tetraedryczna (CH₄)', 'sp³, kąt 109,5°'),
    (90, 200, 30, 280, 'Piramida trygonalna (NH₃)', 'sp³ z 1 wolną parą, kąt ok. 107°'),
    (280, 200, 340, 280, 'Kątowa (H₂O)', 'sp³ z 2 wolnymi parami, kąt ok. 104,5°'),
]

# ---------- diagram fazowy ----------
_faz = (
    '<path class="s" d="M50 35 V255 H370"/>'
    '<text class="t" x="300" y="275">temperatura</text><text class="t" x="8" y="30">ciśnienie</text>'
    '<path class="s" d="M60 250 C120 230 150 190 180 170"/>'  # sublimacja
    '<path class="s" d="M180 170 C185 120 195 80 205 40"/>'   # topnienie
    '<path class="s" d="M180 170 C230 150 290 110 330 70"/>'  # wrzenie
    '<circle class="d" cx="180" cy="170" r="4"/><circle class="d" cx="330" cy="70" r="4"/>'
    '<text class="t" x="95" y="120">ciało stałe</text><text class="t" x="230" y="70">ciecz</text><text class="t" x="250" y="205">gaz</text>'
)
_faz_zn = [
    (180, 170, 120, 200, 'Punkt potrójny', 'współistnieją wszystkie trzy fazy'),
    (330, 70, 365, 105, 'Punkt krytyczny', 'powyżej niego nie da się odróżnić cieczy od gazu'),
    (120, 222, 150, 245, 'Krzywa sublimacji', 'równowaga ciało stałe ⇄ gaz'),
    (194, 100, 160, 60, 'Krzywa topnienia', 'równowaga ciało stałe ⇄ ciecz'),
    (260, 128, 300, 150, 'Krzywa wrzenia', 'równowaga ciecz ⇄ gaz'),
]

# ---------- krzywa ogrzewania ----------
_ogrz = (
    '<path class="s" d="M50 35 V255 H370"/>'
    '<text class="t" x="290" y="275">czas ogrzewania</text><text class="t" x="8" y="30">t, °C</text>'
    '<path class="s" d="M55 240 L100 200 H170 L230 110 H320 L360 60"/>'
    '<path class="dash" d="M50 200 H100 M50 110 H230"/>'
    '<text class="t" x="28" y="204">0</text><text class="t" x="20" y="114">100</text>'
)
_ogrz_zn = [
    (78, 220, 40, 250, 'Ogrzewanie lodu', 'rośnie temperatura ciała stałego'),
    (135, 200, 135, 230, 'Topnienie', 'temperatura stała — energia idzie na zrywanie sieci'),
    (200, 155, 160, 140, 'Ogrzewanie wody', 'rośnie temperatura cieczy'),
    (275, 110, 275, 140, 'Wrzenie', 'temperatura stała — dłuższy odcinek niż topnienie'),
    (340, 85, 370, 120, 'Ogrzewanie pary', ''),
]

S['c-konfiguracja'] = [
    dict(typ='rysunek', tytul='Kształty orbitali s, p i d', svg=_orb, znaczniki=_orb_zn,
         opis='Kontury obszarów, w których prawdopodobieństwo znalezienia elektronu jest największe.',
         uwaga='Orbital nie jest torem elektronu. Na każdym orbitalu mieszczą się najwyżej 2 elektrony o przeciwnych spinach.'),
]
S['c-geometria'] = [
    dict(typ='rysunek', tytul='Kształty cząsteczek (VSEPR)', svg=_ksz, znaczniki=_ksz_zn,
         opis='Najczęstsze kształty cząsteczek na maturze. Owalami zaznaczono wolne pary elektronowe.',
         uwaga='Hybrydyzacja NH₃ i H₂O to sp³, ale kształtu nie nazywa się tetraedrem — opisujesz położenie atomów, nie wolnych par.'),
]
S['c-oddzialywania'] = [
    dict(typ='rysunek', tytul='Diagram fazowy', svg=_faz, znaczniki=_faz_zn,
         opis='Ogólny diagram fazowy substancji (przebieg poglądowy).',
         uwaga='Dla wody krzywa topnienia jest nachylona w lewo (lód ma mniejszą gęstość niż woda). Dla CO₂ punkt potrójny leży powyżej 1 atm — dlatego suchy lód sublimuje.'),
    dict(typ='rysunek', tytul='Krzywa ogrzewania wody', svg=_ogrz, znaczniki=_ogrz_zn,
         opis='Temperatura próbki lodu ogrzewanej ze stałą mocą.',
         uwaga='Podczas przemian fazowych temperatura się nie zmienia. Odcinek wrzenia jest dłuższy, bo ciepło parowania wody jest dużo większe niż ciepło topnienia.'),
]

P = lambda tytul, kroki, opis='', uwaga='': dict(typ='proces', tytul=tytul, kroki=kroki, opis=opis, **({'uwaga': uwaga} if uwaga else {}))

S['c-metale'] = [
    P('Szereg aktywności metali (wybrane)', [
        ('K, Ca, Na', 'reagują z wodą na zimno'),
        ('Mg, Al, Zn, Fe', 'wypierają wodór z kwasów nieutleniających'),
        ('H', 'punkt odniesienia (E° = 0 V)'),
        ('Cu, Hg, Ag', 'nie wypierają wodoru; roztwarzają się w kwasach utleniających'),
        ('Au, Pt', 'tylko woda królewska'),
    ], 'Metal stojący wyżej wypiera z roztworów soli metale stojące niżej.'),
]
S['c-niemetale'] = [
    P('Wykrywanie gazów w laboratorium', [
        ('O₂', 'rozżarzone łuczywo zapala się'),
        ('H₂', 'zapalony — charakterystyczny dźwięk (mieszanina piorunująca)'),
        ('CO₂', 'woda wapienna mętnieje'),
        ('NH₃', 'wilgotny papierek uniwersalny barwi się na niebiesko'),
        ('Cl₂', 'wilgotny papierek jodoskrobiowy granatowieje'),
        ('SO₂', 'odbarwia roztwór KMnO₄ i wodę bromową'),
    ]),
]
S['c-ogniwa'] = [
    P('Ustalanie anody i katody w ogniwie', [
        ('Odczytaj potencjały standardowe', 'z karty wzorów CKE'),
        ('Niższy potencjał', 'anoda, biegun ujemny, utlenianie'),
        ('Wyższy potencjał', 'katoda, biegun dodatni, redukcja'),
        ('SEM', 'E°(katody) − E°(anody), zawsze dodatnia'),
        ('Schemat ogniwa', 'anoda | jon anody || jon katody | katoda'),
    ]),
]
S['c-areny'] = [
    P('Kierowanie podstawników w pierścieniu benzenu', [
        ('Podstawniki I rodzaju', '–OH, –NH₂, –CH₃, fluorowce — kierują w orto i para'),
        ('Podstawniki II rodzaju', '–NO₂, –COOH, –CHO, –SO₃H — kierują w meta'),
        ('Aktywacja', '–OH i –NH₂ ułatwiają substytucję (fenol reaguje z wodą bromową bez katalizatora)'),
        ('Dezaktywacja', '–NO₂ utrudnia kolejną substytucję'),
    ]),
]
S['c-karbonylowe'] = [
    P('Odróżnianie aldehydów i ketonów', [
        ('Próba Tollensa', 'aldehyd: lustro srebrne; keton: brak zmian'),
        ('Próba Trommera', 'aldehyd: ceglasty osad Cu₂O; keton: brak'),
        ('Próba jodoformowa', 'żółty osad CHI₃ — metyloketony, etanal i etanol'),
        ('Utlenianie K₂Cr₂O₇', 'aldehyd utlenia się do kwasu, keton nie'),
    ]),
]
S['c-karboksylowe'] = [
    P('Porównanie mocy kwasów — doświadczenie', [
        ('Kwas mocniejszy + sól słabszego kwasu', 'wypiera słabszy kwas'),
        ('HCl + CH₃COONa', 'zapach octu'),
        ('CH₃COOH + NaHCO₃', 'wydziela się CO₂'),
        ('CO₂ + fenolan sodu', 'zmętnienie — wydziela się fenol'),
        ('Wniosek', 'HCl > CH₃COOH > H₂CO₃ > C₆H₅OH'),
    ]),
]
S['c-aminy'] = [
    P('Hydroliza amidów', [
        ('Środowisko kwasowe', 'RCONH₂ + H₂O + H⁺ → RCOOH + NH₄⁺'),
        ('Środowisko zasadowe', 'RCONH₂ + OH⁻ → RCOO⁻ + NH₃↑'),
        ('Mocznik w kwasie', 'CO(NH₂)₂ + H₂O + 2H⁺ → CO₂↑ + 2NH₄⁺'),
        ('Mocznik w zasadzie', 'CO(NH₂)₂ + 2OH⁻ → CO₃²⁻ + 2NH₃↑'),
    ]),
]
S['c-srodowisko'] = [
    P('Kwaśne deszcze — powstawanie', [
        ('Spalanie paliw z siarką', 'S + O₂ → SO₂'),
        ('Utlenianie w atmosferze', '2SO₂ + O₂ → 2SO₃'),
        ('Reakcja z wodą', 'SO₃ + H₂O → H₂SO₄'),
        ('Tlenki azotu', 'NO₂ z wodą i tlenem → HNO₃'),
        ('Skutki', 'zakwaszenie gleb i wód, niszczenie budowli z wapienia'),
    ]),
]
