# Schematy geografii — porcja 10 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- przejście demograficzne (wykres) ----------
_X = lambda f: 50 + f * 66
_Y = lambda w: 250 - w * 4.4
_ur = [(0, 40), (1, 40), (1.6, 39), (2, 36), (2.6, 26), (3, 18), (3.5, 14), (4, 12), (4.6, 9), (5, 8)]
_zg = [(0, 38), (0.6, 37), (1, 34), (1.6, 22), (2, 16), (2.6, 12), (3, 11), (4, 10.5), (4.6, 11.5), (5, 12)]
_pd = (''.join(f'<path class="dash" d="M50 {_Y(w):.0f} H380"/><text class="ts" x="44" y="{_Y(w) + 3:.0f}" text-anchor="end">{w}</text>' for w in (0, 10, 20, 30, 40))
       + ''.join(f'<path class="s2" d="M{_X(f):.0f} 30 V250"/>' for f in (1, 2, 3, 4))
       + ''.join(f'<text class="tb" x="{_X(f + 0.5):.0f}" y="268" text-anchor="middle">{r}</text>' for f, r in ((0, 'I'), (1, 'II'), (2, 'III'), (3, 'IV'), (4, 'V')))
       + '<polygon class="gp" opacity="0.7" points="' + ' '.join(f'{_X(f):.1f},{_Y(w):.1f}' for f, w in _ur) + ' ' + ' '.join(f'{_X(f):.1f},{_Y(w):.1f}' for f, w in reversed(_zg)) + '"/>'
       + '<polyline class="hot" fill="none" points="' + ' '.join(f'{_X(f):.1f},{_Y(w):.1f}' for f, w in _ur) + '"/>'
       + '<polyline class="cold" fill="none" points="' + ' '.join(f'{_X(f):.1f},{_Y(w):.1f}' for f, w in _zg) + '"/>'
       + '<path class="s" d="M50 30 V250 H380"/>'
       + '<text class="ts" x="8" y="22">‰</text><text class="ts" x="215" y="288" text-anchor="middle">fazy przejścia demograficznego</text>'
       + '<rect class="hotf" x="280" y="34" width="14" height="3"/><text class="ts" x="298" y="38">urodzenia</text>'
       + '<rect class="coldf" x="280" y="46" width="14" height="3"/><text class="ts" x="298" y="50">zgony</text>')
S['g-demografia'] = [
 dict(typ='rysunek', tytul='Przejście demograficzne — wykres', svg=_pd,
      znaczniki=[(_X(0.5), _Y(39), 90, 80, 'Faza I', 'Wysokie urodzenia i zgony — przyrost bliski zera'),
                 (_X(1.8), _Y(28), 160, 60, 'Eksplozja', 'Faza II: zgony gwałtownie spadają, urodzenia wysokie'),
                 (_X(2.6), _Y(26), 245, 100, 'Faza III', 'Spadek urodzeń — przyrost maleje'),
                 (_X(3.5), _Y(12), 270, 170, 'Faza IV', 'Niskie urodzenia i zgony'),
                 (_X(4.8), _Y(10), 345, 200, 'Faza V', 'Ubytek naturalny — zgony powyżej urodzeń')],
      opis='Zmiany współczynników urodzeń i zgonów w kolejnych fazach (wartości umowne); pole między krzywymi — przyrost naturalny.',
      uwaga='Przykłady: faza II–III — Niger, Nigeria; faza III — Indie; faza IV — USA, Francja; faza V — Polska, Japonia, Włochy.'),
]

# ---------- inwersja i smog ----------
_iv = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gs2" d="M0 120 L60 90 L110 160 L290 160 L340 80 L400 110 V300 H0 Z"/>'
       '<path class="gc" d="M110 160 L290 160 L290 200 L110 200 Z" opacity="0.0"/>'
       '<rect class="gs" x="0" y="160" width="400" height="140" opacity="0.5"/>'
       '<path class="gs2" d="M60 125 Q200 120 340 118" style="fill:none;stroke:var(--text-2);stroke-dasharray:6 4"/>'
       '<rect class="gk" x="110" y="128" width="180" height="32" style="opacity:.55;stroke:none"/>'
       + ''.join(f'<rect class="d" x="{x}" y="{160 - h}" width="10" height="{h}"/>' for x, h in ((130, 18), (145, 26), (175, 14), (220, 22), (250, 16), (270, 12)))
       + ''.join(f'<path class="s2" d="M{x + 5} {150 - h} q6 -8 0 -16 q-6 -8 0 -14" style="fill:none"/>' for x, h in ((145, 26), (220, 22)))
       + strz(380, 60, 380, 40, 'hot', 6)
       + '<path class="s" d="M360 160 V30"/>' + ''.join(f'<text class="ts" x="356" y="{y + 3}" text-anchor="end">{t}</text><path class="s" d="M356 {y} H360"/>' for y, t in ((158, '−8°C'), (124, '−2°C'), (60, '−5°C')))
       + '<polyline class="hot" fill="none" points="335,158 350,124 340,60"/>'
       + '<text class="ts" x="200" y="290" text-anchor="middle">dolina w czasie wyżu zimą — brak wiatru, bezchmurna noc</text>')
