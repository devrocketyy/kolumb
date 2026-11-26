# Geografia — porcja 14 (dogęszczanie): skala, współrzędne, ruchy Ziemi, ciśnienie, klimaty, rzeki, tektonika, skały, rolnictwo.
T = {
'g-skala': dict(F=[
 ('Powierzchnia a skala', 'Gdy skala zmniejsza się 2 razy (np. z 1:25 000 na 1:50 000), powierzchnia na mapie maleje 4 razy.'),
 ('1 cm² na mapie 1:50 000', 'Odpowiada 25 ha (0,25 km²) w terenie.'),
 ('1 cm² na mapie 1:10 000', 'Odpowiada 1 ha (10 000 m²) w terenie.'),
 ('Mapa przeglądowa', 'Mapa w małej skali (np. 1:1 000 000 i mniejszej) przedstawiająca duże obszary w uogólnieniu.'),
 ('Obliczanie skali z odległości', 'Skala = odległość na mapie / odległość w terenie, po sprowadzeniu do tych samych jednostek.'),
],
Q=[
 ('1 cm² na mapie w skali 1:50 000 to w terenie:', ['*25 ha', '5 ha', '2,5 ha', '50 ha'], '500 m × 500 m.'),
 ('Zmiana skali z 1:25 000 na 1:50 000 zmniejsza powierzchnię obiektu na mapie:', ['*4 razy', '2 razy', '8 razy', '25 razy'], 'Kwadrat stosunku skal.'),
 ('Odcinek 5 km w terenie ma na mapie 10 cm. Skala mapy to:', ['*1:50 000', '1:5 000', '1:500 000', '1:20 000'], '500 000 cm / 10.'),
]),
'g-wspolrzedne': dict(F=[
 ('Zapis współrzędnych', 'Najpierw szerokość (N/S), potem długość (E/W), np. 52°14′N, 21°01′E — Warszawa.'),
 ('Równik', 'Najdłuższy równoleżnik (ok. 40 075 km), szerokość 0°; dzieli Ziemię na półkule N i S.'),
 ('Południk 0° (Greenwich)', 'Południk zerowy przechodzący przez obserwatorium w Greenwich; dzieli Ziemię na półkule E i W.'),
 ('Odległość wzdłuż południka', 'Liczymy różnicę szerokości × 111,2 km (1° = 111,2 km).'),
],
Q=[
 ('Odległość między punktami 50°N, 20°E i 54°N, 20°E wynosi około:', ['*445 km', '111 km', '220 km', '890 km'], '4° × 111,2 km.'),
 ('Szerokość geograficzna równika wynosi:', ['*0°', '90°', '180°', '23°27′'], 'Najdłuższy równoleżnik.'),
 ('W zapisie współrzędnych jako pierwszą podaje się:', ['*szerokość geograficzną', 'długość geograficzną', 'wysokość n.p.m.', 'azymut'], 'N/S, potem E/W.'),
]),
'g-obrotowy': dict(F=[
 ('Kierunek ruchu obrotowego', 'Z zachodu na wschód (przeciwnie do ruchu wskazówek zegara, patrząc znad bieguna N).'),
 ('Spłaszczenie Ziemi', 'Skutek ruchu obrotowego — promień równikowy (6378 km) jest o ok. 21 km dłuższy od biegunowego.'),
 ('Odchylenie ciał w ruchu', 'Siła Coriolisa odchyla wiatry i prądy w prawo na półkuli N, w lewo na półkuli S.'),
 ('Czas uniwersalny (UTC)', 'Czas słoneczny południka 0°; podstawa liczenia czasów strefowych.'),
],
Q=[
 ('Ziemia obraca się wokół osi:', ['*z zachodu na wschód', 'ze wschodu na zachód', 'z północy na południe', 'z południa na północ'], 'Stąd wschód Słońca na wschodzie.'),
 ('Na półkuli południowej siła Coriolisa odchyla ciała w:', ['*lewo', 'prawo', 'górę', 'nie działa'], 'Na N — w prawo.'),
 ('Czas uniwersalny UTC to czas słoneczny południka:', ['*0°', '15°E', '180°', '90°W'], 'Greenwich.'),
]),
'g-obiegowy': dict(F=[
 ('Długość dnia na równiku', 'Przez cały rok ok. 12 godzin.'),
 ('Długość dnia w Polsce', 'Od ok. 7,5–8 h (22 XII) do ok. 16,5–17 h (22 VI), zależnie od szerokości.'),
 ('Ekliptyka', 'Płaszczyzna orbity Ziemi; oś Ziemi jest nachylona do niej pod kątem 66°33′.'),
 ('Odległość Ziemi od Słońca', 'Średnio ok. 150 mln km (1 jednostka astronomiczna).'),
],
Q=[
 ('Długość dnia na równiku przez cały rok wynosi około:', ['*12 godzin', '24 godzin', '8 godzin', '16 godzin'], 'Brak zmian sezonowych.'),
 ('Oś Ziemi jest nachylona do płaszczyzny orbity pod kątem:', ['*66°33′', '23°27′', '90°', '45°'], '90° − 23°27′.'),
 ('Średnia odległość Ziemi od Słońca wynosi około:', ['*150 mln km', '15 mln km', '1,5 mld km', '384 tys. km'], '384 tys. km — Księżyc.'),
]),
'g-cisnienie': dict(F=[
 ('Spadek ciśnienia z wysokością', 'Ok. 1 hPa na każde 8 m w dolnej troposferze; na 5,5 km ciśnienie jest ok. 2 razy mniejsze.'),
 ('Barometr', 'Przyrząd do pomiaru ciśnienia atmosferycznego.'),
 ('Ruch powietrza w niżu na półkuli N', 'Przeciwnie do ruchu wskazówek zegara, ku środkowi; w wyżu — zgodnie, od środka.'),
 ('Wyż azorski i niż islandzki', 'Ośrodki baryczne decydujące o pogodzie w Europie i w Polsce.'),
],
Q=[
 ('Ciśnienie mierzy się:', ['*barometrem', 'higrometrem', 'anemometrem', 'termometrem'], 'Higrometr — wilgotność.'),
 ('W niżu na półkuli N powietrze krąży:', ['*przeciwnie do ruchu wskazówek zegara', 'zgodnie z ruchem wskazówek zegara', 'pionowo w dół bez wirowania', 'tylko z zachodu na wschód'], 'Siła Coriolisa.'),
 ('Pogodę w Polsce kształtują m.in.:', ['*wyż azorski i niż islandzki', 'pasaty i monsun', 'wyż australijski', 'niż aleucki i bryza'], 'Ośrodki atlantyckie.'),
]),
'g-klimaty': dict(F=[
 ('Klimat sawanny — klimatogram', 'Temperatury wysokie cały rok, wyraźna pora sucha i deszczowa.'),
 ('Klimat wybitnie kontynentalny — przykład', 'Jakuck — amplituda roczna ponad 60°C (zima ok. −39°C, lato ok. +19°C).'),
 ('Klimat górski', 'Zmienia się piętrowo z wysokością; temperatura spada, opady zwykle rosną do pewnej wysokości.'),
 ('Klasyfikacja Köppena', 'Podział klimatów na podstawie temperatury i opadów (strefy A, B, C, D, E).'),
],
Q=[
 ('Amplitudę roczną temperatury ponad 60°C notuje się w:', ['*Jakucku', 'Londynie', 'Singapurze', 'Lizbonie'], 'Klimat wybitnie kontynentalny.'),
 ('W klimacie górskim temperatura wraz z wysokością:', ['*spada', 'rośnie', 'nie zmienia się', 'rośnie tylko zimą'], 'Piętrowość.'),
 ('Wyraźną porę suchą i deszczową ma klimat:', ['*podrównikowy (sawanny)', 'równikowy wilgotny', 'umiarkowany morski', 'polarny'], 'Ruch strefy zbieżności.'),
]),
'g-rzeki': dict(F=[
 ('Meander', 'Zakole rzeki nizinnej powstałe w wyniku erozji bocznej i akumulacji.'),
 ('Starorzecze', 'Odcięty od koryta dawny meander — jezioro w dolinie rzeki.'),
 ('Estuarium', 'Lejkowate ujście rzeki poszerzone przez pływy (np. Tamiza, Łaba).'),
 ('Wododział', 'Granica między dorzeczami lub zlewiskami.'),
],
Q=[
 ('Odcięty dawny meander to:', ['*starorzecze', 'estuarium', 'delta', 'przełom'], 'Jezioro w dolinie.'),
 ('Lejkowate ujście rzeki kształtowane przez pływy to:', ['*estuarium', 'delta', 'meander', 'liman'], 'Np. Tamiza.'),
 ('Linię oddzielającą dorzecza Wisły i Odry nazywamy:', ['*wododziałem', 'izobatą', 'korytem', 'terasą'], 'Dział wodny.'),
]),
'g-tektonika': dict(F=[
 ('Pierścień Ognia', 'Strefa wulkanów i trzęsień wokół Oceanu Spokojnego — strefy subdukcji.'),
 ('Hot spot (plama gorąca)', 'Miejsce wypływu magmy z płaszcza niezwiązane z granicą płyt — np. Hawaje.'),
 ('Tsunami', 'Fala oceaniczna wywołana podmorskim trzęsieniem ziemi, wybuchem wulkanu lub osuwiskiem.'),
 ('Skala Richtera', 'Skala magnitudy — energii wyzwolonej w ognisku trzęsienia ziemi.'),
],
Q=[
 ('Hawaje powstały nad:', ['*plamą gorąca', 'strefą subdukcji', 'grzbietem śródoceanicznym', 'uskokiem przesuwczym'], 'Hot spot.'),
 ('Energię trzęsienia ziemi opisuje skala:', ['*Richtera', 'Beauforta', 'Mohsa', 'Celsjusza'], 'Magnituda.'),
 ('Pierścień Ognia otacza:', ['*Ocean Spokojny', 'Ocean Atlantycki', 'Ocean Indyjski', 'Morze Śródziemne'], 'Strefy subdukcji.'),
]),
'g-skaly': dict(F=[
 ('Bazalt', 'Ciemna skała magmowa wylewna; buduje dno oceanów i pokrywy lawowe.'),
 ('Piaskowiec', 'Skała osadowa okruchowa zwięzła — scementowany piasek (np. Góry Stołowe).'),
 ('Less', 'Pylasta skała osadowa eoliczna; podłoże żyznych gleb (Wyżyna Lubelska).'),
 ('Gnejs', 'Skała metamorficzna o budowie warstewkowej, powstała np. z granitu.'),
],
Q=[
 ('Dno oceanów buduje głównie:', ['*bazalt', 'granit', 'wapień', 'piaskowiec'], 'Skorupa oceaniczna.'),
 ('Less jest skałą pochodzenia:', ['*eolicznego', 'wulkanicznego', 'morskiego', 'metamorficznego'], 'Nawiewany pył.'),
 ('Góry Stołowe zbudowane są głównie z:', ['*piaskowca', 'granitu', 'bazaltu', 'marmuru'], 'Formy skalne.'),
]),
'g-rolnictwo': dict(F=[
 ('Rolnictwo ekstensywne', 'Małe nakłady pracy i kapitału, niskie plony z hektara (np. pasterstwo koczownicze).'),
 ('Rolnictwo intensywne', 'Duże nakłady (nawozy, maszyny), wysokie plony z hektara — np. Holandia.'),
 ('Gospodarka plantacyjna', 'Wielkoobszarowe uprawy jednego gatunku na eksport (kawa, herbata, banany) w strefie tropikalnej.'),
 ('Zielona rewolucja', 'Wprowadzanie wydajnych odmian, nawozów i nawadniania w krajach rozwijających się od lat 60. XX w.'),
],
Q=[
 ('Wysokie nakłady i plony z hektara cechują rolnictwo:', ['*intensywne', 'ekstensywne', 'koczownicze', 'żarowe'], 'Np. Holandia.'),
 ('Uprawy jednego gatunku na eksport w tropikach to:', ['*gospodarka plantacyjna', 'rolnictwo żarowe', 'pasterstwo koczownicze', 'ogrodnictwo działkowe'], 'Kawa, herbata.'),
 ('Istotą zielonej rewolucji było:', ['*wprowadzenie wydajnych odmian i nawozów', 'porzucenie nawozów sztucznych', 'zalesianie pól uprawnych', 'kolektywizacja gospodarstw'], 'Lata 60.'),
]),
}
