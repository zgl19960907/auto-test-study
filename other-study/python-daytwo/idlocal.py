'''
id元素定位
导包小tips：
import   一般用来导入简单的包，类比较少
from ... import ... 一般用来导入复杂的包，多个类，每个类都有自己的方法
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# webUI搜索功能
# 加载驱动,这个只有在老的selenium版本中才能用，新版的好像已经去除这个功能了(这里安装的selenium是4.1.1)
# driver_path = Service(r"F:\pythonProject\auto-test-study\venv\Scripts\chromedriver.exe")
# 打开浏览器


driver = webdriver.Chrome()
# 输入网址
driver.get('https://www.baidu.com/')
time.sleep(1)
# 找到元素，通过id
search_input = driver.find_element(By.ID, 'kw')
time.sleep(1)
# 输入关键字
search_input.send_keys("12306")
time.sleep(1)
# 点击搜索
driver.find_element(By.ID, "su").click()
time.sleep(1)
# 验证结果  可以通过断言去验证
"""
断言 判断一个表达式（true/false）
返回是False  触发异常
特性：条件不满足直接返回错误，不必再运行了
"""
try:
    time.sleep(1)
    assert driver.title == "12306_百度搜索"
    print('成功')
except Exception as e:
    print('失败')


