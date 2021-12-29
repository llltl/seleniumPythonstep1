#coding=utf-8
# 2-14 使用pytesseract识别图片中得问题
import pytesseract
from PIL import Image
image = Image.open("D:/imooc2.png")
text=pytesseract.image_to_string(image)
print("\n")
print(text)
