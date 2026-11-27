# Schematy geografii — porcja 17 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Wąwóz lessowy ----------
_w = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_w += '<path class="gp ol" d="M0 80 H120 C150 80 160 210 185 225 H215 C240 210 250 80 280 80 H400 V300 H0 Z"/>'   # less
_w += '<path class="gs ol" d="M0 250 H400 V300 H0 Z"/>'                                                         # podłoże
_w += '<path class="gt" d="M0 74 H120 V80 H0 Z M280 74 H400 V80 H280 Z"/>'
for x in (20, 50, 80, 310, 340, 370):
    _w += f'<path class="gf ol" d="M{x} 74 l8 -22 l8 22 Z"/>'
_w += '<path class="gw2 ol" d="M188 225 H212 V231 H188 Z"/>'
_w += strz(130, 40, 175, 140, 'cold') + strz(270, 40, 225, 140, 'cold')
_w += '<text class="ts" x="392" y="292" text-anchor="end">skała podłoża</text>'
S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Wąwóz lessowy (przekrój)', svg=_w,
      znaczniki=[(160, 150, 70, 150, 'Strome ściany', 'Less trzyma pionowe ściany, dopóki jest suchy'),
                 (200, 228, 290, 200, 'Okresowy ciek', 'Woda płynie dnem tylko po ulewach i roztopach'),
                 (150, 85, 60, 120, 'Spływ z pól', 'Woda z pól bez roślin rozcina less'),
                 (60, 160, 40, 230, 'Less', 'Pył eoliczny z plejstocenu — miękki, podatny na erozję'),
                 (100, 70, 200, 35, 'Pole uprawne', 'Orka wzdłuż stoku przyspiesza powstawanie wąwozów')],
      opis='Przekrój przez wąwóz w pokrywie lessowej (np. Wyżyna Lubelska, Kazimierz Dolny) — rysunek autorski IndexLab.',
      uwaga='Wąwozy lessowe powstają szybko (nawet w kilkadziesiąt lat) przez erozję wąwozową. Ochrona: zalesianie zboczy, orka w poprzek stoku, zadarnianie. Wąwozy utrudniają rolnictwo i budowę dróg.'),
]

# ---------- 2. Kras powierzchniowy ----------
_k = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_k += '<path class="gs ol" d="M0 110 H40 L60 140 L80 110 H140 C150 110 150 95 160 70 L175 70 L178 110 H220 V170 H330 V110 H400 V300 H0 Z"/>'
_k += '<path class="gs2" d="M0 160 H400 M0 210 H400 M0 255 H400" style="fill:none;stroke-width:1"/>'
_k += '<path class="gg" d="M222 160 H328 V170 H222 Z"/>'
_k += '<path class="gw" d="M100 230 C150 220 230 235 300 225 L300 240 C230 250 150 238 100 245 Z"/>'
_k += '<path class="gs2 ol" d="M150 210 l4 18 l4 -18 Z M190 210 l4 14 l4 -14 Z"/>'
_k += '<text class="ts" x="8" y="292">wapienie</text>'
S['g-rzezba'].append(
 dict(typ='rysunek', tytul='Kras powierzchniowy i podziemny (przekrój)', svg=_k,
      znaczniki=[(60, 130, 40, 60, 'Lej krasowy', 'Zagłębienie po rozpuszczeniu skały lub zapadnięciu stropu'),
                 (167, 80, 230, 40, 'Ostaniec', 'Odporna skała, która przetrwała rozpuszczanie'),
                 (275, 165, 300, 80, 'Polje', 'Płaska, rozległa kotlina krasowa z glebą na dnie'),
                 (200, 238, 300, 275, 'Rzeka podziemna', 'Woda wsiąka szczelinami i płynie w kanałach'),
                 (154, 220, 70, 210, 'Stalaktyty', 'Nacieki ze stropu jaskini')],
      opis='Formy krasowe w wapieniach — rysunek autorski IndexLab.',
      uwaga='Krasowienie: CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂. Polskie przykłady: Jura Krakowsko-Częstochowska (ostańce, jaskinie), Tatry Zachodnie, Roztocze, Polesie (jeziora krasowe). Na obszarach krasowych jest rzadka sieć rzek.'))

# ---------- 3. Cyklon tropikalny ----------
_c = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_c += '<path class="gw ol" d="M0 250 H400 V300 H0 Z"/>'
for sx in (1, -1):
    for i, h in enumerate((150, 185, 205)):
        x = 200 + sx * (40 + i * 45)
        _c += f'<path class="gk ol" d="M{x - 25} 250 C{x - 30} {250 - h} {x + 30} {250 - h} {x + 25} 250 Z"/>'
