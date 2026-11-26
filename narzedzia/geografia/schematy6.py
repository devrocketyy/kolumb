# Schematy geografii — porcja 6 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- warstwy atmosfery ----------
_ky = lambda km: 280 - km * 2.6
_tx = lambda t: 175 + t * 1.25
_pr = [(15, 0), (-56, 11), (-56, 20), (-2, 50), (-90, 85), (-75, 100)]
_at = ('<rect class="gn" x="40" y="20" width="230" height="260"/>'
       f'<rect class="gw" x="40" y="{_ky(11):.0f}" width="230" height="{_ky(0) - _ky(11):.0f}" opacity="0.55"/>'
       f'<rect class="gp" x="40" y="{_ky(30):.0f}" width="230" height="{_ky(20) - _ky(30):.0f}" opacity="0.6"/>'
       + ''.join(f'<path class="dash" d="M40 {_ky(k):.0f} H270"/>' for k in (11, 50, 85))
       + ''.join(f'<path class="s" d="M36 {_ky(k):.0f} H40"/><text class="ts" x="33" y="{_ky(k) + 3:.0f}" text-anchor="end">{k}</text>' for k in (0, 20, 40, 60, 80, 100))
       + ''.join(f'<path class="s" d="M{_tx(t):.0f} 280 V284"/><text class="ts" x="{_tx(t):.0f}" y="294" text-anchor="middle">{t}</text>' for t in (-80, -40, 0))
       + '<polyline class="hot" fill="none" points="' + ' '.join(f'{_tx(t):.1f},{_ky(k):.1f}' for t, k in _pr) + '"/>'
       + ''.join(f'<circle class="hotf" cx="{_tx(t):.1f}" cy="{_ky(k):.1f}" r="2.5"/>' for t, k in _pr)
       + '<path class="s" d="M40 20 V280 H270"/>'
       f'<path class="gk" d="M110 {_ky(3):.0f} q-10 0 -10 -7 q0 -8 10 -7 q4 -9 14 -6 q9 -5 14 3 q9 1 8 8 q-1 7 -10 9 Z"/>'
       f'<path class="cold" d="M70 {_ky(95):.0f} q30 -10 60 0 q30 10 60 0" style="stroke-width:3;opacity:.7"/>'
       f'<path class="s2" d="M220 {_ky(70):.0f} l14 -14"/>'
       '<text class="ts" x="4" y="14">km</text><text class="ts" x="270" y="296" text-anchor="end">°C</text>'
       + ''.join(f'<text class="tb" x="265" y="{_ky(k):.0f}" text-anchor="end">{n}</text>' for n, k in (('troposfera', 6), ('stratosfera', 38), ('mezosfera', 70), ('termosfera', 88))))
S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Warstwy atmosfery i zmiana temperatury', svg=_at,
      znaczniki=[(_tx(15), _ky(0), 300, 270, 'Przy ziemi', 'Średnio ok. 15°C'),
                 (_tx(-56), _ky(11), 300, 225, 'Tropopauza', 'Ok. 11 km (8 km nad biegunami, 17 km nad równikiem); ok. −56°C'),
                 (150, _ky(25), 300, 180, 'Ozon', 'Ok. 20–30 km; ozon pochłania UV, więc temperatura rośnie'),
                 (_tx(-2), _ky(50), 300, 135, 'Stratopauza', 'Ok. 50 km, temperatura bliska 0°C'),
                 (_tx(-90), _ky(85), 300, 90, 'Mezopauza', 'Ok. 85 km — najzimniej, ok. −90°C'),
                 (130, _ky(95), 300, 45, 'Zorza polarna', 'W termosferze; gazy świecą pod wpływem wiatru słonecznego')],
      opis='Pionowa budowa atmosfery i przebieg temperatury (czerwona linia, wartości przybliżone).',
      uwaga='W troposferze temperatura spada średnio o 0,6°C/100 m; tu zachodzą prawie wszystkie zjawiska pogodowe i znajduje się większość masy powietrza i pary wodnej.'),
]

# ---------- krajobraz polodowcowy ----------
_pg = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gi" d="M0 70 H110 Q140 80 145 150 L0 165 Z"/>'
       + ''.join(f'<path class="s2" d="M{x} {y} l12 4"/>' for x, y in ((20, 100), (50, 120), (80, 95), (100, 130)))
       + '<path class="gl" d="M0 165 L145 150 Q155 128 172 132 L182 162 L214 154 L228 130 Q248 98 268 128 L290 172 L400 182 V300 H0 Z"/>'
       '<path class="gc" d="M228 130 Q248 98 268 128 L290 172 L214 154 Z"/>'
       '<path class="gp" d="M290 172 L400 182 V198 L290 188 Z"/>'
       + ''.join(f'<circle class="d" cx="{x}" cy="{186 + (x % 7) * 1.2:.0f}" r="1"/>' for x in range(296, 398, 9))
       + '<path class="gw ol" d="M184 160 L212 153 L206 178 L190 178 Z"/>'
       + '<path class="gs2" d="M0 230 H400 V300 H0 Z" opacity="0.7"/>'
              + strz(300, 165, 380, 172, 'cold', 8)
       + '<text class="ts" x="200" y="290" text-anchor="middle">skały starsze (podłoże)</text>')
