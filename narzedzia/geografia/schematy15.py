# Schematy geografii — porcja 15 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
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

_bT = [7, 7, 8, 10, 13, 15, 17, 17, 16, 13, 10, 8]
_bP = [130, 100, 90, 70, 70, 50, 50, 60, 80, 110, 120, 140]
_b, _bty, _ = klimatogram(_bT, _bP, tmin=0, tmax=30, pmax=160)
S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Klimatogram: klimat umiarkowany morski (Brest)', svg=_b,
      znaczniki=[(kx(0), _bty(7), 95, 70, 'Łagodna zima', 'Styczeń ok. 7°C — brak mrozów'),
                 (kx(7), _bty(17), 210, 30, 'Chłodne lato', 'Sierpień ok. 17°C'),
                 (kx(11), 250 - 210 * 140 / 160, 260, 90, 'Mokra zima', 'Najwięcej opadów jesienią i zimą — niże z Atlantyku'),
                 (kx(5), 250 - 210 * 50 / 160, 150, 160, 'Suchsze lato', 'Mniej opadów, ale żaden miesiąc nie jest suchy')],
      opis='Klimatogram autorski stacji na zachodnim wybrzeżu Francji (wartości przybliżone).',
      uwaga='Klimat morski: mała amplituda (ok. 10°C), łagodne zimy i chłodne lata dzięki Prądowi Północnoatlantyckiemu i wiatrom zachodnim; opady przez cały rok.'),
]

# ---------- przełęcz na poziomicach ----------
_pz = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
_pz += '<path class="gp ol" d="M30 150 C30 70 120 55 200 105 C280 55 370 70 370 150 C370 230 280 245 200 195 C120 245 30 230 30 150 Z"/>'
for (cx, cy), rs, cls in (((115, 150), (70, 48, 26), ('gl', 'gl2', 'gs')), ((285, 150), (72, 50, 28), ('gl', 'gl2', 'gs'))):
    for r, c in zip(rs, cls):
        _pz += f'<ellipse class="{c} ol" cx="{cx}" cy="{cy}" rx="{r}" ry="{r * 0.75:.0f}"/>'
_pz += '<path class="d" d="M110 152 l5 -9 l5 9 Z"/><text class="tb" x="115" y="166" text-anchor="middle">342</text>'
_pz += '<path class="d" d="M280 152 l5 -9 l5 9 Z"/><text class="tb" x="285" y="166" text-anchor="middle">346</text>'
_pz += '<text class="ts" x="115" y="216" text-anchor="middle">300</text><text class="ts" x="115" y="200" text-anchor="middle">310</text><text class="ts" x="115" y="184" text-anchor="middle">320</text>'
_pz += '<path class="dash" d="M20 150 H380"/><text class="tb" x="12" y="146">A</text><text class="tb" x="384" y="146">B</text>'
_pz += '<path class="cold" d="M200 196 C198 230 210 260 205 300" style="stroke-width:2.4"/><path class="cold" d="M200 104 C202 70 190 40 195 0" style="stroke-width:2.4"/>'
_pz += '<text class="ts" x="390" y="292" text-anchor="end">cięcie poziomic 10 m</text>'
S['g-poziomice'] = [
 dict(typ='rysunek', tytul='Przełęcz między dwoma szczytami (poziomice)', svg=_pz,
      znaczniki=[(115, 145, 125, 30, 'Szczyt zachodni', '342 m n.p.m.'),
                 (285, 145, 270, 55, 'Szczyt wschodni', '346 m — wyższy'),
                 (200, 150, 230, 230, 'Przełęcz', 'Najniższy punkt grzbietu między szczytami (ok. 300–310 m)'),
                 (202, 230, 150, 265, 'Źródłowe potoki', 'Spływają z przełęczy na obie strony grzbietu')],
      opis='Fragment mapy poziomicowej z dwoma wzniesieniami i przełęczą (dane autorskie).',
      uwaga='Przełęcz to miejsce, w którym z obu stron grzbietu wznoszą się szczyty, a w poprzek grzbietu teren opada — przez przełęcze prowadzą drogi i szlaki.'),
]
