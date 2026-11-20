# Schematy biologii — porcja 1: komórka i jej elementy (rysunki autorskie IndexLab).
# Rysunki w SVG (viewBox 400×300). Klasy: s — kontur, s2 — cienki kontur, f — wypełnienie jasne,
# f2 — wypełnienie ciemniejsze, d — pełne, dash — przerywana, t — podpis pomocniczy.
# Znacznik: (x, y elementu, x, y numeru, nazwa, krótki opis funkcji).
import math

S = {}


def kropki(pts, r=2):
    return ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="{r}"/>' for x, y in pts)


def szorstkie_er(x0, y0, n=3, dx=12, h=80):
    """Siateczka śródplazmatyczna szorstka: równoległe łuki z rybosomami."""
    out = ''
    for i in range(n):
        x = x0 - i * dx
        out += f'<path class="s" d="M{x} {y0} q-14 {h / 2} 0 {h}"/>'
        for k in range(1, 7):
            t = k / 7
            # punkt na krzywej Béziera kwadratowej
            px = (1 - t) ** 2 * x + 2 * (1 - t) * t * (x - 14) + t ** 2 * x
            py = y0 + h * t
            out += f'<circle class="d" cx="{px - 3:.1f}" cy="{py:.1f}" r="1.8"/>'
    return out


def golgi(x, y, n=4, w=46):
    out = ''
    for i in range(n):
        out += f'<path class="s" d="M{x - w / 2 + i * 3} {y + i * 7} q{w / 2 - i * 3} -14 {w - i * 6} 0"/>'
    out += f'<circle class="s" cx="{x + w / 2 + 6}" cy="{y + 2}" r="4"/><circle class="s" cx="{x + w / 2 + 2}" cy="{y + 20}" r="3.5"/>'
    return out


def mito(cx, cy, rx=30, ry=14, rot=0):
    zig = ' '.join(f'l6 {(-1) ** k * 16}' for k in range(int((2 * rx - 16) / 6)))
    return (f'<g transform="rotate({rot} {cx} {cy})"><ellipse class="f" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>'
            f'<path class="s2" d="M{cx - rx + 10} {cy - 8} {zig}"/></g>')


def chloro(cx, cy, rx=26, ry=12, rot=0):
    stosy = ''.join(f'<rect class="f2" x="{cx - rx + 8 + k * 12}" y="{cy - 5}" width="7" height="10" rx="1.5"/>' for k in range(int((2 * rx - 14) / 12)))
    return (f'<g transform="rotate({rot} {cx} {cy})"><ellipse class="f" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"/>'
            f'<line class="s2" x1="{cx - rx + 6}" y1="{cy}" x2="{cx + rx - 6}" y2="{cy}"/>{stosy}</g>')


