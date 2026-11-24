# Treści kursu chemii — porcja 8: Wstęp do chemii organicznej i węglowodory (XII, XIII).

T = {}

T['c-izomeria'] = dict(F=[
 ('Wyjaśnij pojęcie: izomery', 'Związki o tym samym wzorze sumarycznym, a różnej budowie (lub ułożeniu w przestrzeni), a więc różnych właściwościach.'),
 ('Izomeria łańcuchowa (szkieletowa)', 'Różny układ łańcucha węglowego (prosty lub rozgałęziony), np. butan i 2-metylopropan.'),
 ('Izomeria położenia', 'Różne położenie grupy funkcyjnej lub wiązania wielokrotnego, np. propan-1-ol i propan-2-ol; but-1-en i but-2-en.'),
 ('Izomeria funkcyjna', 'Różne grupy funkcyjne przy tym samym wzorze sumarycznym, np. etanol i eter dimetylowy (C₂H₆O); propanal i propanon.'),
 ('Wyjaśnij pojęcie: izomeria geometryczna (cis–trans)', 'Różne ułożenie podstawników względem płaszczyzny wiązania podwójnego (lub pierścienia); warunek: każdy atom C wiązania podwójnego ma dwa różne podstawniki.'),
 ('Typowy błąd: izomeria cis–trans', 'Wskazywanie izomerii geometrycznej, gdy jeden z atomów węgla wiązania podwójnego ma dwa jednakowe podstawniki (np. propen nie ma izomerów cis–trans).'),
 ('Wyjaśnij pojęcie: atom węgla asymetryczny (centrum stereogeniczne)', 'Atom węgla połączony z czterema różnymi podstawnikami.'),
 ('Wyjaśnij pojęcie: enancjomery', 'Izomery optyczne będące swoimi lustrzanymi odbiciami, nienakładalne na siebie (jak lewa i prawa dłoń); skręcają płaszczyznę światła spolaryzowanego w przeciwne strony.'),
 ('Wyjaśnij pojęcie: chiralność', 'Cecha cząsteczki, która nie jest identyczna ze swoim odbiciem lustrzanym — zwykle ma atom węgla asymetryczny.'),
 ('Wyjaśnij pojęcie: mieszanina racemiczna', 'Mieszanina równomolowa dwóch enancjomerów — optycznie nieczynna.'),
 ('Wzory Fischera', 'Projekcja cząsteczki z atomem asymetrycznym: linie poziome — wiązania „do obserwatora”, pionowe — „od obserwatora”; konfiguracja D/L według położenia grupy –OH (–NH₂) przy ostatnim asymetrycznym C.'),
 ('Liczba stereoizomerów przy n atomach asymetrycznych', 'Maksymalnie 2ⁿ (mniej, jeśli występują formy mezo).'),
 ('Wyjaśnij pojęcie: szereg homologiczny', 'Szereg związków o podobnej budowie i właściwościach, różniących się o grupę –CH₂–, opisany wzorem ogólnym (np. alkany CₙH₂ₙ₊₂).'),
 ('Zasady nazewnictwa IUPAC (podstawowe)', 'Najdłuższy łańcuch zawierający grupę funkcyjną; numeracja tak, by grupa (wiązanie wielokrotne) miała najniższy lokant; podstawniki alfabetycznie z lokantami.'),
 ('Wyjaśnij pojęcie: rzędowość atomu węgla', 'Liczba atomów węgla połączonych z danym atomem węgla: I-rzędowy (1 C), II-rzędowy (2 C), III-rzędowy (3 C), IV-rzędowy (4 C).'),
], Q=[
 ('Etanol i eter dimetylowy to izomery:', ['łańcuchowe', 'położenia', '*funkcyjne', 'optyczne'], 'Ten sam wzór C₂H₆O, różne grupy funkcyjne.'),
 ('Który związek ma izomery cis–trans?', ['propen', '*but-2-en', 'eten', '2-metylopropen'], 'Każdy C wiązania podwójnego ma dwa różne podstawniki.'),
 ('Atom węgla asymetryczny ma:', ['dwa wiązania podwójne', '*cztery różne podstawniki', 'trzy atomy wodoru', 'hybrydyzację sp²'], 'Warunek chiralności.'),
 ('Ile stereoizomerów może mieć związek z dwoma atomami asymetrycznymi (bez form mezo)?', ['2', '*4', '6', '8'], '2ⁿ = 2² = 4.'),
 ('Mieszanina racemiczna jest:', ['czynna optycznie', '*optycznie nieczynna', 'zawsze stała', 'czystym enancjomerem'], 'Skręcalności enancjomerów się znoszą.'),
])

