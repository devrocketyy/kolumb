# Schematy geografii — porcja 8 (rysunki autorskie IndexLab, standard 2.0). SVG 400×300; klasy jak w schematy1.py.
import math
def strz(x1, y1, x2, y2, cls='s', g=7):
    a = math.atan2(y2 - y1, x2 - x1)
    f = 'hotf' if cls == 'hot' else 'coldf' if cls == 'cold' else 'd'
    return (f'<path class="{cls}" d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}"/><path class="{f}" d="M{x2:.1f} {y2:.1f} '
            f'L{x2 - g * math.cos(a - 0.45):.1f} {y2 - g * math.sin(a - 0.45):.1f} L{x2 - g * math.cos(a + 0.45):.1f} {y2 - g * math.sin(a + 0.45):.1f} Z"/>')
S = {}

# ---------- prądy morskie Atlantyku Północnego ----------
_pm = ('<rect class="gw" x="0" y="0" width="400" height="300"/>'
       '<path class="gl ol" d="M0 0 H118 L140 38 L114 78 L130 118 L96 158 L72 196 L40 226 L0 236 Z"/>'
       '<ellipse class="gi" cx="160" cy="22" rx="30" ry="18"/>'
       '<path class="gl ol" d="M262 0 H400 V128 L334 120 L302 110 L282 80 L302 60 L282 30 Z"/>'
       '<path class="gl ol" d="M300 132 L400 132 V300 L332 300 L302 258 L272 220 L266 182 Z"/>'
       '<path class="gl ol" d="M92 262 L150 250 L176 300 H84 Z"/>'
       '<path class="dash" d="M0 252 H400"/><text class="ts" x="395" y="248" text-anchor="end">równik</text>'
       '<path class="dash" d="M0 175 H400" style="opacity:.6"/><text class="ts" x="395" y="171" text-anchor="end">23°27′N</text>'
       '<path class="hot" d="M95 192 C120 175 135 150 150 128 C180 100 230 80 270 62 C290 52 300 42 305 30" style="stroke-width:3.2"/>'
       '<path class="hotf" d="M305 30 l-9 2 l5 -9 Z"/>'
       '<path class="hot" d="M262 218 C220 222 170 215 110 200" style="stroke-width:2.6"/><path class="hotf" d="M110 200 l9 -4 l-2 8 Z"/>'
       '<path class="cold" d="M300 118 C292 140 280 160 276 196" style="stroke-width:3"/><path class="coldf" d="M276 200 l-4 -9 l9 1 Z"/>'
       '<path class="cold" d="M175 40 C160 55 145 70 132 96" style="stroke-width:3"/><path class="coldf" d="M130 100 l0 -10 l8 4 Z"/>'
       '<rect class="hotf" x="8" y="270" width="12" height="4"/><text class="ts" x="24" y="275">ciepły</text>'
       '<rect class="coldf" x="8" y="284" width="12" height="4"/><text class="ts" x="24" y="289">zimny</text>')
S['g-oceany'] = [
 dict(typ='rysunek', tytul='Prądy morskie Atlantyku Północnego', svg=_pm,
      znaczniki=[(140, 140, 160, 175, 'Golfsztrom', 'Ciepły — z Zatoki Meksykańskiej wzdłuż wybrzeży USA'),
                 (240, 75, 200, 110, 'Północnoatlantycki', 'Ciepły — ogrzewa Europę Zachodnią i Norwegię (porty niezamarzające)'),
                 (285, 160, 225, 150, 'Kanaryjski', 'Zimny — wzdłuż Afryki; pustynia nadbrzeżna Sahara Zachodnia'),
                 (150, 70, 190, 80, 'Labradorski', 'Zimny — z Arktyki, niesie góry lodowe'),
                 (190, 214, 170, 235, 'Pasatowy Północny', 'Ciepły — pędzony przez pasaty na zachód')],
      opis='Uproszczony układ głównych prądów Atlantyku Północnego (czerwone — ciepłe, niebieskie — zimne).',
      uwaga='Prądy w strefie zwrotnikowej tworzą wir krążący zgodnie z ruchem wskazówek zegara (półkula N). Zimne prądy wzdłuż zachodnich wybrzeży kontynentów sprzyjają pustyniom nadbrzeżnym.'),
]

