# Geografia — porcja 13 (dogęszczanie): atmosfera, pogoda, oceany, lodowce, gleby, biomy, ludność, miasta, usługi, środowisko.
T = {
'g-atmosfera': dict(F=[
 ('Izoterma', 'Linia na mapie łącząca punkty o jednakowej temperaturze powietrza.'),
 ('Temperatura zredukowana do poziomu morza', 'Temperatura przeliczona tak, jakby stacja leżała na poziomie morza — pozwala porównać stacje na różnych wysokościach.'),
 ('Promieniowanie słoneczne a zachmurzenie', 'Chmury zmniejszają nasłonecznienie w dzień, ale nocą ograniczają wypromieniowanie — noce pochmurne są cieplejsze.'),
 ('Termiczny równik', 'Linia łącząca miejsca o najwyższej średniej temperaturze; leży średnio na półkuli N (ok. 10°N), bo jest tam więcej lądów.'),
 ('Biegun ciepła', 'Obszary o najwyższych temperaturach: Dolina Śmierci, Sahara (Dallol w Etiopii — najwyższa średnia roczna).'),
],
Q=[
 ('Linia łącząca punkty o jednakowej temperaturze to:', ['*izoterma', 'izobara', 'izohieta', 'izobata'], 'Izobata — jednakowa głębokość.'),
 ('Pochmurne noce są cieplejsze, ponieważ chmury:', ['*ograniczają wypromieniowanie ciepła z powierzchni', 'same wytwarzają duże ilości ciepła', 'zwiększają albedo powierzchni nocą', 'przyspieszają nocne wiatry górskie'], 'Efekt „kołdry”.'),
 ('Termiczny równik leży średnio na półkuli:', ['*północnej', 'południowej', 'dokładnie na 0°', 'zmienia się co roku na S'], 'Więcej lądów na półkuli N.'),
]),
'g-pogoda': dict(F=[
 ('Prognoza pogody — źródła danych', 'Stacje meteorologiczne, radiosondy, radary, satelity, modele numeryczne.'),
 ('Ciśnienie a pogoda', 'Spadek ciśnienia zapowiada zwykle niż i pogorszenie pogody; wzrost — wyż i poprawę.'),
 ('Burza', 'Zjawisko z wyładowaniami atmosferycznymi w chmurach cumulonimbus; częsta latem przy dużej chwiejności powietrza.'),
 ('Trąba powietrzna', 'Gwałtowny wir powietrza schodzący z chmury burzowej do ziemi; w USA nazywana tornadem.'),
 ('Skala Beauforta', 'Skala siły wiatru od 0 (cisza) do 12 (huragan).'),
],
Q=[
 ('Gwałtowny spadek ciśnienia zapowiada zwykle:', ['*nadejście niżu i pogorszenie pogody', 'stabilną pogodę wyżową', 'bezchmurne niebo', 'mróz i ciszę'], 'Niż — chmury i opady.'),
 ('Siłę wiatru opisuje skala:', ['*Beauforta', 'Richtera', 'Mohsa', 'Mercallego'], '0–12.'),
 ('Tornado to:', ['*gwałtowny wir powietrza schodzący z chmury burzowej', 'cyklon tropikalny nad Pacyfikiem', 'zimny wiatr górski', 'stały wiatr strefy zwrotnikowej'], 'Trąba powietrzna.'),
]),
'g-oceany': dict(F=[
 ('Temperatura wód powierzchniowych', 'Najwyższa w strefie równikowej (ok. 28°C), maleje ku biegunom; w Bałtyku latem ok. 18–20°C.'),
 ('Lód morski', 'Zamarza woda morska; pokrywa Ocean Arktyczny i otacza Antarktydę — jego zasięg maleje wskutek ocieplenia.'),
 ('Fale wiatrowe', 'Powstają pod wpływem wiatru; ich wysokość zależy od siły i czasu wiania oraz rozległości akwenu.'),
 ('Ocean Arktyczny', 'Najmniejszy i najpłytszy ocean, w dużej części pokryty lodem.'),
 ('Morze Martwe', 'Jezioro bezodpływowe o zasoleniu ok. 340‰; najniżej położony obszar lądu (ok. 430 m p.p.m.).'),
],
Q=[
 ('Najmniejszym oceanem jest:', ['*Ocean Arktyczny', 'Ocean Indyjski', 'Ocean Atlantycki', 'Ocean Spokojny'], 'Także najpłytszy.'),
 ('Najniżej położony obszar lądu na Ziemi to okolice:', ['*Morza Martwego', 'Morza Kaspijskiego', 'Żuław Wiślanych', 'Doliny Śmierci'], 'Ok. 430 m p.p.m.'),
 ('Temperatura wód powierzchniowych oceanów jest najwyższa w strefie:', ['*równikowej', 'umiarkowanej', 'podbiegunowej', 'zwrotnikowej przy zimnych prądach'], 'Najsilniejsze nasłonecznienie.'),
]),
'g-lodowce': dict(F=[
 ('Lodowce Polski', 'Obecnie w Polsce nie ma lodowców; w Tatrach są tylko płaty wieloletniego śniegu i lodu.'),
 ('Wzrost poziomu morza', 'Wynika z topnienia lodowców i lądolodów oraz rozszerzalności cieplnej ogrzewanej wody.'),
 ('Szelfowe lodowce', 'Płaty lodu lądolodu unoszące się na morzu przy Antarktydzie (np. Lodowiec Szelfowy Rossa).'),
 ('Góry lodowe', 'Bryły lodu słodkiego pływające w morzu; ok. 9/10 objętości jest pod wodą.'),
],
Q=[
 ('Pływająca góra lodowa ma pod wodą około:', ['*9/10 objętości', '1/2 objętości', '1/10 objętości', 'całą objętość'], 'Gęstość lodu jest bliska wody.'),
 ('Wzrost poziomu morza wynika m.in. z:', ['*topnienia lądolodów i rozszerzalności cieplnej wody', 'zamarzania wód w strefie polarnej', 'wzrostu zasolenia wód oceanicznych', 'spadku średniej temperatury globu'], 'Ocieplenie.'),
 ('Czy w Polsce występują obecnie lodowce?', ['*nie, są tylko płaty śniegu w Tatrach', 'tak, mały lodowiec w Karkonoszach', 'tak, lodowiec górski pod Kasprowym', 'tak, płaty lodu na Pojezierzu Pomorskim'], 'Tatry są za niskie.'),
]),
'g-gleby': dict(F=[
 ('Gleby płowe', 'Gleby z wymywaniem iłu w głąb profilu; częste w Polsce na glinach i lessach.'),
 ('Czarne ziemie', 'Żyzne gleby powstałe w warunkach podmokłych z dużą ilością próchnicy — Kujawy, okolice Wrocławia.'),
 ('Gleby torfowe', 'Powstają na torfowiskach z obumarłych roślin w warunkach nadmiaru wody; po osuszeniu wykorzystywane jako łąki.'),
 ('Odczyn gleby (pH)', 'Gleby kwaśne (bielicowe) wapnuje się, by poprawić ich przydatność rolniczą.'),
],
Q=[
 ('Glebę kwaśną poprawia się przez:', ['*wapnowanie', 'zasolenie', 'zakwaszanie', 'osuszanie torfu'], 'Podnosi pH.'),
 ('Żyzne czarne ziemie występują m.in. na:', ['*Kujawach', 'Podhalu', 'Mierzei Helskiej', 'Pojezierzu Kaszubskim na wydmach'], 'Także okolice Wrocławia.'),
 ('Gleby torfowe powstają w warunkach:', ['*nadmiaru wody', 'suszy', 'klimatu pustynnego', 'wulkanizmu'], 'Torfowiska.'),
]),
'g-biomy': dict(F=[
 ('Las liściasty strefy umiarkowanej — przystosowania', 'Drzewa zrzucają liście jesienią, by ograniczyć utratę wody i uszkodzenia mrozem.'),
 ('Sukulenty', 'Rośliny gromadzące wodę w tkankach (kaktusy, agawy) — przystosowanie do suszy.'),
 ('Wielowarstwowość lasu równikowego', 'Piętra: drzewa olbrzymy, korony, podszyt, runo; do dna lasu dociera mało światła.'),
 ('Zwierzęta tundry', 'Renifery, lemingi, piżmowoły, lisy polarne; wiele ptaków przylatuje tylko latem.'),
],
Q=[
 ('Kaktusy gromadzące wodę w tkankach to:', ['*sukulenty', 'epifity', 'halofity', 'hydrofity'], 'Przystosowanie do suszy.'),
 ('Drzewa liściaste zrzucają liście jesienią, aby:', ['*ograniczyć utratę wody w zimie', 'przyspieszyć fotosyntezę', 'zwabić zwierzęta', 'odbić promieniowanie'], 'Woda zamarza w glebie.'),
 ('Typowym zwierzęciem tundry jest:', ['*renifer', 'żyrafa', 'wielbłąd', 'jaguar'], 'Strefa subpolarna.'),
]),
'g-demografia': dict(F=[
 ('Spis powszechny', 'Badanie całej ludności kraju; w Polsce ostatni Narodowy Spis Powszechny w 2021 r.'),
 ('Wyż i niż demograficzny', 'Okresy dużej i małej liczby urodzeń; w Polsce wyże po II wojnie światowej i na początku lat 80.'),
 ('Echo wyżu demograficznego', 'Wzrost urodzeń, gdy liczne roczniki z wyżu wchodzą w wiek rodzicielski.'),
 ('Polityka jednego dziecka', 'Polityka antynatalistyczna Chin (1980–2015) — ograniczenie liczby urodzeń.'),
],
Q=[
 ('Ostatni Narodowy Spis Powszechny w Polsce odbył się w roku:', ['*2021', '2011', '2002', '2024'], 'Co ok. 10 lat.'),
 ('Polityka jednego dziecka obowiązywała w:', ['*Chinach', 'Indiach', 'Japonii', 'Nigerii'], '1980–2015.'),
 ('Wzrost urodzeń, gdy liczne roczniki wchodzą w wiek rodzicielski, to:', ['*echo wyżu demograficznego', 'niż demograficzny', 'eksplozja demograficzna', 'drenaż mózgów'], 'Np. lata 80. w Polsce.'),
]),
'g-urbanizacja': dict(F=[
 ('Strefy w mieście', 'Centrum (CBD) — usługi i biura; strefa przejściowa; dzielnice mieszkaniowe; strefa podmiejska.'),
 ('CBD', 'Central Business District — centralna dzielnica biznesu z wieżowcami, bankami i biurami.'),
 ('Fawele i slumsy', 'Dzielnice nędzy w miastach krajów rozwijających się — np. fawele w Rio de Janeiro.'),
 ('Miasta wtórne i satelitarne', 'Miasta satelitarne rozwijają się wokół metropolii, z którą łączą je dojazdy do pracy.'),
],
Q=[
 ('Centralna dzielnica biznesu w mieście to:', ['*CBD', 'fawela', 'strefa podmiejska', 'teren rekreacyjny'], 'Wieżowce, biura.'),
 ('Fawele to dzielnice nędzy w:', ['*Brazylii', 'Japonii', 'Norwegii', 'Kanadzie'], 'Rio de Janeiro, São Paulo.'),
 ('Miasto, z którego mieszkańcy codziennie dojeżdżają do metropolii, to miasto:', ['*satelitarne', 'portowe', 'uzdrowiskowe', 'graniczne'], 'Np. wokół Warszawy.'),
]),
'g-uslugi': dict(F=[
 ('Turystyka w Polsce — rodzaje', 'Wypoczynkowa (morze, góry, jeziora), kulturowa (Kraków, Gdańsk), uzdrowiskowa, biznesowa, kwalifikowana.'),
 ('Obiekty UNESCO w Polsce — przykłady', 'Stare Miasto w Krakowie, kopalnia soli w Wieliczce, Malbork, Toruń, Zamość, Auschwitz-Birkenau.'),
 ('Konteneryzacja', 'Przewóz towarów w standardowych kontenerach — obniżyła koszty transportu i przyspieszyła globalizację.'),
 ('Huby lotnicze', 'Duże porty przesiadkowe, np. Dubaj, Londyn-Heathrow, Frankfurt, Stambuł.'),
],
Q=[
 ('Obiektem UNESCO w Polsce jest:', ['*kopalnia soli w Wieliczce', 'Pałac Kultury i Nauki', 'Stadion Narodowy', 'Port Gdynia'], 'Wpisana w 1978 r.'),
 ('Przewóz towarów w standardowych skrzyniach to:', ['*konteneryzacja', 'offshoring', 'reurbanizacja', 'deglomeracja'], 'Przyspieszyła globalizację.'),
 ('Dużym hubem lotniczym jest:', ['*Dubaj', 'Zakopane', 'Ełk', 'Sopot'], 'Port przesiadkowy.'),
]),
'g-srodowisko': dict(F=[
 ('Gatunki inwazyjne w Polsce', 'Np. barszcz Sosnowskiego, nawłoć kanadyjska, rak pręgowaty — wypierają gatunki rodzime.'),
 ('Susza w Polsce', 'Polska ma małe zasoby wody; susze rolnicze i hydrologiczne są coraz częstsze.'),
 ('Ochrona przeciwpowodziowa', 'Wały, zbiorniki retencyjne, poldery, renaturyzacja dolin i ochrona mokradeł.'),
 ('Odnawialność zasobów', 'Zasoby odnawialne (woda, lasy, ryby) mogą się odtwarzać, jeśli eksploatacja nie przekracza tempa odnowy.'),
],
Q=[
 ('Gatunkiem inwazyjnym w Polsce jest:', ['*barszcz Sosnowskiego', 'żubr', 'buk zwyczajny', 'bocian biały'], 'Groźny dla zdrowia i bioróżnorodności.'),
 ('Ochronie przed powodzią służy m.in.:', ['*budowa zbiorników retencyjnych i polderów', 'osuszanie mokradeł', 'prostowanie i betonowanie koryt', 'wycinka lasów w górach'], 'Zatrzymywanie wody.'),
 ('Zasoby odnawialne to np.:', ['*lasy i woda', 'węgiel i ropa', 'rudy miedzi', 'gaz ziemny'], 'Mogą się odtwarzać.'),
]),
}
