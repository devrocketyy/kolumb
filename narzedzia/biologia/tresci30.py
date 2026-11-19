# Treści kursu biologii — porcja 30: duża partia fiszek i pytań ABCD (nacisk na typowe pułapki maturalne).
T = {}

T['b-czasowniki'] = dict(F=[
 ('Typowy błąd: odpowiedź bez odniesienia do danych', 'Gdy polecenie mówi „na podstawie wyników/wykresu”, odpowiedź musi przywołać konkretne dane (np. wartości, kierunek zmian) — sama wiedza z podręcznika nie wystarcza.'),
 ('Typowy błąd: wniosek zamiast obserwacji', 'Obserwacja opisuje to, co widać („pęcherzyków było więcej”), wniosek wyjaśnia zależność („światło zwiększa intensywność fotosyntezy”).'),
 ('Typowy błąd: antropomorfizacja', 'Nie pisz, że organizm „chce” lub „stara się” — opisz mechanizm (np. „dobór faworyzował osobniki…”).'),
])

T['b-metodologia'] = dict(F=[
 ('Problem badawczy — wzór', '„Czy/Jak [zmienna niezależna] wpływa na [zmienną zależną] u [obiekt badań]?”'),
 ('Hipoteza — wzór', '„[Zmienna niezależna] zwiększa/zmniejsza [zmienną zależną] u [obiektu badań].”'),
 ('Wniosek — wzór', 'Odpowiada na problem badawczy i opiera się na wynikach — potwierdza lub obala hipotezę.'),
], Q=[
 ('Prawidłowo sformułowany problem badawczy to:', ['Światło o dużym natężeniu przyspiesza fotosyntezę moczarki.', '*Jak natężenie światła wpływa na intensywność fotosyntezy moczarki?', 'Moczarka wydziela w świetle pęcherzyki tlenu do wody.', 'Fotosynteza moczarki zachodzi w chloroplastach liści.'], 'Forma pytania z obiema zmiennymi.'),
 ('Wniosek z doświadczenia powinien:', ['powtarzać opis metody', '*odnosić się do problemu badawczego i wyników', 'zawierać nową hipotezę', 'opisywać tylko próbę kontrolną'], 'Odpowiedź na problem.'),
])

T['b-bialka'] = dict(Q=[
 ('Za swoistość działania enzymu odpowiada przede wszystkim struktura:', ['wyłącznie I-rzędowa łańcucha', '*przestrzenna (III-rzędowa) centrum aktywnego', 'II-rzędowa w postaci β-harmonijki', 'zawsze IV-rzędowa kilku podjednostek'], 'Kształt centrum.'),
 ('Białka transportowane do błony powstają na rybosomach:', ['mitochondrialnych', '*związanych z siateczką szorstką', 'wolnych w cytozolu', 'jąderka'], 'ER szorstkie.'),
])

T['b-blony'] = dict(F=[
 ('Typowy błąd: osmoza a dyfuzja', 'Osmoza to przepływ wody przez błonę półprzepuszczalną z roztworu o niższym do wyższego stężenia substancji rozpuszczonych; dyfuzja dotyczy przemieszczania substancji.'),
 ('Roztwór hipotoniczny, izotoniczny, hipertoniczny', 'Względem komórki: hipotoniczny — mniej substancji rozpuszczonych (woda napływa), izotoniczny — równe stężenia, hipertoniczny — więcej (woda wypływa).'),
], Q=[
 ('Woda w osmozie przemieszcza się do roztworu o:', ['niższym stężeniu substancji rozpuszczonych', '*wyższym stężeniu substancji rozpuszczonych', 'tym samym stężeniu', 'wyższym potencjale wody'], 'Niższy potencjał wody.'),
])

