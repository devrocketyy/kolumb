# Treści kursu biologii — porcja 19: dodatkowe pytania ABCD (biochemia, komórka, metabolizm, rośliny, genetyka molekularna, mikroorganizmy, zwierzęta).
T = {}

T['b-bialka'] = dict(Q=[
 ('Struktura II-rzędowa białka stabilizowana jest głównie wiązaniami:', ['peptydowymi', '*wodorowymi', 'disiarczkowymi', 'glikozydowymi'], 'α-helisa, β-harmonijka.'),
 ('Denaturacja białka NIE narusza struktury:', ['II-rzędowej', 'III-rzędowej', '*I-rzędowej', 'IV-rzędowej'], 'Wiązania peptydowe zostają.'),
 ('Mostki disiarczkowe tworzą reszty:', ['seryny', '*cysteiny', 'glicyny', 'lizyny'], 'Grupy –SH.'),
 ('Białko złożone zawiera oprócz aminokwasów:', ['wyłącznie wodę', '*grupę prostetyczną (np. hem, metal)', 'tylko wiązania peptydowe', 'dodatkowe łańcuchy polipeptydowe'], 'Np. hemoglobina.'),
 ('Wysalanie białka jest procesem:', ['nieodwracalnym', '*odwracalnym', 'niszczącym strukturę I-rzędową', 'zachodzącym tylko w 100°C'], 'Koagulacja odwracalna.'),
])

T['b-weglowodany'] = dict(Q=[
 ('Glikogen jest materiałem zapasowym:', ['roślin', '*zwierząt i grzybów', 'wyłącznie bakterii', 'wszystkich organizmów'], 'Wątroba, mięśnie.'),
 ('Celuloza zbudowana jest z reszt:', ['α-glukozy', '*β-glukozy', 'fruktozy', 'galaktozy'], 'Wiązania β-1,4.'),
 ('Sacharoza składa się z:', ['dwóch cząsteczek glukozy', '*glukozy i fruktozy', 'glukozy i galaktozy', 'dwóch cząsteczek fruktozy'], 'Cukier trzcinowy.'),
 ('Cukrem nieredukującym jest:', ['glukoza', 'maltoza', '*sacharoza', 'laktoza'], 'Próba Trommera ujemna.'),
 ('Chityna występuje w:', ['ścianach komórek roślin', '*ścianach grzybów i oskórku stawonogów', 'błonach komórkowych zwierząt', 'ścianach bakterii'], 'Polisacharyd z azotem.'),
])

T['b-lipidy'] = dict(Q=[
 ('Fosfolipidy tworzą dwuwarstwę, ponieważ mają:', ['wyłącznie część hydrofobową', '*hydrofilową głowę i hydrofobowe ogony', 'wiele wiązań peptydowych', 'pierścień steroidowy'], 'Amfipatyczność.'),
 ('Kwasy tłuszczowe nienasycone zawierają:', ['wyłącznie wiązania pojedyncze', '*wiązania podwójne między atomami węgla', 'atomy azotu', 'grupy fosforanowe'], 'Płynność błon.'),
 ('Cholesterol w błonach zwierzęcych:', ['transportuje glukozę', '*reguluje płynność błony', 'tworzy kanały jonowe', 'wiąże tlen'], 'Steroid.'),
 ('Z 1 g tłuszczu organizm uzyskuje w porównaniu z 1 g cukru:', ['tyle samo energii', '*około dwa razy więcej energii', 'dwa razy mniej energii', 'brak energii'], '~38 vs ~17 kJ.'),
])

T['b-woda'] = dict(Q=[
 ('Duża pojemność cieplna wody wynika z:', ['jej niskiej gęstości', '*wiązań wodorowych między cząsteczkami', 'obecności jonów', 'kowalencyjnych wiązań między cząsteczkami'], 'Stabilizacja temperatury.'),
 ('Cząsteczka wody jest polarna, ponieważ:', ['ma ładunek całkowity ujemny i odpycha jony', '*elektrony są przesunięte w stronę tlenu', 'tworzy wiązania jonowe z innymi cząsteczkami', 'zawiera wodór i tlen w równej liczbie atomów'], 'Dipol.'),
])

