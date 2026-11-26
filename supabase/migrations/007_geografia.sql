-- IndexLab — geografia jako piąty płatny przedmiot.
-- Uruchom w Supabase: SQL Editor → wklej całość → Run. Wymaga migracji 004. Można uruchomić ponownie.
alter table public.dostep_przedmiot drop constraint if exists dostep_przedmiot_przedmiot_check;
alter table public.dostep_przedmiot add constraint dostep_przedmiot_przedmiot_check
  check (przedmiot in ('biologia', 'chemia', 'geografia', 'historia', 'wos'));
