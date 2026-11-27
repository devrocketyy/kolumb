# Schematy geografii — porcja 25 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Enklawa i eksklawa ----------
_e = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
_e += '<path class="gl ol" d="M20 40 H230 V270 H20 Z"/>'                     # państwo A
_e += '<path class="gt ol" d="M100 110 H160 V170 H100 Z"/>'                  # enklawa B w A
_e += '<path class="gt ol" d="M250 40 H380 V200 H250 Z"/>'                   # państwo B (główne terytorium)
_e += '<path class="gl ol" d="M300 230 H370 V280 H300 Z"/>'                  # eksklawa A
_e += '<text class="tb" x="60" y="60">państwo A</text><text class="tb" x="275" y="60">państwo B</text>'
S['g-polityka'] = [
 dict(typ='rysunek', tytul='Enklawa i eksklawa (schemat)', svg=_e,
      znaczniki=[(130, 140, 60, 210, 'Enklawa', 'Obszar państwa B otoczony całkowicie przez państwo A (np. San Marino, Lesotho)'),
                 (335, 255, 260, 285, 'Eksklawa', 'Część państwa A oddzielona od niego (np. Obwód Królewiecki Rosji)'),
                 (315, 120, 300, 150, 'Główne terytorium B', 'Dla B obszar w środku A jest eksklawą')],
      opis='Schemat dwóch pojęć terytorialnych (państwa umowne) — rysunek autorski IndexLab.',
      uwaga='Ten sam obszar może być jednocześnie enklawą (z punktu widzenia państwa, które go otacza) i eksklawą (z punktu widzenia państwa, do którego należy).'),
]

# ---------- 2. Powstawanie atolu ----------
_a = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_a += '<rect class="gw" x="0" y="140" width="400" height="160"/>'
for i, (h, isl) in enumerate(((100, True), (55, True), (-30, False))):
    cx = 70 + i * 130
    top = 140 - h
    _a += f'<path class="gs ol" d="M{cx - 55} 290 L{cx - 12} {top} L{cx + 12} {top} L{cx + 55} 290 Z"/>'
    _a += f'<path class="gc ol" d="M{cx - 40} 140 h14 v10 h-14 Z M{cx + 26} 140 h14 v10 h-14 Z"/>'
    if i == 2:
        _a += f'<path class="gc ol" d="M{cx - 42} 130 h18 v12 h-18 Z M{cx + 24} 130 h18 v12 h-18 Z"/>'
_a += '<text class="ts" x="70" y="292" text-anchor="middle">1</text><text class="ts" x="200" y="292" text-anchor="middle">2</text><text class="ts" x="330" y="292" text-anchor="middle">3</text>'
S['g-oceany'] = [
 dict(typ='rysunek', tytul='Powstawanie atolu (teoria Darwina)', svg=_a,
      znaczniki=[(70, 60, 120, 30, 'Wyspa wulkaniczna', 'Rafa obrzeżająca rośnie przy brzegu'),
                 (200, 110, 240, 70, 'Wulkan osiada', 'Wyspa się zanurza, rafa rośnie ku górze — rafa barierowa'),
                 (330, 150, 280, 230, 'Laguna', 'Wulkan pod wodą — w środku płytka laguna'),
                 (300, 135, 350, 95, 'Atol', 'Pierścień raf wystający nad poziom morza')],
      opis='Etapy przekształcania wyspy wulkanicznej w atol — rysunek autorski IndexLab.',
      uwaga='Koralowce żyją tylko w ciepłej, płytkiej i przejrzystej wodzie, dlatego rosną ku górze, gdy dno osiada. Atole są typowe dla Pacyfiku i Oceanu Indyjskiego (Malediwy).'),
]

# ---------- 3. Pływy syzygijne i kwadraturowe ----------
_p = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_p += '<circle class="hotf" cx="30" cy="80" r="22"/><circle class="hotf" cx="30" cy="225" r="22"/>'
for cy, moon in ((80, (300, 80)), (225, (190, 160))):
    _p += f'<ellipse class="gw ol" cx="190" cy="{cy}" rx="{48 if cy == 80 else 36}" ry="{36 if cy == 80 else 46}"/>'
    _p += f'<circle class="gl ol" cx="190" cy="{cy}" r="26"/>'
    _p += f'<circle class="gs2 ol" cx="{moon[0]}" cy="{moon[1]}" r="10"/>'