T['b-kwasy'] = dict(Q=[
 ('Komplementarne pary zasad w DNA to:', ['A–C i G–T', '*A–T i G–C', 'A–U i G–C', 'A–G i C–T'], 'Reguła Chargaffa.'),
 ('Jeśli DNA zawiera 30% adeniny, to cytozyny zawiera:', ['30%', '*20%', '40%', '70%'], 'A = T = 30%; G = C = 20%.'),
 ('Nici w cząsteczce DNA są:', ['równoległe', '*antyrównoległe', 'połączone kowalencyjnie', 'identyczne'], '5′→3′ i 3′→5′.'),
 ('Nukleotyd składa się z:', ['aminokwasu, cukru i zasady', '*zasady azotowej, pentozy i reszty fosforanowej', 'glicerolu i kwasów tłuszczowych', 'pentozy i aminokwasu'], 'Budowa nukleotydu.'),
])

T['b-blony'] = dict(Q=[
 ('Transport aktywny:', ['zachodzi zgodnie z gradientem stężeń', '*wymaga energii z ATP', 'nie wymaga białek błonowych', 'dotyczy tylko wody'], 'Wbrew gradientowi.'),
 ('Komórka roślinna w roztworze hipertonicznym ulega:', ['turgorowi', '*plazmolizie', 'hemolizie', 'cytolizie'], 'Utrata wody.'),
 ('Erytrocyt w wodzie destylowanej:', ['kurczy się', '*pęcznieje i pęka', 'nie zmienia się', 'ulega plazmolizie'], 'Hemoliza.'),
 ('Endocytoza polega na:', ['wydzielaniu substancji z komórki', '*pobieraniu substancji przez wpuklenie błony', 'dyfuzji przez dwuwarstwę', 'transporcie jonów przez kanały'], 'Fagocytoza, pinocytoza.'),
])

T['b-jadro'] = dict(Q=[
 ('Rybosomy 70S występują w:', ['cytoplazmie komórek zwierząt', '*mitochondriach i chloroplastach', 'jądrze komórkowym', 'aparacie Golgiego'], 'Pochodzenie endosymbiotyczne.'),
 ('Lizosomy zawierają:', ['DNA', '*enzymy hydrolityczne', 'chlorofil', 'rybosomy'], 'Trawienie wewnątrzkomórkowe.'),
 ('Synteza lipidów zachodzi w:', ['siateczce szorstkiej', '*siateczce gładkiej', 'jąderku', 'lizosomach'], 'ER gładkie.'),
 ('Jąderko jest miejscem:', ['replikacji DNA', '*powstawania podjednostek rybosomów', 'syntezy białek', 'oddychania komórkowego'], 'rRNA.'),
])

T['b-oddychanie'] = dict(Q=[
 ('Glikoliza zachodzi w:', ['macierzy mitochondrium', '*cytozolu', 'błonie wewnętrznej mitochondrium', 'stromie chloroplastu'], 'Etap beztlenowy.'),
 ('Końcowym akceptorem elektronów w łańcuchu oddechowym jest:', ['NAD⁺', '*tlen', 'CO₂', 'pirogronian'], 'Powstaje woda.'),
 ('CO₂ powstaje podczas:', ['glikolizy', '*reakcji pomostowej i cyklu Krebsa', 'łańcucha oddechowego', 'fosforylacji substratowej w glikolizie'], 'Dekarboksylacje.'),
 ('Najwięcej ATP powstaje w:', ['glikolizie', 'cyklu Krebsa', '*fosforylacji oksydacyjnej', 'reakcji pomostowej'], 'Syntaza ATP.'),
 ('Fermentacja mleczanowa w mięśniach umożliwia:', ['syntezę glukozy', '*regenerację NAD⁺ dla glikolizy', 'produkcję CO₂', 'syntezę ATP w mitochondriach'], 'Glikoliza trwa dalej.'),
])

