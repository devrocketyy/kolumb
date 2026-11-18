# Treści kursu biologii — porcja 13: Genetyka molekularna (gen, transkrypcja, translacja, regulacja).
T = {}

T['b-gen'] = dict(F=[
 ('Wyjaśnij pojęcie: gen', 'Odcinek DNA zawierający informację o budowie produktu — białka (łańcucha polipeptydowego) lub funkcjonalnego RNA (rRNA, tRNA), wraz z sekwencjami regulatorowymi.'),
 ('Budowa genu eukariotycznego', 'Promotor (miejsce przyłączenia polimerazy RNA), sekwencja kodująca złożona z eksonów przedzielonych intronami, terminator; dodatkowo sekwencje wzmacniające (enhancery) i wyciszające.'),
 ('Wyjaśnij pojęcie: ekson i intron', 'Ekson — fragment genu obecny w dojrzałym mRNA (kodujący); intron — fragment niekodujący, przepisywany na pre-mRNA i wycinany w splicingu.'),
 ('Budowa genu prokariotycznego', 'Zwykle ciągła sekwencja kodująca (bez intronów); geny o wspólnej funkcji często zorganizowane w operony pod kontrolą jednego promotora.'),
 ('Wyjaśnij pojęcie: promotor', 'Sekwencja DNA przed genem, do której przyłącza się polimeraza RNA (z czynnikami transkrypcyjnymi) i która wyznacza początek oraz nić matrycową transkrypcji.'),
 ('Wyjaśnij pojęcie: nić matrycowa i kodująca', 'Matrycowa (antysensowna) — odczytywana przez polimerazę RNA; kodująca (sensowna) — ma sekwencję taką jak mRNA (z T zamiast U).'),
 ('Wyjaśnij pojęcie: allele', 'Różne wersje tego samego genu zajmujące ten sam locus w chromosomach homologicznych.'),
 ('Wyjaśnij pojęcie: genotyp i fenotyp', 'Genotyp — zestaw alleli (genów) organizmu; fenotyp — zespół cech, wynik działania genotypu i środowiska.'),
 ('Wyjaśnij pojęcie: ekspresja genu', 'Proces realizacji informacji genetycznej: transkrypcja (DNA → RNA) i, dla genów kodujących białka, translacja (mRNA → białko), wraz z obróbką i modyfikacjami.'),
 ('Wyjaśnij pojęcie: centralny dogmat biologii molekularnej', 'Przepływ informacji DNA → RNA → białko; wyjątki: odwrotna transkrypcja (RNA → DNA u retrowirusów), replikacja RNA u wirusów RNA.'),
 ('Dlaczego jeden gen może kodować kilka białek?', 'Dzięki alternatywnemu splicingowi — z tego samego pre-mRNA mogą powstać różne mRNA przez łączenie różnych zestawów eksonów.'),
 ('Wyjaśnij pojęcie: geny metabolizmu podstawowego', 'Geny konstytutywne (housekeeping) — ulegają ekspresji we wszystkich komórkach, bo kodują białka niezbędne do życia (np. enzymy glikolizy, rybosomy).'),
], Q=[
 ('Introny są:', ['obecne w dojrzałym mRNA', '*wycinane podczas splicingu', 'typowe dla bakterii', 'miejscem przyłączenia polimerazy'], 'Niekodujące fragmenty.'),
 ('Polimeraza RNA przyłącza się do:', ['terminatora', '*promotora', 'intronu', 'kodonu START'], 'Początek transkrypcji.'),
 ('Odwrotna transkrypcja (RNA → DNA) zachodzi u:', ['wszystkich bakterii', '*retrowirusów (np. HIV)', 'wszystkich roślin', 'mitochondriów'], 'Wyjątek od dogmatu.'),
], pp='XIII.1')

