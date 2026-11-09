# Bank zadań autorskich — runda 4, część 2: zadania źródłowe z dziejów Polski.
BANK = {}

BANK['sredniowiecze'] = [
 B('Kronika Galla Anonima', 'Tekst (tekst autorski na wzór kroniki z XII w.). „Ten książę, choć poganin, za radą żony porzucił błędy pogańskie i przyjął wiarę chrześcijańską. Wkrótce cały naród został ochrzczony”.',
   T('podaj', 1, 'Podaj imiona księcia i jego żony.', 'Mieszko I i Dobrawa.'),
   T('podaj', 1, 'Podaj rok wydarzenia opisanego w tekście.', '966.'),
   T('rozstrzygnij', 1, 'Rozstrzygnij, czy kronikarz był świadkiem opisanych wydarzeń. Uzasadnij.', 'Nie — Gall pisał na początku XII w., ok. 140 lat po chrzcie, więc to źródło pośrednie.')),
 B('Koronacje polskie', 'Zestawienie (tekst autorski). A. Bolesław Chrobry. B. Mieszko II. C. Bolesław Śmiały. D. Przemysł II. E. Władysław Łokietek.',
   T('podaj', 2, 'Podaj lata koronacji władców A, C, D i E.', 'A — 1025; C — 1076; D — 1295; E — 1320.'),
   T('wyjasnij', 1, 'Wyjaśnij znaczenie koronacji Łokietka.', 'Zakończyła okres rozbicia dzielnicowego — odnowienie Królestwa Polskiego.')),
 B('Akademia Krakowska', 'Tekst. Uczelnię założył król w 1364 r., ale po jego śmierci podupadła. Odnowiono ją w 1400 r. dzięki zapisowi królowej. W XV w. słynęła z nauczania astronomii. (tekst autorski)',
   T('podaj', 2, 'Podaj imiona króla-założyciela i królowej, której zapis pozwolił odnowić uczelnię.', 'Kazimierz Wielki i Jadwiga.'),
   T('podaj', 1, 'Podaj nazwisko słynnego absolwenta, twórcy teorii heliocentrycznej.', 'Mikołaj Kopernik.')),
]

BANK['nowozytnosc'] = [
 B('Konfederacja warszawska', 'Tekst (na podstawie aktu z 1573 r., tekst autorski). „Ponieważ w naszej Rzeczypospolitej jest niemała różnorodność w sprawach wiary chrześcijańskiej, obiecujemy, że będziemy zachowywać pokój między sobą i nie będziemy przelewać krwi z powodu różnic w wierze”.',
   T('podaj', 1, 'Podaj nazwę aktu i rok jego uchwalenia.', 'Konfederacja warszawska, 1573.'),
   T('wyjasnij', 1, 'Wyjaśnij, w jakiej sytuacji politycznej uchwalono akt.', 'W czasie pierwszego bezkrólewia po śmierci Zygmunta Augusta, by zapewnić pokój przed elekcją.'),
   T('argument', 1, 'Podaj argument, że tolerancja w Rzeczypospolitej była wyjątkowa na tle Europy.', 'W tym czasie we Francji trwały wojny religijne (noc św. Bartłomieja 1572), a w Rzeczypospolitej gwarantowano pokój między wyznaniami.')),
 B('Stefan Batory', 'Tekst. Król utworzył najwyższy sąd szlachecki, piechotę z chłopów z dóbr królewskich i uczelnię w Wilnie. Prowadził zwycięską wojnę z Moskwą o Inflanty. (tekst autorski)',
   T('podaj', 2, 'Podaj nazwy: sądu, piechoty i traktatu kończącego wojnę z Moskwą.', 'Trybunał Koronny; piechota wybraniecka; rozejm w Jamie Zapolskim (1582).')),
 B('Wazowie', 'Zestawienie (tekst autorski). A. Kircholm i zajęcie Moskwy. B. Wojna smoleńska. C. Potop szwedzki i abdykacja.',
   T('przyporzadkuj', 1, 'Przyporządkuj wydarzenia A–C panowaniom: Jan Kazimierz, Władysław IV, Zygmunt III.', 'A — Zygmunt III; B — Władysław IV; C — Jan Kazimierz.'),
   T('wyjasnij', 1, 'Wyjaśnij, jak dążenie Wazów do tronu szwedzkiego wpłynęło na Rzeczpospolitą.', 'Wciągnęło ją w długie wojny ze Szwecją (Inflanty, potop).')),
 B('Jan III Sobieski', 'Zestawienie (tekst autorski). A. Zwycięstwo pod Chocimiem. B. Wybór na króla. C. Odsiecz wiedeńska. D. Pokój Grzymułtowskiego.',
   T('uporzadkuj', 1, 'Podaj lata wydarzeń A–D.', 'A — 1673; B — 1674; C — 1683; D — 1686.'),
   T('wyjasnij', 1, 'Wyjaśnij skutek pokoju Grzymułtowskiego dla Rzeczypospolitej.', 'Ostateczna utrata Kijowa i lewobrzeżnej Ukrainy na rzecz Rosji.')),
]

