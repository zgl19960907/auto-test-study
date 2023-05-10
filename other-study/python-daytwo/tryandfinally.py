'''
try...finally...
无论是否有异常，finally中的代码一定会执行
'''
import time

from selenium import webdriver

msg = 'Hello Orange'
url = 'https://www.baidu.com/'
driver = webdriver.Chrome()

try:
    print(msg[1])
    driver.get(url)
    time.sleep(5)
    assert 1 == 0
except Exception as e:
    print('只要有异常，就会走这里')
finally:
    driver.quit()
    print('无论是否有异常，都会走这里')