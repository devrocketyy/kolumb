-- IndexLab — płatny dostęp: treści premium w bazie, subskrypcje (Stripe) i kody dostępu (np. sprzedawane na Naffy).
-- Uruchom w Supabase: SQL Editor → wklej całość → Run. Skrypt można uruchomić ponownie.

create extension if not exists pgcrypto with schema extensions;

-- Postępy ucznia (jeśli tabela jeszcze nie istnieje — opis w README, „Konta użytkowników”).
create table if not exists public.postepy (
  user_id uuid primary key references auth.users on delete cascade,
  data jsonb not null,
  updated_at timestamptz not null default now()
);
alter table public.postepy enable row level security;
drop policy if exists "własne postępy" on public.postepy;
create policy "własne postępy" on public.postepy
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

-- Dostęp ucznia: do kiedy ma premium i skąd (stripe | kod | recznie).
-- Uczeń może tylko odczytać swój wiersz. Zapisują wyłącznie: webhook Stripe (klucz serwisowy) i funkcja wykorzystaj_kod.
create table if not exists public.dostep (
  user_id uuid primary key references auth.users on delete cascade,
  plan text,
  zrodlo text,
  status text,
  wazne_do timestamptz,
  stripe_customer text unique,
  stripe_subscription text,
  updated_at timestamptz not null default now()
);
alter table public.dostep enable row level security;
drop policy if exists "własny dostęp" on public.dostep;
create policy "własny dostęp" on public.dostep for select using (auth.uid() = user_id);

create or replace function public.ma_dostep() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.dostep where user_id = auth.uid() and wazne_do > now());
$$;

-- Treści kursu: jeden wiersz = jeden plik z katalogu przedmioty/ (wgrywa je narzedzia/wgraj-tresci.mjs).
-- demo = true → widoczne dla wszystkich (spis treści, pierwszy dział, jeden arkusz); reszta tylko z aktywnym dostępem.
create table if not exists public.tresci (
  plik text primary key,
  przedmiot text not null,
  dane jsonb not null,
  demo boolean not null default false,
  updated_at timestamptz not null default now()
);
alter table public.tresci enable row level security;
drop policy if exists "demo albo dostęp" on public.tresci;
create policy "demo albo dostęp" on public.tresci for select using (demo or public.ma_dostep());

-- Kody dostępu: w bazie tylko skrót SHA-256 kodu. Brak polityk RLS = brak dostępu z aplikacji (tylko przez funkcję).
create table if not exists public.kody (
  kod_hash text primary key,
  plan text not null default 'kod',
  dni integer,                -- ile dni dostępu daje kod…
  do_dnia timestamptz,        -- …albo stała data końca (np. dzień po maturze)
  partia text,
  uzyty_przez uuid references auth.users on delete set null,
  uzyty_at timestamptz,
  created_at timestamptz not null default now(),
  check (dni is not null or do_dnia is not null)
);
alter table public.kody enable row level security;

-- Nieudane próby (ochrona przed zgadywaniem kodów).
create table if not exists public.kody_proby (
  user_id uuid not null,
  at timestamptz not null default now()
);
alter table public.kody_proby enable row level security;

create or replace function public.wykorzystaj_kod(kod text) returns timestamptz
language plpgsql security definer set search_path = public, extensions as $$
declare
  uid uuid := auth.uid();
  k public.kody%rowtype;
  stare timestamptz;
  nowe timestamptz;
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
  if k.uzyty_przez = uid then
    return (select wazne_do from public.dostep where user_id = uid);
  end if;
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
  update public.kody set uzyty_przez = uid, uzyty_at = now() where kod_hash = k.kod_hash;
  return nowe;
end;
$$;

revoke all on function public.wykorzystaj_kod(text) from public, anon;
grant execute on function public.wykorzystaj_kod(text) to authenticated;
