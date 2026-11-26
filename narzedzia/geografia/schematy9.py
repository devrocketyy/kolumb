# Schematy geografii — porcja 9 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- piętra w Andach ----------
_hy = lambda h: 280 - h * 0.05
_gora = 'M10 280 L10 270 L40 255 L70 225 L95 190 L120 150 L140 110 L160 70 L175 40 L185 32 L195 44 L215 90 L240 150 L265 200 L290 240 L310 280 Z'
_an = (f'<defs><clipPath id="g9an"><path d="{_gora}"/></clipPath></defs>'
       '<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<g transform="scale(0.8 1)"><g clip-path="url(#g9an)">'
       f'<rect class="gf2" x="0" y="{_hy(1000):.0f}" width="320" height="60"/>'
       f'<rect class="gf" x="0" y="{_hy(2000):.0f}" width="320" height="{_hy(1000) - _hy(2000):.0f}"/>'
       f'<rect class="gt" x="0" y="{_hy(3500):.0f}" width="320" height="{_hy(2000) - _hy(3500):.0f}"/>'
       f'<rect class="gp" x="0" y="{_hy(4500):.0f}" width="320" height="{_hy(3500) - _hy(4500):.0f}"/>'
       f'<rect class="gi" x="0" y="0" width="320" height="{_hy(4500):.0f}" style="stroke:none"/></g>'
       f'<path class="s" d="{_gora}"/></g>'
       + ''.join(f'<path class="dash" d="M10 {_hy(h):.0f} H258"/><path class="s" d="M6 {_hy(h):.0f} H10"/><text class="ts" x="4" y="{_hy(h) - 3:.0f}">{h} m</text>' for h in (1000, 2000, 3500, 4500))
       + ''.join(f'<text class="ts" x="258" y="{_hy(h) - 3:.0f}" text-anchor="end">{t}</text>' for h, t in ((500, '24–28°C'), (1500, '18–24°C'), (2750, '12–18°C'), (4000, '6–12°C'), (5000, '< 6°C'))))
S['g-biomy'] = [
 dict(typ='rysunek', tytul='Piętra klimatyczno-roślinne w Andach', svg=_an,
      znaczniki=[(48, 262, 262, 262, 'Tierra caliente', 'Do ok. 1000 m — las równikowy, banany, kakao, trzcina'),
                 (76, 212, 262, 215, 'Tierra templada', 'Do ok. 2000 m — kawa, kukurydza; najgęściej zaludnione'),
                 (104, 162, 262, 165, 'Tierra fría', 'Do ok. 3500 m — ziemniaki, zboża; Bogota, Quito'),
                 (128, 98, 262, 110, 'Puna / páramo', 'Do ok. 4500 m — murawy, wypas lam i alpak'),
                 (146, 40, 262, 55, 'Tierra helada', 'Wiecznie śnieżne szczyty')],
      opis='Piętrowość klimatu i użytkowania ziemi w Andach równikowych (wartości przybliżone).',
      uwaga='W strefie równikowej to wysokość, a nie pora roku, decyduje o temperaturze — w górach można przejść przez wszystkie strefy klimatyczne na kilkudziesięciu kilometrach.'),
]

# ---------- fiord i szkiery ----------
_fs = ('<rect class="gw2" x="0" y="0" width="400" height="300"/>'
       '<path class="gs" d="M0 0 H190 V300 H0 Z"/>'
       '<path class="gw2" d="M0 150 C40 140 70 160 100 130 C120 110 140 120 160 90 C170 78 182 80 190 70 L190 82 C178 92 168 98 160 108 C140 132 125 124 105 145 C78 172 40 160 0 170 Z"/>'
       '<path class="gs2" d="M0 0 H190 V60 C150 70 110 60 60 80 C40 90 20 110 0 115 Z" opacity="0.6"/>'
       '<path class="gi" d="M120 20 C140 10 170 15 185 30 C165 40 140 35 120 20 Z"/>'
       '<path class="gt" d="M210 0 H400 V300 H210 Z"/>'
       '<path class="gw2" d="M210 120 C260 140 300 200 260 300 H210 Z"/>'
       + ''.join(f'<ellipse class="gs ol" cx="{x}" cy="{y}" rx="{r}" ry="{r * 0.6:.1f}"/>' for x, y, r in ((222, 150, 5), (238, 170, 7), (225, 195, 4), (250, 205, 6), (232, 225, 5), (255, 240, 4), (240, 260, 6), (225, 280, 4), (262, 275, 5), (248, 185, 3), (270, 225, 3)))
       + '<rect class="gn" x="190" y="0" width="20" height="300"/>'
       '<text class="tb" x="95" y="292" text-anchor="middle">fiord</text><text class="tb" x="330" y="292" text-anchor="middle">szkiery</text>')
