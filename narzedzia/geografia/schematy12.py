# Schematy geografii — porcja 12 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- oś czasu dziejów Ziemi ----------
_er = [(20, 140, 'gs2', 'prekambr'), (140, 240, 'gc', 'paleozoik'), (240, 310, 'gp', 'mezozoik'), (310, 380, 'gt', 'kenozoik')]
_os = ''.join(f'<rect class="{c} ol" x="{a}" y="120" width="{b - a}" height="40"/><text class="tb" x="{(a + b) / 2}" y="145" text-anchor="middle">{n}</text>' for a, b, c, n in _er)
_os += ''.join(f'<path class="s" d="M{x} 160 V170"/><text class="ts" x="{x}" y="182" text-anchor="middle">{t}</text>' for x, t in ((20, '4600'), (140, '541'), (240, '252'), (310, '66'), (380, '0')))
_os += '<text class="ts" x="200" y="198" text-anchor="middle">mln lat temu (osie er nie w skali — prekambr to ok. 88% dziejów Ziemi)</text>'
_os += ''.join(f'<path class="s2" d="M{x} 160 V165"/>' for x in (154, 168, 182, 196, 212, 226, 263, 286, 330, 352, 372))
_os += ''.join(f'<path class="d" d="M{x} 115 l-7 -14 l14 0 Z"/>' for x, y, t in ((180, 92, 'kaledońska'), (230, 70, 'hercyńska'), (350, 92, 'alpejska')))
_os += '<text class="ts" x="200" y="40" text-anchor="middle">▼ orogenezy</text>'
_os += ''.join(f'<path class="s2" d="M{x} 205 V225"/><text class="ts" x="{x}" y="{y}" text-anchor="middle">{t}</text>' for x, y, t in ((60, 238, 'pierwsze organizmy'), (215, 238, 'karbon — węgiel'), (275, 256, 'dinozaury'), (370, 274, 'człowiek')))
S['g-skaly'] = [
 dict(typ='rysunek', tytul='Oś czasu dziejów Ziemi', svg=_os,
      znaczniki=[(80, 140, 90, 40, 'Prekambr', 'Najstarsze skały — tarcze kontynentów, platforma wschodnioeuropejska'),
                 (180, 106, 130, 70, 'Kaledońska', 'Góry Skandynawskie'),
                 (230, 90, 255, 40, 'Hercyńska', 'Sudety, Ural, Appalachy; powstają złoża węgla'),
                 (275, 140, 290, 110, 'Mezozoik', 'Rozpad Pangei; wapienie jurajskie i kredowe w Polsce'),
                 (350, 106, 340, 60, 'Alpejska', 'Karpaty, Alpy, Himalaje, Andy — trwa nadal'),
                 (370, 230, 330, 285, 'Czwartorzęd', 'Zlodowacenia i pojawienie się człowieka')],
      opis='Uproszczona oś czasu er geologicznych z orogenezami i ważnymi wydarzeniami.',
      uwaga='Najmłodszą erą jest kenozoik (od 66 mln lat temu). Zasada: im młodsza orogeneza, tym wyższe i bardziej strome góry (Karpaty wyższe od starszych Sudetów).'),
]

# ---------- port i huta ----------
_ph = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
       '<path class="gw2" d="M0 190 Q120 175 200 200 Q300 230 400 215 V300 H0 Z"/>'
       '<path class="gs ol" d="M150 192 H230 V240 H150 Z"/><path class="gw2" d="M160 200 H220 V240 H160 Z"/>'
       '<path class="gs ol" d="M240 205 L320 220 L318 232 L238 217 Z"/>'
       '<path class="f ol" d="M120 260 l30 -8 l20 4 l-5 8 l-40 4 Z"/><path class="f ol" d="M300 260 l30 -8 l20 4 l-5 8 l-40 4 Z"/>'
       '<rect class="gs2" x="165" y="120" width="70" height="45"/>'
       + ''.join(f'<rect class="d" x="{x}" y="{95 - h}" width="7" height="{h + 25}"/>' for x, h in ((175, 20), (190, 30), (215, 25)))
       + '<path class="s2" d="M180 72 q8 -10 0 -20 M195 60 q8 -10 0 -20" style="fill:none"/>'
       + ''.join(f'<ellipse class="gs2 ol" cx="{x}" cy="183" rx="10" ry="5"/>' for x in (245, 268, 291))
       + '<path class="s" d="M0 140 H160 M200 165 V185 M235 140 H400" style="stroke-width:2.4"/>'
       + ''.join(f'<path class="s" d="M{x} 136 V144"/>' for x in range(10, 160, 12)) + ''.join(f'<path class="s" d="M{x} 136 V144"/>' for x in range(245, 400, 12))
       + '<path class="cold" d="M80 0 C90 60 70 120 100 185" style="stroke-width:3"/>'
       + ''.join(f'<path class="f" d="M{x} {y} v-8 l4 -4 l4 4 v8 Z"/>' for x, y in ((300, 60), (312, 70), (326, 55), (340, 75), (355, 62), (320, 90)))
       + '<text class="tb" x="330" y="40" text-anchor="middle">miasto</text><text class="tb" x="40" y="260" text-anchor="middle">morze</text>')
