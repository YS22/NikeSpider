# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import sys
reload(sys)   
sys.setdefaultencoding('utf8')

#注册
regUrl="https://www.adidas.com.cn/customer/account/create/"
regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
          'Referer':'https://www.adidas.com.cn/customer/account/create/'}


html=requests.get(regUrl,headers=regHead).text
#print html

soup=BeautifulSoup(html,'html.parser')
tokens=soup.select('input')[1]['value']
print tokens

# regData={


# }

# regHtml= requests.post(regUrl,data=json.dumps(regData),headers =regHead)
# # print regHtml.text
# print "注册状态:"
# print regHtml.status_code


# #登陆
# loginUrl="https://www.nike.com/profile/login"
# head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'http://store.nike.com/cn/zh_cn/'}
# data={"login":"cky12t@qq.com","password":"112358yS","rememberMe":"true"}
# loginhtml = requests.post(loginUrl,data= data,headers = head)
# #print loginhtml.text
# print "登陆状态:"
# print loginhtml.status_code



