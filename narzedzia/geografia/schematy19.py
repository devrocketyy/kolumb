# Schematy geografii — porcja 19 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Kolizja kontynentów — Himalaje ----------
_h = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_h += '<path class="gm" d="M0 230 H400 V300 H0 Z"/>'
_h += '<path class="gl ol" d="M0 150 H120 L140 175 L150 230 H0 Z"/>'                              # płyta indyjska
_h += '<path class="gs2 ol" d="M120 150 C150 140 170 160 185 215 L150 230 L140 175 Z"/>'           # wsuwająca się
_h += '<path class="gl2 ol" d="M150 230 C170 120 190 40 220 45 C250 50 260 110 290 130 H400 V230 Z"/>'  # Himalaje + Tybet
_h += '<path class="gs ol" d="M175 150 C190 120 205 95 220 90 C235 95 240 120 250 140" style="fill:none"/>'
_h += '<path class="gi" d="M205 55 L220 45 L235 55 C225 60 215 60 205 55 Z"/>'
_h += strz(30, 190, 110, 190, 's')
_h += '<text class="tb" x="40" y="140">płyta indyjska</text><text class="tb" x="300" y="122">płyta euroazjatycka</text>'
_h += '<text class="ts" x="8" y="292">płaszcz</text>'
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Kolizja kontynentów: powstanie Himalajów', svg=_h,
      znaczniki=[(70, 190, 60, 260, 'Ruch płyty indyjskiej', 'Ok. 4–5 cm rocznie ku północy'),
                 (165, 190, 100, 215, 'Pogrubienie skorupy', 'Lekka skorupa kontynentalna nie zanurza się głęboko — piętrzy się'),
                 (220, 50, 280, 30, 'Najwyższe szczyty', 'Mount Everest 8849 m — góry wciąż rosną'),
                 (320, 140, 330, 180, 'Wyżyna Tybetańska', 'Wypiętrzona na ok. 4500 m za pasmem Himalajów'),
                 (210, 100, 120, 100, 'Sfałdowane osady', 'Skały dawnego oceanu Tetydy — skamieniałości morskie na szczytach')],
      opis='Uproszczony przekrój przez strefę kolizji płyty indyjskiej z euroazjatycką — rysunek autorski IndexLab.',
      uwaga='Przy kolizji dwóch płyt kontynentalnych nie ma wulkanizmu typowego dla subdukcji, ale są silne trzęsienia ziemi (Nepal 2015). Podobnie powstały Alpy (płyta afrykańska) i Kaukaz.'),
]

# ---------- 2. Żuławy i przekopy ----------
_z = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
_z += '<path class="gl ol" d="M0 300 V120 C40 110 70 125 110 115 C150 105 200 120 250 110 C300 100 340 120 400 110 V300 Z"/>'
_z += '<path class="gt ol" d="M90 300 C100 220 140 160 200 140 C260 160 300 220 320 300 Z"/>'     # Żuławy
_z += '<path class="cold" d="M150 300 C160 240 180 190 199 112" style="fill:none;stroke-width:4"/>'
_z += '<path class="gw" d="M198 140 L200 112 L205 112 L203 140 Z"/>'
_z += '<path class="cold" d="M190 175 C230 180 270 190 305 190" style="fill:none;stroke-width:2.5"/>'  # Nogat
_z += '<path class="gw ol" d="M300 170 C330 150 370 150 400 160 V215 C370 225 330 215 300 200 Z"/>'  # Zalew Wiślany
_z += '<path class="gp ol" d="M260 120 C300 115 360 125 400 118 V128 C360 135 300 126 262 128 Z"/>'  # mierzeja
_z += '<path class="hot" d="M350 120 V132" style="stroke-width:3"/>'
_z += '<text class="tb" x="20" y="40">Zatoka Gdańska</text><text class="ts" x="392" y="292" text-anchor="end">teren nad poziomem morza</text>'
S['g-pl-wody'] = [
 dict(typ='rysunek', tytul='Żuławy Wiślane i przekopy (plan uproszczony)', svg=_z,
      znaczniki=[(200, 125, 120, 80, 'Przekop Wisły', '1895 — sztuczne, krótkie ujście chroniące Żuławy przed powodziami'),
                 (200, 220, 130, 250, 'Żuławy', 'Delta Wisły z madami; część poniżej poziomu morza — poldery i pompy'),
                 (260, 186, 330, 250, 'Nogat', 'Ramię delty płynące do Zalewu Wiślanego'),
                 (350, 185, 340, 90, 'Zalew Wiślany', 'Laguna odcięta Mierzeją Wiślaną'),
                 (350, 126, 300, 60, 'Przekop Mierzei', '2022 — kanał żeglugowy do portu w Elblągu')],
      opis='Uproszczony plan delty Wisły — rysunek autorski IndexLab (bez skali).',
      uwaga='Żuławy to najżyźniejszy region Polski (mady), ale wymagają stałego odwadniania: wały, kanały, przepompownie. Najniższy punkt Polski: Raczki Elbląskie (ok. −1,8 m).'),
]

