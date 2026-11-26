# Schematy geografii — porcja 3 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
S = {}


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')


# ---------- oświetlenie 22 czerwca ----------
_cx, _cy, _r = 150, 150, 108
_lat = lambda la: (_r * math.cos(math.radians(la)), -_r * math.sin(math.radians(la)))
_os = (f'<defs><clipPath id="g3z"><circle cx="{_cx}" cy="{_cy}" r="{_r}"/></clipPath></defs>'
       f'<circle class="gw" cx="{_cx}" cy="{_cy}" r="{_r}"/>'
       f'<g transform="rotate(-23.45 {_cx} {_cy})">'
       + ''.join(f'<path class="{"s2" if la else "s"}" d="M{_cx - _lat(la)[0]:.1f} {_cy + _lat(la)[1]:.1f} H{_cx + _lat(la)[0]:.1f}"/>' for la in (66.55, 23.45, 0, -23.45, -66.55))
       + f'<path class="s" d="M{_cx} {_cy - _r - 18} V{_cy + _r + 18}"/><circle class="d" cx="{_cx}" cy="{_cy - _r}" r="3"/></g>'
       f'<rect class="gs2" x="{_cx}" y="0" width="200" height="300" clip-path="url(#g3z)" opacity="0.6"/>'
       f'<circle class="s" cx="{_cx}" cy="{_cy}" r="{_r}"/><path class="dash" d="M{_cx} {_cy - _r - 10} V{_cy + _r + 10}"/>'
       + ''.join(strz(4, y, 36, y, 'hot', 7) for y in (70, 110, 150, 190, 230))
       + '<text class="ts" x="20" y="285">promienie Słońca</text><text class="tb" x="215" y="270">noc</text><text class="tb" x="70" y="270">dzień</text>')
def _rot(dx, dy, t=23.45):
    c, n = math.cos(math.radians(t)), math.sin(math.radians(t))
    return (_cx + dx * c + dy * n, _cy - dx * n + dy * c)


S['g-obiegowy'] = [
 dict(typ='rysunek', tytul='Oświetlenie Ziemi 22 czerwca', svg=_os,
      znaczniki=[(*_rot(0, -108), 290, 30, 'Biegun N', 'Oś nachylona ku Słońcu — dzień polarny'),
                 (*_rot(-99.1, -43.0), 285, 75, 'Zwrotnik Raka', 'Słońce w zenicie w południe — 23°27′N'),
                 (*_rot(0, -95), 285, 115, 'Za kołem N', 'Za kołem podbiegunowym N cała doba jest oświetlona'),
                 (_cx, 200, 285, 160, 'Terminator', 'Granica dnia i nocy'),
                 (*_rot(0, 95), 285, 205, 'Za kołem S', 'Za kołem podbiegunowym S noc polarna — Słońce nie wschodzi'),
                 (*_rot(-60, 0), 285, 250, 'Równik', 'Dzień i noc po 12 h przez cały rok')],
      opis='Oświetlenie Ziemi w dniu przesilenia letniego na półkuli północnej (Słońce z lewej).',
      uwaga='22 czerwca: na półkuli N dzień jest dłuższy od nocy i tym dłuższy, im dalej na północ; na kole podbiegunowym S i dalej trwa noc polarna.'),
]

S['g-obrotowy'] = [
 dict(typ='proces', tytul='Obliczanie czasu słonecznego i strefowego', opis='Algorytm do zadań maturalnych.',
      kroki=[('Ustal różnicę długości geograficznej', 'Jeśli punkty leżą na tej samej półkuli — odejmij; na różnych (E i W) — dodaj.'),
             ('Przelicz na czas słoneczny', '1° = 4 min, 1′ = 4 s.'),
             ('Ustal kierunek', 'Na wschód czas jest późniejszy (dodaj), na zachód — wcześniejszy (odejmij).'),
             ('Dla czasu strefowego', 'Policz różnicę stref (po 1 h); uwzględnij czas letni, jeśli jest podany.'),
             ('Sprawdź datę', 'Przy przekroczeniu północy lub linii zmiany daty zmień datę.')],
      uwaga='Najczęstszy błąd: odejmowanie czasu przy przesuwaniu się na wschód.'),
]

