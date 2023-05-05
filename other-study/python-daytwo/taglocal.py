'''
tag定位
By.tag
<> tag HTML的每个元素都是tag，一个tag往往用来定义一类功能
一般很少用这个去定位元素，因为一个html中存在好多好多tag，根本分不清
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
search_input = driver.find_element(By.TAG_NAME, 'input')
time.sleep(1)
search_input.send_keys('12306')
driver.find_element(By.ID, 'su').click()
time.sleep(2)
try:
    assert driver.title == '12306_百度搜索'
    print("成功了")
except Exception as e:
    print("失败了")
driver.quit()