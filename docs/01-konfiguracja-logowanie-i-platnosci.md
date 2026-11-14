# Logowanie mailem i płatności — instrukcja krok po kroku

Ten plik prowadzi Cię przez całą konfigurację. Rób kroki po kolei i odhaczaj. Całość zajmie ok. 45–60 minut.

**Najważniejsza zasada bezpieczeństwa:** tajnych kluczy (zaczynają się od `sk_`, `whsec_`, `sb_secret_` albo są opisane jako „service role” / „secret”) **nigdy nie wklejaj na czat**. W tej instrukcji wpisujesz je sam, bezpośrednio w panelu Supabase.

Co budujemy, w jednym zdaniu: uczeń wpisuje e-mail → dostaje link → klika i jest zalogowany → kupuje dostęp przez Stripe (BLIK / karta / Przelewy24) → Stripe zawiadamia naszą bazę → aplikacja odblokowuje treści.

Trzy usługi:

| Usługa | Do czego | Koszt na start |
|---|---|---|
| **Supabase** | konta użytkowników, logowanie, baza (kto co kupił, postępy) | 0 zł (plan darmowy) |
| **Resend** | wysyłanie maili z linkiem logowania z adresu @indexlab.pl | 0 zł (plan darmowy) |
| **Stripe** | przyjmowanie płatności | tylko prowizja od transakcji |

---

## CZĘŚĆ A — Supabase (konta i baza)

### A1. Załóż projekt
1. Wejdź na **https://supabase.com** → **Start your project** → zaloguj się (najwygodniej przez GitHub, tym samym kontem co repozytorium).
2. Kliknij **New project**.
3. Wypełnij:
   - **Name:** `indexlab`
   - **Database Password:** kliknij **Generate a password** i **zapisz je w menedżerze haseł** (nie wysyłaj mi go — nie będzie potrzebne na czacie).
   - **Region:** **Central EU (Frankfurt)** — najbliżej Polski, dane zostają w UE (ważne dla RODO).
   - **Plan:** Free.
4. **Create new project**. Poczekaj 1–2 minuty, aż projekt się utworzy.

### A2. Skopiuj dwie publiczne wartości (te MOŻESZ mi wysłać)
1. W projekcie kliknij **Project Settings** (zębatka na dole lewego menu) → **API Keys** (lub **API**).
2. Skopiuj:
   - **Project URL** — wygląda jak `https://abcdefghijk.supabase.co`
   - klucz **publishable** (w starszym widoku: **anon public**) — długi ciąg znaków.

   Oba są z założenia publiczne (trafią do kodu aplikacji), więc możesz je wkleić na czat.
3. **Nie kopiuj** klucza **secret** / **service_role** — ten zostaje tylko w Supabase.

### A3. Włącz logowanie mailem
1. Lewe menu → **Authentication** → **Sign In / Providers** (albo **Providers**).
2. **Email** → upewnij się, że jest **Enabled**.
3. Zostaw włączone **Confirm email**.
4. (Opcjonalnie, polecam) **Google** → włączymy później razem — wymaga konta Google Cloud, zrobię osobną instrukcję.

### A4. Ustaw adresy aplikacji
1. **Authentication** → **URL Configuration**.
2. **Site URL:** `https://app.indexlab.pl`
3. **Redirect URLs** → **Add URL** → dodaj kolejno:
   - `https://app.indexlab.pl/**`
   - `https://devrocketyy.github.io/kolumb/**` (stary adres, na wszelki wypadek)
4. **Save**.

### A5. Polskie treści maili
1. **Authentication** → **Emails** (lub **Email Templates**).
2. Otwórz szablon **Magic Link** i wklej:
   - **Subject:** `Twój link do logowania — IndexLab`
   - **Body:**
     ```html
     <h2>Cześć!</h2>
     <p>Kliknij, aby zalogować się do IndexLab:</p>
     <p><a href="{{ .ConfirmationURL }}">Zaloguj się</a></p>
     <p>Link działa przez godzinę. Jeśli to nie Ty — po prostu zignoruj tę wiadomość.</p>
     <p>Zespół IndexLab</p>
     ```
3. To samo dla **Confirm signup**:
   - **Subject:** `Potwierdź konto — IndexLab`
   - Treść jak wyżej, ale pierwsze zdanie: „Kliknij, aby potwierdzić konto w IndexLab:”, przycisk: „Potwierdzam”.
4. **Save** przy każdym szablonie.

---

## CZĘŚĆ B — Resend (własny nadawca maili)

**Po co?** Wbudowany nadawca Supabase wysyła tylko kilka maili na godzinę i z obcego adresu — to wystarczy do testów, ale nie dla uczniów. Resend wysyła z `logowanie@indexlab.pl`, a maile nie lądują w spamie.

