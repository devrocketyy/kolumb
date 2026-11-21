-- IndexLab — dostęp osobno na każdy przedmiot (+ pakiety 2 i 3 przedmiotów).
-- Uruchom w Supabase: SQL Editor → wklej całość → Run. Skrypt można uruchomić ponownie.
-- Wymaga wcześniejszych migracji 001–003.
--
-- Zasada: dotychczasowa tabela „dostep” nadal oznacza dostęp do WSZYSTKICH przedmiotów
-- (stare zakupy, kody bez listy przedmiotów, nagrody za polecenia). Nowe zakupy zapisują się
-- w „dostep_przedmiot” — jeden wiersz na przedmiot. Treść jest widoczna, gdy działa którykolwiek z nich.

create table if not exists public.dostep_przedmiot (
  user_id uuid not null references auth.users on delete cascade,
  przedmiot text not null check (przedmiot in ('biologia', 'historia', 'wos')),
  plan text,                 -- 'matura' | 'miesiac' | 'kod' | 'recznie'
  zrodlo text,               -- 'stripe' | 'kod' | 'recznie'
  status text,
  wazne_do timestamptz,
  stripe_subscription text,
  updated_at timestamptz not null default now(),
  primary key (user_id, przedmiot)
);
alter table public.dostep_przedmiot enable row level security;
drop policy if exists "własny dostęp do przedmiotu" on public.dostep_przedmiot;
create policy "własny dostęp do przedmiotu" on public.dostep_przedmiot for select using (auth.uid() = user_id);
create index if not exists dostep_przedmiot_sub on public.dostep_przedmiot (stripe_subscription);

-- Czy zalogowany uczeń ma dostęp do danego przedmiotu (pełny dostęp albo dostęp do tego przedmiotu).
create or replace function public.ma_dostep_do(p text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.dostep where user_id = auth.uid() and wazne_do > now())
      or exists (select 1 from public.dostep_przedmiot where user_id = auth.uid() and przedmiot = p and wazne_do > now());
$$;

-- Treści: demo dla wszystkich, reszta tylko dla osób z dostępem do TEGO przedmiotu.
drop policy if exists "demo albo dostęp" on public.tresci;
drop policy if exists "demo albo dostęp do przedmiotu" on public.tresci;
create policy "demo albo dostęp do przedmiotu" on public.tresci for select using (demo or public.ma_dostep_do(przedmiot));

-- Kody mogą odblokowywać wybrane przedmioty (null = wszystkie, jak dotąd).
alter table public.kody add column if not exists przedmioty text[];

create or replace function public.wykorzystaj_kod(kod text) returns timestamptz
language plpgsql security definer set search_path = public, extensions as $$
declare
  uid uuid := auth.uid();
  k public.kody%rowtype;
  stare timestamptz;
  nowe timestamptz;
  p text;
begin
  if uid is null then raise exception 'Zaloguj się, aby wykorzystać kod.'; end if;
  if (select count(*) from public.kody_proby where user_id = uid and at > now() - interval '1 hour') >= 10 then
    raise exception 'Za dużo prób — spróbuj za godzinę.';
  end if;
  select * into k from public.kody
    where kod_hash = encode(digest(upper(regexp_replace(kod, '[^A-Za-z0-9]', '', 'g')), 'sha256'), 'hex')
    for update;
  if not found then
    insert into public.kody_proby (user_id) values (uid);
    raise exception 'Nieprawidłowy kod.';
  end if;
  if k.uzyty_przez is not null and k.uzyty_przez <> uid then raise exception 'Ten kod został już wykorzystany.'; end if;
  if k.uzyty_przez = uid then return now(); end if;

  if k.przedmioty is null then
    -- kod na wszystkie przedmioty — jak dotąd, w tabeli „dostep”
    select wazne_do into stare from public.dostep where user_id = uid;
    nowe := coalesce(k.do_dnia, greatest(coalesce(stare, now()), now()) + make_interval(days => k.dni));
    if stare is not null and stare > nowe then nowe := stare; end if;
    insert into public.dostep (user_id, plan, zrodlo, status, wazne_do, updated_at)
      values (uid, k.plan, 'kod', 'active', nowe, now())
      on conflict (user_id) do update set
        wazne_do = excluded.wazne_do,
        plan = case when public.dostep.zrodlo = 'stripe' and public.dostep.status = 'active' then public.dostep.plan else excluded.plan end,
        zrodlo = case when public.dostep.zrodlo = 'stripe' and public.dostep.status = 'active' then public.dostep.zrodlo else 'kod' end,
        status = 'active',
        updated_at = now();
  else
    foreach p in array k.przedmioty loop
      select wazne_do into stare from public.dostep_przedmiot where user_id = uid and przedmiot = p;
      nowe := coalesce(k.do_dnia, greatest(coalesce(stare, now()), now()) + make_interval(days => k.dni));
      if stare is not null and stare > nowe then nowe := stare; end if;
      insert into public.dostep_przedmiot (user_id, przedmiot, plan, zrodlo, status, wazne_do, updated_at)
        values (uid, p, k.plan, 'kod', 'active', nowe, now())
        on conflict (user_id, przedmiot) do update set wazne_do = excluded.wazne_do, status = 'active', updated_at = now();
    end loop;
  end if;
  update public.kody set uzyty_przez = uid, uzyty_at = now() where kod_hash = k.kod_hash;
  return nowe;
end;
$$;
revoke all on function public.wykorzystaj_kod(text) from public, anon;
grant execute on function public.wykorzystaj_kod(text) to authenticated;

-- Polecenia: polecony dostaje +7 dni do świeżo kupionych przedmiotów, polecający — 7 dni pełnego dostępu.
create or replace function public.nagrodz_polecenie(p_uid uuid) returns void
language plpgsql security definer set search_path = public as $$
declare
  ref uuid;
begin
  update public.polecenia set nagrodzone_at = now()
    where polecony = p_uid and nagrodzone_at is null
    returning polecajacy into ref;
  if ref is null then return; end if;
  update public.dostep set wazne_do = wazne_do + interval '7 days', updated_at = now() where user_id = p_uid and wazne_do > now();
  update public.dostep_przedmiot set wazne_do = wazne_do + interval '7 days', updated_at = now() where user_id = p_uid and wazne_do > now();
  insert into public.dostep (user_id, plan, zrodlo, status, wazne_do, updated_at)
    values (ref, 'polecenie', 'polecenie', 'active', now() + interval '7 days', now())
    on conflict (user_id) do update set
      wazne_do = greatest(coalesce(public.dostep.wazne_do, now()), now()) + interval '7 days',
      status = case when public.dostep.wazne_do > now() then public.dostep.status else 'active' end,
      updated_at = now();
end;
$$;
revoke all on function public.nagrodz_polecenie(uuid) from public, anon, authenticated;
grant execute on function public.nagrodz_polecenie(uuid) to service_role;

-- Kod polecający tylko przed pierwszym zakupem — zakupy są teraz też w „dostep_przedmiot”.
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
  if exists (select 1 from public.dostep where user_id = uid and zrodlo = 'stripe')
     or exists (select 1 from public.dostep_przedmiot where user_id = uid and zrodlo = 'stripe') then
    raise exception 'Kod polecający można dodać przed pierwszym zakupem.';
  end if;
  insert into public.polecenia (polecony, polecajacy) values (uid, ref);
end;
$$;
revoke all on function public.uzyj_polecenia(text) from public, anon;
grant execute on function public.uzyj_polecenia(text) to authenticated;
