# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import sys
reload(sys)   
sys.setdefaultencoding('utf8')

#注册
regUrl="https://unite.nike.com/join"
regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
          'Referer':'http://store.nike.com/cn/zh_cn/'}

regData={
"account":{"email": "cky12s@qq.com", "passwordSettings": {"password": "112358yS", "passwordConfirm": "112358yS"}},
"country": "CN",
"dateOfBirth": "1994-01-25",
"firstName": "sheng",
"gender": "male",
"lastName": "yang",
"locale": "zh_CN",
"mobileNumber": "17786493932",
"receiveEmail": "true",
"registrationSiteId": "nikedotcom",
"username": "cky123@qq.com",
"welcomeEmailTemplate": "TSD_PROF_COMM_WELCOME_V1.0"
}

regHtml= requests.post(regUrl,data=json.dumps(regData),headers =regHead)
# print regHtml.text
print "注册状态:"
print regHtml.status_code


#登陆
loginUrl="https://www.nike.com/profile/login"
head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'http://store.nike.com/cn/zh_cn/'}
data={"login":"cky12t@qq.com","password":"112358yS","rememberMe":"true"}
loginhtml = requests.post(loginUrl,data= data,headers = head)
#print loginhtml.text
print "登陆状态:"
print loginhtml.status_code



