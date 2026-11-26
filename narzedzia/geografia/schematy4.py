# Schematy geografii — porcja 4 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}

S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Fen — przekrój przez góry',
      svg=('<rect class="gn" x="40" y="10" width="355" height="262"/>'
           # oś wysokości
           '<path class="s" d="M40 272 V14"/>'
           + ''.join(f'<path class="s2" d="M36 {272 - h * 0.1:.0f} H40"/><text class="ts" x="33" y="{275 - h * 0.1:.0f}" text-anchor="end">{h}</text>' for h in (0, 500, 1000, 1500, 2000))
           + '<text class="ts" x="8" y="12">m n.p.m.</text>'
           # poziom kondensacji
           '<path class="dash" d="M40 152 H395"/><text class="ts" x="44" y="164">poziom kondensacji 1200 m</text>'
           # góry: tło i pierwszy plan
           '<path class="gs2" d="M40 272 L40 205 L95 188 L150 120 L190 70 L215 52 L240 75 L285 140 L330 180 L395 190 L395 272 Z"/>'
           '<path class="gs" d="M40 272 L40 212 L100 195 L155 128 L196 76 L215 58 L236 80 L280 148 L330 188 L395 197 L395 272 Z"/>'
           '<path style="fill:#fff" d="M196 76 L215 58 L236 80 L226 84 L215 76 L205 86 Z" opacity="0.9"/>'
           '<path class="gf2" d="M40 272 L40 212 L100 195 L130 160 L140 170 L110 205 L40 228 Z" opacity="0.8"/>'
           '<path class="gf2" d="M395 272 L395 197 L330 188 L300 165 L292 178 L330 200 L395 215 Z" opacity="0.8"/>'
           # chmury i opad po stronie dowietrznej
           '<path class="gk" d="M118 150 q-14 0 -14 -12 q0 -12 14 -12 q4 -14 20 -12 q10 -12 24 -2 q16 0 16 13 q0 13 -16 13 Z"/>'
           '<path class="gk" d="M150 112 q-12 0 -12 -10 q0 -10 12 -10 q4 -12 18 -10 q10 -9 20 0 q12 1 12 11 q0 9 -12 9 Z"/>'
           + ''.join(f'<path class="cold" style="stroke-width:1.2" d="M{x} {y} l-4 12"/>' for x, y in ((112, 154), (124, 156), (136, 154), (148, 156), (160, 154), (158, 116), (170, 118)))
           # droga powietrza
           + '<path class="cold" d="M48 228 L104 208"/><path class="cold" d="M104 208 L150 150 L198 64" style="stroke-dasharray:6 3"/>'
           '<path class="hot" d="M232 64 L285 140 L345 198 L378 205"/><path class="hotf" d="M378 205 l-10 -7 l1 11 Z"/>'
           '<path class="s2" d="M198 64 Q215 40 232 64"/>'
           # punkty pomiarowe
           '<rect class="f" x="46" y="234" width="88" height="18" rx="4"/><text class="tb" x="90" y="247" text-anchor="middle">700 m · 10°C</text>'
           '<rect class="f" x="170" y="20" width="90" height="18" rx="4"/><text class="tb" x="215" y="33" text-anchor="middle">2200 m · −1°C</text>'
           '<rect class="f" x="300" y="222" width="90" height="18" rx="4"/><text class="tb" x="345" y="235" text-anchor="middle">850 m · 12,5°C</text>'
           # miasteczko
           '<path class="f" d="M352 197 h10 v-8 l5 -5 l5 5 v8 h8 v-6 l4 -4 l4 4 v6 Z"/>'
           '<text class="ts" x="70" y="290" text-anchor="middle">strona dowietrzna</text><text class="ts" x="345" y="290" text-anchor="middle">strona zawietrzna</text>'),
      znaczniki=[(76, 218, 150, 262, 'Wznoszenie suche', 'Do poziomu kondensacji powietrze ochładza się o 1°C/100 m (10°C → 5°C)'),
                 (128, 140, 150, 178, 'Chmury i opady', 'Powyżej 1200 m ochładzanie tylko o ok. 0,6°C/100 m — ciepło kondensacji (5°C → −1°C)'),
                 (215, 58, 290, 60, 'Grzbiet', 'Powietrze straciło większość wilgoci'),
                 (290, 145, 305, 112, 'Opadanie', 'Suche powietrze ogrzewa się o 1°C/100 m na całej drodze w dół'),
                 (362, 192, 340, 150, 'Ciepły, suchy wiatr', 'W dolinie o 2,5°C cieplej niż na tej samej wysokości po drugiej stronie — fen (w Tatrach halny)')],
      opis='Mechanizm wiatru fenowego z obliczeniem temperatur (przykład autorski).',
      uwaga='Algorytm: 1) wznoszenie do poziomu kondensacji 1°C/100 m, 2) dalej 0,6°C/100 m do grzbietu, 3) opadanie 1°C/100 m. Wynik zawsze sprawdzaj: po zawietrznej musi być cieplej.'),
]

import math


def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')


