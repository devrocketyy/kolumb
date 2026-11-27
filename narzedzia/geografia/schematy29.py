# Schematy geografii — porcja 29 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Ryft kontynentalny ----------
_r = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_r += '<path class="gl ol" d="M0 110 H150 L175 180 H225 L250 110 H400 V170 H0 Z"/>'
_r += '<path class="gs ol" d="M0 170 H400 V230 H0 Z"/>'
_r += '<path class="hotf ol" d="M0 230 H400 V300 H0 Z"/>'
_r += '<path class="hotf ol" d="M180 230 C185 210 195 200 200 180 C205 200 215 210 220 230 Z"/>'
_r += '<path class="gw ol" d="M178 180 H222 V172 H178 Z"/>'
_r += '<path class="s" d="M150 110 L175 180 M250 110 L225 180" style="stroke-width:2"/>'
_r += strz(140, 140, 60, 140, 's') + strz(260, 140, 340, 140, 's')
_r += strz(160, 270, 80, 270, 'hot') + strz(240, 270, 320, 270, 'hot')
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Ryft kontynentalny — rozrywanie kontynentu', svg=_r,
      znaczniki=[(200, 176, 230, 40, 'Rów ryftowy', 'Zapadlisko między uskokami, często z jeziorami (Tanganika, Bajkał)'),
                 (162, 145, 130, 40, 'Uskoki normalne', 'Bloki skorupy zsuwają się w dół'),
                 (200, 215, 240, 205, 'Magma', 'Wznosi się pod ryftem — wulkany (Kilimandżaro)'),
                 (170, 270, 160, 205, 'Rozchodzenie się płyt', 'Prądy konwekcyjne w płaszczu rozciągają skorupę')],
      opis='Przekrój przez ryft kontynentalny na granicy rozbieżnej — rysunek autorski IndexLab.',
      uwaga='Wielki Rów Wschodnioafrykański to ryft w początkowym stadium. Gdy rozerwanie się pogłębi, wkracza morze (Morze Czerwone), a w końcu powstaje ocean z grzbietem śródoceanicznym (Atlantyk).'),
]

# ---------- 2. Model sektorowy Hoyta ----------
_h = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
cx, cy, R = 200, 155, 105
sek = [(0, 40, 'gp'), (40, 80, 'gm'), (80, 140, 'gt'), (140, 180, 'gm'), (180, 230, 'gs2'), (230, 290, 'gt'), (290, 330, 'gc'), (330, 360, 'gt')]
for a1, a2, c in sek:
    p1 = (cx + R * math.cos(math.radians(a1)), cy - R * math.sin(math.radians(a1)))
    p2 = (cx + R * math.cos(math.radians(a2)), cy - R * math.sin(math.radians(a2)))
    _h += f'<path class="{c} ol" d="M{cx} {cy} L{p1[0]:.1f} {p1[1]:.1f} A{R} {R} 0 0 0 {p2[0]:.1f} {p2[1]:.1f} Z"/>'
_h += f'<circle class="hotf ol" cx="{cx}" cy="{cy}" r="28"/>'
_h += '<path class="cold" d="M200 155 L305 155" style="stroke-width:3"/><path class="s" d="M200 155 L126 229" style="stroke-width:3"/>'
S['g-urbanizacja'] = [
 dict(typ='rysunek', tytul='Model sektorowy miasta (Hoyt)', svg=_h,
      znaczniki=[(235, 94, 245, 20, 'Sektor przemysłowy', 'Wzdłuż rzeki lub linii kolejowej — z niego wychodzi sektor robotniczy'),
                 (266, 131, 260, 290, 'Dzielnica zamożnych', 'Rozwija się w atrakcyjnym kierunku (wzgórza, zieleń)'),
                 (176, 89, 172, 20, 'Dzielnica klasy średniej', 'Między sektorami bogatych i robotniczych'),
                 (160, 195, 150, 268, 'Linia transportowa', 'Sektory rozwijają się klinami wzdłuż arterii'),
                 (200, 155, 210, 268, 'Centrum (CBD)', 'Handel, biura, usługi')],
      opis='Uproszczony model sektorowy H. Hoyta (1939) — rysunek autorski IndexLab.',
      uwaga='W odróżnieniu od modelu koncentrycznego Burgessa dzielnice tworzą kliny wzdłuż dróg, rzek i kolei. Rzeczywiste miasta łączą cechy obu modeli i modelu wielojądrowego.'),
]

# ---------- 3. Gradient adiabatyczny ----------
_a = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_a += '<path class="gt ol" d="M0 300 V270 C80 260 150 200 200 70 C250 200 320 260 400 270 V300 Z"/>'
_a += '<path class="gk ol" d="M95 180 C100 160 130 155 140 165 C155 150 185 160 180 180 Z"/><path class="gk ol" d="M110 150 C120 120 160 110 175 140 C185 140 190 160 175 165 H110 Z"/>'
_a += '<path class="dash" d="M0 180 H400"/><text class="ts" x="300" y="175">poziom kondensacji</text>'
_a += strz(40, 270, 100, 200, 'hot') + strz(140, 150, 185, 85, 'cold')
for y, t in ((268, '20°C'), (185, '10°C'), (85, '4°C')):
    _a += f'<text class="tb" x="8" y="{y}">{t}</text>'
