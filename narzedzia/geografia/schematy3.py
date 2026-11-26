# Schematy geografii — porcja 3 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}

S['g-obiegowy'] = [
 dict(typ='rysunek', tytul='Oświetlenie Ziemi 22 czerwca',
      svg=('<circle class="d" cx="200" cy="150" r="110"/>'
           '<path class="f2" d="M200 40 A110 110 0 0 1 200 260 A60 110 0 0 0 200 40 Z" opacity="0.5"/>'
           '<path class="s" d="M200 40 A60 110 0 0 0 200 260"/>'
           '<circle class="s" cx="200" cy="150" r="110"/>'
           '<g transform="rotate(-22 200 150)"><path class="s" d="M200 30 V270"/>'
           '<path class="dash" d="M90 150 H310 M101 102 H299 M101 198 H299 M140 58 H260 M140 242 H260"/></g>'
           '<path class="s2" d="M20 150 H70 M55 140 L70 150 L55 160"/>'),
      znaczniki=[(45, 150, 30, 130, 'Promienie Słońca', 'Padają z lewej strony'),
                 (182, 106, 60, 95, 'Zwrotnik Raka', 'Słońce w zenicie — 23°27′N'),
                 (200, 60, 220, 25, 'Dzień polarny', 'Za kołem podbiegunowym N cała doba oświetlona'),
                 (200, 245, 220, 285, 'Noc polarna', 'Za kołem podbiegunowym S'),
                 (160, 140, 120, 175, 'Linia terminatora', 'Granica dnia i nocy'),
                 (200, 150, 230, 145, 'Oś Ziemi', 'Nachylona — półkula N zwrócona ku Słońcu')],
      opis='Oświetlenie Ziemi w dniu przesilenia letniego na półkuli północnej.',
      uwaga='22 czerwca na półkuli N dzień jest dłuższy niż noc, a na półkuli S — krótszy.'),
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

S['g-rzezba'] = [
 dict(typ='rysunek', tytul='Jaskinia krasowa',
      svg=('<path class="f" d="M20 60 H380 V280 H20 Z" opacity="0.35"/><path class="s" d="M20 60 H380"/>'
           '<path class="d" d="M90 170 C110 130 290 130 310 170 C300 220 110 220 90 170 Z"/>'
           '<path class="s" d="M150 140 L150 165 M175 136 L175 158 M240 138 L240 162"/>'
           '<path class="s" d="M160 212 L160 192 M230 212 L230 188"/>'
           '<path class="f2" d="M60 60 L80 100 L100 60 Z"/><path class="s2" d="M330 170 C350 180 360 200 380 205"/>'),
      znaczniki=[(80, 75, 50, 40, 'Lej krasowy', 'Zapadlisko na powierzchni'),
                 (175, 150, 190, 115, 'Stalaktyt', 'Naciek zwisający ze stropu'),
                 (230, 195, 260, 235, 'Stalagmit', 'Naciek rosnący od dna'),
                 (200, 175, 120, 190, 'Komora jaskini', 'Rozpuszczony wapień'),
                 (360, 198, 360, 230, 'Wywierzysko', 'Wypływ wody krasowej na powierzchnię')],
      opis='Formy krasu podziemnego i powierzchniowego w skałach wapiennych.',
      uwaga='Nacieki powstają, gdy z wody wytrąca się węglan wapnia: Ca(HCO₃)₂ → CaCO₃ + H₂O + CO₂.'),
 dict(typ='rysunek', tytul='Wybrzeże klifowe',
      svg=('<path class="f" d="M20 60 H230 L250 260 H20 Z" opacity="0.6"/><path class="s" d="M230 60 L250 260"/>'
           '<path class="s2" d="M250 200 H380"/><path class="f2" d="M250 240 L380 255 V280 H20 V260 H250 Z" opacity="0.4"/>'
           '<path class="d" d="M240 190 C250 200 248 215 240 220 Z"/>'),
      znaczniki=[(235, 110, 200, 90, 'Klif', 'Strome urwisko niszczone przez fale'),
                 (243, 205, 280, 180, 'Nisza abrazyjna', 'Podcięcie u podstawy klifu'),
                 (320, 200, 330, 175, 'Fale', 'Abrazja — niszczenie brzegu'),
                 (320, 250, 350, 270, 'Platforma abrazyjna', 'Zrównane dno przed klifem')],
      opis='Rzeźba wybrzeża niszczonego przez morze (np. Wolin, Orłowo).',
      uwaga='Po podcięciu niszy górna część klifu obrywa się i klif cofa się w głąb lądu.'),
 dict(typ='rysunek', tytul='Delta i estuarium',
      svg=('<path class="s2" d="M40 20 C60 80 80 110 90 140"/><path class="s2" d="M90 140 L50 260 M90 140 L90 270 M90 140 L130 260 M90 140 L160 230"/>'
           '<path class="f" d="M30 180 L170 180 L190 280 L20 280 Z" opacity="0.4"/>'
           '<path class="s2" d="M300 20 C300 100 305 150 310 170"/><path class="s" d="M290 170 L240 280 M330 170 L380 280"/>'),
      znaczniki=[(90, 140, 120, 125, 'Rozgałęzienie koryta', 'Rzeka dzieli się na odnogi'),
                 (90, 230, 40, 200, 'Delta', 'Osady narastają, ląd przyrasta — małe pływy (np. Wisła, Nil)'),
                 (310, 230, 340, 220, 'Estuarium', 'Lejkowate ujście poszerzane przez pływy (np. Tamiza)'),
                 (300, 60, 330, 50, 'Rzeka', 'Jedno koryto do ujścia')],
      opis='Dwa typy ujść rzecznych.',
      uwaga='Delta powstaje, gdy rzeka niesie dużo osadów, a pływy i prądy są słabe.'),
]

S['g-lodowce'] = [
 dict(typ='rysunek', tytul='Lodowiec górski',
      svg=('<path class="f2" d="M20 280 L120 40 L170 80 L260 60 L380 280 Z" opacity="0.3"/>'
           '<path class="d" d="M120 60 C150 100 190 110 210 140 C240 190 260 230 300 270 L340 270 C300 230 280 180 250 130 C230 100 200 80 170 80 Z"/>'
           '<path class="dash" d="M60 140 H340"/><path class="f2" d="M300 270 C320 260 340 265 345 275 Z"/>'),
      znaczniki=[(160, 85, 100, 100, 'Pole firnowe', 'Obszar zasilania w cyrku lodowcowym'),
                 (90, 140, 40, 130, 'Granica wiecznego śniegu', 'Powyżej przeważa zasilanie'),
                 (250, 190, 300, 170, 'Jęzor lodowcowy', 'Spływa doliną poniżej granicy wiecznego śniegu'),
                 (322, 268, 360, 250, 'Morena czołowa', 'Wał osadów przed czołem lodowca')],
      opis='Budowa lodowca dolinnego.',
      uwaga='Po zaniku lodowca zostaje cyrk (kar) z jeziorem i dolina w kształcie U.'),
]

S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Subdukcja na granicy płyt',
      svg=('<path class="f" d="M20 100 H220 L380 70 V150 L220 140 H20 Z" opacity="0.5"/>'
           '<path class="f2" d="M20 140 H200 L330 280 L300 280 L190 160 H20 Z" opacity="0.6"/>'
           '<path class="s" d="M200 100 L220 125 L240 95"/><path class="f2" d="M300 70 L320 40 L340 70 Z"/>'
           '<path class="s2" d="M270 200 C290 150 310 110 320 70"/>'),
      znaczniki=[(100, 150, 60, 180, 'Płyta oceaniczna', 'Cięższa — zanurza się pod kontynentalną'),
                 (320, 110, 360, 160, 'Płyta kontynentalna', 'Lżejsza, wypiętrzana'),
                 (220, 122, 210, 75, 'Rów oceaniczny', 'Najgłębsze części oceanu'),
                 (320, 50, 360, 30, 'Wulkan', 'Magma z topniejącej płyty wznosi się ku powierzchni'),
                 (270, 230, 230, 260, 'Strefa topnienia', 'Ognisko trzęsień i źródło magmy')],
      opis='Zbieżna granica płyty oceanicznej i kontynentalnej (np. Andy).',
      uwaga='Przy subdukcji powstają rowy oceaniczne, łańcuchy wulkanów i silne trzęsienia ziemi.'),
]

S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Niż baryczny w planie',
      svg=('<ellipse class="s" cx="180" cy="150" rx="40" ry="30"/><ellipse class="s" cx="180" cy="150" rx="90" ry="65"/>'
           '<ellipse class="s" cx="180" cy="150" rx="150" ry="110"/><text class="t" x="172" y="155">N</text>'
           '<path class="s2" d="M180 150 C240 160 280 200 300 250"/><path class="s2" d="M180 150 C220 160 230 210 200 260" stroke-dasharray="6 4"/>'),
      znaczniki=[(180, 150, 150, 120, 'Ośrodek niżu', 'Najniższe ciśnienie'),
                 (270, 205, 320, 200, 'Front ciepły', 'Przed nim opady ciągłe'),
                 (210, 230, 240, 270, 'Front chłodny', 'Burze i ulewy'),
                 (240, 225, 270, 245, 'Wycinek ciepły', 'Ciepłe powietrze między frontami'),
                 (330, 150, 360, 130, 'Izobara', 'Linia jednakowego ciśnienia')],
      opis='Niż z frontami — tak wygląda na mapie synoptycznej.',
      uwaga='Na półkuli N powietrze krąży w niżu przeciwnie do ruchu wskazówek zegara.'),
]
