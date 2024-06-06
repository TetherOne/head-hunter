import redis


class RedisService:
    def __init__(
        self,
        host="hh-redis",
        port=6379,
        db=0,
    ):
        self.redis_conn = redis.Redis(
            host=host,
            port=port,
            db=db,
        )

    def set_data(self, key, value):
        self.redis_conn.set(key, value)

    def get_data(self, key):
        return self.redis_conn.get(key)

    def delete_data(self, key):
        self.redis_conn.delete(key)


redis_service = RedisService()
