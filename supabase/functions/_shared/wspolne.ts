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
