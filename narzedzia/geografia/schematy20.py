# Schematy geografii — porcja 20 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Odwzorowania kartograficzne ----------
_o = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
# walcowe
_o += '<rect class="gw ol" x="20" y="60" width="100" height="140"/>'
for y in (85, 110, 130, 150, 175):
    _o += f'<path class="s" d="M20 {y} H120" style="stroke-width:.8"/>'
for x in (40, 60, 80, 100):
    _o += f'<path class="s" d="M{x} 60 V200" style="stroke-width:.8"/>'
# stożkowe
_o += '<path class="gw ol" d="M200 60 L145 200 C180 215 220 215 255 200 Z"/>'
for t in (0.45, 0.65, 0.85):
    y = 60 + 140 * t
    _o += f'<path class="s" fill="none" d="M{200 - 55 * t:.0f} {y:.0f} C{200 - 20 * t:.0f} {y + 12 * t:.0f} {200 + 20 * t:.0f} {y + 12 * t:.0f} {200 + 55 * t:.0f} {y:.0f}" style="stroke-width:.8"/>'
for dx in (-30, -10, 10, 30):
    _o += f'<path class="s" d="M200 60 L{200 + dx * 1.8:.0f} {205}" style="stroke-width:.8"/>'
# azymutalne
_o += '<circle class="gw ol" cx="330" cy="130" r="60"/>'
for r in (20, 40):
    _o += f'<circle class="s" cx="330" cy="130" r="{r}" style="fill:none;stroke-width:.8"/>'
for a in range(0, 180, 30):
    dx, dy = 60 * math.cos(math.radians(a)), 60 * math.sin(math.radians(a))
    _o += f'<path class="s" d="M{330 - dx:.1f} {130 - dy:.1f} L{330 + dx:.1f} {130 + dy:.1f}" style="stroke-width:.8"/>'
_o += '<text class="tb" x="70" y="40" text-anchor="middle">walcowe</text><text class="tb" x="200" y="40" text-anchor="middle">stożkowe</text><text class="tb" x="330" y="40" text-anchor="middle">azymutalne</text>'
S['g-skala'] = [
 dict(typ='rysunek', tytul='Rodzaje odwzorowań kartograficznych (siatki)', svg=_o,
      znaczniki=[(70, 130, 40, 235, 'Siatka prostokątna', 'Południki i równoleżniki to proste prostopadłe — mapy świata (Merkator)'),
                 (200, 160, 215, 262, 'Łuki i promienie', 'Równoleżniki to łuki, południki zbiegają się — mapy średnich szerokości (Europa, Polska)'),
                 (330, 130, 350, 285, 'Okręgi i promienie', 'Równoleżniki to okręgi wokół bieguna — mapy obszarów polarnych'),
                 (20, 60, 40, 20, 'Zniekształcenia', 'Każde odwzorowanie zniekształca kąty, odległości albo powierzchnie')],
      opis='Wygląd siatki kartograficznej w trzech podstawowych odwzorowaniach — rysunek autorski IndexLab.',
      uwaga='Rodzaj odwzorowania rozpoznasz po siatce: proste prostopadłe — walcowe; łuki równoleżników i zbiegające się południki — stożkowe; koncentryczne okręgi — azymutalne (biegunowe).'),
]

# ---------- 2. Cykl skalny ----------
_c = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
for (x, y, cls, t) in ((200, 50, 'gm2', 'magma'), (330, 200, 'gs', 'skały magmowe'), (200, 260, 'gp', 'skały osadowe'), (70, 200, 'gc', 'skały przeobrażone')):
    _c += f'<rect class="{cls} ol" x="{x - 60}" y="{y - 18}" width="120" height="36" rx="10"/><text class="tb" x="{x}" y="{y + 5}" text-anchor="middle">{t}</text>'
_c += strz(250, 70, 320, 178, 'hot') + strz(300, 220, 250, 250, 's') + strz(140, 250, 90, 222, 's') + strz(80, 178, 150, 70, 'hot')
_c += strz(320, 222, 130, 205, 's') + strz(330, 182, 255, 60, 'hot')
S['g-skaly'] = [
 dict(typ='rysunek', tytul='Cykl skalny (przemiany skał)', svg=_c,
      znaczniki=[(290, 125, 350, 110, 'Krzepnięcie', 'Magma stygnie w głębi lub na powierzchni (granit, bazalt)'),
                 (275, 235, 340, 215, 'Wietrzenie i sedymentacja', 'Okruchy są transportowane i osadzane, potem scementowane (diageneza)'),
                 (115, 236, 60, 292, 'Metamorfizm', 'Wysoka temperatura i ciśnienie przeobrażają skałę (wapień → marmur)'),
                 (115, 125, 60, 145, 'Przetopienie', 'W głębi skała topi się i znów staje się magmą'),
                 (225, 213, 230, 170, 'Skrót cyklu', 'Każda skała może zostać przeobrażona lub zwietrzała bez przejścia całego cyklu')],
      opis='Uproszczony schemat obiegu materii skalnej — rysunek autorski IndexLab.',
      uwaga='Przykłady przemian: granit → gnejs (metamorfizm), piaskowiec → kwarcyt, wapień → marmur, granit → piasek → piaskowiec (wietrzenie i diageneza).'),
]

