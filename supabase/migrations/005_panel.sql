-- IndexLab — panel właściciela (#/panel w aplikacji). Uruchom po 001–004: SQL Editor → wklej → Run.
-- Potem dopisz SIEBIE jako admina (raz, w SQL Editorze, podając swój e-mail):
--   insert into public.admini (user_id) select id from auth.users where email = 'TWÓJ_EMAIL' on conflict do nothing;
-- Wszystkie dane panelu idą przez funkcje poniżej; każda najpierw sprawdza, czy pytający jest adminem.

create table if not exists public.admini (
  user_id uuid primary key references auth.users on delete cascade,
  created_at timestamptz not null default now()
);
alter table public.admini enable row level security; -- brak polityk = brak dostępu z aplikacji

-- statusy zgłoszeń błędów (nowe → załatwione)
alter table public.zgloszenia add column if not exists zalatwione_at timestamptz;

create or replace function public.jestem_adminem() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.admini where user_id = auth.uid());
$$;

create or replace function public._tylko_admin() returns void
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.jestem_adminem() then raise exception 'Brak uprawnień.'; end if;
end;
$$;

-- Liczby na pulpit panelu.
create or replace function public.admin_statystyki() returns json
language plpgsql stable security definer set search_path = public, auth as $$
declare wynik json;
begin
  perform public._tylko_admin();
  select json_build_object(
    'konta', (select count(*) from auth.users),
    'konta_7d', (select count(*) from auth.users where created_at > now() - interval '7 days'),
    'aktywni_1d', (select count(*) from public.postepy where updated_at > now() - interval '1 day'),
    'aktywni_7d', (select count(*) from public.postepy where updated_at > now() - interval '7 days'),
    'aktywni_30d', (select count(*) from public.postepy where updated_at > now() - interval '30 days'),
    'pelny_dostep', (select count(*) from public.dostep where wazne_do > now()),
    'przedmioty', (select coalesce(json_object_agg(przedmiot, n), '{}'::json) from
                    (select przedmiot, count(*) n from public.dostep_przedmiot where wazne_do > now() group by przedmiot) x),
    'subskrypcje', (select count(*) from public.dostep_przedmiot where plan = 'miesiac' and status = 'active' and wazne_do > now())
                 + (select count(*) from public.dostep where plan = 'miesiac' and status = 'active' and wazne_do > now()),
    'zakupy_30d', (select count(*) from public.dostep_przedmiot where zrodlo = 'stripe' and updated_at > now() - interval '30 days'),
    'zgloszenia_nowe', (select count(*) from public.zgloszenia where zalatwione_at is null),
    'polecenia', (select count(*) from public.polecenia),
    'polecenia_nagrodzone', (select count(*) from public.polecenia where nagrodzone_at is not null)
  ) into wynik;
  return wynik;
end;
$$;

-- Rejestracje dzień po dniu (ostatnie 30 dni) — do wykresu.
create or replace function public.admin_rejestracje() returns json
language plpgsql stable security definer set search_path = public, auth as $$
declare wynik json;
begin
  perform public._tylko_admin();
  select coalesce(json_agg(json_build_object('dzien', d::date, 'n', coalesce(n, 0)) order by d), '[]'::json) into wynik
  from generate_series(current_date - 29, current_date, interval '1 day') d
  left join (select created_at::date dz, count(*) n from auth.users where created_at > current_date - 30 group by 1) u on u.dz = d::date;
  return wynik;
end;
$$;

create or replace function public.admin_zgloszenia(wszystkie boolean default false) returns json
language plpgsql stable security definer set search_path = public, auth as $$
declare wynik json;
begin
  perform public._tylko_admin();
  select coalesce(json_agg(row_to_json(z) order by z.created_at desc), '[]'::json) into wynik from (
    select g.id, g.temat, g.rodzaj, g.opis, g.created_at, g.zalatwione_at, u.email
    from public.zgloszenia g left join auth.users u on u.id = g.user_id
    where wszystkie or g.zalatwione_at is null
    order by g.created_at desc limit 200) z;
  return wynik;
end;
$$;

create or replace function public.admin_zalatw(p_id bigint) returns void
language plpgsql security definer set search_path = public as $$
begin
  perform public._tylko_admin();
  update public.zgloszenia set zalatwione_at = case when zalatwione_at is null then now() else null end where id = p_id;