> Dlaczego nie skrzynka OVH? Też by zadziałała, ale skrzynki pocztowe mają limity i są robione dla ludzi, a nie dla automatów. Resend jest do tego stworzony i ma darmowy plan. Skrzynkę OVH zostaw na zwykłą korespondencję.

### B1. Konto i domena
1. Wejdź na **https://resend.com** → **Sign up** (możesz przez GitHub).
2. Lewe menu → **Domains** → **Add Domain**.
3. Wpisz `indexlab.pl`, region **EU (Ireland)** → **Add**.
4. Resend pokaże **listę rekordów DNS** (zwykle 3–4: typu **TXT** i **MX**, z nazwami w stylu `resend._domainkey` i `send`). **Zostaw tę kartę otwartą.**

### B2. Dodaj rekordy w Netlify (tam jest Twój DNS — nie w OVH!)
1. Nowa karta → **https://app.netlify.com** → lewe menu **DNS** → **indexlab.pl**.
2. Dla **każdego** rekordu z Resend: **Add new record** →
   - **Record type:** taki jak w Resend (TXT albo MX),
   - **Name:** skopiuj z Resend (np. `resend._domainkey`, `send`) — **bez** dopisywania `.indexlab.pl`,
   - **Value:** skopiuj z Resend dokładnie, w całości,
   - przy MX: **Priority** taki jak w Resend (zwykle 10).
3. **Save** przy każdym.
4. Wróć do Resend → **Verify DNS Records**. Status zmieni się na **Verified** — zwykle w kilka minut, maksymalnie kilka godzin. Nie przejmuj się, jeśli od razu nie przejdzie.

### B3. Klucz Resend → prosto do Supabase
1. W Resend: lewe menu **API Keys** → **Create API Key** → nazwa `supabase`, uprawnienie **Sending access** → **Add**. Skopiuj klucz (zaczyna się od `re_`). **Nie wysyłaj go na czat.**
2. W Supabase: **Authentication** → **Emails** → zakładka **SMTP Settings** → włącz **Enable Custom SMTP** i wpisz:
   | Pole | Wartość |
   |---|---|
   | Sender email | `logowanie@indexlab.pl` |
   | Sender name | `IndexLab` |
   | Host | `smtp.resend.com` |
   | Port | `465` |
   | Username | `resend` |
   | Password | wklej klucz `re_…` |
3. **Save**.
4. **Authentication** → **Rate Limits** → podnieś **emails sent per hour** do np. `100`.

**Test:** **Authentication** → **Users** → **Add user** → **Send magic link** na swój adres. Mail powinien przyjść od „IndexLab”. Jeśli wpadł do spamu — odczekaj, aż Resend pokaże domenę jako Verified.

---

## CZĘŚĆ C — Stripe (płatności)

Wszystko robimy **najpierw w trybie testowym** (przełącznik **Test mode** / **Sandbox** w prawym górnym rogu panelu). Prawdziwe ceny włączymy na końcu.

### C1. Dane konta
1. **https://dashboard.stripe.com** → **Settings** (zębatka) → **Business details**.
2. Typ: **Individual** (osoba prywatna — działalność nierejestrowana). Uzupełnij dane i konto bankowe do wypłat. Stripe może poprosić o zdjęcie dowodu — to normalne.
3. **Public details:** nazwa wyświetlana `IndexLab`, e-mail wsparcia `kontakt.indexlab@gmail.com`, strona `https://indexlab.pl`.

### C2. Metody płatności
1. **Settings** → **Payments** → **Payment methods**.
2. Włącz: **Cards**, **BLIK**, **Przelewy24**. (Apple Pay / Google Pay włączą się razem z kartami.)

### C3. Produkty i ceny
**Product catalog** → **Add product**. Dla każdego wiersza osobny produkt (lub jeden produkt z kilkoma cenami — jak wolisz):

| Produkt | Cena | Typ ceny |
|---|---|---|
| Matura — 1 przedmiot, miesięcznie | 29,99 PLN | Recurring, Monthly |
| Matura — 2 przedmioty, miesięcznie | 44,99 PLN | Recurring, Monthly |
| Matura — wszystkie, miesięcznie | 54,99 PLN | Recurring, Monthly |
| Matura — 1 przedmiot, do matury | 179 PLN | One-off |
| Matura — 2 przedmioty, do matury | 259 PLN | One-off |
| Matura — wszystkie, do matury | 319 PLN | One-off |

Kursy olimpijskie i ebook dodamy po decyzji o cenach (plik `03-ceny-kursow-olimpijskich.md`).

