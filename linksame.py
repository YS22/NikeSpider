# -*- coding: utf-8 -*-
# 程序基本框架
import requests
import json
from bs4 import BeautifulSoup
import pytesseract
import StringIO
from PIL import Image
#import urllib
# ...

def nike(spurl,registerinfo,userinfo):
	# 注册
	# regUrl="https://unite.nike.com/join"
	# regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	#           'Referer':'http://store.nike.com/cn/zh_cn/'}
	# regData={
	# "account":{"email": registerinfo['email'], "passwordSettings": {"password": "112358yS", "passwordConfirm": "112358yS"}},
	# "country": "CN",
	# "dateOfBirth": "1994-01-25",
	# "firstName": "sheng",
	# "gender": "male",
	# "lastName": "yang",
	# "locale": "zh_CN",
	# "mobileNumber": registerinfo['mobile'],
	# "receiveEmail": "true",
	# "registrationSiteId": "nikedotcom",
	# "username": registerinfo['email'],
	# "welcomeEmailTemplate": "TSD_PROF_COMM_WELCOME_V1.0"
	# }
	# requests.post(regUrl,data=json.dumps(regData),headers =regHead)
	# 登陆
	loginUrl="https://www.nike.com/profile/login?Content-Locale=zh_CN"
	head= {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0','Referer': 'http://store.nike.com/cn/zh_cn/'}
	data={"login":registerinfo['email'],"password":"112358yS","rememberMe":"true"}
	loginhtml = requests.post(loginUrl,data= data,headers = head)
	# print loginhtml.text
	c= loginhtml.cookies
	loginCookie=dict(AnalysisUserId= c["AnalysisUserId"],
          ak_bmsc= c["ak_bmsc"],
          llCheck= c["llCheck"],
          slCheck= c["slCheck"],
          sls= c["sls"],
          NIKE_COMMERCE_COUNTRY='CN')
	print loginCookie
	# 商品页面
	#sphtml = requests.get(spurl,headers = head,cookies=loginCookie)
	#print sphtml.text
	# 添加购物车
	# addUrl='https://nod.nikecloud.com/nod/rest/intake'
	# paydata={"t":1498726926137,"upm":"16138156515","analysisUserId":loginCookie['AnalysisUserId'],"guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05","cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1","platform":{"id":"nike.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11819614","qty":"1","skuAndSize":"19844165:40","name":"addToCartEvent","t":1498726926134,"url":"https://store.nike.com/cn/zh_cn/pd/zoom-kd10-ep-男子篮球鞋/pid-11819614/pgid-11852285","swoosh":'false',"location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},"guidS":"8b35890e-c179-4483-fc8f-c6e33962e927"}]}
	# addcart=requests.post(addUrl,headers=head,data=paydata,cookies=loginCookie)
	# print addcart.status_code
	# addUrl2='https://nod.nikecloud.com/nod/rest/intake'
	# paydata2={"t":1498726927281,"upm":"16138156515","analysisUserId":"WUDmUwoMQ10AACGkllAAAARv","guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05","cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1","platform":{"id":"nike.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"name":"addToCartSuccessEvent","t":1498726927278,"url":"https://store.nike.com/cn/zh_cn/pd/zoom-kd10-ep-男子篮球鞋/pid-11819614/pgid-11852285","swoosh":'false',"location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},"guidS":"8b35890e-c179-4483-fc8f-c6e33962e927"}]}
	# addcart2=requests.post(addUrl2,headers=head,data=paydata2,cookies=loginCookie)
	# print addcart2.status_code
	#return payurl 
	
def adidas(spurl,registerinfo,userinfo):
	# 注册
	# infoHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
 #          	   'Referer':'https://www.adidas.com.cn/customer/account/create/'}
	# regUrl="https://www.adidas.com.cn/customer/account/createpost/"
	# cookie=requests.get(regUrl,headers=infoHead).cookies

	# regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	#           'Referer':'https://www.adidas.com.cn/customer/account/create/',
	#           'cookie':str(cookie)
	#           }

	# infoUrl='https://www.adidas.com.cn/customer/account/create/'
	# html=requests.get(infoUrl,headers=infoHead).text
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
	#          'mobile':registerinfo['mobile'],
	#          'gender':'1',
	#          'day':'2',
	#          'year':'1994',
	#          'dob':'1994-3-2',
	#          'osolCatchaTxt':vcode,
	#          'osolCatchaTxtInst':1,
	#          'email':registerinfo['email'],
	#          'username':registerinfo['username'],
	#          'password':'112358yS',
	#          'confirmation':'112358yS',
	#          'agree_terms':1
	# }
	# reghtml=requests.post(regUrl,data=regData,headers =regHead)
	# print reghtml.text
	# loginCookie=reghtml.cookies
	# 登陆
	loginUrl="https://www.adidas.com.cn/customer/account/loginPost/"
	loginHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'https://www.adidas.com.cn/customer/account/login/'}
	loginCookie=requests.get(loginUrl,headers=loginHead).cookies
	#print loginCookie
	head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	       'Referer': 'https://www.adidas.com.cn/customer/account/login/',
	       'cookie':str(loginCookie)
	       }
	data={"login[username]":registerinfo['username'],"login[password]":"112358yS",'send':''}
	loginHtml = requests.post(loginUrl,data=data,headers = head)
	#print loginHtml.text
	loginCookie=loginHtml.cookies
	#print loginCookie
	#print loginCookie
	# 查看购物车
	cartUrl='http://www.adidas.com.cn/checkout/cart/'
	cartHtm=requests.get(cartUrl,headers=loginHead,cookies=loginCookie)
	print cartHtm.text
	#print loginCookie
	#添加购物车
	## 获取验证信息
	spHtml=requests.get(spurl,headers=loginHead,cookies=loginCookie)
	
	soup=BeautifulSoup(spHtml.text,'html.parser')
	script=soup.select('script')[-4]
	productid=str(script).split(',')[2].split('+')[1]
	infoUrl='http://www.adidas.com.cn/specific/product/ajaxview/?id='+productid
	infoHml=requests.get(infoUrl,headers=loginHead,cookies=loginCookie)

	#print infoHml
	infosoup=BeautifulSoup(infoHml.text,'html.parser')
	token=infosoup.select('input')[0]['value']
	#print token
	isajax=infosoup.select('input')[1]['value']
	#print isajax
	release2=infosoup.select('input')[2]['value']
	#print release2
	product=infosoup.select('input')[3]['value']
	#print product
	## 添加
	addurl='http://www.adidas.com.cn/checkout/cart/add/'
	addHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
			 'Referer': 'https://www.adidas.com.cn/customer/account/login/',
			 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	#params = {'token':token,'isajax':isajax,'release2':release2,'product':product,'super_attribute[185]':'811','qty':'1'}        
	# data = urllib.urlencode(params) 
	#print data
	payload = "token="+token+"&isajax="+isajax+"&release2="+release2+"&product="+product+"&super_attribute%5B185%5D="+"811"+"&qty="+"1"
	print payload
	add=requests.post(addurl,data=payload,headers=addHead,cookies=loginCookie)
	print add.status_code


	#return payurl

def apple(spurl,registerinfo,userinfo):
	pass
	return payurl


# 平台标识
nikeUrl='https://store.nike.com/cn/zh_cn'
adidasUrl='http://www.adidas.com.cn/'
appleUrl='https://www.apple.com/cn/'

# 动态数据
weburl='http://www.adidas.com.cn/'
spurl='http://www.adidas.com.cn/cf9797'
userinfo={}
registerinfo={'email':'ysnike123456@qq.com','mobile':'17786495627','username':'ysadidas1998'}


# 平台选择
if weburl==nikeUrl:
	nike(spurl,registerinfo,userinfo)

if weburl==adidasUrl:
	adidas(spurl,registerinfo,userinfo)
	
if weburl==appleUrl:
	payurl=apple(spurl,registerinfo,userinfo)
	
