# Schematy biologii — porcja 8: rysunki — mikroorganizmy, genetyka molekularna, ekologia (wykresy).
import math

S = {}


def kropki(pts, r=2):
    return ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="{r}"/>' for x, y in pts)


def osie(x0=50, y0=260, x1=380, y1=30, ox='czas', oy='liczebność'):
    return (f'<path class="s" d="M{x0} {y1} L{x0} {y0} L{x1} {y0}"/>'
            f'<path class="s" d="M{x0 - 4} {y1 + 6} L{x0} {y1} L{x0 + 4} {y1 + 6} M{x1 - 6} {y0 - 4} L{x1} {y0} L{x1 - 6} {y0 + 4}"/>'
            f'<text class="t" x="{x1 - 40}" y="{y0 + 18}">{ox}</text><text class="t" x="{x0 + 6}" y="{y1 + 4}">{oy}</text>')


# ---------- bakteriofag ----------
def _hex(cx, cy, r, cls='f'):
    pts = ' '.join(f'{cx + r * math.cos(math.radians(a)):.1f},{cy + r * math.sin(math.radians(a)):.1f}' for a in range(-90, 270, 60))
    return f'<polygon class="{cls}" points="{pts}"/>'


_fag = (
    _hex(200, 70, 56)
    + '<path class="s2" d="M175 50 c20 -14 40 10 20 20 s-30 20 -5 26 s40 -10 30 -30 M180 90 c10 -6 30 6 40 -4"/>'
    + '<rect class="f2" x="190" y="124" width="20" height="10"/>'
    + '<rect class="f" x="186" y="134" width="28" height="92" rx="3"/>'
    + ''.join(f'<line class="s2" x1="186" y1="{y}" x2="214" y2="{y}"/>' for y in range(144, 226, 10))
    + '<rect class="f2" x="168" y="226" width="64" height="12" rx="3"/>'
    + '<path class="s" d="M172 236 L130 210 L110 285 M228 236 L270 210 L290 285 M180 238 L156 262 L150 292 M220 238 L244 262 L250 292"/>'
)

# ---------- wirus z osłonką (HIV) ----------
def _hiv():
    out = '<circle class="f" cx="200" cy="150" r="100"/><circle class="dash" cx="200" cy="150" r="88"/>'
    for k in range(12):
        a = math.radians(k * 30 + 10)
        x0, y0 = 200 + 100 * math.cos(a), 150 + 100 * math.sin(a)
        x1, y1 = 200 + 118 * math.cos(a), 150 + 118 * math.sin(a)
        out += f'<line class="s" x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}"/><circle class="f2" cx="{x1:.1f}" cy="{y1:.1f}" r="7"/>'
    out += '<path class="f2" d="M170 82 L230 82 L252 218 L148 218 Z"/>'
    out += '<path class="s" d="M180 100 c10 10 -10 20 0 30 s-10 20 0 30 s-10 20 0 30 M218 100 c10 10 -10 20 0 30 s-10 20 0 30 s-10 20 0 30"/>'
    out += kropki([(200, 120), (204, 180), (196, 150)], 5)
    return out


