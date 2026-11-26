# Geografia — porcja 18 (dogęszczanie: oceany, klimaty, rzeki, tektonika, ludność, rolnictwo, przemysł, polityka, środowisko).
T = {
'g-oceany': dict(F=[
 ('El Niño', 'Okresowe ocieplenie wód wschodniego Pacyfiku przy osłabieniu pasatów — co 2–7 lat.'),
 ('La Niña', 'Faza przeciwna do El Niño — silne pasaty, wyjątkowo zimne wody przy Ameryce Płd.'),
 ('Upwelling', 'Wynoszenie zimnych, bogatych w składniki odżywcze wód głębinowych ku powierzchni — bogate łowiska (Peru, Namibia).'),
 ('Prąd Humboldta (Peruwiański)', 'Zimny prąd wzdłuż zachodnich wybrzeży Ameryki Płd.; współtworzy pustynię Atakama.'),
 ('Prąd Benguelski', 'Zimny prąd wzdłuż zachodnich wybrzeży Afryki Płd.; pustynia Namib.'),
 ('Prąd Kuro-siwo', 'Ciepły prąd Pacyfiku wzdłuż wybrzeży Japonii.'),
],
Q=[
 ('Pustynia Atakama powstała m.in. pod wpływem prądu:', ['*Humboldta', 'Kuro-siwo', 'Golfsztromu', 'Brazylijskiego'], 'Zimny prąd stabilizuje powietrze.'),
 ('W czasie El Niño przy wybrzeżach Peru:', ['*woda jest cieplejsza i spadają połowy', 'woda jest zimniejsza i rosną połowy', 'wieją silniejsze pasaty', 'występuje susza i mróz'], 'Zanika upwelling.'),
 ('Wzdłuż wybrzeży Namibii płynie zimny prąd:', ['*Benguelskiego', 'Agulhas', 'Kuro-siwo', 'Golfsztromu'], 'Zimny prąd u wybrzeży Afryki Płd.'),
]),
'g-klimaty': dict(F=[
 ('Monsun letni w Indiach', 'Wilgotne wiatry znad Oceanu Indyjskiego (VI–IX) — pora deszczowa.'),
 ('Monsun zimowy', 'Suche wiatry z wychłodzonego wnętrza Azji ku oceanowi.'),
 ('Czerrapundżi', 'Jedno z najbardziej deszczowych miejsc świata (ponad 11 000 mm rocznie) — wzgórza Khasi w Indiach.'),
],
Q=[
 ('Monsun letni w Indiach przynosi:', ['*obfite opady', 'suszę i upały bez opadów', 'mroźne powietrze', 'burze piaskowe'], 'Wilgotne wiatry znad oceanu.'),
 ('Monsun zimowy wieje:', ['*z lądu nad ocean', 'z oceanu na ląd', 'wyłącznie wzdłuż wybrzeża', 'tylko w górach'], 'Wyż nad Azją.'),
]),
'g-rzeki': dict(F=[
 ('Terasa zalewowa', 'Najniższa część dna doliny, zalewana w czasie wezbrań.'),
 ('Terasa nadzalewowa', 'Wyższy poziom dawnego dna doliny, niezalewany współcześnie.'),
 ('Przełom rzeczny', 'Odcinek doliny, gdzie rzeka przecina pasmo wzniesień (Dunajec w Pieninach, Wisła pod Puławami).'),
 ('Kaptaż rzeczny', 'Przechwycenie górnego odcinka jednej rzeki przez drugą wskutek erozji wstecznej.'),
],
Q=[
 ('Przełom Dunajca znajduje się w:', ['*Pieninach', 'Tatrach', 'Bieszczadach', 'Sudetach'], 'Spływ flisacki.'),
 ('Część dna doliny zalewana podczas wezbrań to terasa:', ['*zalewowa', 'nadzalewowa', 'erozyjna', 'abrazyjna'], 'Najniższa.'),
]),
'g-tektonika': dict(F=[
 ('Granica przesuwcza (transformacyjna)', 'Płyty przesuwają się poziomo obok siebie — np. uskok San Andreas.'),
 ('Granica rozbieżna na lądzie', 'Wielkie Rowy Afrykańskie — kontynent rozrywa się, powstają rowy i jeziora.'),
 ('Grzbiet śródoceaniczny', 'Podmorskie pasmo wzdłuż granicy rozbieżnej — powstaje nowa skorupa oceaniczna.'),
 ('Wulkan tarczowy', 'Łagodne stoki z rzadkiej lawy bazaltowej (Mauna Loa) — plamy gorąca, granice rozbieżne.'),
],
Q=[
 ('Uskok San Andreas to przykład granicy:', ['*przesuwczej', 'rozbieżnej', 'subdukcyjnej', 'kolizyjnej'], 'Płyty mijają się poziomo.'),
 ('Wulkany tarczowe zbudowane są z lawy:', ['*bazaltowej, rzadkiej', 'andezytowej, lepkiej', 'ryolitowej, bardzo lepkiej', 'wyłącznie z popiołów'], 'Np. Hawaje.'),
]),
'g-pl-wody': dict(F=[
 ('Termoklina', 'Warstwa wody w jeziorze, w której temperatura gwałtownie spada z głębokością (latem).'),
 ('Gęstość wody a temperatura', 'Woda ma największą gęstość w 4°C — dlatego zimą przy dnie jezior jest ok. 4°C.'),
 ('Eutrofizacja jezior', 'Nadmiar biogenów (azot, fosfor) z nawozów i ścieków — zakwity glonów, niedobór tlenu.'),
],
Q=[
 ('Zimą przy dnie głębokiego jeziora temperatura wynosi ok.:', ['*4°C', '0°C', '−4°C', '10°C'], 'Największa gęstość wody.'),
 ('Eutrofizację jezior powoduje głównie:', ['*nadmiar azotu i fosforu', 'brak opadów', 'zakwaszenie przez kras', 'nadmiar soli kamiennej'], 'Nawozy, ścieki.'),
]),
'g-urbanizacja': dict(F=[
 ('Gentryfikacja', 'Zamiana starych dzielnic robotniczych w zamożne — wzrost cen, wypieranie dawnych mieszkańców.'),
 ('Rewitalizacja', 'Kompleksowa odnowa zdegradowanych obszarów miasta (np. Manufaktura w Łodzi, EC1).'),
 ('Megalopolis', 'Pas połączonych aglomeracji — np. BosWash (Boston–Waszyngton), Tokaido (Tokio–Osaka).'),
 ('Miasto globalne', 'Ośrodek o światowym znaczeniu w finansach i zarządzaniu — Nowy Jork, Londyn, Tokio.'),
],
Q=[
 ('Pas połączonych aglomeracji od Bostonu do Waszyngtonu to:', ['*megalopolis', 'konurbacja policentryczna', 'aglomeracja monocentryczna', 'strefa podmiejska'], 'BosWash.'),
 ('Zamiana dawnej fabryki w Łodzi w centrum Manufaktura to:', ['*rewitalizacji', 'suburbanizacji', 'dezurbanizacji', 'deglomeracji'], 'Np. Manufaktura.'),
]),
'g-rolnictwo': dict(F=[
 ('Struktura agrarna', 'Podział gospodarstw według wielkości; w Polsce dużo małych gospodarstw (średnio ok. 11 ha).'),
 ('Rolnictwo ekologiczne', 'Bez nawozów sztucznych i pestycydów; płodozmian, nawozy naturalne.'),
 ('Wspólna Polityka Rolna (WPR)', 'Polityka UE wspierająca rolników dopłatami i rozwojem obszarów wiejskich.'),
 ('Akwakultura', 'Hodowla ryb i owoców morza w zbiornikach — rośnie szybciej niż połowy (Chiny — lider).'),
],
Q=[
 ('Średnia wielkość gospodarstwa rolnego w Polsce wynosi ok.:', ['*11 ha', '1 ha', '100 ha', '500 ha'], 'Rozdrobnienie.'),
 ('Hodowla ryb w zbiornikach to:', ['*akwakultura', 'rybołówstwo dalekomorskie', 'akwaplaning', 'marikultura lodowa'], 'Chiny — lider.'),
]),
'g-przemysl': dict(F=[
 ('Czynniki lokalizacji przemysłu', 'Surowce, energia, siła robocza, rynek zbytu, transport, kapitał, technologie.'),
 ('Przemysł zaawansowanych technologii', 'Wymaga wykwalifikowanych kadr i ośrodków naukowych — Dolina Krzemowa, Bangalore.'),
 ('Technopolia', 'Ośrodki łączące uczelnie, laboratoria i firmy high-tech (Tsukuba, Sophia Antipolis).'),
 ('Deindustrializacja', 'Spadek znaczenia przemysłu tradycyjnego (górnictwo, hutnictwo) — np. Zagłębie Ruhry, Śląsk.'),
],
Q=[
 ('Dla przemysłu high-tech najważniejszym czynnikiem lokalizacji jest:', ['*kadra i zaplecze naukowe', 'bliskość złóż węgla', 'dostęp do taniej wody', 'żyzne gleby w okolicy'], 'Dolina Krzemowa.'),
 ('Spadek znaczenia górnictwa i hutnictwa to:', ['*deindustrializacja', 'industrializacja', 'reurbanizacja', 'konteneryzacja'], 'Np. Zagłębie Ruhry.'),
]),
'g-polityka': dict(F=[
 ('Konflikty o wodę', 'Np. o Nil (Etiopia, Sudan, Egipt), Tygrys i Eufrat (Turcja, Syria, Irak).'),
 ('Separatyzm', 'Dążenie regionu do oderwania od państwa — Katalonia, Szkocja, Kraj Basków.'),
 ('Uchodźca', 'Osoba zmuszona do opuszczenia kraju z powodu prześladowań lub wojny, chroniona prawem międzynarodowym.'),
],
Q=[
 ('Dążenie Katalonii do niepodległości to przykład:', ['*separatyzmu', 'globalizacji', 'aneksji', 'integracji gospodarczej'], 'Hiszpania.'),
 ('Konflikt o wody Tygrysu i Eufratu dotyczy m.in.:', ['*Turcji, Syrii i Iraku', 'Egiptu i Sudanu', 'Indii i Pakistanu', 'Chin i Wietnamu'], 'Zapory w Turcji.'),
]),
'g-srodowisko': dict(F=[
 ('Dziura ozonowa', 'Zmniejszenie ilości ozonu nad Antarktydą przez freony; Protokół montrealski (1987) ograniczył ich użycie.'),
 ('Kwaśne deszcze', 'Opady z SO₂ i NOₓ ze spalania paliw — niszczą lasy, zakwaszają wody i gleby.'),
 ('Pustynnienie', 'Degradacja ziemi na obszarach suchych przez nadmierny wypas, wylesianie i susze — Sahel.'),
 ('Porozumienie paryskie', 'Umowa klimatyczna z 2015 r.: ograniczyć ocieplenie wyraźnie poniżej 2°C.'),
],
Q=[
 ('Za powstanie dziury ozonowej odpowiadają głównie:', ['*freony', 'dwutlenek węgla', 'pyły wulkaniczne', 'metan z hodowli'], 'Protokół montrealski.'),
 ('Kwaśne deszcze powstają głównie z:', ['*SO₂ i tlenków azotu', 'ozonu i tlenu', 'pary wodnej i CO', 'freonów'], 'Spalanie paliw.'),
 ('Porozumienie paryskie zawarto w roku:', ['*2015', '1997', '1987', '2009'], 'Kioto — 1997.'),
]),
}
