# Treści kursu chemii — porcja 13: pytania ABCD (po 3 na temat), odpowiedzi o zbliżonej długości.
T = {}
def q(uid, *pyt):
    T[uid] = dict(F=[], Q=list(pyt))

q('c-polecenia',
 ('Polecenie „Uzasadnij” wymaga:', ['*podania przyczyny z odwołaniem do danych', 'samego podania odpowiedzi', 'narysowania wykresu', 'podania wzoru ogólnego'], 'Uzasadnienie = związek przyczynowo-skutkowy.'),
 ('Wynik liczbowy bez jednostki według CKE jest:', ['*traktowany jako błędny', 'akceptowany zawsze', 'akceptowany w kluczu', 'oceniany na 1 pkt'], 'Wielkość mianowana wymaga jednostki.'),
 ('Gdy uczeń poda dwie odpowiedzi, w tym jedną błędną:', ['*otrzymuje 0 pkt', 'otrzymuje pełne punkty', 'otrzymuje połowę punktów', 'egzaminator wybiera lepszą'], 'Zasada CKE.'))
q('c-obliczenia',
 ('Wynik 0,0004567 z dokładnością do dwóch cyfr znaczących to:', ['*4,6·10⁻⁴', '0,00', '4,5·10⁻⁴', '0,0005'], 'Zaokrąglamy 4,567 → 4,6.'),
 ('Przy przeliczaniu gęstości 1,18 g/cm³ na g/dm³ otrzymamy:', ['*1180 g/dm³', '118 g/dm³', '11,8 g/dm³', '0,00118 g/dm³'], '1 dm³ = 1000 cm³.'),
 ('Temperatura 25°C w kelwinach to:', ['*298 K', '248 K', '25 K', '373 K'], 'T = t + 273.'))
q('c-doswiadczenia',
 ('Obserwacją (a nie wnioskiem) jest zdanie:', ['*wydzielają się pęcherzyki gazu', 'powstaje wodór', 'zachodzi reakcja redoks', 'tworzy się chlorek cynku'], 'Obserwacja opisuje to, co widać.'),
 ('Próba kontrolna w doświadczeniu służy do:', ['*porównania wyników z próbą badaną', 'zwiększenia wydajności reakcji', 'przyspieszenia reakcji', 'zastąpienia próby badanej'], 'Pozwala wykluczyć inne czynniki.'),
 ('Zmienną niezależną w badaniu wpływu temperatury na szybkość reakcji jest:', ['*temperatura', 'szybkość reakcji', 'stężenie kwasu', 'masa substratu'], 'Zmienną niezależną zmienia badacz.'))
q('c-atom',
 ('Liczba neutronów w ⁵⁶Fe (Z = 26) to:', ['*30', '26', '56', '82'], '56 − 26.'),
 ('Izotopy danego pierwiastka różnią się liczbą:', ['*neutronów', 'protonów', 'elektronów', 'powłok'], 'Ta sama liczba atomowa.'),
 ('Liczba elektronów w jonie S²⁻ (Z = 16) wynosi:', ['*18', '16', '14', '32'], 'Dwa elektrony więcej.'))
q('c-konfiguracja',
 ('Konfiguracja walencyjna miedzi w stanie podstawowym to:', ['*4s¹ 3d¹⁰', '4s² 3d⁹', '4s² 3d¹⁰', '4s¹ 3d⁹'], 'Zapełniona podpowłoka d.'),
 ('Maksymalna liczba elektronów na podpowłoce d wynosi:', ['*10', '6', '14', '2'], '5 orbitali × 2.'),
 ('Liczba niesparowanych elektronów w atomie azotu wynosi:', ['*3', '1', '2', '5'], '2p³ — reguła Hunda.'))
q('c-okresowosc',
 ('W grupie od góry do dołu promień atomowy:', ['*rośnie', 'maleje', 'nie zmienia się', 'najpierw maleje'], 'Przybywa powłok.'),
 ('Największą elektroujemność ma:', ['*fluor', 'tlen', 'chlor', 'azot'], 'Skala Paulinga: F = 4,0.'),
 ('W okresie od lewej do prawej charakter metaliczny:', ['*maleje', 'rośnie', 'nie zmienia się', 'najpierw rośnie'], 'Rośnie ładunek jądra.'))
q('c-promieniotworczosc',
 ('Przemiana α zmniejsza liczbę masową o:', ['*4', '2', '1', '0'], 'Emisja jądra helu.'),
 ('Po trzech okresach półtrwania pozostaje izotopu:', ['*12,5%', '25%', '33%', '6,25%'], '(1/2)³.'),
 ('Przemiana β⁻ zwiększa liczbę atomową o:', ['*1', '2', '0', '4'], 'Neutron → proton + elektron.'))
