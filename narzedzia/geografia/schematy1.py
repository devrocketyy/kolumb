# Schematy geografii — porcja 1 (rysunki autorskie IndexLab, standard 2.0).
# SVG 400×300; klasy kolorów: gw/gw2 woda, gl/gl2 ląd, gs/gs2 skała, gp piasek, gf/gf2 las, gi lód, gm/gm2 magma,
# gn niebo, gg gleba, gc glina, gt trawa; hot/cold linie, hotf/coldf wypełnienia; ts/tb podpisy; s, s2, f, f2, d, dash, t.
# Znacznik: (x, y elementu, x, y numeru, nazwa, opis).
import math
S = {}


def strzalka(x1, y1, x2, y2, cls='s', g=7):
    """Linia ze strzałką na końcu."""
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.45), y2 - g * math.sin(a - 0.45))
    p2 = (x2 - g * math.cos(a + 0.45), y2 - g * math.sin(a + 0.45))
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{f}" d="M{x2:.1f} {y2:.1f} L{p1[0]:.1f} {p1[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f} Z"/>')


def polnoc(x, y):
    return f'<path class="d" d="M{x} {y - 14} L{x + 6} {y + 4} L{x} {y} L{x - 6} {y + 4} Z"/><text class="tb" x="{x}" y="{y + 18}" text-anchor="middle">N</text>'


# ---------- 1. Poziomice ----------
_poz = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
        '<path class="gp ol" d="M45 230 C35 120 130 38 240 42 C345 48 380 140 365 222 C350 282 110 292 45 230 Z"/>'
        '<path class="gl ol" d="M70 214 C62 128 140 72 232 76 C318 80 342 150 330 205 C316 252 125 262 70 214 Z"/>'
        '<path class="gl2 ol" d="M88 200 C82 140 148 104 222 108 C290 112 305 162 294 194 C282 226 140 236 88 200 Z"/>'
        '<path class="gs ol" d="M106 186 C102 150 155 132 208 136 C252 139 264 168 256 186 C246 206 132 214 106 186 Z"/>'
        '<path class="cold" d="M352 258 Q362 272 372 284 T392 300" style="stroke-width:2.6"/>'
        '<path class="d" d="M176 168 l5 -9 l5 9 Z"/><text class="tb" x="181" y="182" text-anchor="middle">334,5</text>'
        '<text class="ts" x="200" y="281" text-anchor="middle">300</text><text class="ts" x="200" y="251" text-anchor="middle">310</text><text class="ts" x="200" y="228" text-anchor="middle">320</text><text class="ts" x="200" y="209" text-anchor="middle">330</text>'
        '<path class="dash" d="M20 165 H385"/><text class="tb" x="12" y="169">A</text><text class="tb" x="388" y="169">B</text>'
        '<path class="s" d="M20 285 H120 M20 280 V290 M70 282 V288 M120 280 V290"/><text class="ts" x="20" y="277">0</text><text class="ts" x="62" y="277">250</text><text class="ts" x="108" y="277">500 m</text>'
        + polnoc(375, 30))
S['g-poziomice'] = [
 dict(typ='rysunek', tytul='Poziomice: wzgórze i stoki', svg=_poz,
      znaczniki=[(181, 163, 215, 22, 'Szczyt', 'Punkt wysokościowy 334,5 m wewnątrz najwyższej poziomicy'),
                 (78, 195, 90, 25, 'Stok stromy', 'Po stronie zachodniej poziomice leżą gęsto — duży spadek'),
                 (320, 120, 300, 100, 'Stok łagodny', 'Po stronie wschodniej poziomice są rozsunięte'),
                 (366, 276, 345, 240, 'Ciek', 'Spływa od wyższych poziomic ku niższym, prostopadle do nich'),
                 (300, 165, 285, 135, 'Linia profilu A–B', 'Wzdłuż niej wykreśla się przekrój terenu')],
      opis='Wzgórze na mapie poziomicowej, cięcie 10 m, kolory warstw wysokości.',
      uwaga='Gęste poziomice = stromo, rzadkie = łagodnie. Zamknięte poziomice o rosnących wartościach oznaczają wzniesienie, o malejących — zagłębienie.'),
]

