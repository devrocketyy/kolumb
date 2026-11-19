# Treści kursu biologii — porcja 62: fiszki (biochemia, komórka, metabolizm, genetyka).
T = {}

T['b-woda'] = dict(F=[
 ('Woda — wysokie ciepło właściwe a organizmy', 'Woda wolno się nagrzewa i stygnie — stabilizuje temperaturę ciała i zbiorników wodnych.'),
 ('Lód lżejszy od wody — znaczenie', 'Lód unosi się i izoluje wodę pod spodem — zbiorniki nie zamarzają do dna, organizmy przeżywają zimę.'),
 ('Sole mineralne — formy w organizmie', 'Jony rozpuszczone w płynach (Na⁺, K⁺, Cl⁻) lub związki nierozpuszczalne w strukturach (fosforan wapnia w kościach).'),
])

T['b-weglowodany'] = dict(F=[
 ('Celuloza — dlaczego człowiek jej nie trawi?', 'Brak enzymu rozkładającego wiązania β-glikozydowe; celuloza działa jako błonnik pokarmowy.'),
 ('Chityna — występowanie', 'Ściany komórkowe grzybów i pancerzyki stawonogów; polisacharyd zawierający azot.'),
 ('Próba Trommera — wynik', 'Cukry redukujące (glukoza, fruktoza, maltoza) po ogrzaniu z Cu(OH)₂ dają ceglastoczerwony osad Cu₂O.'),
])

T['b-bialka'] = dict(F=[
 ('Struktura I-rzędowa białka', 'Kolejność aminokwasów w łańcuchu, utrwalona wiązaniami peptydowymi — określona przez gen.'),
 ('Struktura II-rzędowa białka', 'Lokalne pofałdowanie łańcucha (α-helisa, β-harmonijka) stabilizowane wiązaniami wodorowymi między grupami szkieletu.'),
 ('Struktura III- i IV-rzędowa', 'III — przestrzenne ułożenie całego łańcucha (oddziaływania grup R, mostki disiarczkowe); IV — połączenie kilku łańcuchów (np. hemoglobina).'),
 ('Reakcja biuretowa', 'Wykrywa wiązania peptydowe — z Cu²⁺ w środowisku zasadowym białko daje fioletowe zabarwienie.'),
])

T['b-lipidy'] = dict(F=[
 ('Fosfolipidy — budowa', 'Glicerol, dwa kwasy tłuszczowe (hydrofobowe ogony) i reszta fosforanowa z dodatkową grupą (hydrofilowa głowa).'),
 ('Steroidy — przykłady', 'Cholesterol, hormony płciowe (testosteron, estradiol), kortyzol, witamina D, kwasy żółciowe.'),
 ('Tłuszcze nasycone a nienasycone', 'Nasycone: brak wiązań podwójnych, stałe (łój); nienasycone: wiązania podwójne, ciekłe (oleje roślinne).'),
])

T['b-kwasy'] = dict(F=[
 ('Reguła Chargaffa', 'W dwuniciowym DNA liczba A = T i G = C, więc puryny stanowią 50% zasad.'),
 ('Nukleotyd — budowa', 'Zasada azotowa + cukier pięciowęglowy (ryboza lub deoksyryboza) + reszta fosforanowa.'),
 ('Antyrównoległość nici DNA', 'Nici biegną w przeciwnych kierunkach (5′→3′ i 3′→5′) — ma to znaczenie przy replikacji i transkrypcji.'),
])

T['b-blony'] = dict(F=[
 ('Model płynnej mozaiki', 'Dwuwarstwa fosfolipidów z rozproszonymi, ruchomymi białkami; cholesterol reguluje płynność, glikokaliks na zewnątrz.'),
 ('Roztwór hipertoniczny — skutek dla komórki roślinnej', 'Woda wypływa, protoplast odstaje od ściany — plazmoliza.'),
 ('Roztwór hipotoniczny — skutek dla erytrocytu', 'Woda napływa, komórka pęcznieje i pęka — hemoliza (brak ściany komórkowej).'),
])

