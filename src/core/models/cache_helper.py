import json
from datetime import datetime
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
        value = json.dumps(value, default=str)
        await self.redis.set(key, value, ex=expire)

    async def get(self, key: str) -> Optional[dict]:
        data = await self.redis.get(key)
        if data:
            return json.loads(data, object_hook=self._datetime_parser)
        return None

    @staticmethod
    def _datetime_parser(d):
        for k, v in d.items():
            try:
                d[k] = datetime.fromisoformat(v)
            except (TypeError, ValueError):
                pass
        return d

    async def delete(self, key: str):
        await self.redis.delete(key)

    async def clear(self):
        await self.redis.flushdb()
