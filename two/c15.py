#coding=utf-8
# 2-15 showapiRequest解决图片验证码识别

import ddddocr 
ocr=ddddocr.DdddOcr()
with open('D:/imooc1.png', 'rb') as f:
    img_bytes=f.read()
 
res=ocr.classification(img_bytes)
print(res)
