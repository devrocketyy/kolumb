# Schematy biologii — porcja 3: procesy i cykle z fizjologii człowieka.
S = {}

S['b-odzywianie'] = [
    dict(typ='proces', tytul='Droga pokarmu przez przewód pokarmowy',
         kroki=[('Jama ustna', 'rozdrabnianie, amylaza ślinowa'), ('Gardło'), ('Przełyk', 'ruchy perystaltyczne'),
                ('Żołądek', 'pepsyna, HCl'), ('Dwunastnica', 'sok trzustkowy i żółć'), ('Jelito czcze i kręte', 'trawienie końcowe i wchłanianie'),
                ('Jelito grube', 'wchłanianie wody, bakterie'), ('Odbytnica i odbyt')],
         uwaga='Do dwunastnicy uchodzą przewód trzustkowy i przewód żółciowy wspólny.'),
    dict(typ='proces', tytul='Trawienie białek',
         kroki=[('Białko w pokarmie'), ('Denaturacja w kwaśnym środowisku żołądka', 'HCl'), ('Pepsyna tnie białka na polipeptydy'),
                ('Trypsyna i chymotrypsyna w dwunastnicy', 'krótsze peptydy'), ('Peptydazy jelitowe', 'dipeptydy i aminokwasy'),
                ('Wchłanianie aminokwasów do krwi', 'transport do wątroby żyłą wrotną')],
         uwaga='Enzymy proteolityczne powstają jako nieaktywne proenzymy (pepsynogen, trypsynogen) — chroni to ściany narządów przed strawieniem.'),
    dict(typ='proces', tytul='Trawienie tłuszczów',
         kroki=[('Tłuszcz w pokarmie'), ('Emulgacja przez kwasy żółciowe', 'duże krople → drobne kropelki'), ('Lipaza trzustkowa', 'glicerol i kwasy tłuszczowe'),
                ('Wchłanianie do komórek nabłonka jelita'), ('Odtworzenie tłuszczów i chylomikrony'), ('Transport naczyniami limfatycznymi')],
         uwaga='Żółć nie zawiera enzymów — tylko zwiększa powierzchnię tłuszczu dostępną dla lipazy.'),
]

S['b-odpornosc'] = [
    dict(typ='proces', tytul='Odpowiedź odpornościowa humoralna',
         kroki=[('Wniknięcie antygenu'), ('Fagocytoza i prezentacja antygenu przez makrofaga', 'z białkami MHC II'),
                ('Aktywacja limfocytu Th'), ('Aktywacja limfocytu B rozpoznającego antygen'), ('Namnażanie limfocytów B'),
                ('Różnicowanie w plazmocyty i komórki pamięci'), ('Wydzielanie przeciwciał', 'neutralizacja i oznaczanie antygenu')],
         uwaga='Komórki pamięci sprawiają, że odpowiedź wtórna jest szybsza i silniejsza — na tym opiera się szczepienie.'),
    dict(typ='proces', tytul='Odpowiedź odpornościowa komórkowa',
         kroki=[('Komórka zakażona wirusem prezentuje antygen', 'z białkami MHC I'), ('Rozpoznanie przez limfocyt Tc'),
                ('Pobudzenie przez limfocyt Th', 'cytokiny'), ('Namnażanie limfocytów Tc'),
                ('Zniszczenie komórki zakażonej', 'perforyny i wywołanie apoptozy'), ('Powstanie limfocytów pamięci')],
         uwaga='HIV atakuje limfocyty Th — dlatego osłabia zarówno odpowiedź humoralną, jak i komórkową.'),
    dict(typ='proces', tytul='Stan zapalny',
         kroki=[('Uszkodzenie tkanki i wniknięcie drobnoustrojów'), ('Uwolnienie histaminy przez komórki tuczne'),
                ('Rozszerzenie naczyń i wzrost przepuszczalności', 'zaczerwienienie, obrzęk, ucieplenie'), ('Napływ neutrofili i makrofagów'),
                ('Fagocytoza drobnoustrojów'), ('Usunięcie martwych komórek i regeneracja')],
         uwaga='Klasyczne objawy stanu zapalnego: zaczerwienienie, obrzęk, ból, podwyższona temperatura, upośledzenie funkcji.'),
]

