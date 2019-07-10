# coding=utf-8
import os
import requests

# 图片储存路径
os.makedirs("./image/", exist_ok=True)


def image_down(url, image_name):

    """图片下载模块
    url:图片下载路径
    image_name:图片存储名称
    """
    r = requests.get(url)
    with open("./image/" + image_name + ".png", "wb") as f:
        f.write(r.content)
