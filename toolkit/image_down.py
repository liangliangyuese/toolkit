# coding=utf-8
import os
import requests
import uuid

# 图片储存路径
os.makedirs("./image/", exist_ok=True)


def image_down(url):
    if "http" not in url:
        url = "http:" + url
    img_name = uuid.uuid4()
    r = requests.get(url)
    with open("./image/" + str(img_name) + ".png", "wb") as f:
        f.write(r.content)
    return os.getcwd() + "\\image\\" + str(img_name) + ".png"
