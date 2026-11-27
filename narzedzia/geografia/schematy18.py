# Schematy geografii — porcja 18 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Piramida wieku Polski (przybliżona, ok. 2024) ----------
# udział % grupy w ludności ogółem (mężczyźni, kobiety) — wartości przybliżone
_pol = [(2.0, 1.9), (2.6, 2.5), (2.6, 2.5), (2.4, 2.2), (2.5, 2.3), (2.9, 2.8), (3.6, 3.5), (4.1, 4.0), (3.9, 3.8),
        (3.3, 3.3), (2.9, 3.0), (2.7, 2.9), (3.0, 3.4), (3.1, 3.7), (2.2, 2.9), (1.2, 2.0), (0.6, 1.3), (0.3, 0.9)]
_gr = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85+']
_p = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
k = 30  # px na 1%
for i, (m, f) in enumerate(_pol):
    y = 262 - i * 13
    _p += f'<rect class="gw2 ol" x="{200 - m * k:.1f}" y="{y}" width="{m * k:.1f}" height="11"/>'
    _p += f'<rect class="hotf ol" x="200" y="{y}" width="{f * k:.1f}" height="11" style="opacity:.75"/>'
    if i % 2 == 0:
        _p += f'<text class="ts" x="394" y="{y + 9}" text-anchor="end">{_gr[i]}</text>'
_p += '<path class="s" d="M200 20 V275"/>'
for v in (2, 4):
    _p += f'<text class="ts" x="{200 - v * k}" y="292" text-anchor="middle">{v}%</text><text class="ts" x="{200 + v * k}" y="292" text-anchor="middle">{v}%</text>'
_p += '<text class="tb" x="20" y="20">mężczyźni</text><text class="tb" x="300" y="20">kobiety</text>'
S['g-pl-ludnosc'] = [
 dict(typ='rysunek', tytul='Piramida wieku i płci ludności Polski (ok. 2024)', svg=_p,
      znaczniki=[(85, 168, 40, 135, 'Wyż lat 80.', 'Roczniki 35–44 lata — echo powojennego wyżu'),
                 (110, 86, 40, 35, 'Wyż powojenny', 'Roczniki ok. 65–74 lata (urodzeni w latach 50.)'),
                 (150, 262, 300, 280, 'Zwężona podstawa', 'Mało urodzeń — dzietność ok. 1,1–1,2'),
                 (222, 40, 300, 75, 'Przewaga kobiet', 'Kobiety żyją dłużej — feminizacja wśród starszych'),
                 (125, 197, 40, 215, 'Niż lat 90.–2000.', 'Mniej osób 20–29 lat')],
      opis='Piramida autorska IndexLab na podstawie przybliżonych danych GUS (udział grup 5-letnich w %).',
      uwaga='Kształt regresywny (zbliżony do urny): zwężona podstawa i liczne roczniki średnie. Skutki: starzenie się społeczeństwa, rosnące obciążenie emerytalne, w przyszłości spadek liczby ludności w wieku produkcyjnym.'),
]

# ---------- 2. Kontynent hipotetyczny — strefy klimatyczne ----------
_k = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
_k += '<path class="gl ol" d="M150 15 C230 10 300 30 290 60 C285 100 270 120 250 150 C240 190 230 230 205 285 C190 285 175 230 165 190 C150 140 110 110 100 70 C95 35 120 18 150 15 Z"/>'
_k += '<path class="gf" d="M160 140 H255 V160 H170 Z" style="opacity:.8"/>'
_k += '<path class="gp" d="M120 95 H280 V125 H140 Z" style="opacity:.8"/><path class="gp" d="M175 175 H240 V205 H185 Z" style="opacity:.8"/>'
_k += '<path class="gt" d="M105 60 H290 V90 H115 Z" style="opacity:.7"/>'
for y, lab in ((150, '0°'), (110, '23°N'), (192, '23°S'), (40, '50°N'), (260, '50°S')):
    _k += f'<path class="dash" d="M0 {y} H400"/><text class="ts" x="4" y="{y - 3}">{lab}</text>'
