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
  wlaczone: false,
  // Ceny tylko do wyświetlenia — kwoty pobiera Stripe (ceny STRIPE_PRICE_* w funkcjach).
  plany: [
    { id: 'miesiac', nazwa: 'Miesięcznie', cena: '39 zł', okres: 'miesięcznie', opis: 'Odnawiane co miesiąc, anulujesz w każdej chwili. Płatność kartą, Apple Pay lub Google Pay.' },
    { id: 'matura', nazwa: 'Do matury', cena: '199 zł', okres: 'jednorazowo', opis: 'Pełny dostęp do końca maja 2027 bez odnawiania. Płatność BLIK-iem, przelewem lub kartą.', polecany: true },
  ],
  sklepKodow: '', // np. adres strony kursu na Naffy, gdzie można kupić kod dostępu
};

// Tryb prywatny (przed premierą): strona pokazuje „Wkrótce”, a aplikację widzi tylko ten, kto raz otworzy
// adres z kluczem: https://app.indexlab.pl/?klucz=TWÓJ_KLUCZ (przeglądarka zapamięta dostęp).
// Aby opublikować aplikację dla wszystkich: zmień wlaczone na false (oraz usuń „noindex” — instrukcja w docs/06).
export const PRYWATNE = {
  wlaczone: true,
  kluczSha256: '980fb41d7bfee5062b0862055bffccf56fc39d360a05fdb17c7d2782cfd0ed1c',
};