# ---------- pantofelek ----------
def _pantofelek():
    d = 'M40 150 Q40 80 140 70 Q250 60 330 90 Q370 110 365 150 Q370 200 320 215 Q240 238 130 228 Q40 220 40 150 Z'
    out = f'<path class="f" d="{d}"/>'
    for k in range(60):
        t = k / 60 * 2 * math.pi
        x, y = 202 + 168 * math.cos(t), 150 + 82 * math.sin(t)
        x2, y2 = 202 + 180 * math.cos(t), 150 + 92 * math.sin(t)
        out += f'<line class="s2" x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>'
    out += '<path class="f2" d="M150 120 Q200 100 240 130 Q250 160 215 170 Q185 160 160 168 Q135 150 150 120 Z"/>'
    out += '<circle class="d" cx="250" cy="160" r="6"/>'
    out += '<path class="s" d="M150 228 Q180 180 230 190 Q215 205 222 222"/>'
    out += ''.join(f'<circle class="s" cx="{x}" cy="{y}" r="11"/>' + kropki([(x - 3, y), (x + 3, y + 2)], 1.6) for x, y in ((120, 180), (290, 175), (300, 120)))
    for cx, cy in ((90, 120), (330, 140)):
        out += f'<circle class="f2" cx="{cx}" cy="{cy}" r="9"/>' + ''.join(f'<line class="s2" x1="{cx + 9 * math.cos(math.radians(a)):.1f}" y1="{cy + 9 * math.sin(math.radians(a)):.1f}" x2="{cx + 22 * math.cos(math.radians(a)):.1f}" y2="{cy + 22 * math.sin(math.radians(a)):.1f}"/>' for a in range(0, 360, 45))
    out += '<path class="s2" d="M80 200 l-14 6"/>'
    return out


# ---------- euglena ----------
_euglena = (
    '<path class="f" d="M60 150 Q90 100 200 98 Q320 100 360 150 Q320 200 200 202 Q90 200 60 150 Z"/>'
    '<path class="s" d="M70 140 Q50 120 30 130 Q10 140 14 120 Q18 100 4 92"/>'
    '<path class="s2" d="M64 146 Q78 138 92 146"/>'
    '<circle class="d" cx="92" cy="136" r="6"/>'
    '<circle class="s" cx="112" cy="160" r="9"/>'
    '<circle class="f2" cx="210" cy="150" r="22"/><circle class="d" cx="210" cy="150" r="5"/>'
    + ''.join(f'<ellipse class="f2" cx="{x}" cy="{y}" rx="16" ry="6" transform="rotate({r} {x} {y})"/>' for x, y in ((150, 125), (160, 175), (260, 120), (280, 175), (310, 145), (240, 185), (180, 112)) for r in (15,))
    + ''.join(f'<rect class="s" x="{x}" y="{y}" width="10" height="6" rx="2"/>' for x, y in ((130, 145), (250, 150), (290, 135), (190, 182)))
)

# ---------- odcinek DNA ----------
def _dna():
    pary = [('A', 'T'), ('G', 'C'), ('C', 'G'), ('T', 'A'), ('G', 'C')]
    out = ''
    for i, (l, p) in enumerate(pary):
        y = 50 + i * 50
        out += f'<polygon class="f" points="120,{y - 10} 132,{y - 2} 128,{y + 10} 112,{y + 10} 108,{y - 2}"/>'
        out += f'<polygon class="f" points="280,{y + 10} 268,{y + 2} 272,{y - 10} 288,{y - 10} 292,{y + 2}"/>'
        out += f'<rect class="f2" x="136" y="{y - 8}" width="58" height="16" rx="3"/><rect class="f2" x="206" y="{y - 8}" width="58" height="16" rx="3"/>'
        out += f'<text class="t" x="160" y="{y + 4}">{l}</text><text class="t" x="230" y="{y + 4}">{p}</text>'
        n = 3 if 'G' in (l, p) else 2
        out += ''.join(f'<line class="s" x1="195" y1="{y - 6 + k * (12 / (n - 1)):.1f}" x2="205" y2="{y - 6 + k * (12 / (n - 1)):.1f}" stroke-dasharray="2 2"/>' for k in range(n))
        if i < 4:
            out += f'<circle class="f2" cx="100" cy="{y + 25}" r="8"/><text class="t" x="96" y="{y + 29}">P</text>'
            out += f'<circle class="f2" cx="300" cy="{y + 25}" r="8"/><text class="t" x="296" y="{y + 29}">P</text>'
            out += f'<path class="s" d="M110 {y + 10} L104 {y + 18} M104 {y + 32} L112 {y + 40} M290 {y + 10} L296 {y + 18} M296 {y + 32} L288 {y + 40}"/>'
    out += '<rect class="dash" x="86" y="30" width="112" height="56" rx="6"/>'
    out += '<text class="t" x="96" y="22">5′</text><text class="t" x="96" y="290">3′</text><text class="t" x="290" y="22">3′</text><text class="t" x="290" y="290">5′</text>'
    return out


