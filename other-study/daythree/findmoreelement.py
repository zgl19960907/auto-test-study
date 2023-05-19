'''
页面查找多个元素
1、功能测试用例 -- 移交自动化
2、自动化组，对用例进行筛选（把那些性价比低的剔除，比如轮播图）
3、编写脚本
4、转换成自动化用例
5、执行并输出测试报告

定位多个元素，可以使用这个：find_elements_byxxx 获取同样条件下的一组元素
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
# driver.maximize_window()  # 最大化窗口
driver.get(url)
driver.implicitly_wait(20)
search_input = driver.find_element(By.ID, 'kw')
search_input.send_keys("12306")
btn_click = driver.find_element(By.ID, 'su')
btn_click.click()

try:
    link_local = driver.find_element(By.XPATH, '//*[@id="1"]/div/div[1]/h3/a[1]')
    link_local.click()
    assert link_local != '中国铁路12306网站'
    print('找到了')
    time.sleep(5)
    driver.back()
except Exception as e:
    print("出错了，错误是：{}".format(e))
finally:
    driver.quit()