# Schematy biologii — porcja 9: uzupełnienie poddziałów (rysunki i procesy).
import math

S = {}


def kropki(pts, r=2):
    return ''.join(f'<circle class="d" cx="{x}" cy="{y}" r="{r}"/>' for x, y in pts)


# ---------- cząsteczki wody ----------
def _czasteczka(o, hs):
    out = ''.join(f'<line class="s" x1="{o[0]}" y1="{o[1]}" x2="{h[0]}" y2="{h[1]}"/>' for h in hs)
    out += f'<circle class="f2" cx="{o[0]}" cy="{o[1]}" r="20"/>'
    return out + ''.join(f'<circle class="f" cx="{h[0]}" cy="{h[1]}" r="11"/>' for h in hs)


_woda = (
    _czasteczka((200, 130), [(178, 156), (222, 156)])
    + _czasteczka((120, 232), [(100, 254), (142, 256)])
    + _czasteczka((282, 232), [(304, 252), (262, 258)])
    + _czasteczka((185, 36), [(198, 64), (156, 46)])
    + '<path class="dash" d="M170 166 L132 214 M230 166 L268 214 M200 76 L200 108"/>'
    + '<text class="t" x="226" y="122">δ−</text><text class="t" x="160" y="182">δ+</text><text class="t" x="232" y="182">δ+</text>'
)

# ---------- poziomy struktury białka ----------
def _bialko():
    out = ''.join(f'<circle class="f" cx="{20 + k * 16}" cy="40" r="7"/>' for k in range(10))
    out += '<text class="t" x="20" y="18">I</text>'
    pts = ' '.join(f'{210 + 6 * k},{40 + 16 * math.sin(k * 0.9):.1f}' for k in range(30))
    out += f'<polyline points="{pts}" fill="none" stroke="currentColor" stroke-width="2.4"/><text class="t" x="210" y="18">II</text>'
    out += '<path d="M40 190 C20 130 90 120 100 160 S60 230 110 240 S170 180 140 150 S90 110 130 100 S190 150 170 200" fill="none" stroke="currentColor" stroke-width="2.4"/>'
    out += '<line class="dash" x1="100" y1="160" x2="140" y2="150"/><text class="t" x="20" y="100">III</text>'
    for cx, cy in ((250, 160), (310, 160), (250, 220), (310, 220)):
        out += f'<circle class="f" cx="{cx}" cy="{cy}" r="27"/><path class="s2" d="M{cx - 14} {cy} q7 -14 14 0 t14 0"/>'
    out += kropki([(250, 160), (310, 160), (250, 220), (310, 220)], 4) + '<text class="t" x="230" y="120">IV</text>'
    return out


# ---------- tłuszcz i fosfolipid ----------
def _lipidy():
    out = '<rect class="f2" x="30" y="40" width="40" height="120" rx="4"/>'
    for y in (60, 100, 140):
        out += f'<path class="s" d="M70 {y} l20 0"/><rect class="f" x="90" y="{y - 7}" width="16" height="14" rx="2"/>'
        out += f'<path class="s" d="M106 {y} l12 -6 l12 6 l12 -6 l12 6 l12 -6 l12 6 l12 -6"/>'
    out += '<path class="s" d="M106 140 l12 -6 l12 6 l12 -6 l6 3 l8 8 l12 -6 l12 6"/>'
    out += '<circle class="f2" cx="280" cy="50" r="22"/><rect class="f" x="268" y="74" width="24" height="16" rx="2"/>'
    out += '<rect class="f2" x="262" y="92" width="36" height="22" rx="3"/>'
    out += '<path class="s" d="M270 114 l-6 12 l6 12 l-6 12 l6 12 l-6 12 l6 12 l-6 12 M290 114 l6 12 l-6 12 l6 12 l-8 10 l8 10 l-6 12 l6 12"/>'
    out += '<text class="t" x="30" y="190">triacyloglicerol</text><text class="t" x="240" y="230">fosfolipid</text>'
    return out