# ---------- tRNA ----------
def _trna():
    out = ''
    def stem(x1, y1, x2, y2, n):
        s = ''
        for k in range(n + 1):
            t = k / n
            ax, ay = x1[0] + (x2[0] - x1[0]) * t, x1[1] + (x2[1] - x1[1]) * t
            bx, by = y1[0] + (y2[0] - y1[0]) * t, y1[1] + (y2[1] - y1[1]) * t
            s += f'<line class="s2" x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}"/>'
        return s
    out += '<path class="s" d="M190 40 L190 110 L130 110 M210 22 L210 110 L270 110 M130 130 L190 130 L190 205 M270 130 L210 130 L210 205"/>'
    out += stem((190, 44), (210, 44), (190, 104), (210, 104), 6)
    out += stem((136, 110), (136, 130), (184, 110), (184, 130), 4)
    out += stem((216, 110), (216, 130), (264, 110), (264, 130), 4)
    out += stem((190, 140), (210, 140), (190, 200), (210, 200), 5)
    out += '<path class="s" d="M130 110 A28 28 0 1 0 130 130 M270 110 A28 28 0 1 1 270 130 M190 205 A32 32 0 1 0 210 205"/>'
    out += '<path class="s" d="M210 22 L222 10"/><text class="t" x="224" y="14">C C A — 3′</text><text class="t" x="168" y="50">5′</text>'
    out += ''.join(f'<rect class="d" x="{x}" y="262" width="8" height="12" rx="2"/>' for x in (186, 196, 206))
    return out


# ---------- chromosom ----------
def _chromatyda(cx, k):
    return (f'<path class="f" d="M{cx} 30 Q{cx - 12 * k} 30 {cx - 12 * k} 45 L{cx - 8 * k} 135 Q{cx - 5 * k} 146 {cx - 8 * k} 157 '
            f'L{cx - 13 * k} 266 Q{cx - 13 * k} 282 {cx} 282 Q{cx + 13 * k} 282 {cx + 13 * k} 266 L{cx + 8 * k} 157 Q{cx + 5 * k} 146 {cx + 8 * k} 135 '
            f'L{cx + 12 * k} 45 Q{cx + 12 * k} 30 {cx} 30 Z"/>')


_chrom = (
    _chromatyda(182, 1) + _chromatyda(218, 1)
    + '<ellipse class="f2" cx="200" cy="146" rx="20" ry="9"/>'
    + '<rect class="d" x="166" y="139" width="6" height="14" rx="1"/><rect class="d" x="228" y="139" width="6" height="14" rx="1"/>'
    + '<rect class="d" x="174" y="30" width="16" height="5" rx="2"/><rect class="d" x="210" y="30" width="16" height="5" rx="2"/>'
    + '<rect class="d" x="171" y="277" width="22" height="5" rx="2"/><rect class="d" x="207" y="277" width="22" height="5" rx="2"/>'
    + '<path class="s2" d="M250 34 l8 0 l0 100 l-8 0 M250 160 l8 0 l0 118 l-8 0"/>'
)