# ---------- 2. Profil terenu ----------
_pkt = [(0, 296), (0.15, 303), (0.3, 313), (0.42, 323), (0.55, 331), (0.7, 334.5), (0.85, 332), (1.05, 325), (1.3, 316), (1.6, 305), (1.85, 298), (2, 295)]
_X = lambda km: 60 + 155 * km
_Y = lambda h: 250 - (h - 280) * 3.2
_lin = ' '.join(f'{_X(k):.1f},{_Y(h):.1f}' for k, h in _pkt)
_prof = ('<rect class="gn" x="60" y="20" width="310" height="230"/>'
         + ''.join(f'<path class="dash" d="M60 {_Y(h):.0f} H370"/><text class="ts" x="55" y="{_Y(h) + 3:.0f}" text-anchor="end">{h}</text>' for h in (280, 300, 320, 340))
         + ''.join(f'<path class="s" d="M{_X(k):.0f} 250 V255"/><text class="ts" x="{_X(k):.0f}" y="266" text-anchor="middle">{k}</text>' for k in (0, 0.5, 1, 1.5, 2))
         + f'<polygon class="gl2" points="60,250 {_lin} {_X(2):.1f},250"/>'
         + f'<polygon class="gl" points="60,250 ' + ' '.join(f'{_X(k):.1f},{_Y(h) + 8:.1f}' for k, h in _pkt) + f' {_X(2):.1f},250"/>'
         + f'<polyline class="s" style="stroke-width:2.2" fill="none" points="{_lin}"/>'
         + '<path class="s" d="M60 20 V250 H370"/>'
         + f'<path class="dash" d="M{_X(0.7):.1f} {_Y(334.5):.1f} V250"/>'
         + '<text class="ts" x="8" y="14">m n.p.m.</text><text class="ts" x="370" y="282" text-anchor="end">odległość [km]</text>'
         + '<text class="tb" x="60" y="15" text-anchor="middle">A</text><text class="tb" x="370" y="15" text-anchor="middle">B</text>'
         + '<text class="ts" x="215" y="292" text-anchor="middle">skala pozioma 1:25 000, pionowa 1:2 500 — przewyższenie ×10</text>')
S['g-poziomice'].append(
 dict(typ='rysunek', tytul='Profil terenu z mapy', svg=_prof,
      znaczniki=[(_X(0.7), _Y(334.5), 230, 45, 'Kulminacja', '334,5 m — 0,7 km od punktu A'),
                 (_X(0.35), _Y(317), 120, 120, 'Stok zachodni', 'Stromszy: ok. 38 m na 0,7 km'),
                 (_X(1.4), _Y(312), 300, 120, 'Stok wschodni', 'Łagodniejszy: ok. 40 m na 1,3 km'),
                 (_X(2), _Y(295), 340, 200, 'Punkt B', '295 m n.p.m.')],
      opis='Przekrój wzdłuż linii A–B z mapy poziomicowej (dane autorskie).',
      uwaga='Oś pozioma — odległość według skali mapy, pionowa — wysokość. Przewyższenie = skala pionowa / skala pozioma; bez niego profil byłby niemal płaski.'))

# ---------- 3. Strefy oświetlenia ----------
_cx, _cy, _r = 140, 150, 115
_y = lambda lat: _cy - _r * math.sin(math.radians(lat))
_w = lambda lat: _r * math.cos(math.radians(lat))
_osw = (f'<defs><clipPath id="g1osw"><circle cx="{_cx}" cy="{_cy}" r="{_r}"/></clipPath></defs>'
        f'<g clip-path="url(#g1osw)"><rect class="gi" x="0" y="0" width="400" height="300" style="stroke:none"/>'
        f'<rect class="gt" x="0" y="{_y(66.55):.1f}" width="300" height="{_y(-66.55) - _y(66.55):.1f}"/>'
        f'<rect class="gp" x="0" y="{_y(23.45):.1f}" width="300" height="{_y(-23.45) - _y(23.45):.1f}"/></g>'
        f'<circle class="s" cx="{_cx}" cy="{_cy}" r="{_r}"/>'
        + ''.join(f'<path class="{"s" if lat == 0 else "dash"}" d="M{_cx - _w(lat):.1f} {_y(lat):.1f} H{_cx + _w(lat):.1f}"/>' for lat in (66.55, 23.45, 0, -23.45, -66.55))
        + ''.join(f'<text class="ts" x="{_cx + _w(lat) + 4:.1f}" y="{_y(lat) + 3:.1f}">{t}</text>' for lat, t in ((66.55, "66°33′N"), (23.45, "23°27′N"), (0, "0°"), (-23.45, "23°27′S"), (-66.55, "66°33′S")))
        + ''.join(strzalka(5, y, 18, y, 'hot', 6) for y in (110, 150, 190)))