q('c-wiazania',
 ('Wiązanie jonowe powstaje, gdy różnica elektroujemności jest:', ['*duża (powyżej ok. 1,7)', 'równa zeru', 'mniejsza od 0,4', 'ujemna'], 'Przybliżona granica.'),
 ('Wiązanie kowalencyjne niespolaryzowane występuje w:', ['*Cl₂', 'HCl', 'NaCl', 'H₂O'], 'Te same atomy.'),
 ('Wiązanie metaliczne polega na:', ['*przyciąganiu kationów i elektronów', 'uwspólnieniu pary elektronów', 'przyciąganiu jonów o różnych ładunkach', 'oddziaływaniu dipoli'], 'Gaz elektronowy.'))
q('c-geometria',
 ('Cząsteczka CH₄ ma kształt:', ['*tetraedru', 'płaski kwadratowy', 'liniowy', 'trygonalny płaski'], 'sp³, 109,5°.'),
 ('Cząsteczka H₂O ma kształt:', ['*kątowy (zgięty)', 'liniowy', 'tetraedryczny', 'płaski trójkątny'], 'Dwie wolne pary na tlenie.'))
q('c-oddzialywania',
 ('Siły van der Waalsa rosną wraz z:', ['*masą i powierzchnią cząsteczki', 'polarnością wiązań', 'liczbą jonów', 'temperaturą'], 'Siły dyspersyjne.'),
 ('Wiązania wodorowe NIE tworzą się między cząsteczkami:', ['*CH₄', 'H₂O', 'NH₃', 'HF'], 'Brak H przy O, N, F.'))
q('c-mol',
 ('Liczba moli w 9 g wody wynosi:', ['*0,5 mola', '1 mol', '2 mole', '0,25 mola'], '9/18.'),
 ('W 1 molu CO₂ jest atomów tlenu:', ['*2·Nₐ', 'Nₐ', '3·Nₐ', '0,5·Nₐ'], 'Dwa atomy O w cząsteczce.'),
 ('Masa molowa Ca(OH)₂ wynosi:', ['*74 g/mol', '57 g/mol', '58 g/mol', '92 g/mol'], '40 + 2·17.'))
q('c-wzory',
 ('Wzór empiryczny etynu (C₂H₂) to:', ['*CH', 'C₂H₂', 'CH₂', 'C₂H'], 'Stosunek 1 : 1.'),
 ('Zawartość procentowa tlenu w H₂O wynosi ok.:', ['*89%', '11%', '50%', '67%'], '16/18.'))
q('c-stechiometria',
 ('Ile dm³ CO₂ (w. n.) powstaje ze spalenia 1 mola propanu?', ['*67,2 dm³', '22,4 dm³', '44,8 dm³', '89,6 dm³'], '3 mole CO₂.'),
 ('Wydajność 75% oznacza, że z 40 g teoretycznego produktu otrzymano:', ['*30 g', '53 g', '10 g', '75 g'], '0,75 · 40.'))
q('c-energetyka',
 ('Reakcja egzotermiczna ma:', ['*ΔH < 0', 'ΔH > 0', 'ΔH = 0', 'zawsze K < 1'], 'Ciepło oddane.'),
 ('Entalpia tworzenia tlenu O₂ wynosi:', ['*0 kJ/mol', '−286 kJ/mol', '+249 kJ/mol', '−394 kJ/mol'], 'Pierwiastek w stanie standardowym.'),
 ('Odwrócenie równania termochemicznego powoduje:', ['*zmianę znaku ΔH', 'podwojenie ΔH', 'brak zmiany ΔH', 'wyzerowanie ΔH'], 'Prawo Hessa.'))
q('c-szybkosc',
 ('Katalizator przyspiesza reakcję, ponieważ:', ['*obniża energię aktywacji', 'zwiększa ΔH reakcji', 'przesuwa równowagę', 'zwiększa stężenie'], 'Inna droga reakcji.'),
 ('Jednostka stałej szybkości reakcji I rzędu to:', ['*s⁻¹', 'mol·dm⁻³·s⁻¹', 'dm³·mol⁻¹·s⁻¹', 'mol⁻¹'], 'v/c.'),
 ('Rozdrobnienie substancji stałej zwiększa szybkość, ponieważ:', ['*rośnie powierzchnia kontaktu', 'maleje energia aktywacji', 'rośnie temperatura', 'zmienia się ΔH'], 'Więcej zderzeń.'))
