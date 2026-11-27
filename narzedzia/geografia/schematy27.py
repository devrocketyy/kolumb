# Schematy geografii — porcja 27 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Typy jezior w przekroju ----------
_j = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
# rynnowe (wąskie, głębokie)
_j += '<path class="gp ol" d="M10 60 H180 V140 H10 Z"/><path class="gw ol" d="M80 60 L88 128 L102 128 L110 60 Z"/>'
# morenowe (płytkie, nieregularne między wałami)
_j += '<path class="gc ol" d="M220 140 V70 C240 50 260 50 270 70 C290 80 320 80 330 70 C345 50 365 55 390 70 V140 Z"/><path class="gw ol" d="M270 70 C290 85 320 85 330 70 Z"/>'
# wytopiskowe (okrągłe zagłębienie)
_j += '<path class="gp ol" d="M10 200 H180 V280 H10 Z"/><path class="gw ol" d="M70 200 C75 235 115 235 120 200 Z"/>'
# przybrzeżne (mierzeja oddziela od morza)
_j += '<path class="gl ol" d="M220 280 V215 H285 V280 Z"/><path class="gw ol" d="M285 215 C295 230 315 230 325 215 Z"/><path class="gp ol" d="M325 215 C330 205 340 205 345 215 V280 H325 Z"/><path class="gw ol" d="M345 215 H390 V280 H345 Z"/>'
for x, y, t in ((95, 52, 'rynnowe'), (305, 45, 'morenowe'), (95, 192, 'wytopiskowe'), (305, 198, 'przybrzeżne')):
    _j += f'<text class="tb" x="{x}" y="{y}" text-anchor="middle">{t}</text>'
S['g-pl-wody'] = [
 dict(typ='rysunek', tytul='Typy jezior polodowcowych i przybrzeżnych (przekroje)', svg=_j,
      znaczniki=[(95, 110, 150, 160, 'Rynna', 'Wąskie, długie i głębokie (Hańcza 108 m, Gopło)'),
                 (300, 77, 340, 110, 'Zagłębienie między morenami', 'Płytkie, rozległe, o nieregularnych brzegach (Śniardwy)'),
                 (95, 215, 120, 290, 'Oczko wytopiskowe', 'Małe, okrągłe — po bryle martwego lodu'),
                 (335, 225, 360, 260, 'Mierzeja', 'Wał piasku oddziela jezioro od morza (Łebsko, Gardno)')],
      opis='Uproszczone przekroje przez typowe jeziora Polski — rysunek autorski IndexLab (bez skali).',
      uwaga='Rynnowe wyżłobiły wody pod lądolodem, morenowe wypełniają zagłębienia między pagórkami moren, wytopiskowe powstały po stopieniu brył lodu, przybrzeżne — przez odcięcie zatok mierzeją.'),
]

# ---------- 2. Trzy profile glebowe ----------
_g = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
profile = [
 ('bielica', [('O', 10, 'gf2'), ('A', 15, 'gg'), ('E', 40, 'gi'), ('B', 45, 'gc'), ('C', 90, 'gp')]),
 ('czarnoziem', [('A', 110, 'gs2'), ('AC', 40, 'gg'), ('C', 50, 'gp')]),
 ('rędzina', [('A', 40, 'gg'), ('AC', 30, 'gc'), ('C', 130, 'gs')]),
]
for i, (n, warstwy) in enumerate(profile):
    x = 30 + i * 125
    y = 40
    for (sym, h, cls) in warstwy:
        _g += f'<rect class="{cls} ol" x="{x}" y="{y}" width="90" height="{h}"/><text class="tb" x="{x - 6}" y="{y + h / 2 + 4:.0f}" text-anchor="end">{sym}</text>'
        y += h
    _g += f'<text class="tb" x="{x + 45}" y="28" text-anchor="middle">{n}</text>'
