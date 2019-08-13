# -*- coding:utf-8 -*-
import base64
import time
from Crypto.Cipher import AES
t = int(time.time())
# TODO Crypto库 安装有问题，待解决

def add_str(text):
    length = 16  # aes加密的key长度为16位，24位，32位中的一种。key16位，加密的的明文为16的倍数
    count = len(text.encode('utf-8'))  # 计算长度时使用utf-8编码，一个中文3个长度
    if count % length != 0:
        add = length - (count % length)
    else:
        add = 0
    text = text + ('\0' * add)
    return str.encode(text)  # 返回bytes


def my_aes_encrypted(text):
    key = "my_passwordKey16"  # 设置key 长度为16
    aes = AES.new(add_str(key), AES.MODE_ECB)  # 传入key，选择加密模式
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_str(text))), encoding="utf-8").replace("\n", "")
    print(encrypted_text)
    return encrypted_text


def my_aes_decrypted(text):
    key = "my_passwordKey16"
    aes = AES.new(add_str(key), AES.MODE_ECB)
    text_decrypted = str(aes.decrypt(base64.decodebytes(bytes(text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))
    print(text_decrypted)
    return text_decrypted