# ---------- przeciwciało ----------
def _rura(d, w=12):
    return (f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="var(--surface-2)" stroke-width="{w - 4}" stroke-linejoin="round" stroke-linecap="round"/>')


_ab = (
    _rura('M190 290 L190 170 L125 95 L85 50') + _rura('M210 290 L210 170 L275 95 L315 50')
    + _rura('M148 146 L113 105 L73 60', w=11) + _rura('M252 146 L287 105 L327 60', w=11)
    + '<path class="s" d="M190 200 L210 200 M190 214 L210 214 M150 140 L158 133 M250 140 L242 133"/>'
    + '<path class="f2" d="M52 36 Q50 14 72 14 Q78 32 52 36 Z"/><path class="f2" d="M348 36 Q350 14 328 14 Q322 32 348 36 Z"/>'
)

# ---------- naczynia krwionośne ----------
_naczynia = (
    '<circle class="f2" cx="80" cy="140" r="62"/><circle class="f" cx="80" cy="140" r="44"/><circle cx="80" cy="140" r="24" fill="var(--surface)" stroke="currentColor" stroke-width="1.6"/>'
    '<ellipse class="f2" cx="225" cy="140" rx="68" ry="52"/><ellipse class="f" cx="225" cy="140" rx="58" ry="42"/><ellipse cx="225" cy="140" rx="48" ry="34" fill="var(--surface)" stroke="currentColor" stroke-width="1.6"/>'
    '<circle cx="345" cy="140" r="16" fill="var(--surface)" stroke="currentColor" stroke-width="1.6"/>'
    '<text class="t" x="45" y="230">tętnica</text><text class="t" x="207" y="230">żyła</text><text class="t" x="322" y="230">włosowate</text>'
)

# ---------- hamowanie enzymów ----------
_inhib = (
    '<path class="f" d="M30 200 L30 120 L70 120 L70 150 L100 150 L100 120 L150 120 L150 200 Z"/>'
    '<path class="f2" d="M72 152 L98 152 L98 118 L72 118 Z" transform="translate(0 -40)"/>'
    '<path class="f2" d="M72 112 L98 112 L98 150 L72 150 Z"/>'
    '<text class="t" x="40" y="230">kompetycyjne</text>'
    '<path class="f" d="M230 200 L230 130 L270 140 L270 150 L300 150 L300 140 L350 130 L350 200 Z"/>'
    '<path class="f2" d="M300 200 L320 200 L320 214 L300 214 Z"/>'
    '<path class="f2" d="M268 60 L296 60 L296 96 L268 96 Z"/>'
    '<path class="s2" d="M282 100 L285 136"/>'
    '<text class="t" x="240" y="240">niekompetycyjne</text>'
)

S['b-woda'] = [
    dict(typ='rysunek', tytul='Wiązania wodorowe między cząsteczkami wody', svg=_woda,
         znaczniki=[
             (200, 120, 300, 100, 'Atom tlenu', 'częściowy ładunek ujemny (δ−)'),
             (178, 156, 60, 120, 'Atom wodoru', 'częściowy ładunek dodatni (δ+)'),
             (151, 190, 60, 180, 'Wiązanie wodorowe', 'słabe, ale liczne — kohezja, wysokie ciepło właściwe'),
             (211, 143, 320, 160, 'Wiązanie kowalencyjne spolaryzowane', 'łączy O i H w cząsteczce'),
         ],
         viewBox='0 0 400 280',
         opis='Polarne cząsteczki wody łączą się wiązaniami wodorowymi.',
         uwaga='Polarność cząsteczki wody wyjaśnia, dlaczego jest dobrym rozpuszczalnikiem substancji jonowych i polarnych.'),
]

S['b-bialka'] = [
    dict(typ='rysunek', tytul='Poziomy struktury białka', viewBox='0 0 400 270', svg=_bialko(),
         znaczniki=[
             (100, 40, 110, 80, 'Struktura I-rzędowa', 'sekwencja aminokwasów'),
             (270, 40, 340, 80, 'Struktura II-rzędowa (α-helisa)', 'wiązania wodorowe w szkielecie łańcucha'),
             (120, 155, 200, 255, 'Struktura III-rzędowa', 'przestrzenne pofałdowanie łańcucha'),
             (310, 220, 380, 255, 'Struktura IV-rzędowa', 'kilka łańcuchów, np. hemoglobina'),
             (250, 160, 380, 140, 'Grupa prostetyczna (hem)', 'niebiałkowa część białka złożonego'),
         ],
         opis='Od sekwencji aminokwasów do białka z kilku podjednostek.',
         uwaga='Denaturacja niszczy struktury II-, III- i IV-rzędowe, ale nie rozrywa wiązań peptydowych — struktura I-rzędowa zostaje.'),
]

S['b-lipidy'] = [
    dict(typ='rysunek', tytul='Tłuszcz właściwy i fosfolipid', viewBox='0 0 400 250', svg=_lipidy(),
         znaczniki=[
             (50, 100, 20, 230, 'Glicerol', ''),
             (98, 60, 98, 18, 'Wiązanie estrowe', ''),
             (160, 100, 200, 20, 'Kwas tłuszczowy nasycony', 'proste łańcuchy'),
             (150, 140, 220, 190, 'Kwas tłuszczowy nienasycony', 'wiązanie podwójne — zagięcie łańcucha'),
             (280, 50, 350, 30, 'Hydrofilowa główka', 'reszta fosforanowa z grupą polarną'),
             (280, 160, 350, 180, 'Hydrofobowe ogony', 'dwa kwasy tłuszczowe'),
         ],
         opis='Porównanie budowy triacyloglicerolu i fosfolipidu.',
         uwaga='Fosfolipidy mają budowę amfipatyczną — dlatego w wodzie same tworzą dwuwarstwy, z których zbudowane są błony.'),
]

S['b-odpornosc'] = [
    dict(typ='rysunek', tytul='Budowa przeciwciała', svg=_ab,
         znaczniki=[
             (190, 250, 100, 270, 'Łańcuch ciężki', ''),
             (113, 105, 40, 140, 'Łańcuch lekki', ''),
             (79, 50, 150, 30, 'Miejsce wiązania antygenu', 'część zmienna — inna w każdym przeciwciele'),
             (200, 207, 300, 230, 'Mostki disiarczkowe', 'łączą łańcuchy'),
             (210, 265, 300, 285, 'Część stała', 'wspólna dla przeciwciał danej klasy'),
             (60, 28, 20, 90, 'Antygen', ''),
         ],
         opis='Przeciwciało klasy IgG (immunoglobulina).',
         uwaga='Jedno przeciwciało ma dwa identyczne miejsca wiązania antygenu — może więc sklejać antygeny (aglutynacja).'),
]

S['b-krazenie'] = [
    dict(typ='rysunek', tytul='Przekroje naczyń krwionośnych', viewBox='0 40 400 210', svg=_naczynia,
         znaczniki=[
             (80, 99, 40, 60, 'Gruba warstwa mięśniowa tętnicy', 'wytrzymuje wysokie ciśnienie'),
             (80, 140, 150, 60, 'Wąskie światło tętnicy', ''),
             (225, 140, 290, 60, 'Szerokie światło żyły', 'niskie ciśnienie, zastawki zapobiegają cofaniu'),
             (161, 140, 165, 210, 'Cienka ściana żyły', ''),
             (345, 124, 375, 70, 'Ściana z jednej warstwy śródbłonka', 'wymiana substancji z tkankami'),
         ],
         opis='Tętnica, żyła i naczynie włosowate w przekroju poprzecznym.',
         uwaga='Krew w żyłach kończyn płynie dzięki zastawkom i skurczom otaczających mięśni (pompa mięśniowa).'),
]

S['b-enzymy'] = [
    dict(typ='rysunek', tytul='Hamowanie kompetycyjne i niekompetycyjne', viewBox='0 40 400 220', svg=_inhib,
         znaczniki=[
             (90, 160, 20, 90, 'Enzym', ''),
             (85, 130, 150, 60, 'Inhibitor kompetycyjny w centrum aktywnym', 'podobny do substratu'),
             (85, 92, 40, 60, 'Substrat', 'nie może wejść do centrum aktywnego'),
             (310, 207, 370, 240, 'Inhibitor niekompetycyjny', 'wiąże się poza centrum aktywnym'),
             (285, 145, 370, 120, 'Zmienione centrum aktywne', 'substrat do niego nie pasuje'),
         ],
         opis='Po lewej — inhibitor zajmuje centrum aktywne; po prawej — zmienia kształt enzymu.',
         uwaga='Zwiększenie stężenia substratu znosi hamowanie kompetycyjne, ale nie niekompetycyjne.'),
]

S['b-czasowniki'] = [
    dict(typ='proces', tytul='Odpowiedź na polecenie „wyjaśnij”',
         kroki=[('Przeczytaj, o jakie zjawisko pyta polecenie'), ('Wskaż przyczynę', 'mechanizm biologiczny'),
                ('Połącz przyczynę ze skutkiem', 'np. „ponieważ…, więc…”'), ('Użyj terminologii biologicznej'),
                ('Odnieś się do danych z materiału, jeśli są')],
         uwaga='Sam opis zjawiska („co się dzieje”) to nie wyjaśnienie — trzeba podać „dlaczego”.'),
]

S['b-dane'] = [
    dict(typ='proces', tytul='Analiza tabeli z wynikami doświadczenia',
         kroki=[('Przeczytaj tytuł i nagłówki', 'co i w jakich jednostkach mierzono'), ('Ustal zmienną niezależną i zależną'),
                ('Znajdź próbę kontrolną'), ('Porównaj wartości — szukaj trendu'), ('Sprawdź wyjątki i wartości skrajne'),
                ('Sformułuj wniosek', 'tylko taki, który wynika z danych')],
         uwaga='Wniosek z tabeli nie może wykraczać poza badany zakres — np. jeśli badano 10–30°C, nie wnioskuj o 50°C.'),
]

S['b-weglowodany'] = [
    dict(typ='proces', tytul='Trawienie skrobi u człowieka',
         kroki=[('Skrobia w pokarmie'), ('Amylaza ślinowa w jamie ustnej', 'dekstryny, maltoza'), ('Inaktywacja amylazy w kwaśnym żołądku'),
                ('Amylaza trzustkowa w dwunastnicy', 'maltoza'), ('Maltaza jelitowa', 'glukoza'), ('Wchłanianie glukozy do krwi')],
         uwaga='Amylaza działa w pH obojętnym lub lekko zasadowym — w żołądku (pH ok. 2) traci aktywność.'),
]

S['b-sciana'] = [
    dict(typ='proces', tytul='Plazmoliza i deplazmoliza',
         kroki=[('Komórka w roztworze hipertonicznym'), ('Woda wypływa z wakuoli', 'osmoza'), ('Protoplast kurczy się i odstaje od ściany', 'plazmoliza'),
                ('Przeniesienie do wody destylowanej'), ('Woda napływa do wakuoli'), ('Protoplast przylega do ściany', 'deplazmoliza, turgor')],
         uwaga='Ściana komórkowa nie dopuszcza do pęknięcia komórki roślinnej w roztworze hipotonicznym — erytrocyt w tych warunkach ulega hemolizie.'),
]

S['b-wspoldzialanie'] = [
    dict(typ='proces', tytul='Rozpoznawanie współdziałania genów po rozszczepieniu w F₂',
         kroki=[('Zsumuj liczby potomstwa', 'zwykle 16 części'), ('Porównaj ze stosunkiem 9 : 3 : 3 : 1'),
                ('9 : 7', 'geny komplementarne'), ('9 : 3 : 4', 'epistaza recesywna'), ('12 : 3 : 1', 'epistaza dominująca'),
                ('15 : 1', 'geny dublujące (polimeria)')],
         uwaga='Suma części równa 16 wskazuje na dwa geny dziedziczone niezależnie — zmienia się tylko sposób ujawniania fenotypów.'),
]

S['b-plec'] = [
    dict(typ='proces', tytul='Determinacja płci u człowieka',
         kroki=[('Zapłodnienie', 'plemnik z X lub Y'), ('Zygota XX lub XY'), ('Gen SRY na chromosomie Y'),
                ('Przekształcenie gonad w jądra', 'u zarodka XY'), ('Wydzielanie testosteronu'), ('Rozwój męskich narządów płciowych'),
                ('Brak SRY — rozwój jajników i cech żeńskich')],
         uwaga='O płci dziecka decyduje plemnik, bo komórka jajowa zawsze ma chromosom X.'),
]

S['b-choroby-genetyczne'] = [
    dict(typ='proces', tytul='Mukowiscydoza — od mutacji do objawów',
         kroki=[('Mutacja genu CFTR', 'dziedziczenie autosomalne recesywne'), ('Nieprawidłowe białko kanału chlorkowego'),
                ('Zaburzony transport Cl⁻ i wody przez błony'), ('Gęsty, lepki śluz'), ('Zatykanie oskrzeli i przewodów trzustki'),
                ('Nawracające zakażenia płuc i zaburzenia trawienia')],
         uwaga='Choroba ujawnia się tylko u homozygot recesywnych — rodzice chorego dziecka są zwykle zdrowymi nosicielami.'),
    dict(typ='proces', tytul='Anemia sierpowata — od mutacji do objawów',
         kroki=[('Substytucja w genie β-globiny', 'A → T'), ('Zmiana kodonu GAG na GUG'), ('Walina zamiast kwasu glutaminowego'),
                ('Hemoglobina S polimeryzuje przy niskim stężeniu O₂'), ('Sierpowaty kształt erytrocytów'),
                ('Zatykanie naczyń i szybki rozpad krwinek')],
         uwaga='Heterozygoty są bardziej odporne na malarię — dlatego allel sierpowaty jest częsty w Afryce.'),
]

S['b-biotech-tradycyjna'] = [
    dict(typ='proces', tytul='Wytwarzanie jogurtu',
         kroki=[('Pasteryzacja mleka', 'usunięcie niepożądanych drobnoustrojów'), ('Schłodzenie do ok. 42°C'),
                ('Dodanie kultur bakterii fermentacji mlekowej'), ('Fermentacja mleczanowa', 'laktoza → kwas mlekowy'),
                ('Spadek pH i ścięcie białek mleka'), ('Schłodzenie produktu')],
         uwaga='Kwas mlekowy obniża pH, przez co białka (kazeina) koagulują, a rozwój bakterii gnilnych jest hamowany.'),
    dict(typ='proces', tytul='Produkcja wina',
         kroki=[('Zgniecenie owoców'), ('Dodanie drożdży', 'lub drożdże naturalnie obecne na skórce'), ('Fermentacja alkoholowa w warunkach beztlenowych'),
                ('Uwalnianie CO₂'), ('Klarowanie i dojrzewanie wina')],
         uwaga='Dostęp tlenu sprzyjałby rozwojowi bakterii octowych, które utleniają etanol do kwasu octowego.'),
]

S['b-systematyka'] = [
    dict(typ='proces', tytul='Rangi taksonomiczne — od najwyższej',
         kroki=[('Domena'), ('Królestwo'), ('Typ', 'u roślin i grzybów: gromada'), ('Gromada', 'u roślin: klasa'), ('Rząd'), ('Rodzina'), ('Rodzaj'), ('Gatunek')],
         uwaga='Nazwa gatunkowa składa się z nazwy rodzaju i epitetu gatunkowego — np. Homo sapiens.'),
]

S['b-populacje-genetyka'] = [
    dict(typ='proces', tytul='Efekt założyciela',
         kroki=[('Duża populacja wyjściowa'), ('Kilka osobników zasiedla nowy obszar'), ('Pula genowa założycieli nie odzwierciedla populacji wyjściowej'),
                ('Rozród w izolacji'), ('Wysoka częstość rzadkich alleli', 'np. chorób genetycznych')],
         uwaga='Efekt założyciela tłumaczy np. częstość niektórych chorób w izolowanych społecznościach (amisze).'),
    dict(typ='proces', tytul='Efekt wąskiego gardła',
         kroki=[('Liczna populacja o dużej zmienności'), ('Katastrofa lub masowe polowania'), ('Przeżywa niewiele osobników'),
                ('Utrata wielu alleli', 'przypadkowa, nie dobór'), ('Odbudowa liczebności przy małej zmienności genetycznej')],
         uwaga='Przykład: żubr — cała populacja pochodzi od kilkunastu osobników, co zmniejsza jej zmienność i odporność na choroby.'),
]

S['b-nisza'] = [
    dict(typ='proces', tytul='Konkurencyjne wypieranie (zasada Gausego)',
         kroki=[('Dwa gatunki o takiej samej niszy'), ('Konkurencja o ten sam zasób'), ('Jeden gatunek wykorzystuje zasób skuteczniej'),
                ('Spadek liczebności drugiego gatunku'), ('Wyparcie słabszego konkurenta lub zróżnicowanie nisz')],
         uwaga='W klasycznym doświadczeniu Gause hodował dwa gatunki pantofelków — w jednej hodowli przetrwał tylko jeden.'),
]

S['b-kregowce'] = [
    dict(typ='cykl', tytul='Krążenie krwi u ryby',
         kroki=[('Przedsionek serca'), ('Komora serca'), ('Naczynia skrzelowe', 'natlenienie krwi'), ('Aorta grzbietowa'),
                ('Naczynia włosowate narządów'), ('Żyły — powrót krwi odtlenowanej do serca')],
         uwaga='Ryby mają jeden obieg krwi, a przez serce płynie tylko krew odtlenowana.'),
    dict(typ='proces', tytul='Wymiana gazowa w skrzelach ryby',
         kroki=[('Woda wpływa przez otwór gębowy'), ('Przepływ przez łuki skrzelowe'), ('Woda omywa blaszki skrzelowe'),
                ('Przeciwprądowa wymiana gazów', 'krew płynie przeciwnie do wody'), ('Woda wypływa spod pokryw skrzelowych')],
         uwaga='Mechanizm przeciwprądowy pozwala pobrać z wody nawet ok. 80% tlenu.'),
]

S['b-bezkregowce'] = [
    dict(typ='cykl', tytul='Cykl rozwojowy motylicy wątrobowej',
         kroki=[('Dorosła motylica w przewodach żółciowych owcy'), ('Jaja wydalane z kałem'), ('Orzęsiona larwa w wodzie'),
                ('Rozwój w ślimaku błotniarce', 'żywiciel pośredni'), ('Larwy opuszczają ślimaka i otorbiają się na roślinach'),
                ('Zjedzenie roślin przez owcę')],
         uwaga='Zwalczanie ślimaków przerywa cykl — to sposób zapobiegania motyliczności w hodowli.'),
]

S['b-specjacja'] = [
    dict(typ='proces', tytul='Specjacja przez poliploidyzację',
         kroki=[('Mieszaniec dwóch gatunków roślin', 'zwykle bezpłodny'), ('Podwojenie liczby chromosomów', 'np. błąd podziału'),
                ('Chromosomy mają pary w mejozie'), ('Płodny poliploid'), ('Brak płodnego potomstwa z gatunkami rodzicielskimi', 'natychmiastowa izolacja rozrodcza')],
         uwaga='Tak powstało wiele roślin uprawnych, np. pszenica zwyczajna (heksaploid).'),
]

S['b-regulacja'] = [
    dict(typ='proces', tytul='Operon tryptofanowy — represja',
         kroki=[('Mało tryptofanu: represor nieaktywny', 'geny syntezy tryptofanu działają'), ('Wzrost stężenia tryptofanu'),
                ('Tryptofan wiąże się z represorem', 'korepresor'), ('Aktywny represor przyłącza się do operatora'),
                ('Zahamowanie transkrypcji genów'), ('Synteza tryptofanu ustaje')],
         uwaga='To przykład ujemnego sprzężenia zwrotnego — produkt szlaku wyłącza geny własnej syntezy.'),
]

S['b-oddychanie-czl'] = [
    dict(typ='proces', tytul='Transport CO₂ z tkanek do płuc',
         kroki=[('Powstanie CO₂ w mitochondriach'), ('Dyfuzja CO₂ do krwi'), ('W erytrocytach: CO₂ + H₂O → H₂CO₃', 'anhydraza węglanowa'),
                ('Dysocjacja na H⁺ i HCO₃⁻'), ('Transport HCO₃⁻ w osoczu', 'główna forma transportu'), ('W płucach odwrócenie reakcji i dyfuzja CO₂ do pęcherzyków')],
         uwaga='Ok. 70% CO₂ transportowane jest jako jony wodorowęglanowe, ok. 20% — w połączeniu z hemoglobiną.'),
]

S['b-replikacja'] = [
    dict(typ='proces', tytul='Doświadczenie Meselsona i Stahla',
         kroki=[('Hodowla bakterii na pożywce z ciężkim azotem ¹⁵N'), ('Przeniesienie na pożywkę z ¹⁴N'),
                ('Po 1 pokoleniu: jeden prążek DNA pośredni', 'wyklucza replikację konserwatywną'),
                ('Po 2 pokoleniach: prążek pośredni i lekki', 'wyklucza replikację rozproszoną'), ('Wniosek: replikacja jest semikonserwatywna')],
         uwaga='Prążki uzyskano przez wirowanie DNA w gradiencie gęstości chlorku cezu.'),
]

S['b-gen'] = [
    dict(typ='proces', tytul='Doświadczenie Griffitha',
         kroki=[('Szczep S (z otoczką) zabija myszy'), ('Szczep R (bez otoczki) nie zabija myszy'), ('Zabity wysoką temperaturą szczep S nie zabija myszy'),
                ('Mieszanina zabitego S i żywego R zabija myszy'), ('Z martwych myszy izoluje się żywe bakterie S'), ('Wniosek: zaszła transformacja bakterii')],
         uwaga='Avery i współpracownicy wykazali później, że czynnikiem transformującym jest DNA.'),
]

S['b-techniki'] = [
    dict(typ='proces', tytul='Ustalanie ojcostwa metodą profilu DNA',
         kroki=[('Pobranie próbek DNA dziecka, matki i domniemanego ojca'), ('Powielenie wybranych sekwencji powtórzonych (STR) metodą PCR'),
                ('Rozdział fragmentów elektroforezą'), ('Odczyt prążków'), ('Prążki dziecka nieobecne u matki muszą występować u ojca')],
         uwaga='Każdy prążek dziecka pochodzi od matki albo od ojca — tak rozwiązuje się zadania z profilami DNA.'),
]

S['b-techniki'] += [
    dict(typ='proces', tytul='Sekwencjonowanie DNA metodą Sangera',
         kroki=[('Matryca DNA, starter, polimeraza i nukleotydy'), ('Dodatek znakowanych dideoksynukleotydów (ddNTP)', 'brak grupy 3′-OH'),
                ('Synteza nici przerywana losowo po wbudowaniu ddNTP'), ('Fragmenty różnej długości'),
                ('Rozdział fragmentów elektroforezą kapilarną'), ('Odczyt sekwencji z kolejności znaczników')],
         uwaga='Dideoksynukleotyd nie ma grupy –OH przy węglu 3′, więc kolejny nukleotyd nie może zostać dołączony.'),
]

S['b-rozmnazanie'] = [
    dict(typ='proces', tytul='Rozwój zarodkowy — od zygoty do narządów',
         kroki=[('Zygota'), ('Bruzdkowanie', 'podziały mitotyczne bez wzrostu'), ('Blastula (u człowieka blastocysta)'),
                ('Gastrulacja', 'powstanie listków zarodkowych'), ('Ektoderma, mezoderma, endoderma'), ('Organogeneza', 'np. układ nerwowy z ektodermy')],
         uwaga='Z ektodermy powstają naskórek i układ nerwowy, z mezodermy — mięśnie, kości i krew, z endodermy — nabłonek przewodu pokarmowego i płuc.'),
]

S['b-hormony'] = [
    dict(typ='proces', tytul='Reakcja na długotrwały stres (oś podwzgórze–przysadka–nadnercza)',
         kroki=[('Czynnik stresowy'), ('Podwzgórze wydziela kortykoliberynę (CRH)'), ('Przysadka wydziela ACTH'),
                ('Kora nadnerczy wydziela kortyzol'), ('Wzrost glukozy we krwi, hamowanie odporności'), ('Kortyzol hamuje wydzielanie CRH i ACTH')],
         uwaga='Szybką reakcję na stres wywołuje adrenalina z rdzenia nadnerczy, długotrwałą — kortyzol z kory nadnerczy.'),
]

S['b-bezkregowce'] += [
    dict(typ='proces', tytul='Przeobrażenie niezupełne owada',
         kroki=[('Jajo'), ('Larwa podobna do postaci dorosłej', 'np. nimfa szarańczy'), ('Kolejne linienia i wzrost'), ('Postać dorosła (imago)')],
         uwaga='W przeobrażeniu niezupełnym nie ma stadium poczwarki.'),
]
