# Schematy geografii — porcja 13 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- izotermy stycznia w Polsce ----------
_PL = [(14.1, 52.8), (14.6, 51.0), (15.0, 50.9), (16.3, 50.6), (16.7, 50.2), (17.8, 50.0), (18.8, 49.5), (19.5, 49.4), (20.3, 49.4), (21.5, 49.4),
       (22.6, 49.1), (22.8, 49.6), (23.5, 50.4), (24.1, 50.8), (23.6, 51.6), (23.9, 52.7), (23.5, 53.5), (23.5, 54.2), (22.8, 54.4), (19.6, 54.4),
       (18.6, 54.4), (18.3, 54.8), (16.5, 54.5), (14.2, 53.9), (14.4, 53.3)]
_px = lambda lo: 30 + (lo - 14) * 34
_py = lambda la: 30 + (55 - la) * 40
_kontur = 'M' + ' L'.join(f'{_px(a):.0f} {_py(b):.0f}' for a, b in _PL) + ' Z'
_iz = [(0, 14.7, 15.4), (-1, 16.6, 17.6), (-2, 18.8, 19.8), (-3, 21.0, 22.0), (-4, 22.9, 23.8)]
_it = (f'<defs><clipPath id="g13pl"><path d="{_kontur}"/></clipPath></defs>'
       '<rect class="gw" x="0" y="0" width="400" height="300" opacity="0.5"/>'
       f'<path class="gt" d="{_kontur}"/>'
       '<g clip-path="url(#g13pl)">'
       + ''.join(f'<path class="cold" d="M{_px(a):.0f} {_py(55):.0f} L{_px(b):.0f} {_py(49):.0f}"/>' for t, a, b in _iz)
       + f'<path class="gi" d="M{_px(19):.0f} {_py(49.3):.0f} Q{_px(20):.0f} {_py(49.75):.0f} {_px(21):.0f} {_py(49.3):.0f} Z" style="stroke:none"/></g>'
       f'<path class="s" d="{_kontur}"/>'
       + ''.join(f'<text class="tb" x="{_px(a + (b - a) * 0.25):.0f}" y="{_py(53.5):.0f}" text-anchor="middle">{str(t).replace("-", "−")}°C</text>' for t, a, b in _iz)
       + '<text class="ts" x="8" y="292">izotermy stycznia (°C) — wartości przybliżone</text><text class="tb" x="200" y="18" text-anchor="middle">Morze Bałtyckie</text>')
S['g-pl-klimat'] = [
 dict(typ='rysunek', tytul='Temperatura stycznia w Polsce — izotermy', svg=_it,
      znaczniki=[(_px(14.6), _py(53.6), 60, 60, 'Zachód', 'Najcieplejsza zima — wpływ mas oceanicznych (ok. 0°C)'),
                 (_px(23.2), _py(53.9), 330, 60, 'Suwałki', 'Najzimniej na nizinach — ok. −4°C i mniej'),
                 (_px(20), _py(49.6), 250, 285, 'Tatry', 'W górach jeszcze zimniej — spadek z wysokością'),
                 (_px(19.3), _py(52.0), 170, 150, 'Przebieg izoterm', 'Południkowy — temperatura spada z zachodu na wschód')],
      opis='Uproszczony przebieg izoterm stycznia w Polsce.',
      uwaga='Zimą o temperaturze decyduje odległość od Atlantyku (kontynentalizm), dlatego izotermy biegną z północy na południe. Latem przebiegają równoleżnikowo — najcieplej na południu.'),
]

# ---------- dolina na mapie poziomicowej ----------
_dl = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
for k in range(5):
    y = 270 - 55 * k
    _dl += f'<path class="s" d="M0 {y} Q100 {y - 5} 200 {y - 55} Q300 {y - 5} 400 {y}" style="fill:none"/>'
    _dl += f'<text class="ts" x="8" y="{y - 4}">{200 + 10 * k}</text><text class="ts" x="392" y="{y - 4}" text-anchor="end">{200 + 10 * k}</text>'
_dl += '<path class="cold" d="M200 0 C195 60 205 140 198 200 C194 240 202 270 200 300" style="stroke-width:3"/>'
_dl += strz(212, 240, 212, 280, 'cold', 7)
_dl += '<path class="dash" d="M20 150 H380"/><text class="tb" x="14" y="146">A</text><text class="tb" x="384" y="146">B</text>'
_dl += '<path class="d" d="M370 30 l-6 14 l6 -4 l6 4 Z"/><text class="tb" x="370" y="58" text-anchor="middle">N</text>'
S['g-poziomice'] = [
 dict(typ='rysunek', tytul='Dolina rzeczna na mapie poziomicowej', svg=_dl,
      znaczniki=[(200, 160, 250, 120, 'Wygięcie poziomic', 'Poziomice tworzą „V” skierowane w górę doliny'),
                 (198, 230, 140, 255, 'Rzeka', 'Płynie z północy na południe — w dół doliny'),
                 (100, 214, 110, 185, 'Zbocze doliny', 'Wysokość rośnie od rzeki ku krawędziom'),
                 (300, 150, 315, 175, 'Linia A–B', 'Profil przez dolinę: wysoko – nisko – wysoko')],
      opis='Fragment mapy poziomicowej z doliną rzeczną (cięcie poziomic 10 m).',
      uwaga='Na mapie poziomicowej dolina to poziomice wygięte w kształt litery V lub U skierowanej w górę rzeki; grzbiet — wygięte w dół stoku. Rzeka płynie zawsze od wyższych poziomic do niższych.'),
]

