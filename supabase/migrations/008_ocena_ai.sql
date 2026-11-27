-- IndexLab — ocenianie odpowiedzi otwartych przez AI (funkcja Edge „ocen”).
-- Uruchom w Supabase: SQL Editor → wklej całość → Run. Można uruchomić ponownie.
-- Tabela służy do dziennego limitu ocen i statystyk; uczeń widzi tylko swoje wpisy.
create table if not exists public.ocena_ai (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users (id) on delete cascade,
  przedmiot text not null,
  zadanie text,
  pkt smallint,
  max smallint,
  created_at timestamptz not null default now()
);
create index if not exists ocena_ai_user_dzien on public.ocena_ai (user_id, created_at desc);

alter table public.ocena_ai enable row level security;
drop policy if exists "własne oceny AI" on public.ocena_ai;
create policy "własne oceny AI" on public.ocena_ai for select using (auth.uid() = user_id);
-- Zapis tylko przez funkcję Edge (klucz serwisowy) — brak polityki insert dla uczniów.