T['b-transkrypcja'] = dict(F=[
 ('Wyjaśnij pojęcie: transkrypcja', 'Synteza RNA na matrycy jednej nici DNA przez polimerazę RNA, zgodnie z zasadą komplementarności (A–U, T–A, G–C, C–G).'),
 ('Etapy transkrypcji', 'Inicjacja (przyłączenie polimerazy do promotora, rozplecenie DNA) → elongacja (synteza RNA 5′→3′) → terminacja (na terminatorze, uwolnienie RNA).'),
 ('Czym różni się transkrypcja od replikacji?', 'Kopiowany jest tylko fragment DNA (gen) i jedna nić; produktem jest jednoniciowe RNA (z U i rybozą); polimeraza RNA nie potrzebuje startera.'),
 ('Gdzie zachodzi transkrypcja u eukariontów i prokariontów?', 'Eukarionty — w jądrze (oraz mitochondriach i plastydach); prokarionty — w cytoplazmie, równocześnie z translacją.'),
 ('Wyjaśnij pojęcie: obróbka (dojrzewanie) pre-mRNA', 'U eukariontów: dołączenie czapeczki (5′), dołączenie ogona poli-A (3′), wycięcie intronów i połączenie eksonów (splicing) — powstaje dojrzałe mRNA.'),
 ('Rola czapeczki i ogona poli-A', 'Chronią mRNA przed degradacją, ułatwiają transport z jądra i przyłączenie rybosomu (czapeczka).'),
 ('Wyjaśnij pojęcie: splicing', 'Wycinanie intronów z pre-mRNA i łączenie eksonów, przeprowadzane przez spliceosom (kompleks snRNA i białek).'),
 ('Dlaczego u bakterii translacja może zachodzić w trakcie transkrypcji?', 'Brak otoczki jądrowej oddzielającej DNA od rybosomów i brak obróbki mRNA — rybosomy przyłączają się do powstającego mRNA.'),
 ('Rodzaje RNA i ich funkcje', 'mRNA — przenosi informację o sekwencji aminokwasów; tRNA — dostarcza aminokwasy do rybosomu; rRNA — budulec i katalizator rybosomu; snRNA — splicing; miRNA — regulacja ekspresji.'),
 ('Jak ustalić sekwencję mRNA na podstawie nici matrycowej DNA?', 'Zapisać komplementarną sekwencję (A→U, T→A, G→C, C→G), pamiętając, że mRNA jest antyrównoległe do matrycy; mRNA ma taką sekwencję jak nić kodująca, z U zamiast T.'),
 ('Wyjaśnij pojęcie: odwrotna transkryptaza', 'Enzym retrowirusów syntetyzujący DNA na matrycy RNA — wykorzystywany w biotechnologii do otrzymywania cDNA (bez intronów).'),
], Q=[
 ('W RNA zamiast tyminy występuje:', ['cytozyna', '*uracyl', 'adenina', 'guanina'], 'A–U.'),
 ('Ogon poli-A dołączany jest do końca:', ['5′ mRNA', '*3′ mRNA', '5′ DNA', 'intronu'], 'Obróbka pre-mRNA.'),
 ('Jeśli nić matrycowa DNA ma fragment 3′-TAC-5′, to mRNA ma:', ['5′-ATG-3′', '*5′-AUG-3′', '5′-UAC-3′', '3′-AUG-5′'], 'Komplementarność i antyrównoległość.'),
 ('Splicing przeprowadza:', ['rybosom', '*spliceosom', 'polimeraza DNA', 'ligaza DNA'], 'snRNA + białka.'),
], pp='XIII.2–3')

