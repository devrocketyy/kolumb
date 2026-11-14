# Dwie aplikacje IndexLab — wyjaśnienie dla laika

## W jednym zdaniu
Robimy **dwa osobne sklepy z jednym zapleczem**: uczeń widzi dwie różne aplikacje (maturalną i kursową), ale pod spodem działa ten sam silnik i to samo konto.

## Porównanie z życia: sieć restauracji
Wyobraź sobie właściciela, który ma **pizzerię i sushi-bar**:
- Klient widzi **dwa różne lokale**: inny szyld, inne menu, inny wystrój.
- Ale **kuchnia, magazyn i księgowość są wspólne**. Ten sam piec, ta sama dostawa, jedna kasa fiskalna.
- Jeśli kupisz lepszą lodówkę, korzystają z niej oba lokale naraz.
- Stały klient ma **jedną kartę lojalnościową**, honorowaną w obu.

U nas:

| W restauracji | U nas |
|---|---|
| pizzeria | **IndexLab Matura** (`app.indexlab.pl`) |
| sushi-bar | **IndexLab Kursy** (`kursy.indexlab.pl`) |
| wspólna kuchnia | wspólny kod: fiszki, powtórki, zadania, arkusze, statystyki |
| inne menu | inne treści: przedmioty maturalne vs kursy olimpijskie |
| inny szyld i wystrój | inna nazwa, ikona i kolor akcentu |
| karta lojalnościowa | **jedno konto** (ten sam e-mail) i jedna historia zakupów |
| jedna kasa | jeden Stripe |

## Co widzi uczeń

**Maturzysta** wchodzi na `app.indexlab.pl`:
- ekran „Dziś”: plan do matury, „162 dni do matury”;
- zakładki: Nauka · Matura (próbne, arkusze CKE) · Aktualności · Profil;
- czarno-biały wygląd, jak teraz.

**Olimpijczyk** wchodzi na `kursy.indexlab.pl`:
- ekran „Dziś”: „23 dni do etapu okręgowego”;
- zakładki: **Moduły** (prezentacje przewijane jak slajdy) · **Fiszki** · **Arkusze próbne** · Profil;
- ten sam styl, ale np. **granatowy** akcent i inna ikona, żeby nie dało się pomylić aplikacji na telefonie.

**Ktoś, kto kupił oba** (np. maturzysta startujący w olimpiadzie): loguje się tym samym mailem w obu aplikacjach i każda pokazuje swoje rzeczy. W profilu widzi wszystkie swoje zakupy.

## Dlaczego nie dwie zupełnie osobne aplikacje?
Bo wtedy wszystko robilibyśmy **dwa razy**:
- poprawka błędu w fiszkach → poprawiamy w dwóch miejscach;
- nowa funkcja (np. podcast, tryb ciemny) → piszemy dwa razy;
- dwa systemy logowania i dwa systemy płatności → podwójne ryzyko błędów.

Przy wspólnym zapleczu każde ulepszenie dostają **od razu obie aplikacje**.

## Dlaczego nie jedna aplikacja ze wszystkim?
Bo maturzysta nie powinien widzieć olimpiady o Afryce, a olimpijczyk planu do matury. Dwie aplikacje to:
- **prostsze menu** dla każdej grupy,
- **jaśniejszy marketing**: „aplikacja do matury” i „kursy olimpijskie” to dwa różne produkty, które łatwiej sprzedać osobno,
- **osobna ikona na telefonie**.

## Jak to wygląda technicznie (w skrócie)
- **Jedno repozytorium** z kodem.
- Przy publikacji robot buduje je **dwa razy** z innym „plikiem ustawień”: nazwa, kolor, ikona, lista treści, adres.
- Wychodzą z tego dwie strony pod dwoma adresami.
- Obie łączą się z **tą samą bazą Supabase** (konta, zakupy) i **tym samym Stripe**.

## Co z obecnym `fiszki.indexlab.pl`?
- **Do końca sezonu olimpijskiego zostaje bez zmian** — kursanci OWoPC mają tam postępy i hasło.
- Po sezonie: przenosimy fiszki do `kursy.indexlab.pl`, a stary adres przekierowuje na nowy. Obecni kursanci dostają kod, który odblokowuje kurs na ich koncie.

## Mapa adresów IndexLab (docelowo)

| Adres | Co tam jest |
|---|---|
| `indexlab.pl` | strona główna i sklep: oferta, cennik, opinie, FAQ, regulamin |
| `app.indexlab.pl` | aplikacja maturalna |
| `kursy.indexlab.pl` | aplikacja z kursami olimpijskimi |
| `fiszki.indexlab.pl` | stare fiszki OWoPC → po sezonie przekierowanie na `kursy.` |
