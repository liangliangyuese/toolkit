# coding=utf-8
import datetime


class Timer(object):
    def target_time(self, int_):
        return datetime.datetime.now() + datetime.timedelta(days=int_)

    def get_week(self):
        # 获取本周是星期几
        week_num = datetime.datetime.now().weekday()
        return week_num
print(datetime.datetime.now() + datetime.timedelta(days=-1))