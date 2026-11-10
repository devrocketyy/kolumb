// POST /functions/v1/checkout  { plan: 'miesiac' | 'matura' }  →  { url } strony płatności Stripe Checkout.
//  • miesiac — subskrypcja odnawiana co miesiąc (karta, Apple Pay / Google Pay), anulowanie w każdej chwili;
//  • matura  — jednorazowa płatność za dostęp do dnia DOSTEP_MATURA_DO (karta, BLIK, Przelewy24).
import { stripe, json, cors, uczen, klientStripe, appUrl } from '../_shared/wspolne.ts';

const CENY: Record<string, string | undefined> = {
  miesiac: Deno.env.get('STRIPE_PRICE_MIESIAC'),
  matura: Deno.env.get('STRIPE_PRICE_MATURA'),
};

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors });
  try {
    const user = await uczen(req);
    if (!user) return json({ error: 'Zaloguj się, aby kupić dostęp.' }, 401);
    const { plan } = await req.json().catch(() => ({}));
    const price = CENY[plan];
    if (!price) return json({ error: 'Nieznany plan.' }, 400);
    const customer = await klientStripe(user.id, user.email);
    const wspolne = {
      customer,
      client_reference_id: user.id,
      line_items: [{ price, quantity: 1 }],
      success_url: appUrl('#/plany/ok'),
      cancel_url: appUrl('#/plany'),
      locale: 'pl' as const,
      allow_promotion_codes: true,
      metadata: { user_id: user.id, plan },
    };
    const session = plan === 'miesiac'
      ? await stripe.checkout.sessions.create({
          ...wspolne,
          mode: 'subscription',
          subscription_data: { metadata: { user_id: user.id, plan } },
        })
      : await stripe.checkout.sessions.create({
          ...wspolne,
          mode: 'payment',
          payment_method_types: ['card', 'blik', 'p24'],
          payment_intent_data: { metadata: { user_id: user.id, plan } },
        });
    return json({ url: session.url });
  } catch (e) {
    console.error(e);
    return json({ error: 'Nie udało się rozpocząć płatności.' }, 500);
  }
});
