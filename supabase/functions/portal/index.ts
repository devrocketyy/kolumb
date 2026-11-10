// POST /functions/v1/portal  →  { url } panelu klienta Stripe (zmiana karty, faktury, anulowanie subskrypcji).
import { stripe, admin, json, cors, uczen, appUrl } from '../_shared/wspolne.ts';

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors });
  const user = await uczen(req);
  if (!user) return json({ error: 'Zaloguj się.' }, 401);
  const { data } = await admin.from('dostep').select('stripe_customer').eq('user_id', user.id).maybeSingle();
  if (!data?.stripe_customer) return json({ error: 'Brak płatności powiązanych z tym kontem.' }, 404);
  const s = await stripe.billingPortal.sessions.create({ customer: data.stripe_customer, return_url: appUrl('#/plany'), locale: 'pl' });
  return json({ url: s.url });
});
