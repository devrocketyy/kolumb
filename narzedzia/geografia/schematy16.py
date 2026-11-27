# Schematy geografii — porcja 16 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    """Strzałka z grotem."""
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Lej depresyjny wokół odkrywki ----------
_l = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_l += '<path class="gg ol" d="M0 90 H140 L165 175 H235 L260 90 H400 V300 H0 Z"/>'          # grunt z wyrobiskiem
_l += '<path class="gs ol" d="M0 250 H400 V300 H0 Z"/>'                                    # skała nieprzepuszczalna
_l += '<path class="gw2" d="M0 120 C70 122 120 150 160 195 H240 C280 150 330 122 400 120 V250 H0 Z" style="opacity:.55"/>'
_l += '<path class="cold" d="M0 120 C70 122 120 150 160 195 H240 C280 150 330 122 400 120" style="stroke-width:2.2"/>'
_l += '<path class="dash" d="M0 108 H400"/>'
_l += '<path class="gm2 ol" d="M175 160 h50 v15 h-50 Z"/>'                                  # pokład węgla
_l += '<rect class="gs2 ol" x="196" y="120" width="8" height="70"/>' + strz(200, 125, 200, 70, 'cold')
_l += '<text class="ts" x="392" y="290" text-anchor="end">skała nieprzepuszczalna</text>'
for x in (50, 340):
    _l += f'<rect class="gs2 ol" x="{x}" y="70" width="6" height="22"/><path class="s" d="M{x + 3} 70 v-10"/>'
S['g-srodowisko'] = [
 dict(typ='rysunek', tytul='Lej depresyjny wokół kopalni odkrywkowej', svg=_l,
      znaczniki=[(200, 168, 290, 40, 'Pokład węgla', 'Złoże pod wodonośnymi piaskami — trzeba je osuszyć'),
                 (200, 95, 110, 18, 'Pompy odwadniające', 'Studnie wypompowują wodę z wyrobiska'),
                 (130, 160, 60, 210, 'Lej depresyjny', 'Zwierciadło wód obniża się stożkowo ku odkrywce'),
                 (53, 85, 30, 135, 'Wysychające studnie', 'Studnie i mokradła w zasięgu leja tracą wodę'),
                 (300, 108, 345, 245, 'Dawny poziom wód', 'Przerywana linia — zwierciadło przed eksploatacją')],
      opis='Przekrój przez odkrywkę węgla brunatnego (np. Bełchatów) z rysunkiem autorskim IndexLab.',
      uwaga='Lej depresyjny powiększa się wraz z pogłębianiem wyrobiska. Skutki: zanik studni, przesuszenie gleb i lasów, osiadanie terenu. Po zakończeniu wydobycia wyrobisko zalewa się (np. jezioro Bełchatów).'),
]

# ---------- 2. Antyklina i synklina ----------
_f = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
cols = ('gs', 'gc', 'gp', 'gs2')
for i, c in enumerate(cols):
    off = i * 28
    top = f'M0 {150 + off} C60 {150 + off} 70 {70 + off} 130 {70 + off} C190 {70 + off} 200 {230 + off} 270 {230 + off} C340 {230 + off} 350 {150 + off} 400 {150 + off}'
    bot = f'L400 {178 + off} C350 {178 + off} 340 {258 + off} 270 {258 + off} C200 {258 + off} 190 {98 + off} 130 {98 + off} C70 {98 + off} 60 {178 + off} 0 {178 + off} Z'
    _f += f'<path class="{c} ol" d="{top} {bot}"/>'