T['c-alkany'] = dict(F=[
 ('Wzór ogólny alkanów', 'CₙH₂ₙ₊₂ — węglowodory nasycone, tylko wiązania pojedyncze, atomy C o hybrydyzacji sp³.'),
 ('Wzór ogólny cykloalkanów', 'CₙH₂ₙ (np. cykloheksan C₆H₁₂).'),
 ('Właściwości fizyczne alkanów', 'Niepolarne, nierozpuszczalne w wodzie; C₁–C₄ to gazy, C₅–C₁₇ ciecze, wyższe — ciała stałe; temperatura wrzenia rośnie z długością łańcucha.'),
 ('Spalanie całkowite alkanów', 'CₙH₂ₙ₊₂ + O₂ → CO₂ + H₂O, np. CH₄ + 2O₂ → CO₂ + 2H₂O.'),
 ('Spalanie niecałkowite', 'Przy niedostatku tlenu powstaje CO (półspalanie) lub C (sadza), np. 2CH₄ + 3O₂ → 2CO + 4H₂O.'),
 ('Substytucja rodnikowa — warunki i przykład', 'Reakcja z fluorowcem w świetle (hν): CH₄ + Cl₂ → CH₃Cl + HCl.'),
 ('Etapy mechanizmu substytucji rodnikowej', 'Inicjacja (rozpad Cl₂ na rodniki pod wpływem światła), propagacja (rodniki reagują z cząsteczkami, tworząc nowe rodniki), terminacja (łączenie się rodników).'),
 ('Wyjaśnij pojęcie: rodnik', 'Drobina z niesparowanym elektronem, np. Cl•, CH₃• — bardzo reaktywna.'),
 ('Który atom H alkanu najłatwiej ulega substytucji?', 'Przy węglu III-rzędowym, potem II-rzędowym, najtrudniej przy I-rzędowym.'),
 ('Kraking i reforming', 'Kraking — rozkład dłuższych węglowodorów na krótsze (więcej benzyny, alkeny); reforming — przekształcenie w węglowodory rozgałęzione i aromatyczne (wyższa liczba oktanowa).'),
 ('Wyjaśnij pojęcie: liczba oktanowa', 'Miara odporności benzyny na spalanie stukowe; izooktan = 100, heptan = 0.'),
 ('Wyjaśnij pojęcie: konformacja', 'Różne ułożenia atomów cząsteczki wynikające z obrotu wokół wiązań pojedynczych; cykloheksan przyjmuje konformację krzesłową (najtrwalszą) i łódkową.'),
], Q=[
 ('Wzór C₅H₁₂ należy do szeregu:', ['alkenów', '*alkanów', 'alkinów', 'cykloalkanów'], 'CₙH₂ₙ₊₂ dla n = 5.'),
 ('Pierwszym etapem substytucji rodnikowej jest:', ['propagacja', '*inicjacja — rozpad Cl₂ na rodniki', 'terminacja', 'addycja'], 'Pod wpływem światła.'),
 ('Produkty spalania całkowitego metanu to:', ['CO i H₂O', '*CO₂ i H₂O', 'C i H₂', 'CO₂ i H₂'], 'CH₄ + 2O₂ → CO₂ + 2H₂O.'),
 ('Reakcja metanu z chlorem w świetle to:', ['addycja', 'eliminacja', '*substytucja rodnikowa', 'polimeryzacja'], 'Atom H zastąpiony przez Cl.'),
])

