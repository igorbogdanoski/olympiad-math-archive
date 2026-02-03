// Service Worker for PWA functionality
const CACHE_NAME = 'olympiad-math-v1.0.0';
const STATIC_CACHE = 'olympiad-math-static-v1.0.0';
const DYNAMIC_CACHE = 'olympiad-math-dynamic-v1.0.0';
const API_CACHE = 'olympiad-math-api-v1.0.0';

// Resources to cache immediately
const STATIC_ASSETS = [
  '/',
  '/manifest.json',
];

// API endpoints to cache
const API_ENDPOINTS = [
  '/api/curriculum',
  '/api/assessments',
  '/api/manim-suggestions'
];

// Install event - cache static assets
self.addEventListener('install', (event) => {
  console.log('[SW] Installing service worker');
  event.waitUntil(
    Promise.all([
      caches.open(STATIC_CACHE).then(cache => {
        console.log('[SW] Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      }),
      // Skip waiting to activate immediately
      self.skipWaiting()
    ])
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  console.log('[SW] Activating service worker');
  event.waitUntil(
    Promise.all([
      // Clean up old caches
      caches.keys().then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== STATIC_CACHE &&
                cacheName !== DYNAMIC_CACHE &&
                cacheName !== API_CACHE) {
              console.log('[SW] Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      }),
      // Take control of all clients
      self.clients.claim()
    ])
  );
});

// Fetch event - serve from cache or network
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // 🛑 IGNORE NON-HTTP SCHEMES (chrome-extension, etc.)
  if (!url.protocol.startsWith('http')) {
    return; // Let browser handle extensions and other protocols
  }

  // Handle different types of requests
  if (request.method !== 'GET') {
    return; // Don't cache POST, PUT, DELETE, etc.
  }

  // Handle API requests
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(handleApiRequest(request));
    return;
  }

  // Handle static assets
  if (isStaticAsset(request.url)) {
    event.respondWith(handleStaticRequest(request));
    return;
  }

  // Handle HTML pages
  if (request.headers.get('accept').includes('text/html')) {
    event.respondWith(handlePageRequest(request));
    return;
  }

  // Default: Network first, then cache
  event.respondWith(
    fetch(request)
      .then(response => {
        // Cache successful responses
        if (response.ok) {
          const responseClone = response.clone();
          caches.open(DYNAMIC_CACHE).then(cache => {
            cache.put(request, responseClone);
          });
        }
        return response;
      })
      .catch(() => {
        // Fallback to cache
        return caches.match(request);
      })
  );
});

// Handle API requests with cache-first strategy for GET requests
async function handleApiRequest(request) {
  const url = new URL(request.url);

  // For assessment data, try cache first then network
  if (url.pathname === '/api/assessments') {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      // Return cached data and update in background
      fetch(request).then(networkResponse => {
        if (networkResponse.ok) {
          caches.open(API_CACHE).then(cache => {
            cache.put(request, networkResponse.clone());
          });
        }
      });
      return cachedResponse;
    }
  }

  // For other API requests, network first
  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      const responseClone = networkResponse.clone();
      caches.open(API_CACHE).then(cache => {
        cache.put(request, responseClone);
      });
    }
    return networkResponse;
  } catch (error) {
    // Fallback to cache
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }

    // Return offline response
    return new Response(
      JSON.stringify({
        error: 'Offline',
        message: 'Нема интернет конекција. Пробајте подоцна.'
      }),
      {
        status: 503,
        headers: { 'Content-Type': 'application/json' }
      }
    );
  }
}

// Handle static assets with cache-first strategy
async function handleStaticRequest(request) {
  const cachedResponse = await caches.match(request);
  if (cachedResponse) {
    return cachedResponse;
  }

  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      const responseClone = networkResponse.clone();
      caches.open(STATIC_CACHE).then(cache => {
        cache.put(request, responseClone);
      });
    }
    return networkResponse;
  } catch (error) {
    // 🛑 RETURN VALID ERROR RESPONSE (не undefined!)
    console.log('[SW] Static asset fetch failed:', request.url);
    
    // Return offline page for HTML requests
    if (request.headers.get('accept')?.includes('text/html')) {
      return caches.match('/offline.html');
    }
    
    // For images/icons that failed, return a placeholder response
    if (request.url.includes('.png') || request.url.includes('.jpg') || request.url.includes('.svg')) {
      return new Response('', {
        status: 404,
        statusText: 'Not Found',
        headers: { 'Content-Type': 'text/plain' }
      });
    }
    
    // Generic fallback
    return new Response('Network error occurred', {
      status: 503,
      statusText: 'Service Unavailable',
      headers: { 'Content-Type': 'text/plain' }
    });
  }
}

