# Treści kursu biologii — porcja 20: pytania ABCD do podrozdziałów z najmniejszą liczbą pytań.
T = {}

T['b-typy-komorek'] = dict(Q=[
 ('Komórka prokariotyczna NIE ma:', ['rybosomów w cytoplazmie', 'błony komórkowej z białkami', '*jądra otoczonego otoczką', 'cytoplazmy z nukleoidem'], 'Nukleoid bez otoczki.'),
 ('Powiększenie mikroskopu z okularem 10× i obiektywem 40× wynosi:', ['50×', '*400×', '4000×', '40×'], 'Iloczyn powiększeń.'),
 ('Mikroskop elektronowy pozwala obserwować:', ['wyłącznie żywe komórki w ruchu', '*ultrastrukturę organelli', 'tylko barwne preparaty', 'wyłącznie tkanki roślinne'], 'Duża rozdzielczość.'),
 ('Komórkę roślinną od zwierzęcej odróżnia obecność:', ['mitochondriów i rybosomów', 'rybosomów i aparatu Golgiego', '*ściany celulozowej i chloroplastów', 'jądra komórkowego i jąderka'], 'Cechy roślinne.'),
])

T['b-mitochondria'] = dict(Q=[
 ('Grzebienie mitochondrialne zwiększają powierzchnię:', ['błony zewnętrznej', '*błony wewnętrznej', 'otoczki jądrowej', 'tylakoidów'], 'Łańcuch oddechowy.'),
 ('Tylakoidy występują w:', ['mitochondriach', '*chloroplastach', 'lizosomach', 'peroksysomach'], 'Faza jasna.'),
 ('Amyloplasty gromadzą:', ['chlorofil', '*skrobię', 'karotenoidy', 'białka zapasowe w wakuoli'], 'Leukoplasty.'),
 ('Dowodem endosymbiozy NIE jest:', ['własne koliste DNA w macierzy', 'rybosomy 70S podobne do bakteryjnych', 'podwójna błona otaczająca organellum', '*obecność w każdej komórce bakterii'], 'Pozostałe — cechy organelli.'),
])

T['b-sciana'] = dict(Q=[
 ('Plazmodesmy to:', ['pory w otoczce jądrowej komórek roślin', '*połączenia cytoplazmatyczne między komórkami roślin', 'kanały jonowe w błonie komórkowej', 'drobne wakuole w młodych komórkach'], 'Przez ściany.'),
 ('Mikrotubule budują:', ['ścianę komórkową', '*wrzeciono podziałowe', 'błonę komórkową', 'rybosomy'], 'Tubulina.'),
 ('Ciśnienie turgorowe komórka roślinna zawdzięcza głównie:', ['lizosomom', '*wakuoli', 'mitochondriom', 'jąderku'], 'Sok komórkowy.'),
 ('Lignina w ścianie komórkowej:', ['zwiększa elastyczność', '*usztywnia i uszczelnia ścianę', 'umożliwia fotosyntezę', 'jest materiałem zapasowym'], 'Drewnienie.'),
])

T['b-atp'] = dict(Q=[
 ('Fosforylacja substratowa zachodzi w:', ['łańcuchu oddechowym', '*glikolizie i cyklu Krebsa', 'fazie jasnej fotosyntezy', 'błonie tylakoidu'], 'Bez gradientu protonów.'),
 ('NAD⁺ w procesach metabolicznych pełni funkcję:', ['enzymu', '*przenośnika elektronów i protonów', 'substratu glikolizy', 'magazynu energii jak ATP'], 'Koenzym.'),
 ('Procesy kataboliczne:', ['wymagają energii', '*uwalniają energię', 'syntetyzują polimery', 'zachodzą tylko u roślin'], 'Rozkład.'),
])

