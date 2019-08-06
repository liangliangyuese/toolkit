# coding=utf-8
import os
import sys
import requests
import re
import urllib3
from toolkit.spider.settings import random_agent
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


def spider(url):
    res = requests.get(url, headers=random_agent(), verify=False, timeout=10).text
    print(res)


def spider_xpath(url, xpath, encoding="utf-8"):
    # xpath规则采集
    res = requests.get(url, headers=random_agent(), verify=False, timeout=10)
    target_html = etree.HTML(res.content.decode(encoding, errors="ignore"))
    content = target_html.xpath(xpath)
    return content


def spider_re(target_url, re_rule, encoding="utf-8"):
    # 正则规则采集
    res = requests.get(url=target_url, headers=random_agent(), verify=False, timeout=10)
    con = res.content.decode(encoding, errors='ignore')
    content = re.findall(re_rule, con, re.S)
    return content


if __name__ == "__main__":
    pass
