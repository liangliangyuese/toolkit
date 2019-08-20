# coding=utf-8
from pytesseract import image_to_string
from PIL import Image


def get_bin_table(threshold=115):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def code_str(image_name):
    img = Image.open(image_name)
    im = img.crop((4, 1, 86, 19))
    im = im.convert('L')  # 图片转换为 灰度图
    bb = im.point(get_bin_table(), "1")
    aa = image_to_string(bb)
    return aa
