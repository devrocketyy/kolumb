# Schematy chemii — porcja 4: zestawy do syntez i otrzymywania gazów, okresowość, procesy organiczne.
S = {}


def zlewka(x, y, w=80, h=90, poziom=0.55):
    hy = y + h * (1 - poziom)
    return (f'<path class="s" d="M{x} {y} v{h} h{w} v-{h}"/>'
            f'<rect class="f" x="{x + 1}" y="{hy}" width="{w - 2}" height="{y + h - hy - 1}"/>')


# ---------- ogrzewanie pod chłodnicą zwrotną ----------
_zwrot = (
    '<path class="s" d="M193 150 v-130 M207 150 v-130"/>'
    '<path class="f" d="M180 40 h40 v90 h-40 z"/>'
    '<path class="s" d="M193 40 v90 M207 40 v90"/>'
    '<path class="s" d="M220 120 h30 M180 50 h-30"/>'
    '<path class="s" d="M193 150 v20 a40 40 0 1 0 14 0 v-20"/>'
    '<path class="f" d="M168 215 a33 33 0 0 0 64 0 z"/>'
    '<rect class="f2" x="170" y="262" width="60" height="16" rx="4"/>'
    '<circle class="s2" cx="190" cy="225" r="2"/><circle class="s2" cx="205" cy="232" r="2"/><circle class="s2" cx="212" cy="220" r="2"/>'
    '<text class="t" x="252" y="124">← woda (wlot)</text><text class="t" x="92" y="54">woda (wylot) ←</text>'
)
_zwrot_zn = [
    (200, 85, 290, 80, 'Chłodnica zwrotna', 'woda wpływa dołem, wypływa górą; pary skraplają się i wracają do kolby'),
    (200, 220, 290, 220, 'Mieszanina reakcyjna', 'np. kwas + alkohol + kilka kropli stężonego H₂SO₄'),
    (190, 225, 100, 240, 'Kamyczki wrzenne', 'zapobiegają przegrzaniu i gwałtownemu wrzeniu'),
    (200, 270, 290, 280, 'Czasza grzejna', 'łagodne, równomierne ogrzewanie'),
]

# ---------- otrzymywanie gazu z wkraplacza ----------
_wkr = (
    '<path class="s" d="M110 60 h40 l-8 40 v40 h-24 v-40 z"/>'
    '<path class="f" d="M114 64 h32 l-6 30 h-20 z"/>'
    '<rect class="d" x="120" y="112" width="20" height="5" rx="2"/>'
    '<path class="s" d="M126 140 v20 M134 140 v20"/>'
    '<path class="s" d="M70 160 h120 M80 160 v80 a50 30 0 0 0 100 0 v-80"/>'
    '<path class="f2" d="M86 225 h88 a44 22 0 0 1 -88 0 z"/>'
    '<path class="s" d="M180 180 h80 v-60 h40"/>'
    + zlewka(290, 100, w=80, h=120, poziom=0.5)
    + '<path class="s" d="M300 120 v80 M308 120 v80"/>'
)
_wkr_zn = [
    (130, 80, 50, 60, 'Wkraplacz', 'zawiera ciecz, np. kwas solny; kran reguluje szybkość reakcji'),
    (130, 232, 60, 280, 'Kolba z ciałem stałym', 'np. cynk, CaCO₃ lub Na₂SO₃'),
    (230, 180, 230, 210, 'Rurka odprowadzająca', 'prowadzi gaz do płuczki lub odbieralnika'),
    (330, 190, 370, 280, 'Płuczka', 'oczyszcza lub suszy gaz (np. stężony H₂SO₄ suszy CO₂)'),
]