_k += strz(55, 95, 95, 120, 'cold') + strz(345, 120, 300, 110, 'hot')
S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Strefy klimatyczne na kontynencie modelowym', svg=_k,
      znaczniki=[(210, 150, 300, 165, 'Klimat równikowy', 'Opady cały rok — strefa zbieżności'),
                 (200, 110, 230, 230, 'Pustynie zwrotnikowe', 'Wyż zwrotnikowy — osiadanie powietrza'),
                 (112, 112, 30, 140, 'Pustynia nadbrzeżna', 'Zachodnie wybrzeże przy zimnym prądzie — pustynia sięga do morza'),
                 (280, 95, 350, 60, 'Wilgotne wybrzeże E', 'Wschodnie wybrzeże: ciepły prąd i pasaty znad oceanu'),
                 (200, 75, 330, 25, 'Strefa umiarkowana', 'Niże i wiatry zachodnie')],
      opis='Model rozkładu klimatów na idealnym kontynencie — rysunek autorski IndexLab.',
      uwaga='Strefy klimatyczne układają się równoleżnikowo, ale zachodnie i wschodnie wybrzeża się różnią: na zachodzie w strefie zwrotnikowej płyną prądy zimne (pustynie nadbrzeżne: Atakama, Namib), na wschodzie — ciepłe (klimaty wilgotne).'),
]

# ---------- 3. Wtórne zasolenie gleby przy nawadnianiu ----------
_z = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_z += '<path class="gg ol" d="M0 120 H400 V300 H0 Z"/>'
_z += '<path class="gw2" d="M0 215 H400 V300 H0 Z" style="opacity:.6"/>'
_z += '<path class="cold" d="M0 215 H400" style="stroke-width:2"/>'
_z += '<path class="gw2" d="M0 165 H400 V215 H0 Z" style="opacity:.3"/>'
_z += '<path class="dash" d="M0 165 H400"/>'
for x in (40, 110, 180, 250, 320, 380):
    _z += f'<circle class="gs2" cx="{x}" cy="117" r="2.5"/><circle class="gs2" cx="{x + 15}" cy="116" r="2"/>'
for x in (70, 210, 340):
    _z += strz(x, 190, x, 130, 'cold')
_z += strz(150, 112, 150, 60, 'hot') + strz(290, 112, 290, 60, 'hot')
_z += '<path class="gw ol" d="M20 105 H90 V120 H20 Z"/>'
_z += '<text class="ts" x="392" y="292" text-anchor="end">wody gruntowe</text>'
S['g-gleby'] = [
 dict(typ='rysunek', tytul='Wtórne zasolenie gleby przy nawadnianiu', svg=_z,
      znaczniki=[(55, 112, 40, 40, 'Kanał nawadniający', 'Woda zasila pole i podnosi poziom wód gruntowych'),
                 (250, 165, 230, 195, 'Podniesione zwierciadło', 'Woda gruntowa zbliża się do powierzchni'),
                 (70, 150, 40, 150, 'Podsiąk kapilarny', 'Woda z rozpuszczonymi solami wędruje w górę'),
                 (290, 80, 330, 70, 'Silne parowanie', 'Klimat suchy — woda odparowuje'),
                 (180, 117, 220, 90, 'Skorupa solna', 'Sole zostają na powierzchni — gleba jałowieje')],
      opis='Mechanizm zasolenia gleb na obszarach nawadnianych w klimacie suchym — rysunek autorski IndexLab.',
      uwaga='Przykłady: Azja Środkowa (dorzecze Amu-darii), Pakistan, Mezopotamia, Australia (dorzecze Murray). Zapobieganie: drenaż, nawadnianie kropelkowe, ograniczenie ilości wody, płukanie gleby.'),
]