S['g-gleby'] = [
 dict(typ='rysunek', tytul='Profile gleb: bielica, czarnoziem, rędzina', svg=_g,
      znaczniki=[(75, 82, 140, 12, 'Poziom wymywania (E)', 'Jasny, wypłukany — cecha bielic'),
                 (200, 95, 230, 150, 'Gruby poziom próchniczny', 'Czarnoziem: nawet ponad 1 m próchnicy'),
                 (325, 175, 270, 270, 'Skała węglanowa (C)', 'Rędzina leży płytko na wapieniu'),
                 (75, 125, 110, 200, 'Poziom wmywania (B)', 'Gromadzą się związki żelaza i glinu')],
      opis='Uproszczone profile trzech typów gleb (miąższości symboliczne) — rysunek autorski IndexLab.',
      uwaga='Bielica — strefowa, pod lasem iglastym na piaskach; czarnoziem — strefowy, pod stepem na lessie; rędzina — astrefowa, na skałach węglanowych.'),
]

# ---------- 3. Powstawanie niżu na froncie polarnym ----------
_n = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
for i in range(3):
    x0 = 10 + i * 130
    _n += f'<rect class="gw2" x="{x0}" y="40" width="120" height="110" style="opacity:.25"/>'
    if i == 0:
        _n += f'<path class="cold" d="M{x0} 95 H{x0 + 120}" style="stroke-width:2.5"/>'
        _n += strz(x0 + 90, 70, x0 + 30, 70, 'cold') + strz(x0 + 30, 120, x0 + 90, 120, 'hot')
    elif i == 1:
        _n += f'<path class="hot" d="M{x0 + 60} 95 Q{x0 + 85} 85 {x0 + 115} 100" style="fill:none;stroke-width:2.5"/>'
        _n += f'<path class="cold" d="M{x0 + 60} 95 Q{x0 + 40} 110 {x0 + 15} 130" style="fill:none;stroke-width:2.5"/>'
    else:
        _n += f'<path class="hot" d="M{x0 + 60} 90 Q{x0 + 85} 90 {x0 + 112} 112" style="fill:none;stroke-width:2.5"/>'
        _n += f'<path class="cold" d="M{x0 + 60} 90 Q{x0 + 50} 115 {x0 + 30} 135" style="fill:none;stroke-width:2.5"/>'
        _n += f'<path class="s" d="M{x0 + 40} 70 Q{x0 + 52} 80 {x0 + 60} 90" style="fill:none;stroke-width:2.5;stroke-dasharray:4 3"/>'
    _n += f'<text class="tb" x="{x0 + 60}" y="170" text-anchor="middle">etap {i + 1}</text>'
_n += '<text class="ts" x="200" y="200" text-anchor="middle">widok z góry, półkula N</text>'
S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Powstawanie niżu na froncie polarnym (widok z góry)', svg=_n,
      znaczniki=[(70, 95, 70, 240, 'Front polarny', 'Granica mas polarnych i zwrotnikowych, wiatry przeciwne'),
                 (200, 95, 200, 260, 'Fala frontu', 'Front wygina się — tworzy się front ciepły i chłodny'),
                 (330, 90, 330, 240, 'Okluzja', 'Front chłodny dogania ciepły — niż w pełni rozwinięty'),
                 (100, 120, 140, 220, 'Ciepłe powietrze', 'Napływa od strony zwrotników')],
      opis='Uproszczony model rozwoju niżu (cyklonu umiarkowanych szerokości) — rysunek autorski IndexLab.',
      uwaga='Wędrowne niże powstają na froncie polarnym nad Atlantykiem i przesuwają się nad Europę z zachodu na wschód, przynosząc zmienną pogodę Polsce.'),
]

