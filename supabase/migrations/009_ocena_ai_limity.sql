-- IndexLab — limity ocen AI zależne od planu: oznaczenie ocen z darmowej puli i zapis użytego modelu.
-- Uruchom w Supabase: SQL Editor → wklej całość → Run (po migracji 008). Można uruchomić ponownie.
alter table public.ocena_ai add column if not exists darmowa boolean not null default false;
alter table public.ocena_ai add column if not exists model text;
create index if not exists ocena_ai_user_darmowa on public.ocena_ai (user_id, darmowa);
-- Sesja próbnej matury AI (null = zwykła ocena zadania) — do miesięcznego limitu matur.
alter table public.ocena_ai add column if not exists sesja text;
create index if not exists ocena_ai_user_sesja on public.ocena_ai (user_id, sesja) where sesja is not null;