_p += '<path class="dash" d="M52 80 H290"/><path class="dash" d="M52 225 H160 M190 199 V170"/>'
_p += '<text class="tb" x="390" y="18" text-anchor="end">pływy syzygijne (nów, pełnia)</text>'
_p += '<text class="tb" x="390" y="270" text-anchor="end">pływy kwadraturowe (kwadry)</text>'
S['g-oceany'].append(
 dict(typ='rysunek', tytul='Pływy syzygijne i kwadraturowe', svg=_p,
      znaczniki=[(300, 80, 340, 120, 'Księżyc w linii', 'Przyciąganie Księżyca i Słońca sumuje się — największe pływy'),
                 (190, 160, 250, 170, 'Księżyc pod kątem 90°', 'Siły częściowo się znoszą — najmniejsze pływy'),
                 (238, 80, 270, 45, 'Wybrzuszenie wody', 'Ocean wydłużony wzdłuż linii przyciągania'),
                 (30, 80, 60, 30, 'Słońce', 'Wpływ ok. 2 razy słabszy niż Księżyca')],
      opis='Uproszczony układ Słońce–Ziemia–Księżyc (bez skali) i kształt „garbu” pływowego — rysunek autorski IndexLab.',
      uwaga='Pływy syzygijne występują dwa razy w miesiącu (nów i pełnia), kwadraturowe — w pierwszej i ostatniej kwadrze. W Bałtyku pływy są bardzo małe (kilka cm).'))

# ---------- 4. Elektrownia szczytowo-pompowa ----------
_e2 = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_e2 += '<path class="gt ol" d="M0 300 V100 H140 C200 100 230 250 300 250 H400 V300 Z"/>'
_e2 += '<path class="gw ol" d="M20 100 H130 V80 H20 Z"/>'
_e2 += '<path class="gw ol" d="M290 250 H390 V230 H290 Z"/>'
_e2 += '<path class="s" d="M130 95 C190 110 230 230 290 245" style="fill:none;stroke-width:4"/>'
_e2 += '<rect class="gs2 ol" x="250" y="215" width="30" height="20"/>'
_e2 += strz(160, 120, 220, 200, 'cold') + strz(235, 175, 175, 95, 'hot')
_e2 += '<text class="ts" x="215" y="150">szczyt — produkcja</text><text class="ts" x="120" y="160" text-anchor="end">noc — pompowanie</text>'
S['g-energetyka'] = [
 dict(typ='rysunek', tytul='Elektrownia szczytowo-pompowa — zasada działania', svg=_e2,
      znaczniki=[(75, 90, 50, 40, 'Zbiornik górny', 'Magazyn energii w postaci wody na wysokości'),
                 (340, 240, 330, 200, 'Zbiornik dolny', 'Woda spływa tu w czasie szczytu'),
                 (265, 225, 330, 160, 'Turbiny-pompy', 'W dzień produkują prąd, w nocy pompują wodę w górę')],
      opis='Schemat działania elektrowni szczytowo-pompowej (np. Żarnowiec, Porąbka-Żar) — rysunek autorski IndexLab.',
      uwaga='Elektrownia zużywa więcej energii na pompowanie, niż potem oddaje, ale przenosi ją w czasie — z nocy (tania, nadwyżki) na szczyt zapotrzebowania. Ważna przy rozwoju wiatru i fotowoltaiki.'),
]

# ---------- 5. Struktura PKB a poziom rozwoju ----------
_g = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
dane = [('słabo rozwinięty', (35, 20, 45)), ('średnio rozwinięty', (10, 35, 55)), ('wysoko rozwinięty', (1, 22, 77))]
for i, (n, (a, b, c)) in enumerate(dane):
    x = 50 + i * 115
    y = 250
    for v, cls in ((a, 'gt'), (b, 'gs2'), (c, 'gw2')):
        h = v * 2
        _g += f'<rect class="{cls} ol" x="{x}" y="{y - h}" width="80" height="{h}"/>'
        if v >= 10:
            _g += f'<text class="tb" x="{x + 40}" y="{y - h / 2 + 4:.0f}" text-anchor="middle">{v}%</text>'
        y -= h
    _g += f'<text class="ts" x="{x + 40}" y="268" text-anchor="middle">{n}</text>'
_g += '<path class="s" d="M40 250 H380"/>'
_g += '<rect class="gt ol" x="40" y="280" width="10" height="10"/><text class="ts" x="54" y="289">rolnictwo</text><rect class="gs2 ol" x="140" y="280" width="10" height="10"/><text class="ts" x="154" y="289">przemysł</text><rect class="gw2 ol" x="230" y="280" width="10" height="10"/><text class="ts" x="244" y="289">usługi</text>'
S['g-rozwoj'] = [
 dict(typ='rysunek', tytul='Struktura PKB według sektorów a poziom rozwoju', svg=_g,
      znaczniki=[(90, 215, 30, 170, 'Duży udział rolnictwa', 'Typowe dla krajów słabo rozwiniętych (np. Czad, Etiopia)'),
                 (205, 165, 240, 40, 'Wzrost przemysłu', 'Industrializacja krajów średnio rozwiniętych (np. Chiny, Indonezja)'),
                 (320, 120, 330, 22, 'Dominacja usług', 'Kraje wysoko rozwinięte (USA, Wielka Brytania)')],
      opis='Modelowa struktura PKB (wartości przybliżone, typowe) — wykres autorski IndexLab.',
      uwaga='Wraz z rozwojem maleje udział rolnictwa w PKB, najpierw rośnie, a potem maleje udział przemysłu, a usługi stają się dominujące (model trzech sektorów Fishera–Clarka).'),
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