S['g-obiegowy'] = [
 dict(typ='rysunek', tytul='Strefy oświetlenia Ziemi', svg=_osw,
      znaczniki=[(140, 150, 262, 150, 'Strefa gorąca', 'Między zwrotnikami — Słońce może górować w zenicie'),
                 (140, 75, 262, 80, 'Umiarkowana N', 'Słońce nigdy w zenicie; brak dnia i nocy polarnej'),
                 (140, 45, 262, 22, 'Podbiegunowa N', 'Za kołem podbiegunowym — dzień i noc polarna'),
                 (140, 225, 262, 220, 'Umiarkowana S', 'Między zwrotnikiem Koziorożca a kołem podbiegunowym S'),
                 (140, 262, 262, 280, 'Podbiegunowa S', 'Za kołem podbiegunowym S')],
      opis='Podział Ziemi według warunków oświetlenia (żółty — gorąca, zielony — umiarkowane, błękit — podbiegunowe).',
      uwaga='Granice stref wynikają z nachylenia osi Ziemi: zwrotniki leżą na 23°27′, koła podbiegunowe na 90° − 23°27′ = 66°33′.'),
]

# ---------- 4. Cyrkulacja ----------
_cx, _cy, _r = 150, 150, 118
_cyr = (f'<defs><clipPath id="g1cyr"><circle cx="{_cx}" cy="{_cy}" r="{_r}"/></clipPath></defs>'
        f'<circle class="gw" cx="{_cx}" cy="{_cy}" r="{_r}"/>'
        + ''.join(f'<path class="{"s" if lat == 0 else "dash"}" d="M{_cx - _w(lat):.1f} {_y(lat):.1f} H{_cx + _w(lat):.1f}"/>' for lat in (60, 30, 0, -30, -60))
        + f'<circle class="s" cx="{_cx}" cy="{_cy}" r="{_r}"/>')
_y = lambda lat: _cy - _r * math.sin(math.radians(lat))
_w = lambda lat: _r * math.cos(math.radians(lat))
_cyr = (f'<circle class="gw" cx="{_cx}" cy="{_cy}" r="{_r}"/>'
        + ''.join(f'<path class="{"s" if lat == 0 else "dash"}" d="M{_cx - _w(lat):.1f} {_y(lat):.1f} H{_cx + _w(lat):.1f}"/>' for lat in (60, 30, 0, -30, -60))
        + f'<circle class="s" cx="{_cx}" cy="{_cy}" r="{_r}"/>')
for lat, (dx, dy) in ((15, (-16, 10)), (-15, (-16, -10)), (45, (16, -8)), (-45, (16, 8)), (75, (-12, 6)), (-75, (-12, -6))):
    yy = _y(lat)
    for xx in ((_cx - 45, _cx + 15) if abs(lat) < 70 else (_cx - 10,)):
        _cyr += strzalka(xx - dx / 2, yy - dy / 2, xx + dx / 2, yy + dy / 2, 'cold', 6)
for lat, t in ((90, 'W'), (60, 'N'), (30, 'W'), (0, 'N'), (-30, 'W'), (-60, 'N'), (-90, 'W')):
    _cyr += f'<text class="tb" x="{_cx + _w(lat) + 6:.1f}" y="{_y(lat) + (12 if lat == 90 else -2 if lat == -90 else 4):.1f}">{t}</text>'