T['b-fermentacje'] = dict(Q=[
 ('Produktami fermentacji alkoholowej są:', ['mleczan i ATP', '*etanol i CO₂', 'woda i CO₂', 'kwas octowy i woda'], 'Drożdże.'),
 ('Z jednej cząsteczki glukozy w fermentacji powstają:', ['36–38 ATP', '*2 ATP', '4 ATP', '0 ATP'], 'Tylko glikoliza.'),
 ('Kwas octowy powstaje w procesie:', ['beztlenowym przez drożdże', '*tlenowym przez bakterie octowe', 'beztlenowym w mięśniach', 'fotosyntezy bakterii'], 'Utlenianie etanolu.'),
])

T['b-genom'] = dict(Q=[
 ('Plazmidy występują głównie u:', ['ssaków', '*bakterii', 'roślin nasiennych', 'wirusów RNA'], 'Wektory.'),
 ('Człowiek ma w komórkach somatycznych:', ['23 pary autosomów bez chromosomów płci', '*22 pary autosomów i parę chromosomów płci', '46 par chromosomów homologicznych', '23 pojedyncze chromosomy'], 'Kariotyp.'),
 ('Telomery chronią:', ['centromery przed rozpadem', '*końce chromosomów', 'rybosomy przed degradacją', 'mRNA przed splicingiem'], 'Skracanie przy replikacji.'),
])

T['b-replikacja'] = dict(Q=[
 ('Helikaza:', ['łączy fragmenty Okazaki', '*rozplata podwójną helisę DNA', 'syntetyzuje startery', 'dobudowuje nukleotydy'], 'Zrywa wiązania wodorowe.'),
 ('Ligaza DNA tworzy wiązania:', ['wodorowe', '*fosfodiestrowe', 'peptydowe', 'glikozydowe'], 'Łączy fragmenty.'),
 ('Replikacja zachodzi w fazie cyklu:', ['G1', '*S', 'G2', 'M'], 'Synteza DNA.'),
])

T['b-apoptoza'] = dict(Q=[
 ('Cytochrom c w apoptozie:', ['zamyka pory w błonie mitochondriów', '*uwolniony do cytoplazmy aktywuje kaspazy', 'naprawia uszkodzone DNA w jądrze', 'hamuje fagocytozę ciałek apoptotycznych'], 'Droga wewnętrzna.'),
 ('Nekroza w odróżnieniu od apoptozy:', ['nie niszczy komórki', '*wywołuje stan zapalny', 'jest zaprogramowana genetycznie', 'wymaga kaspaz'], 'Niekontrolowana.'),
])

T['b-gen'] = dict(Q=[
 ('Locus to:', ['rodzaj allelu', '*miejsce genu na chromosomie', 'fragment intronu', 'kodon STOP'], 'Położenie.'),
 ('Fenotyp zależy od:', ['wyłącznie genotypu', '*genotypu i środowiska', 'wyłącznie środowiska', 'tylko alleli dominujących'], 'Norma reakcji.'),
 ('Gen kodujący rRNA:', ['ulega translacji', '*ulega tylko transkrypcji', 'nie ulega ekspresji', 'występuje tylko u wirusów'], 'Funkcjonalne RNA.'),
])

T['b-regulacja'] = dict(Q=[
 ('W operonie tryptofanowym nadmiar tryptofanu:', ['indukuje transkrypcję genów operonu', '*aktywuje represor i hamuje transkrypcję', 'rozkłada represor i odblokowuje operator', 'nie wpływa na działanie operonu'], 'Korepresor.'),
 ('Enhancery to sekwencje:', ['kodujące białka', '*wzmacniające transkrypcję genów', 'wycinane w splicingu', 'kończące translację'], 'Regulacja u eukariontów.'),
 ('Modyfikacje epigenetyczne:', ['zmieniają sekwencję DNA', '*zmieniają ekspresję bez zmiany sekwencji', 'występują tylko u bakterii', 'zawsze są mutacjami'], 'Np. metylacja.'),
])

T['b-wspoldzialanie'] = dict(Q=[
 ('Stosunek 12 : 3 : 1 w F2 wskazuje na:', ['geny komplementarne', '*epistazę dominującą', 'polimerię', 'dominację niezupełną'], 'Np. dynia.'),
 ('Stosunek 15 : 1 w F2 wskazuje na:', ['epistazę recesywną', '*geny kumulatywne (dublujące się)', 'kodominację', 'allel letalny'], 'Wystarczy jeden allel dominujący.'),
 ('Rodzice z grupami AB i 0 mogą mieć dziecko z grupą:', ['AB lub 0', '*A lub B', 'tylko 0', 'tylko AB'], 'IᴬIᴮ × ii.'),
])

