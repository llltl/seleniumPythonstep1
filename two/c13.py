#coding=utf-8
# 2-13 如何解决验证码代码实战-裁剪验证码图片并保存
# 安装Pillow库pip install pytesseract --库名：pytesseract
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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

 #把“D:\imooc.png”这张图片命名为一个对象im,然后这个对象就可以调用它的方法crop
im=Image.open("D:/imooc.png") 
img=im.crop((left,top,right,height)) #把这个对象按照一定的坐标去裁剪它裁剪完之后就是一个对象img
img.save("D:/imooc1.png")












# ——————————————————————————————————————————————————————————
# import pytesseract
# from PIL import Image
# from ShowapiRequest import ShowapiRequest
# image=Image.open("D:/imooc1.png")
# text=pytesseract.image_to_string(image)
# print(text)  #由于该图的验证码文字是不规则的，没被识别出来

#用第三方的图片识别api库来识别，地址是https://www.showapi.com/apiGateway/view/2360?tab=1
# r = ShowapiRequest("http://route.showapi.com/2360-1","807905","138396ccfa694517b3ce53b6105baef2" )
# r.addBodyPara("typeID",35)
# r.addBodyPara("conwert_to_jpg",0)
# r.addBodyPara("image",r"D:/img/imooc1")
# res = r.post()
# text = res.json()['showapi_res_body']['msg']
# print(res.text) # 返回信息



