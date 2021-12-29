

# coding:utf-8
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
WebDriverWait(driver, 3).until(ele_exist)
if ele_exist:
    print("【头部】head这个元素存在，页面返回正确！")
time.sleep(3)
driver.quit()  # 等待3s关闭浏览器