T['b-translacja'] = dict(F=[
 ('Wyjaśnij pojęcie: kod genetyczny', 'Sposób zapisu informacji o kolejności aminokwasów w białku za pomocą sekwencji nukleotydów — trójek (kodonów) w mRNA.'),
 ('Cechy kodu genetycznego', 'Trójkowy, jednoznaczny, zdegenerowany (wiele kodonów dla jednego aminokwasu), bezprzecinkowy, niezachodzący, uniwersalny (z nielicznymi wyjątkami, np. mitochondria).'),
 ('Wyjaśnij pojęcie: zdegenerowanie kodu', 'Jeden aminokwas może być kodowany przez kilka kodonów (64 kodony, 20 aminokwasów) — różnią się zwykle trzecim nukleotydem; zmniejsza skutki mutacji.'),
 ('Wyjaśnij pojęcie: jednoznaczność kodu', 'Dany kodon oznacza zawsze tylko jeden aminokwas.'),
 ('Wyjaśnij pojęcie: kodon START i STOP', 'START — AUG (metionina), rozpoczyna translację; STOP — UAA, UAG, UGA, nie kodują aminokwasów, kończą translację.'),
 ('Wyjaśnij pojęcie: antykodon', 'Trójka nukleotydów w pętli tRNA, komplementarna do kodonu mRNA — zapewnia wstawienie właściwego aminokwasu.'),
 ('Budowa tRNA', 'Krótki łańcuch RNA o strukturze „liścia koniczyny”: pętla z antykodonem i koniec 3′ (CCA), do którego przyłączany jest aminokwas.'),
 ('Wyjaśnij pojęcie: aktywacja aminokwasów', 'Przyłączenie aminokwasu do właściwego tRNA przez syntetazę aminoacylo-tRNA kosztem ATP.'),
 ('Budowa rybosomu', 'Podjednostka mała (wiąże mRNA) i duża (katalizuje wiązanie peptydowe); miejsca A (aminoacylowe), P (peptydylowe), E (wyjścia).'),
 ('Etapy translacji', 'Inicjacja (połączenie mRNA, małej podjednostki, tRNA z metioniną przy AUG i dużej podjednostki) → elongacja (dołączanie kolejnych aminokwasów, przesuwanie rybosomu o kodon) → terminacja (kodon STOP, czynnik uwalniający, rozpad kompleksu).'),
 ('Co katalizuje tworzenie wiązania peptydowego?', 'rRNA dużej podjednostki rybosomu (rybozym — aktywność peptydylotransferazy).'),
 ('Wyjaśnij pojęcie: polisom', 'Kilka rybosomów jednocześnie tłumaczących tę samą cząsteczkę mRNA — szybka synteza wielu kopii białka.'),
 ('Gdzie powstają białka wydzielnicze i błonowe?', 'Na rybosomach siateczki śródplazmatycznej szorstkiej; następnie modyfikowane w ER i aparacie Golgiego.'),
 ('Wyjaśnij pojęcie: modyfikacje potranslacyjne', 'Zmiany białka po translacji: fałdowanie (z udziałem białek opiekuńczych), przyłączanie cukrów (glikozylacja), fosforylacja, cięcie (np. proinsulina → insulina), tworzenie mostków disiarczkowych.'),
 ('Jak odczytać sekwencję aminokwasów z mRNA?', 'Znaleźć pierwszy kodon AUG (od 5′), czytać kolejne trójki do kodonu STOP, korzystając z tabeli kodu genetycznego.'),
 ('Ile nukleotydów mRNA koduje białko złożone ze 100 aminokwasów?', '300 nukleotydów kodujących + 3 nukleotydy kodonu STOP = 303 (bez sekwencji niekodujących UTR).'),
 ('Dlaczego liczba nukleotydów genu eukariotycznego jest dużo większa niż 3 × liczba aminokwasów?', 'Gen zawiera introny, promotor, sekwencje nieulegające translacji (UTR) i kodon STOP.'),
], Q=[
 ('Kodonem START jest:', ['UAA', '*AUG', 'UGA', 'UAG'], 'Metionina.'),
 ('Zdegenerowanie kodu oznacza, że:', ['jeden kodon koduje kilka aminokwasów', '*jeden aminokwas może być kodowany przez kilka kodonów', 'kod różni się między gatunkami', 'kodony nakładają się na siebie'], '64 kodony, 20 aminokwasów.'),
 ('Antykodon znajduje się w:', ['mRNA', '*tRNA', 'rRNA', 'DNA'], 'Komplementarny do kodonu.'),
 ('Wiązanie peptydowe tworzone jest dzięki aktywności:', ['tRNA', 'mRNA', '*rRNA dużej podjednostki', 'polimerazy RNA'], 'Rybozym.'),
 ('Aminokwas przyłączany jest do tRNA przez:', ['rybosom', '*syntetazę aminoacylo-tRNA', 'polimerazę RNA', 'ligazę'], 'Aktywacja z ATP.'),
], pp='XIII.4–6')

