'''
name 元素定位
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url)
# 找到输入框
search_input = driver.find_element(By.NAME, "wd")
# 输入框中输入内容
search_input.send_keys("12306")
time.sleep(1)
# 找到搜索按钮，点击click，因为这个百度一下按钮没有name，所以这里还是用的By.ID
driver.find_element(By.ID, "su").click()
time.sleep(3)
try:
    assert driver.title == "12306_百度搜索"
    print("用例成功")
except Exception as e:
    print("用例失败")
driver.quit()