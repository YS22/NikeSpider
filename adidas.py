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
regUrl="https://www.adidas.com.cn/customer/account/createpost/"
regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
          'Referer':'https://www.adidas.com.cn/customer/account/create/'}

infoUrl='https://www.adidas.com.cn/customer/account/create/'
html=requests.get(infoUrl,headers=regHead).text
#print html
#获得token
soup=BeautifulSoup(html,'html.parser')
token=soup.select('input')[1]['value']
#print token
#获得验证码
imageUrl=soup.select('#captchaCode1')[0]['src']
imageHtml=requests.get(imageUrl,headers=regHead).content
file=StringIO.StringIO(imageHtml) #缓存图片
img=Image.open(file)
#print img
vcode = pytesseract.image_to_string(img)
#print (vcode)
regData={
 		 'token':token,
         'firstname':'yangsheng17',
         'mobile':'17789563932',
         'gender':'1',
         'day':'2',
         'year':'1994',
         'dob':'1994-3-2',
         'osolCatchaTxt':vcode,
         'osolCatchaTxtInst':1,
         'email':'cky13t@qq.com',
         'username':'yanhggj',
         'password':'112358yS',
         'confirmation':'112358yS',
         'agree_terms':1
}

regHtml= requests.post(regUrl,data=regData,headers =regHead)
print regHtml.text


# # 登陆
# loginUrl="https://www.adidas.com.cn/customer/account/login/"
# head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'http://store.nike.com/cn/zh_cn/'}
# data={"login[username]":"cky12t@qq.com","login[password]":"112358yS","rememberMe":"true"}
# loginhtml = requests.post(loginUrl,data= data,headers = head)
# print loginhtml.text
# print "登陆状态:"
# print loginhtml.status_code