T['b-regulacja'] = dict(F=[
 ('Wyjaśnij pojęcie: regulacja ekspresji genów', 'Kontrola tego, które geny, kiedy i w jakim stopniu ulegają ekspresji — podstawa różnicowania komórek i reakcji na środowisko.'),
 ('Wyjaśnij pojęcie: operon', 'U prokariontów: zespół genów struktury pod kontrolą wspólnego promotora i operatora, transkrybowanych razem na jedną cząsteczkę mRNA.'),
 ('Budowa operonu laktozowego', 'Promotor, operator, geny struktury (kodujące enzymy rozkładu laktozy, m.in. β-galaktozydazę); gen regulatorowy (poza operonem) koduje represor.'),
 ('Działanie operonu laktozowego bez laktozy', 'Represor wiąże się z operatorem i blokuje polimerazę RNA — geny nie ulegają transkrypcji.'),
 ('Działanie operonu laktozowego przy obecności laktozy', 'Laktoza (allolaktoza) wiąże represor i zmienia jego kształt — odłącza się od operatora, polimeraza transkrybuje geny (operon indukowany).'),
 ('Wyjaśnij pojęcie: operon indukowany i represyjny', 'Indukowany (np. lac) — włączany przez substrat; represyjny (np. trp) — wyłączany przez nadmiar produktu (korepresor aktywuje represor).'),
 ('Działanie operonu tryptofanowego', 'Przy niskim stężeniu tryptofanu geny syntezy są aktywne; nadmiar tryptofanu wiąże się z represorem (korepresor), który blokuje operator.'),
 ('Poziomy regulacji ekspresji u eukariontów', 'Struktura chromatyny (metylacja DNA, modyfikacje histonów), transkrypcja (czynniki transkrypcyjne, enhancery), obróbka RNA (alternatywny splicing), transport i trwałość mRNA (miRNA), translacja, modyfikacje i degradacja białek.'),
 ('Wyjaśnij pojęcie: czynniki transkrypcyjne', 'Białka wiążące się z sekwencjami regulatorowymi DNA i ułatwiające (lub hamujące) przyłączenie polimerazy RNA.'),
 ('Wpływ metylacji DNA na ekspresję', 'Metylacja cytozyny w promotorze zwykle wycisza gen (kondensacja chromatyny, utrudnione przyłączenie czynników transkrypcyjnych).'),
 ('Wyjaśnij pojęcie: epigenetyka', 'Dziedziczne zmiany ekspresji genów niewynikające ze zmiany sekwencji DNA (metylacja DNA, modyfikacje histonów) — np. inaktywacja chromosomu X, piętnowanie genomowe.'),
 ('Wyjaśnij pojęcie: interferencja RNA (miRNA, siRNA)', 'Krótkie RNA łączące się komplementarnie z mRNA, co prowadzi do jego degradacji lub zahamowania translacji — wyciszanie genów.'),
 ('Dlaczego komórki jednego organizmu różnią się, choć mają ten sam genom?', 'Różnią się zestawem aktywnych genów (ekspresja różnicowa), regulowanym m.in. czynnikami transkrypcyjnymi i modyfikacjami epigenetycznymi.'),
 ('Jak hormony steroidowe wpływają na ekspresję genów?', 'Wiążą się z receptorem wewnątrzkomórkowym; kompleks hormon–receptor działa jak czynnik transkrypcyjny, wiążąc się z DNA i regulując transkrypcję.'),
 ('Wyjaśnij pojęcie: inaktywacja chromosomu X (ciałko Barra)', 'U samic ssaków jeden z chromosomów X w każdej komórce somatycznej jest losowo, trwale wyciszany i skondensowany — wyrównanie dawki genów (np. umaszczenie szylkretowe kotek).'),
], Q=[
 ('Represor operonu laktozowego wiąże się z:', ['promotorem', '*operatorem', 'genem struktury', 'rybosomem'], 'Blokuje polimerazę.'),
 ('W obecności laktozy operon lac jest:', ['zablokowany', '*aktywny (indukowany)', 'usunięty', 'zmetylowany'], 'Represor odłączony.'),
 ('Metylacja DNA w promotorze zwykle:', ['zwiększa transkrypcję', '*wycisza gen', 'zmienia sekwencję DNA', 'wywołuje mutację punktową'], 'Epigenetyka.'),
 ('Ciałko Barra to:', ['jąderko', '*nieaktywny chromosom X', 'chromosom Y', 'plazmid'], 'Wyrównanie dawki genów.'),
], pp='XIII.7')