# ---------- widełki replikacyjne ----------
def _widelki():
    def top(x):
        return 140 - (x - 150) * 90 / 230
    def bot(x):
        return 160 + (x - 150) * 90 / 230
    out = '<line class="s" x1="20" y1="140" x2="150" y2="140"/><line class="s" x1="20" y1="160" x2="150" y2="160"/>'
    out += ''.join(f'<line class="s2" x1="{x}" y1="140" x2="{x}" y2="160"/>' for x in range(28, 150, 12))
    out += '<line class="s" x1="150" y1="140" x2="380" y2="50"/><line class="s" x1="150" y1="160" x2="380" y2="250"/>'
    out += f'<line x1="190" y1="{bot(190) - 12:.1f}" x2="380" y2="{bot(380) - 12:.1f}" stroke="currentColor" stroke-width="3"/>'
    for a, b in ((185, 235), (250, 300), (315, 365)):
        out += f'<line x1="{a}" y1="{top(a) + 12:.1f}" x2="{b}" y2="{top(b) + 12:.1f}" stroke="currentColor" stroke-width="3"/>'
        out += f'<line x1="{a}" y1="{top(a) + 12:.1f}" x2="{a + 10}" y2="{top(a + 10) + 12:.1f}" stroke="var(--text-2)" stroke-width="6"/>'
    out += '<path class="f2" d="M138 150 L166 132 L166 168 Z"/>'
    out += f'<ellipse class="f" cx="200" cy="{bot(200) - 12:.1f}" rx="14" ry="9"/>'
    out += kropki([(176, top(176) - 6), (186, top(186) - 6), (178, bot(178) + 6)], 3.5)
    out += '<text class="t" x="20" y="128">kierunek ruchu widełek ←</text>'
    return out


# ---------- wykresy ----------
_wzrost = (
    osie()
    + '<path class="s" d="M60 250 C140 246 190 210 215 140 S240 45 246 30"/>'
    + '<path d="M60 250 C150 247 200 200 235 140 S300 82 370 80" fill="none" stroke="currentColor" stroke-width="3"/>'
    + '<line class="dash" x1="50" y1="78" x2="380" y2="78"/><text class="t" x="34" y="82">K</text>'
)
_przezywanie = (
    osie(ox='wiek', oy='liczba żyjących (skala log.)')
    + '<path d="M50 40 L250 46 Q300 52 330 250" fill="none" stroke="currentColor" stroke-width="2.4"/>'
    + '<path d="M50 40 L330 250" fill="none" stroke="currentColor" stroke-width="2.4" stroke-dasharray="7 4"/>'
    + '<path d="M50 40 Q66 230 120 244 L330 252" fill="none" stroke="currentColor" stroke-width="2.4" stroke-dasharray="2 4"/>'
)


def _dzwon(x0, mu, sig, h, w=110, y0=250, klasa='s', dash=False):
    pts = []
    for k in range(41):
        x = x0 + w * k / 40
        y = y0 - h * math.exp(-((x - mu) ** 2) / (2 * sig ** 2))
        pts.append(f'{x:.1f},{y:.1f}')
    st = ' stroke-dasharray="5 4"' if dash else ''
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="currentColor" stroke-width="{1.4 if dash else 2.4}"{st}/>'


def _dobor():
    out = ''
    for i, x0 in enumerate((10, 145, 280)):
        out += f'<path class="s" d="M{x0} 250 L{x0 + 110} 250"/>' + _dzwon(x0, x0 + 55, 18, 120, dash=True)
    out += _dzwon(10, 65, 9, 190)
    out += _dzwon(145, 225, 16, 120)
    out += _dzwon(280, 298, 10, 90) + _dzwon(280, 372, 10, 90)
    out += '<text class="t" x="20" y="275">A</text><text class="t" x="155" y="275">B</text><text class="t" x="290" y="275">C</text>'
    out += '<text class="t" x="10" y="292">oś X: wartość cechy, oś Y: liczba osobników</text>'
    return out


_piramida = (
    '<rect class="f2" x="60" y="220" width="280" height="40"/>'
    '<rect class="f" x="110" y="175" width="180" height="40"/>'
    '<rect class="f" x="150" y="130" width="100" height="40"/>'
    '<rect class="f" x="180" y="85" width="40" height="40"/>'
    '<path class="s2" d="M350 240 Q372 200 350 160 M346 168 L350 160 L356 166"/><text class="t" x="356" y="200">~10%</text>'
)

