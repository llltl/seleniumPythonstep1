#coding=utf-8
''''本文将运用于定位所有元素'''
''''read_ini=ReadIni()实例化，
 data=read_ini.get_value(key)把key进来，data拿到的值就是像id>register_nickname这样的，然后要以>进行拆分，
 【by=data.split('>')[0]--以>进行拆分第0个值，value=data.split('>')[1]--以>进行拆分第1个值，那这个时候我有定位方式by，和定位
 值，就可以进行下一步操作了,罗列定位方式、值并且进行容错操作（如果说本代码没有定位到任何元素，或者定位的值value是错误的，这个时候就会报错了
 ，这个元素就定位不到，那这时候就得加上try..except进行容错处理；try里面的元素都没定位到，则输出为空（None））】；返回完None之后，那
 我在其他地方调用get_element对象的时候，传回来的就是元素，如果说传回来的元素没有，那就定位为空
'''
#调用ReadIni方法，然后把定位元素的信息给封装起来，也进行了一些简单的容错处理，然后接下来就可以在register_function.py里面调用本模块find_element.py的方法了
from util.read_ini import ReadIni
#封装class
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver


    def get_element(self,key):
        read_ini=ReadIni()
        data=read_ini.get_value(key)
        by=data.split('>')[0]
        value=data.split('>')[1]
        try:
            if by=='id':
                return self.driver.find_element_by_id(value)
            elif by=='name':
                return self.driver.find_element_by_name(value)
            elif by=='className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None