# ---------- 3. Ustrój monsunowy (hydrogram) ----------
_h = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
Q = [10, 8, 8, 12, 20, 55, 95, 100, 80, 40, 20, 12]
x0, x1, y0, y1 = 45, 375, 250, 40
w = (x1 - x0) / 12
pts = ' '.join(f'{x0 + (i + .5) * w:.0f},{y0 - (y0 - y1) * q / 100:.0f}' for i, q in enumerate(Q))
_h += f'<path class="gw2" d="M{x0 + w / 2:.0f} {y0} L{pts.replace(" ", " L")} L{x0 + 11.5 * w:.0f} {y0} Z" style="opacity:.5"/>'
_h += f'<polyline class="cold" fill="none" points="{pts}" style="stroke-width:2.4"/>'
_h += f'<path class="s" d="M{x0} {y1} V{y0} H{x1}"/>'
_h += ''.join(f'<text class="ts" x="{x0 + (i + .5) * w:.0f}" y="{y0 + 14}" text-anchor="middle">{m}</text>' for i, m in enumerate('IFMAMJJASOND'))
_h += f'<text class="ts" x="{x0 - 6}" y="{y1 + 4}" text-anchor="end">max</text><text class="ts" x="{x0 - 6}" y="{y0}" text-anchor="end">min</text>'
_h += '<text class="tb" x="210" y="285" text-anchor="middle">przepływ rzeki w ciągu roku (np. Ganges)</text>'
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Ustrój monsunowy rzeki (hydrogram)', svg=_h,
      znaczniki=[(237, 50, 300, 30, 'Wezbranie letnie', 'VII–IX — ulewy monsunu letniego (i topnienie w Himalajach)'),
                 (100, 230, 120, 180, 'Niżówka zimowa', 'Monsun zimowy — sucha pora, niski przepływ'),
                 (183, 175, 110, 120, 'Gwałtowny wzrost', 'Czerwiec — nadejście monsunu letniego'),
                 (320, 200, 340, 160, 'Opadanie', 'Jesień — koniec pory deszczowej')],
      opis='Schematyczny hydrogram rzeki o ustroju monsunowym (wartości względne) — rysunek autorski IndexLab.',
      uwaga='Rzeki monsunowe (Ganges, Brahmaputra, Mekong, Jangcy) mają ogromne letnie wezbrania i powodzie; zimą przepływy są wielokrotnie mniejsze. Porównaj z ustrojem śnieżnym rzek Polski (wezbranie wiosenne).'),
]

# ---------- 4. Strefowość od równika do bieguna ----------
_s = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
zones = [('gf2', 'las równikowy', 'ferralitowe'), ('gt', 'sawanna', 'czerwone'), ('gp', 'pustynia', 'pustynne'),
         ('gl', 'makia / step', 'czarnoziemy'), ('gf', 'las liściasty', 'brunatne'), ('gf2', 'tajga', 'bielicowe'), ('gi', 'tundra', 'glejowe')]
bw = 400 / len(zones)
for i, (c, r, g) in enumerate(zones):
    x = i * bw
    _s += f'<rect class="{c} ol" x="{x:.1f}" y="70" width="{bw:.1f}" height="110"/>'
    _s += f'<rect class="gg ol" x="{x:.1f}" y="180" width="{bw:.1f}" height="60"/>'
    _s += f'<text class="ts" x="{x + bw / 2:.1f}" y="256" text-anchor="middle">{g}</text>'
_s += '<text class="tb" x="8" y="60">0° (równik)</text><text class="tb" x="392" y="60" text-anchor="end">90° (biegun)</text>'
_s += strz(20, 272, 380, 272, 's')
_s += '<text class="ts" x="200" y="290" text-anchor="middle">maleje dopływ energii słonecznej</text>'
S['g-biomy'] = [
 dict(typ='rysunek', tytul='Strefowość roślinności i gleb od równika do bieguna', svg=_s,
      znaczniki=[(28, 120, 50, 20, 'Las równikowy', 'Ciepło i wilgotno cały rok — gleby ferralitowe'),
                 (142, 120, 160, 42, 'Pustynia', 'Wyż zwrotnikowy — skrajny niedobór wody'),
                 (200, 120, 250, 62, 'Step', 'Czarnoziemy — najżyźniejsze gleby świata'),
                 (314, 120, 300, 225, 'Tajga', 'Gleby bielicowe pod lasem iglastym'),
                 (371, 120, 360, 250, 'Tundra', 'Wieloletnia zmarzlina, krótkie lato')],
      opis='Uproszczony profil stref roślinnych i glebowych półkuli północnej (bez stref astrefowych) — rysunek autorski IndexLab.',
      uwaga='Strefowość wynika z rozkładu energii słonecznej i opadów. Czynniki astrefowe (góry, prądy morskie, odległość od oceanu) zaburzają ten układ — np. pustynia nadbrzeżna przy zimnym prądzie.'),
]