S['b-wirusy'] = [
    dict(typ='rysunek', tytul='Budowa bakteriofaga', svg=_fag,
         znaczniki=[
             (230, 50, 300, 30, 'Główka (kapsyd)', 'białkowa osłona materiału genetycznego'),
             (195, 70, 100, 40, 'DNA', 'materiał genetyczny wstrzykiwany do bakterii'),
             (200, 180, 300, 160, 'Kurczliwa pochewka ogonka', 'wprowadza DNA do komórki'),
             (200, 232, 300, 220, 'Płytka podstawowa', ''),
             (120, 248, 60, 200, 'Włókienka ogonka', 'przyczepianie do receptorów bakterii'),
         ],
         opis='Schemat bakteriofaga typu T4.',
         uwaga='Do wnętrza bakterii wnika tylko DNA faga — kapsyd zostaje na zewnątrz (doświadczenie Hersheya i Chase).'),
    dict(typ='rysunek', tytul='Budowa wirusa z osłonką (HIV)', svg=_hiv(),
         znaczniki=[
             (110, 194, 40, 250, 'Osłonka lipidowa', 'pochodzi z błony komórki gospodarza'),
             (200 + 118 * math.cos(math.radians(40)), 150 + 118 * math.sin(math.radians(40)), 370, 270, 'Glikoproteiny powierzchniowe', 'wiążą się z receptorem CD4 limfocytu'),
             (240, 200, 340, 150, 'Kapsyd', ''),
             (180, 130, 60, 80, 'RNA wirusa', 'dwie kopie jednoniciowego RNA'),
             (204, 180, 200, 285, 'Odwrotna transkryptaza', 'przepisuje RNA na DNA'),
             (200, 62, 200, 14, 'Macierz białkowa', ''),
         ],
         opis='Schemat retrowirusa HIV.',
         uwaga='Osłonka lipidowa czyni wirusa wrażliwym na detergenty i alkohol — dlatego mydło skutecznie niszczy wirusy z osłonką.'),
]

S['b-protisty'] = [
    dict(typ='rysunek', tytul='Budowa pantofelka', svg=_pantofelek(),
         znaczniki=[
             (360, 110, 385, 50, 'Rzęski', 'ruch i napędzanie pokarmu'),
             (200, 125, 200, 20, 'Makronukleus', 'steruje metabolizmem'),
             (250, 160, 300, 270, 'Mikronukleus', 'udział w procesie płciowym (koniugacji)'),
             (205, 195, 150, 280, 'Cytostom (gardziel)', 'pobieranie pokarmu'),
             (290, 175, 385, 220, 'Wodniczka pokarmowa', 'trawienie'),
             (90, 120, 30, 60, 'Wodniczka tętniąca', 'usuwanie nadmiaru wody'),
             (72, 203, 20, 260, 'Cytopyge', 'usuwanie niestrawionych resztek'),
         ],
         opis='Pantofelek — orzęsek słodkowodny.',
         uwaga='Wodniczki tętniące występują u protistów słodkowodnych: woda stale napływa do komórki przez osmozę i musi być usuwana.'),
    dict(typ='rysunek', tytul='Budowa klejnotki (eugleny)', svg=_euglena,
         znaczniki=[
             (14, 120, 30, 40, 'Wić', 'ruch'),
             (92, 136, 110, 50, 'Plamka oczna (stigma)', 'odbiór kierunku światła'),
             (260, 120, 300, 40, 'Chloroplast', 'fotosynteza — odżywianie autotroficzne'),
             (210, 150, 210, 270, 'Jądro komórkowe', ''),
             (112, 160, 60, 250, 'Wodniczka tętniąca', 'osmoregulacja'),
             (255, 153, 340, 260, 'Ziarna paramylonu', 'materiał zapasowy'),
             (340, 140, 385, 100, 'Pellikula', 'elastyczna osłonka białkowa'),
         ],
         opis='Klejnotka (euglena) — protist zdolny do auto- i heterotrofii.',
         uwaga='W ciemności euglena traci chlorofil i odżywia się heterotroficznie — to miksotrof.'),
]

