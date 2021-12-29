#coding=utf-8
# 2-15  ShowapiRequest解决图片验证码识别

from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest
import base64

''' 1、调用chrome浏览器，打开最大化浏览器'''
driver=webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))


'''2、截图浏览器中的图片，进行切割(Pillow库），从网页中提取出验证码图片 '''
def jietu():
    driver.save_screenshot("D:/imooc.png")
    code_element=driver.find_element_by_id("getcode_num")
    print(code_element.location)
    left=code_element.location['x']
    top=code_element.location['y']
    right=code_element.size['width']+left
    height=code_element.size['height']+top
    im=Image.open("D:/imooc.png")
    img=im.crop((left,top,right,height))
    img.save("D:/imooc1.png")
    with open("D:/imooc1.png",'rb') as f:
        data64 = base64.b64encode(f.read())
        text64 = data64.decode()# 转换成图片的base64字符串
        print(text64)
    return text64

'''3、再针对验证码进行识别（易源的接口）'''
def   shibieyanzhengma():
    # 使用接口环境访问接口地址===>前提要注意联网
    yun1 = ShowapiRequest("http://route.showapi.com/2360-1","807905","138396ccfa694517b3ce53b6105baef2" )
# 增加接口请求的参数
    yun1.addBodyPara("img_base64",jietu())
    print(yun1.post().text)
    # 从json提炼出有效的数据
    remark = yun1.post().json()
    text = remark['showapi_res_body']['remark']    #?
    print("验证码是",text)
    return  text

# # 运行
if  __name__=="__main__":
    # # 调用验证码函数获取结果
    yanzhengma = shibieyanzhengma()   #?
    # 将验证码放到网页上
    driver.find_element_by_name("captcha_code").send_keys(yanzhengma)
    # time.sleep(3)
    # driver.quit()

# # email_element=driver.find_element_by_id("register_email")
# driver.save_screenshot("D:\imooc.png")
# code_element=driver.find_element_by_id("getcode_num") #验证码图片的id
# print(code_element.location) #打印x\y的坐标,'x': 1002, 'y': 527
# left=code_element.location['x'] #x值
# top=code_element.location['y']  #y值
# right=code_element.size['width']+left  #图片的宽度加left等于图片右边的点
# height=code_element.size['height']+top  #图片的高度加

#  #把“D:\imooc.png”这张图片命名为一个对象im,然后这个对象就可以调用它的方法crop
# im=Image.open("D:\imooc.png") 
# img=im.crop((left,top,right,height)) #把这个对象按照一定的坐标去裁剪它裁剪完之后就是一个对象img
# img.save("D:\imooc1.png")
















# import pytesseract
# from PIL import Image
# import base64

# from ShowapiRequest import ShowapiRequest






# r = ShowapiRequest("http://route.showapi.com/2360-1","807905","138396ccfa694517b3ce53b6105baef2" )
# r.addBodyPara("imag", "D:/imooc1.png")
# res = r.post()
# print(res.text) # 返回信息