_cyr += '<text class="ts" x="8" y="292">W — wyż, N — niż; strzałki — kierunek wiatru przy powierzchni</text>'
S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Cyrkulacja atmosferyczna', svg=_cyr,
      znaczniki=[(135, _y(15), 290, 110, 'Pasaty NE', 'Od wyżów zwrotnikowych ku równikowi; odchylone w prawo'),
                 (135, _y(-15), 290, 205, 'Pasaty SE', 'Na półkuli S odchylone w lewo'),
                 (60, 150, 70, 18, 'Niż równikowy', 'Wznoszenie powietrza, chmury kłębiaste, codzienne opady'),
                 (165, _y(45), 290, 70, 'Wiatry zachodnie', 'Między wyżem zwrotnikowym a niżem subpolarnym'),
                 (140, _y(75), 290, 30, 'Wschodnie polarne', 'Od wyżu polarnego')],
      opis='Układ stref ciśnienia i stałych wiatrów na Ziemi.',
      uwaga='Na półkuli N wiatry odchylają się w prawo, na S w lewo (siła Coriolisa). W wyżu zwrotnikowym opadające suche powietrze tworzy pustynie.'),
]

# ---------- 5. Fronty ----------
_fr = ('<rect class="gn" x="0" y="0" width="400" height="260"/>'
       '<path class="gi" style="stroke:none" d="M0 260 L0 40 C40 80 75 170 95 260 Z"/>'
       '<path class="gp" style="stroke:none" opacity="0.55" d="M95 260 C75 170 40 80 0 40 L0 0 L400 0 L400 60 C330 90 260 160 220 260 Z"/>'
       '<path class="gi" style="stroke:none" d="M220 260 C260 160 330 90 400 60 L400 260 Z"/>'
       '<path class="cold" d="M0 40 C40 80 75 170 95 260"/><path class="hot" d="M220 260 C260 160 330 90 400 60"/>'
       # cumulonimbus z kowadłem nad frontem chłodnym
       '<path class="gk" d="M70 205 C55 205 50 185 65 178 C60 150 85 140 98 150 C100 120 120 70 125 50 C110 44 85 46 70 40 L175 40 C160 46 140 46 135 52 C140 90 150 130 150 160 C170 160 172 185 158 195 C158 210 140 210 130 205 Z"/>'
       # nimbostratus i cirrus wzdłuż frontu ciepłego
       '<path class="gk" d="M215 205 C205 190 225 178 245 180 C250 160 285 150 305 160 C320 140 360 135 380 150 C395 150 400 165 400 175 L400 200 C370 205 300 210 215 205 Z"/>'
       '<path class="s2" d="M320 70 q15 -8 30 0 M340 52 q15 -8 30 0 M300 92 q14 -8 28 0"/>'
       + ''.join(f'<path class="cold" style="stroke-width:1.3" d="M{x} 210 l-5 14"/>' for x in (95, 107, 119, 131, 143))
       + ''.join(f'<path class="cold" style="stroke-width:1.1" d="M{x} 208 l-3 10"/>' for x in range(230, 400, 12))
       + '<rect class="gl" x="0" y="260" width="400" height="40"/><path class="s" d="M0 260 H400"/>'
       + ''.join(f'<path class="coldf" d="M{x} 260 l7 -10 l7 10 Z"/>' for x in (60, 76))
       + ''.join(f'<path class="hotf" d="M{x} 260 a7 7 0 0 1 14 0 Z"/>' for x in (205, 221))
       + strzalka(20, 280, 70, 280, 's', 7) + strzalka(180, 280, 230, 280, 's', 7)
       + '<text class="ts" x="75" y="284">ruch frontów</text>'
       + '<text class="tb" x="18" y="150">chłodne</text><text class="tb" x="330" y="240">chłodne</text>')