q('c-rownowaga',
 ('Wartość stałej równowagi zmienia:', ['*tylko temperatura', 'stężenie substratów', 'ciśnienie', 'katalizator'], 'K = f(T).'),
 ('Dla reakcji H₂ + I₂ ⇄ 2HI wzrost ciśnienia:', ['*nie przesuwa równowagi', 'przesuwa ją w prawo', 'przesuwa ją w lewo', 'zwiększa K'], 'Równa liczba moli gazów.'),
 ('Usuwanie produktu z układu w równowadze:', ['*przesuwa równowagę w prawo', 'przesuwa ją w lewo', 'zmniejsza K', 'zatrzymuje reakcję'], 'Reguła przekory.'))
q('c-stezenia',
 ('Rozcieńczenie roztworu 2 razy powoduje, że Cm:', ['*maleje 2 razy', 'rośnie 2 razy', 'nie zmienia się', 'maleje 4 razy'], 'n stałe, V × 2.'),
 ('W 250 g roztworu 4% jest substancji:', ['*10 g', '4 g', '25 g', '40 g'], '0,04 · 250.'))
q('c-rozpuszczalnosc',
 ('Rozpuszczalność gazów w wodzie ze wzrostem temperatury:', ['*maleje', 'rośnie', 'nie zmienia się', 'najpierw rośnie'], 'Dlatego ciepłe napoje szybciej wietrzeją.'),
 ('Roztwór, który w danej temperaturze nie rozpuści więcej substancji, to roztwór:', ['*nasycony', 'nienasycony', 'rozcieńczony', 'koloidalny'], 'Definicja.'))
q('c-mieszanie',
 ('Zmieszano 200 g roztworu 10% z 200 g wody. Stężenie wynosi:', ['*5%', '10%', '20%', '2,5%'], '20 g / 400 g.'),
 ('Woda w regule krzyża ma stężenie:', ['*0%', '100%', '50%', '1%'], 'Brak substancji rozpuszczonej.'))
q('c-kwasy-zasady',
 ('Sprzężoną zasadą kwasu HSO₄⁻ jest:', ['*SO₄²⁻', 'H₂SO₄', 'HSO₃⁻', 'OH⁻'], 'Oddanie protonu.'),
 ('Drobiną amfiprotyczną jest:', ['*HCO₃⁻', 'Cl⁻', 'NH₄⁺', 'Na⁺'], 'Może oddać lub przyjąć proton.'),
 ('Najmocniejszym kwasem jest:', ['*HI', 'HF', 'HCl', 'HBr'], 'Najsłabsze wiązanie H–X.'))
q('c-ph',
 ('pH roztworu NaOH o stężeniu 0,001 mol/dm³ wynosi:', ['*11', '3', '13', '10'], 'pOH = 3.'),
 ('Dziesięciokrotne rozcieńczenie roztworu HCl o pH 2 daje pH:', ['*3', '1', '20', '2,1'], '[H⁺] maleje 10 razy.'),
 ('Fenoloftaleina w roztworze o pH 5 jest:', ['*bezbarwna', 'malinowa', 'żółta', 'niebieska'], 'Zmiana barwy od pH 8,2.'))
q('c-hydroliza',
 ('Odczyn zasadowy ma wodny roztwór:', ['*K₂CO₃', 'NH₄Cl', 'NaCl', 'KNO₃'], 'Hydroliza anionu CO₃²⁻.'),
 ('Odczyn kwasowy ma wodny roztwór:', ['*AlCl₃', 'Na₂S', 'CH₃COONa', 'KCl'], 'Hydroliza kationu Al³⁺.'),
 ('Hydrolizie NIE ulega:', ['*KNO₃', 'Na₂CO₃', 'NH₄NO₃', 'FeCl₃'], 'Sól mocnego kwasu i mocnej zasady.'))
q('c-jonowe',
 ('Jonami widzami w reakcji HCl + NaOH są:', ['*Na⁺ i Cl⁻', 'H⁺ i OH⁻', 'Na⁺ i OH⁻', 'H⁺ i Cl⁻'], 'Nie zmieniają się.'),
 ('Biały osad nierozpuszczalny w kwasach daje z Ba²⁺ jon:', ['*SO₄²⁻', 'CO₃²⁻', 'Cl⁻', 'NO₃⁻'], 'BaSO₄.'))
q('c-tlenki',
 ('Tlenkiem zasadowym jest:', ['*CaO', 'SO₂', 'Al₂O₃', 'CO'], 'Reaguje z kwasami.'),
 ('Tlenkiem obojętnym jest:', ['*NO', 'NO₂', 'N₂O₅', 'SO₃'], 'Nie reaguje z kwasami ani zasadami.'))