T['b-oddychanie'] = dict(F=[
 ('Typowy błąd: rośliny nie oddychają', 'Rośliny oddychają przez całą dobę — w dzień fotosynteza zwykle przewyższa oddychanie, w nocy zachodzi tylko oddychanie.'),
 ('Oddychanie beztlenowe a fermentacja', 'Niektóre bakterie oddychają beztlenowo — końcowym akceptorem elektronów jest np. azotan lub siarczan (nie tlen); fermentacja nie wykorzystuje łańcucha oddechowego.'),
], Q=[
 ('Rośliny zielone oddychają:', ['tylko w nocy', 'tylko w dzień', '*przez całą dobę', 'tylko korzeniami'], 'Pułapka maturalna.'),
])

T['b-fotosynteza'] = dict(F=[
 ('Typowy błąd: tlen z CO₂', 'Tlen wydzielany w fotosyntezie pochodzi z wody (doświadczenia z izotopem ¹⁸O), a nie z dwutlenku węgla.'),
 ('Faza niezależna od światła — czy zachodzi w nocy?', 'Bezpośrednio nie wymaga światła, ale potrzebuje ATP i NADPH z fazy jasnej — w praktyce zachodzi głównie w dzień.'),
], Q=[
 ('Cykl Calvina w ciemności szybko ustaje, ponieważ:', ['RuBisCO ulega denaturacji', '*brakuje ATP i NADPH z fazy jasnej', 'brakuje CO₂', 'chloroplasty zanikają'], 'Zależność od fazy jasnej.'),
])

T['b-mitoza-mejoza'] = dict(F=[
 ('Typowy błąd: chromosom a chromatyda', 'Po replikacji chromosom składa się z dwóch chromatyd, ale nadal jest jednym chromosomem; liczbę chromosomów liczy się po centromerach.'),
 ('Typowy błąd: mejoza II zmniejsza ploidalność', 'Ploidalność zmniejsza się w mejozie I; mejoza II zmniejsza tylko ilość DNA (2c → 1c).'),
], Q=[
 ('Liczbę chromosomów w komórce wyznacza liczba:', ['chromatyd', '*centromerów', 'cząsteczek DNA', 'telomerów'], 'Jeden centromer — jeden chromosom.'),
])

T['b-replikacja'] = dict(F=[
 ('Typowy błąd: replikacja a transkrypcja', 'Replikacja kopiuje całe DNA (obie nici, w fazie S) przed podziałem; transkrypcja przepisuje fragment jednej nici na RNA, przez cały cykl.'),
])

T['b-translacja'] = dict(F=[
 ('Typowy błąd: kodon w DNA', 'Kodon to trójka nukleotydów w mRNA; w DNA mówi się o trójkach kodujących (tripletach) — przy zadaniach z kodem trzeba najpierw zapisać mRNA.'),
], Q=[
 ('Tabela kodu genetycznego dotyczy sekwencji:', ['nici matrycowej DNA', '*mRNA', 'tRNA', 'rRNA'], 'Kodony mRNA.'),
])

T['b-krzyzowki'] = dict(F=[
 ('Typowy błąd: „wśród synów” a „wśród dzieci”', 'Przy cechach sprzężonych z X zawsze sprawdź, czy pytanie dotyczy wszystkich dzieci, czy tylko synów/córek — wyniki różnią się dwukrotnie.'),
 ('Typowy błąd: genotyp a fenotyp', 'Genotyp zapisuje się symbolami alleli (Aa), fenotyp — słowami (np. kwiaty czerwone).'),
])

T['b-plec'] = dict(Q=[
 ('Prawdopodobieństwo urodzenia chłopca w każdej ciąży wynosi około:', ['25%', '*50%', '75%', 'zależy od poprzednich dzieci'], 'Zdarzenia niezależne.'),
])

T['b-mutacje'] = dict(F=[
 ('Typowy błąd: mutacja zawsze szkodliwa', 'Mutacje mogą być szkodliwe, obojętne lub korzystne — te ostatnie są surowcem ewolucji.'),
])

