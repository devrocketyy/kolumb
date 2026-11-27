# Schematy geografii — porcja 21 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Drogi Słońca na 30°S (widok na północ) ----------
_s = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
_s += '<path class="gt ol" d="M0 230 H400 V300 H0 Z"/>'
for (h, x1, x2, cls, lab) in ((83.5, 40, 360, 'hot', '22 XII · 83,5°'), (60, 90, 310, 's', '21 III / 23 IX · 60°'), (36.5, 140, 260, 'cold', '22 VI · 36,5°')):
    ymax = 230 - h * 2.2
    _s += f'<path class="{cls}" fill="none" d="M{x1} 230 Q200 {2 * ymax - 230:.0f} {x2} 230" style="stroke-width:2.2"/>'
    _s += f'<circle class="{"hotf" if cls == "hot" else ("coldf" if cls == "cold" else "gs2")}" cx="200" cy="{ymax:.0f}" r="7"/>'
    _s += f'<text class="ts" x="210" y="{ymax - 9:.0f}">{lab}</text>'
_s += '<path class="dash" d="M200 230 V30"/>'
for x, t in ((40, 'SE'), (90, 'E'), (140, 'NE'), (200, 'N'), (260, 'NW'), (310, 'W'), (360, 'SW')):
    _s += f'<text class="tb" x="{x}" y="250" text-anchor="middle">{t}</text>'
_s += '<text class="ts" x="200" y="285" text-anchor="middle">widok na północ · horyzont · 30°S</text>'
S['g-slonce'] = [
 dict(typ='rysunek', tytul='Drogi Słońca nad horyzontem na 30°S', svg=_s,
      znaczniki=[(200, 46, 110, 30, 'Lato na półkuli S', '22 XII: 90° − 30° + 23°26′ ≈ 83,5°'),
                 (200, 98, 300, 80, 'Równonoc', '90° − 30° = 60°'),
                 (200, 150, 300, 160, 'Zima na półkuli S', '22 VI: 90° − 30° − 23°26′ ≈ 36,5°'),
                 (200, 200, 120, 200, 'Górowanie na północy', 'Na półkuli S (poza zwrotnikiem) Słońce góruje nad północnym horyzontem')],
      opis='Pozorne drogi Słońca na szerokości 30°S (np. okolice Durbanu, Porto Alegre) — rysunek autorski IndexLab.',
      uwaga='Na półkuli południowej pory roku są odwrócone: najwyżej Słońce góruje 22 grudnia, najniżej 22 czerwca. Wschodzi na E/SE latem i NE zimą — odwrotnie niż w Polsce.'),
]

# ---------- 2. Linia zmiany daty ----------
_d = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
_d += '<path class="hot" d="M200 0 V60 L215 90 L215 140 L190 175 L190 230 L205 260 V300" style="fill:none;stroke-width:2.6"/>'
_d += '<path class="dash" d="M200 0 V300"/>'
_d += '<path class="gl ol" d="M150 40 C170 45 180 60 178 75 C160 80 145 65 150 40 Z"/>'   # Czukotka
_d += '<path class="gl ol" d="M240 60 C260 55 280 70 270 95 C255 100 240 85 240 60 Z"/>'  # Alaska
for x, y in ((235, 160), (245, 170), (160, 200), (172, 215), (228, 240)):
    _d += f'<circle class="gl ol" cx="{x}" cy="{y}" r="5"/>'
_d += '<text class="tb" x="100" y="150" text-anchor="middle">wtorek</text><text class="tb" x="300" y="150" text-anchor="middle">poniedziałek</text>'
_d += strz(120, 270, 80, 270, 's') + strz(280, 270, 320, 270, 's')
_d += '<text class="ts" x="100" y="290" text-anchor="middle">płynąc na zachód: +1 doba</text><text class="ts" x="300" y="290" text-anchor="middle">płynąc na wschód: −1 doba</text>'
S['g-obrotowy'] = [
 dict(typ='rysunek', tytul='Linia zmiany daty (schemat)', svg=_d,
      znaczniki=[(200, 30, 260, 20, 'Południk 180°', 'Linia zmiany daty biegnie w przybliżeniu wzdłuż niego'),
                 (215, 115, 300, 105, 'Odchylenia linii', 'Omija lądy i archipelagi, by jedno państwo miało jedną datę'),
                 (100, 150, 60, 200, 'Strona zachodnia', 'Na zachód od linii data jest o dobę późniejsza (Azja, Oceania)'),
                 (165, 58, 70, 40, 'Czukotka', 'Rosja — po stronie „jutra”'),
                 (255, 78, 330, 60, 'Alaska', 'USA — po stronie „wczoraj”')],
      opis='Uproszczony schemat linii zmiany daty na Pacyfiku (bez skali) — rysunek autorski IndexLab.',
      uwaga='Przekraczając linię zmiany daty z zachodu na wschód (np. z Japonii do USA) cofamy datę o jedną dobę, a ze wschodu na zachód — dodajemy dobę. Godzina się przy tym nie zmienia.'),
]

