# Źródło części biologicznej zbioru testowego (generuje wiersze do zbior.jsonl).
# Odpowiedzi testowe są AUTORSKIE (IndexLab), oceny wzorcowe wg klucza i zasad z aplikacji.
# Rodzaje odpowiedzi: pelna, czesciowa, bledna, inne_slowa, popr_plus_blad, ogolnik.
# przeglad=True → niejasny przypadek do przejrzenia przez właściciela.
P = 'biologia'
Z = [
 # (ref, typ, czesc, [(rodzaj, odpowiedz, wzor_pkt, [brakuje], przeglad)])
 ('2023-maj/1.3', 'wykaz', 'robocza', [
  ('pelna', 'Dehydrogenaza pirogronianowa zamienia pirogronian powstały w glikolizie w acetylo-CoA, a acetylo-CoA wchodzi do cyklu Krebsa.', 1, [], False),
  ('ogolnik', 'Bo łączy te dwa procesy i dzięki niej oddychanie działa dalej.', 0, ['przekształcenie pirogronianu w acetylo-CoA', 'acetylo-CoA jako substrat cyklu Krebsa'], False),
  ('popr_plus_blad', 'Przekształca pirogronian w acetylo-CoA w cytozolu, który potem trafia do cyklu Krebsa w jądrze komórkowym.', 0, ['błędna lokalizacja cyklu Krebsa (macierz mitochondrium)'], False),
 ]),
 ('2023-maj/3.2', 'wykaz', 'kontrolna', [
  ('pelna', 'Przy zapłodnieniu liczba chromosomów się podwaja, więc bez mejozy, która ją zmniejsza o połowę, w każdym pokoleniu byłoby ich coraz więcej.', 1, [], False),
  ('inne_slowa', 'Mejoza daje gamety haploidalne, więc po połączeniu dwóch gamet zygota ma znów 2n — stała liczba chromosomów w kolejnych pokoleniach.', 1, [], False),
  ('czesciowa', 'Mejoza zmniejsza liczbę chromosomów o połowę.', 0, ['powiązanie z zapłodnieniem / utrzymanie stałej liczby chromosomów w pokoleniach'], False),
 ]),
 ('2023-maj/4.2', 'okresl', 'robocza', [
  ('pelna', 'Żeby na początku drugiego etapu wszystkie rośliny były takie same i żeby różnice wynikały tylko z oświetlenia, a nie z innych czynników.', 1, [], False),
  ('bledna', 'Żeby rośliny szybciej rosły.', 0, ['wyrównanie materiału / wykluczenie wpływu innych czynników'], False),
 ]),
 ('2023-maj/5.1', 'podaj', 'robocza', [
  ('pelna', 'A – karboksylacja, B – redukcja, C – regeneracja RuBP.', 2, [], False),
  ('czesciowa', 'A – karboksylacja, B – redukcja, C – fosforylacja.', 1, ['C – regeneracja RuBP'], False),
  ('bledna', 'A – glikoliza, B – fotoliza wody, C – regeneracja.', 0, ['A – karboksylacja', 'B – redukcja'], False),
 ]),
 ('2024-maj/2', 'okresl', 'robocza', [
  ('pelna', 'Polimeraza syntetyzuje nić DNA na matrycy RNA wirusa, a rybonukleaza rozkłada RNA z hybrydy RNA–DNA, żeby można było dobudować drugą nić DNA.', 2, [], False),
  ('czesciowa', 'Polimeraza tworzy DNA na podstawie RNA wirusa.', 1, ['funkcja rybonukleazy (rozkład RNA z hybrydy)'], False),
  ('popr_plus_blad', 'Polimeraza syntetyzuje DNA na matrycy RNA, a rybonukleaza syntetyzuje nowe RNA wirusa.', 1, ['rybonukleaza rozkłada RNA, a nie syntetyzuje'], False),
  ('bledna', 'Polimeraza rozkłada DNA gospodarza, a rybonukleaza łączy RNA z DNA.', 0, ['funkcja polimerazy', 'funkcja rybonukleazy'], False),
 ]),
 ('2024-maj/12.1', 'wyjasnij', 'kontrolna', [
  ('pelna', 'Wirus niszczy mikrokosmki, więc brakuje enzymów rozkładających dwucukry; niestrawione dwucukry zostają w jelicie i osmotycznie zatrzymują wodę. Dodatkowo zakażone komórki wydzielają jony chlorkowe, a za nimi woda osmotycznie przechodzi do światła jelita.', 2, [], False),
  ('czesciowa', 'Niestrawione disacharydy zostają w świetle jelita i przyciągają wodę osmotycznie, więc jest biegunka.', 1, ['wydzielanie Cl⁻ i osmotyczny wypływ wody do światła jelita'], False),
  ('ogolnik', 'Wirus uszkadza jelito i woda ucieka z organizmu, dlatego jest odwodnienie.', 0, ['zatrzymywanie wody przez niestrawione disacharydy', 'wydzielanie Cl⁻'], False),
 ]),
 ('2024-maj/17.2', 'okresl', 'robocza', [
  ('pelna', 'Ramię akceptorowe przyłącza aminokwas, a antykodon łączy się komplementarnie z kodonem na mRNA, dzięki czemu wstawiany jest właściwy aminokwas.', 2, [], False),
  ('czesciowa', 'Ramię akceptorowe przyłącza aminokwas.', 1, ['funkcja antykodonu'], False),
  ('bledna', 'Ramię akceptorowe transportuje tRNA do jądra, a antykodon tnie mRNA.', 0, ['funkcja ramienia akceptorowego', 'funkcja antykodonu'], False),
  ('inne_slowa', 'Do końca 3′ (CCA) doczepia się aminokwas; trójka nukleotydów antykodonu paruje się z kodonem mRNA na rybosomie.', 2, [], False),
 ]),
 ('2025-maj/1.2', 'uzasadnij', 'robocza', [
  ('pelna', 'III-rzędową, bo rybonukleaza ma tylko jeden łańcuch polipeptydowy.', 1, [], False),
  ('bledna', 'IV-rzędową, bo mostki łączą różne białka.', 0, ['struktura III-rzędowa – jeden łańcuch'], False),
  ('czesciowa', 'III-rzędową.', 0, ['uzasadnienie (jeden łańcuch polipeptydowy)'], False),
 ]),
 ('2025-maj/2.2', 'podaj', 'kontrolna', [
  ('pelna', 'Wszystkie są otoczone dwiema błonami.', 1, [], False),
  ('inne_slowa', 'Mają własny kolisty DNA.', 1, [], False),
  ('bledna', 'Wszystkie zawierają chlorofil.', 0, ['cecha wspólna: dwie błony / własne DNA / rybosomy 70S'], False),
 ]),
 ('2025-maj/3.2', 'podaj', 'robocza', [
  ('pelna', 'Strefa wydłużania.', 1, [], False),
  ('inne_slowa', 'Strefa wzrostu komórek na długość.', 1, [], False),
  ('bledna', 'Stożek wzrostu (merystem wierzchołkowy).', 0, ['strefa wydłużania'], False),
 ]),
 ('2024-czerwiec/19.1', 'oblicz', 'robocza', [
  ('pelna', 'p = 1 − 0,3 = 0,7; 2pq = 2 · 0,7 · 0,3 = 0,42.', 1, [], False),
  ('bledna', '2pq = 2 · 0,3 · 0,3 = 0,18.', 0, ['p = 0,7; 2pq = 0,42'], False),
  ('inne_slowa', 'Heterozygoty to 0,42.', 1, [], True),
 ]),
 ('2024-czerwiec/14.2', 'wyjasnij', 'kontrolna', [
  ('pelna', 'Amoniak jest silnie toksyczny i trzeba go rozcieńczać dużą ilością wody – zwierzęta wodne mają jej dużo. Lądowe muszą oszczędzać wodę, więc przekształcają amoniak w mniej toksyczny mocznik lub kwas moczowy.', 1, [], False),
  ('czesciowa', 'Bo amoniak jest bardzo toksyczny.', 0, ['powiązanie z dostępnością wody / oszczędzaniem wody na lądzie'], False),
 ]),
 ('2025-czerwiec/14.1', 'wyjasnij', 'robocza', [
  ('pelna', 'HIV niszczy limfocyty T pomocnicze, więc odporność komórkowa słabnie i nie utrzymuje uśpionych prątków w ryzach – zaczynają się namnażać.', 1, [], False),
  ('popr_plus_blad', 'HIV niszczy limfocyty B, więc organizm nie wytwarza przeciwciał i prątki się namnażają.', 0, ['HIV niszczy limfocyty T pomocnicze (CD4)'], False),
  ('ogolnik', 'Bo chorzy na AIDS mają słabą odporność.', 0, ['zniszczenie limfocytów T pomocniczych'], False),
 ]),
 ('2026-maj/15.2', 'wyjasnij', 'kontrolna', [
  ('pelna', 'Genom HCV to RNA, a PCR powiela tylko DNA, więc najpierw odwrotna transkryptaza robi cDNA na matrycy RNA.', 1, [], False),
  ('bledna', 'Bo odwrotna transkryptaza namnaża RNA wirusa.', 0, ['RNA jako materiał genetyczny HCV, synteza cDNA do PCR'], False),
 ]),
]
