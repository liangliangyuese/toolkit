# coding:utf-8
import xlrd
import xlwt


def read_excel(place, sheet_number, method=None):
    # place excel文件位置
    # sheet_number读取指定sheet从0开始计数
    # row 行模式 返回每行的数据
    # col 列模式 返回每列的数据
    data = []
    book = xlrd.open_workbook(place)
    sheet = book.sheet_by_index(sheet_number)
    if method == "row":
        rows = sheet.nrows  # 获取行数
        for r in range(rows):  # 读取每一行的数据
            val = sheet.row_values(r)
            data.append(val)
        return data
    elif method == "col":
        cols = sheet.ncols  # 获取列数
        for r in range(cols):  # 读取每一列的数据
            val = sheet.col_values(r)
            data.append(val)
        return data
    else:
        raise ValueError("请使用正确的参数 row or col")


def write_excel(sheet_name, place, data, method=None, ):
    # sheet_name 生成excel的sheet名称
    # place 生成excel的wei'zhi
    # 创建excel，utf-8编码  不压缩内容
    urls = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建一个sheet对象      名字sheet    可以覆盖单元格,默认False
    sheet = urls.add_sheet(sheet_name, cell_overwrite_ok=True)
    if method == "row":  # 数据按行写入
        rows = len(data)
        for i in range(rows):
            for z in range(len(data[i])):
                sheet.write(i, z, data[i][z])
    elif method == "col":  # 数据按列写入
        cols = len(data)
        for i in range(cols):
            for z in range(len(data[i])):
                sheet.write(z, i, data[i][z])
    else:
        raise ValueError("请使用正确的参数 row or col")

    urls.save(place)
