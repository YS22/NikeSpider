# -*- coding: utf-8 -*-
# 程序基本框架
import requests
import json
from bs4 import BeautifulSoup
import pytesseract
import StringIO
from PIL import Image
import urllib
import time 

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
	# cart
	# cartUrl='https://secure-store.nike.com/cn/checkout/html/cart.jsp'
	# cartHtml=requests.get(cartUrl,headers=head,cookies=loginCookie).text
	# print cartHtml

	# 商品页面
	# sphtml = requests.get(spurl,headers = head,cookies=loginCookie)
	# print sphtml.text
	# 添加购物车
	addUrl='https://nod.nikecloud.com/nod/rest/intake'
	payload={"t":1,
			 "upm":1,
			 "analysisUserId":loginCookie['AnalysisUserId'],
			 "guidU":1,
			 "cookies":{"CONSUMERCHOICE":"cn/zh_cn",
			 			"neo.experiments":1,
			 			"neo.swimlane":1},
			 "deviceAtlas":1,
			 "platform":{"id":"nike.com","v":"main"},
			 "source":{"id":"dreamcatcher","v":"3.29.2"},
			 "events":[{"pid":1,
			 			"qty":"1",
			 			"skuAndSize":1,
			 			"name":"addToCartEvent",
			 			"t":1,
			 			"url":1,
			 			"swoosh":'false',
			 			"location":{"cc":"CN","rc":"BJ","tp":"vhigh","tz":"GMT+8","la":"39.90","lo":"116.41","bw":"5000"},
			 			"guidS":1}]}
	print payload
	addcart=requests.post(addUrl,headers=head,data=payload,cookies=loginCookie)
	print addcart.status_code
	# payload2={"t":str(int((time.time())*1000)),
	# 		  "upm":"16154697162",
	# 		  "analysisUserId":loginCookie['AnalysisUserId'],
	# 		  "guidU":"89eb2d42-da51-4460-85ab-c27f62ff6deb",
	# 		  "cookies":{"CONSUMERCHOICE":"cn/zh_cn",
	# 		  			 "neo.experiments":"{\"main\":{},\"ocp\":{}}",
	# 		  			 "neo.swimlane":"22"},
	# 		  "deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/10|bcookieSupport:1",
	# 		  "platform":{"id":"niken"},
	# 		  "source":{"id":"dreamcatcher","v":"3.29.2"},
	# 		  "events":[{"name":"addToCartSuccessEvent",
	# 		  "t":str(int((time.time())*1000)),
	# 		  "url":"https://store.nike.com/cn/zh_cn/pd/loden-女子运动鞋/pid-11597119/pgid-11631130",
	# 		  "swoosh":'false',
	# 		  "location":{"cc":"CN","rc":"BJ","tp":"vhigh","tz":"GMT+8","la":"39.90","lo":"116.41","bw":"5000"},
	# 		  "guidS":"4d595ede-90c9-46a7-ebcc-7845741cf176"}]}
	# addcart2=requests.post(addUrl,headers=head,data=payload2,cookies=loginCookie)
	# print addcart2.status_code
	# addUrl2='https://nod.nikecloud.com/nod/rest/intake'
	# paydata2={"t":1498726927281,"upm":"16138156515","analysisUserId":"WUDmUwoMQ10AACGkllAAAARv","guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05","cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1","platform":{"id":"nike.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"name":"addToCartSuccessEvent","t":1498726927278,"url":"https://store.nike.com/cn/zh_cn/pd/zoom-kd10-ep-男子篮球鞋/pid-11819614/pgid-11852285","swoosh":'false',"location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},"guidS":"8b35890e-c179-4483-fc8f-c6e33962e927"}]}
	# addcart2=requests.post(addUrl2,headers=head,data=paydata2,cookies=loginCookie)
	# print addcart2.status_code
	# return payurl
	
