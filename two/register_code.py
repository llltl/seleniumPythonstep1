#coding=utf-8
# 2-17注册流程梳理及代码封装
from selenium import webdriver
import time
import random
from PIL import Image
import ddddocr 
driver = webdriver.Chrome() #实例化

# 浏览器初始化（封装，创建driver初始化函数）
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

# 获取element信息
def get_element(id):
    element=driver.find_element_by_id(id) #需要定位哪个输入框就传哪个的id进来
    return element

#获取随机数
def get_rang_user():
    user_info=''.join(random.sample('1234567890abcdefg',8))
    return user_info

# 获取图片(这张图片怎么进行命名？)
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element=driver.find_element_by_id("getcode_num") #验证码图片的id
    left=code_element.location['x'] #x值
    top=code_element.location['y']  #y值
    right=code_element.size['width']+left  #图片的宽度加left等于图片右边的点
    height=code_element.size['height']+top  #图片的高度加
    im=Image.open(file_name) 
    img=im.crop((left,top,right,height)) #把这个对象按照一定的坐标去裁剪它裁剪完之后就是一个对象img
    img.save(file_name)

# 解析图片获取验证码,要把文件名file_name传进来,识别出来之后返回结果
def code_ddddocr(file_name):
    ocr=ddddocr.DdddOcr()
    with open(file_name, 'rb') as f:
        img_bytes=f.read()
    text=ocr.classification(img_bytes)
    return text
    
    
# 创建主程序
def run_main():
    user_name_info=get_rang_user() #这样就产生了随机数信息
    user_email=user_name_info+"@163.com" #随机数加上@163.com就变成邮箱
    file_name="D:/SELENIUMPYTHON/part_one/image/test02.png"  #定义验证码图片的存储路径及图片名
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    code_ddddocr(file_name)
    text=code_ddddocr(file_name) #由于code_ddddocr的返回值是text
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    time.sleep(5)
    driver.close()

run_main()   


