'''
xpath元素定位  //*[@id="hotsearch-content-wrapper"]/li[4]/a/span[2]
前几种定位方式 id、name、class、tag、link、模糊   比较理想，需要每个元素都有一个唯一的id/name...
但实际中，元素可能没有id，name，class，刷新页面就会改变
xpath定位方式
1.路径定位--绝对路径、相对路径
    绝对路径：例如，/html/body/div/p[2]
        是以   /   开始
        通过浏览器查看元素属性，右键赋值xpath快速生成
    相对路径(一般配合属性来区分)：例如，//*[@id="kw"]
        是以   //  开始
        通过浏览器查看元素属性，右键赋值xpath快速生成
2.利用元素属性定位
3.层级与属性结合定位
4.属性与逻辑定位结合
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.baidu.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
search_input = driver.find_element(By.XPATH, '//*[@id="hotsearch-content-wrapper"]/li[4]/a/span[2]')
search_input.click()
time.sleep(3)
driver.quit()