# ---------- monsun ----------
def _mon(x0, lato):
    o = f'<rect class="gw2" x="{x0}" y="20" width="190" height="230"/>'
    o += f'<path class="gl ol" d="M{x0} 20 H{x0 + 190} V110 L{x0 + 140} 112 L{x0 + 110} 125 L{x0 + 95} 185 L{x0 + 80} 125 L{x0 + 50} 112 L{x0} 110 Z"/>'
    o += f'<path class="gs" d="M{x0 + 20} 60 Q{x0 + 95} 30 {x0 + 170} 60 L{x0 + 160} 70 Q{x0 + 95} 45 {x0 + 30} 70 Z"/>'
    if lato:
        o += ''.join(strz(x0 + a, 215, x0 + b, 150, 's', 8) for a, b in ((40, 60), (95, 95), (150, 130)))
        o += f'<path class="gk" d="M{x0 + 112} 112 q-10 0 -10 -8 q0 -9 11 -8 q4 -10 16 -7 q10 -6 17 3 q10 0 10 8 q0 8 -10 8 Z"/>'
        o += ''.join(f'<path class="cold" style="stroke-width:1.2" d="M{x0 + x} 118 l-3 10"/>' for x in (114, 124, 134, 144))
        o += f'<text class="tb" x="{x0 + 95}" y="90" text-anchor="middle">N</text><text class="tb" x="{x0 + 95}" y="240" text-anchor="middle">W</text>'
    else:
        o += ''.join(strz(x0 + b, 150, x0 + a, 215, 's', 8) for a, b in ((40, 60), (95, 95), (150, 130)))
        o += f'<text class="tb" x="{x0 + 95}" y="90" text-anchor="middle">W</text><text class="tb" x="{x0 + 95}" y="240" text-anchor="middle">N</text>'
    o += f'<text class="tb" x="{x0 + 95}" y="268" text-anchor="middle">{"LATO — monsun letni" if lato else "ZIMA — monsun zimowy"}</text>'
    return o


S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Monsun letni i zimowy w Azji Południowej',
      svg=_mon(5, True) + _mon(205, False) + '<text class="ts" x="200" y="290" text-anchor="middle">W — wyż, N — niż; strzałki — kierunek wiatru przy ziemi</text>',
      znaczniki=[(115, 88, 130, 32, 'Niż nad lądem', 'Latem ląd się nagrzewa — powstaje niż'),
                 (115, 238, 140, 225, 'Wyż nad oceanem', 'Chłodniejszy ocean latem'),
                 (130, 108, 150, 150, 'Ulewy', 'Wilgotne powietrze znad oceanu — pora deszczowa (VI–IX)'),
                 (312, 88, 290, 62, 'Wyż azjatycki', 'Zimą wychłodzony ląd — suche wiatry od lądu')],
      opis='Sezonowa zmiana kierunku wiatrów nad Azją Południową (schemat).',
      uwaga='Monsun wynika z różnic w nagrzewaniu lądu i oceanu oraz przesuwania się strefy zbieżności. Najwyższe opady na świecie notuje się na stokach Himalajów i wzgórz Khasi (Czerrapundżi).'),
]

# ---------- El Niño ----------
def _pac(x0, nino):
    o = f'<rect class="gn" x="{x0}" y="20" width="190" height="80"/><rect class="gw2" x="{x0}" y="100" width="190" height="140"/>'
    o += f'<path class="gl ol" d="M{x0} 100 L{x0 + 22} 100 L{x0 + 18} 240 L{x0} 240 Z"/><path class="gl ol" d="M{x0 + 190} 100 L{x0 + 168} 100 L{x0 + 174} 240 L{x0 + 190} 240 Z"/>'
    if not nino:
        o += f'<path class="gm2" d="M{x0 + 22} 100 L{x0 + 168} 100 L{x0 + 168} 108 Q{x0 + 90} 125 {x0 + 20} 165 Z" opacity="0.85"/>'
        o += f'<path class="dash" d="M{x0 + 20} 168 Q{x0 + 90} 128 {x0 + 168} 110"/>'
        o += ''.join(strz(x0 + a, 70, x0 + a - 40, 70, 's', 7) for a in (110, 165))
        o += f'<path class="gk" d="M{x0 + 30} 60 q-8 0 -8 -7 q0 -7 9 -7 q3 -8 13 -6 q8 -5 13 2 q8 0 8 7 q0 7 -8 7 Z"/>'
        o += strz(x0 + 150, 140, x0 + 150, 112, 'cold', 6)
    else:
        o += f'<path class="gm2" d="M{x0 + 22} 100 L{x0 + 168} 100 L{x0 + 168} 132 Q{x0 + 90} 138 {x0 + 20} 140 Z" opacity="0.85"/>'
        o += f'<path class="dash" d="M{x0 + 20} 143 Q{x0 + 90} 141 {x0 + 168} 135"/>'
        o += strz(x0 + 60, 70, x0 + 100, 70, 's', 7)
        o += f'<path class="gk" d="M{x0 + 140} 60 q-8 0 -8 -7 q0 -7 9 -7 q3 -8 13 -6 q8 -5 13 2 q8 0 8 7 q0 7 -8 7 Z"/>'
    o += f'<text class="tb" x="{x0 + 95}" y="258" text-anchor="middle">{"El Niño" if nino else "warunki normalne"}</text>'
    o += f'<text class="ts" x="{x0 + 4}" y="275">Australia</text><text class="ts" x="{x0 + 186}" y="275" text-anchor="end">Peru</text>'
    return o


