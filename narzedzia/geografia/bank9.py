# Bank zadań autorskich — geografia, część 9: Ziemia, mapa, ludność, klimat Polski, rolnictwo, energetyka. Dane autorskie.
BANK = {'ziemia': [
 B('Słońce nad Gdańskiem',
   'Tekst autorski. Gdańsk leży na ok. 54°20′N.',
   T('oblicz', 2, 'Oblicz wysokość Słońca w momencie górowania w Gdańsku 22 grudnia i 22 czerwca.', '12°13′ i 59°07′', '90° − 54°20′ ∓ 23°27′.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego w Gdańsku zimą dzień jest krótszy niż w Zakopanem.', 'Gdańsk leży dalej na północ; zimą na półkuli N długość dnia maleje wraz ze wzrostem szerokości geograficznej.', 'Nachylenie osi.')),
 B('Lot do Tokio',
   'Tekst autorski. Samolot wylatuje z Warszawy (zimą UTC+1) o 10:00 czasu lokalnego 15 stycznia i leci do Tokio (UTC+9) 11 godzin.',
   T('oblicz', 2, 'Podaj datę i godzinę lądowania w czasie lokalnym Tokio.', '16 stycznia, 05:00', 'Wylot 09:00 UTC, przylot 20:00 UTC; +9 h.')),
], 'mapa': [
 B('Odległość wzdłuż równoleżnika',
   'Tekst autorski. Punkty A (52°N, 14°E) i B (52°N, 24°E) leżą na tym samym równoleżniku. Długość 1° na równiku przyjmij jako 111,3 km, cos 52° ≈ 0,616.',
   T('oblicz', 2, 'Oblicz odległość między punktami wzdłuż równoleżnika.', 'ok. 686 km', '10° × 111,3 km × 0,616.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego 1° długości geograficznej na 52°N jest krótszy niż na równiku.', 'Równoleżniki maleją ku biegunom, bo południki zbiegają się w biegunach.', 'cos φ.')),
 B('Działka na planie',
   'Tekst autorski. Na mapie w skali 1:10 000 działka ma kształt prostokąta 2,5 cm × 4 cm.',
   T('oblicz', 1, 'Oblicz powierzchnię działki w terenie w hektarach.', '10 ha', '1 cm² = 1 ha; 10 cm².')),
], 'ludnosc': [
 B('Województwo w liczbach',
   'Tekst autorski. Województwo ma 5,4 mln mieszkańców i powierzchnię 35 600 km². Współczynnik urodzeń wynosi 9,2‰, a zgonów 11,5‰.',
   T('oblicz', 1, 'Oblicz gęstość zaludnienia.', 'ok. 152 os./km²', '5 400 000 / 35 600.'),
   T('oblicz', 1, 'Oblicz współczynnik przyrostu naturalnego.', '−2,3‰', '9,2 − 11,5.'),
   T('oblicz', 1, 'Oblicz, o ile osób zmniejszy się w ciągu roku liczba ludności z powodu ubytku naturalnego.', 'ok. 12 400 osób', '5 400 000 × 0,0023 = 12 420.')),
], 'polska-przyroda': [
 B('Hel i Suwałki',
   'Tekst autorski. Średnia temperatura stycznia i lipca: Hel −1°C i 17°C, Suwałki −5°C i 18°C.',
   T('oblicz', 1, 'Oblicz roczne amplitudy temperatury obu stacji.', 'Hel 18°C, Suwałki 23°C', 'Lipiec − styczeń.'),
   T('rozstrzygnij', 1, 'Rozstrzygnij, która stacja ma klimat bardziej kontynentalny. Uzasadnij.', 'Suwałki — większa amplituda i mroźniejsza zima, bo leżą dalej od morza i na wschodzie.', 'Wpływ Bałtyku i mas kontynentalnych.')),
], 'rolnictwo': [
 B('Użytkowanie ziemi w gminie',
   'Tekst autorski. Gmina ma powierzchnię 80 km², z czego 52 km² to użytki rolne, a 18 km² lasy.',
   T('oblicz', 1, 'Oblicz udział użytków rolnych i lasów w powierzchni gminy.', 'UR 65%, lasy 22,5%', '52/80 i 18/80.'),
   T('podaj', 1, 'Podaj dwa przyrodnicze czynniki sprzyjające dużemu udziałowi użytków rolnych.', 'Np. żyzne gleby, równinna rzeźba, korzystny klimat (długi okres wegetacji).', 'Wystarczą dwa.')),
], 'przemysl': [
 B('Farma wiatrowa',
   'Tekst autorski. Farma wiatrowa ma moc zainstalowaną 50 MW. Średnio przez rok pracuje z wykorzystaniem 30% mocy (rok = 8760 h).',
   T('oblicz', 2, 'Oblicz roczną produkcję energii w GWh.', 'ok. 131 GWh', '50 MW × 8760 h × 0,3 = 131 400 MWh.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego farmy na morzu mają wyższy współczynnik wykorzystania mocy niż na lądzie.', 'Nad morzem wiatr jest silniejszy i bardziej stały — brak przeszkód terenowych i mniejsze tarcie.', 'Offshore.')),
 B('Energetyka a węgiel',
   'Tekst autorski. W 1990 r. węgiel dawał w Polsce ok. 95% energii elektrycznej, w 2024 r. ok. 57%.',
   T('oblicz', 1, 'Oblicz, o ile punktów procentowych zmalał udział węgla.', 'o 38 punktów procentowych', '95 − 57.'),
   T('podaj', 2, 'Podaj dwie przyczyny spadku udziału węgla w produkcji energii w Polsce.', 'Rozwój OZE (wiatr, fotowoltaika), polityka klimatyczna UE i koszt uprawnień do emisji CO₂, wzrost znaczenia gazu.', 'Wystarczą dwie.')),
], 'czlowiek': [
 B('Smog w dolinie',
   'Tekst autorski. Zimą, przy pogodzie wyżowej i braku wiatru, w Krakowie stężenia pyłu PM10 przekraczają normę kilkukrotnie.',
   T('wyjasnij', 2, 'Wyjaśnij, dlaczego położenie Krakowa sprzyja smogowi.', 'Miasto leży w dolinie Wisły otoczonej wzniesieniami — słabe przewietrzanie; przy inwersji temperatury chłodne powietrze z zanieczyszczeniami zalega przy ziemi.', 'Inwersja.'),
   T('podaj', 1, 'Podaj główne źródło pyłów zimą w polskich miastach.', 'Niska emisja — ogrzewanie domów piecami na węgiel i drewno.', 'Także transport.')),
]}
