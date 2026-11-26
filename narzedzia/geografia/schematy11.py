# Schematy geografii — porcja 11 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- profil podłużny rzeki ----------
_pp = [(0, 1200), (20, 900), (50, 600), (90, 380), (140, 250), (200, 170), (270, 110), (350, 60), (440, 25), (520, 5), (560, 0)]
_px = lambda km: 40 + km * 0.62
_py = lambda h: 250 - h * 0.17
_pr = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       + f'<polygon class="gl" points="40,250 ' + ' '.join(f'{_px(k):.0f},{_py(h):.0f}' for k, h in _pp) + ' 387,250"/>'
       + '<polyline class="cold" fill="none" style="stroke-width:3" points="' + ' '.join(f'{_px(k):.0f},{_py(h):.0f}' for k, h in _pp) + '"/>'
       + '<rect class="gw2" x="387" y="245" width="13" height="10"/>'
       + ''.join(f'<path class="dash" d="M{_px(k):.0f} 30 V250"/>' for k in (90, 350))
       + ''.join(f'<text class="tb" x="{x}" y="45" text-anchor="middle">{t}</text>' for x, t in ((68, 'bieg górny'), (175, 'bieg środkowy'), (320, 'bieg dolny')))
       + '<path class="s" d="M40 30 V250 H390"/>'
       + ''.join(f'<path class="s" d="M36 {_py(h):.0f} H40"/><text class="ts" x="33" y="{_py(h) + 3:.0f}" text-anchor="end">{h}</text>' for h in (0, 400, 800, 1200))
       + ''.join(f'<text class="ts" x="{_px(k):.0f}" y="264" text-anchor="middle">{k}</text>' for k in (0, 200, 400))
       + '<text class="ts" x="5" y="22">m n.p.m.</text><text class="ts" x="390" y="278" text-anchor="end">odległość od źródła [km]</text>'
       + '<text class="ts" x="200" y="294" text-anchor="middle">profil podłużny przybliżony — przewyższenie ok. ×200</text>')
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Profil podłużny rzeki', svg=_pr,
      znaczniki=[(_px(10), _py(1050), 70, 80, 'Źródło', 'W górach — duży spadek'),
                 (_px(50), _py(600), 110, 150, 'Erozja wgłębna', 'Bieg górny: dolina V, progi, wodospady'),
                 (_px(200), _py(170), 220, 120, 'Transport', 'Bieg środkowy: erozja boczna, meandry'),
                 (_px(440), _py(25), 320, 190, 'Akumulacja', 'Bieg dolny: mały spadek, osady, delta'),
                 (390, 250, 360, 225, 'Ujście', 'Baza erozyjna — poziom morza')],
      opis='Wklęsły profil podłużny rzeki od źródła do ujścia (dane umowne).',
      uwaga='Spadek rzeki maleje od źródła do ujścia, dlatego w biegu górnym przeważa erozja, a w dolnym — akumulacja. Profil wyrównany ma kształt krzywej wklęsłej.'),
]

# ---------- osuwisko ----------
_os = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gl" d="M0 70 L120 75 L330 240 L400 245 V300 H0 Z"/>'
       + ''.join(f'<path class="s2" d="M0 {y} L{120 + (y - 75) * 1.1:.0f} {y + 3} L400 {y + (245 - 75) + 0:.0f}" style="opacity:.6"/>' for y in ())
       + ''.join(f'<path class="gc" d="M0 {y} L{x1} {y + 2} L400 {y2} V{y2 + 10} L{x1} {y + 12} L0 {y + 10} Z" opacity="0.6"/>' for y, x1, y2 in ((110, 140, 275), (150, 175, 290)))
       + '<path class="gl2 ol" d="M150 98 C170 120 200 150 215 175 C235 200 250 225 300 236 L330 240 L300 220 C270 205 240 175 225 150 C210 125 180 108 150 98 Z"/>'
       + '<path class="s" d="M150 98 C160 150 210 210 300 236" style="stroke-dasharray:6 4"/>'
       + '<path class="s" d="M150 98 L158 120" style="stroke-width:2.2"/>'
       + strz(205, 140, 245, 175, 's', 8)
       + ''.join(f'<path class="gk" d="M{x} {y} q-6 0 -6 -5 q0 -6 7 -5 q3 -7 10 -5 q6 -4 10 2 q7 0 7 6 q0 5 -7 5 Z"/>' for x, y in ((50, 30), (90, 20)))
       + ''.join(f'<path class="cold" style="stroke-width:1.2" d="M{x} 38 l-3 10"/>' for x in (50, 60, 70, 90, 100, 110))
       + '<path class="f" d="M335 238 v-10 l6 -6 l6 6 v10 Z"/>'
       + '<text class="ts" x="200" y="290" text-anchor="middle">stok we fliszu karpackim po długotrwałych opadach</text>')
S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Osuwisko na stoku (przekrój)', svg=_os,
      znaczniki=[(155, 108, 120, 40, 'Nisza osuwiskowa', 'Skarpa w miejscu oderwania mas'),
                 (230, 190, 290, 150, 'Koluwium', 'Przemieszczony materiał (jęzor osuwiska)'),
                 (190, 168, 150, 210, 'Powierzchnia poślizgu', 'Nasiąknięte łupki działają jak smar'),
                 (80, 45, 100, 110, 'Opady', 'Długotrwałe deszcze nasycają skały wodą'),
                 (341, 228, 330, 190, 'Zagrożone domy', 'Osuwiska niszczą zabudowę i drogi')],
      opis='Budowa osuwiska — najczęstszego ruchu masowego w Karpatach fliszowych.',
      uwaga='Osuwiskom sprzyjają: flisz (piaskowce na łupkach), ulewy i roztopy, podcinanie stoków przez rzeki i drogi, wylesianie. Zapobiegają im drenaże, zalesianie i mury oporowe.'),
]

