// IndexLab — konfiguracja kont w chmurze.
// Aby włączyć logowanie i zapis postępów na koncie, utwórz bezpłatny projekt w Supabase
// i wpisz tu jego adres oraz klucz publiczny „anon” (instrukcja w README, sekcja „Konta użytkowników”).
// Klucz „anon” jest publiczny z założenia — dostęp do danych chronią reguły RLS w bazie.
export const CLOUD = {
  url: '',      // np. 'https://abcdefgh.supabase.co'
  anonKey: '',  // klucz „anon public” z ustawień projektu (Project Settings → API)
  table: 'postepy',
};