S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Front ciepły i front chłodny', svg=_fr,
      znaczniki=[(34, 88, 50, 20, 'Front chłodny', 'Chłodne powietrze wciska się klinem pod ciepłe i gwałtownie je wypiera ku górze'),
                 (120, 110, 175, 70, 'Cumulonimbus', 'Chmura burzowa z kowadłem — krótkie ulewy, burze, porywy wiatru'),
                 (348, 90, 330, 138, 'Front ciepły', 'Ciepłe powietrze łagodnie wślizguje się po klinie chłodnego'),
                 (300, 190, 270, 235, 'Nimbostratus', 'Długotrwałe opady ciągłe na szerokim pasie przed frontem'),
                 (335, 62, 300, 30, 'Cirrus', 'Pierzaste chmury wysokie — zwiastun frontu ciepłego'),
                 (190, 125, 205, 100, 'Wycinek ciepły', 'Ciepła masa powietrza między frontami niżu')],
      opis='Przekrój przez niż z frontem chłodnym (po lewej) i ciepłym (po prawej); oba przesuwają się na wschód.',
      uwaga='Front ciepły: najpierw chmury piętra wysokiego, potem długie opady, po przejściu ocieplenie. Front chłodny: gwałtowne ulewy i burze, po przejściu ochłodzenie i poprawa widzialności.'),
]

# ---------- 6. Stratowulkan ----------
_st = ('<defs><clipPath id="g1st"><path d="M15 250 L125 72 L165 72 L275 250 Z"/></clipPath></defs>'
       '<rect class="gn" x="0" y="0" width="400" height="250"/>'
       '<g clip-path="url(#g1st)">'
       + ''.join(f'<path class="{"gs" if i % 2 else "gm2"}" style="stroke:none" d="M0 {250 - i * 18} Q145 {170 - i * 18} 290 {250 - i * 18} V{268 - i * 18} Q145 {188 - i * 18} 0 {268 - i * 18} Z"/>' for i in range(12))
       + '</g><path class="s" d="M15 250 L125 72 L165 72 L275 250"/>'
       '<rect class="gs2" x="0" y="250" width="400" height="50"/>'
       '<ellipse class="gm" cx="145" cy="282" rx="75" ry="15"/>'
       '<path class="gm" d="M139 270 L141 74 L149 74 L151 270 Z"/>'
       '<path class="gm" d="M146 160 L189 114 L194 119 L150 168 Z"/>'
       '<path class="gs2 ol" d="M182 124 L192 106 L202 124 Z"/><path class="gm" d="M189 108 L192 104 L195 108 Z"/>'
       '<path class="gm" d="M126 74 L84 140 L91 142 L131 77 Z"/>'
       '<g transform="translate(-55 0)"><path class="gk" d="M175 70 C150 70 140 52 158 44 C150 22 180 10 196 22 C205 2 240 6 240 26 C262 20 275 42 258 54 C270 70 245 78 230 70 Z" opacity="0.95"/></g>'
       + ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="2"/>' for x, y in ((95, 90), (205, 85), (85, 60), (215, 64), (115, 48)))
       + '<text class="ts" x="8" y="296">skorupa ziemska</text>')
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Przekrój stratowulkanu', svg=_st,
      znaczniki=[(150, 35, 285, 22, 'Chmura erupcyjna', 'Gazy, popiół i bomby wulkaniczne'),
                 (145, 74, 285, 55, 'Krater', 'Otwór na szczycie stożka'),
                 (192, 110, 285, 88, 'Stożek boczny', 'Pasożytniczy — erupcja z komina bocznego'),
                 (100, 118, 285, 121, 'Potok lawy', 'Lepka lawa andezytowa spływa na krótkim odcinku'),
                 (230, 205, 285, 154, 'Lawa i popiół', 'Warstwy na przemian — stąd nazwa wulkanu warstwowego'),
                 (145, 215, 285, 200, 'Komin główny', 'Droga magmy na powierzchnię'),
                 (190, 282, 285, 268, 'Komora magmowa', 'Zbiornik magmy w skorupie pod wulkanem')],
      opis='Budowa wulkanu warstwowego (stratowulkanu).',
      uwaga='Stratowulkany powstają głównie w strefach subdukcji: lawa jest lepka, a erupcje wybuchowe (np. Etna, Fudżi, Wezuwiusz).'),
]

