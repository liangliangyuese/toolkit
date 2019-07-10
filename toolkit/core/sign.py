# coding=utf-8
import time
import hashlib


def sign_id():
    """根据时间戳动态生成加密码
        加密码最多有效时间100秒
    """
    # 时间戳
    t = int(time.time())

    key1 = "老夫聊发少年狂，左牵黄，右擎苍，锦帽貂裘,千骑卷平冈"
    key2 = "会挽雕弓如满月，西北望，射天狼"
    # 获取时间戳的倒数第三位 +1
    # 时间戳倒数第4位的值加1
    number = int(str(t)[:7][-1:]) + 1
    # 时间戳去除末尾三位      字符串切片       字符串切片
    data = str(t)[:7] + key1[number:] + key2[number:]
    # 加密全部为最小值
    m = hashlib.md5(data.encode(encoding="utf-8")).hexdigest().upper()
    return m
