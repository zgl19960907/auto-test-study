'''
css 定位方式
相对于xpath简介
css层级关系
    # 表示 id
    . 表示 class
    > 表示 子元素层级
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, '#kw')
search_input.send_keys('12306')
click_btn = driver.find_element(By.CSS_SELECTOR, '#su')
click_btn.click()
time.sleep(3)
driver.quit()