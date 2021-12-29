# 定位元素（使用不同方式进行定位）
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC #判断页面是否正常打开的包
driver=webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))#返回页面是否正常

#定位邮箱id(元素),并传值
driver.find_element_by_id("register_email").send_keys("mushishi_01@163.com")

# 用户名：先定位上级元素，然后赋值给user_name_element_node ，再# 使用获取到的元素，去找下级元素
user_name_element_node=driver.find_elements_by_class_name("controls")[1]
user_element=user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("qerqere")

driver.find_element_by_name("password").send_keys("111111")#密码，通过元素name定位，再传值
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")#验证码，通过xpath定位元素，再传值

# driver.find_element_by_css_selector("")