T['b-dobor'] = dict(F=[
 ('Typowy błąd: dobór tworzy cechy', 'Dobór naturalny nie tworzy nowych cech — selekcjonuje warianty powstałe wcześniej w wyniku mutacji i rekombinacji.'),
 ('Typowy błąd: osobnik ewoluuje', 'Ewolucji podlegają populacje (zmiana częstości alleli), a nie pojedyncze osobniki.'),
], Q=[
 ('Ewolucji w sensie biologicznym podlega:', ['pojedynczy osobnik', '*populacja', 'pojedyncza komórka', 'narząd'], 'Zmiana puli genowej.'),
 ('Źródłem nowych alleli w populacji są:', ['dobór naturalny', '*mutacje', 'dryf genetyczny', 'izolacja geograficzna'], 'Dobór tylko selekcjonuje.'),
])

T['b-ekosystem'] = dict(F=[
 ('Typowy błąd: obieg energii', 'Energia przepływa przez ekosystem jednokierunkowo (i jest rozpraszana jako ciepło); krążą tylko pierwiastki (materia).'),
 ('Typowy błąd: destruenci to tylko grzyby', 'Destruentami są głównie bakterie i grzyby; zwierzęta jak dżdżownice to detrytusożercy.'),
], Q=[
 ('W ekosystemie krąży:', ['energia', '*materia (pierwiastki)', 'energia i materia jednakowo', 'wyłącznie woda'], 'Energia płynie jednokierunkowo.'),
])

T['b-populacje'] = dict(F=[
 ('Typowy błąd: pasożyt zabija żywiciela', 'Pasożyt zwykle nie zabija żywiciela szybko (zależy od niego); żywiciela zabija parazytoid lub drapieżnik.'),
], Q=[
 ('Organizm, którego larwy rozwijają się w żywicielu i go zabijają, to:', ['pasożyt zewnętrzny', '*parazytoid', 'komensal', 'saprotrof'], 'Np. gąsieniczniki.'),
])

T['b-nisza'] = dict(Q=[
 ('Tolerancja ekologiczna to:', ['liczba osobników w danej populacji', '*zakres wartości czynnika, w którym organizm może żyć', 'rodzaj pokarmu preferowanego przez gatunek', 'obszar terytorium bronionego przez osobnika'], 'Shelford.'),
])

T['b-hormony'] = dict(F=[
 ('Typowy błąd: insulina rozkłada glukozę', 'Insulina nie rozkłada glukozy — umożliwia jej pobieranie przez komórki i magazynowanie (glikogen, tłuszcze).'),
 ('Typowy błąd: glukagon a glikogen', 'Glukagon to hormon trzustki; glikogen to polisacharyd zapasowy — glukagon pobudza rozkład glikogenu.'),
], Q=[
 ('Insulina obniża stężenie glukozy we krwi, ponieważ:', ['rozkłada glukozę bezpośrednio w osoczu krwi', '*zwiększa jej pobieranie przez komórki i syntezę glikogenu', 'zwiększa wydalanie glukozy z moczem przez nerki', 'hamuje trawienie skrobi w jelicie cienkim'], 'Pułapka maturalna.'),
])

T['b-odpornosc'] = dict(F=[
 ('Typowy błąd: antybiotyk a szczepionka', 'Antybiotyk leczy zakażenie bakteryjne (zabija lub hamuje bakterie); szczepionka zapobiega chorobie (wywołuje odporność).'),
 ('Typowy błąd: przeciwciała niszczą wirusy w komórce', 'Przeciwciała działają w płynach ustrojowych; komórki zakażone wirusem niszczą limfocyty Tc i komórki NK.'),
], Q=[
 ('Szczepionka:', ['leczy rozwiniętą chorobę bakteryjną', '*zapobiega chorobie przez wytworzenie odporności', 'zawiera antybiotyk niszczący bakterie', 'daje pełną ochronę natychmiast po podaniu'], 'Profilaktyka.'),
])