# ---------- komórka zwierzęca ----------
_zw = (
    '<ellipse class="f" cx="200" cy="150" rx="168" ry="122"/>'
    '<circle class="f2" cx="180" cy="145" r="46"/>'
    '<circle class="d" cx="190" cy="140" r="13"/>'
    + ''.join(f'<rect class="d" x="{180 + 46 * math.cos(a) - 2:.1f}" y="{145 + 46 * math.sin(a) - 2:.1f}" width="4" height="4"/>' for a in (0.5, 1.6, 2.7, 3.8, 4.9, 5.9))
    + szorstkie_er(112, 100, 3)
    + mito(300, 95) + mito(255, 232, rot=-20)
    + golgi(300, 165)
    + '<circle class="f2" cx="100" cy="220" r="11"/><circle class="f2" cx="140" cy="240" r="8"/>'
    + '<rect class="s" x="210" y="205" width="7" height="18" rx="2"/><rect class="s" x="221" y="210" width="18" height="7" rx="2"/>'
    + kropki([(230, 70), (240, 80), (255, 70), (150, 200), (165, 215), (330, 230), (320, 245)])
)
_zw_zn = [
    (41, 112, 18, 40, 'Błona komórkowa', 'oddziela komórkę od otoczenia, wybiórczo przepuszczalna'),
    (180, 175, 140, 286, 'Jądro komórkowe', 'zawiera DNA, steruje życiem komórki'),
    (190, 140, 190, 18, 'Jąderko', 'synteza rRNA i podjednostek rybosomów'),
    (102, 120, 30, 120, 'Siateczka śródplazmatyczna szorstka', 'synteza białek na rybosomach i ich transport'),
    (300, 95, 360, 40, 'Mitochondrium', 'oddychanie komórkowe, produkcja ATP'),
    (310, 175, 385, 175, 'Aparat Golgiego', 'modyfikacja, sortowanie i pakowanie białek'),
    (100, 220, 30, 235, 'Lizosom', 'trawienie wewnątrzkomórkowe'),
    (222, 214, 250, 286, 'Centriole (centrosom)', 'organizacja wrzeciona podziałowego'),
    (240, 80, 270, 18, 'Rybosomy', 'synteza białek'),
]
_ro = (
    '<rect class="f2" x="20" y="25" width="360" height="250" rx="12"/>'
    '<rect class="f" x="28" y="33" width="344" height="234" rx="8"/>'
    '<rect class="s2" x="120" y="70" width="190" height="160" rx="30" style="fill:var(--surface)"/>'
    '<circle class="f2" cx="75" cy="200" r="30"/><circle class="d" cx="80" cy="196" r="9"/>'
    + chloro(70, 80) + chloro(345, 110, rot=80) + chloro(250, 250) + chloro(160, 52)
    + mito(340, 225, rx=22, ry=10, rot=70)
    + ''.join(f'<line class="s" x1="{x}" y1="22" x2="{x}" y2="36"/>' for x in (230, 270))
    + golgi(68, 128, n=3, w=36)
    + kropki([(110, 250), (120, 258), (300, 50), (315, 60)])
)
_ro_zn = [
    (20, 160, 12, 140, 'Ściana komórkowa', 'celulozowa, nadaje kształt i chroni przed pęknięciem'),
    (29, 240, 12, 200, 'Błona komórkowa', 'przylega do ściany, wybiórczo przepuszczalna'),
    (215, 150, 215, 150, 'Wakuola', 'magazyn wody i substancji, utrzymuje turgor'),
    (75, 200, 90, 288, 'Jądro komórkowe', 'zawiera DNA, steruje życiem komórki'),
    (70, 80, 20, 12, 'Chloroplast', 'fotosynteza'),
    (340, 225, 385, 282, 'Mitochondrium', 'oddychanie komórkowe, produkcja ATP'),
    (230, 29, 200, 6, 'Plazmodesmy', 'połączenia cytoplazmy sąsiednich komórek'),
    (68, 135, 160, 288, 'Aparat Golgiego', 'pakowanie substancji, m.in. do budowy ściany'),
]
# wakuola: numer w środku jest czytelny — przesuwamy go lekko, by linia była widoczna
_ro_zn[2] = (200, 160, 250, 150, 'Wakuola', 'magazyn wody i substancji, utrzymuje turgor')