S['g-pl-geologia'] = [
 dict(typ='rysunek', tytul='Krajobraz polodowcowy w przekroju', svg=_pg,
      znaczniki=[(60, 120, 60, 25, 'Lądolód', 'Czoło lądolodu w czasie postoju'),
                 (160, 135, 140, 100, 'Wysoczyzna', 'Morenowa — glina zwałowa spod lodu'),
                 (250, 112, 230, 60, 'Morena czołowa', 'Wał materiału usypany przy czole lądolodu'),
                 (198, 168, 160, 210, 'Jezioro rynnowe', 'Rynna wyżłobiona przez wody pod lodem'),
                 (340, 185, 320, 220, 'Sandr', 'Piaski i żwiry wód roztopowych'),
                 (340, 168, 330, 140, 'Wody roztopowe', 'Płyną od czoła lądolodu')],
      opis='Układ form polodowcowych: wysoczyzna – morena czołowa – sandr.',
      uwaga='Kolejność od strony lądolodu: wysoczyzna morenowa (z jeziorami rynnowymi), morena czołowa, sandr, a dalej pradolina. Typowe dla Pojezierzy.'),
]

# ---------- niecka artezyjska ----------
_ar = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gl" d="M0 60 Q200 140 400 60 V300 H0 Z"/>'
       '<path class="gw ol" d="M0 60 Q200 200 400 60 L400 90 Q200 235 0 90 Z"/>'
       '<path class="gs2" d="M0 90 Q200 235 400 90 V300 H0 Z"/>'
       + ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="1"/>' for x, y in ((60, 92), (110, 112), (160, 126), (240, 126), (290, 112), (340, 92), (200, 130)))
       + '<path class="s" d="M196 132 V92 M204 132 V92"/>'
       + strz(200, 95, 200, 68, 'cold', 8)
       + '<path class="cold" d="M200 68 q-10 6 -18 18 M200 68 q10 6 18 18" style="stroke-width:1.5"/>'
       + '<path class="dash" d="M0 58 H400"/>'
       + ''.join(strz(x, 28, x + 6, 48, 'cold', 5) for x in (10, 30, 360, 380))
       + '<text class="ts" x="200" y="290" text-anchor="middle">skały nieprzepuszczalne (iły)</text>')
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Wody podziemne i źródło artezyjskie', svg=_ar,
      znaczniki=[(20, 64, 60, 25, 'Obszar zasilania', 'Opady wsiąkają w odsłoniętą warstwę wodonośną'),
                 (110, 140, 120, 200, 'Warstwa wodonośna', 'Piaski lub piaskowce między skałami nieprzepuszczalnymi'),
                 (280, 110, 300, 150, 'Nadkład', 'Nieprzepuszczalny — utrzymuje wodę pod ciśnieniem'),
                 (200, 80, 230, 30, 'Studnia artezyjska', 'Woda pod ciśnieniem sama wypływa na powierzchnię'),
                 (370, 58, 340, 80, 'Poziom zasilania', 'Woda wypływa, gdy wylot leży niżej niż ten poziom')],
      opis='Niecka artezyjska — wody podziemne pod ciśnieniem hydrostatycznym (przekrój).',
      uwaga='Wody artezyjskie występują np. w niecce warszawskiej (Mazowsze) i w Wielkim Basenie Artezyjskim w Australii.'),
]

S['g-demografia'] = [
 dict(typ='proces', tytul='Czynniki migracji: wypychające i przyciągające', opis='Model push–pull do zadań o migracjach.',
      kroki=[('Czynniki wypychające (push)', 'Bezrobocie, bieda, wojna, prześladowania, klęski żywiołowe, susza.'),
             ('Czynniki przyciągające (pull)', 'Praca i wyższe płace, bezpieczeństwo, edukacja, opieka zdrowotna, rodzina.'),
             ('Przeszkody', 'Odległość, koszty, granice i wizy, bariery językowe.'),
             ('Skutki dla kraju emigracji', 'Odpływ młodych, drenaż mózgów, przekazy pieniężne od emigrantów.'),
             ('Skutki dla kraju imigracji', 'Uzupełnienie rynku pracy, odmłodzenie, różnorodność kulturowa, problemy integracji.')],
      uwaga='Zawsze rozróżniaj przyczynę po stronie kraju pochodzenia (push) i kraju docelowego (pull).'),
]

S['g-urbanizacja'] = [
 dict(typ='proces', tytul='Fazy rozwoju miasta', opis='Cykl urbanizacji wg modelu stadiów rozwoju.',
      kroki=[('Urbanizacja', 'Szybki napływ ludności do centrum miasta — industrializacja.'),
             ('Suburbanizacja', 'Ludność i usługi przenoszą się na przedmieścia; rośnie strefa podmiejska.'),
             ('Dezurbanizacja', 'Spada liczba ludności całego zespołu miejskiego, rozwijają się małe miasta.'),
             ('Reurbanizacja', 'Powrót do odnowionych centrów — rewitalizacja, gentryfikacja.')],
      uwaga='W Polsce wokół dużych miast trwa silna suburbanizacja (np. gminy wokół Warszawy, Krakowa, Wrocławia).'),
]

S['g-klimaty'] = [
 dict(typ='proces', tytul='Rozpoznawanie typu klimatu z klimatogramu', opis='Algorytm krok po kroku.',
      kroki=[('Najzimniejszy miesiąc', 'Powyżej 18°C — strefa gorąca; poniżej 0°C — klimat umiarkowany chłodny lub zimny.'),
             ('Najcieplejszy miesiąc', 'Poniżej 10°C — klimat subpolarny lub polarny.'),
             ('Półkula', 'Najcieplej w VI–VIII — półkula N; w XII–II — półkula S.'),
             ('Roczna suma opadów', 'Poniżej ok. 250 mm — klimat suchy (pustynny).'),
             ('Rozkład opadów', 'Maksimum zimą — śródziemnomorski; latem — monsunowy lub kontynentalny; cały rok — równikowy lub morski.'),
             ('Amplituda', 'Mała — morski; duża — kontynentalny.')],
      uwaga='Pamiętaj, że na półkuli S zima przypada na czerwiec–sierpień.'),
]
