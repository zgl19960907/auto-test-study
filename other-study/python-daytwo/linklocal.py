'''
link元素定位
针对文本链接，比如超链接之类的。可以不用管标签，直接通过文本就能定位
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
# 比如百度一下首页有个登录按钮
search_input = driver.find_element(By.LINK_TEXT, '登录')
search_input.click()
time.sleep(3)
driver.quit()