S['b-oddychanie-czl'] = [
    dict(typ='proces', tytul='Droga powietrza w układzie oddechowym',
         kroki=[('Jama nosowa', 'ogrzanie, nawilżenie, oczyszczenie'), ('Gardło'), ('Krtań', 'nagłośnia, struny głosowe'), ('Tchawica'),
                ('Oskrzela główne'), ('Oskrzeliki'), ('Pęcherzyki płucne', 'wymiana gazowa')],
         uwaga='Gardło jest wspólnym odcinkiem dróg oddechowych i pokarmowych — nagłośnia zamyka krtań podczas połykania.'),
    dict(typ='proces', tytul='Mechanizm wdechu',
         kroki=[('Impulsy z ośrodka oddechowego w rdzeniu przedłużonym'), ('Skurcz przepony', 'przepona obniża się'),
                ('Skurcz mięśni międzyżebrowych zewnętrznych', 'żebra unoszą się'), ('Wzrost objętości klatki piersiowej'),
                ('Spadek ciśnienia w płucach poniżej atmosferycznego'), ('Napływ powietrza do płuc')],
         uwaga='Spokojny wydech jest bierny — mięśnie rozkurczają się, a sprężyste płuca się zapadają.'),
    dict(typ='proces', tytul='Transport tlenu z płuc do komórek',
         kroki=[('Dyfuzja O₂ z pęcherzyka do krwi'), ('Wiązanie O₂ z hemoglobiną w erytrocytach', 'oksyhemoglobina'),
                ('Transport krwią tętniczą w krwiobiegu dużym'), ('Oddysocjowanie O₂ w tkankach', 'niskie pO₂, wyższe pCO₂, niższe pH'),
                ('Dyfuzja O₂ do komórek'), ('Zużycie O₂ w mitochondriach')],
         uwaga='Efekt Bohra: więcej CO₂ i niższe pH zmniejszają powinowactwo hemoglobiny do tlenu — tkanki pracujące dostają więcej O₂.'),
]

S['b-krazenie'] = [
    dict(typ='cykl', tytul='Krwiobieg duży i mały',
         kroki=[('Lewa komora'), ('Aorta i tętnice', 'krew natleniona'), ('Naczynia włosowate narządów', 'oddanie O₂'),
                ('Żyły główne', 'krew odtlenowana'), ('Prawy przedsionek'), ('Prawa komora'), ('Pień płucny i tętnice płucne'),
                ('Naczynia włosowate płuc', 'pobranie O₂'), ('Żyły płucne'), ('Lewy przedsionek')],
         uwaga='Tętnice płucne niosą krew odtlenowaną, a żyły płucne — natlenioną. Nazwa naczynia zależy od kierunku przepływu, nie od zawartości tlenu.'),
    dict(typ='cykl', tytul='Cykl pracy serca',
         kroki=[('Rozkurcz całego serca', 'krew napływa do przedsionków i komór'), ('Skurcz przedsionków', 'dopełnienie komór'),
                ('Zamknięcie zastawek przedsionkowo-komorowych', 'pierwszy ton serca'), ('Skurcz komór', 'otwarcie zastawek półksiężycowatych'),
                ('Wyrzut krwi do aorty i pnia płucnego'), ('Zamknięcie zastawek półksiężycowatych', 'drugi ton serca')],
         uwaga='Zastawki zapewniają jednokierunkowy przepływ krwi — otwierają się i zamykają pod wpływem różnicy ciśnień.'),
    dict(typ='proces', tytul='Przewodzenie pobudzenia w sercu',
         kroki=[('Węzeł zatokowo-przedsionkowy', 'rozrusznik, ok. 70 impulsów/min'), ('Mięśniówka przedsionków'),
                ('Węzeł przedsionkowo-komorowy', 'opóźnienie przewodzenia'), ('Pęczek Hisa'), ('Odnogi pęczka'), ('Włókna Purkinjego', 'skurcz komór')],
         uwaga='Opóźnienie w węźle przedsionkowo-komorowym pozwala przedsionkom skurczyć się, zanim skurczą się komory.'),
    dict(typ='proces', tytul='Krzepnięcie krwi',
         kroki=[('Uszkodzenie naczynia'), ('Skurcz naczynia'), ('Przyleganie i zlepianie płytek krwi', 'czop płytkowy'),
                ('Uwolnienie czynników krzepnięcia', 'z udziałem Ca²⁺ i witaminy K'), ('Protrombina → trombina'),
                ('Fibrynogen → fibryna (włóknik)'), ('Sieć włóknika z krwinkami — skrzep')],
         uwaga='Hemofilia to brak czynnika krzepnięcia (VIII lub IX) — gen leży na chromosomie X.'),
]