def _panel(x0, dzien):
    """Panel bryzy: ląd po lewej, morze po prawej (szer. 190)."""
    o = f'<rect class="gn" x="{x0}" y="20" width="190" height="210"/>'
    o += f'<path class="gl" d="M{x0} 230 V186 Q{x0 + 50} 182 {x0 + 95} 190 V230 Z"/><rect class="gw2" x="{x0 + 95}" y="190" width="95" height="40"/>'
    o += ''.join(f'<path class="cold" style="stroke-width:1.2" d="M{x0 + 105 + i * 20} 196 q5 -4 10 0"/>' for i in range(4))
    o += f'<path class="f" d="M{x0 + 20} 186 v-10 l6 -6 l6 6 v10 Z"/><path class="gf2" d="M{x0 + 50} 186 l-6 0 l6 -14 l6 14 Z"/>'
    if dzien:
        o += f'<circle class="gm2" cx="{x0 + 165}" cy="42" r="11"/>'
        o += strz(x0 + 140, 175, x0 + 60, 175) + strz(x0 + 45, 168, x0 + 45, 90) + strz(x0 + 60, 80, x0 + 140, 80) + strz(x0 + 150, 90, x0 + 150, 165)
        ln, mo = ('N', '28°C'), ('W', '18°C')
    else:
        o += f'<path class="gk" d="M{x0 + 160} 32 a12 12 0 1 0 12 16 a9 9 0 1 1 -12 -16 Z"/>'
        o += strz(x0 + 60, 175, x0 + 140, 175) + strz(x0 + 150, 168, x0 + 150, 90) + strz(x0 + 140, 80, x0 + 60, 80) + strz(x0 + 45, 90, x0 + 45, 165)
        ln, mo = ('W', '12°C'), ('N', '17°C')
    o += f'<text class="tb" x="{x0 + 45}" y="215" text-anchor="middle">{ln[0]} · {ln[1]}</text><text class="tb" x="{x0 + 145}" y="215" text-anchor="middle">{mo[0]} · {mo[1]}</text>'
    o += f'<text class="tb" x="{x0 + 95}" y="250" text-anchor="middle">{"DZIEŃ — bryza morska" if dzien else "NOC — bryza lądowa"}</text>'
    return o


S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Bryza dzienna i nocna',
      svg=_panel(5, True) + _panel(205, False) + '<text class="ts" x="200" y="285" text-anchor="middle">W — wyż, N — niż; temperatura podłoża po południu i przed świtem</text>',
      znaczniki=[(50, 130, 70, 120, 'Wznoszenie', 'Nad nagrzanym lądem powietrze się wznosi — niż'),
                 (100, 175, 100, 155, 'Bryza morska', 'Przy ziemi wiatr od morza ku lądowi'),
                 (355, 130, 335, 120, 'Wznoszenie', 'Nocą nad cieplejszym morzem — niż'),
                 (300, 175, 300, 155, 'Bryza lądowa', 'Przy ziemi wiatr od lądu ku morzu')],
      opis='Cyrkulacja bryzowa nad wybrzeżem w ciągu doby.',
      uwaga='Ląd nagrzewa się i stygnie szybciej niż woda. Wiatr przy ziemi wieje od wyżu do niżu, czyli od chłodniejszego podłoża ku cieplejszemu.'),
]

_Q = [90, 110, 170, 200, 130, 100, 95, 85, 70, 75, 85, 95]
_qy = lambda q: 250 - q * 1.0
_sr = sum(_Q) / 12
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Ustrój rzeki nizinnej (śnieżny)',
      svg=(''.join(f'<path class="dash" d="M50 {_qy(q):.0f} H385"/><path class="s" d="M46 {_qy(q):.0f} H50"/><text class="ts" x="44" y="{_qy(q) + 3:.0f}" text-anchor="end">{q}</text>' for q in (50, 100, 150, 200))
           + ''.join(f'<rect class="gw2" x="{55 + i * 27.5:.1f}" y="{_qy(q):.0f}" width="21" height="{q}"/>' for i, q in enumerate(_Q))
           + f'<path class="hot" d="M50 {_qy(_sr):.1f} H385" style="stroke-dasharray:6 4"/><text class="ts" x="383" y="{_qy(_sr) - 5:.0f}" text-anchor="end">średni przepływ ok. 109 m³/s</text>'
           + '<path class="s" d="M50 30 V250 H385"/>'
           + ''.join(f'<text class="ts" x="{65.5 + i * 27.5:.1f}" y="264" text-anchor="middle">{m}</text>' for i, m in enumerate('I II III IV V VI VII VIII IX X XI XII'.split()))
           + '<text class="ts" x="8" y="22">Q [m³/s]</text>'),
      znaczniki=[(148, _qy(200), 190, 40, 'Wezbranie roztopowe', 'Marzec–kwiecień: topnienie śniegu, gleba jeszcze zamarznięta'),
                 (286, _qy(70), 300, 120, 'Niżówka', 'Wrzesień: duże parowanie i transpiracja'),
                 (215, _qy(95), 240, 175, 'Lato', 'Opady nawalne dają tylko krótkie, małe wezbrania')],
      opis='Średnie miesięczne przepływy rzeki o ustroju śnieżnym (dane autorskie).',
      uwaga='Ustrój śnieżny: jedno wyraźne maksimum wiosną. Śnieżno-deszczowy: dodatkowe wezbranie letnie. Górski (np. Dunajec): wezbrania wiosną i latem.'),
]

