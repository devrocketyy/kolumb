# Schematy geografii — porcja 2 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}


def klimatogram(temp, opady, tmin=-20, tmax=30, pmax=300):
    """Słupki opadów (mm) i linia temperatury (°C) dla 12 miesięcy w polu 50–370 × 40–260."""
    x0, x1, y0, y1 = 50, 370, 260, 40
    w = (x1 - x0) / 12
    out = f'<path class="s" d="M{x0} {y1} V{y0} H{x1} V{y1}"/>'
    for i, p in enumerate(opady):
        h = (y0 - y1) * p / pmax
        out += f'<rect class="f" x="{x0 + i * w + 3:.1f}" y="{y0 - h:.1f}" width="{w - 6:.1f}" height="{h:.1f}"/>'
    pts = ' '.join(f'{x0 + (i + 0.5) * w:.1f},{y0 - (y0 - y1) * (t - tmin) / (tmax - tmin):.1f}' for i, t in enumerate(temp))
    out += f'<polyline class="s2" fill="none" points="{pts}"/>'
    y_zero = y0 - (y0 - y1) * (0 - tmin) / (tmax - tmin)
    out += f'<path class="dash" d="M{x0} {y_zero:.1f} H{x1}"/><text class="t" x="20" y="{y_zero + 4:.1f}">0°C</text>'
    for i, m in enumerate('IFMAMJJASOND'):
        out += f'<text class="t" x="{x0 + (i + 0.3) * w:.1f}" y="278">{m}</text>'
    return out


def ty(t, tmin=-20, tmax=30):
    return 260 - 220 * (t - tmin) / (tmax - tmin)


S['g-klimaty'] = [
 dict(typ='rysunek', tytul='Klimatogram: klimat równikowy wilgotny',
      svg=klimatogram([27, 27, 27, 27, 27, 26, 26, 26, 27, 27, 27, 27], [250, 230, 260, 280, 240, 180, 170, 180, 200, 240, 260, 270]),
      znaczniki=[(80, ty(27), 70, 30, 'Temperatura', 'Ok. 26–27°C przez cały rok — amplituda ok. 1°C'),
                 (210, 120, 210, 25, 'Opady', 'Obfite w każdym miesiącu, suma ponad 2500 mm'),
                 (200, ty(0), 300, ty(0) - 8, 'Brak termicznej zimy', 'Temperatura nigdy nie spada w pobliże 0°C')],
      opis='Rozpoznawanie klimatu z wykresu temperatury i opadów.',
      uwaga='Mała amplituda + duże opady przez cały rok = klimat równikowy wilgotny.'),
 dict(typ='rysunek', tytul='Klimatogram: klimat śródziemnomorski',
      svg=klimatogram([10, 11, 13, 15, 19, 23, 26, 26, 23, 19, 14, 11], [80, 70, 55, 40, 25, 8, 2, 4, 25, 60, 85, 90]),
      znaczniki=[(240, ty(26), 260, 30, 'Gorące lato', 'Średnio ponad 22°C w lipcu i sierpniu'),
                 (210, 255, 250, 235, 'Susza letnia', 'Najmniej opadów w porze najcieplejszej'),
                 (355, 215, 340, 195, 'Wilgotna zima', 'Najwięcej opadów od listopada do stycznia'),
                 (70, ty(10), 90, ty(10) + 25, 'Łagodna zima', 'Brak średnich miesięcznych poniżej 0°C')],
      opis='Klimat strefy podzwrotnikowej z suchym latem.',
      uwaga='Na półkuli N suche lato przypada na VI–VIII — wtedy dominuje wyż zwrotnikowy.'),
]

S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Dolina rzeczna V i dolina lodowcowa U',
      svg=('<path class="f" d="M20 60 L100 240 L120 240 L190 60 Z" opacity="0.5"/><path class="s" d="M20 60 L100 240 L120 240 L190 60"/>'
           '<path class="f" d="M210 60 C210 230 240 240 295 240 C350 240 380 230 380 60 Z" opacity="0.5"/>'
           '<path class="s" d="M210 60 C210 230 240 240 295 240 C350 240 380 230 380 60"/>'
           '<path class="s2" d="M100 240 H120"/><text class="t" x="85" y="275">V</text><text class="t" x="290" y="275">U</text>'),
      znaczniki=[(110, 240, 140, 255, 'Rzeka w dnie doliny V', 'Erozja wgłębna w górnym biegu'),
                 (60, 150, 30, 160, 'Strome zbocza V', 'Wąskie dno, przekrój klinowy'),
                 (295, 240, 330, 260, 'Szerokie płaskie dno', 'Wyżłobione przez lodowiec'),
                 (215, 150, 245, 130, 'Strome ściany U', 'Żłób lodowcowy, np. Dolina Pięciu Stawów')],
      opis='Porównanie przekrojów doliny rzecznej i lodowcowej.',
      uwaga='Kształt U jest dowodem dawnego zlodowacenia gór, np. w Tatrach.'),
 dict(typ='rysunek', tytul='Meander i starorzecze',
      svg=('<path class="s2" d="M20 150 C80 60 140 60 160 150 C180 240 240 240 260 150 C280 60 340 60 380 150"/>'
           '<path class="s2" d="M300 230 C340 230 360 260 330 275 C300 290 270 260 300 230" fill="none"/>'
           '<path class="dash" d="M120 75 L100 60 M200 225 L220 240"/>'),
      znaczniki=[(90, 78, 60, 40, 'Brzeg wklęsły', 'Erozja — prąd uderza w brzeg, powstaje podcięcie'),
                 (125, 130, 110, 160, 'Brzeg wypukły', 'Akumulacja — łacha piaszczysta'),
                 (210, 215, 240, 205, 'Zakole', 'Meander przesuwa się z biegiem rzeki'),
                 (330, 275, 360, 290, 'Starorzecze', 'Odcięte zakole, jezioro w dolinie')],
      opis='Kręty bieg rzeki nizinnej.',
      uwaga='Na brzegu wklęsłym przeważa erozja, na wypukłym — akumulacja.'),
 dict(typ='rysunek', tytul='Wydma paraboliczna i barchan',
      svg=('<path class="f" d="M40 90 C80 40 160 40 180 90 C150 70 110 70 80 90 L40 90 Z"/>'
           '<path class="f" d="M220 210 C260 260 340 260 360 210 C330 230 290 230 260 210 L220 210 Z"/>'
           '<path class="s2" d="M110 170 V110"/><path class="s2" d="M100 122 L110 105 L120 122"/>'
           '<path class="s2" d="M290 200 V140"/><path class="s2" d="M280 152 L290 135 L300 152"/>'),
      znaczniki=[(110, 55, 110, 25, 'Wydma paraboliczna', 'Ramiona skierowane pod wiatr — wybrzeża (Mierzeja Łebska)'),
                 (290, 245, 290, 280, 'Barchan', 'Ramiona skierowane z wiatrem — pustynie'),
                 (110, 150, 70, 160, 'Wiatr (parabola)', 'Wieje od strony ramion ku czołu wydmy'),
                 (290, 180, 330, 175, 'Wiatr (barchan)', 'Wieje od strony czoła ku ramionom')],
      opis='Kształt wydmy wskazuje kierunek wiatru.',
      uwaga='Najczęstsze pytanie: w którą stronę wiał wiatr. Ramiona barchanu „uciekają” z wiatrem.'),
]