# ---------- jaskinia krasowa ----------
_kr = ('<rect class="gn" x="0" y="0" width="400" height="60"/>'
       '<path class="gs" d="M0 60 H120 Q140 60 150 82 Q160 60 180 60 H300 L320 120 Q330 150 360 150 H400 V300 H0 Z"/>'
       '<path class="gt" d="M0 56 H120 Q140 56 150 78 Q160 56 180 56 H300 L304 64 H182 Q160 64 150 86 Q140 64 120 64 H0 Z"/>'
       '<path class="gs2" d="M222 56 L232 18 L248 14 L256 56 Z"/><path class="gt" d="M228 20 l8 -6 l12 2 l-4 6 Z"/>'
       + ''.join(f'<path class="s2" d="M0 {y} H{400 if y > 150 else 305 + (y - 60) * 0.3:.0f}"/>' for y in (95, 130, 170, 215, 260))
       + ''.join(f'<path class="s2" d="M{x} {y} v25"/>' for x, y in ((40, 95), (95, 130), (260, 95), (340, 170), (60, 215), (300, 215)))
       + '<path class="gg" d="M80 160 C90 120 240 118 270 150 C285 165 280 205 250 212 C200 222 110 222 85 205 C72 195 74 175 80 160 Z"/>'
       '<path class="gw2" d="M95 205 C150 214 210 214 250 207 C290 200 330 175 360 152 L366 158 C330 185 290 210 250 215 C200 222 140 222 95 212 Z"/>'
       + ''.join(f'<path class="gc" d="M{x - 4} {y} L{x + 4} {y} L{x} {y + h} Z"/>' for x, y, h in ((120, 134, 18), (140, 130, 26), (165, 128, 14), (230, 131, 22)))
       + ''.join(f'<path class="gc" d="M{x - 5} {y} l5 -{h} l5 {h} Z"/>' for x, y, h in ((125, 204, 16), (190, 210, 24), (215, 208, 12)))
       + '<path class="gc" d="M245 133 h8 v72 h-8 Z"/>'
       + '<path class="cold" d="M150 86 L152 120" style="stroke-dasharray:3 3"/><path class="coldf" d="M152 124 l-4 -7 l8 0 Z"/>'
       + '<path class="gw2" d="M360 150 Q380 152 400 156 V162 Q380 158 362 156 Z"/>')
S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Jaskinia krasowa', svg=_kr,
      znaczniki=[(150, 78, 120, 25, 'Lej krasowy', 'Zapadlisko — woda wnika w głąb masywu'),
                 (240, 30, 280, 25, 'Ostaniec', 'Odporny fragment wapienia (np. Maczuga Herkulesa)'),
                 (140, 150, 160, 108, 'Stalaktyt', 'Naciek zwisający ze stropu'),
                 (190, 195, 150, 250, 'Stalagmit', 'Naciek rosnący od dna'),
                 (249, 170, 320, 210, 'Stalagnat', 'Kolumna — zrośnięty stalaktyt ze stalagmitem'),
                 (300, 200, 290, 260, 'Ciek podziemny', 'Odprowadza wodę krasową'),
                 (372, 155, 360, 110, 'Wywierzysko', 'Wypływ wody krasowej na powierzchnię')],
      opis='Formy krasu podziemnego i powierzchniowego w wapieniach (przekrój).',
      uwaga='Rozpuszczanie: CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂. Nacieki tworzą się w reakcji odwrotnej, gdy z kapiącej wody uchodzi CO₂.'),
]

