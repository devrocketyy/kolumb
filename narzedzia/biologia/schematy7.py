# Schematy biologii — porcja 7: rysunki z botaniki.
import math

S = {}


def kropki(pts, r=2):
    return ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="{r}"/>' for x, y in pts)


def lustro(d_lewy, d_prawy):
    return f'<path class="f" d="{d_lewy}"/><path class="f" d="{d_prawy}"/>'


# ---------- kwiat ----------
_kwiat = (
    '<rect class="f" x="195" y="222" width="10" height="78"/>'
    + lustro('M172 216 Q96 182 88 86 Q140 116 182 208 Z', 'M228 216 Q304 182 312 86 Q260 116 218 208 Z')
    + lustro('M168 224 Q122 246 102 220 Q138 214 170 218 Z', 'M232 224 Q278 246 298 220 Q262 214 230 218 Z')
    + '<ellipse class="f2" cx="200" cy="218" rx="40" ry="11"/>'
    + '<path class="s" d="M178 210 L152 118 M222 210 L248 118"/>'
    + '<ellipse class="f2" cx="150" cy="108" rx="7" ry="13" transform="rotate(-15 150 108)"/><ellipse class="f2" cx="250" cy="108" rx="7" ry="13" transform="rotate(15 250 108)"/>'
    + '<ellipse class="f" cx="200" cy="184" rx="24" ry="28"/>'
    + '<circle class="s" cx="194" cy="176" r="5"/><circle class="s" cx="206" cy="190" r="5"/><circle class="s" cx="194" cy="196" r="5"/>'
    + '<rect class="f" x="197" y="98" width="6" height="60"/>'
    + '<ellipse class="f2" cx="200" cy="94" rx="15" ry="6"/>'
)

# ---------- przekrój liścia ----------
def _lisc():
    out = '<line x1="10" y1="36" x2="390" y2="36" stroke="currentColor" stroke-width="3"/>'
    out += ''.join(f'<rect class="f" x="{10 + k * 380 / 14:.1f}" y="38" width="{380 / 14:.1f}" height="16" rx="2"/>' for k in range(14))
    out += ''.join(f'<rect class="f" x="{x}" y="56" width="16" height="56" rx="5"/>' + kropki([(x + 5, 66), (x + 11, 80), (x + 5, 94), (x + 11, 104)], 2.2) for x in range(12, 388, 19))
    for i, (x, y) in enumerate([(30, 130), (70, 150), (40, 180), (110, 128), (120, 178), (300, 130), (340, 150), (290, 175), (350, 185), (380, 130), (250, 130), (80, 196), (330, 200)]):
        out += f'<ellipse class="f" cx="{x}" cy="{y}" rx="17" ry="12"/>' + kropki([(x - 5, y - 2), (x + 5, y + 3)], 2)
    out += '<circle class="f" cx="195" cy="160" r="40"/><circle class="f2" cx="195" cy="148" r="18"/>'
    out += ''.join(f'<circle class="s" cx="{x}" cy="{y}" r="5"/>' for x, y in ((186, 142), (200, 140), (194, 154), (206, 152)))
    out += '<path class="s2" d="M170 178 Q195 190 220 178"/>' + kropki([(185, 182), (195, 186), (205, 182)], 2)
    out += ''.join(f'<rect class="f" x="{x}" y="214" width="28" height="16" rx="2"/>' for x in list(range(10, 250, 28)) + list(range(296, 380, 28)))
    out += '<ellipse class="f2" cx="262" cy="222" rx="10" ry="8"/><ellipse class="f2" cx="284" cy="222" rx="10" ry="8"/>'
    out += '<line x1="10" y1="232" x2="390" y2="232" stroke="currentColor" stroke-width="2"/>'
    return out


# ---------- strefy korzenia ----------
_korzen = (
    '<path class="f" d="M184 0 L184 236 Q184 262 200 270 Q216 262 216 236 L216 0 Z"/>'
    '<path class="f2" d="M180 244 Q180 288 200 296 Q220 288 220 244 Q200 256 180 244 Z"/>'
    + ''.join(f'<rect class="s2" x="{x}" y="{y}" width="8" height="8"/>' for y in range(220, 244, 8) for x in range(188, 212, 8))
    + ''.join(f'<path class="s" d="M184 {y} l-{18 + (y % 3) * 6} {-(y % 7)} M216 {y} l{18 + (y % 3) * 6} {-(y % 5)}"/>' for y in range(80, 160, 9))
    + '<path class="f" d="M184 30 L130 8 L128 16 L184 44 Z"/><path class="f" d="M216 48 L272 22 L274 30 L216 62 Z"/>'
)

