# Schematy geografii — porcja 30 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Układy przestrzenne miast ----------
_u = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_u += '<rect class="gt ol" x="15" y="50" width="170" height="200"/><rect class="gt ol" x="215" y="50" width="170" height="200"/>'
for i in range(1, 6):
    _u += f'<path class="s" d="M{15 + i * 28.3:.1f} 50 V250 M15 {50 + i * 33.3:.1f} H185" style="stroke-width:3"/>'
for a in range(0, 360, 45):
    _u += f'<path class="s" d="M300 150 L{300 + 82 * math.cos(math.radians(a)):.1f} {150 + 95 * math.sin(math.radians(a)):.1f}" style="stroke-width:3"/>'
for r in (30, 60):
    _u += f'<circle class="s" cx="300" cy="150" r="{r}" style="fill:none;stroke-width:3"/>'
_u += '<circle class="hotf ol" cx="300" cy="150" r="10"/>'
_u += '<text class="tb" x="100" y="275" text-anchor="middle">szachownicowy</text><text class="tb" x="300" y="275" text-anchor="middle">promienisto-koncentryczny</text>'
S['g-urbanizacja'] = [
 dict(typ='rysunek', tytul='Układy przestrzenne miast: szachownicowy i promienisto-koncentryczny', svg=_u,
      znaczniki=[(71, 83, 90, 14, 'Regularne kwartały', 'Ulice przecinają się pod kątem prostym (Manhattan, Barcelona — Eixample)'),
                 (300, 150, 230, 30, 'Centrum', 'Z niego wychodzą ulice promieniste'),
                 (360, 150, 330, 30, 'Obwodnica', 'Ulice koncentryczne łączą promienie (Moskwa, Paryż)')],
      opis='Dwa modelowe układy sieci ulic — rysunek autorski IndexLab.',
      uwaga='Układ szachownicowy ułatwia orientację i parcelację (miasta lokacyjne, kolonialne, amerykańskie). Promienisty sprzyja dojazdom do centrum, ale je zatłacza. Miasta polskie łączą średniowieczne centrum z późniejszymi obwodnicami.'),
]

# ---------- 2. Upwelling ----------
_p = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_p += '<path class="gw ol" d="M0 100 H300 V300 H0 Z"/>'
_p += '<path class="coldf" d="M180 100 H300 V200 C260 190 220 150 180 100 Z" style="opacity:.7"/>'
_p += '<path class="gl ol" d="M300 100 L300 80 H400 V300 H300 L280 280 C260 260 290 200 300 100 Z"/>'
_p += strz(380, 70, 320, 70, 's') + strz(250, 110, 120, 110, 's')
_p += strz(200, 260, 260, 200, 'cold') + strz(265, 190, 270, 125, 'cold')
_p += '<text class="ts" x="310" y="95">pustynia Atakama</text>'
S['g-oceany'] = [
 dict(typ='rysunek', tytul='Upwelling u wybrzeży Peru (przekrój)', svg=_p,
      znaczniki=[(350, 70, 340, 18, 'Wiatr od lądu', 'Pasat odpycha wody powierzchniowe od brzegu'),
                 (185, 110, 160, 50, 'Odpływ wód powierzchniowych', 'Ciepła woda przemieszcza się w głąb oceanu'),
                 (230, 230, 150, 270, 'Wypływ zimnych wód', 'Z głębin, bogatych w składniki pokarmowe'),
                 (240, 150, 120, 180, 'Bogate łowiska', 'Plankton → ławice sardeli')],
      opis='Uproszczony przekrój przez strefę upwellingu przy zachodnim wybrzeżu Ameryki Pd. — rysunek autorski IndexLab.',
      uwaga='Zimne wody ochładzają powietrze nad wybrzeżem — brak konwekcji i opadów, stąd pustynia Atakama. Podczas El Niño upwelling słabnie, a połowy gwałtownie spadają.'),
]

# ---------- 3. Zarastanie jeziora ----------
_z = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_z += '<path class="gs ol" d="M0 100 H40 C110 120 140 250 200 250 C260 250 290 120 360 105 L400 100 V300 H0 Z"/>'
_z += '<path class="gw ol" d="M40 105 C110 120 140 250 200 250 C260 250 290 120 360 105 Z"/>'
_z += '<path class="gm ol" d="M80 130 C125 175 150 250 200 250 C250 250 275 175 320 130 C290 195 250 228 200 230 C150 228 110 195 80 130 Z"/>'
for x in (48, 60, 72, 84):
    _z += f'<rect class="gl ol" x="{x}" y="70" width="5" height="45"/>'
_z += '<path class="gl ol" d="M290 140 C300 125 330 110 360 105 C330 120 310 135 300 150 Z"/>'
S['g-pl-wody'] = [
 dict(typ='rysunek', tytul='Zarastanie i zanikanie jeziora', svg=_z,
      znaczniki=[(66, 85, 60, 40, 'Szuwar (trzcina)', 'Rośliny wkraczają od brzegu'),
                 (200, 240, 250, 280, 'Osady denne (gytia)', 'Szczątki organizmów spłycają misę'),
                 (325, 120, 340, 60, 'Pło torfowe', 'Pływający kożuch roślin narastający ku środkowi'),
                 (200, 170, 230, 150, 'Toń wodna', 'Zmniejsza się — jezioro staje się płytsze')],
      opis='Etapy zanikania jeziora: spłycanie osadami i zarastanie od brzegów — rysunek autorski IndexLab.',
      uwaga='Jezioro → staw → bagno → torfowisko → łąka. Proces przyspiesza eutrofizacja (nawozy). Polskie jeziora tracą powierzchnię — dodatkowo przez susze i obniżanie wód gruntowych.'),
]

# ---------- 4. Stożek napływowy ----------
_s = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
_s += '<path class="gs ol" d="M0 0 H400 V90 L250 100 L200 120 L150 100 L0 90 Z"/>'
_s += '<path class="gc ol" d="M185 118 C120 180 80 250 70 300 H330 C320 250 280 180 215 118 Z"/>'
_s += '<path class="cold" d="M200 0 C195 40 205 80 200 120" style="stroke-width:3"/>'
for dx in (-90, -40, 10, 60, 100):
    _s += f'<path class="cold" d="M200 120 C{200 + dx * 0.3:.0f} 180 {200 + dx * 0.7:.0f} 240 {200 + dx:.0f} 300" style="stroke-width:1.5"/>'
S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Stożek napływowy u wylotu doliny górskiej (widok z góry)', svg=_s,
      znaczniki=[(200, 60, 230, 40, 'Dolina górska', 'Rzeka o dużym spadku niesie dużo materiału'),
                 (200, 122, 250, 130, 'Wylot doliny', 'Spadek maleje — rzeka traci energię'),
                 (130, 250, 125, 215, 'Stożek napływowy', 'Wachlarz żwirów i piasków, grubszy materiał bliżej wylotu'),
                 (260, 260, 255, 285, 'Rozgałęzione koryta', 'Rzeka błądzi po własnych osadach')],
      opis='Stożek napływowy na przedpolu gór — rysunek autorski IndexLab.',
      uwaga='Stożki napływowe są typowe dla przedgórzy (Podhale, przedpole Alp, oazy na pustyniach). To forma akumulacji rzecznej — podobnie powstaje delta, ale w zbiorniku wodnym.'),
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
