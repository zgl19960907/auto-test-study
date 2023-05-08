'''
seleinum等待机制 --因为有可能出现Message: no such element: Unable to locate element这种报错
出现原因：刚点击完跳转页面后，直接元素定位就经常失败
强制等待：time.sleep(秒数)   这种方式存在很大缺陷
隐式等待：implicitly_wait(秒数)  设置一个  最长等待时间  ，如果在规定时间内，网页加载完成，那就执行下一步，否则一直等到时间截止，
然后执行下一步。   --存在缺陷：程序会一直等待整个页面加载完成

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