// Handle page requests with network-first strategy
async function handlePageRequest(request) {
  try {
    const networkResponse = await fetch(request);
    if (networkResponse.ok) {
      const responseClone = networkResponse.clone();
      caches.open(DYNAMIC_CACHE).then(cache => {
        cache.put(request, responseClone);
      });
    }
    return networkResponse;
  } catch (error) {
    // Try cache first
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
      return cachedResponse;
    }

    // Return offline page
    return caches.match('/offline.html') || new Response(
      `
      <!DOCTYPE html>
      <html lang="mk">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Offline - Олимпијска Математика</title>
        <style>
          body { font-family: system-ui, sans-serif; text-align: center; padding: 2rem; }
          .offline-message { max-width: 400px; margin: 0 auto; }
        </style>
      </head>
      <body>
        <div class="offline-message">
          <h1>🚫 Offline</h1>
          <p>Немате интернет конекција. Пробајте да се освежите кога ќе имате конекција.</p>
          <button onclick="window.location.reload()">Освежи</button>
        </div>
      </body>
      </html>
      `,
      {
        headers: { 'Content-Type': 'text/html' }
      }
    );
  }
}

// Check if URL is a static asset
function isStaticAsset(url) {
  const staticExtensions = ['.css', '.js', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.woff', '.woff2'];
  return staticExtensions.some(ext => url.includes(ext));
}

// Handle background sync for offline actions
self.addEventListener('sync', (event) => {
  console.log('[SW] Background sync triggered:', event.tag);

  if (event.tag === 'assessment-sync') {
    event.waitUntil(syncAssessments());
  }
});

// Background sync for assessments
async function syncAssessments() {
  try {
    // Get pending assessments from IndexedDB or similar
    const pendingAssessments = await getPendingAssessments();

    for (const assessment of pendingAssessments) {
      try {
        const response = await fetch('/api/assessments', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(assessment)
        });

        if (response.ok) {
          // Mark as synced
          await markAssessmentSynced(assessment.id);
        }
      } catch (error) {
        console.error('[SW] Failed to sync assessment:', assessment.id, error);
      }
    }
  } catch (error) {
    console.error('[SW] Background sync failed:', error);
  }
}

// Handle push notifications
self.addEventListener('push', (event) => {
  console.log('[SW] Push notification received');

  if (!event.data) return;

  const data = event.data.json();

  const options = {
    body: data.body,
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    vibrate: [100, 50, 100],
    data: {
      url: data.url || '/'
    },
    actions: [
      {
        action: 'view',
        title: 'Види',
        icon: '/icons/action-view.png'
      },
      {
        action: 'dismiss',
        title: 'Отфрли'
      }
    ]
  };

  event.waitUntil(
    self.registration.showNotification(data.title, options)
  );
});

// Handle notification clicks
self.addEventListener('notificationclick', (event) => {
  console.log('[SW] Notification clicked:', event.action);

  event.notification.close();

  if (event.action === 'view') {
    event.waitUntil(
      clients.openWindow(event.notification.data.url)
    );
  }
});

// Periodic background sync for data updates
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'content-update') {
    event.waitUntil(updateContent());
  }
});

async function updateContent() {
  try {
    // Update curriculum data
    const curriculumResponse = await fetch('/api/curriculum');
    if (curriculumResponse.ok) {
      caches.open(API_CACHE).then(cache => {
        cache.put('/api/curriculum', curriculumResponse.clone());
      });
    }

    // Update assessments
    const assessmentsResponse = await fetch('/api/assessments');
    if (assessmentsResponse.ok) {
      caches.open(API_CACHE).then(cache => {
        cache.put('/api/assessments', assessmentsResponse.clone());
      });
    }

    console.log('[SW] Content updated in background');
  } catch (error) {
    console.error('[SW] Background content update failed:', error);
  }
}

// Placeholder functions for offline data management
// In a real implementation, these would use IndexedDB
async function getPendingAssessments() {
  // Return pending assessments from local storage
  return [];
}

async function markAssessmentSynced(assessmentId) {
  // Mark assessment as synced
  console.log('[SW] Assessment synced:', assessmentId);
}

// Handle messages from the main thread
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }

  if (event.data && event.data.type === 'GET_VERSION') {
    event.ports[0].postMessage({ version: CACHE_NAME });
  }
});