S['g-oceany'].append(
 dict(typ='rysunek', tytul='Warunki normalne i El Niño na Pacyfiku', svg=_pac(5, False) + _pac(205, True) + '<text class="ts" x="200" y="292" text-anchor="middle">przekrój wzdłuż równika; linia przerywana — termoklina</text>',
      znaczniki=[(80, 70, 60, 30, 'Pasaty', 'Silne — spychają ciepłą wodę na zachód'),
                 (60, 120, 70, 200, 'Ciepła woda', 'Gromadzi się przy Indonezji — opady'),
                 (155, 126, 120, 160, 'Upwelling', 'Zimne wody wypływają przy Peru — bogate łowiska'),
                 (285, 70, 270, 30, 'Osłabienie pasatów', 'Ciepła woda przesuwa się na wschód'),
                 (360, 60, 345, 160, 'Ulewy w Peru', 'Powodzie w Ameryce Płd., susze w Australii i Indonezji')],
      opis='Przekrój przez równikowy Pacyfik w warunkach normalnych i w czasie El Niño.',
      uwaga='El Niño występuje co 2–7 lat. Zanika upwelling przy Peru — spadają połowy sardeli; w Australii i Indonezji susze i pożary, w Peru i Ekwadorze ulewy i powodzie.'))

# ---------- terasy rzeczne ----------
_tr = ('<rect class="gn" x="0" y="0" width="400" height="300"/>'
       '<path class="gl" d="M0 60 L40 62 L60 100 L110 102 L125 150 L165 152 L175 200 L225 200 L235 152 L275 150 L290 102 L340 100 L360 62 L400 60 V300 H0 Z"/>'
       '<path class="gp" d="M60 100 L110 102 L112 112 L62 110 Z M290 102 L340 100 L338 110 L288 112 Z M125 150 L165 152 L166 162 L126 160 Z M235 152 L275 150 L274 160 L234 162 Z M175 200 L225 200 L225 212 L175 212 Z"/>'
       '<path class="gw2" d="M188 200 H212 L208 210 H192 Z"/>'
       '<path class="s" d="M0 60 L40 62 L60 100 L110 102 L125 150 L165 152 L175 200 L225 200 L235 152 L275 150 L290 102 L340 100 L360 62 L400 60"/>'
       '<path class="gs2" d="M0 240 H400 V300 H0 Z" opacity="0.6"/>'
       '<path class="s" d="M385 200 V60"/>' + ''.join(f'<path class="s" d="M381 {y} H385"/><text class="ts" x="378" y="{y + 3}" text-anchor="end">{h}</text>' for y, h in ((200, 0), (152, 5), (101, 15), (61, 30)))
       + '<text class="ts" x="395" y="50" text-anchor="end">m nad rzeką</text>'
       '<path class="dash" d="M150 185 H250"/><text class="ts" x="200" y="182" text-anchor="middle">zasięg wezbrań</text>')
S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Terasy rzeczne w przekroju doliny', svg=_tr,
      znaczniki=[(200, 205, 230, 240, 'Koryto', 'Rzeka w dnie doliny'),
                 (215, 200, 270, 185, 'Terasa zalewowa', 'Zalewana w czasie wezbrań'),
                 (145, 151, 90, 140, 'Terasa I', 'Nadzalewowa — dawne dno doliny'),
                 (85, 101, 100, 75, 'Terasa II', 'Starsza i wyżej położona'),
                 (50, 82, 60, 30, 'Zbocze doliny', 'Krawędź wysoczyzny'),
                 (90, 108, 140, 125, 'Aluwia', 'Osady rzeczne budujące terasy')],
      opis='Przekrój doliny z terasami (wysokości umowne).',
      uwaga='Terasy powstają, gdy rzeka na przemian akumuluje osady i wcina się w nie (np. po obniżeniu poziomu morza lub wypiętrzeniu terenu). Im wyżej terasa, tym jest starsza.'),
]

