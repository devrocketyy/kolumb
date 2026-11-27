# Schematy geografii — porcja 28 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math

S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - g * math.cos(a - 0.4), y2 - g * math.sin(a - 0.4))
    p2 = (x2 - g * math.cos(a + 0.4), y2 - g * math.sin(a + 0.4))
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f} L{x2:.1f} {y2:.1f} L{p2[0]:.1f} {p2[1]:.1f}"/>')


# ---------- 1. Bałtyk — przekrój z halokliną ----------
_b = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_b += '<path class="gw ol" d="M0 60 H400 V150 C330 200 300 230 250 240 C200 250 150 200 100 180 C60 170 30 150 0 140 Z"/>'
_b += '<path class="gw2" d="M0 128 C60 150 100 168 140 190 C180 215 230 238 260 236 C300 220 340 190 400 152 V150 C380 140 300 135 260 140 C200 142 120 125 0 115 Z"/>'
_b += '<path class="dash" d="M0 118 C120 128 200 142 260 140 C300 136 380 140 400 150"/>'
_b += '<path class="gs ol" d="M0 140 C30 150 60 170 100 180 C150 200 200 250 250 240 C300 230 330 200 400 150 V300 H0 Z"/>'
_b += strz(20, 135, 120, 170, 'hot') + strz(300, 80, 60, 80, 'cold')
_b += '<text class="ts" x="8" y="52">Cieśniny Duńskie</text><text class="ts" x="300" y="52">Głębia Gotlandzka</text>'
S['g-oceany'] = [
 dict(typ='rysunek', tytul='Bałtyk w przekroju — haloklina i wlewy', svg=_b,
      znaczniki=[(200, 90, 230, 105, 'Wody powierzchniowe', 'Wysłodzone (ok. 7‰) — dopływ rzek, mały ubytek przez parowanie'),
                 (230, 140, 160, 115, 'Haloklina', 'Ok. 60–80 m — skok zasolenia, utrudnia mieszanie wód'),
                 (250, 215, 320, 260, 'Wody przydenne', 'Słone, często beztlenowe (siarkowodór) — martwe strefy'),
                 (70, 155, 40, 210, 'Wlew słonych wód', 'Z Morza Północnego przy silnych wiatrach zachodnich — dotlenia głębie'),
                 (180, 80, 150, 22, 'Odpływ wód wysłodzonych', 'Powierzchnią przez cieśniny do Morza Północnego')],
      opis='Uproszczony przekrój Bałtyku od Cieśnin Duńskich do Głębi Gotlandzkiej (głębokości przesadzone) — rysunek autorski IndexLab.',
      uwaga='Bałtyk jest morzem śródlądowym o słabej wymianie wód. Duże wlewy zdarzają się rzadko (co kilka–kilkanaście lat), dlatego w głębiach rozwijają się strefy beztlenowe, nasilane eutrofizacją.'),
]

# ---------- 2. Piramida Polski 2050 (prognoza) ----------
_p = '<rect class="gn" x="0" y="0" width="400" height="300"/>'
M = [8, 9, 9, 10, 10, 11, 12, 12, 13, 13, 13, 13, 16, 15, 12, 9, 6, 3]
K = [8, 9, 9, 9, 10, 10, 11, 12, 12, 13, 13, 13, 16, 16, 14, 12, 10, 8]
for i, (m, k) in enumerate(zip(M, K)):
    y = 260 - i * 12
    _p += f'<rect class="gw2 ol" x="{200 - m * 6}" y="{y - 11}" width="{m * 6}" height="11"/>'
    _p += f'<rect class="hotf ol" x="200" y="{y - 11}" width="{k * 6}" height="11"/>'
for i, t in ((0, '0'), (5, '25'), (10, '50'), (15, '75'), (17, '85+')):
    _p += f'<text class="ts" x="8" y="{258 - i * 12}">{t}</text>'