# ---------- 7. Gleba bielicowa ----------
_gl = ('<rect class="gn" x="0" y="0" width="400" height="40"/>'
       + ''.join(f'<path class="gf2" d="M{x} 40 l-12 0 l12 -26 l12 26 Z"/><path class="gf2" d="M{x} 30 l-9 0 l9 -20 l9 20 Z"/>' for x in (90, 135, 180))
       + '<rect class="gg" x="70" y="40" width="130" height="16"/>'
       + ''.join(f'<path class="s2" d="M{x} {y} l6 -2"/>' for x, y in ((78, 46), (100, 50), (122, 45), (144, 52), (166, 47), (188, 51)))
       + '<rect class="gs2" x="70" y="56" width="130" height="22"/>'
       + '<rect class="f" style="stroke:none" x="70" y="78" width="130" height="52"/>'
       + '<path class="gm2" d="M70 130 H200 V185 Q172 178 135 186 T70 182 Z"/>'
       + '<path class="gc" d="M70 182 Q103 190 135 186 T200 185 V210 H70 Z" opacity="0.7"/>'
       + '<rect class="gp" x="70" y="210" width="130" height="80"/>'
       + ''.join(f'<circle class="d" cx="{75 + (i * 37) % 120}" cy="{216 + (i * 23) % 70}" r="1.3"/>' for i in range(34))
       + '<rect class="s" x="70" y="40" width="130" height="250"/>'
       + '<path class="s" d="M45 40 V290"/>'
       + ''.join(f'<path class="s" d="M41 {40 + d * 2.083:.0f} H45"/><text class="ts" x="38" y="{43 + d * 2.083:.0f}" text-anchor="end">{d}</text>' for d in (0, 20, 40, 60, 80, 100, 120))
       + '<text class="ts" x="5" y="12">głębokość [cm]</text>')
S['g-gleby'] = [
 dict(typ='rysunek', tytul='Profil gleby bielicowej', svg=_gl,
      znaczniki=[(135, 48, 225, 50, 'O — ściółka', 'Igły i szczątki roślin, kwaśna próchnica'),
                 (135, 67, 225, 75, 'A — próchniczny', 'Cienki, ciemnoszary'),
                 (135, 104, 225, 104, 'E — wymywania', 'Jasnoszary, „popielaty” — wymyte związki żelaza i glinu'),
                 (135, 158, 225, 158, 'B — wmywania', 'Rdzawobrunatny — nagromadzone związki żelaza i glinu'),
                 (135, 196, 225, 196, 'BC — przejściowy', 'Stopniowe przejście w skałę macierzystą'),
                 (135, 250, 225, 250, 'C — skała macierzysta', 'Piaski polodowcowe'),
                 (180, 25, 225, 20, 'Bór sosnowy', 'Roślinność iglasta dostarcza kwaśnej ściółki')],
      opis='Profil gleby bielicowej pod lasem iglastym (głębokości przybliżone).',
      uwaga='Bielicowanie: kwaśne związki z rozkładu ściółki wymywają żelazo i glin z poziomu E do poziomu B. Gleba jest kwaśna i mało żyzna — w rolnictwie wymaga wapnowania.'),
]

# ---------- 8. Pasy rzeźby Polski — przekrój N–S ----------
_pts = [(0, 0), (8, 5), (14, 2), (22, 60), (30, 140), (36, 95), (42, 170), (50, 120), (58, 150), (66, 110), (74, 130), (84, 120), (92, 160), (100, 140), (110, 180),
        (118, 240), (126, 300), (134, 260), (142, 330), (150, 280), (158, 230), (166, 200), (174, 210), (182, 190), (188, 260), (196, 420), (204, 520), (212, 700), (220, 900),
        (226, 1300), (232, 1600), (236, 2499), (240, 1500), (244, 900)]
