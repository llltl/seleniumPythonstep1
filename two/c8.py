# coding:utf-8
#2-8
#使用定位方式来判断页面元素是否存在
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(3)
locator = (By.XPATH, "//*[@id='head']")  # CSDN页面【头部】head的xpath
ele_exist = EC.visibility_of_element_located(locator)  # 判断元素是否存在
print(ele_exist)  # 打印结果：<function visibility_of_element_located.<locals>._predicate at 0x000002C789F4B160>
WebDriverWait(driver, 3).until(ele_exist)#找until里面的内容找3秒钟。（判断页面元素在1s内是否找到,找到后往下进行,没找到就返回false）
if ele_exist:
    print("【头部】head这个元素存在，页面返回正确！")
time.sleep(3)
driver.quit()  # 等待3s关闭浏览器







# 1.调用 visibility_of_element_located(locator) 这个方法的目的是为了在输入框输入
# 内容之前判断该元素是否可见，若元素可见，则输入内容，不可见就报错。
# 2.此处引入from selenium.webdriver.support import expected_conditions as EC
'''
调用 visibility_of_element_located(locator) 这个方法的目的是为了在输入框输入内容之前判断该元素是否可见，若可见，则进行输入内容，不可见就报错。

调用这个方法需要引入 expected_conditions、WebDriverWait、By 这三个包
调用该方法的语法：
lacator=(BY.ID,"")
WebDriverWait(driver,10).unitl（EC.visibility_of_element_located(locator)）

该方法比普通 的find_element定位元素更加友好
'''