_mc = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
       '<circle class="gt" cx="135" cy="150" r="128" style="stroke:var(--text-2);stroke-width:1"/>'
       '<circle class="gc" cx="135" cy="150" r="95" opacity="0.6"/>'
       '<circle class="gs" cx="135" cy="150" r="62"/>'
       '<circle class="gm2" cx="135" cy="150" r="28"/>'
       + ''.join(f'<path class="s2" d="M135 150 L{135 + 135 * math.cos(math.radians(a)):.0f} {150 + 135 * math.sin(math.radians(a)):.0f}"/>' for a in (20, 110, 200, 290))
       + ''.join(f'<rect class="d" x="{x}" y="{150 - h}" width="5" height="{h}"/>' for x, h in ((122, 20), (129, 28), (136, 24), (143, 16)))
       + ''.join(f'<path class="d" d="M{x} {y} h10 v-8 l-3 -3 v3 l-3 -3 v3 l-4 -3 Z" opacity="0.8"/>' for x, y in ((95, 115), (172, 190)))
       + ''.join(f'<rect class="f" x="{x}" y="{y}" width="8" height="5"/>' for x, y in ((70, 140), (78, 150), (190, 130), (200, 142), (120, 220), (130, 228)))
       + ''.join(f'<path class="f" d="M{x} {y} v-4 l3 -3 l3 3 v4 Z"/>' for x, y in ((30, 150), (40, 100), (240, 170), (230, 220), (130, 40), (150, 270)))
       # wykres cen gruntu
       + '<path class="s" d="M280 200 V285 H395"/><path class="hot" d="M282 205 C300 260 330 275 392 280"/>'
       + '<text class="ts" x="282" y="196">cena gruntu</text><text class="ts" x="393" y="296" text-anchor="end">odległość od centrum</text>')
S['g-urbanizacja'] = [
 dict(typ='rysunek', tytul='Strefy w mieście (model koncentryczny)', svg=_mc,
      znaczniki=[(135, 140, 280, 25, 'CBD', 'Centrum biznesu: biurowce, banki, handel'),
                 (100, 112, 280, 60, 'Przejściowa', 'Stara zabudowa, dawny przemysł, rewitalizacja'),
                 (205, 140, 280, 95, 'Mieszkaniowa', 'Kamienice i osiedla bloków'),
                 (238, 175, 280, 130, 'Podmiejska', 'Suburbia: domy, centra handlowe, logistyka'),
                 (300, 245, 330, 225, 'Renta', 'Ceny gruntów maleją wraz z odległością od centrum')],
      opis='Uproszczony model stref funkcjonalnych miasta (Burgessa) i spadek cen gruntu.',
      uwaga='W CBD ceny gruntu i wysokość zabudowy są największe — opłaca się tam tylko działalność o dużym dochodzie z m² (biura, banki, handel).'),
]

S['g-energetyka'] = [
 dict(typ='proces', tytul='Wybór lokalizacji elektrowni', opis='Jak odpowiadać na pytania o czynniki lokalizacji.',
      kroki=[('Węglowa', 'Blisko złóż węgla (Bełchatów, Śląsk) i dużej ilości wody chłodzącej.'),
             ('Wodna', 'Duży spadek i przepływ rzeki, dolina do zbiornika (Solina, Żarnowiec — szczytowo-pompowa).'),
             ('Wiatrowa', 'Duża średnia prędkość wiatru: wybrzeże, morze (Bałtyk), otwarte wyniesienia.'),
             ('Słoneczna', 'Duże usłonecznienie, tani grunt; w Polsce najlepiej południe i wschód.'),
             ('Jądrowa', 'Stabilne podłoże, woda chłodząca, akceptacja społeczna (planowana na Pomorzu).')],
      uwaga='Zawsze łącz czynnik z konkretnym miejscem — sam ogólnik nie daje punktu.'),
]

S['g-srodowisko'] = [
 dict(typ='proces', tytul='Efekt cieplarniany — łańcuch przyczyn i skutków', opis='Schemat do zadań o zmianach klimatu.',
      kroki=[('Emisja gazów cieplarnianych', 'CO₂ ze spalania paliw, CH₄ z hodowli i wysypisk, N₂O z nawozów.'),
             ('Wzrost ich stężenia', 'Atmosfera silniej zatrzymuje promieniowanie długofalowe Ziemi.'),
             ('Wzrost temperatury', 'Ocieplenie globalne o ok. 1,2°C od epoki przedprzemysłowej.'),
             ('Skutki w przyrodzie', 'Topnienie lodowców, wzrost poziomu morza, ekstremalne zjawiska pogodowe.'),
             ('Skutki dla człowieka', 'Susze, powodzie, migracje klimatyczne, zmiany w rolnictwie.')],
      uwaga='Naturalny efekt cieplarniany jest korzystny — bez niego średnia temperatura Ziemi wynosiłaby ok. −18°C.'),
]
