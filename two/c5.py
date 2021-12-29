# print('~~~~~~~~~~~~~~~~~')
# from selenium import webdriver #从模块selenium中导入webdriver定义
# print('~~~~~~~~~~~~~~~~~')
# driver=webdriver.Edge() #调用IE
# driver.get("http://www.baidu.com")#用Edge()函数的get方法打开百度

from selenium import webdriver #从模块selenium中导入webdriver定义
print('~~~~~~~~~~~~~~~~~')
driver=webdriver.Firefox()#调用火狐
driver.get("http://www.baidu.com")#用Firefox()函数的get方法打开百度
driver1=webdriver.Chrome() #调用谷歌
driver1.get("http://www.baidu.com")
driver2=webdriver.Edge() #调用win10的ie
driver2.get("http://www.baidu.com")

