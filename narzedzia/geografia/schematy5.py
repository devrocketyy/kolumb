# Schematy geografii — porcja 5 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- plama gorąca ----------
_wys = [(40, 6, 'atol'), (115, 14, '5 mln lat'), (185, 24, '3 mln lat'), (250, 34, '1 mln lat'), (320, 52, '0')]
_hs = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<rect class="gw2" x="0" y="110" width="400" height="40"/>'
       '<path class="gs2" d="M0 150 H400 V190 H0 Z"/><path class="gs" d="M0 150 H400 V158 H0 Z" opacity="0.8"/>'
       '<rect class="gm2" x="0" y="190" width="400" height="110"/>'
       '<path class="gm" d="M300 300 C292 250 310 215 312 190 L328 190 C330 215 348 250 340 300 Z"/>'
       '<path class="gm" d="M316 190 L318 110 L322 110 L324 190 Z"/>')
for x, h, t in _wys:
    _hs += f'<path class="gs2 ol" d="M{x - h * 1.0:.0f} 150 Q{x} {110 - h * 2.0:.0f} {x + h * 1.0:.0f} 150 Z"/>'
    _hs += f'<text class="ts" x="{x}" y="205" text-anchor="middle">{t}</text>'
_hs += ('<ellipse class="gp" cx="40" cy="110" rx="14" ry="3"/>'
        '<path class="gm" d="M316 12 L320 6 L324 12 Z"/><path class="gm" d="M320 12 C334 40 338 70 346 108 L340 110 C332 72 328 44 318 14 Z" opacity="0.9"/>'
        '<path class="gk" d="M300 14 q-8 -10 6 -14 q10 -8 20 2 q14 -2 12 10 q-6 8 -20 4 q-10 6 -18 -2 Z"/>'
        + strz(250, 232, 150, 232, 's', 8)
        + '<text class="ts" x="200" y="248" text-anchor="middle">ruch płyty ~8 cm/rok</text>'
        '<text class="ts" x="8" y="292">płaszcz (astenosfera)</text><text class="ts" x="8" y="145">dno oceanu</text>')
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Plama gorąca i łańcuch wysp', svg=_hs,
      znaczniki=[(320, 50, 240, 30, 'Czynny wulkan', 'Nad plamą gorąca — tarczowy, lawa rzadka (np. Hawaje)'),
                 (250, 85, 180, 60, 'Wygasły wulkan', 'Przesunięty z płytą poza plamę'),
                 (40, 108, 60, 88, 'Atol', 'Pierścień raf na zatopionej wyspie'),
                 (322, 270, 290, 285, 'Pióropusz płaszcza', 'Gorąca materia z głębi płaszcza — plama stoi w miejscu'),
                 (170, 232, 140, 270, 'Ruch płyty', 'Płyta przesuwa się nad nieruchomą plamą')],
      opis='Powstawanie łańcucha wysp wulkanicznych nad plamą gorąca (wiek wysp przybliżony).',
      uwaga='Wiek wysp rośnie w kierunku ruchu płyty — to jeden z dowodów na przesuwanie się płyt. Starsze wyspy są niższe: wulkany wygasają, erodują i osiadają.'),
]

# ---------- struktura zatrudnienia ----------
_kraje = [('Kraj A', 70, 10, 20), ('Kraj B', 30, 30, 40), ('Kraj C', 3, 20, 77)]
_zy = lambda p: 255 - p * 2.1
_za = ''.join(f'<path class="dash" d="M50 {_zy(p):.0f} H280"/><text class="ts" x="44" y="{_zy(p) + 3:.0f}" text-anchor="end">{p}%</text>' for p in (0, 25, 50, 75, 100))
for i, (n, r, pz, u) in enumerate(_kraje):
    x = 70 + i * 72
    y = 255
    for v, cl in ((r, 'gf'), (pz, 'gs2'), (u, 'gw2')):
        _za += f'<rect class="{cl} ol" x="{x}" y="{y - v * 2.1:.1f}" width="46" height="{v * 2.1:.1f}"/>'
        if v >= 8:
            _za += f'<text class="tb" x="{x + 23}" y="{y - v * 1.05 + 4:.1f}" text-anchor="middle">{v}</text>'
        y -= v * 2.1
    _za += f'<text class="tb" x="{x + 23}" y="272" text-anchor="middle">{n}</text>'
_za += ('<path class="s" d="M50 40 V255 H280"/>'
        + ''.join(f'<rect class="{c} ol" x="300" y="{y}" width="12" height="12"/><text class="ts" x="318" y="{y + 10}">{t}</text>' for c, y, t in (('gw2', 200, 'usługi'), ('gs2', 220, 'przemysł'), ('gf', 240, 'rolnictwo'))))
