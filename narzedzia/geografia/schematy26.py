# Schematy geografii — porcja 26 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Budowa wnętrza Ziemi ----------
_b = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
cx, cy = 150, 300
for r, cls in ((270, 'gl'), (255, 'gm'), (150, 'hotf'), (70, 'gi')):
    _b += f'<path class="{cls} ol" d="M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy} Z"/>'
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Budowa wnętrza Ziemi (przekrój)', svg=_b,
      znaczniki=[(150, 38, 300, 25, 'Skorupa ziemska', 'Kontynentalna 30–70 km, oceaniczna 5–10 km'),
                 (60, 120, 300, 80, 'Płaszcz', 'Do ok. 2900 km; w górnej części astenosfera — plastyczna'),
                 (150, 190, 300, 150, 'Jądro zewnętrzne', 'Ciekłe (żelazo, nikiel) — źródło pola magnetycznego'),
                 (150, 262, 300, 230, 'Jądro wewnętrzne', 'Stałe, temperatura ok. 5000–6000°C')],
      opis='Uproszczony przekrój przez wnętrze Ziemi (grubości warstw nie w skali — skorupa powiększona) — rysunek autorski IndexLab.',
      uwaga='Litosfera = skorupa + najwyższa, sztywna część płaszcza; pod nią astenosfera, po której przesuwają się płyty. Granicę skorupa–płaszcz nazywamy nieciągłością Moho.'),
]

# ---------- 2. Kąt padania promieni ----------
_k = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_k += '<circle class="gl ol" cx="60" cy="300" r="240"/>'
for y in (95, 115, 255, 275):
    _k += strz(390, y, 310 if y < 200 else 304, y, 'hot', 6)
_k += '<path class="hot" d="M279 95 L298 115" style="stroke-width:5"/>'
_k += '<path class="hot" d="M296 255 L300 275" style="stroke-width:5"/>'
_k += '<text class="ts" x="8" y="290">Ziemia (fragment)</text>'
S['g-slonce'] = [
 dict(typ='rysunek', tytul='Kąt padania promieni a nagrzewanie powierzchni', svg=_k,
      znaczniki=[(298, 265, 250, 230, 'Promienie prostopadłe', 'Wiązka pada na mały obszar — silne nagrzanie (strefa międzyzwrotnikowa)'),
                 (288, 105, 230, 60, 'Promienie ukośne', 'Ta sama wiązka rozkłada się na większą powierzchnię — słabsze nagrzanie'),
                 (380, 185, 330, 185, 'Równoległe promienie Słońca', 'Docierają do Ziemi pod różnym kątem zależnie od szerokości')],
      opis='Ta sama ilość energii pada na różną powierzchnię w zależności od kąta — rysunek autorski IndexLab.',
      uwaga='Im mniejszy kąt padania, tym większa powierzchnia i grubsza warstwa atmosfery, przez którą przechodzi światło — dlatego ku biegunom jest coraz zimniej.'),
]

# ---------- 3. Bilans wodny zlewni ----------
_w = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_w += '<path class="gt ol" d="M0 170 C80 140 140 140 200 200 C260 140 320 140 400 170 V300 H0 Z"/>'
_w += '<path class="gw2" d="M0 250 H400 V300 H0 Z" style="opacity:.6"/>'
_w += '<path class="cold" d="M200 205 V300" style="stroke-width:5"/>'
_w += '<path class="gk ol" d="M120 30 C130 10 170 10 180 30 C200 30 200 55 180 55 H120 C100 55 100 30 120 30 Z"/>'
for x in (130, 150, 170):
    _w += f'<path class="cold" d="M{x} 60 l-6 22"/>'
_w += strz(300, 150, 300, 90, 'hot') + strz(80, 160, 140, 185, 'cold') + strz(60, 175, 60, 240, 'cold')
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Bilans wodny zlewni', svg=_w,
      znaczniki=[(150, 70, 240, 40, 'Opad (P)', 'Woda dopływająca do zlewni'),
                 (300, 110, 340, 70, 'Parowanie (E)', 'Ewapotranspiracja z gleby i roślin'),
                 (110, 172, 60, 120, 'Spływ powierzchniowy', 'Szybko trafia do rzeki'),
                 (60, 215, 100, 270, 'Infiltracja', 'Zasila wody podziemne, potem rzekę'),
                 (200, 270, 270, 280, 'Odpływ (H)', 'Rzeką wypływa ze zlewni')],
      opis='Składniki bilansu wodnego zlewni — rysunek autorski IndexLab.',
      uwaga='Równanie bilansu: P = H + E ± ΔR (opad = odpływ + parowanie ± zmiana retencji). W Polsce ok. 70% opadu wyparowuje, a tylko ok. 30% odpływa rzekami.'),
]

