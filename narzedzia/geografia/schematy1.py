# Schematy geografii — porcja 1 (rysunki autorskie IndexLab). SVG w viewBox 400×300; klasy: s, s2, f, f2, d, dash, t.
# Znacznik: (x, y elementu, x, y numeru, nazwa, krótki opis).
S = {}

_poziomice = (
 '<path class="s" d="M100 240 C100 120 160 60 220 60 C300 60 360 140 360 240"/>'
 '<path class="s" d="M115 240 C115 140 165 95 215 95 C280 95 310 160 310 240"/>'
 '<path class="s" d="M130 240 C130 165 170 130 210 130 C250 130 260 180 260 240"/>'
 '<ellipse class="s" cx="190" cy="190" rx="40" ry="25"/>'
 '<path class="s2" d="M330 240 L345 295"/>'
 '<text class="t" x="215" y="55">300</text><text class="t" x="210" y="90">310</text><text class="t" x="205" y="125">320</text><text class="t" x="178" y="194">330</text>'
)
S['g-poziomice'] = [
 dict(typ='rysunek', tytul='Poziomice: wzgórze i stoki', svg=_poziomice,
      znaczniki=[(190, 190, 190, 235, 'Szczyt', 'Zamknięta poziomica o najwyższej wartości'),
                 (115, 200, 60, 200, 'Stok stromy', 'Poziomice gęsto — duża różnica wysokości na małej odległości'),
                 (320, 170, 375, 160, 'Stok łagodny', 'Poziomice rzadko'),
                 (338, 268, 375, 280, 'Ciek', 'Woda spływa prostopadle do poziomic, od wyższych ku niższym')],
      opis='Wzgórze na mapie poziomicowej z cięciem 10 m.',
      uwaga='Gęste poziomice = stromo. Zamknięte poziomice o rosnących wartościach = wzniesienie, o malejących = zagłębienie.'),
 dict(typ='rysunek', tytul='Profil terenu z mapy',
      svg=('<path class="s" d="M30 250 H370"/><path class="s" d="M30 250 V40"/>'
           '<path class="f" d="M30 250 L30 200 L90 170 L150 110 L190 90 L230 130 L280 150 L330 190 L370 210 L370 250 Z"/>'
           '<path class="dash" d="M190 90 L190 250"/><text class="t" x="10" y="205">200</text><text class="t" x="10" y="95">300</text>'
           '<text class="t" x="180" y="268">km</text>'),
      znaczniki=[(190, 90, 210, 70, 'Kulminacja', 'Najwyższy punkt na linii profilu'),
                 (110, 150, 80, 125, 'Stok zachodni', 'Bardziej stromy — szybki przyrost wysokości'),
                 (300, 170, 320, 150, 'Stok wschodni', 'Łagodniejszy'),
                 (30, 150, 50, 50, 'Skala pionowa', 'Zwykle przewyższona, by uwidocznić rzeźbę')],
      opis='Przekrój terenu wykreślony z punktów przecięcia linii z poziomicami.',
      uwaga='Na osi poziomej odległość według skali mapy, na pionowej — wysokość. Podaj przewyższenie, jeśli skale są różne.'),
]

S['g-obiegowy'] = [
 dict(typ='rysunek', tytul='Strefy oświetlenia Ziemi',
      svg=('<circle class="s" cx="200" cy="150" r="120"/>'
           '<path class="f2" d="M120 60 A120 120 0 0 1 280 60 Z"/><path class="f2" d="M120 240 A120 120 0 0 0 280 240 Z"/>'
           '<path class="f" d="M85 112 H315 V188 H85 Z" opacity="0.6"/>'
           '<path class="s2" d="M80 150 H320"/><path class="dash" d="M85 112 H315"/><path class="dash" d="M85 188 H315"/>'
           '<path class="dash" d="M120 60 H280"/><path class="dash" d="M120 240 H280"/>'),
      znaczniki=[(200, 150, 340, 150, 'Strefa gorąca', 'Między zwrotnikami — Słońce może górować w zenicie'),
                 (200, 85, 340, 85, 'Strefa umiarkowana północna', 'Między zwrotnikiem Raka a kołem podbiegunowym'),
                 (200, 45, 340, 40, 'Strefa zimna północna', 'Za kołem podbiegunowym — dzień i noc polarna'),
                 (300, 112, 360, 115, 'Zwrotnik Raka', '23°27′N'),
                 (280, 60, 360, 62, 'Koło podbiegunowe', '66°33′N'),
                 (300, 188, 360, 190, 'Zwrotnik Koziorożca', '23°27′S')],
      opis='Podział Ziemi na strefy według kąta padania promieni słonecznych.',
      uwaga='Granice stref oświetlenia wynikają z nachylenia osi Ziemi (23°27′).'),
]