_p += '<text class="tb" x="60" y="285" text-anchor="middle">mężczyźni</text><text class="tb" x="395" y="285" text-anchor="end">kobiety</text>'
S['g-pl-ludnosc'] = [
 dict(typ='rysunek', tytul='Piramida wieku Polski — prognoza na ok. 2050 r.', svg=_p,
      znaczniki=[(155, 254, 210, 285, 'Wąska podstawa', 'Mało urodzeń — dzietność ok. 1,2–1,4'),
                 (290, 106, 300, 106, 'Wyż 60–70 lat', 'Duże roczniki wchodzą w wiek poprodukcyjny'),
                 (255, 50, 300, 30, 'Przewaga kobiet w starszym wieku', 'Kobiety żyją dłużej (nadumieralność mężczyzn)'),
                 (130, 182, 100, 182, 'Kształt urny', 'Społeczeństwo bardzo stare — regres demograficzny')],
      opis='Schematyczna piramida oparta na kierunku prognoz demograficznych dla Polski (wartości przybliżone, nie dane GUS) — rysunek autorski IndexLab.',
      uwaga='Według prognoz w 2050 r. ok. 1/3 mieszkańców Polski będzie miała 65+ lat, a liczba ludności spadnie do ok. 33–34 mln. Rośnie współczynnik obciążenia demograficznego.'),
]

# ---------- 3. Cyrkulacja Walkera ----------
_w = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_w += '<path class="gw ol" d="M60 200 H340 V300 H60 Z"/>'
_w += '<path class="gl ol" d="M0 190 H60 V300 H0 Z"/><path class="gl ol" d="M340 190 H400 V300 H340 Z"/>'
_w += '<path class="hotf" d="M250 200 H340 V225 H250 Z" style="opacity:.7"/><path class="coldf" d="M60 200 H150 V225 H60 Z" style="opacity:.7"/>'
_w += '<path class="gk ol" d="M330 120 C335 95 365 95 370 120 C390 120 390 145 370 145 H330 C310 145 310 120 330 120 Z"/>'
for x in (340, 352, 364):
    _w += f'<path class="cold" d="M{x} 150 l-5 18"/>'
_w += strz(310, 185, 310, 70, 'hot') + strz(300, 55, 100, 55, 's') + strz(90, 70, 90, 185, 'cold') + strz(110, 195, 290, 195, 's')
_w += '<text class="ts" x="8" y="182">Ameryka Pd.</text><text class="ts" x="340" y="182">Indonezja</text>'
S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Cyrkulacja Walkera nad Pacyfikiem (warunki normalne)', svg=_w,
      znaczniki=[(310, 120, 255, 95, 'Wznoszenie powietrza', 'Nad ciepłymi wodami zach. Pacyfiku — niż, chmury, ulewy'),
                 (90, 130, 130, 155, 'Osiadanie powietrza', 'Nad chłodnymi wodami u wybrzeży Peru — wyż, susza'),
                 (200, 195, 230, 240, 'Pasaty przy powierzchni', 'Wieją ze wschodu na zachód i spychają ciepłą wodę'),
                 (100, 212, 70, 280, 'Upwelling', 'Wypływ zimnych, żyznych wód — bogate łowiska'),
                 (200, 55, 210, 30, 'Powrót górą', 'Przepływ w górnej troposferze ku wschodowi')],
      opis='Komórka cyrkulacji Walkera w pasie równikowym Pacyfiku — rysunek autorski IndexLab.',
      uwaga='Podczas El Niño pasaty słabną, komórka Walkera osłabia się lub odwraca: ciepła woda przesuwa się ku Ameryce — ulewy w Peru, susze w Australii i Indonezji. La Niña wzmacnia układ normalny.'),
]