# ---------- 4. Obieg węgla ----------
_c = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
boxes = [(200, 40, 'atmosfera (CO₂)', 'gk'), (70, 150, 'rośliny i zwierzęta', 'gt'), (200, 250, 'paliwa kopalne', 'gs2'), (330, 150, 'ocean', 'gw2')]
for x, y, t, c in boxes:
    w = len(t) * 6.5 + 20
    _c += f'<rect class="{c} ol" x="{x - w / 2:.0f}" y="{y - 15}" width="{w:.0f}" height="30" rx="8"/><text class="tb" x="{x}" y="{y + 5}" text-anchor="middle">{t}</text>'
_c += strz(150, 50, 90, 133, 'cold') + strz(105, 133, 165, 58, 's')
_c += strz(250, 58, 315, 133, 'cold') + strz(300, 133, 230, 58, 's')
_c += strz(200, 233, 200, 60, 'hot')
_c += strz(90, 168, 170, 238, 's')
S['g-srodowisko'] = [
 dict(typ='rysunek', tytul='Obieg węgla w przyrodzie', svg=_c,
      znaczniki=[(120, 90, 30, 95, 'Fotosynteza', 'Rośliny pobierają CO₂ z atmosfery'),
                 (135, 95, 160, 125, 'Oddychanie i rozkład', 'Organizmy oddają CO₂ do atmosfery'),
                 (200, 150, 230, 160, 'Spalanie paliw', 'Człowiek uwalnia węgiel zmagazynowany przez miliony lat'),
                 (282, 95, 330, 100, 'Wymiana z oceanem', 'Ocean pochłania ok. 1/4 emisji CO₂ (zakwaszenie)'),
                 (130, 203, 100, 225, 'Fosylizacja', 'Szczątki organizmów → węgiel, ropa, gaz (bardzo powoli)')],
      opis='Uproszczony schemat obiegu węgla między atmosferą, biosferą, oceanem i litosferą — rysunek autorski IndexLab.',
      uwaga='Spalanie paliw kopalnych i wylesianie zaburzają obieg węgla — rośnie stężenie CO₂ w atmosferze (z ok. 280 do ponad 420 ppm) i nasila się efekt cieplarniany.'),
]

# ---------- 5. Strefy czasowe — model ----------
_t = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
for i in range(-6, 7):
    x = 200 + i * 28
    _t += f'<path class="s" d="M{x - 14} 40 V250" style="stroke-width:.6"/>'
    lab = f'+{i}' if i > 0 else str(i)
    _t += f'<text class="ts" x="{x}" y="265" text-anchor="middle">{lab}</text>'
_t += '<rect class="hotf" x="186" y="40" width="28" height="210" style="opacity:.35"/>'
_t += '<rect class="gt" x="214" y="40" width="28" height="210" style="opacity:.45"/>'
_t += '<text class="ts" x="200" y="285" text-anchor="middle">strefy czasu względem UTC (co 15° długości)</text>'
_t += '<path class="dash" d="M200 30 V250"/><text class="ts" x="200" y="25" text-anchor="middle">0° Greenwich</text>'
_t += strz(250, 150, 330, 150, 'hot') + strz(150, 150, 70, 150, 'cold')
S['g-obrotowy'] = [
 dict(typ='rysunek', tytul='Model stref czasowych (co 15° długości)', svg=_t,
      znaczniki=[(200, 120, 150, 80, 'Strefa UTC (0)', 'Południk środkowy 0°, od 7,5°W do 7,5°E'),
                 (228, 120, 250, 105, 'Strefa +1 (Polska)', 'Południk środkowy 15°E'),
                 (300, 150, 330, 190, 'Na wschód: +1 h co strefę', 'Zegary przestawiamy do przodu'),
                 (100, 150, 60, 215, 'Na zachód: −1 h co strefę', 'Zegary cofamy')],
      opis='Uproszczony model stref czasowych (bez rzeczywistych, nieregularnych granic) — rysunek autorski IndexLab.',
      uwaga='Teoretycznie jest 24 strefy po 15°, ale granice stref w praktyce biegną po granicach państw. Polska zimą ma UTC+1, latem UTC+2 (czas letni).'),
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