S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Inwersja temperatury i smog w dolinie', svg=_iv,
      znaczniki=[(200, 145, 160, 210, 'Smog', 'Pyły i gazy zalegają przy ziemi'),
                 (200, 122, 200, 50, 'Warstwa inwersyjna', 'Cieplejsze powietrze nad zimnym — „pokrywka”'),
                 (150, 140, 60, 240, 'Kominy', 'Niska emisja z ogrzewania domów'),
                 (345, 140, 300, 230, 'Profil temperatury', 'Przy ziemi zimniej niż wyżej — odwrotnie niż zwykle')],
      opis='Przekrój przez dolinę z miastem w czasie inwersji temperatury (wartości przybliżone).',
      uwaga='Inwersja tworzy się przy pogodzie wyżowej: bezchmurne noce wychładzają grunt, zimne powietrze spływa do dolin. Blokuje mieszanie pionowe — stąd smog w Krakowie, Nowym Targu, Zakopanem.'),
]

# ---------- użytkowanie ziemi w Polsce (wykres kołowy) ----------
_ul = [('Użytki rolne', 60, 'gt'), ('Lasy', 31, 'gf2'), ('Zabudowa', 5, 'gs'), ('Wody', 2, 'gw2'), ('Inne', 2, 'gp')]
_pc = ''
_a0 = -90
for n, p, c in _ul:
    a1 = _a0 + p * 3.6
    x0, y0 = 140 + 110 * math.cos(math.radians(_a0)), 150 + 110 * math.sin(math.radians(_a0))
    x1, y1 = 140 + 110 * math.cos(math.radians(a1)), 150 + 110 * math.sin(math.radians(a1))
    _pc += f'<path class="{c} ol" d="M140 150 L{x0:.1f} {y0:.1f} A110 110 0 {1 if p > 50 else 0} 1 {x1:.1f} {y1:.1f} Z"/>'
    am = math.radians((_a0 + a1) / 2)
    if p >= 5:
        _pc += f'<text class="tb" x="{140 + 70 * math.cos(am):.0f}" y="{154 + 70 * math.sin(am):.0f}" text-anchor="middle">{p}%</text>'
    _a0 = a1
_pc += ''.join(f'<rect class="{c} ol" x="275" y="{60 + i * 24}" width="14" height="14"/><text class="ts" x="295" y="{71 + i * 24}">{n} — {p}%</text>' for i, (n, p, c) in enumerate(_ul))
S['g-pl-gospodarka'] = [
 dict(typ='rysunek', tytul='Użytkowanie ziemi w Polsce', svg=_pc,
      znaczniki=[(120, 210, 150, 285, 'Użytki rolne', 'Grunty orne, łąki, pastwiska, sady — ok. 60%'),
                 (70, 110, 90, 22, 'Lasy', 'Ok. 31% — lesistość rośnie dzięki zalesieniom'),
                 (150, 45, 200, 22, 'Zabudowa', 'Tereny osiedlowe i komunikacyjne — szybko rosną')],
      opis='Struktura użytkowania ziemi w Polsce (wartości zaokrąglone).',
      uwaga='Najwyższą lesistość mają województwa lubuskie i podkarpackie (ok. 50% i 40%), najniższą — łódzkie i mazowieckie (ok. 20–23%).'),
]