T['b-krazenie'] = dict(F=[
 ('Typowy błąd: tętnice zawsze z krwią natlenowaną', 'Tętnica płucna prowadzi krew odtlenowaną, a żyła płucna — natlenowaną; nazwa zależy od kierunku przepływu względem serca.'),
], Q=[
 ('Krew odtlenowaną prowadzi:', ['aorta', 'żyła płucna', '*pień płucny', 'tętnica wieńcowa'], 'Do płuc.'),
])

T['b-oddychanie-czl'] = dict(F=[
 ('Typowy błąd: oddychanie a wymiana gazowa', 'Oddychanie komórkowe to utlenianie związków organicznych w komórkach; wymiana gazowa to dyfuzja O₂ i CO₂ w płucach i tkankach.'),
])

T['b-nerwy'] = dict(F=[
 ('Typowy błąd: impuls przez synapsę w obie strony', 'W synapsie chemicznej impuls jest przekazywany tylko w jednym kierunku — z kolbki presynaptycznej na błonę postsynaptyczną.'),
], Q=[
 ('Jednokierunkowość przekazywania w synapsie chemicznej wynika z:', ['obecności osłonki mielinowej na aksonie', '*rozmieszczenia pęcherzyków i receptorów po przeciwnych stronach', 'różnicy temperatur po obu stronach szczeliny', 'działania pompy sodowo-potasowej w kolbce'], 'Budowa synapsy.'),
])

T['b-rozmnazanie'] = dict(F=[
 ('Typowy błąd: plemnik decyduje o płci a komórka jajowa', 'Płeć dziecka zależy od plemnika (X lub Y) — komórka jajowa zawsze ma chromosom X.'),
])

T['b-rozmnazanie-roslin'] = dict(F=[
 ('Typowy błąd: zapylenie a zapłodnienie', 'Zapylenie to przeniesienie pyłku na znamię; zapłodnienie — połączenie gamet w zalążku (po wzroście łagiewki).'),
], Q=[
 ('Przeniesienie pyłku na znamię słupka to:', ['zapłodnienie', '*zapylenie', 'kiełkowanie', 'apomiksja'], 'Pułapka pojęciowa.'),
])

T['b-gospodarka-wodna'] = dict(Q=[
 ('Woda z gleby do włośnika przemieszcza się, ponieważ potencjał wody we włośniku jest:', ['wyższy niż w glebie', '*niższy niż w glebie', 'równy potencjałowi gleby', 'zawsze dodatni'], 'Od wyższego do niższego ψ.'),
])

T['b-wirusy'] = dict(F=[
 ('Typowy błąd: wirusy jako bakterie', 'Wirusy nie są komórkami, nie mają rybosomów ani metabolizmu; są znacznie mniejsze od bakterii.'),
])

T['b-bakterie'] = dict(F=[
 ('Typowy błąd: wszystkie bakterie chorobotwórcze', 'Większość bakterii jest nieszkodliwa lub pożyteczna (destruenci, wiązanie azotu, mikrobiom); chorobotwórcze stanowią niewielką część.'),
])

T['b-techniki'] = dict(F=[
 ('Typowy błąd: PCR a sekwencjonowanie', 'PCR powiela fragment DNA (bez ustalania sekwencji); sekwencjonowanie ustala kolejność nukleotydów.'),
], Q=[
 ('Do ustalenia kolejności nukleotydów w genie służy:', ['PCR', 'elektroforeza', '*sekwencjonowanie', 'hybrydyzacja z sondą'], 'Metoda Sangera.'),
])

T['b-gmo'] = dict(F=[
 ('Typowy błąd: klon a GMO', 'Klon to organizm genetycznie identyczny z innym (bez zmiany genów); GMO ma zmieniony materiał genetyczny.'),
], Q=[
 ('Owca Dolly była:', ['organizmem transgenicznym', '*klonem', 'mieszańcem międzygatunkowym', 'organizmem poliploidalnym'], 'Transfer jądra.'),
])