# ---------- bilans promieniowania ----------
_bp = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<rect class="gw" x="0" y="110" width="400" height="110" opacity="0.35"/>'
       '<rect class="gl" x="0" y="220" width="400" height="80"/>'
       '<circle class="gm2" cx="40" cy="40" r="22"/>'
       '<text class="tb" x="40" y="45" text-anchor="middle">100</text>'
       '<path class="gk" d="M160 150 q-14 0 -14 -12 q0 -13 16 -12 q6 -16 24 -12 q14 -9 24 4 q16 0 16 13 q0 12 -16 12 Z"/>'
       + strz(62, 55, 120, 210, 'hot', 9)
       + strz(150, 125, 150, 70, 's', 8) + strz(250, 210, 270, 70, 's', 8) + strz(110, 160, 90, 70, 's', 8)
       + strz(330, 215, 330, 140, 'hot', 8) + strz(330, 135, 330, 70, 'hot', 8)
       + ''.join(f'<text class="tb" x="{x}" y="{y}" text-anchor="middle">{t}</text>' for x, y, t in ((155, 62, '20'), (275, 62, '4'), (85, 62, '6'), (130, 235, '50'), (270, 165, 'pochłonięte 20'), (345, 105, 'ciepło')))
       + '<text class="ts" x="8" y="292">powierzchnia Ziemi</text><text class="ts" x="395" y="125" text-anchor="end">atmosfera</text>'
       + '<text class="ts" x="200" y="18" text-anchor="middle">przestrzeń kosmiczna</text>')
S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Bilans promieniowania słonecznego', svg=_bp,
      znaczniki=[(58, 58, 80, 100, 'Promieniowanie Słońca', '100 jednostek docierających do atmosfery'),
                 (150, 100, 190, 80, 'Odbite od chmur', 'Ok. 20 jednostek'),
                 (100, 115, 112, 172, 'Rozproszone', 'Ok. 6 — rozproszenie w atmosferze'),
                 (262, 140, 250, 200, 'Odbite od podłoża', 'Ok. 4 — zależy od albedo'),
                 (120, 210, 170, 250, 'Pochłonięte', 'Ok. 50 przez powierzchnię; ok. 20 przez atmosferę i chmury')],
      opis='Uproszczony bilans promieniowania krótkofalowego (wartości przybliżone, 100 = całe promieniowanie u górnej granicy atmosfery).',
      uwaga='Łącznie ok. 30% promieniowania jest odbijane (albedo planety). Ogrzana powierzchnia oddaje ciepło jako promieniowanie długofalowe, które gazy cieplarniane częściowo zatrzymują.'),
]

# ---------- ludność świata ----------
_ld = [(1800, 1.0), (1850, 1.26), (1900, 1.65), (1927, 2.0), (1950, 2.5), (1960, 3.0), (1974, 4.0), (1987, 5.0), (1999, 6.0), (2011, 7.0), (2022, 8.0)]
_pg = [(2022, 8.0), (2037, 9.0), (2050, 9.7), (2080, 10.3), (2100, 10.2)]
_lx = lambda r: 50 + (r - 1800) * 1.1
_ly = lambda m: 250 - m * 18
_lw = (''.join(f'<path class="dash" d="M50 {_ly(m):.0f} H380"/><text class="ts" x="44" y="{_ly(m) + 3:.0f}" text-anchor="end">{m}</text>' for m in (0, 2, 4, 6, 8, 10, 12))
       + ''.join(f'<path class="s" d="M{_lx(r):.0f} 250 V254"/><text class="ts" x="{_lx(r):.0f}" y="266" text-anchor="middle">{r}</text>' for r in (1800, 1850, 1900, 1950, 2000, 2050, 2100))
       + '<polyline class="hot" fill="none" points="' + ' '.join(f'{_lx(r):.1f},{_ly(m):.1f}' for r, m in _ld) + '"/>'
       + '<polyline class="hot" fill="none" style="stroke-dasharray:6 4" points="' + ' '.join(f'{_lx(r):.1f},{_ly(m):.1f}' for r, m in _pg) + '"/>'
       + ''.join(f'<circle class="hotf" cx="{_lx(r):.1f}" cy="{_ly(m):.1f}" r="2.5"/>' for r, m in _ld)
       + '<path class="s" d="M50 30 V250 H385"/>'
       + '<text class="ts" x="8" y="22">mld ludzi</text><text class="ts" x="215" y="286" text-anchor="middle">linia ciągła — dane, przerywana — prognoza ONZ</text>')
S['g-demografia'] = [
 dict(typ='rysunek', tytul='Liczba ludności świata 1800–2100', svg=_lw,
      znaczniki=[(_lx(1800), _ly(1.0), 70, 160, '1 mld', 'Ok. 1800 r.'),
                 (_lx(1927), _ly(2.0), 120, 120, '2 mld', 'Po ponad 120 latach'),
                 (_lx(1974), _ly(4.0), 170, 80, 'Eksplozja', 'Od 3 do 4 mld w 14 lat'),
                 (_lx(2022), _ly(8.0), 270, 60, '8 mld', 'Rok 2022'),
                 (_lx(2080), _ly(10.3), 330, 100, 'Szczyt', 'Prognoza ok. 10,3 mld w latach 2080')],
      opis='Wzrost liczby ludności świata i prognoza ONZ (wartości przybliżone).',
      uwaga='Tempo wzrostu było największe w latach 60. XX w. (ok. 2% rocznie); dziś spada, bo dzietność maleje na wszystkich kontynentach. Większość przyrostu do 2100 r. przypadnie na Afrykę.'),
]
