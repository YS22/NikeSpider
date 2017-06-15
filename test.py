import pytesseract
from PIL import Image

image = Image.open(r'D:\Documents\Downloads\2.jpg','r')
print type(image)
vcode = pytesseract.image_to_string(image)
print (vcode)