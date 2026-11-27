# Schematy geografii — porcja 22 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Struktura zatrudnienia w Polsce 1989 i 2023 ----------
_d = {'1989': (28.6, 35.7, 35.7), '2023': (8.1, 28.0, 63.9)}
_z = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
y0 = 250
for i, (rok, (a, b, c)) in enumerate(_d.items()):
    x = 90 + i * 150
    yy = y0
    for v, cls in ((a, 'gt'), (b, 'gs2'), (c, 'gw2')):
        h = v * 2
        _z += f'<rect class="{cls} ol" x="{x}" y="{yy - h:.0f}" width="80" height="{h:.0f}"/>'
        _z += f'<text class="tb" x="{x + 40}" y="{yy - h / 2 + 4:.0f}" text-anchor="middle">{str(v).replace(".", ",")}%</text>'
        yy -= h
    _z += f'<text class="tb" x="{x + 40}" y="{y0 + 18}" text-anchor="middle">{rok}</text>'
_z += f'<path class="s" d="M60 {y0} H360"/>'
_z += '<rect class="gt ol" x="20" y="270" width="12" height="10"/><text class="ts" x="36" y="279">rolnictwo</text>'
_z += '<rect class="gs2 ol" x="130" y="270" width="12" height="10"/><text class="ts" x="146" y="279">przemysł i budownictwo</text>'
_z += '<rect class="gw2 ol" x="290" y="270" width="12" height="10"/><text class="ts" x="306" y="279">usługi</text>'
S['g-pl-gospodarka'] = [
 dict(typ='rysunek', tytul='Struktura pracujących w Polsce: 1989 i 2023', svg=_z,
      znaczniki=[(130, 221, 30, 200, 'Spadek w rolnictwie', 'Z 28,6% do 8,1% — modernizacja i scalanie gospodarstw'),
                 (280, 90, 340, 60, 'Wzrost usług', 'Z 35,7% do 63,9% — finanse, handel, IT, usługi biznesowe'),
                 (280, 175, 370, 150, 'Przemysł', 'Spadek po restrukturyzacji lat 90., potem stabilizacja ok. 28%')],
      opis='Udział pracujących według sektorów (dane przybliżone wg GUS, jak w arkuszu CKE maj 2026) — wykres autorski IndexLab.',
      uwaga='Przemiany po 1989 r.: gospodarka rynkowa, prywatyzacja i inwestycje zagraniczne przesunęły zatrudnienie z rolnictwa i ciężkiego przemysłu do usług — typowa droga kraju doganiającego wysoko rozwinięte.'),
]

# ---------- 2. Korytarze transportowe Polski ----------
_k = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
_k += '<path class="gl ol" d="M60 40 C150 20 250 25 330 40 C360 90 370 160 340 220 C300 270 120 280 70 240 C40 190 35 100 60 40 Z"/>'
_k += '<path class="hot" d="M180 30 L190 150 L200 270" style="stroke-width:3"/>'           # A1
_k += '<path class="hot" d="M60 135 L200 150 L340 150" style="stroke-width:3"/>'           # A2
_k += '<path class="cold" d="M200 150 L300 70 L330 45" style="stroke-width:2.5;stroke-dasharray:6 4"/>'  # S61
_k += '<path class="cold" d="M320 90 L320 160 L300 250" style="stroke-width:2.5;stroke-dasharray:6 4"/>'  # S19
_k += '<path class="hot" d="M70 230 L200 250 L330 225" style="stroke-width:3"/>'           # A4
for x, y, n in ((185, 38, 'Gdańsk'), (200, 150, 'Łódź/Warszawa'), (200, 262, 'Śląsk'), (70, 138, 'Świecko'), (335, 225, 'Rzeszów')):
    _k += f'<circle class="d" cx="{x}" cy="{y}" r="4"/>'
S['g-uslugi'] = [
 dict(typ='rysunek', tytul='Główne korytarze transportowe Polski (schemat)', svg=_k,
      znaczniki=[(188, 90, 110, 70, 'Autostrada A1', 'Północ–południe: Gdańsk–Łódź–Śląsk (korytarz Bałtyk–Adriatyk)'),
                 (120, 142, 90, 175, 'Autostrada A2', 'Zachód–wschód: Świecko–Poznań–Warszawa'),
                 (260, 102, 240, 35, 'Via Baltica (S61)', 'Do Litwy i państw bałtyckich'),
                 (320, 125, 360, 105, 'Via Carpatia (S19)', 'Wschodnia Polska: Białystok–Lublin–Rzeszów'),
                 (130, 241, 120, 210, 'Autostrada A4', 'Południe: Zgorzelec–Wrocław–Katowice–Kraków–Rzeszów')],
      opis='Uproszczony schemat najważniejszych korytarzy drogowych Polski (bez skali) — rysunek autorski IndexLab.',
      uwaga='Polska leży na skrzyżowaniu korytarzy TEN-T: Morze Północne–Bałtyk (E–W) i Bałtyk–Adriatyk (N–S). Położenie tranzytowe sprzyja rozwojowi logistyki (centra magazynowe przy węzłach autostrad, np. w okolicach Łodzi i Strykowa).'),
]

