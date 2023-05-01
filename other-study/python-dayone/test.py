from deal_data import deal_tq

res = deal_tq('https://v0.yiketianqi.com/api',
              {"appid": "28315316", "appsecret": "TVJ6MAhn", "version": "v61", "city": "北京"}, 'get')
print(res.json())