q('c-wodorotlenki-kwasy',
 ('Wodorotlenkiem amfoterycznym jest:', ['*Zn(OH)₂', 'NaOH', 'Mg(OH)₂', 'Ca(OH)₂'], 'Reaguje z kwasami i zasadami.'),
 ('Kwasem nietrwałym jest:', ['*H₂CO₃', 'H₂SO₄', 'HCl', 'H₃PO₄'], 'Rozkłada się na CO₂ i H₂O.'))
q('c-sole',
 ('Biały bezwodny CuSO₄ po dodaniu wody staje się:', ['*niebieski', 'zielony', 'czarny', 'żółty'], 'Powstaje hydrat.'))
q('c-metale',
 ('Wodoru z kwasu solnego NIE wypiera:', ['*miedź', 'cynk', 'magnez', 'żelazo'], 'E° > 0.'),
 ('Żółtą barwę płomienia daje:', ['*sód', 'potas', 'lit', 'miedź'], 'Test płomieniowy.'))
q('c-niemetale',
 ('Halogenem, który wypiera brom z KBr, jest:', ['*chlor', 'jod', 'astat', 'żaden'], 'Cl₂ silniejszy utleniacz.'),
 ('Odmianą alotropową węgla przewodzącą prąd jest:', ['*grafit', 'diament', 'karbid', 'węglan'], 'Zdelokalizowane elektrony.'))
q('c-stopnie',
 ('Stopień utlenienia tlenu w H₂O₂ wynosi:', ['*−I', '−II', '0', '+I'], 'Nadtlenek.'),
 ('Stopień utlenienia manganu w KMnO₄ wynosi:', ['*+VII', '+VI', '+IV', '+II'], '1 + x − 8 = 0.'))
q('c-bilans',
 ('W reakcji redoks utleniacz:', ['*przyjmuje elektrony', 'oddaje elektrony', 'nie zmienia stopnia utlenienia', 'zawsze jest metalem'], 'Sam się redukuje.'),
 ('W środowisku kwasowym brakujący tlen w równaniu połówkowym uzupełniamy:', ['*cząsteczkami H₂O', 'jonami OH⁻', 'jonami H⁺', 'cząsteczkami O₂'], 'Wodór — jonami H⁺.'))
q('c-ogniwa',
 ('Anodą w ogniwie Daniella jest:', ['*cynk', 'miedź', 'klucz elektrolityczny', 'roztwór CuSO₄'], 'Niższy potencjał.'),
 ('SEM ogniwa liczymy jako:', ['*E(katody) − E(anody)', 'E(anody) − E(katody)', 'E(katody) + E(anody)', 'E(anody) · E(katody)'], 'Wynik dodatni.'))
q('c-elektroliza',
 ('Podczas elektrolizy wodnego roztworu NaCl na katodzie wydziela się:', ['*wodór', 'sód', 'chlor', 'tlen'], 'Redukuje się woda.'),
 ('Podczas elektrolizy wodnego roztworu CuSO₄ (elektrody Pt) na anodzie wydziela się:', ['*tlen', 'miedź', 'wodór', 'SO₂'], 'Utlenia się woda.'))
q('c-izomeria',
 ('Izomerami są:', ['*butan i 2-metylopropan', 'etan i eten', 'metanol i etanol', 'propan i propen'], 'Ten sam wzór C₄H₁₀.'),
 ('Izomeria cis–trans występuje w:', ['*but-2-enie', 'but-1-enie', 'propenie', 'etenie'], 'Różne podstawniki przy obu C.'))
q('c-alkany',
 ('Alkany ulegają głównie reakcji:', ['*substytucji rodnikowej', 'addycji elektrofilowej', 'polimeryzacji', 'eliminacji'], 'Z halogenami w świetle.'),
 ('Wzór ogólny cykloalkanów to:', ['*CₙH₂ₙ', 'CₙH₂ₙ₊₂', 'CₙH₂ₙ₋₂', 'CₙHₙ'], 'Jak alkenów.'))
q('c-alkeny',
 ('Eten odbarwia wodę bromową w reakcji:', ['*addycji', 'substytucji', 'eliminacji', 'kondensacji'], 'Przyłączenie Br₂.'),
 ('Główny produkt addycji HBr do propenu to:', ['*2-bromopropan', '1-bromopropan', '1,2-dibromopropan', 'bromoetan'], 'Reguła Markownikowa.'),
 ('Hybrydyzacja węgla w etynie to:', ['*sp', 'sp²', 'sp³', 'sp³d'], 'Wiązanie potrójne.'))
