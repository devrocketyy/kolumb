// stripe-webhook — wersja jednoplikowa do wklejenia w Supabase → Edge Functions → Open Editor (nazwa funkcji: stripe-webhook).
// Generowana z functions/stripe-webhook/index.ts + functions/_shared/wspolne.ts — edytuj tamte pliki.
// Wspólne elementy funkcji płatności IndexLab (Supabase Edge Functions, Deno).
import Stripe from 'npm:stripe@17.7.0';
import { createClient } from 'npm:@supabase/supabase-js@2.49.4';

export const stripe = new Stripe(Deno.env.get('STRIPE_SECRET_KEY') ?? '', {
  httpClient: Stripe.createFetchHttpClient(),
});

// Klient z kluczem serwisowym — omija RLS, tylko po stronie serwera.
export const admin = createClient(Deno.env.get('SUPABASE_URL')!, Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!, {
  auth: { persistSession: false },
});

const ORIGIN = Deno.env.get('APP_URL') ?? '*';
export const cors = {
  'Access-Control-Allow-Origin': ORIGIN === '*' ? '*' : new URL(ORIGIN).origin,
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
};

export const json = (body: unknown, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { ...cors, 'Content-Type': 'application/json' } });

// Zalogowany uczeń na podstawie tokenu z nagłówka Authorization.
export async function uczen(req: Request) {
  const token = (req.headers.get('Authorization') ?? '').replace(/^Bearer\s+/i, '');
  if (!token) return null;
  const { data, error } = await admin.auth.getUser(token);
  return error ? null : data.user;
}

// Klient Stripe przypisany do ucznia (tworzony przy pierwszym zakupie).
export async function klientStripe(uid: string, email?: string) {
  const { data } = await admin.from('dostep').select('stripe_customer').eq('user_id', uid).maybeSingle();
  if (data?.stripe_customer) {
    // klient mógł powstać na innym koncie/trybie Stripe (np. test → produkcja) — wtedy tworzymy nowego
    try {
      const c = await stripe.customers.retrieve(data.stripe_customer as string);
      if (!(c as { deleted?: boolean }).deleted) return data.stripe_customer as string;
    } catch { /* brak takiego klienta na tym koncie */ }
  }
  const c = await stripe.customers.create({ email, metadata: { user_id: uid } });
  await admin.from('dostep').upsert({ user_id: uid, stripe_customer: c.id, updated_at: new Date().toISOString() });
  return c.id;
}

export const appUrl = (hash: string) => `${(Deno.env.get('APP_URL') ?? '').replace(/\/+$/, '')}/${hash}`;

// Przedmioty, które można kupić osobno. Lista musi zgadzać się z migracją 004 (check w dostep_przedmiot).
export const PRZEDMIOTY = ['biologia', 'chemia', 'historia', 'wos'];
export const listaPrzedmiotow = (x: unknown): string[] => {
  const arr = Array.isArray(x) ? x : String(x ?? '').split(',');
  return [...new Set(arr.map((v) => String(v).trim()).filter((v) => PRZEDMIOTY.includes(v)))].sort();
};

// Webhook Stripe → tabela dostep. Jedyne miejsce (poza kodami), które nadaje dostęp premium.
// W Stripe: Developers → Webhooks → endpoint https://<projekt>.supabase.co/functions/v1/stripe-webhook
// Jedno konto Stripe może obsługiwać inne projekty: zdarzenia bez metadata.app='indexlab' są pomijane.
// zdarzenia: checkout.session.completed, invoice.paid, customer.subscription.updated, customer.subscription.deleted

const SECRET = Deno.env.get('STRIPE_WEBHOOK_SECRET') ?? '';
const MATURA_DO = Deno.env.get('DOSTEP_MATURA_DO') ?? '2027-05-31'; // koniec dostępu „do matury”
const crypto = Stripe.createSubtleCryptoProvider();

const iso = (sec?: number | null) => (sec ? new Date(sec * 1000).toISOString() : null);
const koniecOkresu = (sub: Stripe.Subscription) =>
  // od API 2025-03-31 koniec okresu jest w pozycjach subskrypcji
  (sub as unknown as { current_period_end?: number }).current_period_end ?? sub.items?.data?.[0]?.current_period_end;

async function zapisz(uid: string, zmiany: Record<string, unknown>, wydluz?: string | null) {
  const { data: stary } = await admin.from('dostep').select('wazne_do').eq('user_id', uid).maybeSingle();
  const row: Record<string, unknown> = { user_id: uid, ...zmiany, updated_at: new Date().toISOString() };
  // dostęp tylko się wydłuża (nie skracamy np. okresu z kodu)
  if (wydluz) row.wazne_do = !stary?.wazne_do || new Date(wydluz) > new Date(stary.wazne_do) ? wydluz : stary.wazne_do;
  const { error } = await admin.from('dostep').upsert(row);
  if (error) throw error;
}

