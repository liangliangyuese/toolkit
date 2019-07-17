# coding=utf-8
import pymongo


class Mongodb(object):
    def __init__(self, database, collection, host="127.0.0.1", port=27017):
        self.conn = pymongo.MongoClient(host=host, port=port)
        self.db = self.conn[database]
        self.collection = self.db[collection]

    def insert(self, data):
        self.collection.insert_many(data)

    def update_delete(self, data):
        self.collection.find_one(data)

    def select(self, data, sort=None):
        self.collection.find_one(data)

    def count(self):
        print("统计集合内的数据量")
        print(self.collection.count())


if __name__ == '__main__':
    mongodb = Mongodb("spider", "films")
    mongodb.count()
