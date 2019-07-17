# coding:utf-8
# import pymongo
# '''连接mongodb数据库'''
# # 连接数据库
# client = pymongo.MongoClient('localhost', 27017)
# # 数据库名称
# db = client.spider
# # 连接的集合
# collection = db.film
# def insert(insert_data):
#     collection.insert(insert_data)


class A(object):
    def a(self):
        return self.__class__.__name__


a = A()
print(a.a())