BANK['xviii-wiek'] = [
 B('Konstytucja 3 maja — chłopi i mieszczanie', 'Tekst (na podstawie Ustawy Rządowej, tekst autorski). „Lud rolniczy, z pod którego ręki płynie najobfitsze bogactw krajowych źródło, przyjmujemy pod opiekę prawa i rządu krajowego”. Prawo o miastach weszło w skład konstytucji.',
   T('wyjasnij', 1, 'Wyjaśnij, co oznaczało dla chłopów przyjęcie ich „pod opiekę prawa”.', 'Umowy z panami miały być respektowane przez państwo; nie zniesiono jednak pańszczyzny ani poddaństwa.'),
   T('podaj', 1, 'Podaj dwa uprawnienia, które mieszczanie uzyskali w 1791 r.', 'Nietykalność osobista, prawo kupna ziemi, dostęp do urzędów, możliwość nobilitacji.')),
 B('Legiony Dąbrowskiego', 'Tekst (tekst autorski na wzór pieśni z 1797 r.). „Jeszcze Polska nie zginęła, kiedy my żyjemy… Marsz, marsz Dąbrowski, z ziemi włoskiej do Polski”.',
   T('podaj', 2, 'Podaj tytuł pieśni, nazwisko autora i rok jej powstania.', '„Pieśń Legionów Polskich we Włoszech” (Mazurek Dąbrowskiego), Józef Wybicki, 1797.'),
   T('wyjasnij', 1, 'Wyjaśnij, z czym Polacy wiązali nadzieje, walcząc we Włoszech.', 'Z pomocą Napoleona (Francji) w odbudowie niepodległej Polski.')),
]

BANK['xix-wiek'] = [
 B('Mesjanizm', 'Tekst (tekst autorski na wzór romantycznego poematu). „Naród polski cierpi i umiera, jak Chrystus, za grzechy innych narodów. Ale trzeciego dnia zmartwychwstanie i przyniesie wolność całej Europie”.',
   T('podaj', 1, 'Podaj nazwę idei wyrażonej w tekście.', 'Mesjanizm (Polska „Chrystusem narodów”).'),
   T('podaj', 1, 'Podaj nazwisko poety, z którym ta idea jest najczęściej łączona.', 'Adam Mickiewicz.'),
   T('wyjasnij', 1, 'Wyjaśnij, w jakich okolicznościach idea ta zyskała popularność.', 'Po upadku powstania listopadowego, wśród Wielkiej Emigracji — dawała sens klęsce i nadzieję.')),
 B('Polacy w zaborze pruskim', 'Tekst. Chłop, któremu władze odmówiły zgody na budowę domu, zamieszkał w wozie cyrkowym. Jego historia obiegła prasę europejską jako symbol oporu przeciw germanizacji. (tekst autorski)',
   T('podaj', 1, 'Podaj nazwisko chłopa.', 'Michał Drzymała.'),
   T('podaj', 1, 'Podaj nazwę instytucji pruskiej, która wykupywała ziemię od Polaków.', 'Komisja Kolonizacyjna (1886).')),
 B('Wielka Emigracja — kultura', 'Zestawienie (tekst autorski). A. „Pan Tadeusz”. B. Polonezy i mazurki. C. „Kordian”. D. „Nie-Boska komedia”.',
   T('przyporzadkuj', 2, 'Przyporządkuj dzieła A–D twórcom: Chopin, Krasiński, Mickiewicz, Słowacki.', 'A — Mickiewicz; B — Chopin; C — Słowacki; D — Krasiński.')),
]

