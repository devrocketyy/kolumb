-- IndexLab — program poleceń: każdy uczeń z kontem ma kod; gdy polecony kupi dostęp, obaj dostają +7 dni.
-- Uruchom w Supabase: SQL Editor → wklej → Run. Skrypt można uruchomić ponownie.

create table if not exists public.polecenia_kody (
  user_id uuid primary key references auth.users on delete cascade,
  kod text not null unique,
  created_at timestamptz not null default now()
);
alter table public.polecenia_kody enable row level security;

create table if not exists public.polecenia (
  polecony uuid primary key references auth.users on delete cascade,
  polecajacy uuid not null references auth.users on delete cascade,
  created_at timestamptz not null default now(),
  nagrodzone_at timestamptz
);
alter table public.polecenia enable row level security;
-- brak polityk RLS = brak bezpośredniego dostępu z aplikacji; wszystko przez funkcje poniżej

-- Mój kod (tworzony przy pierwszym wywołaniu) + statystyki poleceń.
create or replace function public.moj_kod_polecajacy() returns json
language plpgsql security definer set search_path = public, extensions as $$
declare
  uid uuid := auth.uid();
  k text;
begin
  if uid is null then raise exception 'Zaloguj się.'; end if;
  select kod into k from public.polecenia_kody where user_id = uid;
  while k is null loop
    k := upper(substr(translate(encode(gen_random_bytes(8), 'base64'), '+/=0O1IL', ''), 1, 6));
    if length(k) = 6 and not exists (select 1 from public.polecenia_kody where kod = k) then
      insert into public.polecenia_kody (user_id, kod) values (uid, k);
    else
      k := null;
    end if;
  end loop;
  return json_build_object(
    'kod', k,
    'polecone', (select count(*) from public.polecenia where polecajacy = uid),
    'nagrodzone', (select count(*) from public.polecenia where polecajacy = uid and nagrodzone_at is not null),
    'moje', (select pk.kod from public.polecenia p join public.polecenia_kody pk on pk.user_id = p.polecajacy where p.polecony = uid)
  );
end;
$$;

-- Dodanie kodu znajomego (raz, przed pierwszym zakupem, nie własnego).
create or replace function public.uzyj_polecenia(kod text) returns void
language plpgsql security definer set search_path = public as $$
declare
  uid uuid := auth.uid();
  ref uuid;
begin
  if uid is null then raise exception 'Zaloguj się.'; end if;
  select user_id into ref from public.polecenia_kody where polecenia_kody.kod = upper(trim(uzyj_polecenia.kod));
  if ref is null then raise exception 'Nie ma takiego kodu polecającego.'; end if;
  if ref = uid then raise exception 'Nie możesz polecić samego siebie.'; end if;
  if exists (select 1 from public.polecenia where polecony = uid) then raise exception 'Kod polecający jest już dodany do Twojego konta.'; end if;
  if exists (select 1 from public.dostep where user_id = uid and zrodlo = 'stripe') then
    raise exception 'Kod polecający można dodać przed pierwszym zakupem.';
  end if;
  insert into public.polecenia (polecony, polecajacy) values (uid, ref);
end;
$$;

-- Nagroda po zakupie: wywołuje ją tylko webhook Stripe (klucz serwisowy).
create or replace function public.nagrodz_polecenie(p_uid uuid) returns void
language plpgsql security definer set search_path = public as $$
declare
  ref uuid;
begin
  update public.polecenia set nagrodzone_at = now()
    where polecony = p_uid and nagrodzone_at is null
    returning polecajacy into ref;
  if ref is null then return; end if;
  -- polecony: +7 dni do świeżo kupionego dostępu
  update public.dostep set wazne_do = wazne_do + interval '7 days', updated_at = now() where user_id = p_uid;
  -- polecający: +7 dni od końca obecnego dostępu albo od dziś
  insert into public.dostep (user_id, plan, zrodlo, status, wazne_do, updated_at)
    values (ref, 'polecenie', 'polecenie', 'active', now() + interval '7 days', now())
    on conflict (user_id) do update set
      wazne_do = greatest(coalesce(public.dostep.wazne_do, now()), now()) + interval '7 days',
      status = case when public.dostep.wazne_do > now() then public.dostep.status else 'active' end,
      updated_at = now();
end;
$$;

revoke all on function public.moj_kod_polecajacy() from public, anon;
revoke all on function public.uzyj_polecenia(text) from public, anon;
revoke all on function public.nagrodz_polecenie(uuid) from public, anon, authenticated;
grant execute on function public.moj_kod_polecajacy() to authenticated;
grant execute on function public.uzyj_polecenia(text) to authenticated;
grant execute on function public.nagrodz_polecenie(uuid) to service_role;