q('c-areny',
 ('Benzen reaguje z bromem w obecności FeBr₃ w reakcji:', ['*substytucji elektrofilowej', 'addycji elektrofilowej', 'substytucji rodnikowej', 'eliminacji'], 'Zachowanie aromatyczności.'),
 ('Grupa –OH w pierścieniu kieruje podstawnik w położenie:', ['*orto i para', 'tylko meta', 'tylko orto', 'tylko para'], 'Grupa aktywująca.'))
q('c-alkohole',
 ('Alkoholem II-rzędowym jest:', ['*propan-2-ol', 'propan-1-ol', '2-metylopropan-2-ol', 'metanol'], '–OH przy węglu połączonym z dwoma C.'),
 ('Glicerol z Cu(OH)₂ daje:', ['*szafirowy roztwór', 'ceglasty osad', 'srebrne lustro', 'żółty osad'], 'Kompleks — sąsiednie –OH.'),
 ('Alkohol III-rzędowy przy łagodnym utlenianiu:', ['*nie utlenia się', 'daje keton', 'daje aldehyd', 'daje kwas'], 'Brak H przy C–OH.'))
q('c-karbonylowe',
 ('Ceglastoczerwony osad w próbie Trommera to:', ['*Cu₂O', 'CuO', 'Cu(OH)₂', 'Cu'], 'Tlenek miedzi(I).'),
 ('Redukcja ketonu prowadzi do:', ['*alkoholu II-rzędowego', 'alkoholu I-rzędowego', 'kwasu', 'aldehydu'], 'C=O → CH–OH.'))
q('c-karboksylowe',
 ('Kwas octowy reaguje z Na₂CO₃ z wydzieleniem:', ['*CO₂', 'H₂', 'O₂', 'CO'], 'Mocniejszy kwas wypiera słabszy.'),
 ('Kwasem nienasyconym jest kwas:', ['*oleinowy', 'stearynowy', 'palmitynowy', 'octowy'], 'Jedno wiązanie C=C.'))
q('c-estry',
 ('Hydroliza zasadowa estru jest:', ['*nieodwracalna', 'odwracalna', 'niemożliwa', 'reakcją addycji'], 'Powstaje anion karboksylanowy.'),
 ('Produktem reakcji kwasu mrówkowego z metanolem jest:', ['*mrówczan metylu', 'octan metylu', 'metanian etylu', 'eter dimetylowy'], 'HCOOCH₃.'))
q('c-aminy',
 ('Amina II-rzędowa to:', ['*(CH₃)₂NH', 'CH₃NH₂', '(CH₃)₃N', 'CH₃CONH₂'], 'Dwie grupy alkilowe przy N.'),
 ('Roztwór metyloaminy barwi fenoloftaleinę na:', ['*malinowo', 'żółto', 'nie barwi', 'niebiesko'], 'Odczyn zasadowy.'))
q('c-aminokwasy',
 ('Achiralnym aminokwasem białkowym jest:', ['*glicyna', 'alanina', 'seryna', 'cysteina'], 'Dwa atomy H przy C-α.'),
 ('Wiązanie peptydowe ma postać:', ['*–CO–NH–', '–COO–', '–NH–NH–', '–O–O–'], 'Amidowe.'),
 ('W punkcie izoelektrycznym aminokwas występuje głównie jako:', ['*jon obojnaczy', 'kation', 'anion', 'cząsteczka obojętna'], 'Ładunek wypadkowy 0.'))
q('c-cukry',
 ('Skrobia z roztworem jodu daje barwę:', ['*granatową', 'czerwoną', 'żółtą', 'zieloną'], 'Kompleks z amylozą.'),
 ('Glukoza jest:', ['*aldoheksozą', 'ketoheksozą', 'aldopentozą', 'disacharydem'], '6 C, grupa –CHO.'))
q('c-chemia-zycia',
 ('Reakcja biuretowa wykrywa:', ['*wiązania peptydowe', 'pierścienie aromatyczne', 'grupy –SH', 'wiązania estrowe'], 'Fioletowe zabarwienie.'),
 ('Utwardzanie olejów polega na:', ['*uwodornieniu wiązań C=C', 'hydrolizie estrów', 'utlenianiu', 'zmydlaniu'], 'Margaryna.'))
q('c-srodowisko',
 ('Główną przyczyną kwaśnych deszczy są tlenki:', ['*siarki i azotu', 'węgla(IV)', 'węgla(II)', 'krzemu'], 'Tworzą H₂SO₄ i HNO₃.'),
 ('Katalizator samochodowy przekształca CO w:', ['*CO₂', 'C', 'CH₄', 'O₂'], 'Utlenianie.'))
