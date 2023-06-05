import base64
import hashlib
import time

import requests

'''
requests的get方法
请求-get方法
响应：
    响应对象.url   获取请求url
    响应对象.status_code  获取响应状态码
    响应对象.text  以文本形式显示响应内容
解决乱码问题：
    响应对象.encoding  查看默认请求编码格式
    响应对象.encoding=编码格式  设置相应编码格式

post请求-post方法(一般用来提交资源、新增资源)
requests.post(url, json, headers)
    url:接口地址
    json:请求参数
    headers:请求头信息
获取响应对象：
    响应对象.status_code  响应状态码
    响应对象.json()  以json格式查看响应内容
'''
# url = 'https://www.baidu.com'
# re = requests.get(url)
# print("请求地址", re.url)
# print("响应状态码", str(re.status_code))
# print("响应内容", re.text)

# requests.post(url, data=)  #这里的参数一般使用data=，这样会防止敏感信息暴露
# md5加密
tokenStr = 'jiayouzglyouarebest'
md5Str = hashlib.md5()
t = str(round(time.time()*1000)) # 获取当前时间的毫秒数去掉小数点
conn = t + tokenStr
md5Str.update(conn.encode('utf-8'))
print(md5Str.hexdigest())

# base64加密
base64Str = base64.b64encode(str(md5Str.hexdigest()).encode('utf-8')).upper()
print(str(base64Str, encoding='utf-8'))