T['b-fotosynteza'] = dict(Q=[
 ('Tlen wydzielany w fotosyntezie pochodzi z:', ['CO₂', '*wody', 'glukozy', 'chlorofilu'], 'Fotoliza wody.'),
 ('Cykl Calvina zachodzi w:', ['tylakoidach', '*stromie chloroplastu', 'cytozolu', 'mitochondrium'], 'Faza niezależna od światła.'),
 ('Enzymem wiążącym CO₂ w cyklu Calvina jest:', ['karboksylaza PEP', '*RuBisCO', 'syntaza ATP', 'reduktaza NADP⁺'], 'Najliczniejsze białko na Ziemi.'),
 ('Produktami fazy zależnej od światła są:', ['glukoza i tlen', '*ATP, NADPH i tlen', 'CO₂ i woda', 'RuBP i ATP'], 'Siła asymilacyjna.'),
 ('Chlorofil najsłabiej pochłania światło:', ['czerwone', 'niebieskie', '*zielone', 'fioletowe'], 'Odbijane — barwa liści.'),
])

T['b-enzymy'] = dict(Q=[
 ('Enzym obniża:', ['energię produktów', '*energię aktywacji reakcji', 'temperaturę reakcji', 'stężenie substratu'], 'Kataliza.'),
 ('Inhibitor kompetycyjny:', ['wiąże się z centrum allosterycznym', '*konkuruje z substratem o centrum aktywne', 'trwale niszczy enzym', 'zwiększa szybkość reakcji'], 'Podobny do substratu.'),
 ('Hamowanie inhibitora kompetycyjnego można znieść przez:', ['obniżenie temperatury', '*zwiększenie stężenia substratu', 'zmniejszenie stężenia enzymu', 'dodanie drugiego inhibitora'], 'Konkurencja.'),
 ('Koenzymem jest:', ['pepsyna', '*NAD⁺', 'jon Mg²⁺', 'amylaza'], 'Pochodna witaminy.'),
])

T['b-gospodarka-wodna'] = dict(Q=[
 ('Główną siłą transportu wody w drewnie wysokich drzew jest:', ['parcie korzeniowe', '*transpiracja (siła ssąca liści)', 'transport aktywny', 'grawitacja'], 'Kohezja + adhezja.'),
 ('Pasemka Caspary’ego znajdują się w:', ['skórce liścia', '*śródskórni korzenia', 'łyku', 'miękiszu palisadowym'], 'Kontrola wnikania do walca osiowego.'),
 ('Gutacja zachodzi przez:', ['szparki', '*hydatody', 'przetchlinki', 'włośniki'], 'Krople wody.'),
 ('Niedobór magnezu powoduje chlorozę, ponieważ Mg jest składnikiem:', ['celulozy', '*chlorofilu', 'ATP-azy', 'DNA'], 'Centrum chlorofilu.'),
])

T['b-tkanki-roslinne'] = dict(Q=[
 ('Przyrost wtórny na grubość zapewnia:', ['merystem wierzchołkowy', '*kambium i fellogen', 'kolenchyma', 'epiderma'], 'Merystemy boczne.'),
 ('Martwą tkanką wzmacniającą jest:', ['kolenchyma', '*sklerenchyma', 'miękisz', 'tkanka okrywająca'], 'Zdrewniałe ściany.'),
 ('Rurki sitowe przewodzą:', ['wodę z solami', '*roztwory związków organicznych', 'wyłącznie hormony', 'gazy'], 'Łyko.'),
 ('Naczynia i cewki to elementy:', ['łyka', '*drewna', 'kolenchymy', 'miękiszu asymilacyjnego'], 'Martwe, zdrewniałe.'),
])

T['b-translacja'] = dict(Q=[
 ('Ile różnych kodonów koduje aminokwasy?', ['20', '64', '*61', '3'], '64 − 3 STOP.'),
 ('Kodon mRNA 5′-GCU-3′ rozpoznaje antykodon:', ['5′-CGA-3′', '*5′-AGC-3′', '5′-GCU-3′', '5′-UCG-3′'], 'Komplementarny i antyrównoległy.'),
 ('Translacja zachodzi na:', ['jąderku', '*rybosomach', 'chromatynie', 'aparacie Golgiego'], 'Synteza białek.'),
 ('Rybosom przesuwa się wzdłuż mRNA w kierunku:', ['3′→5′', '*5′→3′', 'dowolnym', 'od kodonu STOP'], 'Odczyt od 5′.'),
])

