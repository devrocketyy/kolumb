# Treści kursu biologii — porcja 29: duża partia fiszek i pytań ABCD.
T = {}

T['b-woda'] = dict(F=[
 ('Sole mineralne w organizmie — formy', 'Występują jako jony rozpuszczone w płynach (Na⁺, K⁺, Cl⁻) lub jako składniki struktur (fosforany wapnia w kościach).'),
 ('Makroelementy u człowieka — przykłady', 'Ca, P, K, Na, Cl, Mg, S — potrzebne w ilościach powyżej 100 mg dziennie.'),
 ('Mikroelementy u człowieka — przykłady', 'Fe, Zn, Cu, I, F, Se, Mn — potrzebne w śladowych ilościach (składniki enzymów, hormonów).'),
 ('Fluor — znaczenie', 'Wzmacnia szkliwo zębów, chroni przed próchnicą.'),
], Q=[
 ('Mikroelementem dla człowieka jest:', ['wapń', 'sód', '*cynk', 'fosfor'], 'Śladowe ilości.'),
 ('Jod jest składnikiem:', ['hemoglobiny', '*hormonów tarczycy', 'chlorofilu', 'insuliny'], 'Tyroksyna.'),
])

T['b-bialka'] = dict(F=[
 ('Hemoglobina — budowa', 'Białko o strukturze IV-rzędowej: 4 łańcuchy (2α, 2β), każdy z hemem z jonem Fe²⁺ wiążącym O₂.'),
 ('Kolagen — budowa', 'Białko fibrylarne z trzech skręconych łańcuchów (potrójna helisa); najliczniejsze białko ciała.'),
 ('Białka a aminokwasy — liczby', 'Białka budowane są z 20 rodzajów aminokwasów; kolejność decyduje o funkcji.'),
], Q=[
])

T['b-weglowodany'] = dict(F=[
 ('Cukry proste — podział', 'Według liczby atomów węgla: triozy (C3), pentozy (C5 — ryboza, deoksyryboza), heksozy (C6 — glukoza, fruktoza, galaktoza).'),
 ('Fruktoza', 'Heksoza — cukier owoców i miodu; najsłodszy cukier prosty; składnik sacharozy.'),
], Q=[
 ('Deoksyryboza jest:', ['heksozą', '*pentozą', 'triozą', 'disacharydem'], 'Składnik DNA.'),
])

T['b-lipidy'] = dict(F=[
 ('Lipoproteiny LDL i HDL', 'Kompleksy transportujące cholesterol we krwi: LDL — do tkanek (nadmiar sprzyja miażdżycy), HDL — z tkanek do wątroby („dobry”).'),
 ('Karotenoidy', 'Barwniki lipidowe (karoteny, ksantofile) — barwniki pomocnicze fotosyntezy, prekursory witaminy A.'),
], Q=[
 ('Nadmiar którego cholesterolu sprzyja miażdżycy?', ['HDL', '*LDL', 'obu jednakowo', 'żadnego'], 'Transport do tkanek.'),
])

T['b-kwasy'] = dict(F=[
 ('Funkcje RNA — podsumowanie', 'mRNA — matryca do translacji; tRNA — transport aminokwasów; rRNA — budowa i kataliza w rybosomie; inne RNA — regulacja.'),
 ('DNA a RNA — stabilność', 'DNA (dwuniciowy, bez grupy –OH przy C2′) jest trwalszy — dobry do przechowywania informacji; RNA — krótkotrwały.'),
], Q=[
 ('Dlaczego DNA jest trwalsze niż RNA?', ['zawiera uracyl', '*ma deoksyrybozę i dwie nici', 'jest krótsze', 'nie ma reszt fosforanowych'], 'Brak 2′-OH.'),
])

T['b-blony'] = dict(F=[
 ('Receptory błonowe', 'Białka błony wiążące sygnały (hormony, neuroprzekaźniki) i przekazujące informację do wnętrza komórki.'),
 ('Połączenia międzykomórkowe u zwierząt', 'Ścisłe (uszczelniają nabłonki), zwierające (desmosomy — wytrzymałość), szczelinowe (komunikacja).'),
], Q=[
 ('Połączenia ścisłe między komórkami nabłonka:', ['umożliwiają przepływ jonów', '*uszczelniają przestrzenie międzykomórkowe', 'przewodzą impulsy', 'wiążą hormony'], 'Bariera.'),
])