BANK['lata-1914-1939'] = [
 B('Konstytucja marcowa', 'Tekst (na podstawie konstytucji z 1921 r., tekst autorski). „Władza zwierzchnia należy do Narodu. Organami Narodu są: w zakresie ustawodawstwa — Sejm i Senat, w zakresie władzy wykonawczej — Prezydent Rzeczypospolitej łącznie z odpowiedzialnymi ministrami, w zakresie wymiaru sprawiedliwości — niezawisłe sądy”.',
   T('podaj', 2, 'Podaj dwie zasady ustrojowe wyrażone w tekście.', 'Suwerenność narodu i trójpodział władzy.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego konstytucja marcowa dawała słabą pozycję prezydentowi.', 'Endecja obawiała się, że prezydentem zostanie Piłsudski, więc wzmocniono sejm kosztem prezydenta.')),
 B('Zabójstwo prezydenta', 'Tekst. Pięć dni po zaprzysiężeniu pierwszy prezydent Rzeczypospolitej zginął zastrzelony w galerii sztuki „Zachęta”. Sprawca był związany ze środowiskiem nacjonalistycznym. (tekst autorski)',
   T('podaj', 2, 'Podaj nazwisko prezydenta i rok zabójstwa.', 'Gabriel Narutowicz, 1922.'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego wybór Narutowicza wywołał gwałtowny sprzeciw prawicy.', 'Wybrano go głosami lewicy i mniejszości narodowych — prawica uznała go za „prezydenta wybranego przez nie-Polaków”.')),
]

BANK['ii-wojna'] = [
 B('Akcja pod Arsenałem', 'Tekst. W marcu 1943 r. harcerze odbili więźnia przewożonego z siedziby Gestapo. Ranny w akcji „Alek” zmarł, a odbity „Rudy”, skatowany w śledztwie, zmarł tego samego dnia. (tekst autorski)',
   T('podaj', 1, 'Podaj nazwę organizacji, która przeprowadziła akcję.', 'Szare Szeregi.'),
   T('podaj', 1, 'Podaj tytuł książki opisującej losy bohaterów akcji i nazwisko jej autora.', '„Kamienie na szaniec”, Aleksander Kamiński.')),
 B('Witold Pilecki', 'Tekst. Oficer dobrowolnie dał się aresztować w łapance, by trafić do obozu w Oświęcimiu. Tworzył tam konspirację i wysyłał raporty, a po ucieczce walczył w powstaniu warszawskim. Po wojnie został stracony przez komunistów. (tekst autorski)',
   T('podaj', 1, 'Podaj rok śmierci Pileckiego.', '1948.'),
   T('wyjasnij', 1, 'Wyjaśnij znaczenie raportów Pileckiego.', 'Przekazywały aliantom pierwsze szczegółowe informacje o zbrodniach w Auschwitz.')),
]

BANK['polska-po-1945'] = [
 B('Gomułka i Kościół', 'Tekst. W 1966 r. państwo obchodziło tysiąclecie państwa polskiego, a Kościół — tysiąclecie chrztu. Obie strony organizowały konkurencyjne uroczystości. (tekst autorski)',
   T('podaj', 1, 'Podaj nazwę dziewięcioletniego programu przygotowań Kościoła do obchodów.', 'Wielka Nowenna (1957–1966).'),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego władze organizowały konkurencyjne obchody.', 'Chciały osłabić wpływ Kościoła i przedstawić rocznicę jako świeckie święto państwa.')),
 B('Stan wojenny — opór', 'Zestawienie (tekst autorski). A. Podziemne wydawnictwa. B. Strajki okupacyjne w kopalniach. C. Msze za ojczyznę. D. Pomoc rodzinom internowanych.',
   T('wyjasnij', 1, 'Wyjaśnij rolę Kościoła w okresie stanu wojennego.', 'Udzielał schronienia i pomocy represjonowanym, organizował msze za ojczyznę (ks. Popiełuszko), był przestrzenią wolności.'),
   T('podaj', 1, 'Podaj nazwę kopalni, w której zginęło 9 górników.', 'Kopalnia „Wujek”.')),
]

BANK['swiat-po-1945'] = [
 B('Mur berliński', 'Tekst. W sierpniu 1961 r. władze NRD w ciągu jednej nocy odgrodziły Berlin Zachodni. Mur stał 28 lat; przy próbach jego przekroczenia zginęło ponad 100 osób. (tekst autorski)',
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego władze NRD zbudowały mur.', 'By powstrzymać masowe ucieczki mieszkańców NRD na Zachód.'),
   T('podaj', 1, 'Podaj datę upadku muru.', '9 XI 1989.')),
]
