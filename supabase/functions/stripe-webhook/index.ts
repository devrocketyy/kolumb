// Webhook Stripe → tabela dostep. Jedyne miejsce (poza kodami), które nadaje dostęp premium.
// W Stripe: Developers → Webhooks → endpoint https://<projekt>.supabase.co/functions/v1/stripe-webhook
// zdarzenia: checkout.session.completed, invoice.paid, customer.subscription.updated, customer.subscription.deleted
import Stripe from 'npm:stripe@17.7.0';
import { stripe, admin, listaPrzedmiotow } from '../_shared/wspolne.ts';

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

async function zSubskrypcji(sub: Stripe.Subscription) {
  const uid = sub.metadata?.user_id || (await uidKlienta(sub.customer as string));
  if (!uid) return;
  const aktywna = sub.status === 'active' || sub.status === 'trialing';
  const przedmioty = listaPrzedmiotow(sub.metadata?.przedmioty);
  if (przedmioty.length) {
    await admin.from('dostep').upsert({ user_id: uid, stripe_customer: sub.customer, updated_at: new Date().toISOString() });
    await zapiszPrzedmioty(uid, przedmioty, { plan: 'miesiac', zrodlo: 'stripe', status: sub.status, stripe_subscription: sub.id },
      aktywna ? iso(koniecOkresu(sub)) : null);
    return;
  }
  // subskrypcja sprzed podziału na przedmioty — pełny dostęp
  await zapisz(uid, { plan: 'miesiac', zrodlo: 'stripe', status: sub.status, stripe_customer: sub.customer, stripe_subscription: sub.id },
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