# ---------- opady na przekroju Polski ----------
_st = [('Gdańsk', 600, 20), ('Kartuzy', 700, 220), ('Toruń', 520, 60), ('Kujawy', 480, 90), ('Warszawa', 550, 100), ('Kraków', 700, 220), ('Zakopane', 1100, 850), ('Kasprowy', 1700, 1990)]
_op = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
for i, (n, p, h) in enumerate(_st):
    x = 30 + i * 46
    _op += f'<rect class="gw2" x="{x - 12}" y="{170 - p * 0.08:.0f}" width="24" height="{p * 0.08:.0f}"/><text class="tb" x="{x}" y="{164 - p * 0.08:.0f}" text-anchor="middle">{p}</text>'
    _op += f'<text class="ts" x="{x}" y="292" text-anchor="middle">{n}</text>'
_prof = ' '.join(f'{30 + i * 46},{278 - h * 0.045:.0f}' for i, (n, p, h) in enumerate(_st))
_op += f'<polygon class="gl" points="10,280 {_prof} 390,280"/><polyline class="s" fill="none" points="{_prof}"/>'
_op += '<path class="s" d="M10 170 H390"/><text class="ts" x="8" y="14">opady roczne [mm]</text><text class="ts" x="8" y="200">wysokość (przewyższona)</text>'
S['g-pl-klimat'] = [
 dict(typ='rysunek', tytul='Opady roczne na przekroju Polski N–S', svg=_op,
      znaczniki=[(76, 114, 95, 40, 'Pojezierze', 'Wyżej położone — opady orograficzne ok. 700 mm'),
                 (168, 132, 175, 70, 'Kujawy', 'Najsuchszy region — cień opadowy pojezierzy'),
                 (352, 34, 320, 30, 'Tatry', 'Najwyższe opady — ponad 1700 mm')],
      opis='Średnie roczne sumy opadów wybranych stacji na linii północ–południe (wartości przybliżone).',
      uwaga='Opady w Polsce rosną z wysokością (opady orograficzne). Średnio w Polsce spada ok. 600 mm rocznie, najmniej na Kujawach i w Wielkopolsce.'),
]

# ---------- wietrzenie mrozowe ----------
def _skala(x0, krok):
    o = f'<rect class="gs" x="{x0}" y="60" width="110" height="160"/>'
    o += f'<path class="d" d="M{x0 + 55} 60 L{x0 + 50} {100 + krok * 20} L{x0 + 58} {130 + krok * 25}" style="fill:none;stroke:var(--text);stroke-width:{2 + krok}"/>'
    if krok == 1:
        o += f'<path class="gw" d="M{x0 + 50} 62 L{x0 + 56} 62 L{x0 + 55} 120 Z"/>'
    if krok == 2:
        o += f'<path class="gi" d="M{x0 + 48} 62 L{x0 + 60} 62 L{x0 + 57} 140 Z"/>' + strz(x0 + 42, 90, x0 + 28, 90, 's', 6) + strz(x0 + 66, 90, x0 + 80, 90, 's', 6)
    return o


_wm = (_skala(15, 0) + _skala(145, 1) + _skala(275, 2)
       + ''.join(f'<path class="gs2 ol" d="M{x} 270 l8 -12 l10 4 l4 10 Z"/>' for x in (290, 310, 335, 355))
       + '<rect class="gt" x="0" y="280" width="400" height="20"/>'
       + ''.join(f'<text class="tb" x="{x}" y="245" text-anchor="middle">{t}</text>' for x, t in ((70, '1. szczelina'), (200, '2. woda (dzień)'), (330, '3. lód (noc)')))
       + '<text class="ts" x="200" y="30" text-anchor="middle">lód zajmuje o ok. 9% większą objętość niż woda</text>')
S['g-skaly'] = [
 dict(typ='rysunek', tytul='Wietrzenie mrozowe skały', svg=_wm,
      znaczniki=[(70, 100, 100, 50, 'Szczelina', 'Spękanie w skale'),
                 (200, 90, 230, 50, 'Woda', 'Wnika w szczelinę w ciągu dnia'),
                 (330, 90, 360, 50, 'Lód', 'Zamarza nocą i rozsadza skałę'),
                 (320, 266, 260, 270, 'Gruz skalny', 'Ostrokrawędzisty rumosz — piargi, gołoborza')],
      opis='Etapy wietrzenia mrozowego (zamróz) przy wielokrotnym przechodzeniu temperatury przez 0°C.',
      uwaga='Wietrzenie mrozowe jest najsilniejsze w klimatach, w których temperatura często przechodzi przez 0°C: w górach i strefie subpolarnej. Tworzy piargi (Tatry) i gołoborza (Góry Świętokrzyskie).'),
]
