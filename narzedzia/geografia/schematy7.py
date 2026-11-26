# Schematy geografii — porcja 7 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}


def klimatogram(temp, opady, tmin=-40, tmax=30, pmax=150):
    x0, x1, y0, y1 = 50, 370, 260, 40
    w = (x1 - x0) / 12
    out = f'<path class="s" d="M{x0} {y1} V{y0} H{x1} V{y1}"/>'
    for i, p in enumerate(opady):
        h = (y0 - y1) * p / pmax
        out += f'<rect class="f" x="{x0 + i * w + 3:.1f}" y="{y0 - h:.1f}" width="{w - 6:.1f}" height="{h:.1f}"/>'
    pts = ' '.join(f'{x0 + (i + 0.5) * w:.1f},{y0 - (y0 - y1) * (t - tmin) / (tmax - tmin):.1f}' for i, t in enumerate(temp))
    out += f'<polyline class="s2" fill="none" points="{pts}"/>'
    yz = y0 - (y0 - y1) * (0 - tmin) / (tmax - tmin)
    out += f'<path class="dash" d="M{x0} {yz:.1f} H{x1}"/><text class="t" x="15" y="{yz + 4:.1f}">0°C</text>'
    for i, m in enumerate('IFMAMJJASOND'):
        out += f'<text class="t" x="{x0 + (i + 0.3) * w:.1f}" y="278">{m}</text>'
    return out


def ty(t, tmin=-40, tmax=30):
    return 260 - 220 * (t - tmin) / (tmax - tmin)


TAJGA_T = [-38, -33, -20, -5, 7, 16, 19, 15, 6, -8, -27, -36]
TAJGA_P = [8, 6, 5, 8, 15, 30, 40, 38, 22, 15, 12, 9]
PUST_T = [13, 15, 19, 24, 28, 31, 32, 32, 29, 25, 19, 14]
PUST_P = [3, 2, 2, 1, 0, 0, 0, 1, 0, 1, 2, 3]

S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Klimatogram: klimat umiarkowany kontynentalny chłodny (tajga)',
      svg=klimatogram(TAJGA_T, TAJGA_P),
      znaczniki=[(63, ty(-38), 90, 250, 'Mroźna zima', 'Styczeń ok. −38°C (np. Jakuck)'),
                 (237, ty(19), 220, 70, 'Krótkie, ciepłe lato', 'Lipiec ok. 19°C'),
                 (250, 200, 300, 120, 'Opady letnie', 'Maksimum latem, rocznie ok. 210 mm'),
                 (330, ty(-27), 330, 245, 'Amplituda', 'Ok. 57°C — klimat skrajnie kontynentalny')],
      opis='Klimatogram autorski dla stacji we wschodniej Syberii (dane przybliżone).',
      uwaga='Mimo małych opadów klimat nie jest suchy — niskie parowanie i wieczna zmarzlina zatrzymują wodę.'),
 dict(typ='rysunek', tytul='Klimatogram: klimat zwrotnikowy suchy (pustynia)',
      svg=klimatogram(PUST_T, PUST_P, tmin=0, tmax=40, pmax=50),
      znaczniki=[(237, ty(32, 0, 40), 230, 60, 'Upalne lato', 'Średnio ponad 30°C'),
                 (63, ty(13, 0, 40), 80, 140, 'Ciepła zima', 'Ok. 13°C'),
                 (200, 255, 200, 230, 'Brak opadów', 'Rocznie ok. 15 mm')],
      opis='Klimatogram autorski dla stacji na Saharze (dane przybliżone).',
      uwaga='Na pustyniach duża jest dobowa amplituda temperatury — noce bywają chłodne.'),
]

S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Zrąb i rów tektoniczny',
      svg=('<path class="f2" d="M20 120 H120 L130 200 L270 200 L280 120 H380 V280 H20 Z"/>'
           '<path style="fill:#ffcc80" d="M20 150 H120 L124 180 H276 L280 150 H380 V165 H282 L280 215 H120 L118 165 H20 Z"/>'
           '<path class="s" d="M120 110 L135 290 M280 110 L265 290"/>'
           '<path class="s2" d="M200 140 V185 M192 175 L200 187 L208 175"/>'),
      znaczniki=[(70, 120, 60, 95, 'Zrąb', 'Blok wyniesiony między uskokami'),
                 (200, 200, 200, 235, 'Rów tektoniczny', 'Blok obniżony wzdłuż uskoków'),
                 (127, 150, 150, 100, 'Uskok', 'Pęknięcie z przesunięciem bloków'),
                 (70, 158, 40, 260, 'Warstwa przewodnia', 'Ta sama warstwa na różnych wysokościach')],
      opis='Przekrój przez strukturę zrębowo-rowową.',
      uwaga='Przykłady: zrąb — Sudety (Śnieżnik), rów — Kotlina Kłodzka; rowy na świecie: Wielkie Rowy Afrykańskie, rów Renu.'),
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