_f += '<path class="gl ol" d="M0 150 C60 150 70 70 130 70 C190 70 200 230 270 230 C340 230 350 150 400 150 V0 H0 Z" style="opacity:.0"/>'
_f += '<path class="dash" d="M130 40 V290"/><path class="dash" d="M270 40 V290"/>'
_f += '<text class="tb" x="130" y="32" text-anchor="middle">oś antykliny</text><text class="tb" x="270" y="32" text-anchor="middle">oś synkliny</text>'
_f += strz(20, 280, 70, 280) + strz(380, 280, 330, 280)
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Fałd: antyklina i synklina', svg=_f,
      znaczniki=[(130, 85, 70, 55, 'Antyklina', 'Siodło — warstwy wygięte ku górze; w jądrze najstarsze skały'),
                 (270, 245, 330, 80, 'Synklina', 'Łęk — warstwy wygięte w dół; w jądrze najmłodsze skały'),
                 (200, 160, 230, 120, 'Skrzydło fałdu', 'Nachylona część warstw między osiami'),
                 (45, 280, 60, 230, 'Kompresja', 'Ściskanie poziome przy zderzeniu płyt fałduje warstwy')],
      opis='Przekrój przez sfałdowane warstwy skał osadowych (rysunek autorski IndexLab).',
      uwaga='Fałdowanie to deformacja ciągła (warstwy nie pękają). Na mapie geologicznej antyklinę rozpoznasz po najstarszych skałach w osi, synklinę — po najmłodszych. Przykład w Polsce: Góry Świętokrzyskie, Pieniny, Karpaty fliszowe.'),
]

# ---------- 3. Drogi Słońca na 52°N ----------
_s = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_s += '<path class="gt ol" d="M0 230 H400 V300 H0 Z"/>'
for (h, x1, x2, cls, lab) in ((61.5, 45, 355, 'hot', '22 VI'), (38, 95, 305, 's', '21 III / 23 IX'), (14.5, 145, 255, 'cold', '22 XII')):
    ymax = 230 - h * 2.6
    _s += f'<path class="{cls}" fill="none" d="M{x1} 230 Q200 {2 * ymax - 230:.0f} {x2} 230" style="stroke-width:2.2"/>'
    _s += f'<circle class="{"hotf" if cls == "hot" else ("coldf" if cls == "cold" else "gs2")}" cx="200" cy="{ymax:.0f}" r="7"/>'
    _s += f'<text class="ts" x="210" y="{ymax - 9:.0f}">{lab} · {str(h).replace(".", ",")}°</text>'
_s += '<path class="dash" d="M200 230 V40"/>'
_s += '<text class="tb" x="45" y="250" text-anchor="middle">NE</text><text class="tb" x="95" y="250" text-anchor="middle">E</text><text class="tb" x="145" y="250" text-anchor="middle">SE</text>'
_s += '<text class="tb" x="200" y="250" text-anchor="middle">S</text>'
_s += '<text class="tb" x="255" y="250" text-anchor="middle">SW</text><text class="tb" x="305" y="250" text-anchor="middle">W</text><text class="tb" x="355" y="250" text-anchor="middle">NW</text>'
_s += '<text class="ts" x="200" y="285" text-anchor="middle">widok na południe · horyzont</text>'
S['g-slonce'] = [
 dict(typ='rysunek', tytul='Drogi Słońca nad horyzontem na 52°N', svg=_s,
      znaczniki=[(45, 230, 30, 205, 'Wschód latem', '22 VI Słońce wschodzi na NE — dzień ok. 16,5 h'),
                 (200, 70, 120, 55, 'Górowanie letnie', '90° − 52° + 23°26′ ≈ 61,5°'),
                 (95, 230, 70, 270, 'Wschód w równonoc', 'Dokładnie na E, dzień = noc (12 h)'),
                 (200, 192, 300, 175, 'Górowanie zimowe', '90° − 52° − 23°26′ ≈ 14,5°; dzień ok. 7,5 h'),
                 (200, 150, 290, 120, 'Południe słoneczne', 'Słońce zawsze góruje dokładnie na S')],
      opis='Pozorne dobowe drogi Słońca w Polsce w dniach przesileń i równonocy (rysunek autorski IndexLab).',
      uwaga='Im wyżej Słońce góruje, tym dłuższa jest jego droga nad horyzontem i dłuższy dzień. Latem w Polsce Słońce wschodzi na NE i zachodzi na NW, zimą — na SE i SW.'),
]

# ---------- 4. Wiatr a izobary ----------
_w = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
for i, p in enumerate((1000, 1005, 1010, 1015, 1020)):
    y = 50 + i * 50
    _w += f'<path class="s" d="M20 {y} C140 {y - 8} 250 {y + 8} 352 {y}"/><text class="ts" x="356" y="{y + 4}">{p} hPa</text>'