# ---------- 3. Wiry oceaniczne ----------
_w = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
_w += '<path class="dash" d="M0 150 H400"/><text class="ts" x="4" y="146">równik</text>'
_w += '<path class="gl ol" d="M0 20 H40 C50 80 45 220 35 280 H0 Z"/><path class="gl ol" d="M400 20 H360 C350 80 355 220 365 280 H400 Z"/>'
# wir N (zgodnie ze wskazówkami): W brzeg oceanu ciepły ku N, góra ku E, E brzeg zimny ku S, dół (równikowy) ku W
_w += '<path class="hot" fill="none" d="M80 135 C75 100 85 70 110 58" style="stroke-width:2.4"/>' + strz(84, 90, 92, 74, 'hot')
_w += '<path class="s" fill="none" d="M110 58 C170 45 240 45 290 58" style="stroke-width:2.4"/>' + strz(190, 49, 215, 49, 's')
_w += '<path class="cold" fill="none" d="M290 58 C315 70 325 100 320 135" style="stroke-width:2.4"/>' + strz(320, 105, 321, 122, 'cold')
_w += '<path class="hot" fill="none" d="M320 135 C250 142 150 142 80 135" style="stroke-width:2.4"/>' + strz(220, 141, 190, 141, 'hot')
# wir S (przeciwnie do wskazówek): W brzeg oceanu ciepły ku S, dół ku E, E brzeg zimny ku N, góra (równikowy) ku W
_w += '<path class="hot" fill="none" d="M80 165 C75 200 85 230 110 242" style="stroke-width:2.4"/>' + strz(84, 210, 92, 226, 'hot')
_w += '<path class="s" fill="none" d="M110 242 C170 255 240 255 290 242" style="stroke-width:2.4"/>' + strz(190, 251, 215, 251, 's')
_w += '<path class="cold" fill="none" d="M290 242 C315 230 325 200 320 165" style="stroke-width:2.4"/>' + strz(321, 195, 320, 178, 'cold')
_w += '<path class="hot" fill="none" d="M320 165 C250 158 150 158 80 165" style="stroke-width:2.4"/>' + strz(220, 159, 190, 159, 'hot')
_w += '<text class="tb" x="20" y="14">kontynent W</text><text class="tb" x="380" y="14" text-anchor="end">kontynent E</text>'
S['g-oceany'] = [
 dict(typ='rysunek', tytul='Wiry prądów oceanicznych (model oceanu)', svg=_w,
      znaczniki=[(82, 100, 100, 95, 'Prąd ciepły przy E brzegu', 'Wschodnie wybrzeża kontynentów: ciepłe prądy (Golfsztrom, Brazylijski)'),
                 (321, 100, 300, 75, 'Prąd zimny przy W brzegu', 'Zachodnie wybrzeża: zimne prądy (Kanaryjski, Kalifornijski)'),
                 (200, 141, 120, 125, 'Prądy równikowe', 'Pasaty pchają wodę ze wschodu na zachód'),
                 (250, 250, 200, 280, 'Wir półkuli S', 'Krąży przeciwnie do ruchu wskazówek zegara'),
                 (250, 50, 260, 25, 'Wir półkuli N', 'Krąży zgodnie z ruchem wskazówek zegara')],
      opis='Model krążenia wód powierzchniowych w oceanie między dwoma kontynentami — rysunek autorski IndexLab.',
      uwaga='Wiry oceaniczne napędzają pasaty i wiatry zachodnie, a siła Coriolisa skręca ruch wody. Efekt: zachodnie wybrzeża kontynentów w strefie zwrotnikowej są chłodne i suche (pustynie nadbrzeżne), wschodnie — ciepłe i wilgotne.'),
]

# ---------- 4. Gospodarka liniowa i o obiegu zamkniętym ----------
_g = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
for i, t in enumerate(('surowce', 'produkcja', 'użycie', 'odpady')):
    x = 20 + i * 95
    _g += f'<rect class="gs2 ol" x="{x}" y="30" width="80" height="30" rx="6"/><text class="tb" x="{x + 40}" y="50" text-anchor="middle">{t}</text>'
    if i < 3:
        _g += strz(x + 82, 45, x + 93, 45, 's')