# ---------- promień i energia jonizacji w układzie okresowym ----------
_okr = (
    '<rect class="f" x="60" y="60" width="280" height="160" rx="6"/>'
    + ''.join(f'<path class="s2" d="M{60 + 40 * i} 60 v160"/>' for i in range(1, 7))
    + ''.join(f'<path class="s2" d="M60 {60 + 40 * i} h280"/>' for i in range(1, 4))
    + '<path class="s" d="M80 245 H320"/><path class="d" d="M320 241 l8 4 l-8 4 z"/>'
    + '<path class="s" d="M35 80 V200"/><path class="d" d="M31 200 l4 8 l4 -8 z"/>'
    + '<path class="dash" d="M80 40 H320"/><path class="d" d="M80 36 l-8 4 l8 4 z"/>'
    + '<path class="dash" d="M365 80 V200"/><path class="d" d="M361 200 l4 8 l4 -8 z"/>'
    + '<text class="t" x="120" y="262">elektroujemność, energia jonizacji ↑</text>'
    + '<text class="t" x="140" y="32">promień atomowy ↑</text>'
)
_okr_zn = [
    (200, 245, 200, 285, 'W okresie (w prawo)', 'rośnie elektroujemność i energia jonizacji, maleje promień'),
    (35, 140, 15, 140, 'W grupie (w dół)', 'rośnie promień i charakter metaliczny, maleje energia jonizacji'),
    (80, 40, 40, 20, 'Promień w okresie', 'największy w grupie 1 (lewa strona)'),
    (365, 140, 385, 140, 'Promień w grupie', 'rośnie w dół — przybywa powłok'),
]

S['c-doswiadczenia'] = [
    dict(typ='rysunek', tytul='Ogrzewanie pod chłodnicą zwrotną', svg=_zwrot, znaczniki=_zwrot_zn,
         opis='Zestaw do długotrwałego ogrzewania mieszaniny bez utraty lotnych składników (np. estryfikacja, hydroliza estru).',
         uwaga='Chłodnica zwrotna stoi pionowo — w odróżnieniu od destylacji produkt nie opuszcza kolby.'),
    dict(typ='rysunek', tytul='Otrzymywanie gazu z wkraplaczem', svg=_wkr, znaczniki=_wkr_zn,
         opis='Zestaw do otrzymywania gazu z cieczy i ciała stałego bez ogrzewania.',
         uwaga='Gaz suszy się w płuczce ze stężonym H₂SO₄ (nie dla NH₃ — ten suszy się CaO).'),
]
S['c-okresowosc'] = [
    dict(typ='rysunek', tytul='Zmiany właściwości w układzie okresowym', svg=_okr, znaczniki=_okr_zn,
         opis='Kierunki zmian promienia atomowego, elektroujemności i energii jonizacji (gazy szlachetne pominięte przy elektroujemności).',
         uwaga='Najbardziej elektroujemny jest fluor, najmniej — cez i frans. Charakter niemetaliczny rośnie w prawo i w górę.'),
]

P = lambda tytul, kroki, opis='', uwaga='': dict(typ='proces', tytul=tytul, kroki=kroki, opis=opis, **({'uwaga': uwaga} if uwaga else {}))