# ---------- wybrzeże klifowe ----------
_kl = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gw2" d="M150 170 H400 V300 H150 Z"/>'
       '<path class="gp" d="M150 205 L400 225 V300 H150 Z" opacity="0.8"/>'
       '<path class="gc" d="M0 70 H190 L200 120 L212 160 L205 178 L222 188 L215 205 H0 Z"/>'
       '<path class="gp" d="M0 70 H190 L194 95 H0 Z"/><path class="gt" d="M0 64 H192 L190 72 H0 Z"/>'
       '<path class="gg" d="M0 150 H212 L214 160 H0 Z" opacity="0.5"/>'
       '<path class="gs" d="M205 178 L240 184 L262 196 L230 200 L215 205 Z"/>'
       + ''.join(f'<circle class="gs2" cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in ((236, 188, 4), (250, 192, 3), (226, 194, 3.5)))
       + '<path class="dash" d="M260 64 L265 160 L262 210"/>'
       + ''.join(f'<path class="cold" d="M{x} 172 q8 -8 16 0"/>' for x in (275, 305, 335, 365))
       + strz(350, 160, 300, 160, 'cold', 7)
       + ''.join(f'<path class="gf2" d="M{x} 64 l-6 0 l6 -14 l6 14 Z"/>' for x in (30, 60, 150, 172))
       + '<text class="ts" x="268" y="58">dawny zasięg lądu</text>')
S['g-rzezba'].append(
 dict(typ='rysunek', tytul='Wybrzeże klifowe', svg=_kl,
      znaczniki=[(198, 120, 120, 30, 'Klif', 'Strome urwisko w glinach i piaskach'),
                 (212, 182, 120, 230, 'Nisza abrazyjna', 'Fale podcinają podstawę klifu'),
                 (240, 190, 290, 120, 'Rumowisko', 'Obrywy z klifu, rozbijane przez fale'),
                 (300, 230, 320, 270, 'Platforma', 'Abrazyjna — zrównane dno przed klifem'),
                 (330, 160, 340, 100, 'Abrazja', 'Fale niszczą brzeg'),
                 (262, 120, 240, 30, 'Cofanie klifu', 'Klif przesuwa się w głąb lądu')],
      opis='Wybrzeże niszczone przez morze (np. Wolin, Orłowo, Jastrzębia Góra).',
      uwaga='Fale wymywają niszę u podstawy, górna część klifu obrywa się, a klif cofa się w głąb lądu. Klify chroni się opaskami i ostrogami.'))

# ---------- delta i estuarium ----------
_de = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
       '<path class="gw2" d="M0 210 Q100 200 195 210 V300 H0 Z"/><path class="gw2" d="M205 210 Q300 200 400 210 V300 H205 Z"/>'
       '<path class="gp ol" d="M40 212 Q60 255 100 268 Q140 255 160 212 Z"/>'
       '<path class="cold" d="M100 20 C95 80 105 140 100 190" style="stroke-width:5"/>'
       '<path class="cold" d="M100 190 L60 240 M100 190 L85 260 M100 190 L115 262 M100 190 L145 238" style="stroke-width:2.2"/>'
       '<path class="gw2" d="M296 20 C298 80 300 130 300 150 L250 212 L350 212 Z"/>'
       '<path class="cold" d="M296 20 C298 80 300 130 300 150" style="stroke-width:5"/>'
       + strz(275, 250, 275, 220, 'cold', 7) + strz(325, 222, 325, 252, 'cold', 7)
       + '<path class="s" d="M200 0 V300" style="stroke-dasharray:4 3"/>'
       '<text class="tb" x="100" y="290" text-anchor="middle">delta</text><text class="tb" x="300" y="290" text-anchor="middle">estuarium</text>'
       '<text class="ts" x="300" y="270" text-anchor="middle">przypływ ↑  odpływ ↓</text>')
