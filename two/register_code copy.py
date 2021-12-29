import time
from selenium import webdriver
import random
import ddddocr
from PIL import Image


driver=webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_element(id):
    element=driver.find_element_by_id(id)
    return element


#获取随机数
def get_rang_user():
    user_info=''.join(random.sample('1234567abcdef',8))
    return user_info


#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element=driver.find_element_by_id("getcode_num")
    left=code_element.location['x']
    top=code_element.location['y']
    right=code_element.size['width']+left
    height=code_element.size['height']+top
    im=Image.open(file_name)
    img=im.crop((left, top, right, height))
    img.save(file_name)

#解析图片获取验证码
def code_ddddocr(file_name):
        ocr=ddddocr.DdddOcr()
        with open(file_name, 'rb') as f:
            img_bytes=f.read()
        text=ocr.classification(img_bytes)
        return text


#创建主程序
def run_main():
    user_name_info=get_rang_user()
    user_email=user_name_info+'@163.com'
    file_name="D:/SELENIUMPYTHON/part_one/image/test02.png"
    driver_init()
    get_element('register_email').send_keys(user_email)
    get_element('register_nickname').send_keys(user_name_info)
    get_element('register_password').send_keys("11111")
    get_code_image(file_name)
    code_ddddocr(file_name)
    text=code_ddddocr(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    time.sleep(5)
    driver.close()

run_main()