S['b-wydalanie'] = [
    dict(typ='proces', tytul='Powstawanie moczu w nefronie',
         kroki=[('Kłębuszek nerkowy', 'filtracja osocza'), ('Torebka Bowmana', 'mocz pierwotny, ok. 180 l/dobę'),
                ('Kanalik kręty I rzędu', 'resorpcja glukozy, aminokwasów, Na⁺, wody'), ('Pętla Henlego', 'zagęszczanie rdzenia nerki'),
                ('Kanalik kręty II rzędu', 'sekrecja H⁺, K⁺, regulacja przez aldosteron'), ('Kanalik zbiorczy', 'resorpcja wody pod wpływem ADH'),
                ('Mocz ostateczny', 'ok. 1,5 l/dobę')],
         uwaga='Glukoza w moczu oznacza, że jej stężenie we krwi przekroczyło próg nerkowy — typowy objaw cukrzycy.'),
    dict(typ='proces', tytul='Droga moczu',
         kroki=[('Nefrony'), ('Kanaliki zbiorcze'), ('Kielichy nerkowe'), ('Miedniczka nerkowa'), ('Moczowód'), ('Pęcherz moczowy'), ('Cewka moczowa')],
         uwaga='Pęcherz moczowy magazynuje mocz; jego opróżnianie to odruch kontrolowany przez rdzeń kręgowy i świadomie przez mózg.'),
    dict(typ='proces', tytul='Cykl mocznikowy — w skrócie',
         kroki=[('Rozkład aminokwasów', 'odłączenie grupy aminowej'), ('Powstaje amoniak', 'silnie toksyczny'),
                ('Przekształcenie amoniaku w mocznik w wątrobie', 'zużycie ATP'), ('Transport mocznika krwią do nerek'), ('Wydalenie z moczem')],
         uwaga='Mocznik jest mniej toksyczny od amoniaku, ale jego synteza kosztuje energię — dlatego ryby wydalają amoniak bezpośrednio do wody.'),
]

S['b-hormony'] = [
    dict(typ='proces', tytul='Regulacja poziomu glukozy po posiłku',
         kroki=[('Wzrost stężenia glukozy we krwi'), ('Pobudzenie komórek β wysp trzustki'), ('Wydzielenie insuliny'),
                ('Pobieranie glukozy przez komórki mięśni i tkanki tłuszczowej'), ('Synteza glikogenu w wątrobie i mięśniach'),
                ('Spadek stężenia glukozy do normy')],
         uwaga='W cukrzycy typu 1 brakuje insuliny (zniszczenie komórek β), w typie 2 komórki są na nią oporne.'),
    dict(typ='proces', tytul='Oś podwzgórze–przysadka–tarczyca',
         kroki=[('Podwzgórze wydziela TRH (tyreoliberynę)'), ('Przysadka wydziela TSH (tyreotropinę)'),
                ('Tarczyca wydziela tyroksynę (T₄) i T₃'), ('Przyspieszenie metabolizmu komórek'),
                ('Wysoki poziom T₄ hamuje wydzielanie TRH i TSH', 'ujemne sprzężenie zwrotne')],
         uwaga='Niedobór jodu: mało tyroksyny → dużo TSH → przerost tarczycy (wole).'),
    dict(typ='proces', tytul='Działanie hormonu steroidowego',
         kroki=[('Hormon przenika przez błonę komórkową'), ('Wiązanie z receptorem w cytoplazmie lub jądrze'),
                ('Kompleks hormon–receptor wiąże się z DNA'), ('Zmiana transkrypcji wybranych genów'), ('Synteza nowych białek — efekt działania')],
         uwaga='Hormony białkowe nie przechodzą przez błonę — działają przez receptory błonowe i przekaźniki wtórne (np. cAMP).'),
]

