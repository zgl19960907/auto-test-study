'''
class元素定位
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# URL
url = 'https://www.baidu.com/'
# driver
driver = webdriver.Chrome()
driver.get(url)
# 输入框
search_input = driver.find_element(By.CLASS_NAME, 's_ipt')
# 输入内容
search_input.send_keys('12306')
time.sleep(1)
# 点击搜索按钮
driver.find_element(By.CLASS_NAME, 's_btn').click()
time.sleep(1)
# 断言
try:
    assert driver.title == '12306_百度搜索'
    print("根据class定位成功")
except Exception as e:
    print("根据class定位成功")
time.sleep(2)
# 退出
driver.quit()