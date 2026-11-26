# Schematy geografii — porcja 7 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}


import math
MIES = 'IFMAMJJASOND'
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')


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


TAJGA_T = [-38, -33, -20, -5, 7, 16, 19, 15, 6, -8, -27, -36]
TAJGA_P = [8, 6, 5, 8, 15, 30, 40, 38, 22, 15, 12, 9]
PUST_T = [13, 15, 19, 24, 28, 31, 32, 32, 29, 25, 19, 14]
PUST_P = [3, 2, 2, 1, 0, 0, 0, 1, 0, 1, 2, 3]

_t, _tty, _ = klimatogram(TAJGA_T, TAJGA_P, tmin=-40, tmax=30, pmax=80)
_p, _pty, _ = klimatogram(PUST_T, PUST_P, tmin=0, tmax=40, pmax=20)
S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Klimatogram: klimat umiarkowany kontynentalny chłodny (tajga)', svg=_t,
      znaczniki=[(kx(0), _tty(-38), 90, 222, 'Mroźna zima', 'Styczeń ok. −38°C (np. Jakuck)'),
                 (kx(6), _tty(19), 200, 30, 'Krótkie lato', 'Lipiec ok. 19°C; tylko 3–4 miesiące powyżej 10°C'),
                 (kx(7), 250 - 210 * 38 / 80, 190, 110, 'Opady letnie', 'Maksimum latem, rocznie ok. 210 mm'),
                 (kx(10), _tty(-27), 230, 200, 'Amplituda', 'Ok. 57°C — klimat skrajnie kontynentalny')],
      opis='Klimatogram autorski stacji we wschodniej Syberii (dane przybliżone).',
      uwaga='Mimo małych opadów klimat nie jest suchy: parowanie jest niewielkie, a wieczna zmarzlina zatrzymuje wodę w glebie — rośnie tajga.'),
 dict(typ='rysunek', tytul='Klimatogram: klimat zwrotnikowy suchy (pustynia)', svg=_p,
      znaczniki=[(kx(6), _pty(32), 200, 30, 'Upalne lato', 'Średnio ponad 30°C'),
                 (kx(0), _pty(13), 95, 90, 'Ciepła zima', 'Ok. 13°C'),
                 (kx(5), 247, 170, 200, 'Brak opadów', 'Rocznie ok. 15 mm — wyż zwrotnikowy')],
      opis='Klimatogram autorski stacji na Saharze (dane przybliżone).',
      uwaga='Na pustyniach duża jest dobowa amplituda temperatury — nocą bezchmurne niebo pozwala na szybkie wypromieniowanie ciepła.'),
]

S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Zrąb i rów tektoniczny',
      svg=('<rect class="gn" x="0" y="0" width="400" height="300"/>'
           '<path class="gl" d="M10 90 H118 L126 165 H274 L282 90 H390 V290 H10 Z"/>'
           + ''.join(f'<path class="{c}" d="M10 {y} H118 L{122 + 0} {y + 75 - 75} H10 Z"/>' for c, y in ())
           + '<path class="gp" d="M10 120 H120 L122 140 H10 Z M280 120 H390 V140 H278 Z M124 195 H276 L274 215 H126 Z"/>'
           '<path class="gc" d="M10 160 H122 L124 180 H10 Z M278 160 H390 V180 H276 Z M128 235 H272 L270 255 H130 Z"/>'
           '<path class="s" d="M114 70 L132 290 M286 70 L268 290"/>'
           + strz(105, 200, 105, 175, 's', 6) + strz(140, 225, 140, 250, 's', 6) + strz(295, 200, 295, 175, 's', 6) + strz(260, 225, 260, 250, 's', 6)
           + '<path class="gw" d="M150 165 H250 V172 H150 Z"/>'
           '<text class="tb" x="60" y="82" text-anchor="middle">zrąb</text><text class="tb" x="200" y="155" text-anchor="middle">rów</text><text class="tb" x="340" y="82" text-anchor="middle">zrąb</text>'),
      znaczniki=[(60, 92, 60, 30, 'Zrąb', 'Blok wyniesiony między uskokami (np. Śnieżnik)'),
                 (200, 168, 200, 115, 'Rów', 'Blok obniżony wzdłuż uskoków (np. Kotlina Kłodzka)'),
                 (120, 110, 160, 50, 'Uskok', 'Pęknięcie skorupy z przesunięciem bloków'),
                 (60, 130, 70, 225, 'Ta sama warstwa', 'Leży na różnej wysokości po obu stronach uskoku — dowód przesunięcia'),
                 (140, 238, 175, 275, 'Ruch w dół', 'Środkowy blok osiadł')],
      opis='Przekrój przez strukturę zrębowo-rowową.',
      uwaga='Przykłady: Sudety (zręby i rowy, np. Śnieżnik i Kotlina Kłodzka), rów Renu, Wielkie Rowy Afrykańskie (z jeziorami Tanganika i Malawi).'),
]

S['g-rzezba'] = [
 dict(typ='proces', tytul='Typy wybrzeży morskich — jak je rozpoznać', opis='Wybrzeża powstałe z zalania lądu i działalności morza.',
      kroki=[('Fiordowe', 'Zalane doliny lodowcowe (żłoby) — głębokie i wąskie zatoki, Norwegia.'),
             ('Szkierowe', 'Zalane wygłady i mutony — tysiące skalistych wysepek, Szwecja i Finlandia.'),
             ('Riasowe', 'Zalane doliny rzeczne w górach — Bretania, Galicja.'),
             ('Dalmatyńskie', 'Zalane równoległe pasma górskie — wyspy wzdłuż brzegu, Chorwacja.'),
             ('Mierzejowo-zalewowe', 'Mierzeje odcinają zalewy — polski Bałtyk (Zalew Wiślany).'),
             ('Klifowe', 'Abrazja podcina strome brzegi — Wolin, Orłowo.')],
      uwaga='Przy wybrzeżach z zalania lądu zawsze podaj, jaka forma została zalana.'),
]
