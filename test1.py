# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import pytesseract
import StringIO
from PIL import Image

# # 登陆
cartUrl='http://www.adidas.com.cn/checkout/cart/'
head={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:54.0) Gecko/20100101 Firefox/54.0',
	  'Referer':'https://www.adidas.com.cn'}
cartHtml=requests.get(cartUrl,headers=head).text
print cartHtml