S['g-przemysl'] = [
 dict(typ='rysunek', tytul='Huta przy porcie morskim (plan)', svg=_ph,
      znaczniki=[(200, 142, 260, 110, 'Huta', 'Zakład przy nabrzeżu — surowce bez przeładunku na ląd'),
                 (190, 220, 110, 230, 'Port', 'Baseny i nabrzeża do rozładunku statków'),
                 (140, 262, 160, 285, 'Rudowiec', 'Import rudy żelaza (np. z Brazylii, Australii)'),
                 (268, 183, 255, 172, 'Hałdy surowców', 'Ruda i węgiel koksujący na składowiskach'),
                 (60, 140, 70, 110, 'Kolej', 'Wywóz wyrobów stalowych w głąb kraju'),
                 (320, 260, 310, 240, 'Węglowiec', 'Import węgla koksującego')],
      opis='Lokalizacja hutnictwa żelaza nad morzem — model „huty nadmorskiej” (np. Dunkierka, Taranto, Kaohsiung).',
      uwaga='Po wyczerpaniu lokalnych złóż hutnictwo przeniosło się do portów: tańszy jest import surowców drogą morską niż transport lądowy. Czynniki: port głębokowodny, wolne tereny, woda, dostęp do rynku.'),
]

# ---------- struktura eksportu Polski ----------
_ex = [('Maszyny i urządzenia', 24, 'gw2'), ('Pojazdy i części', 12, 'gs2'), ('Żywność i napoje', 13, 'gt'), ('Metale i wyroby', 9, 'gc'), ('Chemia i tworzywa', 12, 'gp'), ('Meble i inne', 30, 'gl')]
_eb = ''
for i, (n, p, c) in enumerate(sorted(_ex, key=lambda t: -t[1])):
    y = 40 + i * 36
    _eb += f'<text class="ts" x="150" y="{y + 15}" text-anchor="end">{n}</text><rect class="{c} ol" x="156" y="{y}" width="{p * 5:.0f}" height="22"/><text class="tb" x="{162 + p * 5:.0f}" y="{y + 16}">{p}%</text>'
_eb += '<path class="s" d="M156 30 V260"/>' + ''.join(f'<path class="dash" d="M{156 + v * 5:.0f} 30 V260"/><text class="ts" x="{156 + v * 5:.0f}" y="274" text-anchor="middle">{v}%</text>' for v in (10, 20, 30))
_eb += '<text class="ts" x="200" y="292" text-anchor="middle">udział w wartości eksportu (dane przybliżone)</text>'
S['g-pl-gospodarka'] = [
 dict(typ='rysunek', tytul='Struktura eksportu Polski', svg=_eb,
      znaczniki=[(306, 51, 335, 40, 'Inne', 'Meble, odzież, wyroby z drewna, papier, minerały — razem ok. 30%'),
                 (276, 87, 335, 85, 'Maszyny', 'Największa pojedyncza grupa: AGD, elektronika, baterie'),
                 (221, 123, 335, 130, 'Żywność', 'Mięso drobiowe, wyroby mleczne, słodycze, owoce')],
      opis='Główne grupy towarów w eksporcie Polski (wartości przybliżone, zaokrąglone).',
      uwaga='Polska eksportuje głównie wyroby przetworzone, a największym odbiorcą są Niemcy. Dodatnie saldo handlu daje m.in. żywność, meble i pojazdy.'),
]