S['b-nerwy'] = [
    dict(typ='proces', tytul='Potencjał czynnościowy',
         kroki=[('Potencjał spoczynkowy', 'ok. −70 mV'), ('Bodziec przekracza próg pobudliwości'), ('Depolaryzacja', 'otwarcie kanałów Na⁺, napływ Na⁺'),
                ('Odwrócenie polaryzacji', 'ok. +30 mV'), ('Repolaryzacja', 'otwarcie kanałów K⁺, wypływ K⁺'), ('Hiperpolaryzacja'),
                ('Przywrócenie stanu spoczynku', 'pompa Na⁺/K⁺')],
         uwaga='Zasada „wszystko albo nic”: bodziec podprogowy nie wywołuje impulsu, a silniejszy bodziec zwiększa częstotliwość, nie wielkość potencjału.'),
    dict(typ='proces', tytul='Przekazywanie impulsu przez synapsę chemiczną',
         kroki=[('Impuls dociera do zakończenia aksonu'), ('Otwarcie kanałów Ca²⁺ i napływ wapnia'), ('Egzocytoza neuroprzekaźnika do szczeliny'),
                ('Wiązanie neuroprzekaźnika z receptorami błony postsynaptycznej'), ('Otwarcie kanałów jonowych — depolaryzacja'),
                ('Rozkład lub wychwyt zwrotny neuroprzekaźnika', 'np. acetylocholinesteraza')],
         uwaga='Synapsa chemiczna przewodzi jednokierunkowo i z opóźnieniem — to miejsce działania wielu leków i toksyn.'),
    dict(typ='proces', tytul='Łuk odruchowy',
         kroki=[('Receptor', 'odbiera bodziec'), ('Neuron czuciowy (dośrodkowy)', 'korzeń grzbietowy'), ('Ośrodek w rdzeniu kręgowym', 'synapsy, neurony pośredniczące'),
                ('Neuron ruchowy (odśrodkowy)', 'korzeń brzuszny'), ('Efektor', 'mięsień lub gruczoł')],
         uwaga='W odruchu kolanowym nie ma neuronu pośredniczącego — to odruch monosynaptyczny.'),
    dict(typ='proces', tytul='Droga światła w oku',
         kroki=[('Rogówka'), ('Komora przednia z cieczą wodnistą'), ('Źrenica', 'otwór w tęczówce'), ('Soczewka', 'akomodacja'),
                ('Ciało szkliste'), ('Siatkówka', 'pręciki i czopki'), ('Nerw wzrokowy'), ('Kora wzrokowa płata potylicznego')],
         uwaga='Na siatkówce powstaje obraz rzeczywisty, odwrócony i pomniejszony — mózg go „odwraca”.'),
    dict(typ='proces', tytul='Droga dźwięku w uchu',
         kroki=[('Małżowina uszna'), ('Przewód słuchowy zewnętrzny'), ('Błona bębenkowa'), ('Kosteczki słuchowe', 'młoteczek, kowadełko, strzemiączko'),
                ('Okienko owalne'), ('Ślimak — drgania płynu'), ('Narząd Cortiego — komórki rzęsate'), ('Nerw słuchowy i kora płata skroniowego')],
         uwaga='Trąbka słuchowa wyrównuje ciśnienie po obu stronach błony bębenkowej.'),
]

S['b-ruch'] = [
    dict(typ='proces', tytul='Skurcz mięśnia szkieletowego',
         kroki=[('Impuls nerwowy w płytce nerwowo-mięśniowej', 'acetylocholina'), ('Depolaryzacja błony włókna mięśniowego'),
                ('Uwolnienie Ca²⁺ z siateczki sarkoplazmatycznej'), ('Odsłonięcie miejsc wiązania na aktynie', 'Ca²⁺ wiąże troponinę'),
                ('Tworzenie mostków poprzecznych miozyna–aktyna'), ('Przesuwanie filamentów kosztem ATP'), ('Skrócenie sarkomerów')],
         uwaga='ATP jest potrzebny także do odłączenia miozyny od aktyny — jego brak po śmierci powoduje stężenie pośmiertne.'),
]