_w += '<text class="tb" x="20" y="30">NIŻ (L)</text><text class="tb" x="20" y="290">WYŻ (H)</text>'
_w += strz(110, 230, 110, 140, 'hot')            # siła gradientu
_w += strz(110, 200, 190, 200, 'cold')           # Coriolis
_w += strz(260, 230, 320, 170, 's')              # wiatr przyziemny
_w += strz(250, 120, 330, 120, 's')              # wiatr geostroficzny
S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Wiatr a izobary: siły kształtujące kierunek wiatru (półkula N)', svg=_w,
      znaczniki=[(110, 150, 60, 110, 'Siła gradientu', 'Pcha powietrze od wyżu do niżu, prostopadle do izobar'),
                 (180, 200, 170, 245, 'Siła Coriolisa', 'Odchyla ruch w prawo na półkuli N'),
                 (300, 190, 240, 285, 'Wiatr przyziemny', 'Tarcie osłabia Coriolisa — wiatr przecina izobary pod kątem'),
                 (300, 120, 300, 80, 'Wiatr geostroficzny', 'Wysoko (bez tarcia) wieje równolegle do izobar')],
      opis='Schemat sił działających na poruszające się powietrze (rysunek autorski IndexLab).',
      uwaga='Na półkuli N, stojąc plecami do wiatru, niż masz po lewej (prawo Buys-Ballota). Im gęstsze izobary, tym większy gradient i silniejszy wiatr.'),
]

# ---------- 5. Grzbiet śródoceaniczny ----------
_g = '<rect class="gw" x="0" y="0" width="400" height="120"/>'
_g += '<path class="gm ol" d="M0 300 V180 H400 V300 Z"/>'
for i, c in enumerate(('gs', 'gs2', 'gc', 'gs2', 'gs')):
    _g += f'<path class="{c} ol" d="M{40 * i} 120 L{40 * i} 180 L{40 * i + 40} 180 L{40 * i + 40} 120 Z"/>'
    _g += f'<path class="{c} ol" d="M{400 - 40 * i} 120 L{400 - 40 * i} 180 L{360 - 40 * i} 180 L{360 - 40 * i} 120 Z"/>'
_g += '<path class="gs ol" d="M0 120 L170 110 L190 85 L200 100 L210 85 L230 110 L400 120 V122 H0 Z"/>'
_g += '<path class="gm2" d="M195 180 L190 120 H210 L205 180 Z"/>'
_g += '<path class="hot" fill="none" d="M200 290 C200 240 200 220 200 185"/>'
_g += '<path class="hot" fill="none" d="M200 260 C150 255 90 240 60 210"/><path class="hot" fill="none" d="M200 260 C250 255 310 240 340 210"/>'
_g += strz(150, 150, 70, 150, 's') + strz(250, 150, 330, 150, 's')
_g += '<text class="ts" x="8" y="114">ocean</text><text class="ts" x="8" y="296">płaszcz (astenosfera)</text>'
S['g-tektonika'].append(
 dict(typ='rysunek', tytul='Grzbiet śródoceaniczny i spreading', svg=_g,
      znaczniki=[(200, 92, 260, 50, 'Ryft', 'Dolina w osi grzbietu — tu powstaje nowa skorupa'),
                 (200, 150, 290, 205, 'Magma', 'Wypływa ze szczeliny i krzepnie jako bazalt'),
                 (100, 150, 70, 60, 'Rozsuwanie płyt', 'Płyty oddalają się o kilka cm rocznie'),
                 (60, 210, 50, 255, 'Prądy konwekcyjne', 'Rozbieżne prądy w płaszczu ciągną płyty na boki'),
                 (20, 150, 110, 210, 'Najstarsze skały', 'Wiek dna rośnie symetrycznie z odległością od ryftu')],
      opis='Przekrój przez granicę rozbieżną na dnie oceanu (rysunek autorski IndexLab).',
      uwaga='Przykład: Grzbiet Śródatlantycki i Islandia. Symetryczne pasy wieku i namagnesowania skał po obu stronach grzbietu to dowód rozrastania się dna oceanicznego (spreadingu).'))


def _dopasuj(z):
    """Przestawia podpis pinu na stronę, po której mieści się w kadrze 400 px."""
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
