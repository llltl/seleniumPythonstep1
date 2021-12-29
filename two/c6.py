# 使用title_contains检查页面是否正确

# 使用title_contains检查页面是否正确


from selenium import webdriver #从模块selenium中导入webdriver定义
import time
print('~~~~~~~~~~~~~~~~~')
from selenium.webdriver.support import expected_conditions as EC #expected_conditions这个包市面上不常用
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(5)
tile=EC.title_contains("百度一下")
title_return=print(tile(driver))
print(title_return)
if title_return:
    print("title存在，页面返回正确")
time.sleep(3)
driver.quit()  # 等待3s关闭浏览器
