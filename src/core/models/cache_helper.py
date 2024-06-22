import json
from typing import Optional
import redis

from src.core.config import settings


class AsyncRedisCache:
    def __init__(
        self,
        host: str = settings.cache.url,
        port: int = settings.cache.port,
        db: int = settings.cache.db,
    ):
        self.redis = redis.asyncio.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )

    async def set(self, key: str, value: dict, expire: int = 10):
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