S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Wybrzeże fiordowe i szkierowe (widok z góry)', svg=_fs,
      znaczniki=[(120, 120, 60, 210, 'Fiord', 'Zalany żłób lodowcowy: wąski, głęboki, ze stromymi ścianami'),
                 (150, 25, 100, 40, 'Lodowiec', 'Dawniej wypełniał dolinę aż do morza'),
                 (238, 170, 320, 120, 'Szkiery', 'Zalane wygłady i mutony — tysiące wysepek'),
                 (300, 80, 285, 40, 'Ląd wygładzony', 'Rzeźba wypolerowana przez lądolód')],
      opis='Dwa typy wybrzeży powstałych z zalania rzeźby polodowcowej.',
      uwaga='Fiordy — Norwegia, Chile, Nowa Zelandia; szkiery — Szwecja, Finlandia. Oba powstały po stopnieniu lądolodu i podniesieniu poziomu morza.'),
]

# ---------- dorzecze i dział wodny ----------
_dz = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
       '<path class="gw2" d="M0 250 Q120 240 240 255 Q320 262 400 250 V300 H0 Z"/>'
       '<path class="gl" d="M30 30 C80 10 160 20 200 40 C240 60 260 110 250 160 C240 200 200 230 160 250 C110 255 60 240 40 200 C20 150 10 80 30 30 Z" opacity="0.55"/>'
       '<path class="dash" d="M30 30 C80 10 160 20 200 40 C240 60 260 110 250 160 C240 200 200 230 160 250 C110 255 60 240 40 200 C20 150 10 80 30 30 Z" style="stroke-width:2"/>'
       '<path class="cold" d="M140 248 C135 200 140 150 120 110 C105 80 90 60 70 40" style="stroke-width:3.4"/>'
       '<path class="cold" d="M134 190 C170 180 200 160 225 130 M124 120 C100 125 70 120 45 140 M140 160 C110 170 80 180 55 205 M115 90 C140 75 170 65 195 55" style="stroke-width:1.8"/>'
       '<path class="cold" d="M330 250 C325 200 310 150 300 90 M318 170 C340 160 360 140 380 120" style="stroke-width:2.4"/>')
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Dorzecze i dział wodny (widok z góry)', svg=_dz,
      znaczniki=[(72, 42, 60, 15, 'Źródło', 'Początek rzeki głównej'),
                 (135, 175, 180, 200, 'Rzeka główna', 'Uchodzi do morza'),
                 (210, 145, 270, 70, 'Dopływ', 'Prawy dopływ rzeki głównej'),
                 (245, 120, 290, 30, 'Dział wodny', 'Granica dorzecza — linia grzbietowa'),
                 (100, 200, 110, 280, 'Dorzecze', 'Obszar, z którego wody spływają do jednej rzeki'),
                 (330, 230, 300, 280, 'Inne dorzecze', 'Inna rzeka — po drugiej stronie działu')],
      opis='Schemat dorzecza z siecią rzeczną.',
      uwaga='Dorzecze — obszar zasilania jednej rzeki; zlewisko — obszar odwadniany do jednego morza lub oceanu. Prawy i lewy dopływ określa się, patrząc z biegiem rzeki.'),
]

# ---------- tarasy ryżowe ----------
_st = [(20, 250), (80, 210), (140, 170), (200, 130), (260, 90), (320, 50)]
_tt = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_pts = 'M0 300 L0 250 ' + ' '.join(f'L{x + 60} {y} L{x + 60} {y - 40}' for x, y in _st[:-1]) + ' L400 50 L400 300 Z'
_tt += f'<path class="gl" d="{_pts}"/>'
for x, y in _st[:-1]:
    _tt += f'<rect class="gw" x="{x + 2}" y="{y - 8}" width="56" height="8"/>'
    _tt += ''.join(f'<path class="gf2" d="M{x + 8 + i * 9} {y - 7} l-2 -9 M{x + 8 + i * 9} {y - 7} l2 -9" style="stroke:var(--g-las2);stroke-width:1.4;fill:none"/>' for i in range(6))
    _tt += f'<rect class="gc" x="{x + 56}" y="{y - 12}" width="5" height="12"/>'
