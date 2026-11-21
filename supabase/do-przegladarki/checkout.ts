// checkout — wersja jednoplikowa do wklejenia w Supabase → Edge Functions → Open Editor (nazwa funkcji: checkout).
// Generowana z functions/checkout/index.ts + functions/_shared/wspolne.ts — edytuj tamte pliki.
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
  if (data?.stripe_customer) return data.stripe_customer as string;
  const c = await stripe.customers.create({ email, metadata: { user_id: uid } });
  await admin.from('dostep').upsert({ user_id: uid, stripe_customer: c.id, updated_at: new Date().toISOString() });
  return c.id;
}

export const appUrl = (hash: string) => `${(Deno.env.get('APP_URL') ?? '').replace(/\/+$/, '')}/${hash}`;

// Przedmioty, które można kupić osobno. Lista musi zgadzać się z migracją 004 (check w dostep_przedmiot).
export const PRZEDMIOTY = ['biologia', 'historia', 'wos'];
export const listaPrzedmiotow = (x: unknown): string[] => {
  const arr = Array.isArray(x) ? x : String(x ?? '').split(',');
  return [...new Set(arr.map((v) => String(v).trim()).filter((v) => PRZEDMIOTY.includes(v)))].sort();
};

// POST /functions/v1/checkout  { plan: 'miesiac' | 'matura', przedmioty: ['biologia', …] }  →  { url } Stripe Checkout.
//  • miesiac — subskrypcja odnawiana co miesiąc (karta, Apple Pay / Google Pay), anulowanie w każdej chwili;
//  • matura  — jednorazowa płatność za dostęp do dnia DOSTEP_MATURA_DO (karta, BLIK, Przelewy24).
// Cena zależy od planu i liczby przedmiotów: sekrety STRIPE_PRICE_MATURA_1/2/3 i STRIPE_PRICE_MIESIAC_1/2/3.

const cena = (plan: string, n: number) => Deno.env.get(`STRIPE_PRICE_${plan.toUpperCase()}_${n}`);

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors });
  try {
    const user = await uczen(req);
    if (!user) return json({ error: 'Zaloguj się, aby kupić dostęp.' }, 401);
    const body = await req.json().catch(() => ({}));
    const plan = body.plan;
    const przedmioty = listaPrzedmiotow(body.przedmioty);
    if (!['miesiac', 'matura'].includes(plan)) return json({ error: 'Nieznany plan.' }, 400);
    if (!przedmioty.length) return json({ error: 'Wybierz co najmniej jeden przedmiot.' }, 400);
    const price = cena(plan, przedmioty.length);
    if (!price) return json({ error: 'Ten pakiet nie jest jeszcze dostępny.' }, 400);
    const customer = await klientStripe(user.id, user.email);
    const wspolne = {
      customer,
      client_reference_id: user.id,
      line_items: [{ price, quantity: 1 }],
      success_url: appUrl('#/plany/ok'),
      cancel_url: appUrl('#/plany'),
      locale: 'pl' as const,
      allow_promotion_codes: true,
      metadata: { app: 'indexlab', user_id: user.id, plan, przedmioty: przedmioty.join(',') },
    };
    const session = plan === 'miesiac'
      ? await stripe.checkout.sessions.create({
          ...wspolne,
          mode: 'subscription',
          subscription_data: { metadata: { app: 'indexlab', user_id: user.id, plan, przedmioty: przedmioty.join(',') } },
        })
      : await stripe.checkout.sessions.create({
          ...wspolne,
          mode: 'payment',
          payment_method_types: ['card', 'blik', 'p24'],
          payment_intent_data: { metadata: { app: 'indexlab', user_id: user.id, plan, przedmioty: przedmioty.join(',') } },
        });
    return json({ url: session.url });
  } catch (e) {
    console.error(e);
    return json({ error: 'Nie udało się rozpocząć płatności.' }, 500);
  }
});
