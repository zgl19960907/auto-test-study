import requests

'''
一个示例，调用API接口
网页地址  https://www.tianqiapi.com/index/doc?version=v61
'''
url = "https://v0.yiketianqi.com/api"
data = {"appid": "28315316", "appsecret": "TVJ6MAhn", "version": "v61", "city": "北京"}
res = requests.get(url, data)
print(res.json())