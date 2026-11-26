# Geografia — porcja 17 (dogęszczanie najsłabszych poddziałów).
T = {
'g-polecenia': dict(F=[
 ('Polecenie „Wyjaśnij”', 'Podaj przyczynę i mechanizm — odpowiedź typu „ponieważ… w wyniku czego…”.'),
 ('Polecenie „Uzasadnij”', 'Podaj argument potwierdzający wskazane stwierdzenie — zwykle z materiału źródłowego.'),
 ('Polecenie „Podaj” / „Wymień”', 'Krótka odpowiedź bez uzasadnienia; liczba elementów musi się zgadzać z poleceniem.'),
 ('Polecenie „Rozstrzygnij”', 'Wybierz jedną opcję (tak/nie, A/B) i zawsze uzasadnij — bez uzasadnienia brak punktu.'),
 ('Polecenie „Wykaż związek”', 'Pokaż zależność przyczynowo-skutkową między dwoma zjawiskami.'),
 ('Czynniki przyrodnicze a pozaprzyrodnicze', 'Przyrodnicze: klimat, gleby, rzeźba, wody; pozaprzyrodnicze: ludność, kapitał, transport, polityka.'),
 ('Typowy błąd: ogólnik', '„Dobre warunki” czy „rozwój gospodarki” nie dają punktu — trzeba nazwać konkretną cechę.'),
],
Q=[
 ('Polecenie „Rozstrzygnij” wymaga:', ['*wyboru jednej opcji i uzasadnienia', 'samego wyboru odpowiedzi', 'narysowania schematu', 'podania definicji pojęcia'], 'Bez uzasadnienia brak punktu.'),
 ('Czynnikiem pozaprzyrodniczym rozwoju rolnictwa jest:', ['*dostęp do kapitału i maszyn', 'długość okresu wegetacji', 'żyzność gleb', 'ukształtowanie terenu'], 'Pozostałe są przyrodnicze.'),
 ('Gdy polecenie każe podać dwie przyczyny, a podasz trzy, w tym błędną:', ['*możesz stracić punkt', 'dostaniesz punkt dodatkowy', 'błędna jest pomijana', 'zawsze dostajesz komplet'], 'Zasada oceniania.'),
]),
'g-slonce': dict(F=[
 ('Wysokość Słońca w dniu równonocy', 'h = 90° − φ (na obu półkulach).'),
 ('Wysokość Słońca na równiku 22 VI', '90° − 23°27′ = 66°33′ — Słońce góruje po stronie północnej.'),
 ('Wyznaczanie szerokości z wysokości Słońca', 'Np. 21 III: φ = 90° − h; 22 VI (półkula N): φ = 90° − h + 23°27′.'),
 ('Kąt padania a nagrzewanie', 'Im większa wysokość Słońca, tym więcej energii na jednostkę powierzchni.'),
 ('Zenit', 'Punkt na niebie dokładnie nad głową obserwatora (h = 90°).'),
],
Q=[
 ('W dniu równonocy na 40°N Słońce góruje na wysokości:', ['*50°', '40°', '73°27′', '26°33′'], '90 − 40.'),
 ('22 VI Słońce górowało na wysokości 60°, półkula N. Szerokość obserwatora:', ['*53°27′N', '30°00′N', '36°33′N', '6°33′N'], '90 − 60 + 23°27′.'),
 ('Na równiku 22 czerwca Słońce góruje na wysokości:', ['*66°33′', '90°', '23°27′', '45°'], '90 − 23°27′.'),
]),
'g-pl-ludnosc': dict(F=[
 ('Rozmieszczenie ludności Polski', 'Najgęściej: aglomeracje (śląska, warszawska, krakowska, łódzka, trójmiejska); najrzadziej: północny wschód i zachód.'),
 ('Odsetek ludności miejskiej w Polsce', 'Ok. 60% — od lat bez wzrostu (suburbanizacja).'),
 ('Starzenie się ludności Polski', 'Udział osób 65+ ok. 20% i rośnie; mediana wieku ponad 42 lata.'),
 ('Saldo migracji zagranicznych Polski', 'Od niedawna dodatnie — napływ z Ukrainy i Azji przewyższa emigrację.'),
 ('Migracje wewnętrzne w Polsce', 'Głównie ze wsi i małych miast do dużych miast i ich stref podmiejskich.'),
],
Q=[
 ('Odsetek ludności miejskiej w Polsce wynosi ok.:', ['*60%', '40%', '80%', '95%'], 'Bez wzrostu od lat.'),
 ('Najrzadziej zaludnione województwo to:', ['*podlaskie', 'śląskie', 'małopolskie', 'mazowieckie'], 'Ok. 55 os./km².'),
 ('Udział osób w wieku 65+ w Polsce wynosi ok.:', ['*20%', '5%', '40%', '10%'], 'I szybko rośnie.'),
]),
'g-orientacja': dict(F=[
 ('Mech na drzewach a kierunek', 'Mało pewna metoda — mchy rosną po stronie wilgotniejszej, niekoniecznie północnej.'),
 ('Kierunek wschodu Słońca w Polsce', '21 III i 23 IX — dokładnie na wschodzie; latem na północnym wschodzie, zimą na południowym wschodzie.'),
 ('Ołtarze w kościołach', 'W starych kościołach zwykle skierowane na wschód (orientacja).'),
],
Q=[
 ('22 grudnia w Polsce Słońce wschodzi na:', ['*południowym wschodzie', 'północnym wschodzie', 'dokładnie na wschodzie', 'południu'], 'Krótki dzień.'),
 ('Azymut kierunku południowo-wschodniego wynosi:', ['*135°', '45°', '225°', '315°'], 'SE.'),
]),
'g-obliczenia': dict(F=[
 ('Przyrost naturalny (‰)', '(urodzenia − zgony) / liczba ludności × 1000.'),
 ('Saldo migracji', 'Napływ − odpływ.'),
 ('Przyrost rzeczywisty', 'Przyrost naturalny + saldo migracji.'),
 ('Spadek terenu (%)', 'Różnica wysokości / odległość pozioma × 100%.'),
 ('Plon', 'Zbiory / powierzchnia uprawy (t/ha lub dt/ha).'),
],
Q=[
 ('Urodzenia 900, zgony 1200, ludność 100 tys. Przyrost naturalny:', ['*−3‰', '3‰', '−0,3‰', '−30‰'], '−300/100 000 × 1000.'),
 ('Różnica wysokości 50 m na 1 km. Spadek:', ['*5%', '0,5%', '50%', '20%'], '50/1000.'),
 ('Zbiory 3000 t z 500 ha. Plon:', ['*60 dt/ha', '6 dt/ha', '600 dt/ha', '15 dt/ha'], '6 t/ha.'),
]),
'g-pl-krajobrazy': dict(F=[
 ('Krajobraz nadmorski', 'Mierzeje, wydmy, jeziora przybrzeżne, klify — Pobrzeże Słowińskie, Hel.'),
 ('Krajobraz krasowy w Polsce', 'Wyżyna Krakowsko-Częstochowska: ostańce, jaskinie, doliny (Ojców, Pieskowa Skała).'),
 ('Krajobraz przemysłowy', 'Górny Śląsk: hałdy, zapadliska, kopalnie, zwarta zabudowa miejska.'),
 ('Krajobraz kulturowy', 'Ukształtowany przez człowieka: pola, wsie, miasta, sieć dróg.'),
],
Q=[
 ('Ostańce i jaskinie są typowe dla:', ['*Wyżyny Krakowsko-Częstochowskiej', 'Żuław Wiślanych', 'Pojezierza Mazurskiego', 'Niziny Mazowieckiej'], 'Wapienie jurajskie.'),
 ('Hałdy i zapadliska to cechy krajobrazu:', ['*przemysłowego', 'nadmorskiego', 'wysokogórskiego', 'lessowego'], 'Górny Śląsk.'),
]),
'g-dane': dict(F=[
 ('Metoda sygnaturowa', 'Znaki (symbole) w miejscu występowania obiektu, np. kopalnie, elektrownie.'),
 ('Metoda izolinii', 'Linie łączące punkty o tej samej wartości (izotermy, izohiety, poziomice).'),
 ('Metoda kropkowa', 'Kropki o stałej wartości pokazują rozmieszczenie, np. 1 kropka = 1000 osób.'),
 ('Metoda zasięgów', 'Linią lub barwą zaznacza się obszar występowania zjawiska, np. zasięg buka.'),
],
Q=[
 ('Rozmieszczenie ludności (1 kropka = 1000 osób) to metoda:', ['*kropkowa', 'kartogramu', 'izolinii', 'sygnaturowa'], 'Wartości bezwzględne.'),
 ('Izohiety pokazują rozkład:', ['*opadów', 'temperatury', 'ciśnienia', 'głębokości'], 'Metoda izolinii.'),
 ('Zasięg występowania buka przedstawia się metodą:', ['*zasięgów', 'kartodiagramu', 'kropkową', 'kartogramu'], 'Linia zasięgu.'),
]),
'g-gis': dict(F=[
 ('Teledetekcja', 'Pozyskiwanie informacji o powierzchni Ziemi z odległości — zdjęcia satelitarne i lotnicze, radar, lidar.'),
 ('Copernicus i Sentinel', 'Europejski program obserwacji Ziemi; satelity Sentinel udostępniają dane bezpłatnie.'),
 ('Rozdzielczość przestrzenna', 'Wielkość terenu odpowiadająca jednemu pikselowi obrazu (np. 10 m).'),
],
Q=[
 ('Europejski program obserwacji Ziemi to:', ['*Copernicus', 'Galileo', 'Apollo', 'Hubble'], 'Satelity Sentinel.'),
 ('Rozdzielczość 10 m oznacza, że jeden piksel to teren:', ['*10 × 10 m', '1 × 1 m', '100 × 100 m', '10 × 10 km'], 'Rozdzielczość przestrzenna.'),
]),
'g-rozwoj': dict(F=[
 ('PKB per capita (PPP)', 'Produkt krajowy brutto na mieszkańca według parytetu siły nabywczej — uwzględnia różnice cen.'),
 ('Kraje najsłabiej rozwinięte', 'Głównie Afryka Subsaharyjska (np. Niger, Czad, Somalia) — najniższe HDI.'),
 ('Pułapka ubóstwa', 'Bieda → słaba edukacja i zdrowie → niska wydajność → bieda.'),
 ('Pomoc rozwojowa', 'Wsparcie finansowe i techniczne krajów bogatych dla rozwijających się (ODA).'),
 ('Współczynnik Giniego', 'Miara nierówności dochodów: 0 — pełna równość, 1 (100) — skrajna nierówność.'),
],
Q=[
 ('Nierówność dochodów mierzy:', ['*współczynnik Giniego', 'wskaźnik urbanizacji', 'współczynnik feminizacji', 'saldo migracji'], '0–1.'),
 ('PKB według parytetu siły nabywczej uwzględnia:', ['*różnice poziomu cen', 'tylko eksport', 'liczbę ludności miejskiej', 'emisję CO₂'], 'PPP.'),
]),
'g-uslugi': dict(F=[
 ('Usługi wyższego rzędu', 'Wymagają specjalistycznej wiedzy: finanse, nauka, doradztwo, IT — koncentrują się w metropoliach.'),
 ('Outsourcing usług', 'Przenoszenie usług (np. księgowość, IT, centra obsługi) do krajów o niższych kosztach — np. Kraków, Wrocław.'),
 ('Porty morskie Polski', 'Gdańsk (największy), Gdynia, Szczecin–Świnoujście.'),
 ('Transport intermodalny', 'Przewóz ładunku kilkoma środkami transportu w tym samym kontenerze.'),
],
Q=[
 ('Największy port morski Polski to:', ['*Gdańsk', 'Gdynia', 'Kołobrzeg', 'Elbląg'], 'Terminal kontenerowy.'),
 ('Centra usług biznesowych w Krakowie i Wrocławiu to przykład:', ['*outsourcingu usług', 'rolnictwa intensywnego', 'deindustrializacji wsi', 'turystyki uzdrowiskowej'], 'BPO/SSC.'),
]),
'g-demografia': dict(F=[
 ('Współczynnik dzietności', 'Średnia liczba dzieci urodzonych przez kobietę w ciągu życia; 2,1 zapewnia zastępowalność pokoleń.'),
 ('Najwyższa dzietność na świecie', 'Niger, Czad, Somalia — ponad 6 dzieci na kobietę.'),
 ('Przeciętne trwanie życia', 'Najdłuższe w Japonii, Szwajcarii, Hiszpanii (ponad 83 lata); w Polsce ok. 78 lat.'),
 ('Umieralność niemowląt', 'Liczba zgonów dzieci do 1. roku życia na 1000 urodzeń — dobry wskaźnik poziomu życia.'),
],
Q=[
 ('Zastępowalność pokoleń zapewnia współczynnik dzietności ok.:', ['*2,1', '1,3', '3,5', '1,0'], 'Prosta zastępowalność.'),
 ('Najwyższą dzietność mają kraje:', ['*Afryki Subsaharyjskiej', 'Europy Zachodniej', 'Azji Wschodniej', 'Ameryki Północnej'], 'Np. Niger.'),
]),
'g-lodowce': dict(F=[
 ('Plejstocen', 'Epoka zlodowaceń (ok. 2,6 mln – 11,7 tys. lat temu); lądolody kilkakrotnie wkraczały na obszar Polski.'),
 ('Zlodowacenia w Polsce', 'Najstarsze (m.in. południowopolskie) sięgały do Sudetów i Karpat; najmłodsze (północnopolskie) do pojezierzy.'),
 ('Głazy narzutowe', 'Bloki skał skandynawskich przyniesione przez lądolód.'),
],
Q=[
 ('Głazy narzutowe w Polsce pochodzą głównie ze:', ['*Skandynawii', 'Tatr', 'Sudetów', 'Uralu'], 'Przyniósł je lądolód.'),
 ('Ostatnie zlodowacenie objęło w Polsce:', ['*północną część kraju (pojezierza)', 'cały kraj aż po Tatry', 'tylko Tatry i Sudety', 'tylko wybrzeże Bałtyku'], 'Zlodowacenie północnopolskie.'),
]),
'g-wspolrzedne': dict(F=[
 ('Długość równoleżnika na 60°', 'Połowa długości równika — ok. 20 000 km (cos 60° = 0,5).'),
 ('Odległość wzdłuż równoleżnika', 'Różnica długości × 111,3 km × cos φ.'),
 ('Położenie matematyczne Polski', 'Ok. 49°00′–54°50′N i 14°07′–24°09′E.'),
],
Q=[
 ('Odległość 10° wzdłuż równoleżnika 60°N wynosi ok.:', ['*556 km', '1113 km', '111 km', '278 km'], '10 × 111,3 × 0,5.'),
 ('Najdalej na północ wysunięty punkt Polski leży na ok.:', ['*54°50′N', '49°00′N', '52°00′N', '56°00′N'], 'Jastrzębia Góra.'),
]),
'g-obrotowy': dict(F=[
 ('Czas letni w Polsce', 'Od ostatniej niedzieli marca do ostatniej niedzieli października — UTC+2.'),
 ('Różnica czasu Warszawa–Nowy Jork', 'Zwykle 6 godzin (Nowy Jork UTC−5, Warszawa UTC+1).'),
],
Q=[
 ('Gdy w Warszawie (UTC+1) jest 18:00, w Nowym Jorku (UTC−5) jest:', ['*12:00', '24:00', '13:00', '23:00'], 'Różnica 6 h.'),
 ('Czas letni w Polsce to czas strefy:', ['*UTC+2', 'UTC+1', 'UTC+0', 'UTC+3'], 'Od końca marca do końca października.'),
]),
}