T['b-jadro'] = dict(F=[
 ('Jąderko — funkcja', 'Miejsce syntezy rRNA i składania podjednostek rybosomów.'),
 ('Pory jądrowe — funkcja', 'Kontrolowany transport między jądrem a cytoplazmą: mRNA i podjednostki rybosomów na zewnątrz, białka (np. polimerazy) do środka.'),
 ('Lizosomy — funkcje', 'Trawienie wewnątrzkomórkowe pobranego materiału i zużytych organelli (autofagia) dzięki hydrolazom w kwaśnym pH.'),
 ('Peroksysomy', 'Pęcherzyki z enzymami utleniającymi (np. katalazą rozkładającą H₂O₂) — detoksykacja, rozkład kwasów tłuszczowych.'),
])

T['b-mitochondria'] = dict(F=[
 ('Dowody endosymbiozy', 'Mitochondria i chloroplasty mają własne koliste DNA, rybosomy 70S, dwie błony i dzielą się niezależnie od komórki.'),
 ('Grzebienie mitochondrialne — znaczenie', 'Fałdy błony wewnętrznej zwiększają powierzchnię dla łańcucha oddechowego i syntazy ATP.'),
])

T['b-enzymy'] = dict(F=[
 ('Inhibicja kompetycyjna', 'Inhibitor podobny do substratu wiąże się z centrum aktywnym; można ją znieść, zwiększając stężenie substratu.'),
 ('Inhibicja niekompetycyjna', 'Inhibitor wiąże się poza centrum aktywnym i zmienia kształt enzymu; wzrost stężenia substratu jej nie znosi.'),
 ('Koenzymy — przykłady', 'NAD⁺, FAD, koenzym A — często pochodne witamin z grupy B; przenoszą elektrony lub grupy chemiczne.'),
 ('Energia aktywacji a enzym', 'Enzym obniża energię aktywacji reakcji, nie zmieniając jej bilansu energetycznego ani położenia równowagi.'),
])

T['b-fotosynteza'] = dict(F=[
 ('Faza zależna od światła — produkty', 'ATP, NADPH i O₂ (z fotolizy wody); zachodzi w błonach tylakoidów.'),
 ('Cykl Calvina — etapy', 'Karboksylacja (RuBisCO wiąże CO₂ z RuBP) → redukcja do aldehydu 3-fosfoglicerynowego (ATP, NADPH) → regeneracja RuBP.'),
 ('Czynniki ograniczające fotosyntezę', 'Natężenie światła, stężenie CO₂, temperatura, dostępność wody — tempo wyznacza czynnik w minimum.'),
])

T['b-oddychanie'] = dict(F=[
 ('Etapy oddychania tlenowego — lokalizacja', 'Glikoliza — cytozol; reakcja pomostowa i cykl Krebsa — matriks; łańcuch oddechowy — wewnętrzna błona mitochondrium.'),
 ('Tlen w oddychaniu — rola', 'Końcowy akceptor elektronów w łańcuchu oddechowym; łączy się z H⁺ w wodę.'),
 ('Chemiosmoza', 'Gradient protonów utworzony przez łańcuch oddechowy napędza syntazę ATP, przez którą H⁺ wracają do matriks.'),
])

T['b-replikacja'] = dict(F=[
 ('Nić wiodąca a opóźniona', 'Wiodąca — synteza ciągła w kierunku widełek; opóźniona — nieciągła, we fragmentach Okazakiego łączonych przez ligazę.'),
 ('Replikacja semikonserwatywna', 'Każda nowa cząsteczka DNA zawiera jedną nić starą i jedną nowo zsyntetyzowaną (doświadczenie Meselsona i Stahla).'),
])

T['b-krzyzowki'] = dict(F=[
 ('Krzyżówka testowa — cel', 'Ustalenie genotypu osobnika o fenotypie dominującym przez skrzyżowanie z homozygotą recesywną.'),
 ('I prawo Mendla', 'Allele jednego genu rozchodzą się do różnych gamet — każda gameta ma jeden allel danego genu.'),
 ('II prawo Mendla', 'Allele różnych genów (leżących na różnych chromosomach) dziedziczą się niezależnie — w F2 rozszczepienie 9:3:3:1.'),
])

T['b-mutacje'] = dict(F=[
 ('Czynniki mutagenne — podział', 'Fizyczne (promieniowanie UV, X, γ), chemiczne (benzopiren, iperyt, kwas azotawy), biologiczne (niektóre wirusy).'),
 ('Mutacja somatyczna a generatywna', 'Somatyczna — dotyczy komórek ciała, nie przechodzi na potomstwo; generatywna — w gametach, jest dziedziczona.'),
])