T['b-mitochondria'] = dict(F=[
 ('Dlaczego mitochondriów jest dużo w mięśniach i plemnikach?', 'Komórki te potrzebują dużo ATP do skurczu i ruchu.'),
 ('Chloroplasty w komórkach — gdzie najwięcej?', 'W miękiszu palisadowym liścia — najsilniej oświetlonym.'),
], Q=[
 ('Najwięcej mitochondriów mają komórki:', ['tłuszczowe żółte', '*mięśnia sercowego', 'naskórka', 'erytrocyty'], 'Duże zapotrzebowanie na ATP.'),
])

T['b-enzymy'] = dict(F=[
 ('Nazewnictwo enzymów', 'Najczęściej końcówka „-aza” dodana do nazwy substratu lub reakcji (np. laktaza, polimeraza, dehydrogenaza).'),
 ('Wpływ metali ciężkich na enzymy', 'Jony Hg²⁺, Pb²⁺ wiążą się z grupami –SH i trwale unieczynniają enzymy (inhibicja nieodwracalna).'),
], Q=[
 ('Jony rtęci hamują enzymy w sposób:', ['kompetycyjny odwracalny', '*nieodwracalny', 'allosteryczny aktywujący', 'zależny od substratu'], 'Wiązanie –SH.'),
])

T['b-fotosynteza'] = dict(F=[
 ('Chemosynteza a fotosynteza', 'Obie są autotroficzne; w chemosyntezie energia pochodzi z utleniania związków nieorganicznych (NH₃, H₂S, Fe²⁺), a nie ze światła.'),
 ('Doświadczenie Engelmanna', 'Bakterie tlenowe gromadziły się przy nici skrętnicy w miejscach oświetlonych światłem czerwonym i niebieskim — tam najintensywniejsza fotosynteza.'),
], Q=[
 ('Energię do syntezy związków organicznych z utleniania H₂S czerpią:', ['sinice w jeziorach', '*bakterie siarkowe (chemosynteza)', 'rośliny C4 w upale', 'grzyby saprotroficzne'], 'Chemoautotrofy.'),
])

T['b-mitoza-mejoza'] = dict(Q=[
 ('Ile chromosomów ma komórka 2n = 12 w telofazie I mejozy (w jednym jądrze)?', ['12', '*6', '24', '3'], 'n po redukcji.'),
 ('Komórka 2n = 6 po replikacji zawiera cząsteczek DNA:', ['6', '*12', '3', '24'], '4c.'),
])

T['b-regulacja'] = dict(Q=[
 ('miRNA wycisza geny przez:', ['metylację DNA', '*wiązanie z mRNA i hamowanie translacji', 'zmianę sekwencji promotora', 'rozkład białek'], 'Interferencja RNA.'),
])

T['b-wspoldzialanie'] = dict(F=[
 ('Epistaza recesywna — przykład', 'Barwa sierści labradorów: ee daje sierść żółtą niezależnie od genu B (czarna/brązowa) — stosunek 9 : 3 : 4.'),
 ('Allele wielokrotne u królików', 'Barwa sierści: C (dzika) > cᶜʰ (szynszyla) > cʰ (himalajska) > c (albinos) — szereg alleli o różnej dominacji.'),
], Q=[
 ('U labradorów stosunek 9 czarne : 3 brązowe : 4 żółte wskazuje na:', ['kodominację', '*epistazę recesywną', 'geny komplementarne', 'allel letalny'], '9:3:4.'),
])

T['b-rodowody'] = dict(Q=[
 ('W rodowodzie choroby autosomalnej recesywnej chore dziecko zdrowych rodziców oznacza, że rodzice są:', ['homozygotami dominującymi', '*heterozygotami (nosicielami)', 'homozygotami recesywnymi', 'hemizygotami'], 'Aa × Aa.'),
])

T['b-techniki'] = dict(F=[
 ('Klonowanie genu', 'Uzyskanie wielu kopii genu przez wprowadzenie go do wektora i namnożenie w bakteriach (lub przez PCR).'),
 ('Transformacja bakterii w laboratorium', 'Wprowadzanie plazmidu do bakterii np. przez szok cieplny lub elektroporację.'),
], Q=[
 ('Elektroporacja to wprowadzanie DNA do komórek za pomocą:', ['wirusa', '*impulsu elektrycznego', 'mikroigły', 'bakterii glebowej'], 'Pory w błonie.'),
])

