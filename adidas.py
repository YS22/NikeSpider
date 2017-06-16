# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import pytesseract
import StringIO
from PIL import Image
import sys
reload(sys)   
sys.setdefaultencoding('utf8')

#注册
#infoHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
#          'Referer':'https://www.adidas.com.cn/customer/account/create/'}
# regUrl="https://www.adidas.com.cn/customer/account/createpost/"
# cookie=requests.get(regUrl,headers=infoHead).cookies
# #print cookie

# regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
#           'Referer':'https://www.adidas.com.cn/customer/account/create/',
#           'cookie':str(cookie)}

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
# #print (vcode)
# regData={
#  		 'token':token,
#          'firstname':'杨胜',
#          'mobile':'17786596377',
#          'gender':'1',
#          'day':'2',
#          'year':'1994',
#          'dob':'1994-3-2',
#          'osolCatchaTxt':vcode,
#          'osolCatchaTxtInst':1,
#          'email':'cky255512@qq.com',
#          'username':'yeelink44',
#          'password':'112358yS',
#          'confirmation':'112358yS',
#          'agree_terms':1
# }

# regHtml= requests.post(regUrl,data=regData,headers =regHead)

#print regHtml.text
# # 登陆
# afterUrl='http://www.adidas.com.cn/'
# loginUrl="https://www.adidas.com.cn/customer/account/loginPost/"
# head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'https://www.adidas.com.cn/customer/account/login/'}
# data={"login[username]":'yeelink44',"login[password]":"112358yS",'send':''}
# loginhtml = requests.post(loginUrl,data= data,headers = head)
# print loginhtml.cookies
# afterhtml = requests.get(afterUrl,headers = head,cookies=loginhtml.cookies)
# print afterhtml.text