S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Przemiany adiabatyczne — sucha i wilgotna', svg=_a,
      znaczniki=[(70, 235, 120, 250, 'Gradient suchoadiabatyczny', 'Powietrze nienasycone ochładza się o ok. 1°C/100 m'),
                 (140, 180, 230, 205, 'Kondensacja', 'Osiągnięcie punktu rosy — powstaje chmura'),
                 (162, 118, 195, 112, 'Gradient wilgotnoadiabatyczny', 'Ok. 0,6°C/100 m — ciepło kondensacji spowalnia ochładzanie'),
                 (200, 75, 250, 45, 'Szczyt', 'Opady po stronie dowietrznej')],
      opis='Wznoszenie powietrza po stoku: do poziomu kondensacji przemiana sucha, wyżej wilgotna (wartości przybliżone) — rysunek autorski IndexLab.',
      uwaga='Przykład zadania: na 0 m 20°C, kondensacja na 1000 m (10°C), szczyt 2000 m → 10 − 6 = 4°C. Po zawietrznej powietrze opada suchoadiabatycznie i ogrzewa się — fen.'),
]

# ---------- 4. Gleby w przekroju doliny ----------
_g = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_g += '<path class="gs ol" d="M0 80 C60 85 100 120 130 180 H270 C300 120 340 85 400 80 V300 H0 Z"/>'
_g += '<path class="gm ol" d="M0 80 C60 85 100 120 130 180 L135 195 C100 140 60 100 0 98 Z"/>'
_g += '<path class="gp ol" d="M130 180 H270 V200 H130 Z"/>'
_g += '<path class="gw ol" d="M185 180 H215 V192 H185 Z"/>'
_g += '<path class="gc ol" d="M270 180 C300 120 340 85 400 80 V96 C345 100 305 135 268 196 Z"/>'
S['g-gleby'] = [
 dict(typ='rysunek', tytul='Gleby w przekroju doliny rzecznej', svg=_g,
      znaczniki=[(160, 190, 120, 240, 'Mady', 'Na osadach powodziowych w dnie doliny — żyzne, warstwowane'),
                 (200, 186, 240, 150, 'Rzeka', 'Wylewy nanoszą namuły'),
                 (60, 95, 70, 40, 'Gleby brunatne/płowe', 'Na glinach wysoczyzny'),
                 (330, 100, 320, 40, 'Rędziny', 'Na zboczu z wapieniem — płytkie, kamieniste')],
      opis='Uproszczone rozmieszczenie gleb w dolinie (catena) — rysunek autorski IndexLab.',
      uwaga='Mady są żyzne, ale zagrożone powodziami — w dnach dolin częściej łąki i pastwiska niż pola. Typ gleby zależy od skały macierzystej, rzeźby i wody gruntowej.'),
]

# ---------- 5. Chmura burzowa ----------
_c = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_c += '<path class="gl ol" d="M0 270 H400 V300 H0 Z"/>'
_c += '<path class="gn ol" d="M120 200 C110 160 140 140 150 120 C150 80 170 60 180 50 H100 C130 40 290 40 320 50 H220 C240 70 250 100 250 120 C270 140 290 170 280 200 Z"/>'
for x in (150, 170, 190, 210, 230, 250):
    _c += f'<path class="cold" d="M{x} 205 l-6 50"/>'
_c += strz(200, 260, 200, 70, 'hot') + strz(300, 120, 330, 240, 'cold')
_c += '<path class="hot" d="M300 205 L285 235 L298 235 L282 265" style="stroke-width:2"/>'
S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Chmura burzowa Cumulonimbus (przekrój)', svg=_c,
      znaczniki=[(200, 150, 260, 150, 'Prąd wstępujący', 'Silna konwekcja nad nagrzanym podłożem'),
                 (210, 45, 300, 25, 'Kowadło', 'Rozpływ chmury pod tropopauzą (ok. 10–12 km)'),
                 (306, 140, 315, 112, 'Prąd w dół', 'Zimne powietrze z opadem — szkwał'),
                 (200, 230, 120, 250, 'Ulewa, grad', 'Opady nawalne, krótkotrwałe'),
                 (290, 250, 300, 285, 'Wyładowanie', 'Pioruny i grzmoty')],
      opis='Uproszczony przekrój dojrzałej chmury Cb — rysunek autorski IndexLab.',
      uwaga='Burze termiczne powstają latem po południu (maksimum nagrzania), frontalne — przy froncie chłodnym. W strefie równikowej burze konwekcyjne zdarzają się niemal codziennie.'),
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
