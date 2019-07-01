# coding:utf-8
import xlrd
import xlwt


def read_excel(place, sheet_number, col_data):
    # 打开指定路径的xls文件
    # book = xlrd.open_workbook(u'E:\\网址url.xlsx')
    book = xlrd.open_workbook(place)
    # 获取对应sheet表
    # sheet0 = book.sheet_by_index(0)
    sheet0 = book.sheet_by_index(sheet_number)
    # 获取第一列每行的数据
    # cols = sheet0.col_values(0)
    # for i in cols:
    #     print(i)
    cols = sheet0.col_values(col_data)
    return cols


def write_excel(sheet_name, row, col, content, place):
    # 创建excel，utf-8编码  不压缩内容
    urls = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # 创建一个sheet对象      名字sheet    可以覆盖单元格,默认False
    # sheet = urls.add_sheet('sheet1', cell_overwrite_ok=True)
    sheet = urls.add_sheet(sheet_name, cell_overwrite_ok=True)

    # 添加数据0行 0列 写入的内容
    # sheet.write(0, 0, "www.baidu.com")
    # sheet.write(1, 0, "www.qidian.com")
    # text1 = "中文字体"
    # text2 = "必须解码"
    # sheet.write(2, 0, text1.decode('utf-8'))
    # sheet.write(3, 0, text2.decode('utf-8'))
    sheet.write(row, col, content)
    urls.save(r'e:\test1.xls')
    # urls.save(place)
