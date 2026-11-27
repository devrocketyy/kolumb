# Schematy geografii — porcja 24 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


def dl_dnia(phi, d):
    """Długość dnia (h) dla szerokości phi i dnia roku d (bez refrakcji)."""
    dec = 23.44 * math.sin(math.radians(360 * (284 + d) / 365))
    x = -math.tan(math.radians(phi)) * math.tan(math.radians(dec))
    x = max(-1, min(1, x))
    return 2 * math.degrees(math.acos(x)) / 15


# ---------- 1. Długość dnia w ciągu roku ----------
x0, x1, y0, y1 = 50, 380, 250, 30
_d = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
for h in (0, 6, 12, 18, 24):
    y = y0 - (y0 - y1) * h / 24
    _d += f'<path class="dash" d="M{x0} {y:.0f} H{x1}"/><text class="ts" x="{x0 - 6}" y="{y + 4:.0f}" text-anchor="end">{h} h</text>'
for phi, cls in ((0, 's'), (52, 'cold'), (70, 'hot')):
    pts = ' '.join(f'{x0 + (x1 - x0) * d / 365:.0f},{y0 - (y0 - y1) * dl_dnia(phi, d) / 24:.0f}' for d in range(0, 366, 5))
    _d += f'<polyline class="{cls}" fill="none" points="{pts}" style="stroke-width:2.4"/>'
_d += ''.join(f'<text class="ts" x="{x0 + (x1 - x0) * (i + .5) / 12:.0f}" y="{y0 + 15}" text-anchor="middle">{m}</text>' for i, m in enumerate('IFMAMJJASOND'))
_d += f'<path class="s" d="M{x0} {y1} V{y0} H{x1}"/>'
S['g-slonce'] = [
 dict(typ='rysunek', tytul='Długość dnia w ciągu roku na różnych szerokościach', svg=_d,
      znaczniki=[(215, 140, 230, 120, 'Równik', 'Przez cały rok ok. 12 h'),
                 (205, 101, 120, 80, 'Polska (52°N)', 'Od ok. 7,5 h w grudniu do ok. 16,5 h w czerwcu'),
                 (230, 30, 300, 15, 'Za kołem podbiegunowym (70°N)', 'Latem dzień polarny (24 h), zimą noc polarna (0 h)'),
                 (105, 140, 60, 180, 'Równonoc', 'Ok. 21 III i 23 IX wszystkie krzywe przecinają 12 h')],
      opis='Długość dnia obliczona astronomicznie (bez refrakcji) dla równika, 52°N i 70°N — wykres autorski IndexLab.',
      uwaga='Im dalej od równika, tym większa roczna zmienność długości dnia. Na półkuli S krzywe są odwrócone — najdłuższy dzień przypada 22 grudnia.'),
]

# ---------- 2. Izostazja ----------
_i = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_i += '<path class="gm" d="M0 210 H400 V300 H0 Z"/>'
# lewa: pod lądolodem
_i += '<path class="gl ol" d="M10 140 H190 V230 C150 240 50 240 10 230 Z"/>'
_i += '<path class="gi ol" d="M25 140 C40 60 160 60 175 140 Z"/>'
_i += strz(100, 50, 100, 120, 's')
# prawa: po stopieniu
_i += '<path class="gl ol" d="M210 120 H390 V205 H210 Z"/>'
_i += '<path class="gw" d="M210 125 H230 V120 H210 Z"/>'
_i += strz(300, 190, 300, 135, 'hot')
_i += '<text class="tb" x="100" y="290" text-anchor="middle">obciążenie lodem</text><text class="tb" x="300" y="290" text-anchor="middle">po ustąpieniu lodu</text>'
S['g-lodowce'] = [
 dict(typ='rysunek', tytul='Izostazja polodowcowa (przekrój)', svg=_i,
      znaczniki=[(100, 100, 40, 40, 'Lądolód', 'Masa lodu (do 3 km) wgniata skorupę'),
                 (100, 233, 60, 265, 'Ugięcie skorupy', 'Skorupa zanurza się głębiej w plastycznym płaszczu'),
                 (300, 160, 340, 100, 'Wynurzanie', 'Po stopieniu lodu ląd powoli się podnosi (Zatoka Botnicka do ok. 1 cm/rok)'),
                 (220, 122, 240, 60, 'Dawne plaże', 'Wyniesione terasy brzegowe świadczą o podnoszeniu lądu')],
      opis='Schemat równowagi izostatycznej skorupy przed i po zlodowaceniu — rysunek autorski IndexLab.',
      uwaga='Izostazja to dążenie skorupy do równowagi „pływania” na płaszczu. Skandynawia i Kanada wciąż się podnoszą po zlodowaceniu; kraje bałtyckie zyskują nowy ląd.'),
]

# ---------- 3. Powstawanie węgla kamiennego ----------
_w = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
etapy = [('bagno karbońskie', 'gf'), ('torf', 'gg'), ('węgiel brunatny', 'gc'), ('węgiel kamienny', 'gs2'), ('antracyt', 'gs')]
for i, (t, c) in enumerate(etapy):
    x = 15 + i * 77
    h = 150 - i * 22
    _w += f'<rect class="{c} ol" x="{x}" y="{240 - h}" width="68" height="{h}"/>'
    _w += f'<text class="ts" x="{x + 34}" y="{262 + (i % 2) * 14}" text-anchor="middle">{t}</text>'
    if i < 4:
        _w += strz(x + 70, 160, x + 76, 160, 'hot')