T['c-alkeny'] = dict(F=[
 ('Wzór ogólny alkenów i alkinów', 'Alkeny CₙH₂ₙ (wiązanie C=C, sp²); alkiny CₙH₂ₙ₋₂ (wiązanie C≡C, sp).'),
 ('Addycja do alkenów — przykłady', 'Z H₂ (katalizator Ni/Pt) → alkan; z Br₂ → dibromopochodna; z HCl → chloropochodna; z H₂O (H⁺) → alkohol.'),
 ('Odbarwianie wody bromowej przez eten', 'CH₂=CH₂ + Br₂ → CH₂Br–CH₂Br (1,2-dibromoetan) — dowód obecności wiązania wielokrotnego.'),
 ('Reguła Markownikowa', 'Przy addycji HX do niesymetrycznego alkenu atom wodoru przyłącza się do atomu węgla, który ma więcej atomów wodoru (np. propen + HCl → 2-chloropropan).'),
 ('Mechanizm addycji elektrofilowej', 'Elektrofil (np. H⁺, Br⁺) atakuje bogate w elektrony wiązanie π, powstaje karbokation, do którego przyłącza się nukleofil.'),
 ('Utlenianie alkenów KMnO₄ (środowisko obojętne)', 'Powstaje diol (np. z etenu glikol etylenowy), a fioletowy roztwór odbarwia się i wytrąca brunatny MnO₂.'),
 ('Polimeryzacja alkenów', 'Łączenie wielu cząsteczek monomeru dzięki rozerwaniu wiązań π, np. n CH₂=CH₂ → (–CH₂–CH₂–)ₙ (polietylen).'),
 ('Otrzymywanie etenu', 'Dehydratacja etanolu (stężony H₂SO₄, ogrzewanie) albo kraking; eliminacja HX z chlorowcopochodnej (KOH w alkoholu).'),
 ('Otrzymywanie etynu (acetylenu)', 'Karbid z wodą: CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂.'),
 ('Addycja wody do etynu (reakcja Kuczerowa)', 'HC≡CH + H₂O → CH₃CHO (przez nietrwały alkohol winylowy; katalizator HgSO₄, H⁺) — powstaje etanal.'),
 ('Trimeryzacja etynu', '3HC≡CH → C₆H₆ (benzen) — w wysokiej temperaturze, z katalizatorem.'),
 ('Typowy błąd: wzór polimeru', 'Pozostawienie wiązania podwójnego w merze polimeru albo zapisanie monomeru zamiast powtarzającego się fragmentu z nawiasem i indeksem n.'),
], Q=[
 ('Propen + HBr — główny produkt według reguły Markownikowa:', ['1-bromopropan', '*2-bromopropan', '1,2-dibromopropan', 'propan'], 'H przyłącza się do C bogatszego w wodór.'),
 ('Wzór ogólny alkinów to:', ['CₙH₂ₙ₊₂', 'CₙH₂ₙ', '*CₙH₂ₙ₋₂', 'CₙHₙ'], 'Jedno wiązanie potrójne.'),
 ('Etyn otrzymuje się w reakcji:', ['etanolu z H₂SO₄', '*karbidu z wodą', 'metanu z chlorem', 'benzenu z wodorem'], 'CaC₂ + 2H₂O → C₂H₂ + Ca(OH)₂.'),
 ('Odbarwienie wody bromowej świadczy o obecności:', ['grupy –OH', '*wiązania wielokrotnego C=C lub C≡C', 'pierścienia benzenowego', 'grupy –COOH'], 'Addycja bromu.'),
])

T['c-areny'] = dict(F=[
 ('Budowa benzenu', 'Pierścień sześciu atomów C o hybrydyzacji sp²; sześć elektronów π zdelokalizowanych nad i pod płaszczyzną pierścienia (sekstet elektronowy). Wszystkie wiązania C–C jednakowej długości.'),
 ('Wyjaśnij pojęcie: aromatyczność', 'Szczególna trwałość płaskich, cyklicznych układów ze zdelokalizowanymi elektronami π (4n + 2 elektronów, reguła Hückla).'),
 ('Dlaczego benzen nie odbarwia wody bromowej?', 'Zdelokalizowany układ elektronów π jest trwały — benzen nie ulega łatwo addycji, tylko substytucji (z katalizatorem).'),
 ('Substytucja elektrofilowa — bromowanie benzenu', 'C₆H₆ + Br₂ → C₆H₅Br + HBr (katalizator FeBr₃).'),
 ('Nitrowanie benzenu', 'C₆H₆ + HNO₃ → C₆H₅NO₂ + H₂O (mieszanina nitrująca: stężony HNO₃ + stężony H₂SO₄).'),
 ('Wpływ podstawnika na kolejną substytucję (kierowanie)', 'Podstawniki I rodzaju (–OH, –NH₂, –CH₃, –Cl) kierują do pozycji orto i para; II rodzaju (–NO₂, –COOH, –CHO, –SO₃H) — do pozycji meta.'),
 ('Toluen z chlorem: w świetle a z katalizatorem', 'W świetle (hν) — substytucja rodnikowa w grupie –CH₃ (chlorek benzylu); z FeCl₃ — substytucja w pierścieniu (orto i para).'),
 ('Utlenianie toluenu', 'KMnO₄ utlenia grupę metylową do –COOH — powstaje kwas benzoesowy (pierścień pozostaje nienaruszony).'),
 ('Wielopierścieniowe węglowodory aromatyczne', 'Naftalen (2 pierścienie), antracen (3) — część z nich ma działanie rakotwórcze (np. benzo[a]piren w dymie i spalinach).'),
], Q=[
 ('Benzen z bromem w obecności FeBr₃ ulega:', ['addycji', '*substytucji elektrofilowej', 'substytucji rodnikowej', 'polimeryzacji'], 'Powstaje bromobenzen.'),
 ('Grupa –NO₂ w pierścieniu kieruje kolejny podstawnik w pozycję:', ['orto', 'para', '*meta', 'orto i para'], 'Podstawnik II rodzaju.'),
 ('Hybrydyzacja atomów węgla w benzenie to:', ['sp³', '*sp²', 'sp', 'sp³d'], 'Płaski pierścień.'),
 ('Produktem utleniania toluenu KMnO₄ jest:', ['fenol', '*kwas benzoesowy', 'benzaldehyd', 'benzen'], 'Utlenia się grupa –CH₃.'),
])