T['b-wirusy'] = dict(Q=[
 ('Antybiotyków nie stosuje się w leczeniu grypy, ponieważ:', ['grypa zawsze mija sama w ciągu jednego dnia', '*wirusy nie mają struktur, na które działają antybiotyki', 'grypę wywołują grzyby, a nie wirusy', 'antybiotyki uszkadzają przeciwciała przeciw grypie'], 'Brak ściany, rybosomów 70S.'),
])

T['b-protisty'] = dict(Q=[
 ('Przenosicielem zarodźca malarii jest:', ['mucha tse-tse', '*komar widliszek', 'kleszcz', 'pchła'], 'Samica komara.'),
])

T['b-organy'] = dict(F=[
 ('Budowa anatomiczna liścia', 'Skórka górna i dolna (szparki), miękisz palisadowy, miękisz gąbczasty, wiązki przewodzące (nerwy).'),
 ('Kłącze', 'Podziemna łodyga gromadząca materiały zapasowe i służąca rozmnażaniu wegetatywnemu (np. perz, kosaciec).'),
 ('Rozłogi', 'Płożące się pędy nadziemne, na których węzłach powstają nowe rośliny (np. truskawka).'),
], Q=[
 ('Kłącze perzu to:', ['korzeń spichrzowy', '*podziemna łodyga', 'liść spichrzowy', 'korzeń przybyszowy'], 'Ma węzły i pąki.'),
])

T['b-gospodarka-wodna'] = dict(F=[
 ('Czynniki zwiększające transpirację', 'Wysoka temperatura, niska wilgotność powietrza, wiatr, silne światło (otwarte szparki).'),
 ('Kseromorfizm', 'Przystosowania roślin do suchych siedlisk: gruba kutykula, zagłębione szparki, zwinięte liście, owłosienie, tkanki wodne.'),
], Q=[
 ('Transpiracja jest najsilniejsza przy:', ['wysokiej wilgotności powietrza', '*wietrze i niskiej wilgotności', 'zamkniętych szparkach', 'niskiej temperaturze'], 'Gradient pary wodnej.'),
])

T['b-rozmnazanie-roslin'] = dict(F=[
 ('Kiełkowanie ziarna pyłku', 'Na znamieniu słupka ziarno pyłku tworzy łagiewkę, która rośnie przez szyjkę do zalążka i przez okienko wnika do woreczka zalążkowego.'),
 ('Owocostan', 'Zespół owoców powstałych z kwiatostanu (np. ananas, morwa).'),
], Q=[
 ('Łagiewka pyłkowa wnika do zalążka przez:', ['znamię', '*okienko (mikropyle)', 'szyjkę słupka', 'osłonki'], 'Wejście do woreczka.'),
])

T['b-bezkregowce'] = dict(F=[
 ('Rozwój skorupiaków morskich', 'Wiele skorupiaków morskich ma larwę pływającą (nauplius) — rozwój złożony.'),
 ('Pierścienice — układ nerwowy', 'Zwój nadgardzielowy, obrączka okołogardzielowa i brzuszny łańcuszek nerwowy z parą zwojów w każdym segmencie.'),
], Q=[
 ('Łańcuszkowy układ nerwowy mają:', ['parzydełkowce', '*pierścienice i stawonogi', 'kręgowce', 'gąbki'], 'Brzuszny łańcuszek.'),
])

T['b-kregowce'] = dict(F=[
 ('Ptaki — trawienie', 'Wole (gromadzenie, zmiękczanie), żołądek gruczołowy i mięśniowy (rozcieranie z kamykami), brak zębów.'),
 ('Ssaki — mózg', 'Silnie rozwinięta kora mózgowa (u wielu pofałdowana) — złożone zachowania i uczenie się.'),
], Q=[
 ('Żołądek mięśniowy ptaków służy do:', ['wydzielania pepsyny', '*mechanicznego rozcierania pokarmu', 'magazynowania wody', 'wchłaniania tłuszczów'], 'Brak zębów.'),
])

T['b-tkanki-zwierzece'] = dict(F=[
 ('Komórki tuczne', 'Komórki tkanki łącznej zawierające histaminę i heparynę — udział w stanie zapalnym i alergii.'),
 ('Limfa', 'Płyn tkankowy w naczyniach limfatycznych; zawiera limfocyty, transportuje tłuszcze z jelit.'),
], Q=[
 ('Heparynę i histaminę zawierają:', ['erytrocyty', '*komórki tuczne', 'fibroblasty', 'osteocyty'], 'Tkanka łączna.'),
])

