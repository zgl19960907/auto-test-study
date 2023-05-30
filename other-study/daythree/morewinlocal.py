'''
多窗口打开
selenium在点击某个链接的时候，某些情况下，会新打开一个窗口，这时候就需要进行多窗口切换处理，
否则，元素定位的时候不知道定位的哪个窗口，就会报错
句柄：每个窗口都有一个属性，handle标识窗口。--程序聚焦点在哪个窗口
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://sz.ganji.com/'
driver = webdriver.Chrome()
# driver.maximize_window()  # 最大化窗口
driver.get(url)
driver.implicitly_wait(10)
try:
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/img').click()
    time.sleep(2)
    handle = driver.current_window_handle  # 获取当前窗口的句柄
    print('当前的handle：{}'.format(handle))
    handles = driver.window_handles
    print('handles is {}'.format(handles))
    driver.switch_to.window(handles[1])
    print('切换句柄后的title是:{}'.format(driver.title))
    driver.find_element(By.XPATH, '//*[@id="dataCollectionId"]/div[1]/a/ul[1]/li[1]').click()
    driver.close()
    time.sleep(3)
    driver.switch_to.window(handle)
    print('切换句柄关闭后的title是:{}'.format(driver.title))
except Exception as e:
    print('错误是:{}'.format(e))
finally:
    driver.quit()