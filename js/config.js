// IndexLab — konfiguracja kont w chmurze.
// Aby włączyć logowanie i zapis postępów na koncie, utwórz bezpłatny projekt w Supabase
// i wpisz tu jego adres oraz klucz publiczny „anon” (instrukcja w README, sekcja „Konta użytkowników”).
// Klucz „anon” jest publiczny z założenia — dostęp do danych chronią reguły RLS w bazie.
export const CLOUD = {
  url: 'https://fepprnkhuotbeyuqpqid.supabase.co',
  anonKey: 'sb_publishable_zX2SXqBqfBmfkFMVOlrm_A_YTUTm-t-', // klucz publiczny (publishable) — może być w kodzie
  table: 'postepy',
};

// Płatny dostęp (subskrypcja). Gdy wylaczone — wszystkie treści są wczytywane z plików i nic nie jest zablokowane.
// Po włączeniu treści pochodzą z tabeli „tresci” w Supabase (RLS: demo dla wszystkich, reszta z aktywnym dostępem),
// a płatności obsługują funkcje supabase/functions (Stripe). Instrukcja: README → „Płatny dostęp”.
export const PREMIUM = {
  wlaczone: true,
  // Ceny tylko do wyświetlenia — kwoty pobiera Stripe (sekrety STRIPE_PRICE_MATURA_1/2/3 i STRIPE_PRICE_MIESIAC_1/2/3).
  // Klucz = liczba przedmiotów w pakiecie.
  cennik: {
    matura: { 1: '179 zł', 2: '289 zł', 3: '369 zł' },
    miesiac: { 1: '35 zł', 2: '55 zł', 3: '69 zł' },
  },
  maturaDo: 'końca maja 2027',
  sklepKodow: '', // np. adres strony kursu na Naffy, gdzie można kupić kod dostępu
};

// Tryb prywatny (przed premierą): strona pokazuje „Wkrótce”, a aplikację widzi tylko ten, kto raz otworzy
// adres z kluczem: https://app.indexlab.pl/?klucz=TWÓJ_KLUCZ (przeglądarka zapamięta dostęp).
// Aby opublikować aplikację dla wszystkich: zmień wlaczone na false (oraz usuń „noindex” — instrukcja w docs/06).
export const PRYWATNE = {
  wlaczone: true,
  kluczSha256: '980fb41d7bfee5062b0862055bffccf56fc39d360a05fdb17c7d2782cfd0ed1c',
};