S['g-cisnienie'] = [
 dict(typ='rysunek', tytul='Cyrkulacja atmosferyczna',
      svg=('<path class="s" d="M60 20 H340 M60 280 H340"/>'
           '<path class="s2" d="M60 150 H340"/><path class="dash" d="M60 95 H340 M60 205 H340 M60 50 H340 M60 250 H340"/>'
           '<path class="s" d="M150 100 L130 140"/><path class="s" d="M260 100 L240 140"/>'
           '<path class="s" d="M150 200 L130 160"/><path class="s" d="M260 200 L240 160"/>'
           '<path class="s" d="M130 90 L170 60"/><path class="s" d="M240 90 L280 60"/>'
           '<text class="t" x="20" y="155">0°</text><text class="t" x="15" y="100">30°N</text><text class="t" x="15" y="55">60°N</text><text class="t" x="15" y="210">30°S</text>'),
      znaczniki=[(140, 120, 100, 125, 'Pasaty NE', 'Wieją od wyżów zwrotnikowych ku równikowi, odchylone w prawo'),
                 (140, 180, 100, 185, 'Pasaty SE', 'Na półkuli S odchylone w lewo'),
                 (200, 150, 200, 135, 'Niż równikowy', 'Strefa konwergencji, wznoszenie powietrza i opady'),
                 (200, 95, 300, 100, 'Wyż zwrotnikowy', 'Opadanie suchego powietrza — pustynie'),
                 (150, 75, 120, 55, 'Wiatry zachodnie', 'Strefa umiarkowana'),
                 (200, 50, 300, 45, 'Niż subpolarny', 'Ok. 60°, zbieżność mas powietrza')],
      opis='Uproszczony układ stref ciśnienia i stałych wiatrów.',
      uwaga='Na półkuli N wiatry odchylają się w prawo, na S w lewo (siła Coriolisa).'),
]

S['g-pogoda'] = [
 dict(typ='rysunek', tytul='Front ciepły i front chłodny',
      svg=('<path class="s" d="M10 260 H390"/>'
           '<path class="f" d="M20 260 L180 120 L180 260 Z"/><path class="f2" d="M220 260 C250 180 280 150 380 140 L380 260 Z"/>'
           '<path class="s2" d="M20 258 L180 120"/><path class="s2" d="M220 258 C250 180 280 150 380 140"/>'
           '<path class="dash" d="M60 110 H160 M270 80 C300 60 330 60 360 80"/>'),
      znaczniki=[(100, 195, 60, 230, 'Front ciepły', 'Ciepłe powietrze łagodnie nasuwa się na chłodne'),
                 (110, 110, 110, 90, 'Chmury warstwowe', 'Długotrwałe opady ciągłe'),
                 (260, 200, 250, 230, 'Front chłodny', 'Chłodne powietrze wciska się pod ciepłe'),
                 (315, 70, 330, 40, 'Chmury kłębiaste', 'Krótkie ulewy, burze'),
                 (180, 200, 200, 210, 'Powietrze ciepłe', 'Między frontami (wycinek ciepły niżu)')],
      opis='Przekroje przez fronty atmosferyczne.',
      uwaga='Po przejściu frontu ciepłego — ocieplenie, po chłodnym — ochłodzenie i poprawa widzialności.'),
]

S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Przekrój stratowulkanu',
      svg=('<path class="f" d="M30 270 L170 70 L230 70 L370 270 Z"/>'
           '<path class="s2" d="M200 270 L200 70"/><ellipse class="f2" cx="200" cy="280" rx="60" ry="14"/>'
           '<path class="s" d="M60 230 L340 230 M90 190 L310 190 M120 150 L280 150 M150 110 L250 110"/>'
           '<path class="s" d="M200 140 L270 175"/><path class="dash" d="M190 60 C170 30 210 20 200 5"/>'),
      znaczniki=[(200, 280, 280, 290, 'Komora magmowa', 'Zbiornik magmy pod wulkanem'),
                 (200, 200, 160, 205, 'Komin główny', 'Droga magmy na powierzchnię'),
                 (200, 70, 240, 55, 'Krater', 'Otwór na szczycie stożka'),
                 (270, 175, 300, 160, 'Komin boczny', 'Erupcje z boku stożka (stożki pasożytnicze)'),
                 (90, 190, 50, 175, 'Warstwy lawy i popiołów', 'Na przemian — stąd nazwa stratowulkan'),
                 (200, 25, 240, 20, 'Chmura erupcyjna', 'Gazy i materiał piroklastyczny')],
      opis='Budowa wulkanu warstwowego.',
      uwaga='Stratowulkany powstają głównie w strefach subdukcji (lawa lepka, erupcje wybuchowe).'),
]

