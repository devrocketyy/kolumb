# Geografia — porcja 22 (dogęszczanie).
T = {
'g-orientacja': dict(F=[
 ('Azymut topograficzny', 'Kąt mierzony od kierunku północy siatki kilometrowej mapy.'),
 ('Wyznaczanie azymutu na mapie', 'Kątomierz przykładamy do linii północ–południe; kąt mierzymy zgodnie z ruchem wskazówek zegara.'),
 ('Marsz na azymut', 'Poruszanie się w terenie w stałym kierunku wyznaczonym kompasem.'),
 ('Kierunek przeciwny do azymutu 60°', 'Azymut wsteczny 240° — kierunek południowo-zachodni.'),
],
Q=[
 ('Azymut mierzymy od kierunku:', ['*północnego, zgodnie z ruchem wskazówek zegara', 'południowego, przeciwnie do wskazówek', 'wschodniego, zgodnie ze wskazówkami', 'zachodniego, przeciwnie do wskazówek'], 'Od N.'),
 ('Azymut 270° wskazuje kierunek:', ['*zachodni', 'wschodni', 'północny', 'południowy'], 'W.'),
]),
'g-skala': dict(F=[
 ('Skala 1:1 000 000', '1 cm na mapie = 10 km w terenie.'),
 ('Skala 1:200 000', '1 cm = 2 km — mapy samochodowe.'),
 ('Pomniejszenie skali', 'Mapa 1:100 000 jest w mniejszej skali niż 1:50 000 — pokazuje większy obszar mniej szczegółowo.'),
 ('Obliczanie skali z porównania odległości', 'Np. 15 km w terenie = 3 cm na mapie → 1 cm = 5 km → skala 1:500 000.'),
],
Q=[
 ('Odległość 15 km w terenie ma na mapie 3 cm. Skala mapy:', ['*1:500 000', '1:50 000', '1:5 000 000', '1:150 000'], '1 cm = 5 km.'),
 ('Na mapie 1:200 000 odcinek 4,5 cm to w terenie:', ['*9 km', '0,9 km', '90 km', '45 km'], '4,5 × 2 km.'),
 ('W większej skali jest mapa:', ['*1:25 000', '1:100 000', '1:500 000', '1:1 000 000'], 'Mniejszy mianownik.'),
]),
'g-obliczenia': dict(F=[
 ('Gęstość sieci kolejowej', 'Długość linii (km) na 100 km² powierzchni.'),
 ('Wskaźnik lesistości', 'Powierzchnia lasów / powierzchnia regionu × 100%.'),
 ('Średnia ważona', 'Gdy jednostki mają różną wielkość, średnią liczy się z wagami (np. ludnością).'),
 ('Zaokrąglenia na maturze', 'Zaokrąglaj dopiero wynik końcowy, z dokładnością podaną w poleceniu.'),
],
Q=[
 ('Województwo 20 000 km², lasy 6000 km². Lesistość:', ['*30%', '3%', '60%', '33%'], '6000/20 000.'),
 ('Linie kolejowe 1800 km na 20 000 km². Gęstość sieci:', ['*9 km/100 km²', '90 km/100 km²', '0,9 km/100 km²', '11 km/100 km²'], '1800/200.'),
]),
'g-dane': dict(F=[
 ('Wykres słupkowy skumulowany', 'Słupki dzielone na części — pokazuje strukturę w kilku jednostkach naraz.'),
 ('Diagram trójkątny', 'Pokazuje strukturę z trzech składników sumujących się do 100% — np. zatrudnienie w trzech sektorach.'),
 ('Wykres dwuosiowy', 'Dwie wielkości o różnych jednostkach na dwóch osiach — np. klimatogram.'),
 ('Anamorfoza', 'Mapa, na której powierzchnia państw jest proporcjonalna do zjawiska (np. liczby ludności).'),
],
Q=[
 ('Strukturę zatrudnienia w trzech sektorach dla wielu krajów najlepiej pokazać na:', ['*diagramie trójkątnym', 'mapie izarytmicznej', 'profilu terenu', 'wykresie liniowym'], 'Trzy składniki = 100%.'),
 ('Mapa, na której wielkość państw zależy od liczby ludności, to:', ['*anamorfoza', 'kartogram', 'mapa hipsometryczna', 'ortofotomapa'], 'Zniekształcona powierzchnia.'),
]),
'g-pl-wody': dict(F=[
 ('Jeziora lobeliowe', 'Ubogie w biogeny jeziora z rzadkimi roślinami (lobelia jeziorna) — Pomorze.'),
 ('Żuławy Wiślane', 'Delta Wisły — depresja do ok. 1,8 m p.p.m. (Raczki Elbląskie); polderowe osuszanie, pompownie.'),
 ('Retencja w Polsce', 'Sztuczne zbiorniki magazynują tylko ok. 6–7% odpływu rzek — za mało wobec susz.'),
 ('Najdłuższe rzeki Polski', 'Wisła (ok. 1047 km), Odra (ok. 854 km, w Polsce ok. 742 km), Warta (ok. 808 km).'),
],
Q=[
 ('Najniżej położony punkt Polski leży na:', ['*Żuławach Wiślanych', 'Pojezierzu Mazurskim', 'Nizinie Śląskiej', 'Kotlinie Sandomierskiej'], 'Raczki Elbląskie.'),
 ('Drugą pod względem długości rzeką Polski jest:', ['*Odra', 'Warta', 'Bug', 'Narew'], 'Ok. 854 km.'),
]),
'g-urbanizacja': dict(F=[
 ('Aglomeracja monocentryczna', 'Jedno dominujące miasto z otoczeniem (warszawska, krakowska).'),
 ('Konurbacja (aglomeracja policentryczna)', 'Kilka równorzędnych miast zrośniętych ze sobą (górnośląska, trójmiejska).'),
 ('Najwięcej ludności miejskiej', 'Ameryka Płd. i Północna, Europa Zachodnia — ponad 80%; najmniej Afryka Wsch. i Azja Płd.'),
 ('Miasto 15-minutowe', 'Koncepcja miasta, w którym usługi codzienne są dostępne pieszo lub rowerem w 15 minut.'),
],
Q=[
 ('Konurbacją w Polsce jest aglomeracja:', ['*górnośląska', 'warszawska', 'krakowska', 'łódzka'], 'Policentryczna.'),
 ('Najwyższy wskaźnik urbanizacji ma:', ['*Ameryka Południowa', 'Afryka Wschodnia', 'Azja Południowa', 'Oceania wyspiarska'], 'Ponad 80%.'),
]),
'g-uprawy': dict(F=[
 ('Pszenica — najwięksi producenci', 'Chiny, Indie, Rosja, USA, Francja; Rosja — największy eksporter.'),
 ('Ryż — najwięksi producenci', 'Chiny, Indie, Bangladesz, Indonezja; Indie — największy eksporter.'),
 ('Kukurydza', 'Najwięcej produkują USA i Chiny; pasza, bioetanol.'),
 ('Kawa', 'Największy producent — Brazylia, potem Wietnam i Kolumbia.'),
 ('Kakao', 'Wybrzeże Kości Słoniowej i Ghana — ok. 60% światowej produkcji.'),
 ('Soja', 'Brazylia, USA, Argentyna — pasza i olej; uprawa sprzyja wylesianiu Amazonii.'),
],
Q=[
 ('Drugim po Brazylii producentem kawy jest:', ['*Wietnam', 'Kenia', 'Etiopia', 'Jamajka'], 'Kawa robusta.'),
 ('Najwięcej kakao produkuje:', ['*Wybrzeże Kości Słoniowej', 'Republika Południowej Afryki', 'Indonezja Zachodnia', 'Ekwador i Peru'], 'Z Ghaną ok. 60%.'),
 ('Uprawa soi przyczynia się szczególnie do wylesiania:', ['*Amazonii', 'Syberii', 'Skandynawii', 'Alp'], 'Brazylia.'),
]),
'g-struktura': dict(F=[
 ('Analfabetyzm', 'Najwyższy w Afryce Subsaharyjskiej i Azji Południowej (Niger, Czad, Afganistan).'),
 ('Wiek środkowy (mediana wieku)', 'Japonia i Włochy ok. 48–49 lat; Niger ok. 15 lat; Polska ok. 42 lata.'),
 ('Kraje z przewagą mężczyzn', 'Chiny i Indie (preferencja synów), państwa Zatoki Perskiej (imigranci).'),
],
Q=[
 ('Najmłodszą strukturę wieku (mediana ok. 15 lat) ma:', ['*Niger', 'Japonia', 'Polska', 'Kanada'], 'Wysoka dzietność.'),
 ('Przewaga mężczyzn w Chinach wynika m.in. z:', ['*preferencji synów', 'emigracji mężczyzn', 'wojen', 'dłuższego życia kobiet'], 'Polityka jednego dziecka.'),
]),
}
