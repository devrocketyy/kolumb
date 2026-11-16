-- IndexLab — usuwanie konta przez ucznia (przycisk „Usuń konto” w Ustawieniach).
-- Uruchom w Supabase: SQL Editor → wklej → Run. Skrypt można uruchomić ponownie.
-- Usuwa użytkownika z auth.users; postępy (postepy) i dostęp (dostep) znikają dzięki „on delete cascade”,
-- a wykorzystane kody zostają w bazie bez przypisania (on delete set null).
-- Uwaga: aktywną subskrypcję Stripe trzeba anulować osobno (uczeń widzi to ostrzeżenie przed usunięciem).
create or replace function public.usun_konto() returns void
language plpgsql security definer set search_path = public, auth as $$
begin
  if auth.uid() is null then raise exception 'Nie zalogowano.'; end if;
  delete from auth.users where id = auth.uid();
end;
$$;
revoke all on function public.usun_konto() from public, anon;
grant execute on function public.usun_konto() to authenticated;