S['g-pl-wody'] = [
 dict(typ='rysunek', tytul='Mierzeja i zalew',
      svg=('<path class="f2" d="M20 280 L20 180 C100 170 160 200 220 180 C280 160 340 190 380 180 L380 280 Z" opacity="0.4"/>'
           '<path class="f" d="M20 140 C120 130 260 130 380 140 L380 150 C260 142 120 142 20 152 Z"/>'
           '<path class="s2" d="M40 165 C120 158 260 158 360 165"/><path class="dash" d="M20 40 H380"/>'),
      znaczniki=[(200, 140, 200, 115, 'Mierzeja', 'Wał piasku usypany przez prądy przybrzeżne'),
                 (200, 165, 240, 170, 'Zalew', 'Odcięty fragment zatoki, wody wysłodzone przez rzeki'),
                 (200, 80, 200, 60, 'Morze otwarte', 'Bałtyk'),
                 (120, 230, 80, 255, 'Ląd i ujście rzeki', 'Rzeka zasila zalew wodą słodką')],
      opis='Wybrzeże akumulacyjne — np. Mierzeja Wiślana i Zalew Wiślany.',
      uwaga='Mierzeje i zalewy powstają w wyniku akumulacji morskiej, nie abrazji.'),
]

S['g-struktura'] = [
 dict(typ='rysunek', tytul='Piramidy wieku: młode i starzejące się społeczeństwo',
      svg=('<path class="s" d="M100 40 V270 M300 40 V270"/>'
           '<path class="f" d="M100 60 L110 60 L130 110 L150 160 L170 210 L185 260 L100 260 Z"/><path class="f2" d="M100 60 L90 60 L70 110 L50 160 L30 210 L15 260 L100 260 Z" opacity="0.7"/>'
           '<path class="f" d="M300 60 L320 60 L340 110 L345 160 L335 210 L320 260 L300 260 Z"/><path class="f2" d="M300 60 L285 60 L262 110 L256 160 L264 210 L278 260 L300 260 Z" opacity="0.7"/>'),
      znaczniki=[(100, 255, 100, 285, 'Szeroka podstawa', 'Dużo dzieci — wysoki przyrost naturalny (np. Nigeria)'),
                 (300, 255, 300, 285, 'Zwężona podstawa', 'Mało urodzeń — starzenie się (np. Polska, Japonia)'),
                 (340, 120, 370, 100, 'Szeroki środek i wierzchołek', 'Duży udział osób w wieku produkcyjnym i starszych'),
                 (30, 210, 20, 180, 'Mężczyźni / kobiety', 'Po obu stronach osi — struktura płci')],
      opis='Dwa typy struktury wieku ludności.',
      uwaga='Piramida „ula” lub „urny” oznacza starzenie się społeczeństwa.'),
]

S['g-biomy'] = [
 dict(typ='rysunek', tytul='Piętra roślinności w Tatrach',
      svg=('<path class="f" d="M20 280 L170 40 L230 40 L380 280 Z" opacity="0.25"/>'
           '<path class="s" d="M20 280 L170 40 L230 40 L380 280"/>'
           '<path class="dash" d="M65 208 H335 M100 152 H300 M130 104 H270 M152 69 H248"/>'),
      znaczniki=[(200, 245, 340, 255, 'Regiel dolny', 'Do ok. 1250 m — lasy mieszane, buk, jodła'),
                 (200, 180, 340, 185, 'Regiel górny', 'Do ok. 1550 m — świerk'),
                 (200, 128, 340, 130, 'Kosodrzewina', 'Do ok. 1800 m — kosówka'),
                 (200, 86, 340, 85, 'Hale', 'Do ok. 2300 m — łąki wysokogórskie'),
                 (200, 52, 340, 45, 'Turnie', 'Powyżej — skały, porosty')],
      opis='Piętrowy układ roślinności w zależności od wysokości.',
      uwaga='Granice pięter są wyżej na stokach południowych i niżej na północnych.'),
]
