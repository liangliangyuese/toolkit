# coding:utf-8
import random
import datetime
import sys
import os

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


def random_agent():
    all_headers = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60 ",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 ",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0 ",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    ]
    # 请求头按需配置
    headers = {
        'Connection': 'close',
        "User-Agent": random.sample(all_headers, 1)[0]}
    return headers


def now_time():
    # 这周一的日期
    week_num = datetime.datetime.now().weekday()
    now_monday = datetime.datetime.now() + datetime.timedelta(days=-week_num)
    now_monday = str(now_monday)[0:10]
    return now_monday


def old_time():
    # 上周一
    week_num = datetime.datetime.now().weekday() + 7
    yes_monday = datetime.datetime.now() + datetime.timedelta(days=-week_num)
    yes_monday = str(yes_monday)[0:10]
    return yes_monday