T['b-sprzezenia'] = dict(Q=[
 ('Im dalej od siebie leżą geny na chromosomie, tym:', ['rzadziej zachodzi między nimi crossing-over', '*częściej zachodzi między nimi crossing-over', 'silniej są sprzężone', 'mniej jest rekombinantów'], 'Proporcjonalność.'),
 ('Morgan prowadził badania na:', ['grochu', '*muszce owocowej', 'myszach', 'kukurydzy'], 'Drosophila.'),
 ('1% rekombinantów odpowiada odległości:', ['10 cM', '*1 cM', '0,1 cM', '100 cM'], 'Centymorgan.'),
])

T['b-rodowody'] = dict(Q=[
 ('Cecha występuje w każdym pokoleniu, chory ma zawsze chorego rodzica. Najpewniej dziedziczy się:', ['autosomalnie recesywnie', '*autosomalnie dominująco', 'w sposób mitochondrialny', 'recesywnie z X'], 'Brak przeskakiwania pokoleń.'),
 ('Chorują prawie wyłącznie mężczyźni, choroba przeskakuje pokolenia. Najpewniej:', ['autosomalna dominująca', '*recesywna sprzężona z X', 'holandryczna', 'mitochondrialna'], 'Nosicielki.'),
 ('Dwoje chorych rodziców ma zdrowe dziecko. Cecha jest:', ['recesywna', '*dominująca', 'mitochondrialna', 'sprzężona z Y'], 'Rodzice heterozygotami.'),
])

T['b-mutacje'] = dict(Q=[
 ('Delecja jednego nukleotydu w sekwencji kodującej powoduje zwykle:', ['mutację cichą', '*przesunięcie ramki odczytu', 'zmianę jednego aminokwasu', 'brak skutków'], 'Kod bezprzecinkowy.'),
 ('Translokacja polega na:', ['utracie fragmentu chromosomu', '*przeniesieniu fragmentu na inny chromosom', 'odwróceniu fragmentu', 'podwojeniu fragmentu'], 'Np. chromosom Philadelphia.'),
 ('Organizm 3n to:', ['aneuploid', '*triploid', 'trisomik', 'haploid'], 'Euploidia.'),
])

T['b-choroby-genetyczne'] = dict(Q=[
 ('Zespół Turnera ma kariotyp:', ['47,XXY', '*45,X', '47,XX,+21', '47,XYY'], 'Monosomia X.'),
 ('Mukowiscydoza dziedziczy się:', ['dominująco autosomalnie', '*recesywnie autosomalnie', 'recesywnie z X', 'mitochondrialnie'], 'Gen CFTR.'),
 ('Mutagenem biologicznym jest:', ['promieniowanie UV', 'benzopiren', '*wirus HPV', 'azbest'], 'Wirusy onkogenne.'),
 ('Amniopunkcja polega na pobraniu:', ['krwi matki', '*płynu owodniowego', 'fragmentu łożyska po porodzie', 'krwi pępowinowej po porodzie'], 'Diagnostyka prenatalna.'),
])

T['b-techniki'] = dict(Q=[
 ('Starter w PCR jest:', ['termostabilnym enzymem syntetyzującym DNA', '*krótkim odcinkiem DNA komplementarnym do końca fragmentu', 'pojedynczym nukleotydem przyłączanym do matrycy', 'plazmidem zawierającym gen markerowy'], 'Primer.'),
 ('W elektroforezie DNA wędruje w kierunku:', ['katody (−)', '*anody (+)', 'losowym', 'studzienki'], 'Ładunek ujemny.'),
 ('Lepkie końce powstają po cięciu DNA przez:', ['ligazę', '*enzym restrykcyjny', 'polimerazę', 'helikazę'], 'Cięcie przesunięte.'),
])