# ---------- 3. Przekrój pionowy niżu i wyżu ----------
_c = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_c += '<path class="gt ol" d="M0 250 H400 V300 H0 Z"/>'
_c += '<path class="gk ol" d="M60 200 C50 130 90 70 120 80 C150 70 190 130 180 200 Z"/>'
_c += strz(120, 200, 120, 70, 'hot') + strz(30, 240, 100, 240, 's') + strz(210, 240, 140, 240, 's')
_c += strz(130, 50, 200, 40, 's') + strz(110, 50, 40, 40, 's')
_c += strz(300, 70, 300, 220, 'cold') + strz(310, 240, 380, 240, 's') + strz(290, 240, 230, 240, 's')
_c += strz(250, 50, 290, 60, 's') + strz(370, 50, 320, 60, 's')
_c += '<text class="tb" x="120" y="275" text-anchor="middle">NIŻ (L)</text><text class="tb" x="300" y="275" text-anchor="middle">WYŻ (H)</text>'
S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Ruch powietrza w niżu i wyżu (przekrój pionowy)', svg=_c,
      znaczniki=[(120, 140, 40, 105, 'Prądy wstępujące', 'Powietrze wznosi się, ochładza — chmury i opady'),
                 (60, 240, 30, 220, 'Zbieżność przy ziemi', 'Powietrze napływa do środka niżu'),
                 (300, 150, 360, 160, 'Prądy zstępujące', 'Powietrze opada i ogrzewa się — zanikają chmury'),
                 (350, 240, 360, 195, 'Rozbieżność przy ziemi', 'Powietrze wypływa z wyżu na boki'),
                 (170, 45, 210, 20, 'Odpływ górą', 'Na wysokości niż „wysysa” powietrze, wyż je przyjmuje')],
      opis='Schemat cyrkulacji w układach barycznych — rysunek autorski IndexLab.',
      uwaga='Niż: zbieżność przy ziemi + ruch wstępujący = pogoda pochmurna i deszczowa. Wyż: ruch zstępujący + rozbieżność = pogoda bezchmurna (latem upał, zimą mróz i mgły).'),
]

