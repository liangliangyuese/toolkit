# coding:utf-8
import redis
#

class MyRedis(object):
    def __init__(self, db, host="127.0.0.1", port=6379, password='123456'):
        self.redis_conn = redis.StrictRedis(host=host, port=port, decode_responses=True, password=password, db=db)

    def all_key(self):
        return self.redis_conn.keys()

    def insert(self, key, value):
        return self.redis_conn.set(key, value)

    def key_over(self, key, time):
        return self.redis_conn.expire(key, time)

    def search(self, key):
        return self.redis_conn.get(key)

    def clear_key(self, key):
        return self.redis_conn.delete(key)

    def count_key(self):
        return self.redis_conn.dbsize()


class RedisConn:
    def __init__(self, db, host="127.0.0.1", port=6379, password='123456'):
        self.pool = redis.ConnectionPool(host=host, port=port, decode_responses=True, password=password, db=db)

    def get_conn(self):
        return redis.StrictRedis(connection_pool=self.pool)


class RedisExe:
    def __init__(self, conn):
        self.conn = conn

    def all_key(self):
        return self.conn.keys()

    def insert(self, key, value):
        return self.conn.set(key, value)

    def key_over(self, key, time):
        return self.conn.expire(key, time)

    def search(self, key):
        return self.conn.get(key)

    def clear_key(self, key):
        return self.conn.delete(key)

    def count_key(self):
        return self.conn.dbsize()


if __name__ == "__main__":
    print("具体使用用例可参考mysql")