cx, cy, r = 200, 190, 75
for i, t in enumerate(('projekt', 'produkcja', 'użycie', 'naprawa', 'recykling')):
    a = math.radians(-90 + i * 72)
    x, y = cx + r * math.cos(a), cy + r * math.sin(a)
    _g += f'<rect class="gt ol" x="{x - 38:.0f}" y="{y - 13:.0f}" width="76" height="26" rx="6"/><text class="tb" x="{x:.0f}" y="{y + 5:.0f}" text-anchor="middle">{t}</text>'
    a2 = math.radians(-90 + i * 72 + 36)
    _g += f'<circle class="hotf" cx="{cx + r * math.cos(a2):.0f}" cy="{cy + r * math.sin(a2):.0f}" r="4"/>'
_g += f'<circle class="dash" cx="{cx}" cy="{cy}" r="{r}" style="fill:none"/>'
_g += '<text class="ts" x="200" y="22" text-anchor="middle">gospodarka liniowa</text><text class="ts" x="200" y="296" text-anchor="middle">gospodarka o obiegu zamkniętym</text>'
S['g-srodowisko'] = [
 dict(typ='rysunek', tytul='Gospodarka liniowa a gospodarka o obiegu zamkniętym', svg=_g,
      znaczniki=[(345, 45, 330, 85, 'Odpady na końcu', 'Model „weź–wyprodukuj–wyrzuć” — rosnące składowiska'),
                 (238, 115, 300, 125, 'Projekt', 'Produkt projektuje się tak, by dało się go naprawić i odzyskać'),
                 (153, 251, 70, 285, 'Naprawa', 'Wydłużenie życia produktu zamiast kupna nowego'),
                 (128, 167, 60, 140, 'Recykling', 'Odzysk surowców wtórnych — zamyka obieg'),
                 (200, 190, 230, 215, 'Mniej surowców pierwotnych', 'Obieg zmniejsza wydobycie i ilość odpadów')],
      opis='Porównanie dwóch modeli gospodarki — rysunek autorski IndexLab.',
      uwaga='Gospodarka o obiegu zamkniętym (cyrkularna) to cel polityki UE. Przykłady: kaucja za butelki, prawo do naprawy, recykling elektroodpadów (odzysk metali z telefonów).'),
]

# ---------- 5. Pacyficzny Pierścień Ognia (schemat) ----------
_r = '<rect class="gw" x="0" y="0" width="400" height="300"/>'
_r += '<path class="gl ol" d="M0 0 H120 C110 60 90 120 70 160 C60 200 80 250 60 300 H0 Z"/>'      # Azja–Australia (W)
_r += '<path class="gl ol" d="M400 0 H300 C310 60 330 110 320 150 C310 200 330 250 340 300 H400 Z"/>'  # Ameryki (E)
_r += '<path class="gl ol" d="M120 0 C160 10 240 10 300 0 Z"/>'
_r += '<path class="hot" fill="none" d="M100 270 C110 200 100 120 130 40 C180 20 250 20 290 40 C315 110 310 200 325 270" style="stroke-width:3;stroke-dasharray:6 4"/>'
for x, y in ((112, 230), (108, 160), (122, 90), (170, 32), (240, 30), (295, 70), (312, 140), (318, 210)):
    _r += f'<path class="gm ol" d="M{x - 6} {y + 5} L{x} {y - 6} L{x + 6} {y + 5} Z"/>'
_r += '<text class="tb" x="210" y="160" text-anchor="middle">Ocean Spokojny</text>'
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Pacyficzny Pierścień Ognia (schemat)', svg=_r,
      znaczniki=[(122, 90, 180, 90, 'Japonia i Kuryle', 'Subdukcja płyty pacyficznej — łuki wysp'),
                 (240, 30, 260, 70, 'Aleuty i Alaska', 'Rowy oceaniczne i wulkany na północy Pacyfiku'),
                 (312, 140, 250, 130, 'Kordyliery i Andy', 'Subdukcja pod kontynenty amerykańskie'),
                 (108, 160, 160, 200, 'Filipiny i Indonezja', 'Liczne wulkany i silne trzęsienia ziemi'),
                 (318, 210, 260, 240, 'Chile', 'Najsilniejsze zmierzone trzęsienie (1960, M 9,5)')],
      opis='Uproszczony schemat strefy wulkanów i trzęsień ziemi wokół Pacyfiku — rysunek autorski IndexLab (bez skali i odwzorowania).',
      uwaga='Ok. 75% czynnych wulkanów i ok. 90% trzęsień ziemi występuje wokół Pacyfiku, gdzie płyty oceaniczne wsuwają się pod inne płyty (subdukcja). Tu powstają też tsunami.'),
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
