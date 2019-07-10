# coding:utf-8
import redis
import sys
import os

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


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


if __name__ == "__main__":
    a = MyRedis(2)
    d = a.count_key()
    s = 200
    print(s - d)
    print((s - d) / s)
