# coding=utf-8
import os, sys
from functools import wraps
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


def method_examine(func):
    """函数检查器,当函数报错时打印错误
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print("函数报错了")
            print(e)

    return wrapper


if __name__ == '__main__':
    @method_examine
    def a(aa):
        print(int(aa))


    a("sad")
