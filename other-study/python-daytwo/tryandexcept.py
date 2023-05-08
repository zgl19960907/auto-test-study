'''
异常：程序执行不下去，中断当前程序，并抛出异常
常用的有
try:
    可能出问题的代码
except 描述异常类型:
    出现异常后执行这里 --异常处理方案
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(100)  # 隐式等待，针对driver设置等待时间
time.sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, '#kw')
search_input.send_keys('12306')
click_btn = driver.find_element(By.CSS_SELECTOR, '#su')
click_btn.click()
# time.sleep(3)  # 强制等待
elem = driver.find_element(By.XPATH, '//*[@id="1"]/div/div[1]/h3/a[1]')
try:
    assert elem != None
    print("Success!")
except Exception as e:
    print("Failed!")
time.sleep(3)
driver.quit()