_w += strz(20, 60, 380, 60, 'hot')
_w += '<text class="ts" x="200" y="50" text-anchor="middle">rośnie ciśnienie, temperatura i zawartość węgla pierwiastkowego</text>'
S['g-pl-geologia'] = [
 dict(typ='rysunek', tytul='Powstawanie węgla (uwęglanie)', svg=_w,
      znaczniki=[(49, 120, 80, 85, 'Szczątki roślin', 'W karbonie bagienne lasy paprotników i skrzypów'),
                 (126, 160, 150, 120, 'Torf', 'Brak tlenu w wodzie hamuje rozkład — ok. 60% węgla'),
                 (203, 175, 230, 115, 'Węgiel brunatny', 'Bełchatów, Turów — młodszy (neogen), mniej kaloryczny'),
                 (280, 190, 300, 145, 'Węgiel kamienny', 'GZW, LZW — karbon, ok. 80–90% węgla'),
                 (357, 205, 340, 230, 'Antracyt', 'Najwyższy stopień uwęglenia')],
      opis='Etapy uwęglania materii roślinnej (wysokość słupków — symboliczna, maleje miąższość) — rysunek autorski IndexLab.',
      uwaga='Uwęglanie trwa miliony lat: przykrycie osadami → wzrost ciśnienia i temperatury → usuwanie wody i gazów. Im wyższy stopień uwęglenia, tym większa wartość opałowa.'),
]

# ---------- 4. Dywidenda demograficzna ----------
_g = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
xx0, xx1, yy0, yy1 = 50, 380, 250, 40
_g += f'<path class="s" d="M{xx0} {yy1} V{yy0} H{xx1}"/>'
_g += '<path class="cold" fill="none" d="M50 160 C120 160 160 90 220 80 C280 75 320 130 380 170" style="stroke-width:2.6"/>'
_g += '<path class="hot" fill="none" d="M50 90 C120 90 170 190 220 200 C270 205 320 140 380 120" style="stroke-width:2.6"/>'
_g += '<rect class="gt" x="170" y="40" width="110" height="210" style="opacity:.35"/>'
_g += '<text class="ts" x="215" y="268" text-anchor="middle">czas (fazy przejścia demograficznego) →</text>'
S['g-demografia'] = [
 dict(typ='rysunek', tytul='Dywidenda demograficzna', svg=_g,
      znaczniki=[(220, 80, 300, 40, 'Udział wieku produkcyjnego', 'Rośnie, gdy spada dzietność, a dzieci z wyżu dorastają'),
                 (220, 200, 300, 230, 'Obciążenie demograficzne', 'Najniższe w „oknie demograficznym”'),
                 (225, 140, 120, 125, 'Okno szansy', 'Dużo pracujących, mało osób zależnych — szansa na szybki wzrost'),
                 (370, 165, 330, 195, 'Starzenie się', 'Później rośnie udział seniorów — obciążenie znów rośnie')],
      opis='Schemat zmian struktury wieku w trakcie przejścia demograficznego (wartości względne) — wykres autorski IndexLab.',
      uwaga='Dywidendę wykorzystały m.in. Korea Pd. i Chiny (inwestycje w edukację i pracę). Kraje Afryki mogą ją osiągnąć, jeśli spadnie dzietność i powstaną miejsca pracy.'),
]

# ---------- 5. Lokalizacja centrum logistycznego ----------
_c = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
_c += '<path class="hot" d="M0 150 H400" style="stroke-width:5"/><path class="hot" d="M200 0 V300" style="stroke-width:5"/>'
_c += '<path class="s" d="M0 110 C120 110 300 210 400 200" style="stroke-width:3;stroke-dasharray:10 5"/>'
_c += '<rect class="gs2 ol" x="215" y="160" width="90" height="50"/><rect class="gs2 ol" x="215" y="215" width="60" height="30"/>'
for x in (225, 245, 265, 285):
    _c += f'<rect class="gk ol" x="{x}" y="168" width="12" height="8"/>'
_c += '<rect class="gl2 ol" x="60" y="40" width="80" height="60"/><text class="ts" x="100" y="75" text-anchor="middle">miasto</text>'
S['g-uslugi'] = [
 dict(typ='rysunek', tytul='Czynniki lokalizacji centrum logistycznego', svg=_c,
      znaczniki=[(200, 150, 140, 190, 'Węzeł autostrad', 'Skrzyżowanie A1 i A2 (np. Stryków) — szybki dojazd w całym kraju'),
                 (330, 190, 320, 260, 'Bocznica kolejowa', 'Transport intermodalny kontenerów'),
                 (260, 185, 340, 125, 'Hale magazynowe', 'Duża, tania działka poza miastem'),
                 (100, 70, 180, 30, 'Rynek i pracownicy', 'Bliskość dużego miasta — klienci i kadra')])
]
S['g-uslugi'][0].update(opis='Schemat typowej lokalizacji parku logistycznego przy węźle komunikacyjnym — rysunek autorski IndexLab.',
                        uwaga='Centra logistyczne w Polsce skupiają się wokół Łodzi (Stryków), Warszawy, Poznania, Wrocławia i Górnego Śląska — przy węzłach autostrad i w zasięgu wielkich rynków zbytu.')


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