# ---------- 4. Arktyka i Antarktyka ----------
_a = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_a += '<circle class="gw ol" cx="100" cy="150" r="90"/>'
_a += '<path class="gl ol" d="M10 150 C20 100 40 70 70 62 L60 90 C45 110 40 130 42 150 Z M190 150 C185 110 165 80 140 66 L150 95 C165 115 168 135 168 150 Z M60 235 C80 245 120 245 140 236 L130 215 C110 222 90 222 70 214 Z"/>'
_a += '<path class="gi ol" d="M90 75 C120 70 135 90 128 105 C115 112 100 108 90 98 Z"/>'   # Grenlandia
_a += '<circle class="gi" cx="100" cy="150" r="38" style="opacity:.85"/>'                    # lód morski
_a += '<circle class="gw ol" cx="300" cy="150" r="90"/>'
_a += '<path class="gi ol" d="M240 150 C240 100 280 85 310 92 C350 100 365 130 358 160 C350 200 310 215 280 205 C255 197 240 180 240 150 Z"/>'
_a += '<circle class="d" cx="100" cy="150" r="3"/><circle class="d" cx="300" cy="150" r="3"/>'
_a += '<text class="tb" x="100" y="20" text-anchor="middle">ARKTYKA</text><text class="tb" x="300" y="20" text-anchor="middle">ANTARKTYKA</text>'
_a += '<text class="ts" x="100" y="290" text-anchor="middle">ocean otoczony lądami</text><text class="ts" x="300" y="290" text-anchor="middle">kontynent otoczony oceanem</text>'
S['g-lodowce'] = [
 dict(typ='rysunek', tytul='Arktyka i Antarktyka — porównanie (widok znad biegunów)', svg=_a,
      znaczniki=[(100, 150, 60, 200, 'Lód morski', 'Kra i pak lodowy grubości kilku m — kurczy się latem'),
                 (110, 88, 160, 40, 'Grenlandia', 'Lądolód na wyspie — jedyny lądolód półkuli N'),
                 (300, 140, 330, 120, 'Lądolód antarktyczny', 'Średnio ok. 2 km lodu na kontynencie'),
                 (300, 230, 340, 255, 'Ocean Południowy', 'Silny Dryf Wiatrów Zachodnich wokół kontynentu'),
                 (40, 120, 30, 70, 'Wybrzeża Eurazji i Ameryki', 'Tundra i wieloletnia zmarzlina')],
      opis='Uproszczone mapy obszarów okołobiegunowych — rysunek autorski IndexLab.',
      uwaga='Antarktyka jest zimniejsza od Arktyki: wysoki kontynent pokryty lodem i izolowany przez prąd okołobiegunowy. W Arktyce ocean łagodzi zimę (−30 do −40°C), na Antarktydzie notowano −89°C.'),
]

# ---------- 5. Mała retencja ----------
_r = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_r += '<path class="gt ol" d="M0 120 C100 130 200 180 400 200 V300 H0 Z"/>'
_r += '<path class="gg" d="M0 230 C120 240 250 260 400 265 V300 H0 Z" style="opacity:.6"/>'
for x in (20, 45, 70):
    _r += f'<path class="gf ol" d="M{x} {122 + x * 0.1:.0f} l9 -28 l9 28 Z"/>'
_r += '<ellipse class="gw ol" cx="170" cy="160" rx="30" ry="7"/>'
_r += '<path class="gw2" d="M240 178 C270 182 300 192 330 197" style="fill:none;stroke-width:4"/>'
_r += '<rect class="gs2 ol" x="285" y="180" width="6" height="18"/>'
_r += '<path class="gw ol" d="M340 205 h40 v10 h-40 Z"/>'
_r += '<rect class="gl2 ol" x="95" y="95" width="30" height="25"/><path class="gs ol" d="M92 95 L110 80 L128 95 Z"/><path class="gw ol" d="M128 115 h8 v15 h-8 Z"/>'
_r += strz(150, 40, 150, 80, 'cold') + strz(260, 40, 260, 80, 'cold')
S['g-srodowisko'] = [
 dict(typ='rysunek', tytul='Mała retencja w krajobrazie rolniczym', svg=_r,
      znaczniki=[(45, 110, 30, 60, 'Zadrzewienia', 'Zatrzymują opad, ograniczają spływ i erozję'),
                 (132, 122, 60, 170, 'Zbiornik na deszczówkę', 'Woda z dachów do podlewania'),
                 (170, 160, 200, 110, 'Oczko wodne', 'Gromadzi wodę i zasila wody gruntowe'),
                 (288, 185, 300, 140, 'Zastawka na rowie', 'Spowalnia odpływ wody z pól'),
                 (360, 210, 330, 250, 'Mokradło', 'Naturalny „magazyn wody” i siedlisko')],
      opis='Elementy małej retencji w zlewni rolniczej — rysunek autorski IndexLab.',
      uwaga='Mała retencja to tanie, rozproszone sposoby zatrzymywania wody tam, gdzie spadła. Łagodzi susze i spłaszcza fale powodziowe. W Polsce szczególnie ważna ze względu na małe zasoby wodne.'),
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
