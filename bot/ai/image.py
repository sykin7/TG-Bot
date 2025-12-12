import os, openai, asyncio
from bot.utils.cache import cache_get, cache_set

openai.api_key = os.environ.get("OPENAI_API_KEY")

async def generate_image(prompt: str):
    key = f"img_cache:{prompt}"
    cached = await cache_get(key)
    if cached:
        return cached
    resp = await asyncio.to_thread(lambda: openai.Image.create(prompt=prompt, n=1, size="512x512"))
    url = resp.data[0].url
    await cache_set(key, url, expire=86400)
    return url
