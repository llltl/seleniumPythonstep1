# 2-10 输入注册用户名字及获取用户信息

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #判断页面是否正常打开的包
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))#返回页面是否正常
email_element=driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))

email_element.send_keys("test@163.com")
print(email_element.get_attribute("value"))  
driver.close()