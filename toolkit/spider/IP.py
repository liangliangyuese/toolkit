# coding=utf-8
import sys, os, re, requests, time
import urllib3
from lxml import etree
from spider.spider_rule import spider_re
from spider.settings import random_agent
from database.mysql_db import MysqlDb
from function.decorator import method_examine

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 禁用警告
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


class Ip(MysqlDb):
    """IP类，插入ip，删除ip"""

    def __init__(self, database, host, port):
        self.mysql_db = MysqlDb.__init__(self, database, host, port)

    @method_examine
    def save_ip(self, ip, port_number):
        """插入ip"""
        sql = "insert into ip(ip,port) values (%s,%s)"
        data = [ip, port_number]
        res = MysqlDb.insert(self, sql, data)
        return res

    @method_examine
    def clear_ip(self, ip, port_number):
        """清除ip"""
        sql = "delete from ip where ip='{}' and port='{}'".format(ip, port_number)
        res = MysqlDb.delete_update(self, sql)
        return res

    @method_examine
    def get_ip(self):
        """获取ip(从数据库中获取IP)"""
        sql = "select ip,port from ip order by id;"
        res = MysqlDb.select(self, sql)
        return res

    @method_examine
    def ip_examine(self):  # IP检测，清除失效IP
        all_ip = self.get_ip()
        print("开始检测IP")
        for i in all_ip:
            print(i)
            proxies = {
                "http": "http://{}:{}".format(i[0], i[1]),
                "https": "http://{}:{}".format(i[0], i[1])
            }
            url = "http://ip.90rl.com/"
            try:
                res = requests.get(url, headers=random_agent(), proxies=proxies, timeout=5)
                print(res.status_code)
                print("可用IP")
            except (requests.exceptions.ConnectTimeout, requests.exceptions.ProxyError, requests.exceptions.ReadTimeout,
                    requests.exceptions.SSLError):
                print("失效IP")
                self.clear_ip(i[0], i[1])
            except requests.exceptions.ChunkedEncodingError:
                print("数据读取错误")
                self.clear_ip(i[0], i[1])
            except requests.exceptions.ConnectionError:
                print("网络状态不稳定/dns异常")
                self.clear_ip(i[0], i[1])


class IPSpider(Ip):
    def __init__(self):
        self.ip = Ip.__init__(self, "spider", "127.0.0.1", 3306)

    @method_examine
    def kuaidaili(self):
        """快代理"""
        for i in range(1, 21):
            url = "https://www.kuaidaili.com/free/inha/{}/".format(i)
            rule = '<td data-title="IP">(.*?)</t.*?e="PORT">(.*?)</td>'
            con = spider_re(url, rule)
            for z in con:
                print(z)
                Ip.save_ip(self, z[0], z[1])
            time.sleep(1)

    @method_examine
    def zdaye(self):
        """站大爷
        """
        url = "http://ip.zdaye.com/dayProxy/{}/{}/1.html".format(time.strftime("%Y"), time.strftime("%m"))
        rule = 'div class="title"><a href="(.*?)">'
        the_head = random_agent()
        # TODO cookie 生成研究
        the_head[
            'Cookie'] = "acw_tc=76b20f6a15501144654263861e7e5fc647d94140f582e23d95236f2292be0b; ASPSESSIONIDASTASBSQ=JPCMBECDLPNBGKJLFNFIEJBL; __51cke__=; ASPSESSIONIDCQTDQATQ=PNMFCLCDNPMNDENJJIAGHLGF; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1550114479,1550209479,1550211987; acw_sc__v2=5c665c4627456e6bb4b5d6dac345c9d9277822d5; ASPSESSIONIDCSTDRBTR=NOKLCCDDHCBBELIPLCEGOKDK; __tins__16949115=%7B%22sid%22%3A%201550214435995%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201550216235995%7D; __51laig__=7; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1550214436"
        res = requests.get(url, headers=the_head, verify=False, timeout=10).text.encode('ISO-8859-1').decode('gbk')
        print(res)
        con = re.findall(rule, res, re.S)
        print(con)
        base_url = 'http://ip.zdaye.com'
        rule2 = ''
        for i in con:
            url = base_url + i
            print(url)
            res = requests.get(url, headers=the_head, verify=False, timeout=10).text.encode('ISO-8859-1').decode('gbk')
            print(res)
            break

    @method_examine
    def bajiuip(self):
        for i in range(1, 21):
            url = "http://www.89ip.cn/index_{}.html".format(i)
            response = requests.get(url, headers=random_agent(), verify=False, timeout=10)
            target_html = etree.HTML(response.content.decode("utf-8", errors="ignore"))
            ip_rule = '//tr[position()]/td[1]/text()'
            port_rule = '//tr[position()]/td[2]/text()'
            content1 = target_html.xpath(ip_rule)
            content2 = target_html.xpath(port_rule)
            for z, x in zip(content1, content2):
                print(z, x)
                Ip.save_ip(self, z.strip(), x.strip())
            time.sleep(1)

    @method_examine
    def wuuip(self):
        url = "http://www.data5u.com/free/gngn/index.shtml"
        rule = '<span><li>([0-9\.]*?)</li>.*?style="width: 100px;"><li class=.*?>(.*?)<'
        con = spider_re(url, rule)
        for z in con:
            print(z)
            Ip.save_ip(self, z[0], z[1])

    @method_examine
    def xici(self):
        url = "https://www.xicidaili.com/nn/"
        response = requests.get(url, headers=random_agent(), verify=False, timeout=10)
        ip_rule = "//tr[position()]/td[2]/text()"
        port_rule = "//tr[position()]/td[3]/text()"
        target_html = etree.HTML(response.content.decode("utf-8", errors="ignore"))
        content1 = target_html.xpath(ip_rule)
        content2 = target_html.xpath(port_rule)
        for z, x in zip(content1, content2):
            print(z, x)
            Ip.save_ip(self, z.strip(), x.strip())

    @method_examine
    def all_spider(self):
        self.kuaidaili()
        self.bajiuip()
        self.wuuip()


if __name__ == '__main__':
    ip = Ip('spider', '127.0.0.1', 3306)
    # ip.ip_examine()
    ip.clear_ip("127.0.0.1", "555")