T['b-odzywianie'] = dict(F=[
 ('Uzębienie człowieka', 'Dorosły: 32 zęby — 8 siekaczy, 4 kły, 8 przedtrzonowców, 12 trzonowców; mleczne: 20.'),
 ('Ślinianki człowieka', 'Przyuszne, podżuchwowe i podjęzykowe — wydzielają ok. 1–1,5 l śliny dziennie.'),
 ('Odruch połykania', 'Nagłośnia zamyka krtań, podniebienie miękkie — jamę nosową; pokarm przesuwa się do przełyku.'),
], Q=[
 ('Dorosły człowiek ma zębów:', ['20', '28', '*32', '36'], 'Z ósemkami.'),
])

T['b-oddychanie-czl'] = dict(Q=[
 ('Płuca rozprężają się w czasie wdechu dzięki:', ['skurczowi mięśni gładkich płuc', '*przyleganiu do ścian klatki przez opłucną', 'wypełnianiu się krwią', 'pracy przepony w wydechu'], 'Opłucna.'),
])

T['b-hormony'] = dict(Q=[
 ('Prolaktyna pobudza:', ['owulację', '*wytwarzanie mleka', 'skurcze macicy', 'wzrost kości'], 'Przedni płat przysadki.'),
])

T['b-rozmnazanie'] = dict(Q=[
 ('Zapłodnienie in vitro polega na zapłodnieniu:', ['w macicy', '*poza organizmem kobiety', 'w jajowodzie', 'bez plemnika'], 'Pozaustrojowe.'),
])

T['b-skora'] = dict(F=[
 ('Grubość naskórka a ochrona', 'Najgrubszy na stopach i dłoniach — ochrona przed ścieraniem; warstwa rogowa z martwych komórek z keratyną.'),
 ('Witamina D a skóra', 'Prowitamina w skórze pod wpływem UV-B przekształca się w witaminę D3 (cholekalcyferol).'),
], Q=[
 ('Witamina D powstaje w skórze pod wpływem:', ['podczerwieni', '*promieniowania UV', 'niskiej temperatury', 'potu'], 'UV-B.'),
])

T['b-dobor'] = dict(F=[
 ('Przystosowania ochronne zwierząt', 'Kamuflaż (barwy ochronne), ubarwienie ostrzegawcze (aposematyzm), mimikra, mimetyzm (upodobnienie do tła lub obiektów, np. patyczaki).'),
], Q=[
 ('Patyczak upodobniony do gałązki to przykład:', ['mimikry Batesa', '*mimetyzmu', 'ubarwienia ostrzegawczego', 'konwergencji'], 'Upodobnienie do otoczenia.'),
])

T['b-specjacja'] = dict(Q=[
 ('Homo sapiens powstał najpewniej w:', ['Europie', 'Azji', '*Afryce', 'Australii'], 'Ok. 300 tys. lat temu.'),
])

T['b-nisza'] = dict(F=[
 ('Rośliny cieniolubne i światłolubne', 'Cieniolubne (np. szczawik zajęczy) fotosyntezują wydajnie przy słabym świetle; światłolubne (np. sosna) wymagają silnego światła.'),
 ('Czynniki abiotyczne wody', 'Temperatura, zawartość tlenu, światło, pH, zasolenie, prąd wody — wpływają na rozmieszczenie organizmów wodnych.'),
], Q=[
 ('Rośliną cieniolubną runa leśnego jest:', ['sosna', '*szczawik zajęczy', 'brzoza', 'kukurydza'], 'Słabe światło.'),
])

T['b-ekosystem'] = dict(F=[
 ('Strefy jeziora', 'Litoral (strefa przybrzeżna z roślinami), pelagial (toń wodna z planktonem), profundal (głębia bez światła).'),
 ('Fitoplankton i zooplankton', 'Fitoplankton — mikroskopijne glony i sinice (producenci); zooplankton — drobne zwierzęta i pierwotniaki (konsumenci).'),
], Q=[
 ('Strefa przybrzeżna jeziora z roślinami to:', ['pelagial', '*litoral', 'profundal', 'bental głęboki'], 'Płytka woda.'),
])

T['b-ochrona'] = dict(Q=[
 ('Ochrona gatunkowa ścisła oznacza m.in. zakaz:', ['prowadzenia jakichkolwiek badań', '*zrywania, niszczenia i handlu okazami', 'fotografowania roślin w terenie', 'zakładania nowych parków narodowych'], 'Ochrona osobników.'),
])
