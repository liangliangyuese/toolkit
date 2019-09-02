# coding=utf-8
import time

from datetime import datetime, timedelta


def week_date(target_year, target_week):
    """返回目标周，周一-周日的日期"""
    start = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime('{}-{}-1'.format(target_year, target_week), '%Y-%W-%w'))
    start_date = datetime.strptime(start[:10], "%Y-%m-%d")
    end = (start_date + timedelta(days=+6)).strftime("%Y-%m-%d") + " 00:00:00"
    return [target_week, start, end]


def getBetweenDay(begin_date, end_date):
    """返回范围内时间"""
    date_list = []
    begin_date = datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += timedelta(days=1)
    return date_list