// Zakup konkretnych przedmiotów → wiersze w dostep_przedmiot (dostęp tylko się wydłuża).
async function zapiszPrzedmioty(uid: string, przedmioty: string[], zmiany: Record<string, unknown>, wydluz?: string | null) {
  for (const p of przedmioty) {
    const { data: stary } = await admin.from('dostep_przedmiot').select('wazne_do').eq('user_id', uid).eq('przedmiot', p).maybeSingle();
    const row: Record<string, unknown> = { user_id: uid, przedmiot: p, ...zmiany, updated_at: new Date().toISOString() };
    if (wydluz) row.wazne_do = !stary?.wazne_do || new Date(wydluz) > new Date(stary.wazne_do) ? wydluz : stary.wazne_do;
    const { error } = await admin.from('dostep_przedmiot').upsert(row);
    if (error) throw error;
  }
}

async function uidKlienta(customer: string | null) {
  if (!customer) return null;
  const { data } = await admin.from('dostep').select('user_id').eq('stripe_customer', customer).maybeSingle();
  return (data?.user_id as string) ?? null;
}

// Jedno konto Stripe obsługuje kilka projektów — bierzemy tylko płatności oznaczone app=indexlab.
const nasze = (m?: Stripe.Metadata | null) => m?.app === 'indexlab';

async function zSubskrypcji(sub: Stripe.Subscription) {
  if (!nasze(sub.metadata)) return;
  const uid = sub.metadata?.user_id || (await uidKlienta(sub.customer as string));
  if (!uid) return;
  const aktywna = sub.status === 'active' || sub.status === 'trialing';
  // anulowana „na koniec okresu” — Stripe zostawia status active; zapisujemy osobny status, żeby aplikacja nie pisała „odnawia się”
  const konczy = aktywna && (sub.cancel_at_period_end || !!(sub as unknown as { cancel_at?: number }).cancel_at);
  const status = konczy ? 'anulowana' : sub.status;
  const przedmioty = listaPrzedmiotow(sub.metadata?.przedmioty);
  if (przedmioty.length) {
    await admin.from('dostep').upsert({ user_id: uid, stripe_customer: sub.customer, updated_at: new Date().toISOString() });
    await zapiszPrzedmioty(uid, przedmioty, { plan: 'miesiac', zrodlo: 'stripe', status, stripe_subscription: sub.id },
      aktywna ? iso(koniecOkresu(sub)) : null);
    return;
  }
  // subskrypcja sprzed podziału na przedmioty — pełny dostęp
  await zapisz(uid, { plan: 'miesiac', zrodlo: 'stripe', status, stripe_customer: sub.customer, stripe_subscription: sub.id },
    aktywna ? iso(koniecOkresu(sub)) : null);
}

Deno.serve(async (req) => {
  let event: Stripe.Event;
  try {
    event = await stripe.webhooks.constructEventAsync(await req.text(), req.headers.get('Stripe-Signature') ?? '', SECRET, undefined, crypto);
  } catch (e) {
    return new Response(`Zły podpis: ${(e as Error).message}`, { status: 400 });
  }
  try {
    switch (event.type) {
      case 'checkout.session.completed':
      case 'checkout.session.async_payment_succeeded': {
        const s = event.data.object as Stripe.Checkout.Session;
        if (!nasze(s.metadata)) break;
        const uid = s.client_reference_id || s.metadata?.user_id;
        if (!uid) break;
        if (s.mode === 'subscription' && s.subscription) {
          await zSubskrypcji(await stripe.subscriptions.retrieve(s.subscription as string));
        } else if (s.mode === 'payment' && s.payment_status === 'paid') {
          const koniec = new Date(`${MATURA_DO}T23:59:59+02:00`).toISOString();
          const przedmioty = listaPrzedmiotow(s.metadata?.przedmioty);
          if (przedmioty.length) {
            await admin.from('dostep').upsert({ user_id: uid, stripe_customer: s.customer, updated_at: new Date().toISOString() });
            await zapiszPrzedmioty(uid, przedmioty, { plan: 'matura', zrodlo: 'stripe', status: 'active' }, koniec);
          } else {
            await zapisz(uid, { plan: 'matura', zrodlo: 'stripe', status: 'active', stripe_customer: s.customer }, koniec);
          }
        }
        // program poleceń: +7 dni dla poleconego i polecającego (tylko raz, przy pierwszym zakupie)
        const { error: blad } = await admin.rpc('nagrodz_polecenie', { p_uid: uid });
        if (blad) console.error('polecenie', blad);
        break;
      }
      case 'invoice.paid': {
        const inv = event.data.object as Stripe.Invoice & { subscription?: string; parent?: { subscription_details?: { subscription?: string } } };
        const subId = inv.subscription || inv.parent?.subscription_details?.subscription;
        if (subId) await zSubskrypcji(await stripe.subscriptions.retrieve(subId));
        break;
      }
      case 'customer.subscription.updated':
      case 'customer.subscription.deleted':
        await zSubskrypcji(event.data.object as Stripe.Subscription);
        break;
    }
  } catch (e) {
    console.error(e);
    return new Response('Błąd zapisu', { status: 500 }); // Stripe ponowi wysyłkę
  }
  return new Response(JSON.stringify({ ok: true }), { headers: { 'Content-Type': 'application/json' } });
});