# ---------- 5. Formy terenu na mapie poziomicowej ----------
_p = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
# skarpa
_p += '<path class="s" d="M20 60 H180" style="stroke-width:1.6"/>'
for x in range(24, 180, 8):
    _p += f'<path class="s" d="M{x} 60 v8" style="stroke-width:1"/>'
_p += '<text class="ts" x="100" y="45" text-anchor="middle">skarpa</text>'
# wąwóz
_p += '<path class="s" d="M220 40 C230 90 235 140 230 180" style="fill:none;stroke-width:1.6"/><path class="s" d="M260 40 C255 90 255 140 262 180" style="fill:none;stroke-width:1.6"/>'
for y in range(48, 180, 10):
    _p += f'<path class="s" d="M{228 + (y - 40) * 0.03:.0f} {y} h7" style="stroke-width:1"/><path class="s" d="M{256 - (y - 40) * 0.01:.0f} {y} h-7" style="stroke-width:1"/>'
_p += '<text class="ts" x="245" y="30" text-anchor="middle">wąwóz</text>'
# wydmy
for dx in (0, 40):
    _p += f'<path class="s" fill="none" d="M{300 + dx} 120 C{310 + dx} 90 {340 + dx} 90 {350 + dx} 120" style="stroke-width:1.4"/>'
    _p += f'<path class="s" fill="none" d="M{310 + dx} 120 C{318 + dx} 102 {332 + dx} 102 {340 + dx} 120" style="stroke-width:1.2"/>'
_p += '<rect class="gp" x="295" y="125" width="100" height="0"/>'
_p += '<text class="ts" x="345" y="140" text-anchor="middle">wydmy</text>'
# zagłębienie
_p += '<ellipse class="s" cx="90" cy="200" rx="60" ry="35" style="fill:none;stroke-width:1.4"/><ellipse class="s" cx="90" cy="200" rx="35" ry="20" style="fill:none;stroke-width:1.4"/>'
for a in range(0, 360, 45):
    x = 90 + 35 * math.cos(math.radians(a)); y = 200 + 20 * math.sin(math.radians(a))
    _p += f'<path class="s" d="M{x:.0f} {y:.0f} L{90 + 28 * math.cos(math.radians(a)):.0f} {200 + 15 * math.sin(math.radians(a)):.0f}" style="stroke-width:1"/>'
_p += '<text class="ts" x="90" y="255" text-anchor="middle">zagłębienie bezodpływowe</text>'
# kopiec / wzgórze z punktem wysokościowym
_p += '<circle class="s" cx="300" cy="220" r="45" style="fill:none;stroke-width:1.4"/><circle class="s" cx="300" cy="220" r="25" style="fill:none;stroke-width:1.4"/><circle class="d" cx="300" cy="220" r="3"/>'
_p += '<text class="tb" x="308" y="216">214,5</text><text class="ts" x="300" y="285" text-anchor="middle">kulminacja z punktem wysokościowym</text>'
S['g-poziomice'] = [
 dict(typ='rysunek', tytul='Formy terenu na mapie topograficznej — sygnatury', svg=_p,
      znaczniki=[(100, 64, 140, 95, 'Ząbki skarpy', 'Skierowane w dół skarpy'),
                 (245, 120, 300, 70, 'Wąwóz', 'Strome ściany z obu stron — ząbki do środka'),
                 (325, 105, 360, 175, 'Wydmy', 'Łukowate, drobne poziomice na terenie piaszczystym'),
                 (90, 200, 170, 140, 'Kreski spadu', 'Skierowane do środka — zagłębienie, nie wzgórze'),
                 (300, 220, 230, 260, 'Punkt wysokościowy', 'Kropka z liczbą — wysokość n.p.m. szczytu')],
      opis='Wybrane sygnatury form rzeźby na mapie topograficznej (uproszczone) — rysunek autorski IndexLab.',
      uwaga='Na maturze często trzeba rozpoznać formę z mapy: wąwóz (skarpy po obu stronach), wydmy (łuki poziomic), zagłębienie (kreski spadu do środka), hałdę i wyrobisko (formy antropogeniczne przy kopalniach).'),
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
