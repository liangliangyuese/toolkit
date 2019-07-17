# coding=utf-8
import pymongo


# 连接本地mongodb数据库
# mongo_conn = pymongo.MongoClient('127.0.0.1', 27017)
# # 连接my_spider数据库，没有的话会自动创建
# db = mongo_conn.my_spider


class Mongodb(object):
    def __init__(self, host, port):
        self.mongo_conn = pymongo.MongoClient(host, port)

    # 获取类名，创建表名字,新类继承旧mongodb类
    @classmethod
    def db_path(cls):
        return cls.__name__

    # 构造实例
    @classmethod
    def new(cls, *args, **kwargs):
        i = cls(*args, **kwargs)
        # setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在。
        # getattr()函数用于返回一个对象属性值。
        setattr(i, '_id', kwargs['_id'])
        return i

    # 遍历查看对应数据库里所有的键值对
    @classmethod
    def all(cls):
        path = cls.db_path()
        d = db[path].find()
        return [cls.new(**i) for i in d]

    # 查看单个键值对
    @classmethod
    def get(cls, *args, **kwargs):
        path = cls.db_path()
        d = db[path].find_one(kwargs)
        if d:
            return cls.new(**d)

    # 过滤，如果值在数据库中存在，就不再插入
    @classmethod
    def filter(cls, **kwargs):
        path = cls.db_path()
        d = db[path].find(kwargs)
        return [cls.new(**i) for i in d]

    # 存在时更新，不存在时创建
    def save(self):
        path = self.db_path()
        # hasattr() 函数用于判断对象是否包含对应的属性。
        if not hasattr(self, '_id'):
            db[path].insert_one(self.__dict__)
        else:
            db[path].update_one({'_id': self._id}, {'$set': self.__dict__})

    # 删除
    def delete(self):
        path = self.db_path()
        # hasattr() 函数用于判断对象是否包含对应的属性。
        if hasattr(self, '_id'):
            a = db[path].delete_one({'_id': self._id})

    # repr 重构显示方法,返回类方法名
    def __repr__(self):
        return self.__class__.__name__


if __name__ == '__main__':
    class User(Mongodb):
        def __init__(self, **kwargs):
            self.name = kwargs.get('name', '')
    u = User(name='小明')
    u.save()
    u = User.get(name='小明')
    u.delete()
    print(User.get(name='小明'))
    print(u.db_path())