# ---------- przekroje łodyg ----------
def _lodygi():
    out = '<circle class="f" cx="105" cy="150" r="92"/><circle cx="105" cy="150" r="56" fill="var(--surface)" stroke="none"/>'
    out += '<circle class="dash" cx="105" cy="150" r="66"/>'
    for k in range(8):
        a = math.radians(k * 45)
        x, y = 105 + 66 * math.cos(a), 150 + 66 * math.sin(a)
        out += f'<ellipse class="f2" cx="{x:.1f}" cy="{y:.1f}" rx="9" ry="14" transform="rotate({k * 45 + 90} {x:.1f} {y:.1f})"/>'
    out += '<circle cx="295" cy="150" r="92" fill="var(--surface-2)" stroke="currentColor" stroke-width="1.6"/>'
    for x, y in ((295, 150), (260, 110), (330, 105), (250, 170), (340, 175), (295, 90), (295, 205), (230, 135), (360, 140), (270, 220), (320, 220), (275, 70), (318, 70), (262, 145), (325, 145)):
        out += f'<ellipse class="f2" cx="{x}" cy="{y}" rx="7" ry="9"/>'
    out += '<text class="t" x="70" y="292">dwuliścienna</text><text class="t" x="255" y="292">jednoliścienna</text>'
    return out


# ---------- aparat szparkowy ----------
_szpark = (
    '<path class="f" d="M10 10 L150 10 L170 60 L130 120 L150 180 L170 240 L150 290 L10 290 Z"/>'
    '<path class="f" d="M390 10 L250 10 L230 60 L270 120 L250 180 L230 240 L250 290 L390 290 Z"/>'
    '<path class="f" d="M150 10 L250 10 L230 60 L170 60 Z"/><path class="f" d="M150 290 L250 290 L230 240 L170 240 Z"/>'
    '<path class="f2" d="M200 62 Q140 66 142 150 Q140 234 200 238 Q178 150 200 62 Z"/>'
    '<path class="f2" d="M200 62 Q260 66 258 150 Q260 234 200 238 Q222 150 200 62 Z"/>'
    '<path d="M200 66 Q182 150 200 234 Q218 150 200 66 Z" fill="var(--surface)" stroke="currentColor" stroke-width="3.5"/>'
    + kropki([(160, 110), (165, 160), (162, 200), (240, 100), (236, 150), (240, 205)], 4)
    + '<circle class="s" cx="168" cy="140" r="8"/><circle class="s" cx="232" cy="175" r="8"/>'
)

# ---------- nasienie fasoli ----------
_nasienie = (
    '<path class="f2" d="M60 150 Q60 60 200 60 Q340 60 340 150 Q340 240 200 240 Q120 240 110 200 Q100 175 80 190 Q60 200 60 150 Z"/>'
    '<path class="f" d="M74 150 Q74 74 200 74 Q326 74 326 150 Q326 226 200 226 Q130 226 120 196 Q112 168 96 176 Q74 186 74 150 Z"/>'
    '<path class="s2" d="M120 120 Q200 100 290 130 M130 175 Q210 200 300 170"/>'
    '<path class="f2" d="M100 120 L130 140 L104 150 Z"/>'
    '<path class="f2" d="M126 126 q10 -18 26 -14 q-6 14 -26 14 Z M128 130 q16 -6 24 6 q-14 6 -24 -6 Z"/>'
    '<rect class="d" x="74" y="186" width="16" height="5" rx="2" transform="rotate(-30 82 188)"/>'
)

