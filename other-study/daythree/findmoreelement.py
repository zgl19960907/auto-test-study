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


# url = 'https://www.12306.cn/index/'
# driver = webdriver.Chrome()
# # driver.maximize_window()  # 最大化窗口
# driver.get(url)
# driver.implicitly_wait(20)
#
# try:
#     inabc_click = driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[4]/ul/li[4]/a/i')
#     time.sleep(2)
#     inabc_click.click()
#     assert driver.title == '中国铁路12306网站'
#     print('找到了')
#     driver.back()
#     time.sleep(5)
# except Exception as e:
#     print("出错了，错误是：{}".format(e))
# finally:
#     driver.quit()

url = 'https://www.12306.cn/index/'
driver = webdriver.Chrome()
# driver.maximize_window()  # 最大化窗口
driver.get(url)
driver.implicitly_wait(30)
# 获取一个列表
menu_list = driver.find_elements(By.XPATH, '//*[@id="toolbar_Div"]/div[4]/div[3]/div[2]/ul/li')
print("快捷小功能数量：{}".format(len(menu_list)))
try:
    # 循环遍历点击返回
    for onemenu in range(len(menu_list)-1):
        '''
         为什么要加下面这行？为了防止ABA问题,因为经过第一次点击->back()之后，
         会认为原来的元素已经过期(不在安全)，然后清空原来的元素，会出现下面的报错。
         Message: stale element reference: element is not attached to the page document
         但是这样有点问题，如果需要遍历的元素比较多，很大可能会出现list index out of range
        '''
        menu_list = driver.find_elements(By.XPATH, '//*[@id="toolbar_Div"]/div[4]/div[3]/div[2]/ul/li')
        time.sleep(2)
        menu_list[onemenu].click()
        # time.sleep(2)
        assert driver.title == '中国铁路12306网站'
        print('测试通过')
        time.sleep(1)
        driver.back()
except Exception as e:
    print("出错了，错误是：{}".format(e))
finally:
    driver.quit()