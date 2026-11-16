# Tryb prywatny (przed premierą) i jak opublikować aplikację

## Jak działa teraz
- Każdy, kto wejdzie na app.indexlab.pl, widzi tylko stronę **„Już wkrótce”**.
- Google nie indeksuje strony: jest `robots.txt` z blokadą oraz znacznik `noindex` w `index.html` i w dokumentach prawnych.
- **Ty** wchodzisz raz przez adres z kluczem:
  `https://app.indexlab.pl/?klucz=TWÓJ_KLUCZ`
  Przeglądarka zapamięta dostęp, więc potem wystarczy zwykły adres app.indexlab.pl. Na każdym nowym urządzeniu, w nowej przeglądarce lub oknie incognito otwórz link z kluczem jeszcze raz.
- Klucza nie ma w repozytorium. Jest tam tylko jego skrót (SHA-256), z którego nie da się go odtworzyć.

To blokada „dla ludzi”, nie sejf. Ktoś, kto zna budowę strony, mógłby podejrzeć pliki z treścią. Przed premierą to wystarczy, bo nikt nie zna adresu, a Google go nie pokaże.

## Jak opublikować dla wszystkich (3 zmiany, ok. 2 minuty)
Wszystko zrobisz na github.com w przeglądarce: otwórz plik → ikonka ołówka (Edit) → zmień → **Commit changes**.

1. `js/config.js`: w sekcji `PRYWATNE` zmień `wlaczone: true` na **`wlaczone: false`**.
2. `index.html`: usuń całą linijkę
   `<meta name="robots" content="noindex, nofollow">`
3. `robots.txt`: zamień treść na
   ```
   User-agent: *
   Allow: /
   ```
   (W `prawne/regulamin.html` i `prawne/prywatnosc.html` też możesz usunąć linijkę z `noindex`, jeśli chcesz, żeby regulamin był w Google — nie jest to konieczne.)

Po ok. 1–2 minutach (wdrożenie GitHub Pages) aplikacja jest publiczna. Żeby znów ją ukryć, zrób odwrotnie.

Możesz też po prostu napisać do mnie „publikujemy” — zrobię to za Ciebie.
