# Schematy biologii — porcja 6: kolejne rysunki z fizjologii człowieka.
import math

S = {}


def rura(d, w=9, fill='var(--surface-2)'):
    return (f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{w - 4}" stroke-linecap="round" stroke-linejoin="round"/>')


def luk(cx, cy, r, a0, a1):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    duzy = 1 if (a1 - a0) % 360 > 180 else 0
    return f'M{x0:.1f} {y0:.1f} A{r} {r} 0 {duzy} 1 {x1:.1f} {y1:.1f}'


def pkt(cx, cy, r, a):
    return (round(cx + r * math.cos(math.radians(a)), 1), round(cy + r * math.sin(math.radians(a)), 1))


# ---------- oko ----------
_oko = (
    '<circle class="f" cx="220" cy="150" r="110"/>'
    f'<path class="s2" d="{luk(220, 150, 104, -135, 135)}"/>'
    f'<path d="{luk(220, 150, 98, -125, 125)}" fill="none" stroke="currentColor" stroke-width="3"/>'
    '<path d="M128 92 Q80 150 128 208" fill="var(--surface)" stroke="currentColor" stroke-width="1.6"/>'
    '<rect class="d" x="136" y="100" width="5" height="32" rx="2"/><rect class="d" x="136" y="168" width="5" height="32" rx="2"/>'
    '<ellipse class="f2" cx="140" cy="96" rx="9" ry="6"/><ellipse class="f2" cx="140" cy="204" rx="9" ry="6"/>'
    '<path class="s2" d="M146 99 L152 118 M146 201 L152 182"/>'
    '<ellipse class="f" cx="153" cy="150" rx="13" ry="32"/>'
    '<rect class="f2" x="326" y="158" width="70" height="26"/>'
    '<circle class="d" cx="322" cy="135" r="3.5"/>'
    '<path class="s2" d="M10 130 L90 140 M10 170 L90 160"/><text class="t" x="10" y="122">światło</text>'
)

# ---------- sarkomer ----------
_sark = (
    '<rect class="d" x="36" y="30" width="7" height="160"/><rect class="d" x="357" y="30" width="7" height="160"/>'
    + ''.join(f'<line class="s" x1="43" y1="{y}" x2="152" y2="{y}"/><line class="s" x1="248" y1="{y}" x2="357" y2="{y}"/>' for y in (48, 78, 108, 138, 168))
    + ''.join(f'<rect class="f2" x="118" y="{y - 4}" width="164" height="8" rx="3"/>'
              + ''.join(f'<path class="s2" d="M{x} {y - 4} l-4 -6 M{x} {y + 4} l-4 6"/>' for x in range(128, 196, 12))
              + ''.join(f'<path class="s2" d="M{x} {y - 4} l4 -6 M{x} {y + 4} l4 6"/>' for x in range(208, 276, 12)) for y in (63, 93, 123, 153))
    + '<line class="dash" x1="200" y1="26" x2="200" y2="194"/>'
    + '<path class="s" d="M43 210 l0 -6 M43 210 L118 210 L118 204 M282 204 l0 6 L357 210 L357 204"/>'
    + '<path class="s" d="M118 16 l0 6 M118 16 L282 16 L282 22"/>'
    + '<path class="s" d="M152 222 l0 -6 M152 222 L248 222 L248 216"/>'
)

# ---------- pęcherzyk płucny ----------
_pech = (
    rura('M150 0 L150 74', w=22, fill='var(--surface)')
    + '<circle class="f" cx="150" cy="150" r="82"/><circle cx="150" cy="150" r="77" fill="var(--surface)" stroke="none"/>'
    + rura('M247 15 L247 285', w=30)
    + ''.join(f'<ellipse class="f2" cx="247" cy="{y}" rx="9" ry="5"/>' for y in (60, 110, 160, 210, 255))
    + '<text class="t" x="196" y="128">O₂ →</text><text class="t" x="190" y="182">← CO₂</text>'
    + '<text class="t" x="290" y="290">krew odtlenowana ↑</text><text class="t" x="290" y="20">krew natleniona</text>'
    + '<text class="t" x="110" y="150">powietrze</text>'
)

# ---------- kosmek jelitowy ----------
_kos = (
    '<path class="f2" d="M120 290 L120 80 Q120 20 200 20 Q280 20 280 80 L280 290"/>'
    '<path d="M134 290 L134 82 Q134 36 200 36 Q266 36 266 82 L266 290" fill="var(--surface)" stroke="currentColor" stroke-width="1.2"/>'
    + ''.join(f'<line class="s2" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>' for x1, y1, x2, y2 in
              [(120, y, 113, y) for y in range(90, 290, 10)] + [(280, y, 287, y) for y in range(90, 290, 10)]
              + [(200 + 80 * math.cos(math.radians(a)), 80 - 60 * math.sin(math.radians(a)), 200 + 87 * math.cos(math.radians(a)), 80 - 66 * math.sin(math.radians(a))) for a in range(10, 171, 12)])
    + '<ellipse class="s" cx="127" cy="170" rx="5" ry="10"/><ellipse class="s" cx="273" cy="120" rx="5" ry="10"/>'
    + rura('M160 290 L160 90 Q160 60 200 58 Q240 60 240 90 L240 290', w=7)
    + '<path class="s2" d="M160 120 L240 130 M160 160 L240 150 M160 200 L240 210 M160 240 L240 235"/>'
    + rura('M200 290 L200 95', w=14, fill='var(--surface)')
    + '<text class="t" x="140" y="300">↑ krew</text><text class="t" x="232" y="300">krew ↓</text>'
)

# ---------- skóra ----------
_skora = (
    '<rect class="f2" x="10" y="30" width="380" height="30"/>'
    '<line x1="10" y1="34" x2="390" y2="34" stroke="currentColor" stroke-width="2.5"/>'
    '<rect class="f" x="10" y="60" width="380" height="140"/>'
    '<rect x="10" y="200" width="380" height="92" fill="var(--surface)" stroke="currentColor" stroke-width="1.6"/>'
    + ''.join(f'<circle class="s2" cx="{x}" cy="{y}" r="13"/>' for x, y in ((40, 228), (68, 252), (40, 276), (100, 228), (200, 270), (230, 240), (370, 270), (360, 240)))
    + rura('M120 40 L120 180', w=16, fill='var(--surface)')
    + '<line x1="120" y1="4" x2="120" y2="182" stroke="currentColor" stroke-width="3"/>'
    + '<ellipse class="f2" cx="120" cy="186" rx="11" ry="9"/>'
    + '<path class="f2" d="M128 95 q22 -6 22 10 q8 12 -6 18 q-10 8 -16 -4 z"/>'
    + '<path d="M127 150 L170 70" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"/>'
    + '<path class="s" d="M262 30 c-6 20 6 40 0 60 s6 40 0 60 s6 40 0 60"/>'
    + '<path class="s" d="M262 210 c-20 0 -20 14 0 14 s20 14 0 14 s-20 14 0 14 s20 14 -4 10"/>'
    + rura('M10 196 L390 196', w=10)
    + '<ellipse class="s" cx="330" cy="240" rx="16" ry="11"/><ellipse class="s" cx="330" cy="240" rx="10" ry="6"/><ellipse class="s" cx="330" cy="240" rx="4" ry="2.5"/>'
    + '<path class="s2" d="M330 251 L330 290"/>'
    + '<ellipse class="f2" cx="320" cy="68" rx="5" ry="8"/>'
)

# ---------- staw ----------
_staw = (
    '<path class="f" d="M150 0 L150 110 Q150 160 200 160 Q250 160 250 110 L250 0 Z"/>'
    '<path d="M154 120 Q158 152 200 154 Q242 152 246 120" fill="none" stroke="currentColor" stroke-width="6" opacity=".45"/>'
    '<path class="f" d="M120 300 L120 190 Q120 174 140 172 Q170 196 200 196 Q230 196 260 172 Q280 174 280 190 L280 300 Z"/>'
    '<path d="M146 178 Q170 200 200 200 Q230 200 254 178" fill="none" stroke="currentColor" stroke-width="6" opacity=".45"/>'
    '<path class="s" d="M138 70 Q120 170 126 250 M262 70 Q280 170 274 250"/>'
    '<path d="M130 90 Q100 170 112 230 M270 90 Q300 170 288 230" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>'
    + ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="1.4"/>' for x, y in ((180, 172), (200, 176), (220, 172), (168, 166), (232, 166)))
)

# ---------- plemnik ----------
_plem = (
    '<ellipse class="f" cx="62" cy="80" rx="42" ry="27"/>'
    '<path class="f2" d="M40 57 Q12 66 20 80 Q12 94 40 103 Q30 80 40 57 Z"/>'
    '<ellipse class="f2" cx="68" cy="80" rx="24" ry="17"/>'
    '<rect class="f" x="104" y="74" width="14" height="12" rx="3"/>'
    '<rect class="f" x="118" y="72" width="64" height="16" rx="6"/>'
    + ''.join(f'<path class="s2" d="M{x} 72 l8 16"/>' for x in range(122, 180, 8))
    + '<path class="s" d="M182 80 q15 -16 30 0 t30 0 t30 0 t30 0 t30 0 t30 0"/>'
)

S['b-nerwy'] = [
    dict(typ='rysunek', tytul='Budowa oka', svg=_oko,
         znaczniki=[
             (104, 150, 60, 285, 'Rogówka', 'przezroczysta, załamuje światło'),
             (138, 115, 70, 30, 'Tęczówka', 'reguluje ilość światła'),
             (139, 150, 20, 150, 'Źrenica', 'otwór w tęczówce'),
             (153, 168, 150, 285, 'Soczewka', 'akomodacja — ostre widzenie'),
             (140, 96, 130, 14, 'Ciało rzęskowe', 'zmienia kształt soczewki'),
             (230, 165, 230, 285, 'Ciało szkliste', ''),
             pkt(220, 150, 98, -40) + (320, 30, 'Siatkówka', 'fotoreceptory: pręciki i czopki'),
             pkt(220, 150, 104, -70) + (240, 14, 'Naczyniówka', 'odżywia siatkówkę'),
             pkt(220, 150, 110, 60) + (310, 285, 'Twardówka', 'ochrona i nadanie kształtu'),
             (322, 135, 385, 110, 'Plamka żółta', 'najwięcej czopków — najostrzejsze widzenie'),
             (328, 171, 345, 285, 'Tarcza nerwu wzrokowego (plamka ślepa)', 'brak fotoreceptorów'),
             (370, 171, 385, 225, 'Nerw wzrokowy', ''),
         ],
         opis='Przekrój poziomy przez gałkę oczną.',
         uwaga='Pręciki odpowiadają za widzenie w słabym świetle, czopki — za widzenie barw i ostrość. Plamka ślepa nie ma fotoreceptorów.'),
]

S['b-ruch'] = [
    dict(typ='rysunek', tytul='Budowa sarkomeru', viewBox='0 -12 400 252', svg=_sark,
         znaczniki=[
             (40, 100, 14, 14, 'Linia Z', 'granica sarkomeru, zakotwiczenie aktyny'),
             (95, 48, 70, 14, 'Filament aktynowy (cienki)', ''),
             (215, 93, 320, 100, 'Filament miozynowy (gruby)', 'główki miozyny tworzą mostki poprzeczne'),
             (200, 30, 330, 14, 'Linia M', 'środek sarkomeru'),
             (200, 16, 200, 4, 'Prążek A (anizotropowy)', 'długość filamentów miozyny — nie zmienia się przy skurczu'),
             (80, 210, 20, 222, 'Prążek I (izotropowy)', 'tylko aktyna — skraca się przy skurczu'),
             (200, 222, 300, 222, 'Strefa H', 'tylko miozyna — zanika przy pełnym skurczu'),
         ],
         opis='Sarkomer — jednostka kurczliwa włókna mięśnia poprzecznie prążkowanego.',
         uwaga='Podczas skurczu długość filamentów się nie zmienia — przesuwają się względem siebie. Skracają się prążek I i strefa H, prążek A pozostaje taki sam.'),
    dict(typ='rysunek', tytul='Budowa stawu', svg=_staw,
         znaczniki=[
             (200, 120, 300, 20, 'Głowa stawowa', ''),
             (200, 230, 300, 280, 'Panewka stawowa', ''),
             (215, 152, 350, 120, 'Chrząstka stawowa', 'zmniejsza tarcie, amortyzuje'),
             (126, 167, 30, 170, 'Torebka stawowa', 'zamyka jamę stawową'),
             (200, 174, 40, 250, 'Jama stawowa z mazią', 'maź zmniejsza tarcie'),
             (289, 165, 370, 200, 'Więzadło', 'wzmacnia staw'),
         ],
         opis='Schemat budowy stawu maziowego.',
         uwaga='Chrząstka stawowa nie ma naczyń krwionośnych — odżywia ją maź stawowa, dlatego słabo się regeneruje.'),
]

S['b-oddychanie-czl'] = [
    dict(typ='rysunek', tytul='Pęcherzyk płucny i naczynie włosowate', svg=_pech,
         znaczniki=[
             (150, 30, 60, 40, 'Oskrzelik', 'doprowadza powietrze'),
             (95, 210, 40, 270, 'Ściana pęcherzyka', 'nabłonek jednowarstwowy płaski — krótka droga dyfuzji'),
             (150, 110, 150, 30, 'Światło pęcherzyka', 'powietrze bogate w O₂'),
             (247, 135, 330, 135, 'Naczynie włosowate', 'ściana z jednej warstwy komórek'),
             (247, 210, 330, 220, 'Erytrocyt', 'transportuje tlen związany z hemoglobiną'),
             (215, 124, 200, 85, 'Kierunek dyfuzji tlenu', 'z pęcherzyka do krwi'),
         ],
         opis='Wymiana gazowa między powietrzem a krwią.',
         uwaga='Gazy dyfundują zgodnie z gradientem ciśnień parcjalnych: O₂ z pęcherzyka do krwi, CO₂ z krwi do pęcherzyka.'),
]

S['b-odzywianie'] = [
    dict(typ='rysunek', tytul='Kosmek jelitowy', svg=_kos,
         znaczniki=[
             (127, 230, 40, 230, 'Nabłonek jednowarstwowy walcowaty', 'wchłanianie'),
             (200, 18, 120, 10, 'Mikrokosmki (rąbek szczoteczkowy)', 'zwiększają powierzchnię wchłaniania'),
             (127, 170, 40, 150, 'Komórka kubkowa', 'wydziela śluz'),
             (200, 125, 330, 60, 'Sieć naczyń włosowatych', 'wchłanianie cukrów i aminokwasów'),
             (200, 200, 330, 200, 'Naczynie chłonne (limfatyczne)', 'wchłanianie tłuszczów'),
             (160, 270, 70, 290, 'Tętniczka', ''),
             (240, 270, 330, 290, 'Żyłka', 'krew płynie do żyły wrotnej wątroby'),
         ],
         opis='Przekrój podłużny przez kosmek jelita cienkiego.',
         uwaga='Produkty trawienia tłuszczów trafiają do naczyń chłonnych, a cukry i aminokwasy — do krwi i żyłą wrotną do wątroby.'),
]

S['b-skora'] = [
    dict(typ='rysunek', tytul='Budowa skóry', viewBox='0 -8 400 308', svg=_skora,
         znaczniki=[
             (40, 45, 20, 15, 'Naskórek', 'nabłonek wielowarstwowy płaski rogowaciejący'),
             (40, 130, 20, 110, 'Skóra właściwa', 'tkanka łączna z naczyniami, receptorami, gruczołami'),
             (68, 252, 20, 290, 'Tkanka podskórna', 'tłuszcz — izolacja i magazyn energii'),
             (120, 20, 60, 8, 'Włos', ''),
             (113, 160, 60, 180, 'Mieszek włosowy', ''),
             (145, 105, 200, 100, 'Gruczoł łojowy', 'natłuszcza włos i naskórek'),
             (160, 88, 210, 70, 'Mięsień przywłośny', 'stroszy włos („gęsia skórka”)'),
             (262, 225, 300, 285, 'Gruczoł potowy', 'termoregulacja i wydalanie'),
             (220, 196, 220, 150, 'Naczynie krwionośne', 'termoregulacja przez zwężanie i rozszerzanie'),
             (330, 240, 380, 200, 'Ciałko blaszkowate', 'receptor ucisku i wibracji'),
             (320, 68, 380, 100, 'Ciałko dotykowe', 'receptor dotyku'),
         ],
         opis='Przekrój przez skórę owłosioną.',
         uwaga='Naskórek nie ma naczyń krwionośnych — odżywia się przez dyfuzję ze skóry właściwej.'),
]

S['b-rozmnazanie'] = [
    dict(typ='rysunek', tytul='Budowa plemnika', viewBox='0 0 400 160', svg=_plem,
         znaczniki=[
             (24, 80, 20, 140, 'Akrosom', 'enzymy rozpuszczające osłonki komórki jajowej'),
             (68, 80, 80, 140, 'Jądro', 'haploidalny materiał genetyczny'),
             (62, 54, 62, 14, 'Główka', ''),
             (111, 80, 120, 140, 'Szyjka', 'centriola'),
             (150, 72, 160, 14, 'Wstawka', 'mitochondria — energia do ruchu'),
             (300, 80, 300, 140, 'Witka (ogonek)', 'ruch'),
         ],
         opis='Schemat budowy plemnika człowieka.',
         uwaga='Mitochondria plemnika zwykle nie trafiają do zygoty — dlatego DNA mitochondrialne dziedziczy się po matce.'),
]