# ---------- 3. Wiatry lokalne Europy (schemat) ----------
_e = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
_e += '<path class="gl ol" d="M0 0 H400 V120 C350 130 320 150 300 170 C280 160 260 150 250 170 C240 200 220 210 200 190 C180 160 160 150 140 170 C120 190 80 175 60 160 C40 150 20 160 0 165 Z"/>'
_e += '<path class="gp ol" d="M0 250 C100 235 300 235 400 250 V300 H0 Z"/>'
_e += strz(140, 60, 150, 150, 'cold') + strz(255, 100, 265, 155, 'cold') + strz(200, 245, 210, 205, 'hot')
_e += '<text class="ts" x="200" y="290" text-anchor="middle">Afryka Północna (Sahara)</text><text class="ts" x="200" y="20" text-anchor="middle">Europa</text>'
S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Wiatry lokalne basenu Morza Śródziemnego (schemat)', svg=_e,
      znaczniki=[(145, 100, 60, 100, 'Mistral', 'Zimny wiatr N doliną Rodanu nad Zatokę Lwią'),
                 (260, 130, 340, 100, 'Bora', 'Zimny, porywisty wiatr z gór nad Adriatyk'),
                 (205, 225, 280, 215, 'Sirocco', 'Gorący, pylisty wiatr z Sahary nad Włochy i Maltę')],
      opis='Uproszczony schemat wiatrów lokalnych nad Morzem Śródziemnym (bez skali) — rysunek autorski IndexLab.',
      uwaga='Wiatry lokalne powstają przez różnice ciśnienia między lądem a morzem i przez rzeźbę: zimne masy spływają z gór (mistral, bora), a gorące powietrze z pustyni napływa przed niżami (sirocco).'),
]

# ---------- 4. Wodospad i erozja wsteczna ----------
_f = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_f += '<path class="gs ol" d="M0 110 H210 V300 H0 Z"/>'                                  # twarda skała
_f += '<path class="gc ol" d="M0 140 H195 C190 170 200 210 230 230 H400 V300 H0 Z"/>'      # miękka skała niżej
_f += '<path class="gs ol" d="M0 110 H210 V140 H0 Z"/>'
_f += '<path class="cold" d="M0 105 H210 C220 140 225 200 230 225 H400" style="fill:none;stroke-width:4"/>'
_f += '<ellipse class="gw ol" cx="245" cy="230" rx="25" ry="8"/>'
_f += strz(260, 70, 200, 70, 'hot')
_f += '<text class="ts" x="270" y="74">cofanie się progu</text>'
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Wodospad i erozja wsteczna (przekrój)', svg=_f,
      znaczniki=[(100, 125, 80, 60, 'Twarda skała', 'Odporna warstwa tworzy krawędź progu'),
                 (100, 200, 60, 250, 'Miękka skała', 'Łatwo wymywana pod twardą warstwą'),
                 (245, 230, 320, 285, 'Kocioł eworsyjny', 'Zagłębienie wybite przez spadającą wodę i okruchy'),
                 (205, 170, 300, 150, 'Podcięcie progu', 'Woda wymywa miękką skałę — nawis twardej warstwy się obrywa')],
      opis='Przekrój przez wodospad na granicy skał odpornych i nieodpornych — rysunek autorski IndexLab.',
      uwaga='Erozja wsteczna przesuwa wodospad w górę doliny. Niagara cofa się nawet o ok. 1 m rocznie (dziś mniej dzięki regulacji przepływu). W Polsce progi skalne tworzą m.in. szumy na Roztoczu i wodospady w Tatrach.'),
]

# ---------- 5. Struktura religijna świata ----------
_r = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_dane = [('chrześcijaństwo', 31, 'gw2'), ('islam', 25, 'gt'), ('bez wyznania', 16, 'gs2'), ('hinduizm', 15, 'hotf'), ('buddyzm', 7, 'gp'), ('inne', 6, 'gc')]
cx, cy, R = 150, 150, 110
a0 = -90
for n, v, cls in _dane:
    a1 = a0 + v * 3.6
    x0, y0_ = cx + R * math.cos(math.radians(a0)), cy + R * math.sin(math.radians(a0))
    x1, y1_ = cx + R * math.cos(math.radians(a1)), cy + R * math.sin(math.radians(a1))
    big = 1 if a1 - a0 > 180 else 0
    _r += f'<path class="{cls} ol" d="M{cx} {cy} L{x0:.1f} {y0_:.1f} A{R} {R} 0 {big} 1 {x1:.1f} {y1_:.1f} Z"/>'
    a0 = a1
for i, (n, v, cls) in enumerate(_dane):
    _r += f'<rect class="{cls} ol" x="285" y="{60 + i * 30}" width="14" height="14"/><text class="ts" x="305" y="{72 + i * 30}">{n} {v}%</text>'
S['g-struktura'] = [
 dict(typ='rysunek', tytul='Struktura religijna ludności świata (wykres kołowy)', svg=_r,
      znaczniki=[(200, 80, 230, 30, 'Chrześcijaństwo', 'Ok. 2,4 mld — Europa, Ameryki, Afryka Subsaharyjska'),
                 (178, 214, 230, 270, 'Islam', 'Ok. 2 mld — najszybciej rosnąca religia (wysoka dzietność)'),
                 (60, 110, 30, 60, 'Hinduizm', 'Głównie Indie i Nepal')],
      opis='Przybliżony udział wyznawców religii w ludności świata (ok. 2020, zaokrąglenia) — wykres autorski IndexLab.',
      uwaga='Udziały są przybliżone i różnią się w zależności od źródła. Wzrost udziału islamu wynika głównie z wysokiej dzietności w krajach muzułmańskich; w Europie rośnie odsetek osób niewierzących.'),
]


def _dopasuj(z):
    out = []
    for (x, y, lx, ly, n, d) in z:
        w = len(n) * 6.4 + 16
        if lx > x and lx + w > 400:
            lx = max(x - 25, w)
        elif lx <= x and lx - w < 0:
            lx = min(x + 25, 400 - w)
        if lx <= x and lx > x - 5:
            lx = x - 5
        out.append((x, y, round(lx), ly, n, d))
    return out


for _v in S.values():
    for _s in _v:
        _s['znaczniki'] = _dopasuj(_s['znaczniki'])
