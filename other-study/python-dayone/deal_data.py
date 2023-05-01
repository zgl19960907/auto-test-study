import requests

'''
将处理api天气接口封装成一个方法,需要传几个参数
'''
def deal_tq(url, data, method):
    if 'post' == method:
        res = requests.post(url, data)
    elif 'get' == method:
        str_data = eval(data)
        res = requests.get(url, str_data)
    return res