T['b-gmo'] = dict(Q=[
 ('Organizm transgeniczny zawiera:', ['wyłącznie własne geny', '*gen innego gatunku', 'zmniejszoną liczbę chromosomów', 'tylko mitochondrialne DNA'], 'Transgen.'),
 ('Komórki iPS powstają z:', ['komórek wczesnych zarodków', '*przeprogramowanych komórek somatycznych', 'dojrzałych plemników', 'erytrocytów pobranych z krwi'], 'Pluripotencja.'),
 ('Komórką totipotencjalną jest:', ['neuron', 'komórka szpiku', '*zygota', 'erytrocyt'], 'Pełny potencjał.'),
])

T['b-biotech-medycyna'] = dict(Q=[
 ('Wektorem w terapii genowej najczęściej jest:', ['bakteria chorobotwórcza', '*zmodyfikowany wirus', 'erytrocyt', 'przeciwciało'], 'Dostarcza gen.'),
 ('Szczepionka mRNA zawiera:', ['osłabione wirusy', '*mRNA kodujące antygen', 'gotowe przeciwciała', 'DNA człowieka'], 'Komórki wytwarzają antygen.'),
])

T['b-biotech-tradycyjna'] = dict(Q=[
 ('Kiszenie kapusty wykorzystuje fermentację:', ['alkoholową', '*mlekową', 'octową', 'metanową'], 'Bakterie mlekowe.'),
 ('Bioremediacja to:', ['hodowla roślin w warunkach in vitro', '*usuwanie zanieczyszczeń przez organizmy', 'selekcja odmian o wysokim plonie', 'produkcja antybiotyków przez grzyby'], 'Np. rozkład ropy.'),
])

T['b-wirusy'] = dict(Q=[
 ('Kapsyd wirusa jest zbudowany z:', ['lipidów', '*białek', 'celulozy', 'kwasów nukleinowych'], 'Kapsomery.'),
 ('Wirus HIV atakuje komórki z receptorem:', ['CD8', '*CD4', 'insulinowym', 'MHC I'], 'Limfocyty Th.'),
 ('Bakteriofagi namnażają się w:', ['komórkach roślin', '*komórkach bakterii', 'erytrocytach', 'wodzie'], 'Pasożyty bakterii.'),
])

T['b-grzyby'] = dict(Q=[
 ('Zarodniki płciowe pieczarki powstają na:', ['workach', '*podstawkach', 'konidioforach', 'rodniach'], 'Podstawczaki.'),
 ('Drożdże rozmnażają się bezpłciowo przez:', ['podział podłużny', '*pączkowanie', 'zarodniki ruchome', 'fragmentację grzybni'], 'Jednokomórkowe.'),
 ('Aflatoksyny wytwarzane są przez:', ['muchomora', '*kropidlaka', 'drożdże piekarskie', 'pieczarkę'], 'Rakotwórcze.'),
])

T['b-systematyka'] = dict(Q=[
 ('Najniższą jednostką systematyczną jest:', ['rodzaj', 'rodzina', '*gatunek', 'rząd'], 'Hierarchia.'),
 ('Ptaki i ssaki jako „zwierzęta stałocieplne” tworzą grupę:', ['monofiletyczną', 'parafiletyczną', '*polifiletyczną', 'siostrzaną'], 'Brak wspólnego bezpośredniego przodka.'),
 ('Na kladogramie bliżej spokrewnione są grupy, które:', ['są narysowane obok siebie', '*mają bliżej położony wspólny węzeł', 'mają podobny wygląd', 'żyją w tym samym środowisku'], 'Wspólny przodek.'),
])

T['b-specjacja'] = dict(Q=[
 ('Izolacja czasowa polega na:', ['różnej budowie narządów', '*rozrodzie w różnych porach', 'bezpłodności mieszańców', 'barierze geograficznej'], 'Prezygotyczna.'),
 ('Specjacja przez poliploidyzację to przykład specjacji:', ['allopatrycznej', '*sympatrycznej', 'kierunkowej', 'konwergentnej'], 'Natychmiastowa izolacja.'),
 ('Doświadczenie Millera-Ureya wykazało możliwość:', ['powstania pierwszych komórek', '*abiotycznej syntezy związków organicznych', 'endosymbiozy mitochondriów', 'samoreplikacji cząsteczek RNA'], 'Ewolucja chemiczna.'),
])