# ---------- 4. Kaptaż rzeczny ----------
_k = '<rect class="gt" x="0" y="0" width="400" height="300"/>'
_k += '<path class="gl2 ol" d="M190 0 C200 60 180 120 200 150 C215 175 205 220 210 300 H260 C255 220 265 175 250 150 C240 120 250 60 240 0 Z" style="opacity:.7"/>'
_k += '<path class="cold" d="M40 40 C100 70 160 110 215 150" style="stroke-width:4"/>'
_k += '<path class="cold" d="M215 150 C230 200 225 250 235 300" style="stroke-width:5"/>'
_k += '<path class="cold" d="M215 150 C260 170 320 200 390 240" style="stroke-width:1.5"/>'
_k += '<path class="dash" d="M260 168 C300 190 350 215 390 236"/>'
_k += '<path class="cold" d="M225 0 C228 40 220 100 215 150" style="stroke-width:3"/>'
_k += strz(228, 40, 220, 100, 'hot')
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Kaptaż rzeczny (przechwycenie rzeki)', svg=_k,
      znaczniki=[(225, 60, 290, 55, 'Erozja wsteczna', 'Rzeka o większym spadku cofa źródła i wcina się w dział wód'),
                 (215, 150, 150, 160, 'Kolano kaptażowe', 'Miejsce przechwycenia — ostre załamanie biegu rzeki'),
                 (60, 51, 30, 20, 'Rzeka przechwycona', 'Jej górny bieg płynie teraz do rzeki kaptującej'),
                 (360, 224, 330, 285, 'Dolina martwa', 'Rzeka pozbawiona źródeł — dolina zbyt szeroka jak na mały ciek (dolina martwa)')],
      opis='Schemat kaptażu — rzeka erodująca wstecz przechwytuje górny bieg sąsiedniej rzeki — rysunek autorski IndexLab.',
      uwaga='Kaptaże zmieniają przebieg działów wodnych. W Polsce przykłady opisywano m.in. w Sudetach i Karpatach; dawne pradoliny też były wykorzystywane przez rzeki zmieniające bieg.'),
]

# ---------- 5. Polder ----------
_d = '<rect class="gk" x="0" y="0" width="400" height="300"/>'
_d += '<path class="gw ol" d="M0 150 H120 V300 H0 Z"/>'
_d += '<path class="gs ol" d="M110 300 V150 L140 120 L170 120 L200 190 H400 V300 Z"/>'
_d += '<path class="gl ol" d="M200 190 H400 V200 H200 Z"/>'
_d += '<path class="gw2 ol" d="M300 200 H320 V215 H300 Z"/>'
_d += '<path class="gm ol" d="M360 150 H380 V190 H360 Z"/><path class="s" d="M370 150 V130 M358 130 L382 130"/>'
_d += strz(320, 208, 340, 175, 'cold')
_d += '<path class="dash" d="M0 150 H120"/><path class="dash" d="M0 230 H400"/><text class="ts" x="215" y="245">poziom morza (0 m)</text>'
S['g-pl-wody'] = [
 dict(typ='rysunek', tytul='Polder — teren poniżej poziomu morza', svg=_d,
      znaczniki=[(150, 125, 160, 70, 'Wał przeciwpowodziowy', 'Chroni polder przed zalaniem przez morze lub rzekę'),
                 (300, 195, 250, 165, 'Polder', 'Obszar osuszony, często poniżej poziomu morza (Żuławy, Holandia)'),
                 (310, 208, 290, 265, 'Rów melioracyjny', 'Zbiera nadmiar wody z pól'),
                 (370, 170, 330, 120, 'Pompownia', 'Przepompowuje wodę ponad wałem — bez niej polder by się zalał')],
      opis='Uproszczony przekrój przez polder z wałem i pompownią (proporcje przesadzone) — rysunek autorski IndexLab.',
      uwaga='Najniższy punkt Polski: Raczki Elbląskie na Żuławach Wiślanych (ok. 2,2 m p.p.m.). Żuławy wymagają stałej pracy pompowni i utrzymania wałów — zagrożenie przy powodziach i sztormach (cofka).'),
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