S['g-rzezba'].append(
 dict(typ='rysunek', tytul='Delta i estuarium', svg=_de,
      znaczniki=[(100, 190, 130, 150, 'Rozwidlenie', 'Rzeka dzieli się na odnogi'),
                 (100, 250, 130, 230, 'Stożek delty', 'Osady narastają — ląd przyrasta (Wisła, Nil)'),
                 (300, 180, 320, 120, 'Ujście', 'Pływy wymywają osady'),
                 (275, 235, 350, 175, 'Pływy', 'Silne przypływy i odpływy (Tamiza, Łaba)')],
      opis='Dwa typy ujść rzecznych (widok z góry).',
      uwaga='Delta powstaje, gdy rzeka niesie dużo osadów, a pływy i prądy są słabe; estuarium — w morzach o silnych pływach.'))

# ---------- lodowiec górski ----------
_ld = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gs2" d="M0 300 V70 L40 30 L80 50 L110 20 L150 60 L220 120 L300 180 L400 210 V300 Z"/>'
       '<path class="gi" d="M45 70 Q70 40 110 45 Q140 60 150 80 L220 140 L290 196 Q300 206 290 214 L270 214 Q240 190 200 162 L120 110 Q70 100 45 70 Z"/>'
       + ''.join(f'<path class="s2" d="M{x} {y} l10 -8"/>' for x, y in ((160, 112), (180, 128), (200, 142), (220, 158), (240, 172)))
       + '<path class="gc" d="M262 214 Q280 196 300 210 Q290 226 262 222 Z"/>'
       '<path class="gc" d="M160 92 l60 48 l-4 4 l-60 -47 Z" opacity="0.9"/>'
       '<path class="cold" d="M285 222 C310 240 340 250 400 252" style="stroke-width:3"/>'
       '<path class="dash" d="M0 112 H400"/><text class="ts" x="395" y="106" text-anchor="end">granica wiecznego śniegu</text>'
       '<path class="gw" d="M300 268 q20 -8 40 0 q-20 8 -40 0 Z"/>')
S['g-lodowce'] = [
 dict(typ='rysunek', tytul='Lodowiec górski', svg=_ld,
      znaczniki=[(85, 70, 120, 20, 'Pole firnowe', 'Obszar zasilania w cyrku — śnieg zmienia się w lód'),
                 (190, 150, 120, 190, 'Jęzor lodowcowy', 'Spływa doliną poniżej granicy wiecznego śniegu'),
                 (210, 150, 260, 130, 'Szczeliny', 'Lód pęka na załomach podłoża'),
                 (188, 116, 250, 70, 'Morena boczna', 'Materiał zebrany ze stoków'),
                 (282, 210, 270, 240, 'Morena czołowa', 'Wał osadów przed czołem lodowca'),
                 (340, 250, 350, 285, 'Potok', 'Wody roztopowe wypływają spod lodowca')],
      opis='Budowa lodowca górskiego (dolinnego) — przekrój wzdłuż doliny.',
      uwaga='Powyżej granicy wiecznego śniegu przeważa zasilanie, poniżej — ablacja (topnienie). Po zaniku lodowca zostaje cyrk (kar) z jeziorem i dolina U.'),
]

