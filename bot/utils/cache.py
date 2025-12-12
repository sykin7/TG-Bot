import aioredis, os
import asyncio

REDIS_URL = os.environ.get("REDIS_URL")
redis = None

async def get_redis():
    global redis
    if not redis:
        redis = await aioredis.from_url(REDIS_URL, decode_responses=True)
    return redis

async def cache_set(key, value, expire=3600):
    r = await get_redis()
    await r.set(key, value, ex=expire)

async def cache_get(key):
    r = await get_redis()
    return await r.get(key)
