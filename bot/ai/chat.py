import os, openai, asyncio
from bot.utils.cache import cache_get, cache_set

openai.api_key = os.environ.get("OPENAI_API_KEY")

async def gpt_reply(message: str):
    key = f"gpt_cache:{message}"
    cached = await cache_get(key)
    if cached:
        return cached
    resp = await asyncio.to_thread(lambda: openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":message}],
        max_tokens=500
    ))
    text = resp.choices[0].message.content
    await cache_set(key, text, expire=1800)
    return text
