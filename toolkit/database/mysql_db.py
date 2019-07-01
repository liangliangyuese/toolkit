# -*-coding:utf-8-*-
import sys, os, pymysql

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


class MysqlDb(object):
    # TODO 本机只能使用127.0.0.1链接数据库，不能使用本机IP链接
    # 连接MySQL数据库，初始化IP，数据库
    def __init__(self, database, host, port, user='root', password='123456', charset='utf8mb4'):
        self.conn = pymysql.connect(database=database, host=host, port=port, user=user, password=password,
                                    charset=charset)
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


# 数据库连接池

if __name__ == "__main__":
    pass

