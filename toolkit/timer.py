# coding=utf-8
import datetime


class Timer(object):
    @staticmethod
    def target_time(int_):
        return datetime.datetime.now() + datetime.timedelta(days=int_)

    @staticmethod
    def get_week():
        # 获取本周是星期几
        week_num = datetime.datetime.now().weekday()
        return week_num


print(datetime.datetime.now() + datetime.timedelta(days=-1))
