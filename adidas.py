# -*- coding: utf-8 -*-
import requests
#from lxml import etree
from bs4 import BeautifulSoup
import json
import pytesseract
import StringIO
from PIL import Image
import sys
reload(sys)   
sys.setdefaultencoding('utf8')
import time

#注册
# infoHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
#          'Referer':'https://www.adidas.com.cn/customer/account/create/'}
# regUrl="https://www.adidas.com.cn/customer/account/createpost/"
# cookie=requests.get(regUrl,headers=infoHead).cookies
# #print cookie

# regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
#           'Referer':'https://www.adidas.com.cn/customer/account/create/',
#           'cookie':str(cookie)
#           }

# infoUrl='https://www.adidas.com.cn/customer/account/create/'
# html=requests.get(infoUrl,headers=infoHead).text
# #print html
# #获得token
# soup=BeautifulSoup(html,'html.parser')
# token=soup.select('input')[1]['value']
# #print token
# #获得验证码
# imageUrl=soup.select('#captchaCode1')[0]['src']
# imageHtml=requests.get(imageUrl,headers=infoHead).content
# imgFile=StringIO.StringIO(imageHtml) #缓存图片
# img=Image.open(imgFile)
# #print img
# vcode = pytesseract.image_to_string(img)
# print (vcode)
# regData={
#  		 'token':token,
#          'firstname':'杨胜',
#          'mobile':'17786596431',
#          'gender':'1',
#          'day':'2',
#          'year':'1994',
#          'dob':'1994-3-2',
#          'osolCatchaTxt':vcode,
#          'osolCatchaTxtInst':1,
#          'email':'ys23441@qq.com',
#          'username':'ys95279521',
#          'password':'112358yS',
#          'confirmation':'112358yS',
#          'agree_terms':1
# }

# regHtml= requests.post(regUrl,data=regData,headers =regHead)
# cookie=regHtml.cookies
# print regHtml.text

# # 登陆
loginUrl="https://www.adidas.com.cn/customer/account/loginPost/"
loginHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'https://www.adidas.com.cn/customer/account/login/'}
loginCookie=requests.get(loginUrl,headers=loginHead).cookies
#print loginCookie
head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
       'Referer': 'https://www.adidas.com.cn/customer/account/login/',
       'cookie':str(loginCookie)
       }
data={"login[username]":'ys95279521',"login[password]":"112358yS",'send':''}
loginHtml = requests.post(loginUrl,data=data,headers = head)
#print loginHtml.text
loginCookie=loginHtml.cookies
#print loginCookie


# #添加购物车
# addUrl='http://www.adidas.com.cn/checkout/cart/add/'
addHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
		 'Referer': 'https://www.adidas.com.cn/customer/account/login/'
		  }

spUrl='http://www.adidas.com.cn/bp8910'
spHtml=requests.get(spUrl,headers=addHead).text
#spcookie=spHtml.cookies
print spHtml


# infoUrl='http://www.adidas.com.cn/specific/product/ajaxview/?id=348123'#如何得到这个链接
# infoHtml=requests.get(infoUrl,headers=addHead).text
# #print infoHtml
# soup=BeautifulSoup(spHtml,'html.parser')
# token=soup.select('input')[0]['value']
# print token


# data={'token':token,
#   	  'isajax':'yes',
#   	  'rerelease2':'yes',
#   	  'product':'348123',
#  	  'super_attribute[184]':'96',
#  	  'qty':'1'
#  }

# addHtml=requests.post(addUrl,headers=addHead,data=data)
# print addHtml.text
# print addHtml.status_code