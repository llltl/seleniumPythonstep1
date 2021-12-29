'''
Selenium 是一个用于 Web 测试的工具，测试运行在浏览器中，就像真正的用户在手工操作一样。支持所有主流浏览器

这个工具的主要功能包括：

　　1）测试与浏览器的兼容性 ，应用程序是否能够很好地工作在不同浏览器和操作系统之上

　　2）测试系统功能，创建回归测试检验软件功能和用户需求
WebDriver 就是对浏览器提供的原生API进行封装，使其成为一套更加面向对象的Selenium WebDriver API。
使用这套API可以操控浏览器的开启、关闭，打开网页，操作界面元素，控制Cookie，还可以操作浏览器截屏、安装插件、设置代理、配置证书等
'''
#coding=utf-8
print('~~~~~~~~~~~~~~~~~')
from selenium import webdriver #从模块selenium中导入webdriver定义
print('~~~~~~~~~~~~~~~~~')
#driver=webdriver.Chrome() #调用webdriver.Chrome()，启动浏览器
#driver.get("http://www.baidu.com")#用Chrome()函数的get方法打开百度
hh=webdriver.Firefox()
# hh.get("http://www.baidu.com")

