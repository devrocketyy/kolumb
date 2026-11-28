-- IndexLab — „bez płacenia dwa razy”: zapamiętany wynik oceny AI dla identycznej odpowiedzi na to samo zadanie.
-- Uruchom w Supabase: SQL Editor → wklej całość → Run (po migracjach 008 i 009). Można uruchomić ponownie.
-- skrot  = SHA-256 z (wersja instrukcji, model, zadanie, polecenie, materiał, klucz, zasady, punkty, znormalizowana odpowiedź),
-- wynik  = { uzasadnienie, brakuje[], wskazowka } — punkty są w kolumnie pkt.
alter table public.ocena_ai add column if not exists skrot text;
alter table public.ocena_ai add column if not exists wynik jsonb;
create index if not exists ocena_ai_skrot on public.ocena_ai (skrot) where skrot is not null;