S['b-typy-komorek'] = [
    dict(typ='rysunek', tytul='Komórka zwierzęca', svg=_zw, znaczniki=_zw_zn,
         opis='Schemat typowej komórki zwierzęcej widzianej w mikroskopie elektronowym.',
         uwaga='Komórka zwierzęca nie ma ściany komórkowej, chloroplastów ani dużej wakuoli, ma natomiast centriole. Tych różnic dotyczy wiele zadań typu „porównaj” i „rozpoznaj”.'),
    dict(typ='rysunek', tytul='Komórka roślinna', viewBox='0 -8 400 308', svg=_ro, znaczniki=_ro_zn,
         opis='Schemat komórki miękiszu asymilacyjnego liścia.',
         uwaga='Duża wakuola spycha cytoplazmę i jądro pod ścianę. Plazmodesmy łączą protoplasty sąsiednich komórek — to droga transportu symplastycznego.'),
    dict(typ='rysunek', tytul='Komórka bakteryjna', viewBox='0 0 400 260',
         svg=('<ellipse class="dash" cx="200" cy="130" rx="150" ry="78"/>'
              '<ellipse class="f2" cx="200" cy="130" rx="138" ry="66"/>'
              '<ellipse class="f" cx="200" cy="130" rx="130" ry="58"/>'
              '<path class="s" d="M150 130 c10 -30 40 -20 30 0 s-30 30 0 25 s40 -30 20 -40 s-60 0 -40 30 s50 10 60 -10"/>'
              '<circle class="s" cx="290" cy="110" r="10"/><circle class="s" cx="120" cy="160" r="7"/>'
              + kropki([(240, 160), (255, 150), (265, 165), (130, 105), (145, 95), (230, 95)])
              + '<path class="s" d="M350 130 q12 -12 22 0 t22 0"/>'
              + ''.join(f'<line class="s2" x1="{200 + 138 * math.cos(a):.0f}" y1="{130 + 66 * math.sin(a):.0f}" x2="{200 + 152 * math.cos(a):.0f}" y2="{130 + 80 * math.sin(a):.0f}"/>' for a in (3.6, 4.0, 4.4, 5.0, 5.4, 1.9, 2.3, 1.2))),
         znaczniki=[
             (200, 52, 200, 14, 'Otoczka śluzowa', 'ochrona przed wysychaniem i fagocytozą'),
             (72, 150, 20, 200, 'Ściana komórkowa', 'z mureiny (peptydoglikanu)'),
             (72, 120, 20, 70, 'Błona komórkowa', 'tu zachodzi m.in. oddychanie u bakterii'),
             (180, 130, 120, 246, 'Nukleoid', 'koliste DNA, brak otoczki jądrowej'),
             (290, 110, 330, 30, 'Plazmid', 'małe koliste DNA, np. geny oporności'),
             (255, 150, 290, 246, 'Rybosomy 70S', 'synteza białek'),
             (375, 128, 380, 200, 'Rzęska (wić)', 'ruch'),
             (110, 72, 60, 22, 'Fimbrie (pile)', 'przyczepianie się, koniugacja'),
         ],
         opis='Schemat komórki prokariotycznej.',
         uwaga='Bakterie nie mają jądra ani organelli otoczonych błonami. Plazmidy są wykorzystywane w inżynierii genetycznej jako wektory.'),
]

# ---------- mitochondrium ----------
def _krysta(x, gora):
    yb = 84 * math.sqrt(max(0, 1 - ((x + 8 - 200) / 166) ** 2))
    y0 = 150 - yb + 1 if gora else 150 + yb - 1
    y1 = 122 if gora else 178
    k = 1 if gora else -1
    return f'<path class="f" d="M{x} {y0:.1f} L{x} {y1} q0 {8 * k} 8 {8 * k} q8 0 8 {-8 * k} L{x + 16} {y0:.1f}"/>'


_cr = ''.join(_krysta(x, k % 2 == 0) for k, x in enumerate(range(95, 300, 34)))
_mi = ('<ellipse class="f2" cx="200" cy="150" rx="180" ry="98"/>'
       '<ellipse class="f" cx="200" cy="150" rx="166" ry="84"/>' + _cr
       + '<circle class="s" cx="318" cy="150" r="12"/>' + kropki([(80, 150), (90, 165), (330, 190), (340, 182), (322, 182)]))
S['b-mitochondria'] = [
    dict(typ='rysunek', tytul='Mitochondrium', svg=_mi,
         znaczniki=[
             (200, 52, 200, 18, 'Błona zewnętrzna', 'gładka, przepuszczalna dla małych cząsteczek'),
             (34, 150, 12, 220, 'Błona wewnętrzna', 'łańcuch oddechowy i syntaza ATP'),
             (103, 115, 40, 40, 'Grzebień mitochondrialny', 'fałd błony wewnętrznej — większa powierzchnia'),
             (230, 150, 230, 286, 'Macierz (matriks)', 'cykl Krebsa, reakcja pomostowa'),
             (25, 150, 12, 120, 'Przestrzeń międzybłonowa', 'gromadzą się tu protony (H⁺)'),
             (318, 150, 385, 150, 'DNA mitochondrialne', 'koliste, dziedziczone po matce'),
             (330, 190, 370, 250, 'Rybosomy 70S', 'synteza części białek mitochondrium'),
         ],
         opis='Przekrój podłużny przez mitochondrium.',
         uwaga='Własne koliste DNA i rybosomy 70S to argumenty za endosymbiotycznym pochodzeniem mitochondriów. Pamiętaj: łańcuch oddechowy leży w błonie wewnętrznej, cykl Krebsa zachodzi w macierzy.'),
    dict(typ='rysunek', tytul='Chloroplast',
         svg=('<ellipse class="f2" cx="200" cy="150" rx="180" ry="96"/>'
              '<ellipse class="f" cx="200" cy="150" rx="168" ry="84"/>'
              + ''.join(f'<rect class="f2" x="{x}" y="{y + i * 9}" width="40" height="7" rx="3"/>' for x, y in ((80, 110), (170, 95), (260, 115), (150, 175)) for i in range(5))
              + '<path class="s2" d="M120 130 L170 120 M210 120 L260 135 M190 140 L170 185 M100 155 L150 190 M300 150 L330 175"/>'
              + '<ellipse class="d" cx="270" cy="200" rx="22" ry="11"/>'
              + '<circle class="s" cx="110" cy="200" r="11"/>' + kropki([(330, 120), (320, 130), (240, 90)])),
         znaczniki=[
             (200, 54, 200, 18, 'Błona zewnętrzna', ''),
             (60, 112, 18, 60, 'Błona wewnętrzna', ''),
             (190, 113, 190, 286, 'Granum', 'stos tylakoidów — faza zależna od światła'),
             (240, 128, 330, 30, 'Tylakoid stromy', 'łączy grana'),
             (230, 230, 120, 286, 'Stroma', 'cykl Calvina (faza niezależna od światła)'),
             (270, 200, 385, 220, 'Ziarno skrobi', 'materiał zapasowy'),
             (110, 200, 18, 240, 'DNA chloroplastowe', 'koliste'),
             (330, 120, 385, 100, 'Rybosomy 70S', ''),
         ],
         opis='Przekrój przez chloroplast.',
         uwaga='Zadania często pytają, gdzie zachodzą fazy fotosyntezy: faza zależna od światła — błony tylakoidów (grana), cykl Calvina — stroma.'),
]

