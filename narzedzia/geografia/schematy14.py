# Schematy geografii — porcja 14 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
MIES = 'IFMAMJJASOND'
def klimatogram(temp, opady, tmin=-10, tmax=30, pmax=400, x0=45, x1=330, y0=250, y1=40):
    """Klimatogram: słupki opadów (gw2), linia temperatury (hot), dwie osie z podziałką."""
    w = (x1 - x0) / 12
    ty = lambda t: y0 - (y0 - y1) * (t - tmin) / (tmax - tmin)
    out = ''.join(f'<path class="dash" d="M{x0} {ty(t):.1f} H{x1}"/>' for t in range(tmin, tmax + 1, 10))
    for i, p in enumerate(opady):
        h = (y0 - y1) * p / pmax
        out += f'<rect class="gw2" x="{x0 + i * w + 3:.1f}" y="{y0 - h:.1f}" width="{w - 6:.1f}" height="{h:.1f}"/>'
    pts = [(x0 + (i + 0.5) * w, ty(t)) for i, t in enumerate(temp)]
    out += '<polyline class="hot" fill="none" points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '"/>'
    out += ''.join(f'<circle class="hotf" cx="{x:.1f}" cy="{y:.1f}" r="2.4"/>' for x, y in pts)
    out += f'<path class="s" d="M{x0} {y1} V{y0} H{x1} V{y1}"/>'
    for t in range(tmin, tmax + 1, 10):
        out += f'<path class="s" d="M{x0 - 4} {ty(t):.1f} H{x0}"/><text class="ts" x="{x0 - 6}" y="{ty(t) + 3:.1f}" text-anchor="end">{t}</text>'
    for k in range(0, pmax + 1, pmax // 4):
        yy = y0 - (y0 - y1) * k / pmax
        out += f'<path class="s" d="M{x1} {yy:.1f} H{x1 + 4}"/><text class="ts" x="{x1 + 6}" y="{yy + 3:.1f}">{k}</text>'
    out += ''.join(f'<text class="ts" x="{x0 + (i + 0.5) * w:.1f}" y="{y0 + 13}" text-anchor="middle">{m}</text>' for i, m in enumerate(MIES))
    out += f'<text class="ts" x="{x0 - 6}" y="{y1 - 8}" text-anchor="end">°C</text><text class="ts" x="{x1 + 6}" y="{y1 - 8}">mm</text>'
    tsr = sum(temp) / 12
    tt = f'{tsr:.1f}'.replace('.', ',')
    out += (f'<text class="tb" x="{(x0 + x1) / 2:.0f}" y="{y0 + 32}" text-anchor="middle">'
            f'średnia {tt}°C · amplituda {max(temp) - min(temp)}°C · suma opadów {sum(opady)} mm</text>')
    return out, ty, w


def kx(i, x0=45, x1=330):
    return x0 + (i + 0.5) * (x1 - x0) / 12


S = {}

_wT = [-2, -1, 3, 9, 14, 17, 19, 18, 14, 9, 4, 0]
_wP = [30, 28, 33, 38, 55, 65, 75, 60, 45, 38, 38, 40]
_w, _wty, _ = klimatogram(_wT, _wP, tmin=-10, tmax=30, pmax=100)
S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Klimatogram: klimat umiarkowany przejściowy (Warszawa)', svg=_w,
      znaczniki=[(kx(0), _wty(-2), 95, 215, 'Zima', 'Styczeń ok. −2°C — miesiące z ujemną średnią'),
                 (kx(6), _wty(19), 200, 30, 'Lato', 'Lipiec ok. 19°C'),
                 (kx(6), 250 - 210 * 75 / 100, 180, 135, 'Maksimum opadów', 'Lipiec — opady konwekcyjne (burze)'),
                 (kx(1), 250 - 210 * 28 / 100, 120, 160, 'Mało opadów zimą', 'Luty ok. 28 mm')],
      opis='Klimatogram autorski stacji w środkowej Polsce (wartości przybliżone).',
      uwaga='Klimat przejściowy: amplituda ok. 21°C — większa niż w klimacie morskim, mniejsza niż w kontynentalnym; opady umiarkowane z maksimum latem.'),
]

_lata = [(2000, 96, 1, 2, 1), (2010, 88, 3, 7, 2), (2020, 70, 10, 18, 2), (2024, 57, 10, 28, 5)]
_ey = lambda p: 250 - p * 2.1
_en = ''.join(f'<path class="dash" d="M50 {_ey(p):.0f} H300"/><text class="ts" x="44" y="{_ey(p) + 3:.0f}" text-anchor="end">{p}%</text>' for p in (0, 25, 50, 75, 100))
for i, (r, w, g, o, n) in enumerate(_lata):
    x = 70 + i * 58
    y = 250
    for v, c in ((w, 'gs2'), (g, 'gp'), (o, 'gf'), (n, 'gw')):
        _en += f'<rect class="{c} ol" x="{x}" y="{y - v * 2.1:.1f}" width="38" height="{v * 2.1:.1f}"/>'
        if v >= 8:
            _en += f'<text class="tb" x="{x + 19}" y="{y - v * 1.05 + 4:.1f}" text-anchor="middle">{v}</text>'
        y -= v * 2.1
    _en += f'<text class="tb" x="{x + 19}" y="266" text-anchor="middle">{r}</text>'
_en += '<path class="s" d="M50 35 V250 H300"/>'
_en += ''.join(f'<rect class="{c} ol" x="315" y="{y}" width="12" height="12"/><text class="ts" x="332" y="{y + 10}">{t}</text>' for c, y, t in (('gw', 150, 'inne'), ('gf', 170, 'OZE'), ('gp', 190, 'gaz'), ('gs2', 210, 'węgiel')))
_en += '<text class="ts" x="175" y="290" text-anchor="middle">udział źródeł w produkcji energii elektrycznej (dane przybliżone)</text>'
S['g-energetyka'] = [
 dict(typ='rysunek', tytul='Produkcja energii elektrycznej w Polsce wg źródeł', svg=_en,
      znaczniki=[(89, 200, 120, 25, 'Węgiel 2000', 'Prawie cała energia z węgla kamiennego i brunatnego'),
                 (263, 175, 290, 60, 'Węgiel 2024', 'Udział spadł do ok. 57%'),
                 (263, 99, 320, 100, 'OZE', 'Wiatr i fotowoltaika — szybki wzrost do ok. 28%')],
      opis='Zmiany struktury produkcji energii elektrycznej w Polsce 2000–2024 (wartości przybliżone, zaokrąglone).',
      uwaga='Przyczyny zmian: polityka klimatyczna UE i koszty uprawnień do emisji CO₂, tanienie farm wiatrowych i paneli, rozwój energetyki gazowej. Planowana jest też energetyka jądrowa.'),
]
