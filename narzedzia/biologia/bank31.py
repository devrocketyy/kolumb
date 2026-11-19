# Bank zadań autorskich — biologia, część 31: duża partia (wszystkie działy).
BANK = {
'biochemia': [
 B('Mioglobina u ssaków nurkujących',
   'Dane (autorskie). Zawartość mioglobiny w mięśniach (mg/g): człowiek — 6; foka — 45; kaszalot — 70.',
   T('wyjasnij', 2, 'Wyjaśnij znaczenie dużej zawartości mioglobiny dla ssaków nurkujących.', 'Mioglobina magazynuje tlen w mięśniach — podczas długiego nurkowania (bez oddychania) mięśnie korzystają z zapasu tlenu i mogą dłużej pracować tlenowo.', '')),
],
'komorka': [
 B('Ruch cytoplazmy w moczarce',
   'Doświadczenie (autorskie). W komórkach liścia moczarki obserwowano ruch chloroplastów wzdłuż ścian. Po podaniu substancji niszczącej filamenty aktynowe ruch ustał.',
   T('podaj', 1, 'Sformułuj wniosek.', 'Ruch cytoplazmy (cyklosa) zależy od filamentów aktynowych cytoszkieletu.', ''),
   T('podaj', 1, 'Podaj, jakiego związku wymaga ten ruch jako źródła energii.', 'ATP.', '')),
],
'metabolizm': [
 B('Cyjanek i oddychanie',
   'Doświadczenie (autorskie). Do zawiesiny mitochondriów z substratem dodano cyjanek. Pobieranie tlenu ustało, a stężenie ATP gwałtownie spadło.',
   T('wyjasnij', 2, 'Wyjaśnij, dlaczego zatrzymanie łańcucha oddechowego zatrzymuje syntezę ATP.', 'Bez przepływu elektronów przez łańcuch oddechowy nie są pompowane protony do przestrzeni międzybłonowej — zanika gradient protonów, który napędza syntazę ATP.', ''),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego komórki mózgu są najbardziej wrażliwe na cyjanek.', 'Neurony mają duże zapotrzebowanie na ATP i prawie wyłącznie korzystają z oddychania tlenowego (słaba zdolność do fermentacji).', '')),
],
'podzialy': [
 B('Źródła zmienności',
   'Opis (autorski). Rodzeństwo (poza bliźniętami jednojajowymi) różni się genetycznie, choć ma tych samych rodziców.',
   T('podaj', 2, 'Wymień trzy procesy odpowiedzialne za zróżnicowanie genetyczne rodzeństwa i podaj, kiedy zachodzą.', 'Crossing-over (profaza I mejozy), niezależna segregacja chromosomów homologicznych (anafaza I), losowe łączenie się gamet (zapłodnienie).', '')),
],
'genetyka-molekularna': [
 B('Antybiotyki a etapy ekspresji genów',
   'Tabela (autorska). Antybiotyk A hamuje polimerazę RNA bakterii; B — wiąże się z małą podjednostką rybosomu 70S; C — hamuje bakteryjną gyrazę (topoizomerazę niezbędną do replikacji).',
   T('podaj', 1, 'Przyporządkuj antybiotyki do procesów, które hamują.', 'A — transkrypcja; B — translacja; C — replikacja DNA.', ''),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego antybiotyk B jest mało szkodliwy dla komórek człowieka.', 'Komórki człowieka mają w cytoplazmie rybosomy 80S, do których antybiotyk się nie wiąże.', '')),
],
'genetyka': [
 B('Grupy krwi i Rh w rodzinie',
   'Opis (autorski). Matka ma grupę A Rh⁻, ojciec — B Rh⁺; ich pierwsze dziecko ma grupę 0 Rh⁻.',
   T('podaj', 1, 'Zapisz genotypy rodziców.', 'Matka Iᴬi dd; ojciec Iᴮi Dd.', ''),
   T('podaj', 1, 'Oblicz prawdopodobieństwo, że kolejne dziecko będzie miało grupę AB Rh⁺.', '1/4 × 1/2 = 1/8.', '')),
],
'biotechnologia': [
 B('Test ELISA',
   'Opis (autorski). W teście na obecność przeciwciał przeciw wirusowi płytkę pokrytą antygenem wirusa inkubuje się z surowicą pacjenta, płucze, a następnie dodaje przeciwciało wtórne z enzymem. Zmiana barwy świadczy o wyniku dodatnim.',
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego zmiana barwy świadczy o obecności przeciwciał pacjenta.', 'Przeciwciała pacjenta związały antygen na płytce, a przeciwciało wtórne z enzymem związało się z nimi — enzym przekształca substrat w barwny produkt.', ''),
   T('podaj', 1, 'Podaj, o czym świadczy dodatni wynik tego testu.', 'O kontakcie z wirusem (zakażeniu obecnym lub przebytym) lub szczepieniu — organizm wytworzył przeciwciała.', '')),
],
'mikroorganizmy': [
 B('Toksoplazmoza',
   'Opis (autorski). Myszy zarażone toksoplazmą tracą lęk przed zapachem kota.',
   T('wyjasnij', 2, 'Wyjaśnij, jakie znaczenie dla pasożyta ma zmiana zachowania myszy.', 'Mysz bez lęku łatwiej pada ofiarą kota — pasożyt trafia do żywiciela ostatecznego, w którym rozmnaża się płciowo, co zamyka jego cykl rozwojowy.', '')),
],
'rosliny': [
 B('Zasolenie gleby',
   'Doświadczenie (autorskie). Siewki pszenicy podlewano roztworami NaCl: 0, 50 i 150 mmol/l. Po 2 tygodniach masa siewek wynosiła 100%, 70% i 25% masy kontroli; przy 150 mmol/l liście więdły.',
   T('wyjasnij', 1, 'Wyjaśnij więdnięcie liści przy najwyższym stężeniu soli.', 'Wysokie stężenie soli obniżyło potencjał wody w glebie — korzenie nie mogły pobierać wody (susza fizjologiczna).', ''),
   T('podaj', 1, 'Sformułuj wniosek z doświadczenia.', 'Im wyższe zasolenie gleby, tym słabszy wzrost siewek pszenicy.', '')),
],
'zwierzeta': [
 B('Rozwój żaby',
   'Opis (autorski). Kijanki hodowane w wodzie z dodatkiem tyroksyny przeobraziły się wcześniej niż kontrolne; kijanki z usuniętą tarczycą nie przeobraziły się wcale.',
   T('podaj', 1, 'Sformułuj wniosek.', 'Hormon tarczycy (tyroksyna) jest niezbędny do przeobrażenia kijanki w żabę i je przyspiesza.', ''),
   T('podaj', 1, 'Podaj dwie zmiany zachodzące podczas przeobrażenia kijanki.', 'Np. rozwój kończyn, zanik ogona, zastąpienie skrzeli płucami, zmiana układu pokarmowego (z roślinożernego na mięsożerny).', '')),
],
'fizjologia': [
 B('Leptyna',
   'Doświadczenie (autorskie). Myszy z mutacją uniemożliwiającą wytwarzanie leptyny jadły bardzo dużo i stawały się otyłe. Po podawaniu leptyny ich apetyt i masa ciała zmalały.',
   T('podaj', 1, 'Podaj funkcję leptyny.', 'Hamuje apetyt — informuje mózg (podwzgórze) o zapasach tkanki tłuszczowej.', ''),
   T('wyjasnij', 1, 'Wyjaśnij, dlaczego podawanie leptyny nie pomaga większości otyłych ludzi.', 'Większość otyłych ludzi ma wysoki poziom leptyny, ale ich organizm jest na nią mniej wrażliwy (oporność) — problemem nie jest brak hormonu.', '')),
 B('Odruch warunkowy',
   'Opis (autorski). Uczeń zawsze przed jedzeniem słyszy dźwięk mikrofalówki. Po kilku tygodniach sam dźwięk mikrofalówki wywołuje u niego wydzielanie śliny.',
   T('podaj', 1, 'Określ rodzaj odruchu. Uzasadnij.', 'Warunkowy — powstał w wyniku wielokrotnego skojarzenia bodźca obojętnego (dźwięk) z bezwarunkowym (pokarm).', ''),
   T('podaj', 1, 'Przewidź, co się stanie, jeśli dźwięk przestanie poprzedzać jedzenie.', 'Odruch będzie stopniowo wygasał (wygaszanie odruchu warunkowego).', '')),
],
'ewolucja-ekologia': [
 B('Starzenie się społeczeństwa',
   'Opis (autorski). W Polsce od lat spada liczba urodzeń, a średnia długość życia rośnie.',
   T('podaj', 1, 'Opisz, jak zmienia się kształt piramidy wieku populacji Polski.', 'Zwęża się u podstawy (mniej dzieci), a poszerza w górnej części (więcej osób starszych) — populacja regresywna/starzejąca się.', ''),
   T('podaj', 1, 'Podaj jeden skutek tej zmiany dla społeczeństwa.', 'Np. mniej osób w wieku produkcyjnym / większe wydatki na opiekę zdrowotną i emerytury.', '')),
 B('Owady zapylające',
   'Dane (autorskie). Plon jabłek w sadzie: z ulami pszczół i pasem kwietnym — 100%; bez uli, z pasem kwietnym — 75%; bez uli i bez pasa (opryski) — 40%.',
   T('wyjasnij', 2, 'Wyjaśnij różnice plonów.', 'Pszczoły z uli i dzikie zapylacze (wspierane przez pas kwietny) zapylają kwiaty jabłoni — więcej zapylonych kwiatów to więcej owoców; opryski i brak pożytku ograniczają liczbę zapylaczy.', '')),
]}