Po utworzeniu każdej ceny kliknij ją i skopiuj jej **ID** (zaczyna się od `price_…`). **ID cen nie są tajne** — wyślij mi listę na czat w formacie „Matura 1 przedmiot miesięcznie: price_…”.

### C4. Portal klienta (anulowanie subskrypcji przez ucznia)
**Settings** → **Billing** → **Customer portal** → **Activate** (w trybie testowym osobno). Zaznacz: anulowanie subskrypcji, aktualizacja metody płatności, historia faktur/potwierdzeń.

---

## CZĘŚĆ D — Połączenie Stripe ↔ Supabase

Ten krok robimy **razem**, po tym jak zrobię swoją część (wgram bazę i funkcje — opis w części E). Dam znać, kiedy.

### D1. Webhook (Stripe zawiadamia bazę o płatności)
1. Stripe → **Developers** → **Webhooks** → **Add endpoint** (lub **Add destination**).
2. **Endpoint URL:** `https://TWOJ-PROJEKT.supabase.co/functions/v1/stripe-webhook` (podmienię Ci gotowy adres).
3. **Events** — zaznacz dokładnie te:
   - `checkout.session.completed`
   - `checkout.session.async_payment_succeeded`
   - `invoice.paid`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
4. **Add endpoint**. Na stronie webhooka kliknij **Reveal** przy **Signing secret** (zaczyna się od `whsec_`).

### D2. Wpisz tajne klucze w Supabase (sam, nie na czat)
1. Stripe → **Developers** → **API keys** → **Secret key** → **Reveal** → skopiuj (`sk_test_…`).
2. Supabase → lewe menu **Edge Functions** → **Secrets** (albo **Project Settings → Edge Functions**) → **Add new secret** i dodaj:
   | Name | Value |
   |---|---|
   | `STRIPE_SECRET_KEY` | `sk_test_…` |
   | `STRIPE_WEBHOOK_SECRET` | `whsec_…` |
   | `APP_URL` | `https://app.indexlab.pl` |
3. **Save**. Napisz mi na czacie tylko: „sekrety dodane”.

---

## CZĘŚĆ E — Co robię ja (żebyś wiedział, na co czekasz)

1. Poproszę Cię o **token dostępu Supabase** przez **bezpieczny formularz**, który wyświetli się w tej rozmowie (Supabase → awatar w prawym górnym rogu → **Account preferences** → **Access Tokens** → **Generate new token**, nazwa `claude-indexlab`). Formularz zapisze go poza czatem — ja go nie widzę, tylko mogę go użyć. Po skończeniu możesz go usunąć tym samym przyciskiem.
2. Wgrywam tabele (dostępy, postępy, kody, zgłoszenia) i zabezpieczenia: każdy uczeń widzi tylko swoje dane.
3. Wgrywam funkcje `checkout`, `stripe-webhook`, `portal`, rozszerzone o nowy cennik (1 / 2 / wszystkie przedmioty, miesięcznie i do matury).
4. Wpisuję publiczny adres i klucz do aplikacji i włączam ekran logowania.
5. **Test na sucho:** kupuję dostęp kartą testową Stripe `4242 4242 4242 4242` i BLIK-iem testowym. Sprawdzam, że dostęp się nalicza, a po anulowaniu wygasa.
6. Pokazuję Ci wynik. Dopiero po Twojej akceptacji przełączamy Stripe na **tryb produkcyjny** (powtarzamy C3 i D1–D2 z kluczami `sk_live_…`).

---

## Lista kontrolna — co mi wysyłasz na czat

- [ ] Project URL Supabase (`https://….supabase.co`)
- [ ] Klucz publishable / anon public
- [ ] Lista ID cen Stripe (`price_…`) z nazwami
- [ ] „Resend: domena Verified”
- [ ] „Sekrety dodane” (po części D)

**Czego NIE wysyłasz:** hasła do bazy, klucza secret/service_role, `sk_…`, `whsec_…`, `re_…`.

## Gdy coś nie działa

| Objaw | Co sprawdzić |
|---|---|
| Mail z linkiem nie przychodzi | Spam; w Resend → **Logs** czy wysłał; czy domena jest Verified |
| Link przenosi na złą stronę | A4: Site URL i Redirect URLs |
| Płatność przeszła, a dostęp się nie włączył | Stripe → Webhooks → endpoint → zakładka zdarzeń: czerwone = błąd — zrób zrzut i wyślij mi |
| Resend nie weryfikuje domeny | czy rekordy dodałeś w **Netlify**, nie w OVH; czy nazwa nie ma dopisanego `.indexlab.pl.indexlab.pl` |