S['b-kwasy'] = [
    dict(typ='rysunek', tytul='Fragment cząsteczki DNA', svg=_dna(),
         znaczniki=[
             (100, 75, 30, 100, 'Reszta fosforanowa', ''),
             (120, 150, 30, 160, 'Deoksyryboza', 'cukier pięciowęglowy'),
             (165, 50, 160, 14, 'Zasada azotowa', ''),
             (200, 100, 340, 100, 'Wiązania wodorowe (para G–C: 3)', ''),
             (200, 200, 340, 200, 'Wiązania wodorowe (para A–T: 2)', ''),
             (90, 34, 30, 50, 'Nukleotyd', 'cukier + fosforan + zasada'),
         ],
         opis='Dwie antyrównoległe nici połączone parami komplementarnych zasad.',
         uwaga='Zawartość par G–C podnosi temperaturę topnienia DNA, bo para G–C ma trzy wiązania wodorowe, a A–T — dwa.'),
]

S['b-translacja'] = [
    dict(typ='rysunek', tytul='Budowa tRNA', svg=_trna(),
         znaczniki=[
             (222, 10, 320, 30, 'Miejsce przyłączenia aminokwasu (koniec 3′)', ''),
             (200, 70, 300, 70, 'Ramię akceptorowe', ''),
             (200, 268, 300, 270, 'Antykodon', 'komplementarny do kodonu w mRNA'),
             (102, 120, 40, 60, 'Pętla D', ''),
             (298, 120, 360, 170, 'Pętla T', ''),
             (200, 160, 100, 200, 'Wiązania wodorowe między zasadami', 'utrzymują kształt „liścia koniczyny”'),
         ],
         opis='Struktura drugorzędowa tRNA (model liścia koniczyny).',
         uwaga='Każdy tRNA przenosi określony aminokwas, a dobiera go enzym — syntetaza aminoacylo-tRNA.'),
]

S['b-genom'] = [
    dict(typ='rysunek', tytul='Chromosom metafazowy', svg=_chrom,
         znaczniki=[
             (182, 220, 100, 220, 'Chromatyda', 'jedna cząsteczka DNA'),
             (200, 146, 100, 146, 'Centromer (przewężenie pierwotne)', 'łączy chromatydy siostrzane'),
             (231, 146, 320, 200, 'Kinetochor', 'miejsce przyczepu włókien wrzeciona'),
             (182, 32, 100, 30, 'Telomer', 'chroni końce chromosomu'),
             (258, 84, 330, 84, 'Ramię krótkie (p)', ''),
             (258, 220, 330, 260, 'Ramię długie (q)', ''),
         ],
         opis='Chromosom zbudowany z dwóch chromatyd siostrzanych.',
         uwaga='Chromosom metafazowy ma dwie chromatydy, bo DNA zostało powielone w fazie S. Po anafazie każda chromatyda staje się osobnym chromosomem.'),
]

S['b-replikacja'] = [
    dict(typ='rysunek', tytul='Widełki replikacyjne', svg=_widelki(),
         znaczniki=[
             (152, 150, 90, 220, 'Helikaza', 'rozplata podwójną helisę'),
             (80, 150, 40, 270, 'Nić macierzysta (podwójna helisa)', ''),
             (300, 207, 300, 285, 'Nić wiodąca', 'synteza ciągła'),
             (275, 140 - 125 * 90 / 230 + 12, 320, 20, 'Fragment Okazakiego', 'odcinek nici opóźnionej'),
             (189, 140 - 39 * 90 / 230 + 12, 210, 30, 'Starter RNA', 'synteza przez prymazę'),
             (200, 160 + 50 * 90 / 230 - 12, 120, 285, 'Polimeraza DNA', 'dobudowuje nukleotydy do końca 3′'),
             (181, 140 - 31 * 90 / 230 - 6, 100, 60, 'Białka SSB', 'stabilizują pojedyncze nici'),
             (355, 72, 385, 120, 'Nić opóźniona', 'synteza nieciągła'),
         ],
         opis='Replikacja DNA w obrębie widełek.',
         uwaga='Fragmenty Okazakiego powstają, bo polimeraza syntetyzuje tylko w kierunku 5′→3′, a nić opóźniona biegnie przeciwnie do ruchu widełek.'),
]

