# 2-11 生成随机数
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #判断页面是否正常打开的包
from selenium.webdriver.support.wait import WebDriverWait
for i in range(5):
    user_email=''.join(random.sample('1234567890abcdefg',5)) + "@163.com"        #从1234567890abcdefg里面输出5位数的随机数
    print(user_email)



# element=driver.find_element_by_class_name("controls")
# locator=(By.CLASS_NAME,"controls")
# WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
# email_element=driver.find_element_by_id("register_email")

# print(email_element.get_attribute("placeholder"))

# email_element.send_keys("test@163.com")
# print(email_element.get_attribute("value"))  
# driver.close()

 
