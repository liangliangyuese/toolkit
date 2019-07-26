# -*-coding:utf-8-*-
import pymysql
from DBUtils.PooledDB import PooledDB
from DBUtils.PersistentDB import PersistentDB


class MysqlDb(object):
    def __init__(self, database=None, host="127.0.0.1", port=3306, user='root', password='123456', charset='utf8mb4'):
        self.conn = pymysql.connect(database=database, host=host, port=port, user=user, password=password,
                                    charset=charset)
        self.cursor = self.conn.cursor()
        if database:
            pass
        else:
            raise ValueError("初始化失败，缺少关键字参数database")

    def insert(self, insert_sql, params, flag=True):
        self.conn.ping(reconnect=True)
        if flag:
            rows = self.cursor.execute(insert_sql, params)
        else:
            # 同时插入多组数据
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


class MysqlConn(object):
    def __init__(self, database, host="127.0.0.1", port=3306, user="root", password="123456", pool=None):
        if not pool:
            raise ValueError("构建数据库链接池失败，请选择使用正确的链接池类型")
        else:
            if pool == "PersistentDB":
                print("---使用PersistentDB构建线程专用数据库连接---")
                self._pool = PersistentDB(creator=pymysql, maxusage=None, setsession=[], ping=0,
                                          closeable=False, threadlocal=None
                                          , host=host, port=port, user=user, password=password,
                                          database=database,
                                          charset="utf8mb4")
            elif pool == "PooledDB":
                print("---使用PooledDB构建线程共用数据库连接---")
                self._pool = PooledDB(creator=pymysql, mincached=0, maxcached=10, maxshared=10, maxusage=10000,
                                      host=host,
                                      port=port, user=user, password=password, database=database, charset="utf8mb4")
            else:
                raise ValueError("构建数据库链接池失败，请选择使用正确的链接池类型")

    def get_conn(self):
        return self._pool.connection()


class MysqlExe(object):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def insert(self, insert_sql, params, flag=True):
        self.conn.ping(reconnect=True)
        if flag:
            rows = self.cursor.execute(insert_sql, params)
        else:
            rows = self.cursor.executemany(insert_sql, params)
        self.conn.commit()
        return rows

    def select(self, sql):
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql)
        print(self.conn)
        result = self.cursor.fetchall()
        return result

    def delete_update(self, sql):
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
    Conn = MysqlConn(database="api", pool="PooledDB")
    mysql1 = MysqlExe(Conn.get_conn())
    mysql1.select("select * from api_data where id<2")


