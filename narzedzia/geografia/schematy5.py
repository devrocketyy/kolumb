# Schematy geografii — porcja 5 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}

S['g-tektonika'] = [
 dict(typ='rysunek', tytul='Plama gorąca i łańcuch wysp',
      svg=('<path d="M10 120 H390 V140 H10 Z" style="fill:#64b5f6"/>'
           '<path class="f2" d="M10 140 H390 V190 H10 Z"/>'
           '<path d="M10 190 H390 V290 H10 Z" style="fill:#ffccbc"/>'
           '<path class="f2" d="M300 140 L320 80 L340 140 Z M220 140 L235 105 L250 140 Z M140 140 L150 125 L160 140 Z M60 140 L65 135 L70 140 Z"/>'
           '<path style="fill:#e64a19" d="M310 290 Q300 220 320 190 Q330 220 330 290 Z"/>'
           '<path class="s2" d="M360 165 H260 M272 157 L260 165 L272 173"/>'),
      znaczniki=[(320, 85, 350, 60, 'Czynny wulkan', 'Leży nad plamą gorąca (np. Hawaje)'),
                 (235, 108, 230, 80, 'Wygasły wulkan', 'Przesunięty wraz z płytą'),
                 (65, 137, 50, 100, 'Najstarsza wyspa', 'Zerodowana, przechodzi w atol'),
                 (318, 250, 350, 240, 'Pióropusz płaszcza', 'Gorąca magma z głębi płaszcza'),
                 (300, 165, 280, 210, 'Ruch płyty', 'Płyta przesuwa się nad nieruchomą plamą')],
      opis='Powstawanie łańcucha wysp wulkanicznych nad plamą gorąca.',
      uwaga='Wiek wysp rośnie w kierunku ruchu płyty — to dowód na przesuwanie się płyt.'),
]

S['g-uslugi'] = [
 dict(typ='rysunek', tytul='Struktura zatrudnienia a poziom rozwoju',
      svg=(''.join(f'<rect x="{60+i*110}" y="{260-a}" width="60" height="{a}" style="fill:#9ccc65"/><rect x="{60+i*110}" y="{260-a-b}" width="60" height="{b}" style="fill:#8d6e63"/><rect x="{60+i*110}" y="{60}" width="60" height="{200-a-b}" style="fill:#64b5f6"/>' for i, (a, b) in enumerate([(140, 20), (60, 60), (6, 40)]))
           + '<text class="t" x="55" y="280">Kraj A</text><text class="t" x="165" y="280">Kraj B</text><text class="t" x="275" y="280">Kraj C</text>'),
      znaczniki=[(90, 190, 20, 200, 'Rolnictwo', 'Kraj A: 70% — przedprzemysłowy'),
                 (200, 170, 140, 140, 'Przemysł', 'Kraj B: 30% — przemysłowy'),
                 (310, 130, 370, 100, 'Usługi', 'Kraj C: 77% — postindustrialny')],
      opis='Udział sektorów w zatrudnieniu (rolnictwo zielone, przemysł brązowy, usługi niebieskie), dane umowne.',
      uwaga='Teoria trzech sektorów (Fisher–Clark): wraz z rozwojem zatrudnienie przesuwa się z rolnictwa do przemysłu, a potem do usług.'),
]

S['g-rolnictwo'] = [
 dict(typ='proces', tytul='Typy rolnictwa — jak je rozpoznać', opis='Klucz do zadań z materiałem źródłowym.',
      kroki=[('Wysokie nakłady, wysokie plony z ha', 'Rolnictwo intensywne — Holandia, Belgia, Japonia.'),
             ('Ogromne gospodarstwa, maszyny, mało ludzi', 'Rolnictwo ekstensywne wysokotowarowe — USA, Kanada, Australia, Argentyna.'),
             ('Jedna roślina na eksport w tropikach', 'Gospodarka plantacyjna — kawa w Brazylii, herbata w Kenii, banany w Ekwadorze.'),
             ('Wypalanie lasu, uprawa kilka lat', 'Rolnictwo żarowe (wędrówkowe) — Afryka, Amazonia.'),
             ('Stada w ruchu za paszą', 'Pasterstwo koczownicze — Sahel, Mongolia.'),
             ('Wysoka praca ręczna, ryż na tarasach', 'Rolnictwo intensywne tradycyjne — Azja Monsunowa.')],
      uwaga='Na maturze zawsze łącz typ z cechą (nakłady, plony, towarowość) i przykładem regionu.'),
]

S['g-obrotowy'] = [
 dict(typ='rysunek', tytul='Strefy czasowe wokół Polski',
      svg=(''.join(f'<rect x="{20+i*90}" y="40" width="90" height="200" style="fill:{c};stroke:#999"/><text class="t" x="{40+i*90}" y="260">UTC{z}</text>' for i, (c, z) in enumerate([('#e3f2fd', '+0'), ('#c8e6c9', '+1'), ('#fff9c4', '+2'), ('#ffe0b2', '+3')]))
           + '<path class="dash" d="M65 40 V240 M155 40 V240 M245 40 V240 M335 40 V240"/>'
           + '<text class="t" x="55" y="30">0°</text><text class="t" x="140" y="30">15°E</text><text class="t" x="230" y="30">30°E</text><text class="t" x="320" y="30">45°E</text>'),
      znaczniki=[(65, 120, 40, 100, 'Londyn', 'UTC+0 (zimą)'),
                 (155, 140, 175, 120, 'Polska', 'UTC+1 zimą, UTC+2 latem'),
                 (245, 160, 265, 140, 'Ukraina, Finlandia', 'UTC+2'),
                 (335, 180, 350, 160, 'Moskwa', 'UTC+3 przez cały rok'),
                 (110, 210, 120, 225, 'Granica strefy', 'Co 15° — 1 godzina (granice zwykle wzdłuż granic państw)')],
      opis='Uproszczony układ stref czasowych w Europie.',
      uwaga='Południkiem środkowym strefy UTC+1 jest 15°E — przechodzi przez Zgorzelec i Stargard.'),
]