def adidas(spurl,registerinfo,userinfo):
	#注册
	# infoHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
 #           	   'Referer':'https://www.adidas.com.cn/customer/account/create/'}
	# regUrl="https://www.adidas.com.cn/customer/account/createpost/"
	# cookie=requests.get(regUrl,headers=infoHead).cookies

	# regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	#            'Referer':'https://www.adidas.com.cn/customer/account/create/',
	#            'cookie':str(cookie)
	#            }

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
	#          'agree_terms':1}
	# reghtml=requests.post(regUrl,data=regData,headers =regHead)
	# loginCookie=reghtml.cookies
	
	# 登陆
	loginUrl="https://www.adidas.com.cn/customer/account/loginPost/"
	loginHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'https://www.adidas.com.cn/customer/account/login/'}
	loginCookie=requests.get(loginUrl,headers=loginHead).cookies

	head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	       'Referer': 'https://www.adidas.com.cn/customer/account/login/',
	       'cookie':str(loginCookie)
	       }
	data={"login[username]":registerinfo['username'],"login[password]":"112358yS",'send':''}
	loginHtml = requests.post(loginUrl,data=data,headers = head)
	print "登陆成功"
	loginCookie=loginHtml.cookies
	
	# 查看购物车
	cartUrl='http://www.adidas.com.cn/checkout/cart/'
	cartHtm=requests.get(cartUrl,headers=loginHead,cookies=loginCookie)
	print cartHtm.text
	#添加购物车
	#1 获取验证信息
	# spHtml=requests.get(spurl,headers=loginHead,cookies=loginCookie)
	
	# soup=BeautifulSoup(spHtml.text,'html.parser')
	# script=soup.select('script')[-4]
	# productid=str(script).split(',')[2].split('+')[1]
	# infoUrl='http://www.adidas.com.cn/specific/product/ajaxview/?id='+productid
	# infoHml=requests.get(infoUrl,headers=loginHead,cookies=loginCookie)

	# infosoup=BeautifulSoup(infoHml.text,'html.parser')
	# token=infosoup.select('input')[0]['value']
	# isajax=infosoup.select('input')[1]['value']
	# release2=infosoup.select('input')[2]['value']
	# product=infosoup.select('input')[3]['value']

	# ## 2 添加
	# print "开始抢购"
	# addurl='http://www.adidas.com.cn/checkout/cart/add/'
	# addHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	# 		 'Referer': spurl,
	# 		 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
	# #params = {'token':token,'isajax':isajax,'release2':release2,'product':product,'super_attribute[185]':'811','qty':'1'}        
	# # data = urllib.urlencode(params)
	# #print data
	# payload = "token="+token+"&isajax="+isajax+"&release2="+release2+"&product="+product+"&super_attribute%5B185%5D="+"69"+"&qty="+"1"
	# print payload
	# add=requests.post(addurl,data=payload,headers=addHead,cookies=loginCookie)
	# print add.status_code
	# loginCookie=add.cookies
	
	# # reghtml=requests.get(regUrl,headers =loginHead,cookies=loginCookie)
	# # print reghtml.text
	
	# # 添加收货信息
	print "添加收货信息"
	infoUrl='https://www.adidas.com.cn/yancheckout/process/'
	head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
		  'Referer': 'https://www.adidas.com.cn/customer/account/login/'}

	infohtml=requests.get(infoUrl,headers=head,cookies=loginCookie)
	soup=BeautifulSoup(infohtml.text,"html.parser")
	token=soup.select('input')[20]['value']
	#loginCookie=infohtml.cookies
	#print token
	addresUrl='https://www.adidas.com.cn/yancheckout/process/saveShippingAndPayment/'
	userinfo={"shipping[firstname]":"yangsheng",
			  "shipping[country_id]":"CN",
			  "shipping[region_id]":"515",
			  "shipping[region]":"天津",
			  "shipping[city_id]":"342",
			  "shipping[district_id]":"3127",
			  "shipping[city]":"天津市",
			  "shipping[district]":"河东区",
			  "shipping[street][]":"苏家爱华yangsheng21",
			  "shipping[postcode]":"432000",
			  "shipping[mobile]":"17786493931",
			  "shipping[tel_areacode]":"",
			  "shipping[telephone]":"",
			  "shipping[save_in_address_book]":"1",
			  "shipping[use_for_shipping]":"1",
			  "shipping[update_region]":"0",
			  "shipping[primary_shipping]":"1",
			  "shipping[primary_billing]":"1",
			  "shipping[delivery_memo]":"湖区yangsheng2",
			  "shipping[id]":"",
			  "shipping[yancheckout_page]":"1",
			  "delivery_type":"Normal",
			  "token":token,
			  "payment[alipay_pay_bank]":"ALIPAY",
			  "payment[alipay_pay_method]":"bankPay",
			  "shipping_method":"carrier_bestway",
			  "fapiao[fapiao_type]":"personal",
			  "fapiao[fapiao_title]":"",
			  "fapiao[fapiao_memo]":""}
	data = urllib.urlencode(userinfo)
	print data
	add_head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
			 'Referer': 'https://www.adidas.com.cn/yancheckout/process/',
			 'Content-Type':'application/x-www-form-urlencoded'}
	add_addres=requests.post(addresUrl,headers=add_head,data=data,cookies=loginCookie)
	print add_addres.status_code
	print add_addres.text

	# reghtml=requests.get(regUrl,headers =loginHead,cookies=loginCookie)
	# print reghtml.text
    # 获得付款链接

    ## 提交订单
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
spurl='http://www.adidas.com.cn/by4472'
userinfo={}
registerinfo={'email':'linksamewuyang121@qq.com','mobile':'17786493873','username':'wuhanyangshengR2r'}


# 平台选择
if weburl==nikeUrl:
	nike(spurl,registerinfo,userinfo)

if weburl==adidasUrl:
	adidas(spurl,registerinfo,userinfo)
	
if weburl==appleUrl:
	payurl=apple(spurl,registerinfo,userinfo)
	