# ---------- zalążek ----------
_zalazek = (
    '<path class="f2" d="M72 135 Q80 60 200 60 Q320 60 322 150 Q320 240 200 240 Q80 240 72 165 L96 160 L96 140 Z"/>'
    '<path class="f" d="M88 138 Q96 76 200 76 Q306 76 308 150 Q306 224 200 224 Q96 224 88 162 L100 158 L100 142 Z"/>'
    '<ellipse cx="200" cy="150" rx="78" ry="44" fill="var(--surface)" stroke="currentColor" stroke-width="1.6"/>'
    '<circle class="f2" cx="150" cy="150" r="12"/><circle class="d" cx="150" cy="150" r="3"/>'
    '<circle class="f" cx="136" cy="134" r="9"/><circle class="f" cx="136" cy="166" r="9"/>'
    '<circle class="d" cx="198" cy="146" r="5"/><circle class="d" cx="210" cy="156" r="5"/>'
    '<circle class="f" cx="258" cy="136" r="8"/><circle class="f" cx="266" cy="152" r="8"/><circle class="f" cx="258" cy="166" r="8"/>'
    '<rect class="f" x="320" y="142" width="76" height="16"/>'
    '<text class="t" x="20" y="150">pyłek ⟶</text>'
)

S['b-rozmnazanie-roslin'] = [
    dict(typ='rysunek', tytul='Budowa kwiatu', svg=_kwiat,
         znaczniki=[
             (200, 92, 200, 20, 'Znamię słupka', 'przyjmuje pyłek'),
             (200, 130, 270, 60, 'Szyjka słupka', 'przez nią rośnie łagiewka pyłkowa'),
             (215, 200, 340, 220, 'Zalążnia', 'przekształca się w owoc'),
             (194, 176, 330, 150, 'Zalążek', 'przekształca się w nasienie'),
             (150, 108, 120, 30, 'Pylnik', 'wytwarza ziarna pyłku'),
             (165, 165, 60, 160, 'Nitka pręcika', ''),
             (100, 100, 40, 60, 'Płatek korony', 'zwabia zapylaczy'),
             (110, 222, 40, 250, 'Działka kielicha', 'chroni pąk kwiatowy'),
             (230, 222, 340, 260, 'Dno kwiatowe', ''),
             (200, 270, 260, 290, 'Szypułka', ''),
         ],
         opis='Schemat obupłciowego kwiatu rośliny okrytonasiennej (przekrój podłużny).',
         uwaga='Pręciki to męskie organy kwiatu, słupek — żeński. Z zalążni powstaje owoc, z zalążków — nasiona.'),
    dict(typ='rysunek', tytul='Budowa zalążka', svg=_zalazek,
         znaczniki=[
             (200, 66, 200, 18, 'Osłonki zalążka', 'przekształcają się w łupinę nasienną'),
             (92, 150, 30, 100, 'Okienko (mikropyle)', 'tędy wnika łagiewka pyłkowa'),
             (150, 150, 120, 280, 'Komórka jajowa', 'po zapłodnieniu — zygota'),
             (136, 166, 50, 230, 'Synergidy', 'kierują łagiewkę pyłkową'),
             (204, 151, 210, 280, 'Komórka centralna z jądrami biegunowymi', 'po zapłodnieniu — bielmo (3n)'),
             (266, 152, 300, 280, 'Antypody', ''),
             (285, 110, 340, 40, 'Ośrodek (nucellus)', ''),
             (360, 150, 380, 100, 'Sznureczek', 'łączy zalążek z łożyskiem'),
         ],
         opis='Przekrój przez zalążek z dojrzałym woreczkiem zalążkowym (gametofitem żeńskim).',
         uwaga='Woreczek zalążkowy ma 7 komórek i 8 jąder: komórkę jajową, 2 synergidy, 3 antypody i komórkę centralną z 2 jądrami biegunowymi.'),
    dict(typ='rysunek', tytul='Budowa nasienia fasoli', svg=_nasienie,
         znaczniki=[
             (200, 66, 200, 20, 'Łupina nasienna', 'ochrona zarodka'),
             (230, 150, 300, 280, 'Liścień', 'magazynuje materiały zapasowe'),
             (110, 136, 30, 90, 'Korzeń zarodkowy', 'pierwszy wyrasta przy kiełkowaniu'),
             (140, 120, 150, 30, 'Pąk (zawiązek pędu)', ''),
             (82, 188, 30, 260, 'Znaczek', 'ślad po sznureczku'),
         ],
         opis='Nasienie fasoli po zdjęciu części łupiny — widoczny jeden liścień i oś zarodka.',
         uwaga='Fasola jest dwuliścienna i nie ma bielma — materiały zapasowe zgromadzone są w liścieniach.'),
]