S['g-uslugi'] = [
 dict(typ='rysunek', tytul='Struktura zatrudnienia a poziom rozwoju', svg=_za,
      znaczniki=[(93, 45, 100, 22, 'Rolniczy', 'Kraj A: 70% w rolnictwie — gospodarka przedprzemysłowa'),
                 (165, 45, 180, 22, 'Przemysłowy', 'Kraj B: duży udział przemysłu, usługi rosną'),
                 (237, 45, 276, 22, 'Usługowy', 'Kraj C: 77% w usługach — postindustrialny')],
      opis='Udział sektorów gospodarki w zatrudnieniu (%) — dane umowne.',
      uwaga='Teoria trzech sektorów (Fisher–Clark): wraz z rozwojem zatrudnienie przesuwa się z rolnictwa do przemysłu, a potem do usług. Polska: ok. 8% rolnictwo, 30% przemysł, 62% usługi.'),
]

S['g-rolnictwo'] = [
 dict(typ='proces', tytul='Typy rolnictwa — jak je rozpoznać', opis='Klucz do zadań z materiałem źródłowym.',
      kroki=[('Wysokie nakłady, wysokie plony z ha', 'Rolnictwo intensywne — Holandia, Belgia, Japonia.'),
             ('Ogromne gospodarstwa, maszyny, mało ludzi', 'Rolnictwo ekstensywne wysokotowarowe — USA, Kanada, Australia, Argentyna.'),
             ('Jedna roślina na eksport w tropikach', 'Gospodarka plantacyjna — kawa w Brazylii, herbata w Kenii, banany w Ekwadorze.'),
             ('Wypalanie lasu, uprawa kilka lat', 'Rolnictwo żarowe (wędrówkowe) — Afryka, Amazonia.'),
             ('Stada w ruchu za paszą', 'Pasterstwo koczownicze — Sahel, Mongolia.'),
             ('Wysoka praca ręczna, ryż na tarasach', 'Rolnictwo intensywne tradycyjne — Azja Monsunowa.')],
      uwaga='Na maturze zawsze łącz typ z cechą (nakłady, plony, towarowość) i przykładem regionu.'),
]

# ---------- strefy czasowe ----------
_st = ''.join(f'<rect class="{c}" x="{20 + i * 90}" y="40" width="90" height="190"/>' for i, c in enumerate(('gw', 'gt', 'gp', 'gc')))
_st += ''.join(f'<path class="dash" d="M{65 + i * 90} 40 V230"/><text class="ts" x="{65 + i * 90}" y="34" text-anchor="middle">{d}</text>' for i, d in enumerate(('0°', '15°E', '30°E', '45°E')))
_st += '<path class="s" d="M20 40 H380 V230 H20 Z"/>'
for i, (g, mia) in enumerate((('12:00', 'Londyn'), ('13:00', 'Warszawa'), ('14:00', 'Kijów'), ('15:00', 'Moskwa'))):
    cx = 65 + i * 90
    _a = math.radians(i * 30)
    _st += (f'<circle class="f" cx="{cx}" cy="190" r="16"/><path class="s" d="M{cx} 190 V{176} M{cx} 190 L{cx + 9 * math.sin(_a):.1f} {190 - 9 * math.cos(_a):.1f}" style="stroke-width:2.4"/>'
            f'<text class="tb" x="{cx}" y="252" text-anchor="middle">{g}</text><text class="ts" x="{cx}" y="268" text-anchor="middle">{mia}</text>'
            f'<text class="tb" x="{cx}" y="130" text-anchor="middle">UTC{"+" + str(i) if i else "+0"}</text>')
_st += '<text class="ts" x="200" y="290" text-anchor="middle">czas strefowy, gdy w Londynie jest 12:00 (zima)</text>'
S['g-obrotowy'] = [
 dict(typ='rysunek', tytul='Strefy czasowe wokół Polski', svg=_st,
      znaczniki=[(65, 100, 100, 52, 'Strefa UTC+0', 'Środkowy południk 0° (Greenwich)'),
                 (155, 100, 190, 70, 'Polska', 'Strefa UTC+1 (południk 15°E), latem czas UTC+2'),
                 (335, 100, 300, 52, 'Moskwa', 'UTC+3 przez cały rok'),
                 (110, 210, 135, 215, 'Granica strefy', 'Co 15° — 1 godzina różnicy; w praktyce granice biegną wzdłuż granic państw')],
      opis='Uproszczony układ stref czasowych w Europie (każda strefa ma szerokość 15°).',
      uwaga='Południk środkowy strefy UTC+1 to 15°E — przechodzi m.in. przez Zgorzelec i okolice Stargardu. Na wschód od niego Słońce góruje przed 12:00 czasu strefowego.'),
]