# ---------- subdukcja ----------
_sb = ('<rect class="gn" x="0" y="0" width="400" height="60"/>'
       '<path class="gm2" d="M0 120 H400 V300 H0 Z" opacity="0.8"/>'
       '<path class="gw2" d="M0 60 H170 L185 100 L0 100 Z"/>'
       '<path class="gs2" d="M0 100 H185 L210 112 L330 300 L280 300 L180 130 H0 Z"/>'
       '<path class="gl" d="M185 100 L196 70 L240 60 L270 30 L290 55 L320 45 L400 58 V160 L330 160 L260 140 L210 112 Z"/>'
       '<path class="gm" d="M262 170 C266 120 272 80 276 40 L282 40 C280 80 274 125 272 175 Z"/>'
       '<ellipse class="gm" cx="268" cy="185" rx="18" ry="9"/>'
       '<path class="gm" d="M270 30 L276 24 L282 30 Z"/>'
       + ''.join(f'<circle class="hotf" cx="{x}" cy="{y}" r="2.6"/>' for x, y in ((200, 118), (215, 130), (232, 150), (248, 175), (262, 200), (276, 225), (290, 250)))
       + strz(40, 85, 120, 85, 'cold', 8)
       + '<text class="ts" x="8" y="290">astenosfera</text><text class="ts" x="20" y="118">skorupa oceaniczna</text><text class="ts" x="320" y="150">skorupa kontynentalna</text>')
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Subdukcja na granicy płyt', svg=_sb,
      znaczniki=[(100, 112, 110, 160, 'Płyta oceaniczna', 'Cięższa (bazalt) — zanurza się pod kontynentalną'),
                 (187, 98, 150, 30, 'Rów oceaniczny', 'Głębokie obniżenie dna (np. Rów Atakamski)'),
                 (290, 45, 330, 22, 'Wulkan', 'Magma z topniejącej płyty wznosi się ku powierzchni'),
                 (268, 185, 250, 205, 'Ognisko magmy', 'Topnienie skał nad zanurzającą się płytą'),
                 (248, 175, 180, 230, 'Ogniska trzęsień', 'Coraz głębsze w głąb lądu (strefa Benioffa)'),
                 (350, 80, 355, 110, 'Góry', 'Fałdowe góry na krawędzi kontynentu (Andy)')],
      opis='Zbieżna granica płyty oceanicznej i kontynentalnej (np. Andy).',
      uwaga='Przy subdukcji powstają rowy oceaniczne, łańcuchy wulkanów i silne trzęsienia ziemi; ogniska trzęsień układają się w pochyłą strefę.'),
]

# ---------- niż w planie ----------
_nz = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gp" d="M170 140 L290 200 C270 230 230 255 175 262 Z" opacity="0.55"/>'
       + ''.join(f'<ellipse class="s2" cx="170" cy="140" rx="{rx}" ry="{ry}" fill="none"/><text class="ts" x="{170 - rx + 3}" y="137">{v}</text>' for rx, ry, v in ((35, 26, 990), (75, 55, 995), (115, 85, 1000), (155, 118, 1005)))
       + '<text class="tb" x="170" y="145" text-anchor="middle">N</text>'
       '<path class="hot" d="M170 140 C220 160 260 180 290 200"/>'
       + ''.join(f'<path class="hotf" d="M{x} {y} a6 6 0 0 1 11 5 Z"/>' for x, y in ((205, 150), (235, 165), (262, 182)))
       + '<path class="cold" d="M170 140 C180 190 180 230 175 262"/>'
       + ''.join(f'<path class="coldf" d="M{x} {y - 6} L{x} {y + 6} L{x + 10} {y} Z"/>' for x, y in ((179, 175), (181, 205), (179, 235)))
       + ''.join(strz(*c, 's2', 6) for c in ((250, 70, 200, 60), (90, 90, 80, 140), (110, 225, 160, 240), (290, 150, 285, 100)))
       + strz(330, 270, 385, 270, 's', 8) + '<text class="ts" x="300" y="290">ruch niżu (na wschód)</text>')
S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Niż baryczny w planie', svg=_nz,
      znaczniki=[(170, 140, 100, 25, 'Ośrodek niżu', 'Najniższe ciśnienie (poniżej 990 hPa)'),
                 (262, 186, 300, 170, 'Front ciepły', 'Półkola — przed nim długie opady ciągłe'),
                 (181, 215, 120, 270, 'Front chłodny', 'Trójkąty — burze i ulewy'),
                 (215, 215, 290, 230, 'Wycinek ciepły', 'Ciepła masa między frontami'),
                 (325, 140, 340, 110, 'Izobara', 'Linia jednakowego ciśnienia (co 5 hPa)'),
                 (225, 63, 250, 25, 'Wiatr', 'Krąży przeciwnie do wskazówek zegara, ku środkowi')],
      opis='Niż z frontami na mapie synoptycznej (półkula N).',
      uwaga='Na półkuli N powietrze w niżu krąży przeciwnie do ruchu wskazówek zegara i wpływa do środka; po przejściu frontu chłodnego następuje ochłodzenie.'),
]