T['b-nisza'] = dict(Q=[
 ('Organizm o wąskim zakresie tolerancji to:', ['eurybiont', '*stenobiont', 'kosmopolita', 'saprobiont'], 'Bioindykatory.'),
 ('Prawo minimum sformułował:', ['Shelford', '*Liebig', 'Gause', 'Darwin'], 'Czynnik ograniczający.'),
 ('Larwy jętek w rzece świadczą o:', ['silnym zanieczyszczeniu', '*czystej, natlenionej wodzie', 'eutrofizacji', 'zasoleniu'], 'Bioindykator.'),
])

T['b-ochrona'] = dict(Q=[
 ('Konwencja CITES reguluje:', ['emisję CO₂', '*handel gatunkami zagrożonymi', 'ochronę ozonu', 'połowy na Bałtyku'], 'Konwencja Waszyngtońska.'),
 ('Najwyższą formą ochrony obszarowej w Polsce jest:', ['park krajobrazowy', '*park narodowy', 'użytek ekologiczny', 'pomnik przyrody'], 'Ochrona całości przyrody.'),
 ('Banki nasion to forma ochrony:', ['in situ', '*ex situ', 'czynnej w parku', 'krajobrazowej'], 'Poza siedliskiem.'),
])

T['b-rozmnazanie'] = dict(Q=[
 ('Ciałko żółte wydziela głównie:', ['FSH', '*progesteron', 'LH', 'oksytocynę'], 'Faza lutealna.'),
 ('Owodnia rozwija się z udziałem:', ['endodermy i ściany macicy', '*ektodermy i mezodermy (błona płodowa)', 'wyłącznie endodermy zarodka', 'tkanki łożyska matki'], 'Błona płodowa.'),
 ('Zarodek najbardziej wrażliwy na teratogeny jest w okresie:', ['płodowym (od 9. tygodnia)', '*zarodkowym (do 8. tygodnia)', 'porodu i połogu', 'tuż po urodzeniu'], 'Organogeneza.'),
])

T['b-skora'] = dict(Q=[
 ('Gorączka powstaje wskutek:', ['uszkodzenia receptorów skóry', '*przestawienia temperatury zadanej w podwzgórzu', 'nadmiaru melaniny w naskórku', 'całkowitego braku wydzielania potu'], 'Pirogeny.'),
 ('Wymiennik przeciwprądowy w kończynach ptaków ogranicza:', ['utratę wody', '*utratę ciepła', 'pobieranie tlenu', 'krzepnięcie krwi'], 'Ciepła krew tętnicza ogrzewa żylną.'),
])

T['b-ruch'] = dict(Q=[
 ('Miozyna tworzy filamenty:', ['cienkie', '*grube', 'pośrednie', 'aktynowe'], 'Prążek A.'),
 ('Staw kolanowy jest stawem:', ['kulistym (wieloosiowym)', '*zawiasowym (z możliwością rotacji)', 'siodełkowym (dwuosiowym)', 'nieruchomym (szwem)'], 'Zginanie i prostowanie.'),
 ('Szpik czerwony w dorosłym organizmie występuje głównie w:', ['trzonach kości długich', '*kościach płaskich i nasadach', 'chrząstkach stawowych', 'ścięgnach mięśni'], 'Krwiotworzenie.'),
])

T['b-odzywianie'] = dict(Q=[
 ('Pepsyna trawi:', ['skrobię', '*białka', 'tłuszcze', 'kwasy nukleinowe'], 'Żołądek.'),
 ('Wchłanianie wody zachodzi głównie w:', ['żołądku', '*jelicie cienkim i grubym', 'przełyku', 'jamie ustnej'], 'Jelito grube — zagęszczanie.'),
 ('Witaminą rozpuszczalną w wodzie jest:', ['A', 'D', '*C', 'K'], 'C i grupa B.'),
])

