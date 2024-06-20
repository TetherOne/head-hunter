import redis.asyncio as redis
import json
from typing import Optional


class AsyncRedisCache:
    def __init__(self, host: str = "hh-redis", port: int = 6379, db: int = 0):
        self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    async def set(self, key: str, value: dict, expire: int = 3600):
        await self.redis.set(key, json.dumps(value), ex=expire)

    async def get(self, key: str) -> Optional[dict]:
        data = await self.redis.get(key)
        if data:
            return json.loads(data)
        return None

    async def delete(self, key: str):
        await self.redis.delete(key)

    async def clear(self):
        await self.redis.flushdb()
