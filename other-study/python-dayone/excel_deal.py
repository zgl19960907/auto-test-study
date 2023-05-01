'''
读取Excel里面的内容   接口地址，参数，请求方式
读取完成后，放到deal_tq(url, data, method)这个里面
预期结果和实际结果比对，一致则成功，否则失败
'''
import openpyxl


def ex_read():
    workbook = openpyxl.load_workbook('case.xlsx')
    sheet = workbook['Sheet1']
    lista = []
    # print(sheet)
    for i in sheet.values:
        # 类型是int就打印出来
        if type(i[0]) is int:
            lista.append(i)
            # print(i)
    return lista