T['b-oddychanie-czl'] = dict(Q=[
 ('Wymiana gazowa w płucach zachodzi przez:', ['transport aktywny', '*dyfuzję', 'osmozę', 'endocytozę'], 'Gradient ciśnień parcjalnych.'),
 ('Ośrodek oddechowy znajduje się w:', ['móżdżku', '*rdzeniu przedłużonym', 'korze mózgu', 'przysadce'], 'Pień mózgu.'),
])

T['b-tkanki-zwierzece'] = dict(Q=[
 ('Osteoklasty:', ['wytwarzają kość', '*rozkładają tkankę kostną', 'wytwarzają chrząstkę', 'przewodzą impulsy'], 'Przebudowa kości.'),
 ('Komórki glejowe:', ['przewodzą impulsy na duże odległości', '*odżywiają i izolują neurony', 'kurczą się', 'wytwarzają przeciwciała'], 'Wsparcie neuronów.'),
])

T['b-odzywianie-roslin'] = dict(Q=[
 ('Leghemoglobina w brodawkach korzeniowych:', ['transportuje cukry', '*chroni nitrogenazę przed tlenem', 'wiąże azot', 'przeprowadza fotosyntezę'], 'Niskie stężenie O₂.'),
 ('Jemioła pobiera od żywiciela:', ['związki organiczne', '*wodę i sole mineralne', 'tylko światło', 'tlen'], 'Półpasożyt.'),
])

T['b-rozmnazanie-roslin'] = dict(Q=[
 ('Woreczek zalążkowy zawiera zwykle:', ['4 komórki', '*7 komórek (8 jąder)', '2 komórki', '16 komórek'], 'Gametofit żeński.'),
 ('Przedrośle to gametofit:', ['mchu', '*paproci', 'sosny', 'okrytonasiennych'], 'Samodzielny, mały.'),
 ('Pestkowcem jest owoc:', ['pomidora', '*wiśni', 'groszku', 'maku'], 'Zdrewniały endokarp.'),
])

T['b-rozwoj-roslin'] = dict(Q=[
 ('Kwas abscysynowy:', ['przerywa spoczynek nasion', '*zamyka szparki i utrzymuje spoczynek', 'stymuluje podziały', 'przyspiesza dojrzewanie owoców'], 'Hormon stresu.'),
 ('Etiolacja występuje u roślin rosnących:', ['w silnym świetle', '*w ciemności', 'w niskiej temperaturze', 'w zasolonej glebie'], 'Wydłużone, blade.'),
 ('Wernalizacja to pobudzenie kwitnienia przez:', ['długi dzień', '*okres niskiej temperatury', 'etylen', 'światło czerwone'], 'Oziminy.'),
])

T['b-organy'] = dict(Q=[
 ('Bulwa ziemniaka to zmodyfikowana:', ['korzeń spichrzowy', '*łodyga (pęd podziemny)', 'liść spichrzowy', 'kwiatostan'], 'Ma oczka (pąki).'),
 ('Ciernie berberysu to przekształcone:', ['korzenie', '*liście', 'kwiaty', 'owoce'], 'Ochrona.'),
 ('Włośniki występują w strefie:', ['merystematycznej wierzchołka', '*włośnikowej (absorpcyjnej) korzenia', 'czapeczki korzeniowej', 'wydłużania komórek'], 'Pobieranie wody.'),
])

T['b-przeglad-roslin'] = dict(Q=[
 ('U mchów pokoleniem dominującym jest:', ['sporofit', '*gametofit', 'przedrośle', 'zarodnia'], 'Zielona roślinka.'),
 ('Tkanki przewodzące jako pierwsze wykształciły:', ['mchy', '*paprotniki', 'glony', 'wątrobowce'], 'Rośliny naczyniowe.'),
 ('Nasiona okryte owocnią mają:', ['nagonasienne', '*okrytonasienne', 'paprocie', 'skrzypy'], 'Zalążnia.'),
])
