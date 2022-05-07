const staticPrefix = "static-files-v1"

const assetsUrls = [
    "/static/js/item_new.js",
    "/static/main.css"
]

self.addEventListener('install', async event => {
    const cache = await caches.open(staticPrefix)
    await cache.addAll(assetsUrls)
})

self.addEventListener('fetch', async event => {
    event.respondWith(cacheFirst(event.request))
})

async function cacheFirst(request) {
    const cached = await caches.match(request)
    return cached ?? await fetch(request)

}