S['c-hydroliza'] = [
    P('Przewidywanie odczynu roztworu soli', [
        ('Rozpoznaj kwas i zasadę', 'z których pochodzi sól'),
        ('Mocny kwas + mocna zasada', 'brak hydrolizy, odczyn obojętny (NaCl, KNO₃)'),
        ('Słaby kwas + mocna zasada', 'hydroliza anionowa, odczyn zasadowy (Na₂CO₃, CH₃COONa)'),
        ('Mocny kwas + słaba zasada', 'hydroliza kationowa, odczyn kwasowy (NH₄Cl, AlCl₃)'),
        ('Słaby kwas + słaba zasada', 'odczyn zależy od Ka i Kb (CH₃COONH₄ — ok. obojętny)'),
        ('Wodorosole', 'porównaj dysocjację i hydrolizę: NaHCO₃ — zasadowy, NaHSO₄ — kwasowy'),
    ]),
]
S['c-ph'] = [
    P('Obliczanie pH słabego kwasu', [
        ('Zapisz równanie dysocjacji', 'HA ⇄ H⁺ + A⁻'),
        ('Sprawdź c/Ka', 'jeśli > 400 (α < 5%), można stosować uproszczenie'),
        ('Uproszczenie', '[H⁺] = √(Ka · c)'),
        ('Bez uproszczenia', 'Ka = x² / (c − x) — równanie kwadratowe'),
        ('pH', '−log[H⁺]; podaj z dokładnością wymaganą w poleceniu'),
    ]),
]
S['c-stezenia'] = [
    P('Przeliczanie stężenia procentowego na molowe', [
        ('Przyjmij 1 dm³ roztworu', 'masa = 1000 · d (g)'),
        ('Masa substancji', 'mₛ = cₚ · m_r / 100%'),
        ('Liczba moli', 'n = mₛ / M'),
        ('Stężenie molowe', 'c = n / 1 dm³ — skrótowo c = cₚ · d · 10 / M'),
    ]),
]
S['c-wzory'] = [
    P('Ustalanie wzoru związku z analizy spalania', [
        ('Masa C', 'z masy CO₂: m(C) = m(CO₂) · 12/44'),
        ('Masa H', 'z masy H₂O: m(H) = m(H₂O) · 2/18'),
        ('Masa O', 'różnica: masa próbki − m(C) − m(H)'),
        ('Stosunek moli', 'podziel przez najmniejszą liczbę → wzór empiryczny'),
        ('Wzór rzeczywisty', 'M związku / M wzoru empirycznego = krotność'),
    ]),
]
S['c-cukry'] = [
    P('Od projekcji Fischera do wzoru Hawortha (D-glukoza)', [
        ('Łańcuch w projekcji Fischera', 'grupa –CHO na górze, –CH₂OH na dole'),
        ('Zamknięcie pierścienia', '–OH przy C5 atakuje C1 — powstaje półacetal (pierścień sześcioczłonowy)'),
        ('Podstawniki z prawej strony', 'w Haworcie skierowane w dół'),
        ('Podstawniki z lewej strony', 'w Haworcie skierowane w górę'),
        ('Grupa –CH₂OH (D-cukry)', 'skierowana w górę'),
        ('Anomer α / β', '–OH przy C1 w dół (α) lub w górę (β)'),
    ]),
]
S['c-alkeny'] = [
    P('Reakcje alkenów — przegląd', [
        ('Uwodornienie (H₂, Ni)', 'alkan'),
        ('Addycja X₂', 'dihalogenoalkan — odbarwienie wody bromowej'),
        ('Addycja HX', 'halogenoalkan wg reguły Markownikowa'),
        ('Hydratacja (H₂O, H⁺)', 'alkohol wg reguły Markownikowa'),
        ('Utlenianie KMnO₄ (obojętne)', 'diol, brunatny osad MnO₂'),
        ('Polimeryzacja', 'polialken, np. polietylen, polipropylen'),
    ]),
]
S['c-alkohole'] = [
    P('Odróżnianie alkoholi mono- i polihydroksylowych oraz fenoli', [
        ('Cu(OH)₂', 'szafirowy roztwór — glicerol, glikol (–OH przy sąsiednich C)'),
        ('FeCl₃', 'fioletowe zabarwienie — fenol'),
        ('Woda bromowa', 'biały osad — fenol'),
        ('NaOH(aq)', 'roztwarza fenol, nie reaguje z alkoholami'),
        ('Na', 'wodór wydzielają i alkohole, i fenole'),
    ]),
]
S['c-aminokwasy'] = [
    P('Ustalanie sekwencji peptydu z hydrolizy częściowej', [
        ('Wypisz dipeptydy i tripeptydy', 'z wyników hydrolizy'),
        ('Szukaj wspólnych reszt', 'nakładają się na siebie fragmenty'),
        ('Ustal N-koniec', 'reszta z wolną grupą –NH₂ (zapisywana z lewej)'),
        ('Złóż sekwencję', 'sprawdź, czy wyjaśnia wszystkie fragmenty'),
    ]),
]