_px = lambda d: 30 + d * 1.45
_py = lambda h: 245 - h * 0.075
_pl = ' '.join(f'{_px(d):.1f},{_py(h):.1f}' for d, h in _pts)
_pas = ('<rect class="gn" x="0" y="0" width="400" height="245"/>'
        '<rect class="gw" x="0" y="230" width="34" height="15"/>'
        f'<polygon class="gl" points="30,245 {_pl} {_px(244):.1f},245"/>'
        f'<polyline class="s" fill="none" points="{_pl}"/>'
        + ''.join(f'<ellipse class="gw" cx="{_px(d):.1f}" cy="{_py(h) + 2:.1f}" rx="4" ry="1.6"/>' for d, h in ((36, 95), (50, 120), (66, 110)))
        + '<rect class="gs2" x="0" y="245" width="400" height="20"/>'
        + ''.join(f'<path class="dash" d="M{_px(d):.1f} 30 V245"/>' for d in (14, 92, 116, 182, 192))
        + ''.join(f'<text class="ts" x="{x}" y="282" text-anchor="middle">{t}</text>' for x, t in ((40, 'pobrzeża'), (105, 'pojezierza'), (180, 'niziny'), (247, 'wyżyny'), (300, 'kotliny'), (350, 'góry')))
        + '<text class="ts" x="5" y="296">N — Bałtyk</text><text class="ts" x="395" y="296" text-anchor="end">S — Tatry</text>'
        )
S['g-pl-geologia'] = [
 dict(typ='rysunek', tytul='Pasy rzeźby Polski', svg=_pas,
      znaczniki=[(_px(8), _py(5), 55, 40, 'Pobrzeża', 'Niskie wybrzeże: mierzeje, wydmy, jeziora przybrzeżne, klify'),
                 (_px(50), _py(120), 112, 70, 'Pojezierza', 'Młodoglacjalne: moreny, rynny z jeziorami, sandry'),
                 (_px(100), _py(140), 185, 100, 'Niziny', 'Staroglacjalne, zrównane, z pradolinami'),
                 (_px(142), _py(330), 245, 130, 'Wyżyny', 'Starsze skały, less, formy krasowe'),
                 (_px(182), _py(190), 300, 110, 'Kotliny', 'Kotliny podkarpackie — zapadliska u podnóża Karpat'),
                 (_px(236), _py(2499), 300, 30, 'Karpaty', 'Góry młode (orogeneza alpejska); Tatry z Rysami 2499 m')],
      opis='Uproszczony przekrój północ–południe przez Polskę (wysokości przewyższone).',
      uwaga='Układ pasowy wynika z budowy geologicznej i zasięgu zlodowaceń: najświeższa rzeźba polodowcowa jest na północy, najstarsza i najwyższa — na południu.'),
]

S['g-demografia'] = [
 dict(typ='proces', tytul='Przejście demograficzne', opis='Model zmian urodzeń i zgonów w miarę rozwoju społeczno-gospodarczego.',
      kroki=[('Faza I — przedtransformacyjna', 'Wysokie urodzenia i wysokie zgony; przyrost bliski zera.'),
             ('Faza II — spadek zgonów', 'Poprawa wyżywienia i medycyny; urodzenia wysokie — eksplozja demograficzna.'),
             ('Faza III — spadek urodzeń', 'Urbanizacja, edukacja kobiet, planowanie rodziny; przyrost maleje.'),
             ('Faza IV — posttransformacyjna', 'Niskie urodzenia i niskie zgony; przyrost bliski zera.'),
             ('Faza V (wg części autorów)', 'Urodzenia poniżej zgonów — ubytek naturalny i starzenie się (np. Polska, Japonia).')],
      uwaga='Kraje Afryki Subsaharyjskiej są w fazie II–III, Europa w fazie IV–V.'),
]

S['g-oceany'] = [
 dict(typ='proces', tytul='Obieg wody w przyrodzie', opis='Krążenie wody między oceanem, atmosferą i lądem.',
      kroki=[('Parowanie', 'Głównie z oceanów, napędzane energią Słońca.'),
             ('Transport pary wodnej', 'Wiatry przenoszą parę nad lądy.'),
             ('Kondensacja', 'Ochładzające się powietrze tworzy chmury.'),
             ('Opady', 'Deszcz i śnieg nad oceanami i lądami.'),
             ('Spływ powierzchniowy i podziemny', 'Rzekami i wodami podziemnymi woda wraca do oceanu.'),
             ('Ewapotranspiracja', 'Parowanie z gleby i roślin na lądzie zamyka mały obieg.')],
      uwaga='Duży obieg obejmuje ocean i ląd, mały — tylko ocean lub tylko ląd.'),
]
