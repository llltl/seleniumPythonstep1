from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# # 页面元素，title判断
# time.sleep(3)
# print(EC.title_contains("百度一下"))

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
# 判断页面是否正常打开，可以通过打开页面窗口的title是否等于预期进行判断
time.sleep(3)
if EC.title_contains("drrr"):
    print(True)
print(driver.title)
