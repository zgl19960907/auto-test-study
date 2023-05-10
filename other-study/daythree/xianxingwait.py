'''
等待机制：停止当前代码的运行
WebDriverWait类 显性等待类，更为灵活
driver, 实例
timeout, 超时时间
poll_frequency=POLL_FREQUENCY,间隔时间，默认0.5
ignored_exceptions 忽略异常（元组），一旦发生了自己定义的异常，不中断代码继续等待；如果不是，就会直接中断代码
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
search_input = driver.find_element(By.ID, 'kw')
search_input.send_keys('12306')
driver.find_element(By.ID, 'su').click()
locator = (By.XPATH, '//*[@id="title-content"]/span[2]')
'''
方法 until(method, message)
    method--在等待期间，每隔一段时间，就会调用当前的方法，如果不能执行，返回FALSE，否则返回值为正常值
    message--如果超时，抛出TimeoutException，把message传入异常
    
    not_until(method, message) 当某条件不成立则继续执行
'''
WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator), '没获取到对应元素')
# WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(locator), '没获取到对应元素')
print('当前页面元素已经被获取到了')
driver.quit()