S['g-gleby'] = [
 dict(typ='rysunek', tytul='Profil gleby bielicowej',
      svg=('<rect class="s" x="120" y="20" width="160" height="260"/>'
           '<rect class="f2" x="120" y="20" width="160" height="20"/><rect class="f" x="120" y="40" width="160" height="40" opacity="0.9"/>'
           '<rect class="d" x="120" y="80" width="160" height="50"/><rect class="f2" x="120" y="130" width="160" height="60" opacity="0.6"/>'
           '<rect class="f" x="120" y="190" width="160" height="90" opacity="0.3"/>'),
      znaczniki=[(200, 30, 320, 30, 'O — poziom organiczny', 'Ściółka iglasta'),
                 (200, 60, 320, 60, 'A — próchniczny', 'Cienki, ubogi w próchnicę'),
                 (200, 105, 320, 105, 'E — wymywania', 'Jasny, „bielicowy”'),
                 (200, 160, 320, 160, 'B — wmywania', 'Nagromadzenie związków żelaza i glinu, rdzawy'),
                 (200, 235, 320, 235, 'C — skała macierzysta', 'Np. piaski polodowcowe')],
      opis='Układ poziomów genetycznych w glebie bielicowej.',
      uwaga='Wyraźny poziom wymywania E to cecha rozpoznawcza gleb bielicowych.'),
]

S['g-pl-geologia'] = [
 dict(typ='rysunek', tytul='Pasy rzeźby Polski',
      svg=('<path class="s" d="M40 20 H360 V280 H40 Z"/>'
           '<path class="f" d="M40 20 H360 V45 H40 Z" opacity="0.4"/><path class="f" d="M40 45 H360 V95 H40 Z" opacity="0.6"/>'
           '<path class="f" d="M40 95 H360 V165 H40 Z" opacity="0.25"/><path class="f2" d="M40 165 H360 V215 H40 Z" opacity="0.5"/>'
           '<path class="f" d="M40 215 H360 V240 H40 Z" opacity="0.35"/><path class="f2" d="M40 240 H360 V280 H40 Z"/>'),
      znaczniki=[(200, 32, 380, 32, 'Pobrzeża', 'Wydmy, mierzeje, jeziora przybrzeżne, klify'),
                 (200, 70, 380, 70, 'Pojezierza', 'Rzeźba młodoglacjalna, liczne jeziora'),
                 (200, 130, 380, 130, 'Niziny Środkowopolskie', 'Rzeźba staroglacjalna, pradoliny'),
                 (200, 190, 380, 190, 'Wyżyny', 'Starsze skały, lessy, kras'),
                 (200, 228, 380, 228, 'Kotliny podkarpackie', 'Obniżenia u podnóża Karpat'),
                 (200, 260, 380, 260, 'Góry', 'Sudety (stare, odmłodzone) i Karpaty (młode, alpejskie)')],
      opis='Równoleżnikowy układ krain w Polsce (schemat).',
      uwaga='Układ pasowy wynika z budowy geologicznej i zasięgu zlodowaceń — najmłodsza rzeźba polodowcowa na północy.'),
]

S['g-demografia'] = [
 dict(typ='proces', tytul='Przejście demograficzne', opis='Model zmian urodzeń i zgonów w miarę rozwoju społeczno-gospodarczego.',
      kroki=[('Faza I — przedtransformacyjna', 'Wysokie urodzenia i wysokie zgony; przyrost bliski zera.'),
             ('Faza II — spadek zgonów', 'Poprawa wyżywienia i medycyny; urodzenia wysokie — eksplozja demograficzna.'),
             ('Faza III — spadek urodzeń', 'Urbanizacja, edukacja kobiet, planowanie rodziny; przyrost maleje.'),
             ('Faza IV — posttransformacyjna', 'Niskie urodzenia i niskie zgony; przyrost bliski zera.'),
             ('Faza V (wg części autorów)', 'Urodzenia poniżej zgonów — ubytek naturalny i starzenie się (np. Polska, Japonia).')],
      uwaga='Kraje Afryki Subsaharyjskiej są w fazie II–III, Europa w fazie IV–V.'),
]

S['g-oceany'] = [
 dict(typ='proces', tytul='Obieg wody w przyrodzie', opis='Krążenie wody między oceanem, atmosferą i lądem.',
      kroki=[('Parowanie', 'Głównie z oceanów, napędzane energią Słońca.'),
             ('Transport pary wodnej', 'Wiatry przenoszą parę nad lądy.'),
             ('Kondensacja', 'Ochładzające się powietrze tworzy chmury.'),
             ('Opady', 'Deszcz i śnieg nad oceanami i lądami.'),
             ('Spływ powierzchniowy i podziemny', 'Rzekami i wodami podziemnymi woda wraca do oceanu.'),
             ('Ewapotranspiracja', 'Parowanie z gleby i roślin na lądzie zamyka mały obieg.')],
      uwaga='Duży obieg obejmuje ocean i ląd, mały — tylko ocean lub tylko ląd.'),
]