_c += '<path class="gn ol" d="M185 250 C185 120 215 120 215 250 Z"/>'
_c += strz(60, 268, 180, 268, 'hot') + strz(340, 268, 220, 268, 'hot')
_c += strz(110, 70, 30, 40, 's') + strz(290, 70, 370, 40, 's')
_c += '<text class="ts" x="8" y="292">ciepły ocean (powyżej 26–27°C)</text>'
S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Cyklon tropikalny w przekroju', svg=_c,
      znaczniki=[(200, 220, 260, 282, 'Oko cyklonu', 'Spokojny środek — osiadanie powietrza, brak chmur'),
                 (225, 160, 120, 125, 'Ściana oka', 'Najsilniejsze wiatry i ulewy'),
                 (120, 268, 120, 230, 'Wilgotne powietrze', 'Wiatry przy oceanie zbiegają się ku środkowi'),
                 (70, 55, 140, 25, 'Odpływ górą', 'Na wysokości powietrze rozpływa się na zewnątrz'),
                 (330, 200, 300, 110, 'Pasma chmur', 'Spiralne pasma Cb z opadami')],
      opis='Przekrój przez huragan/tajfun — rysunek autorski IndexLab.',
      uwaga='Cyklon tropikalny czerpie energię z ciepła kondensacji pary nad oceanem ≥ 26–27°C; nie powstaje na równiku (brak siły Coriolisa). Nad lądem słabnie. Nazwy: huragan (Atlantyk), tajfun (Pacyfik Zach.), cyklon (Ocean Indyjski).'),
]

# ---------- 4. Front zokludowany ----------
_o = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_o += '<path class="cold" d="M0 250 C60 248 120 200 175 150" style="stroke-width:2"/>'
_o += '<path class="hot" d="M175 150 C240 170 320 230 400 248" style="stroke-width:2"/>'
_o += '<path class="gk ol" d="M120 150 C150 70 260 60 300 150 C260 135 170 140 120 150 Z"/>'
_o += '<path class="d" d="M0 250 H400" style="stroke-width:2"/>'
_o += '<text class="tb" x="60" y="275" text-anchor="middle">chłodne</text>'
_o += '<text class="tb" x="200" y="58" text-anchor="middle">ciepłe (wypchnięte w górę)</text>'
_o += '<text class="tb" x="340" y="275" text-anchor="middle">chłodne</text>'
S['g-pogoda'].append(
 dict(typ='rysunek', tytul='Front zokludowany (przekrój)', svg=_o,
      znaczniki=[(175, 150, 280, 30, 'Okluzja', 'Front chłodny dogonił ciepły'),
                 (80, 220, 130, 205, 'Chłodne powietrze z tyłu', 'Napiera i podnosi powietrze ciepłe'),
                 (230, 110, 330, 90, 'Chmury okluzji', 'Mieszanka Ns i Cb — opady ciągłe i przelotne'),
                 (330, 235, 360, 160, 'Chłodne z przodu', 'Powietrze, nad które wcześniej nasuwał się front ciepły')],
      opis='Przekrój przez front zokludowany — rysunek autorski IndexLab.',
      uwaga='Okluzja to końcowy etap rozwoju niżu: ciepły wycinek zostaje oderwany od ziemi. Na mapie synoptycznej oznaczana fioletową linią z trójkątami i półkolami po tej samej stronie.'))

# ---------- 5. Krajobraz polodowcowy z góry ----------
_p = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
_p += '<path class="gi ol" d="M0 0 H400 V40 C300 55 100 55 0 40 Z"/>'                              # lądolód
_p += '<path class="gc ol" d="M0 70 C100 95 300 95 400 70 V90 C300 112 100 112 0 90 Z"/>'          # morena czołowa
_p += '<path class="gp ol" d="M0 110 C100 135 300 135 400 110 V230 H0 Z"/>'                        # sandr
_p += '<path class="gw ol" d="M0 245 C120 262 280 262 400 245 V275 C280 290 120 290 0 275 Z"/>'      # pradolina
_p += '<path class="gw ol" d="M170 40 C165 60 175 80 165 95 L178 95 C188 80 180 60 186 40 Z"/>'    # rynna
_p += '<ellipse class="gw ol" cx="90" cy="60" rx="10" ry="6"/><ellipse class="gw ol" cx="300" cy="58" rx="8" ry="5"/>'
for x in (60, 140, 230, 320):
    _p += strz(x, 135, x - 10, 215, 'cold')
S['g-lodowce'] = [
 dict(typ='rysunek', tytul='Strefy krajobrazu polodowcowego (widok z góry)', svg=_p,
      znaczniki=[(200, 20, 260, 20, 'Lądolód', 'Czoło lądolodu w czasie postoju'),
                 (300, 88, 340, 60, 'Morena czołowa', 'Wał usypany przed czołem lądolodu'),
                 (176, 60, 110, 30, 'Rynna', 'Wyżłobiona przez wody pod lodem — dziś jeziora rynnowe'),
                 (200, 180, 260, 160, 'Sandr', 'Płaska równina piasków i żwirów wód roztopowych'),
                 (200, 265, 250, 230, 'Pradolina', 'Szeroka dolina odprowadzająca wody wzdłuż czoła ku zachodowi'),
                 (90, 60, 60, 110, 'Oczko wytopiskowe', 'Jeziorko po stopieniu bryły martwego lodu')],
      opis='Układ form polodowcowych przed czołem lądolodu (widok z góry, północ u góry) — rysunek autorski IndexLab.',
      uwaga='Kolejność od północy: wysoczyzna morenowa → morena czołowa → sandr → pradolina. W Polsce: Pojezierze Pomorskie, Równina Tucholska (sandr), pradolina Toruńsko-Eberswaldzka.'),
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
