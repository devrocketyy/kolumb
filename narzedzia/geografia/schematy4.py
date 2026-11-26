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

S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Bryza dzienna i nocna',
      svg=('<path class="f" d="M10 150 H190 V180 H10 Z"/><path class="s2" d="M10 150 H190" opacity="0"/>'
           '<rect class="d" x="10" y="150" width="0" height="0"/>'
           '<path d="M100 150 H190 V180 H100 Z" fill="#64b5f6"/>'
           '<path class="s" d="M150 140 H40 M50 133 L40 140 L50 147 M40 135 V60 M140 60 H40 M150 60 V135 M143 125 L150 135 L157 125"/>'
           '<text class="t" x="70" y="30">DZIEŃ</text>'
           '<path class="f" d="M210 150 H390 V180 H210 Z"/>'
           '<path d="M300 150 H390 V180 H300 Z" fill="#64b5f6"/>'
           '<path class="s" d="M240 140 H350 M340 133 L350 140 L340 147 M350 135 V60 M250 60 H350 M240 60 V135 M233 125 L240 135 L247 125"/>'
           '<text class="t" x="270" y="30">NOC</text>'),
      znaczniki=[(55, 165, 40, 210, 'Ląd w dzień', 'Nagrzewa się szybciej — powietrze wznosi się, niż'),
                 (145, 165, 140, 210, 'Morze w dzień', 'Chłodniejsze — wyż'),
                 (95, 140, 95, 120, 'Bryza morska', 'Przy ziemi wiatr od morza'),
                 (255, 165, 240, 240, 'Ląd nocą', 'Szybko się wychładza — wyż'),
                 (345, 165, 350, 240, 'Morze nocą', 'Cieplejsze — niż'),
                 (295, 140, 295, 120, 'Bryza lądowa', 'Przy ziemi wiatr od lądu')],
      opis='Cyrkulacja bryzowa nad wybrzeżem w dzień i w nocy.',
      uwaga='Wiatr zawsze wieje przy ziemi od wyżu do niżu — od chłodniejszego do cieplejszego podłoża.'),
]

S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Ustrój rzeki nizinnej (śnieżny)',
      svg=('<path class="s" d="M40 260 H380 M40 260 V30"/>'
           + ''.join(f'<rect style="fill:#64b5f6" x="{48+i*27}" y="{260-h}" width="20" height="{h}" fill="#64b5f6"/>' for i, h in enumerate([90,110,170,200,130,100,95,85,70,75,85,95]))
           + ''.join(f'<text class="t" x="{52+i*27}" y="278">{m}</text>' for i, m in enumerate('I II III IV V VI VII VIII IX X XI XII'.split()))
           + '<text class="t" x="45" y="25">przepływ</text>'),
      znaczniki=[(137, 60, 160, 40, 'Wezbranie roztopowe', 'Marzec–kwiecień: topnienie śniegu'),
                 (264, 190, 270, 150, 'Niżówka', 'Późne lato–wrzesień: parowanie i transpiracja'),
                 (210, 165, 200, 120, 'Wezbranie letnie', 'Słabe — opady nawalne')],
      opis='Średnie miesięczne przepływy rzeki o ustroju śnieżnym, dane autorskie.',
      uwaga='Ustrój deszczowo-śnieżny ma dodatkowe wyraźne wezbranie letnie; górski — maksima wiosną i latem.'),
]

S['g-urbanizacja'] = [
 dict(typ='rysunek', tytul='Strefy w mieście (model koncentryczny)',
      svg=('<circle class="d" cx="200" cy="150" r="135" fill="#e8f5e9"/>'
           '<circle cx="200" cy="150" r="100" fill="#fff9c4" stroke="#999"/>'
           '<circle cx="200" cy="150" r="65" fill="#ffe0b2" stroke="#999"/>'
           '<circle cx="200" cy="150" r="30" fill="#ef9a9a" stroke="#999"/>'
           '<text class="t" x="185" y="155">CBD</text>'),
      znaczniki=[(205, 140, 330, 30, 'CBD', 'Centrum biznesowe: biura, banki, handel'),
                 (200, 100, 370, 70, 'Strefa przejściowa', 'Stara zabudowa, przemysł, rewitalizacja'),
                 (200, 65, 370, 110, 'Strefa mieszkaniowa', 'Bloki i kamienice'),
                 (200, 25, 370, 150, 'Strefa podmiejska', 'Suburbia, domy jednorodzinne, centra handlowe')],
      opis='Uproszczony model stref funkcjonalnych miasta.',
      uwaga='Ceny gruntów i wysokość zabudowy są największe w CBD i maleją ku przedmieściom.'),
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