S['b-skora'] = [
    dict(typ='proces', tytul='Termoregulacja przy przegrzaniu',
         kroki=[('Wzrost temperatury ciała'), ('Odbiór przez termoreceptory'), ('Ośrodek termoregulacji w podwzgórzu'),
                ('Rozszerzenie naczyń skóry', 'większa utrata ciepła'), ('Wydzielanie potu', 'parowanie chłodzi skórę'),
                ('Spadek temperatury do normy')],
         uwaga='Przy wysokiej wilgotności powietrza pot słabo paruje — chłodzenie jest mniej skuteczne.'),
    dict(typ='proces', tytul='Termoregulacja przy wychłodzeniu',
         kroki=[('Spadek temperatury ciała'), ('Odbiór przez termoreceptory'), ('Ośrodek termoregulacji w podwzgórzu'),
                ('Zwężenie naczyń skóry', 'mniejsza utrata ciepła'), ('Drżenie mięśni', 'produkcja ciepła'),
                ('Wzrost wydzielania tyroksyny i adrenaliny', 'szybszy metabolizm'), ('Wzrost temperatury do normy')],
         uwaga='Termoregulacja to przykład ujemnego sprzężenia zwrotnego — reakcja przeciwdziała zmianie.'),
]

S['b-rozmnazanie'] = [
    dict(typ='cykl', tytul='Cykl miesiączkowy',
         kroki=[('Faza menstruacyjna', 'złuszczenie endometrium, spadek progesteronu'), ('Faza folikularna', 'FSH: dojrzewanie pęcherzyka, estrogeny odbudowują endometrium'),
                ('Szczyt LH'), ('Owulacja', 'ok. 14. dnia cyklu 28-dniowego'), ('Faza lutealna', 'ciałko żółte wydziela progesteron'),
                ('Zanik ciałka żółtego przy braku zapłodnienia')],
         uwaga='Jeśli dojdzie do zapłodnienia, hCG z zarodka podtrzymuje ciałko żółte — dlatego testy ciążowe wykrywają hCG.'),
    dict(typ='proces', tytul='Od zapłodnienia do zagnieżdżenia',
         kroki=[('Zapłodnienie w jajowodzie'), ('Zygota'), ('Bruzdkowanie', 'morula'), ('Blastocysta'),
                ('Wędrówka do macicy'), ('Implantacja w błonie śluzowej macicy', 'ok. 6–7 dni po zapłodnieniu')],
         uwaga='Ciąża pozamaciczna powstaje, gdy zarodek zagnieździ się poza macicą — najczęściej w jajowodzie.'),
    dict(typ='proces', tytul='Droga plemników',
         kroki=[('Kanaliki nasienne jąder', 'spermatogeneza'), ('Najądrze', 'dojrzewanie i magazynowanie'), ('Nasieniowód'),
                ('Gruczoły dodatkowe', 'pęcherzyki nasienne, gruczoł krokowy'), ('Cewka moczowa')],
         uwaga='Jądra leżą w mosznie, bo spermatogeneza wymaga temperatury niższej niż temperatura wnętrza ciała.'),
]

S['b-tkanki-zwierzece'] = [
    dict(typ='proces', tytul='Hematopoeza — powstawanie krwinek',
         kroki=[('Krwiotwórcza komórka macierzysta w szpiku czerwonym'), ('Komórki progenitorowe linii szpikowej i limfoidalnej'),
                ('Erytroblasty — erytrocyty', 'utrata jądra u ssaków'), ('Megakariocyty — płytki krwi', 'fragmenty cytoplazmy'),
                ('Granulocyty i monocyty'), ('Limfocyty', 'dojrzewanie w szpiku (B) lub grasicy (T)')],
         uwaga='Produkcję erytrocytów pobudza erytropoetyna (EPO) wydzielana przez nerki przy niedotlenieniu.'),
]