# ---------- błona ----------
def _blona():
    out = ''
    for x in range(30, 380, 16):
        if 140 <= x <= 200 or 270 <= x <= 300:
            continue
        for y, kier in ((95, 1), (205, -1)):
            out += f'<circle class="f2" cx="{x}" cy="{y}" r="6"/>'
            out += f'<path class="s2" d="M{x - 2} {y + 6 * kier} l0 {38 * kier} M{x + 2} {y + 6 * kier} l0 {38 * kier}"/>'
    out += '<path class="f" d="M140 70 q30 -20 62 0 l0 160 q-30 20 -62 0 z"/>'                # białko integralne (przezbłonowe)
    out += '<path class="f" d="M268 82 l14 0 l0 136 l-14 0 z M290 82 l14 0 l0 136 l-14 0 z"/>'   # kanał
    out += '<ellipse class="f" cx="80" cy="222" rx="26" ry="12"/>'                                  # białko powierzchniowe
    out += '<path class="s" d="M170 60 l0 -20 l-12 -12 M170 40 l12 -12 M182 28 l8 -10"/>'           # łańcuch cukrowy
    out += ''.join(f'<circle class="s" cx="{x}" cy="{y}" r="4"/>' for x, y in ((158, 28), (182, 28), (190, 18), (170, 40)))
    out += '<rect class="d" x="225" y="110" width="6" height="26" rx="2"/>'                          # cholesterol
    out += '<text class="t" x="10" y="20">środowisko zewnętrzne</text><text class="t" x="10" y="292">cytoplazma</text>'
    return out