_tt += '<path class="s" d="' + _pts.replace(' Z', '').replace('M0 300 L0 250', 'M0 250') + '"/>'
_tt += '<path class="dash" d="M0 250 L380 30"/><text class="ts" x="20" y="228">pierwotny stok</text>'
_tt += '<path class="f" d="M345 50 v-12 l8 -8 l8 8 v12 Z"/>'
S['g-uprawy'] = [
 dict(typ='rysunek', tytul='Tarasy ryżowe na stoku (przekrój)', svg=_tt,
      znaczniki=[(110, 205, 120, 150, 'Pole ryżowe', 'Zalane wodą — ryż rośnie w płytkiej wodzie'),
                 (138, 196, 175, 225, 'Grobla', 'Zatrzymuje wodę i glebę na tarasie'),
                 (230, 115, 210, 60, 'Taras', 'Poziomy stopień wycięty w stoku'),
                 (300, 70, 305, 110, 'Mniej erozji', 'Tarasy zatrzymują spływ wody i gleby')],
      opis='Uprawa ryżu na tarasach — Azja Południowo-Wschodnia (np. Indonezja, Filipiny, Chiny).',
      uwaga='Tarasowanie pozwala uprawiać strome stoki, chroni glebę przed erozją i umożliwia zalewanie pól. Wymaga bardzo dużych nakładów pracy ręcznej — rolnictwo intensywne tradycyjne.'),
]

# ---------- komórka Hadleya ----------
_hd = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<rect class="gf" x="20" y="240" width="120" height="20"/><rect class="gp" x="260" y="240" width="120" height="20"/>'
       '<rect class="gl" x="140" y="240" width="120" height="20"/>'
       '<path class="s" d="M20 240 H380 M20 40 V260"/>'
       + strz(70, 220, 70, 70, 's', 9) + strz(90, 55, 300, 55, 's', 9) + strz(330, 70, 330, 220, 's', 9) + strz(310, 230, 100, 230, 'cold', 9)
       + '<path class="gk" d="M50 150 q-10 0 -10 -9 q0 -10 12 -9 q4 -12 18 -9 q10 -7 18 3 q12 0 12 10 q0 9 -12 9 Z"/>'
       + ''.join(f'<path class="cold" style="stroke-width:1.2" d="M{x} 156 l-3 12"/>' for x in (55, 66, 77, 88))
       + '<circle class="gm2" cx="330" cy="120" r="12"/>'
       + '<text class="tb" x="70" y="276" text-anchor="middle">0° · N</text><text class="tb" x="330" y="276" text-anchor="middle">30°N · W</text>'
       '<text class="ts" x="195" y="48" text-anchor="middle">ok. 12–15 km</text>'
       '<text class="ts" x="200" y="296" text-anchor="middle">N — niż równikowy, W — wyż zwrotnikowy</text>')
S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Komórka Hadleya (przekrój pionowy)', svg=_hd,
      znaczniki=[(70, 180, 110, 160, 'Wznoszenie', 'Nagrzane powietrze nad równikiem — chmury i ulewy'),
                 (200, 55, 210, 90, 'Odpływ górą', 'Powietrze płynie ku zwrotnikom'),
                 (330, 180, 290, 160, 'Osiadanie', 'Suche powietrze ogrzewa się — pustynie'),
                 (200, 230, 230, 205, 'Pasaty', 'Wracają przy ziemi ku równikowi')],
      opis='Pionowy schemat cyrkulacji między równikiem a zwrotnikiem (półkula N).',
      uwaga='Komórka Hadleya tłumaczy wilgotny klimat równikowy (wznoszenie, opady zenitalne) i pustynie zwrotnikowe (osiadanie suchego powietrza w wyżach).'),
]

# ---------- model von Thünena ----------
_vt = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
       '<circle class="gp" cx="150" cy="150" r="135" opacity="0.7"/>'
       '<circle class="gt" cx="150" cy="150" r="105" style="stroke:var(--text-2)"/>'
       '<circle class="gc" cx="150" cy="150" r="78" opacity="0.8"/>'
       '<circle class="gf2" cx="150" cy="150" r="52"/>'
       '<circle class="gf" cx="150" cy="150" r="28"/>'
       '<rect class="d" x="140" y="140" width="20" height="20"/>')
S['g-rolnictwo'] = [
 dict(typ='rysunek', tytul='Model pierścieni von Thünena', svg=_vt,
      znaczniki=[(150, 150, 300, 40, 'Miasto', 'Rynek zbytu w centrum'),
                 (169, 150, 300, 80, 'Ogrodnictwo', 'Warzywa, mleko — szybko się psują, drogi transport'),
                 (190, 150, 300, 120, 'Las', 'Drewno na opał i budowę — ciężkie w transporcie'),
                 (215, 150, 300, 160, 'Uprawy polowe', 'Uprawy polowe z płodozmianem'),
                 (242, 150, 300, 200, 'Ekstensywne', 'Ugorowanie, niższe nakłady'),
                 (270, 150, 300, 240, 'Hodowla', 'Ekstensywny wypas — zwierzęta „idą same” na rynek')],
      opis='Model rozmieszczenia upraw wokół rynku zbytu (J.H. von Thünen, 1826).',
      uwaga='Im dalej od miasta, tym wyższe koszty transportu i niższa renta z ziemi — dlatego blisko miasta opłacają się uprawy intensywne, a daleko ekstensywne.'),
]
