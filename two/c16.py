#coding=utf-8
# 2-16 注册输入验证码流程整合
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import ddddocr 

'''裁剪验证码并保存'''
driver=webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))
# email_element=driver.find_element_by_id("register_email")
driver.save_screenshot("D:/imooc.png")
code_element=driver.find_element_by_id("getcode_num") #验证码图片的id
print(code_element.location) #打印x\y的坐标,'x': 1002, 'y': 527
left=code_element.location['x'] #x值
top=code_element.location['y']  #y值
right=code_element.size['width']+left  #图片的宽度加left等于图片右边的点
height=code_element.size['height']+top  #图片的高度加

'''把“D:\imooc.png”这张图片命名为一个对象im,然后这个对象就可以调用它的方法crop'''
im=Image.open("D:/imooc.png") 
img=im.crop((left,top,right,height)) #把这个对象按照一定的坐标去裁剪它裁剪完之后就是一个对象img
img.save("D:/imooc1.png")

'''识别验证码并输入'''
ocr=ddddocr.DdddOcr()
with open(r'D:\imooc1.png', 'rb') as f:
    img_bytes=f.read()
 
res=ocr.classification(img_bytes)
print(res)
time.sleep(3)
driver.find_element_by_id('captcha_code').send_keys(res)
time.sleep(20)
driver.close()