'''
模糊定位
有时候一个链接文本很长，如果全部输入比较麻烦，并且不美观
就可以用模糊定位，截取一部分  find_element.by.PARTIAL_LINK_TEXT
如果能匹配多个，只会点击匹配到的第一个
所以在使用的时候需要特别注意，要保证模糊搜索的唯一性
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
# 比如百度一下首页有个登录按钮
search_input = driver.find_element(By.PARTIAL_LINK_TEXT, '创新')
search_input.click()
time.sleep(3)
driver.quit()