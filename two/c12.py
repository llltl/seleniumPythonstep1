# 2-12 裁剪验证码图片的思路
# 安装Pillow库pip install Pillow  --库名：PIL

from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #判断页面是否正常打开的包
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))#返回页面是否正常
email_element=driver.find_element_by_id("register_email")
driver.save_screenshot("D:/imooc.png") #获取整个网页的图片
code_element=driver.find_element_by_id("getcode_num")  #定位到验证码图片的元素
print(code_element.location)       #打印验证码图片的坐标为：{'x': 552, 'y': 527}
left=code_element.location['x']
top=code_element.location['y']
right=code_element.size['width']+left
height=code_element.size['height']+top
im=Image.open("D:/imooc.png") #打开图片
img=im.crop((left,top,right,height))
img.save("D:/imooc1.png")



# for i in range(5):
#     user_email=''.join(random.sample('1234567890abcdefg',5)) + "@163.com"        #从1234567890abcdefg里面输出5位数的随机数
#     print(user_email)



# element=driver.find_element_by_class_name("controls")
# locator=(By.CLASS_NAME,"controls")
# WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
# email_element=driver.find_element_by_id("register_email")

# print(email_element.get_attribute("placeholder"))

# email_element.send_keys("test@163.com")
# print(email_element.get_attribute("value"))  
# driver.close()