# ---------- 4. Ozy i kemy ----------
_o = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_o += '<path class="gi ol" d="M0 60 H400 V150 H0 Z"/>'
_o += '<path class="gw ol" d="M80 150 C90 120 110 120 120 150 Z"/>'
_o += '<path class="gw ol" d="M270 60 H300 V150 H270 Z" style="opacity:.7"/>'
_o += '<path class="gc ol" d="M0 230 H400 V300 H0 Z"/>'
_o += '<path class="gp ol" d="M60 230 C80 180 120 180 140 230 Z"/>'
_o += '<path class="gp ol" d="M250 230 C260 195 310 195 320 230 Z"/>'
_o += '<path class="dash" d="M0 190 H400"/><text class="ts" x="392" y="186" text-anchor="end">po stopieniu lodu ↓</text>'
_o += '<text class="tb" x="8" y="52">lądolód (martwy lód)</text>'
S['g-lodowce'] = [
 dict(typ='rysunek', tytul='Powstawanie ozów i kemów (przekrój)', svg=_o,
      znaczniki=[(100, 140, 160, 85, 'Tunel podlodowcowy', 'Rzeka płynie pod lodem i osadza piasek i żwir'),
                 (100, 205, 170, 270, 'Oz', 'Wąski, długi wał po rzece podlodowcowej'),
                 (285, 100, 330, 130, 'Szczelina w lodzie', 'Wypełniana osadami wód roztopowych'),
                 (285, 210, 340, 265, 'Kem', 'Pagórek z warstwowanych piasków po stopieniu lodu')],
      opis='Schemat powstawania form glacifluwialnych przy zanikającym lądolodzie — rysunek autorski IndexLab.',
      uwaga='Ozy i kemy zbudowane są z warstwowanych piasków i żwirów (osady wodnolodowcowe), w przeciwieństwie do moren z nieposortowanej gliny. Przykłady: Pojezierze Mazurskie, Pomorze.'),
]

# ---------- 5. Formy osadnictwa wiejskiego ----------
_w = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
# ulicówka
_w += '<path class="s" d="M20 70 H180" style="stroke-width:3"/>'
for x in range(30, 180, 20):
    _w += f'<rect class="gs2 ol" x="{x}" y="55" width="10" height="10"/><rect class="gs2 ol" x="{x}" y="75" width="10" height="10"/>'
# owalnica
_w += '<ellipse class="s" cx="300" cy="70" rx="70" ry="35" style="fill:none;stroke-width:3"/><ellipse class="gt ol" cx="300" cy="70" rx="40" ry="15"/>'
for a in range(0, 360, 30):
    x = 300 + 82 * math.cos(math.radians(a)); y = 70 + 45 * math.sin(math.radians(a))
    _w += f'<rect class="gs2 ol" x="{x - 5:.0f}" y="{y - 5:.0f}" width="10" height="10"/>'
# rozproszona
for (x, y) in ((40, 190), (90, 220), (140, 180), (60, 260), (160, 250), (120, 280)):
    _w += f'<rect class="gs2 ol" x="{x}" y="{y}" width="10" height="10"/>'
# wielodrożnica / skupiona
_w += '<path class="s" d="M220 180 L380 280 M380 180 L220 280 M300 170 V290" style="stroke-width:2"/>'
for (x, y) in ((280, 220), (310, 215), (295, 240), (320, 240), (270, 245), (300, 260), (330, 265), (285, 200)):
    _w += f'<rect class="gs2 ol" x="{x}" y="{y}" width="10" height="10"/>'
for x, y, t in ((100, 30, 'ulicówka'), (300, 22, 'owalnica'), (100, 160, 'zabudowa rozproszona'), (300, 160, 'wieś skupiona')):
    _w += f'<text class="tb" x="{x}" y="{y}" text-anchor="middle">{t}</text>'
S['g-urbanizacja'] = [
 dict(typ='rysunek', tytul='Formy osadnictwa wiejskiego (plan)', svg=_w,
      znaczniki=[(100, 70, 30, 110, 'Wzdłuż drogi', 'Ulicówka — zagrody po obu stronach drogi (częsta w Polsce)'),
                 (300, 70, 330, 145, 'Plac w środku', 'Owalnica — zagrody wokół placu (nawsia), dawniej obronna'),
                 (90, 225, 40, 205, 'Kolonie', 'Pojedyncze zagrody wśród pól — np. Kurpie, Podhale'),
                 (300, 230, 340, 290, 'Skrzyżowanie dróg', 'Wieś skupiona, wielodrożnica')],
      opis='Uproszczone plany typowych form wsi — rysunek autorski IndexLab.',
      uwaga='Kształt wsi zależy od historii osadnictwa i warunków przyrodniczych: ulicówki zakładano na prawie niemieckim, rozproszona zabudowa powstała po parcelacji majątków i w górach.'),
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