# ---------- uskok przesuwczy ----------
_up = ('<rect class="gt" x="0" y="0" width="400" height="300"/>'
       '<path class="gl" d="M0 0 H180 L230 300 H0 Z" opacity="0.6"/>'
       '<path class="s" d="M180 0 L230 300" style="stroke-width:2.6"/>'
       '<path class="s2" d="M0 120 H197 M209 175 H400" style="stroke-width:6"/><path class="f" d="M0 118 H197 V122 H0 Z M209 173 H400 V177 H209 Z" style="stroke:none"/>'
       '<path class="cold" d="M20 230 C80 220 140 215 205 210" style="stroke-width:3"/><path class="cold" d="M219 265 C280 262 340 270 400 268" style="stroke-width:3"/>'
       + strz(120, 40, 120, 90, 's', 9) + strz(300, 260, 300, 210, 's', 9)
       + '<path class="d" d="M80 60 l-8 0 l8 -16 l8 16 Z"/><path class="d" d="M300 120 l-8 0 l8 -16 l8 16 Z"/>'
       '<text class="ts" x="320" y="120">płyta pacyficzna</text><text class="ts" x="20" y="285">płyta północnoamerykańska</text>'
       '<path class="s" d="M370 30 V10" /><path class="d" d="M370 6 l-5 8 l10 0 Z"/><text class="tb" x="370" y="44" text-anchor="middle">N</text>')
S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Uskok przesuwczy (widok z góry)', svg=_up,
      znaczniki=[(195, 90, 240, 60, 'Linia uskoku', 'Granica przesuwcza — płyty mijają się poziomo'),
                 (120, 65, 140, 100, 'Ruch płyty', 'Bloki przesuwają się w przeciwnych kierunkach'),
                 (203, 150, 250, 140, 'Przesunięta droga', 'Dowód ruchu wzdłuż uskoku'),
                 (212, 240, 260, 235, 'Przesunięty ciek', 'Koryto „łamie się” na uskoku')],
      opis='Granica transformacyjna (przesuwcza) w widoku z góry — np. uskok San Andreas w Kalifornii.',
      uwaga='Na granicach przesuwczych skorupa nie powstaje ani nie znika; naprężenia rozładowują się w silnych, płytkich trzęsieniach ziemi (San Francisco 1906, Turcja 2023).'),
]

# ---------- stratyfikacja jeziora ----------
def _jez(x0, lato):
    o = f'<rect class="gn" x="{x0}" y="20" width="190" height="40"/>'
    if lato:
        o += f'<rect class="gm2" x="{x0}" y="60" width="190" height="55" opacity="0.6"/><rect class="gw" x="{x0}" y="115" width="190" height="35"/><rect class="gw2" x="{x0}" y="150" width="190" height="100"/>'
        o += f'<polyline class="hot" fill="none" points="{x0 + 160},60 {x0 + 158},115 {x0 + 80},150 {x0 + 60},250"/>'
        labs = (('22°C', 85), ('termoklina', 135), ('4°C', 200))
    else:
        o += f'<rect class="gi" x="{x0}" y="60" width="190" height="14"/><rect class="gw" x="{x0}" y="74" width="190" height="60"/><rect class="gw2" x="{x0}" y="134" width="190" height="116"/>'
        o += f'<polyline class="cold" fill="none" points="{x0 + 40},62 {x0 + 50},74 {x0 + 60},134 {x0 + 62},250"/>'
        labs = (('0°C — lód', 70), ('1–3°C', 105), ('4°C', 200))
    o += f'<path class="gg" d="M{x0} 250 H{x0 + 190} V262 H{x0} Z"/><path class="s" d="M{x0} 60 V250 H{x0 + 190} V60"/>'
    o += ''.join(f'<text class="tb" x="{x0 + 100}" y="{y + 4}" text-anchor="middle">{t}</text>' for t, y in labs)
    o += f'<text class="tb" x="{x0 + 95}" y="280" text-anchor="middle">{"LATO" if lato else "ZIMA"}</text>'
    return o


S['g-pl-wody'] = [
 dict(typ='rysunek', tytul='Termika jeziora latem i zimą', svg=_jez(5, True) + _jez(205, False) + '<text class="ts" x="200" y="296" text-anchor="middle">linia — temperatura wody w głąb jeziora</text>',
      znaczniki=[(40, 85, 60, 40, 'Epilimnion', 'Ciepła warstwa powierzchniowa, mieszana przez wiatr'),
                 (40, 135, 50, 170, 'Termoklina', 'Gwałtowny spadek temperatury z głębokością'),
                 (40, 200, 70, 230, 'Hypolimnion', 'Zimna woda przy dnie, ok. 4°C'),
                 (230, 66, 280, 40, 'Pokrywa lodowa', 'Lód jest lżejszy od wody i izoluje jezioro'),
                 (230, 200, 260, 230, 'Woda przy dnie', 'Ok. 4°C — największa gęstość wody')],
      opis='Uwarstwienie termiczne jeziora strefy umiarkowanej (wartości przybliżone).',
      uwaga='Woda ma największą gęstość w 4°C, dlatego zimą najcieplejsza jest przy dnie, a lód pływa — jeziora nie zamarzają do dna. Wiosną i jesienią następuje pełne mieszanie wód (cyrkulacja).'),
]
