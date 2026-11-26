# Schematy geografii — porcja 4 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}

S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Fen — przekrój przez góry',
      svg=('<path class="f2" d="M20 270 L120 220 L200 70 L280 230 L380 260 L380 290 L20 290 Z"/>'
           '<path class="s2" d="M30 250 L110 205 L190 70 M210 70 L290 215 L370 245"/>'
           '<path class="s2" d="M360 238 L370 245 L358 250"/>'
           '<ellipse class="d" cx="150" cy="130" rx="45" ry="22"/>'
           '<path class="dash" d="M90 150 l-6 18 M110 152 l-6 18 M130 152 l-6 18"/>'
           '<text class="t" x="20" y="235">10°C</text><text class="t" x="180" y="55">−1°C</text><text class="t" x="330" y="230">12,5°C</text>'),
      znaczniki=[(70, 228, 40, 200, 'Strona dowietrzna', 'Powietrze wznosi się i ochładza'),
                 (150, 130, 95, 100, 'Chmury i opady', 'Kondensacja — ciepło kondensacji spowalnia ochładzanie (ok. 0,6°C/100 m)'),
                 (200, 70, 240, 60, 'Grzbiet', 'Powietrze traci większość wilgoci'),
                 (300, 220, 300, 190, 'Strona zawietrzna', 'Suche powietrze opada i ogrzewa się o 1°C/100 m'),
                 (360, 245, 330, 275, 'Ciepły, suchy wiatr', 'Fen (w Tatrach — halny)')],
      opis='Mechanizm powstawania wiatru fenowego.',
      uwaga='Na maturze liczysz temperaturę: najpierw wznoszenie (sucho- i wilgotnoadiabatyczne), potem opadanie 1°C/100 m.'),
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