S['b-populacje'] = [
    dict(typ='rysunek', tytul='Krzywe wzrostu populacji', svg=_wzrost,
         znaczniki=[
             (241, 62, 300, 30, 'Wzrost wykładniczy (krzywa J)', 'nieograniczone zasoby'),
             (330, 81, 330, 120, 'Wzrost logistyczny (krzywa S)', 'opór środowiska'),
             (120, 78, 150, 40, 'Pojemność środowiska (K)', 'maksymalna liczebność możliwa do utrzymania'),
             (235, 140, 300, 200, 'Faza szybkiego wzrostu', ''),
         ],
         opis='Porównanie wzrostu wykładniczego i logistycznego.',
         uwaga='W naturze wzrost wykładniczy trwa krótko — np. po zasiedleniu nowego terenu przez gatunek inwazyjny.'),
    dict(typ='rysunek', tytul='Krzywe przeżywania', svg=_przezywanie,
         znaczniki=[
             (250, 46, 230, 18, 'Typ I', 'wysoka przeżywalność do starości — np. człowiek, słoń'),
             (190, 145, 250, 140, 'Typ II', 'stałe ryzyko śmierci — np. wiele ptaków'),
             (70, 160, 130, 170, 'Typ III', 'ogromna śmiertelność młodych — np. ryby, ostrygi'),
         ],
         opis='Trzy typy krzywych przeżywania (oś Y w skali logarytmicznej).',
         uwaga='Typ III wiąże się z dużą liczbą potomstwa bez opieki (strategia r), typ I — z małą liczbą potomstwa i opieką (strategia K).'),
]

S['b-dobor'] = [
    dict(typ='rysunek', tytul='Typy doboru naturalnego', svg=_dobor(),
         znaczniki=[
             (65, 60, 65, 25, 'Dobór stabilizujący', 'eliminuje skrajne fenotypy'),
             (225, 130, 225, 70, 'Dobór kierunkowy', 'przesuwa średnią wartość cechy'),
             (298, 160, 335, 70, 'Dobór rozrywający', 'faworyzuje oba skrajne fenotypy'),
             (120, 236, 130, 150, 'Rozkład cechy przed doborem', 'linia przerywana'),
         ],
         opis='A, B, C — rozkład cechy w populacji przed doborem (linia przerywana) i po nim (linia ciągła).',
         uwaga='Dobór rozrywający może prowadzić do specjacji sympatrycznej.'),
]

S['b-ekosystem'] = [
    dict(typ='rysunek', tytul='Piramida ekologiczna', viewBox='0 60 400 235', svg=_piramida,
         znaczniki=[
             (200, 240, 60, 285, 'Producenci', 'rośliny, glony, sinice'),
             (200, 195, 40, 195, 'Konsumenci I rzędu', 'roślinożercy'),
             (200, 150, 40, 140, 'Konsumenci II rzędu', 'drapieżniki'),
             (200, 105, 40, 85, 'Konsumenci III rzędu', 'drapieżniki szczytowe'),
             (360, 200, 380, 280, 'Przekazanie energii na wyższy poziom', 'ok. 10%, reszta to ciepło z oddychania'),
         ],
         opis='Piramida energii (produkcji) w ekosystemie.',
         uwaga='Piramida energii nigdy nie jest odwrócona, natomiast piramida liczebności może być (np. jedno drzewo i tysiące owadów).'),
]