T['b-transkrypcja'] = dict(Q=[
 ('Polimeraza RNA syntetyzuje RNA w kierunku:', ['3′→5′', '*5′→3′', 'obu', 'od terminatora do promotora'], 'Jak polimeraza DNA.'),
 ('Splicing zachodzi u eukariontów w:', ['cytoplazmie', '*jądrze komórkowym', 'rybosomach', 'aparacie Golgiego'], 'Przed eksportem mRNA.'),
 ('Dojrzałe mRNA eukariontów w porównaniu z pre-mRNA:', ['zawiera wszystkie introny genu', '*jest krótsze i ma czapeczkę oraz ogon poli-A', 'nie ma kodonu START ani STOP', 'jest dwuniciowe i zawiera tyminę'], 'Obróbka.'),
])

T['b-bakterie'] = dict(Q=[
 ('Transdukcja to przeniesienie DNA za pośrednictwem:', ['pilusa', '*bakteriofaga', 'otoczenia', 'plazmidu R'], 'Wirus bakteryjny.'),
 ('Bakterie nitryfikacyjne są:', ['fotoautotrofami', '*chemoautotrofami', 'heterotrofami pasożytniczymi', 'saprotrofami'], 'Energia z utleniania NH₃.'),
 ('Chorobą bakteryjną jest:', ['odra', 'grypa', '*tężec', 'malaria'], 'Laseczka tężca.'),
 ('Bakterie Gram-ujemne mają:', ['grubą warstwę mureiny', '*cienką mureinę i błonę zewnętrzną', 'ścianę z chityny', 'brak ściany'], 'Barwienie Grama.'),
])

T['b-protisty'] = dict(Q=[
 ('Mikronukleus pantofelka odpowiada za:', ['metabolizm komórki', '*procesy płciowe (koniugację)', 'ruch rzęsek', 'osmoregulację'], 'Makronukleus — funkcje życiowe.'),
 ('Śpiączkę afrykańską wywołuje:', ['zarodziec', '*świdrowiec', 'pełzak', 'toksoplazma'], 'Mucha tse-tse.'),
 ('Fikoerytryna jest charakterystyczna dla:', ['brunatnic', '*krasnorostów', 'okrzemek', 'zielenic'], 'Czerwone glony.'),
])

T['b-bezkregowce'] = dict(Q=[
 ('Jama chłonąco-trawiąca z jednym otworem występuje u:', ['nicieni', '*parzydełkowców', 'pierścienic', 'owadów'], 'Stułbia.'),
 ('Pajęczaki mają:', ['3 pary odnóży i czułki', '*4 pary odnóży i brak czułków', '5 par odnóży i 2 pary czułków', '2 pary odnóży'], 'Pająki, kleszcze.'),
 ('Metanefrydia to narządy wydalnicze:', ['owadów', '*pierścienic', 'płazińców', 'gąbek'], 'Dżdżownica.'),
 ('Ruch odrzutowy jest typowy dla:', ['małży', '*głowonogów', 'ślimaków', 'skorupiaków'], 'Kałamarnica.'),
])

T['b-kregowce'] = dict(Q=[
 ('Pęcherz pławny występuje u:', ['rekinów i płaszczek', '*ryb kostnoszkieletowych', 'płazów bezogonowych', 'gadów wodnych'], 'Regulacja głębokości.'),
 ('Przepona występuje u:', ['ptaków', 'gadów', '*ssaków', 'płazów'], 'Oddychanie ssaków.'),
 ('Kości pneumatyczne są przystosowaniem:', ['ryb do pływania w głębinach', '*ptaków do lotu', 'gadów do kopania nor', 'ssaków do szybkiego biegu'], 'Lekkość.'),
])