end;
$$;

create or replace function public.admin_kody() returns json
language plpgsql stable security definer set search_path = public as $$
declare wynik json;
begin
  perform public._tylko_admin();
  select coalesce(json_agg(row_to_json(k) order by k.utworzone desc), '[]'::json) into wynik from (
    select partia, count(*) wszystkie, count(uzyty_przez) uzyte, min(created_at) utworzone,
           max(do_dnia) do_dnia, max(dni) dni, max(array_to_string(przedmioty, ', ')) przedmioty
    from public.kody group by partia) k;
  return wynik;
end;
$$;

-- Ręczne nadanie dostępu (np. dla testera albo po reklamacji). p_przedmiot = null → wszystkie przedmioty.
create or replace function public.admin_nadaj(p_email text, p_przedmiot text, p_do date) returns text
language plpgsql security definer set search_path = public, auth as $$
declare uid uuid; koniec timestamptz := (p_do::timestamp + time '23:59:59') at time zone 'Europe/Warsaw';
begin
  perform public._tylko_admin();
  select id into uid from auth.users where lower(email) = lower(trim(p_email));
  if uid is null then raise exception 'Nie ma konta z tym e-mailem.'; end if;
  if p_przedmiot is null or p_przedmiot = '' then
    insert into public.dostep (user_id, plan, zrodlo, status, wazne_do, updated_at)
      values (uid, 'recznie', 'recznie', 'active', koniec, now())
      on conflict (user_id) do update set wazne_do = greatest(coalesce(public.dostep.wazne_do, now()), koniec), status = 'active', updated_at = now();
  else
    insert into public.dostep_przedmiot (user_id, przedmiot, plan, zrodlo, status, wazne_do, updated_at)
      values (uid, p_przedmiot, 'recznie', 'recznie', 'active', koniec, now())
      on conflict (user_id, przedmiot) do update set wazne_do = greatest(coalesce(public.dostep_przedmiot.wazne_do, now()), koniec), status = 'active', updated_at = now();
  end if;
  return 'ok';
end;
$$;

-- Wyszukiwanie ucznia po e-mailu (obsługa zgłoszeń, reklamacje).
create or replace function public.admin_uczen(p_email text) returns json
language plpgsql stable security definer set search_path = public, auth as $$
declare uid uuid; wynik json;
begin
  perform public._tylko_admin();
  select id into uid from auth.users where lower(email) = lower(trim(p_email));
  if uid is null then return null; end if;
  select json_build_object(
    'email', (select email from auth.users where id = uid),
    'od', (select created_at from auth.users where id = uid),
    'ostatnio', (select updated_at from public.postepy where user_id = uid),
    'pelny', (select row_to_json(d) from (select plan, zrodlo, status, wazne_do from public.dostep where user_id = uid) d),
    'przedmioty', (select coalesce(json_agg(row_to_json(p)), '[]'::json) from
                    (select przedmiot, plan, zrodlo, status, wazne_do from public.dostep_przedmiot where user_id = uid) p)
  ) into wynik;
  return wynik;
end;
$$;

revoke all on function public._tylko_admin() from public, anon;
revoke all on function public.admin_statystyki() from public, anon;
revoke all on function public.admin_rejestracje() from public, anon;
revoke all on function public.admin_zgloszenia(boolean) from public, anon;
revoke all on function public.admin_zalatw(bigint) from public, anon;
revoke all on function public.admin_kody() from public, anon;
revoke all on function public.admin_nadaj(text, text, date) from public, anon;
revoke all on function public.admin_uczen(text) from public, anon;
grant execute on function public.jestem_adminem() to authenticated;
grant execute on function public._tylko_admin() to authenticated;
grant execute on function public.admin_statystyki() to authenticated;
grant execute on function public.admin_rejestracje() to authenticated;
grant execute on function public.admin_zgloszenia(boolean) to authenticated;
grant execute on function public.admin_zalatw(bigint) to authenticated;
grant execute on function public.admin_kody() to authenticated;
grant execute on function public.admin_nadaj(text, text, date) to authenticated;
grant execute on function public.admin_uczen(text) to authenticated;