S['b-organy'] = [
    dict(typ='rysunek', tytul='Przekrój poprzeczny liścia', svg=_lisc(),
         znaczniki=[
             (60, 36, 40, 12, 'Kutykula', 'ogranicza parowanie'),
             (150, 46, 150, 12, 'Skórka górna', ''),
             (240, 84, 300, 12, 'Miękisz palisadowy', 'najwięcej chloroplastów — główne miejsce fotosyntezy'),
             (70, 150, 20, 100, 'Miękisz gąbczasty', ''),
             (95, 155, 20, 160, 'Przestwory międzykomórkowe', 'wymiana gazowa'),
             (195, 146, 380, 100, 'Drewno', 'woda i sole mineralne'),
             (195, 184, 380, 170, 'Łyko', 'produkty fotosyntezy'),
             (160, 160, 140, 250, 'Wiązka przewodząca (nerw liścia)', ''),
             (60, 222, 20, 245, 'Skórka dolna', ''),
             (273, 224, 330, 280, 'Aparat szparkowy', 'wymiana gazowa i transpiracja'),
         ],
         opis='Przekrój przez liść rośliny dwuliściennej.',
         uwaga='W wiązce przewodzącej liścia drewno leży od górnej strony, a łyko — od dolnej. Aparaty szparkowe są zwykle w skórce dolnej.'),
    dict(typ='rysunek', tytul='Strefy korzenia', svg=_korzen,
         znaczniki=[
             (200, 284, 280, 290, 'Czapeczka', 'chroni stożek wzrostu, odbiera grawitację'),
             (200, 230, 290, 230, 'Stożek wzrostu (merystem wierzchołkowy)', 'podziały komórek'),
             (200, 190, 290, 180, 'Strefa wydłużania', 'wzrost komórek na długość'),
             (200, 120, 300, 120, 'Strefa włośnikowa', 'pobieranie wody i soli'),
             (160, 98, 70, 120, 'Włośnik', 'wypustka komórki skórki'),
             (150, 18, 70, 40, 'Korzeń boczny', 'wyrasta z okolnicy'),
         ],
         opis='Wierzchołek korzenia z kolejnymi strefami.',
         uwaga='Włośniki są krótkotrwałe i powstają tylko w młodej części korzenia — dlatego przesadzanie może uszkodzić roślinę.'),
]

S['b-tkanki-roslinne'] = [
    dict(typ='rysunek', tytul='Przekrój łodygi dwuliściennej i jednoliściennej', svg=_lodygi(),
         znaczniki=[
             (105, 58, 60, 18, 'Skórka', ''),
             (75, 76, 160, 18, 'Kora pierwotna', ''),
             (171, 150, 200, 70, 'Wiązka przewodząca w pierścieniu', 'typowa dla dwuliściennych'),
             (80, 211, 30, 270, 'Kambium', 'merystem boczny — przyrost na grubość'),
             (105, 150, 20, 150, 'Rdzeń', 'miękisz'),
             (330, 105, 380, 30, 'Wiązki rozproszone', 'typowe dla jednoliściennych, brak kambium'),
         ],
         opis='Po lewej łodyga rośliny dwuliściennej, po prawej — jednoliściennej.',
         uwaga='Jednoliścienne nie mają kambium w wiązkach — dlatego większość z nich nie przyrasta na grubość (wyjątek: np. palmy przez inny mechanizm).'),
]

S['b-gospodarka-wodna'] = [
    dict(typ='rysunek', tytul='Aparat szparkowy', svg=_szpark,
         znaczniki=[
             (155, 150, 40, 150, 'Komórka szparkowa', 'ma chloroplasty, reguluje otwarcie szparki'),
             (200, 150, 300, 150, 'Szparka', 'otwór, przez który zachodzi wymiana gazów'),
             (192, 110, 300, 40, 'Zgrubiała ściana od strony szparki', 'decyduje o wyginaniu komórek'),
             (160, 110, 80, 40, 'Chloroplast', ''),
             (232, 175, 300, 260, 'Jądro komórkowe', ''),
             (80, 230, 60, 280, 'Komórka skórki', 'brak chloroplastów'),
         ],
         opis='Aparat szparkowy w widoku z powierzchni liścia.',
         uwaga='Komórki szparkowe jako jedyne w skórce mają chloroplasty. Wzrost turgoru wygina je i otwiera szparkę.'),
]
