# -*-coding:utf-8-*-
import sys, os, pymysql
from DBUtils.PooledDB import PooledDB
from DBUtils.PersistentDB import PersistentDB

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


class MysqlConn(object):
    def __init__(self, database, host, port, user, password, flag=False):
        if flag:
            self._pool = PersistentDB(creator=pymysql, maxusage=None, setsession=[], ping=0,
                                      closeable=False, threadlocal=None
                                      , host=host, port=port, user=user, password=password,
                                      database=database,
                                      charset="utf8mb4")  # 根据选择不同使用不同的库
        else:
            self._pool = PooledDB(creator=pymysql, mincached=0, maxcached=10, maxshared=10, maxusage=10000, host=host,
                                  port=port, user=user, password=password, database=database, charset="utf8mb4")

    def getConn(self):
        return self._pool.connection()


class DatabaseExe(object):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def insert(self, insert_sql, params, flag=True):
        # 插入数据，默认为插入单条记录，flag为flase是执行插入多条记录
        # 对数据库发出请求保证连接正常
        self.conn.ping(reconnect=True)
        if flag:
            rows = self.cursor.execute(insert_sql, params)
        else:
            rows = self.cursor.executemany(insert_sql, params)
        self.conn.commit()
        return rows

    def select(self, sql):
        # 查找数据
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def delete_update(self, sql):
        # 删除，更新数据
        self.conn.ping(reconnect=True)
        rows = self.cursor.execute(sql)
        self.conn.commit()
        return rows

    def free(self):
        self.conn.ping(reconnect=True)
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

if __name__ == "__main__":
    conn = MysqlConn('spider', '127.0.0.1', 3306, 'root', '123456')
    for i in range(10):
        mysql = DatabaseExe(conn.getConn())
        print(mysql)
