// Kolumb — service worker: działanie offline.
// Przy wdrożeniu przez GitHub Actions znacznik __BUILD__ jest zastępowany identyfikatorem
// commita, dzięki czemu każda nowa wersja odświeża pamięć podręczną.
const VERSION = 'kolumb-__BUILD__';

const SHELL = [
  './',
  'index.html',
  'css/style.css',
  'js/app.js',
  'js/store.js',
  'js/srs.js',
  'js/data.js',
  'manifest.webmanifest',
  'ikony/ikona.svg',
  'ikony/ikona-192.png',
  'ikony/ikona-512.png',
  'ikony/apple-touch-icon.png',
  'przedmioty/index.json',
];

async function precache() {
  const cache = await caches.open(VERSION);
  await cache.addAll(SHELL.map((u) => new Request(u, { cache: 'reload' })));
  // Wszystkie przedmioty z indeksu — żeby nauka działała bez internetu.
  try {
    const res = await cache.match('przedmioty/index.json');
    const idx = await res.json();
    const files = Array.isArray(idx) ? idx : idx.przedmioty || [];
    await cache.addAll(files.map((f) => new Request(`przedmioty/${f}`, { cache: 'reload' })));
  } catch (e) {
    /* przedmioty zostaną zapisane przy pierwszym użyciu */
  }
}

self.addEventListener('install', (event) => {
  event.waitUntil(precache().then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith('kolumb-') && k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

function timeout(ms) {
  return new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), ms));
}

// Treści (JSON): najpierw sieć, żeby poprawki docierały od razu; offline — kopia z pamięci.
async function networkFirst(req) {
  const cache = await caches.open(VERSION);
  try {
    const res = await Promise.race([fetch(req), timeout(5000)]);
    if (res.ok) cache.put(req, res.clone());
    return res;
  } catch {
    const hit = await cache.match(req, { ignoreSearch: true });
    if (hit) return hit;
    throw new Error('offline');
  }
}

// Pliki aplikacji: natychmiast z pamięci, w tle aktualizacja.
async function staleWhileRevalidate(req, event) {
  const cache = await caches.open(VERSION);
  const hit = await cache.match(req, { ignoreSearch: true });
  const update = fetch(req)
    .then((res) => {
      if (res.ok) cache.put(req, res.clone());
      return res;
    })
    .catch(() => null);
  if (hit) {
    event.waitUntil(update);
    return hit;
  }
  const res = await update;
  if (res) return res;
  if (req.mode === 'navigate') return cache.match('index.html');
  return Response.error();
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req).catch(async () => (await caches.match('index.html')) || (await caches.match('./')))
    );
    return;
  }
  if (url.pathname.endsWith('.json')) {
    event.respondWith(networkFirst(req));
    return;
  }
  event.respondWith(staleWhileRevalidate(req, event));
});
