# coding:utf-8
import base64
from Crypto.Cipher import AES


class AESEncryption(object):
    def __init__(self, length, key):
        if length == 16 or length == 24 or length == 32:
            if len(key) == length:
                self.length = length
                self.key = key
            else:
                raise ValueError("aes加密的key长度为16位，24位，32位中的一种。key长度应与预期长度相等")
        else:
            raise ValueError("aes加密的key长度为16位，24位，32位中的一种。key为多少位，明文需要为key的倍数")

    # 加密
    def add_str(self, text):
        count = len(text.encode('utf-8'))  # 计算长度时使用utf-8编码，一个中文3个长度
        if count % self.length != 0:
            add = self.length - (count % self.length)
        else:
            add = 0
        text = text + ('\0' * add)
        return str.encode(text)  # 返回bytes

    # 加密
    def aes_encrypted(self, text):
        aes = AES.new(self.add_str(self.key), AES.MODE_ECB)  # 传入key，选择加密模式
        encrypted_text = str(base64.encodebytes(aes.encrypt(self.add_str(text))), encoding="utf-8").replace("\n", "")
        print(encrypted_text)
        return encrypted_text

    # 解密
    def aes_decrypted(self, text):
        aes = AES.new(self.add_str(self.key), AES.MODE_ECB)
        text_decrypted = str(aes.decrypt(base64.decodebytes(bytes(text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))
        print(text_decrypted)
        return text_decrypted


# 哈希加密
def hashlib_text(text, type__="md5"):
    import hashlib
    if type__ in ["blake2b", "blake2s", "md5", "sha1", "sha224", "sha256", "sha384", "sha3_224", "sha3_256", "sha3_384",
                  "sha3_512", "sha512"]:
        text = text.encode('utf-8')
        return eval("hashlib.{}({}).hexdigest()".format(type__, text))
    else:
        raise ValueError("请使用正确的哈希加密方式")