# ---------- 4. Wyspa ciepła miasta ----------
_c = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_c += '<path class="gt ol" d="M0 240 H400 V300 H0 Z"/>'
for x, h in ((140, 40), (160, 70), (180, 110), (200, 90), (220, 120), (240, 60), (260, 45), (110, 25), (290, 25)):
    _c += f'<rect class="gs2 ol" x="{x - 9}" y="{240 - h}" width="18" height="{h}"/>'
for x in (30, 60, 340, 370):
    _c += f'<path class="gf ol" d="M{x} 240 l9 -26 l9 26 Z"/>'
_c += '<path class="hot" fill="none" d="M10 90 C80 88 100 75 130 55 C170 30 230 30 270 55 C300 75 320 88 390 90" style="stroke-width:2.4"/>'
_c += '<text class="ts" x="8" y="80">temperatura powietrza</text>'
_c += '<text class="tb" x="40" y="262">wieś</text><text class="tb" x="200" y="262" text-anchor="middle">centrum</text><text class="tb" x="355" y="262">wieś</text>'
S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Miejska wyspa ciepła (profil temperatury)', svg=_c,
      znaczniki=[(200, 33, 270, 20, 'Szczyt wyspy ciepła', 'Centrum cieplejsze nawet o kilka °C, najbardziej nocą'),
                 (220, 130, 300, 140, 'Zabudowa', 'Beton i asfalt magazynują ciepło, mało parowania'),
                 (45, 230, 40, 170, 'Teren wiejski', 'Roślinność i parowanie chłodzą powietrze'),
                 (130, 56, 60, 40, 'Spadek ku obrzeżom', 'Temperatura maleje wraz z odległością od centrum')],
      opis='Schematyczny profil temperatury przez miasto i jego otoczenie — rysunek autorski IndexLab.',
      uwaga='Przyczyny wyspy ciepła: ciemne, nieprzepuszczalne powierzchnie, emisja ciepła (ruch, ogrzewanie, klimatyzacja), mała ilość zieleni, ograniczone przewietrzanie. Łagodzenie: zielone dachy, parki, zbiorniki wodne, jasne powierzchnie.'),
]

# ---------- 5. Profil dna oceanu ----------
_o = '<rect class="gn" x="0" y="0" width="400" height="60"/><rect class="gw" x="0" y="60" width="400" height="240"/>'
_o += '<path class="gl ol" d="M0 40 H60 L66 75 H120 L150 85 L200 220 L240 240 H290 L305 290 L315 290 L330 200 L360 150 L400 130 V300 H0 Z"/>'
_o += '<path class="dash" d="M0 60 H400"/><text class="ts" x="392" y="56" text-anchor="end">poziom morza</text>'
S['g-oceany'] = [
 dict(typ='rysunek', tytul='Profil dna oceanu: szelf, stok, rów', svg=_o,
      znaczniki=[(100, 75, 140, 110, 'Szelf', 'Płytka część dna do ok. 200 m — łowiska, ropa i gaz'),
                 (175, 140, 110, 160, 'Stok kontynentalny', 'Stromy spadek do głębi oceanicznej'),
                 (265, 240, 150, 260, 'Równina abisalna', 'Płaskie dno na głębokości 4–6 km'),
                 (310, 288, 360, 280, 'Rów oceaniczny', 'Najgłębsze miejsca nad strefą subdukcji (do ok. 11 km)'),
                 (360, 150, 340, 100, 'Łuk wysp / góry', 'Wypiętrzenie po drugiej stronie rowu')],
      opis='Schematyczny przekrój przez brzeg kontynentu i dno oceanu (pionowo przesadzony) — rysunek autorski IndexLab.',
      uwaga='Szelf to podwodne przedłużenie kontynentu — najbardziej produktywna biologicznie i gospodarczo część oceanu (np. Morze Północne, Zatoka Perska). Rowy oceaniczne występują głównie wokół Pacyfiku.'),
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
