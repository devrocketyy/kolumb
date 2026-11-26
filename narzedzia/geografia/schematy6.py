# Schematy geografii — porcja 6 (rysunki autorskie IndexLab). SVG 400×300; klasy: s, s2, f, f2, d, dash, t.
S = {}

S['g-atmosfera'] = [
 dict(typ='rysunek', tytul='Warstwy atmosfery i zmiana temperatury',
      svg=('<rect x="40" y="20" width="200" height="270" style="fill:#e3f2fd"/>'
           '<rect x="40" y="230" width="200" height="60" style="fill:#bbdefb"/>'
           '<rect x="40" y="150" width="200" height="80" style="fill:#c5cae9"/>'
           '<rect x="40" y="90" width="200" height="60" style="fill:#d1c4e9"/>'
           '<path class="dash" d="M40 230 H240 M40 150 H240 M40 90 H240"/>'
           '<path style="fill:none;stroke:#d32f2f;stroke-width:3" d="M200 290 L90 230 L150 150 L60 90 L180 20"/>'
           '<text class="t" x="250" y="294">0 km</text><text class="t" x="250" y="234">ok. 11 km</text><text class="t" x="250" y="154">ok. 50 km</text><text class="t" x="250" y="94">ok. 85 km</text>'
           '<text class="t" x="150" y="300" style="font-size:10px">temperatura →</text>'),
      znaczniki=[(140, 260, 330, 270, 'Troposfera', 'Spadek ok. 0,6°C/100 m; zjawiska pogodowe'),
                 (140, 190, 330, 200, 'Stratosfera', 'Warstwa ozonowa — temperatura rośnie'),
                 (140, 120, 330, 125, 'Mezosfera', 'Temperatura spada do ok. −90°C'),
                 (140, 50, 330, 50, 'Termosfera', 'Temperatura rośnie, zorze polarne'),
                 (90, 230, 20, 215, 'Tropopauza', 'Granica troposfery: ok. 8 km nad biegunami, 17 km nad równikiem')],
      opis='Pionowa budowa atmosfery i przebieg temperatury (czerwona linia).',
      uwaga='Ozon pochłania promieniowanie UV — dlatego w stratosferze temperatura rośnie z wysokością.'),
]

S['g-pl-geologia'] = [
 dict(typ='rysunek', tytul='Krajobraz polodowcowy w przekroju',
      svg=('<path style="fill:#e0e0e0" d="M0 0 H400 V300 H0 Z" opacity="0.3"/>'
           '<path style="fill:#b3e5fc;stroke:#4fc3f7" d="M0 80 L120 80 Q140 80 140 140 L0 160 Z"/>'
           '<path class="f2" d="M0 160 L140 140 Q150 120 170 125 L180 160 L215 150 L230 130 Q250 100 270 130 L290 175 L400 185 V300 H0 Z"/>'
           '<path style="fill:#ffe082" d="M290 175 L400 185 V200 L290 190 Z"/>'
           '<path style="fill:#64b5f6" d="M185 158 L212 151 L205 175 L192 175 Z"/>'
           '<path class="s2" d="M300 165 L380 172 M370 166 L380 172 L370 178"/>'),
      znaczniki=[(70, 120, 40, 50, 'Lądolód', 'Czoło lądolodu w czasie postoju'),
                 (155, 130, 140, 100, 'Wysoczyzna morenowa', 'Glina zwałowa spod lodu'),
                 (250, 112, 260, 70, 'Morena czołowa', 'Wał materiału przy czole lądolodu'),
                 (198, 165, 190, 220, 'Jezioro rynnowe', 'Rynna wyżłobiona przez wody pod lodem'),
                 (340, 182, 330, 230, 'Sandr', 'Piaski i żwiry wód roztopowych'),
                 (340, 168, 340, 145, 'Wody roztopowe', 'Płyną od czoła lądolodu')],
      opis='Układ form polodowcowych: wysoczyzna – morena czołowa – sandr.',
      uwaga='Kolejność od strony lądolodu: wysoczyzna morenowa, morena czołowa, sandr, pradolina.'),
]

S['g-rzeki'] = [
 dict(typ='rysunek', tytul='Wody podziemne i źródło artezyjskie',
      svg=('<path style="fill:#a1887f" d="M0 60 Q200 140 400 60 V300 H0 Z"/>'
           '<path style="fill:#90caf9" d="M0 60 Q200 200 400 60 L400 90 Q200 235 0 90 Z"/>'
           '<path style="fill:#6d4c41" d="M0 90 Q200 235 400 90 V300 H0 Z"/>'
           '<path class="s" d="M196 132 V92 M204 132 V92"/>'
           '<path class="s2" d="M200 95 V70 M192 80 L200 68 L208 80"/>'
           '<path class="dash" d="M0 58 H400"/>'),
      znaczniki=[(20, 64, 30, 30, 'Obszar zasilania', 'Woda wsiąka w odsłoniętą warstwę przepuszczalną'),
                 (110, 140, 90, 200, 'Warstwa wodonośna', 'Piaski lub piaskowce między skałami nieprzepuszczalnymi'),
                 (280, 110, 300, 150, 'Warstwa nieprzepuszczalna', 'Iły, gliny — nad i pod wodonośną'),
                 (200, 95, 230, 85, 'Studnia artezyjska', 'Woda pod ciśnieniem wypływa sama'),
                 (380, 58, 330, 40, 'Poziom zasilania', 'Woda wypływa, gdy wylot leży niżej niż ten poziom')],
      opis='Niecka artezyjska — wody podziemne pod ciśnieniem.',
      uwaga='Wody artezyjskie występują np. w niecce warszawskiej i w Wielkim Basenie Artezyjskim w Australii.'),
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