S['b-blony'] = [
    dict(typ='rysunek', tytul='Model płynnej mozaiki', svg=_blona(),
         znaczniki=[
             (110, 95, 60, 50, 'Hydrofilowa główka fosfolipidu', 'zwrócona do wody'),
             (112, 150, 30, 150, 'Hydrofobowe ogony kwasów tłuszczowych', 'wnętrze dwuwarstwy'),
             (171, 150, 240, 286, 'Białko integralne (przezbłonowe)', 'przechodzi przez całą błonę'),
             (80, 222, 120, 286, 'Białko powierzchniowe', 'związane z powierzchnią błony'),
             (286, 150, 360, 270, 'Białko kanałowe', 'transport jonów i wody'),
             (170, 40, 230, 30, 'Glikokaliks (łańcuch cukrowy)', 'rozpoznawanie komórek'),
             (228, 123, 270, 50, 'Cholesterol', 'reguluje płynność błony'),
         ],
         opis='Budowa błony komórkowej według modelu płynnej mozaiki (Singer i Nicolson).',
         uwaga='Glikokaliks znajduje się zawsze po stronie zewnętrznej — po tym rozpoznasz na schemacie, która strona błony to wnętrze komórki.'),
    dict(typ='proces', tytul='Endocytoza — przebieg',
         kroki=[('Rozpoznanie cząstki', 'np. przez receptory w błonie'), ('Wpuklenie błony komórkowej', 'błona otacza cząstkę'),
                ('Odcięcie pęcherzyka', 'powstaje pęcherzyk endocytarny (fagosom)'), ('Połączenie z lizosomem', 'enzymy hydrolityczne trafiają do pęcherzyka'),
                ('Trawienie zawartości', 'produkty przechodzą do cytoplazmy')],
         uwaga='Endocytoza i egzocytoza wymagają ATP — to transport czynny, choć nie przez białka nośnikowe.'),
    dict(typ='proces', tytul='Pompa sodowo-potasowa — cykl pracy',
         kroki=[('Przyłączenie 3 Na⁺ od strony cytoplazmy'), ('Hydroliza ATP i fosforylacja białka'),
                ('Zmiana konformacji — wyrzucenie 3 Na⁺ na zewnątrz'), ('Przyłączenie 2 K⁺ od zewnątrz'),
                ('Odłączenie fosforanu i powrót do pierwotnego kształtu'), ('Uwolnienie 2 K⁺ do cytoplazmy')],
         uwaga='Bilans: 3 Na⁺ na zewnątrz, 2 K⁺ do środka, 1 ATP — dlatego wnętrze komórki jest ujemne.'),
]

# ---------- jądro ----------
S['b-jadro'] = [
    dict(typ='rysunek', tytul='Jądro komórkowe',
         svg=('<circle class="f2" cx="200" cy="150" r="118"/><circle class="f" cx="200" cy="150" r="108"/>'
              + ''.join(f'<rect class="f" x="{200 + 113 * math.cos(a) - 4:.1f}" y="{150 + 113 * math.sin(a) - 4:.1f}" width="8" height="8"/>' for a in (0.3, 1.1, 1.9, 2.7, 3.5, 4.3, 5.1, 5.8))
              + '<circle class="d" cx="215" cy="140" r="26"/>'
              + '<path class="s2" d="M120 120 c20 -20 30 20 50 0 s20 -30 10 -40 M140 190 c20 10 40 -10 60 10 s30 10 40 -10 M250 210 c10 -20 30 0 20 -30"/>'
              + '<path class="s" d="M318 150 q30 -30 60 -10 M318 150 q30 30 60 10 M330 176 q25 10 45 30"/>'
              + kropki([(350, 128), (360, 133), (370, 140), (352, 172), (362, 176), (350, 194)])),
         znaczniki=[
             (82, 150, 20, 150, 'Otoczka jądrowa', 'podwójna błona'),
             (200 + 113 * math.cos(5.1), 150 + 113 * math.sin(5.1), 280, 18, 'Por jądrowy', 'transport mRNA i białek'),
             (215, 140, 260, 100, 'Jąderko', 'synteza rRNA, składanie podjednostek rybosomów'),
             (160, 195, 120, 286, 'Chromatyna', 'DNA z białkami histonowymi'),
             (150, 110, 70, 50, 'Kariolimfa (nukleoplazma)', ''),
             (355, 130, 380, 60, 'Siateczka śródplazmatyczna szorstka', 'łączy się z otoczką jądrową'),
         ],
         opis='Przekrój przez jądro komórkowe w interfazie.',
         uwaga='Zewnętrzna błona otoczki jądrowej przechodzi w siateczkę śródplazmatyczną szorstką — dlatego na jej powierzchni też są rybosomy.'),
    dict(typ='proces', tytul='Droga białka wydzielniczego',
         kroki=[('Transkrypcja w jądrze', 'powstaje mRNA'), ('Wyjście mRNA przez pory jądrowe'),
                ('Translacja na rybosomach siateczki szorstkiej', 'łańcuch trafia do wnętrza ER'), ('Pęcherzyk transportujący z ER'),
                ('Modyfikacja w aparacie Golgiego', 'np. dołączenie reszt cukrowych'), ('Pęcherzyk wydzielniczy'), ('Egzocytoza', 'uwolnienie białka na zewnątrz')],
         uwaga='Typowe zadanie: znakowany radioaktywnie aminokwas pojawia się kolejno w ER szorstkim, aparacie Golgiego, pęcherzykach i poza komórką.'),
]
