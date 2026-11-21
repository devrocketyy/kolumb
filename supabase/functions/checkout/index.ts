// POST /functions/v1/checkout  { plan: 'miesiac' | 'matura', przedmioty: ['biologia', …] }  →  { url } Stripe Checkout.
//  • miesiac — subskrypcja odnawiana co miesiąc (karta, Apple Pay / Google Pay), anulowanie w każdej chwili;
//  • matura  — jednorazowa płatność za dostęp do dnia DOSTEP_MATURA_DO (karta, BLIK, Przelewy24).
// Cena zależy od planu i liczby przedmiotów: sekrety STRIPE_PRICE_MATURA_1/2/3 i STRIPE_PRICE_MIESIAC_1/2/3.
import { stripe, json, cors, uczen, klientStripe, appUrl, listaPrzedmiotow } from '../_shared/wspolne.ts';

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
