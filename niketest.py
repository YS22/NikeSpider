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
import random
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 


def nike(spurl):
	#添加购物车
	head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	 		   'Referer': 'https://www.adidas.com.cn/customer/account/login/'}
	spHtml=requests.get(spurl,headers=head)
	cookies=spHtml.cookies
	#print cookies
	soup=BeautifulSoup(spHtml.text,'html.parser')
	action=soup.select('.add-to-cart-form input')[0]['value']
	lang_locale=soup.select('.add-to-cart-form input')[1]['value']
	country=soup.select('.add-to-cart-form input')[2]['value']
	catalogId=soup.select('.add-to-cart-form input')[3]['value']
	productId=soup.select('.add-to-cart-form input')[4]['value']
	price=soup.select('.add-to-cart-form input')[5]['value']
	siteId=soup.select('.add-to-cart-form input')[6]['value']
	sizeType=soup.select('.add-to-cart-form input')[8]['value']
	#qty=soup.select('.add-to-cart-form input')[9]['value']

	#print action,lang_locale,country,catalogId,productId,price,siteId,sizeType,qty
	info={'callback':'nike_Cart_handleJCartResponse',
		  'action':action,
		  'lang_locale':lang_locale,
		  'country':country,
		  'catalogId':catalogId,
		  'productId':productId,
		  'price':price,
		  'siteId':'null',
		  'passcode':'null',
		  'sizeType':'null',
		  'qty':'1',
		  'skuAndSize':'19281031:42.5',#尺码参数
		  'rt':'json',
		  'view':'3',
		  'skuId':'19281031',#尺码参数
		  'displaySize':'42.5',#尺码参数
		  '_':'1500631304791'} #时间参数，可以固定
	params = urllib.urlencode(info)
	print params

	addHead={'referer':spurl,
			 'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
	}
	url='https://secure-store.nike.com/ap/services/jcartService?'+params #参数从RUL传递
	add=requests.get(url,headers=addHead,cookies=cookies)
	
	print add.status_code
	print add.text
	# cartUrl='https://secure-store.nike.com/cn/checkout/html/cart.jsp?country=CN&country=CN&l=cart&country=cn&lang_locale=zh_cn&site=nikestore'
	# cartHtml=requests.get(cartUrl,headers=head,cookies=Cookie).text
	# print cartHtml
	# 添加收货信息

	# url='https://secure-store.nike.com/cn/checkout/html/shipping.jsp?country=CN&register=unchecked'
	# html=requests.get(url,headers=addHead,cookies=Cookie)
	# Cookie=dict(spCookie)
	# Cookie['NIKE_COMMERCE_COUNTRY']='CN'
	# #print html.text
	# soup=BeautifulSoup(html.text,'html.parser')
	# _dynSessConf=soup.select('.formValidation input')[1]['value']
	# print _dynSessConf

	# data={'_dyncharset':'UTF-8',
	# 	'_dynSessConf':_dynSessConf,
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.copyfrom':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.copyfrom': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.copyAddress':'true',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.copyAddress': '',
	# 	'copyShipToBillingAddress':'true',
	# 	'_D:copyShipToBillingAddress': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.saveShipAddressToProfile':'false',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.saveShipAddressToProfile': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.firstName':'胜',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.firstName': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.lastName':'杨',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.lastName': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altFirstName':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altFirstName': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altLastName':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altLastName': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.postalCode':'432000',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.postalCode': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address1':'汉阳造',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address1': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address2':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address2': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address3':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address3': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.city':'武汉市',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.city': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.county':'汉阳区',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.county': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.state':'CN-42',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.state': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.companyName':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.companyName': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.accessPointId':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.accessPointId': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.cppId':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.cppId': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.validatedCode':'0',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.validatedCode': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.phoneNumber':'17786493932',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.phoneNumber': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.faxNumber':'',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.faxNumber': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.email':'494178252@qq.com',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.email': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.captureFapiao':'false',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.captureFapiao': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.capturePreferredDeliveryDay':'true',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.capturePreferredDeliveryDay': '',
	# 	'hasSavedAddresses':'false',
	# 	'selectAddressType':'singleAddress',
	# 	'lname':'杨',
	# 	'fname':'胜',
	# 	'singleState':'CN-42',
	# 	'city':'武汉市',
	# 	'countyField':'汉阳区',
	# 	'address1Field':'汉阳造',
	# 	'address2Field':'',
	# 	'postalCodeField':'432000',
	# 	'countryField':'CN',
	# 	'phoneNumber':'17786493932',
	# 	'email':'494178252@qq.com',
	# 	'lname':'',
	# 	'fname':'',
	# 	'singleState':'',
	# 	'phoneNumber':'',
	# 	'email':'',
	# 	'companyName':'',
	# 	'address1Field':'',
	# 	'address2Field':'',
	# 	'accessPointField':'',
	# 	'cppField':'',
	# 	'preferredDeliveryDay':'noPreference',
	# 	'/shared/UserAttributes.isNewMember':'',
	# 	'_D:/shared/UserAttributes.isNewMember':'' ,
	# 	'/shared/UserAttributes.emailOptIn':'',
	# 	'_D:/shared/UserAttributes.emailOptIn': '',
	# 	'apoFlag':'false',
	# 	'langLocale':'zh_CN',
	# 	'country':'CN',
	# 	'route':'html',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoErrorURL':'shippingPageURL',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoErrorURL': '',
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoSuccessURL':'paymentPageURL',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoSuccessURL':'' ,
	# 	'/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfo':'true',
	# 	'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfo':'' ,
	# 	'_DARGS':'/ap/checkout/common/includes/shippingFormInputsIdentity.jsp.shippingForm'}
	# head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	#  		   'Referer': 'https://www.adidas.com.cn/customer/account/login/',
	#  		   'Content-Type':'application/x-www-form-urlencoded'}
	# params=urllib.urlencode(data)
	# postUrl='https://secure-store.nike.com/cn/checkout/html/shipping.jsp?_DARGS=/ap/checkout/common/includes/shippingFormInputsIdentity.jsp.shippingForm'
	# html=requests.post(postUrl,data=params,headers=head,cookies=Cookie)
	# print html.text
	# print html.status_code
	# print html.url
	#提交结算
	## 1
# 	cartUrl='https://secure-store.nike.com/cn/checkout/html/cart.jsp?country=CN&country=CN&l=cart&site=nikestore&returnURL=http://store.nike.com/cn/zh_cn/&route=html'
# 	cartHtml=requests.get(cartUrl,headers=head,cookies=loginCookie)
# 	#print cartHtml.text
# 	loginCookie=dict(cartHtml.cookies)
# 	loginCookie['NIKE_COMMERCE_COUNTRY']='CN'
# 	soup=BeautifulSoup(cartHtml.text,'html.parser')
# 	print soup.select('#cartForm input')[15]['value']
# 	print soup.select('#cartForm input')[15]['name']


# 	data={'_dyncharset':soup.select('#cartForm input')[0]['value'],
#       '_dynSessConf':soup.select('#cartForm input')[1]['value'],
#       'saveGiftFlag':soup.select('#cartForm input')[2]['value'],
#       'country':soup.select('#cartForm input')[3]['value'],
#       'route':soup.select('#cartForm input')[4]['value'],
#       'populateBillingAddressWithShippingAddress':soup.select('#cartForm input')[5]['value'],
#       '_D:populateBillingAddressWithShippingAddress':soup.select('#cartForm input')[6]['value'],
#       '/atg/commerce/order/purchase/CartModifierFormHandler.expressCheckoutErrorURL':soup.select('#cartForm input')[7]['value'],
#       '_D:/atg/commerce/order/purchase/CartModifierFormHandler.expressCheckoutErrorURL':soup.select('#cartForm input')[8]['value'] ,
#       '/atg/commerce/order/purchase/CartModifierFormHandler.expressCheckoutSuccessURL':soup.select('#cartForm input')[9]['value'],
#       '_D:/atg/commerce/order/purchase/CartModifierFormHandler.expressCheckoutSuccessURL':soup.select('#cartForm input')[10]['value'] ,
#       '/atg/commerce/order/purchase/CartModifierFormHandler.moveToReviewSuccessURL':soup.select('#cartForm input')[11]['value'],
#       '_D:/atg/commerce/order/purchase/CartModifierFormHandler.moveToReviewSuccessURL':soup.select('#cartForm input')[12]['value'],
#       'deviceId':soup.select('#cartForm input')[13]['value'],
#       '_D:deviceId':soup.select('#cartForm input')[14]['value'],
#       soup.select('#cartForm input')[15]['name']:soup.select('#cartForm input')[15]['value'],#这列key是变的
#       '/atg/commerce/order/purchase/CartModifierFormHandler.moveToPurchaseInfoSuccessURL':soup.select('#cartForm input')[16]['value'],
#       '_D:/atg/commerce/order/purchase/CartModifierFormHandler.moveToPurchaseInfoSuccessURL':soup.select('#cartForm input')[17]['value'],
#       '/atg/commerce/order/purchase/CartModifierFormHandler.moveToPurchaseInfoErrorURL':soup.select('#cartForm input')[18]['value'],
#       '_D:/atg/commerce/order/purchase/CartModifierFormHandler.moveToPurchaseInfoErrorURL':soup.select('#cartForm input')[19]['value'],
#       '/atg/commerce/order/purchase/CartModifierFormHandler.shipToDoneErrorURL':soup.select('#cartForm input')[20]['value'],
#       '_D:/atg/commerce/order/purchase/CartModifierFormHandler.shipToDoneErrorURL':soup.select('#cartForm input')[21]['value'],
#       '/atg/commerce/order/purchase/CartModifierFormHandler.moveToCheckout':soup.select('#cartForm input')[22]['value'],
#       '_D:/atg/commerce/order/purchase/CartModifierFormHandler.moveToCheckout':soup.select('#cartForm input')[23]['value'],
#       '_DARGS':soup.select('#cartForm input')[24]['value']
# }	
# 	params=urllib.urlencode(data)
# 	payhead={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
# 			 'Referer': 'http://store.nike.com/cn/zh_cn/',
# 			 'content-type':'application/x-www-form-urlencoded'}

# 	postUrl='https://secure-store.nike.com/cn/checkout/html/cart.jsp?_DARGS='+soup.select('#cartForm input')[24]['value']
# 	toPay=requests.post(postUrl,headers=payhead,data=params,cookies=loginCookie)
# 	print toPay.status_code
# 	#print toPay.text
# 	print toPay.url

# 	# loginCookie=dict(toPay.cookies)
# 	# loginCookie['NIKE_COMMERCE_COUNTRY']='CN'
# 	# print loginCookie


# 	## 2
# 	soup=BeautifulSoup(toPay.text,'html.parser')
# 	_dyncharset=soup.select('#billingForm input')[0]['value']
# 	_dynSessConf=soup.select('#billingForm input')[1]['value']

# 	secureProxyKey=soup.select('.ch4_checkoutAccordion input')[0]['value']
# 	print _dynSessConf,secureProxyKey ,logininfo['email']
# 	posturl='https://secure-store.nike.com/cn/checkout/html/payment.jsp?_DARGS=/ap/checkout/html/payment.jsp.billingForm'
	
# 	data={'_dyncharset':'UTF-8',
# 		'_dynSessConf':_dynSessConf,
# 		'/atg/userprofiling/Profile.email':logininfo['email'],
# 		'_D:/atg/userprofiling/Profile.email':'',
# 		'secureProxyKey':secureProxyKey,
# 		'runPaymentValidation':'false',
# 		'route':'html',
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoSuccessURL':'https://secure-store.nike.com/cn/checkout/html/confirm.jsp',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoSuccessURL':'',
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoErrorURL':'https://secure-store.nike.com/cn/checkout/html/payment.jsp',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoErrorURL':'',
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'alipay',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'' ,
# 		'/atg/commerce/order/purchase/PaymentGroupFormHandler.captureFapiao':'true',
# 		'_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.captureFapiao':'' ,
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.captureFapiao':'true',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.captureFapiao':'',
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.values.bankName':'',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.values.bankName':'',
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.submitMode':'billingReviewSubmit',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.submitMode':'',
# 		'/atg/commerce/order/purchase/PaymentGroupFormHandler.useProfileEmailAddress':'false',
# 		'_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.useProfileEmailAddress':'',
# 		'deviceId':'',
# 		'_D:deviceId':'' ,
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.executeBillingReview':'true',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.executeBillingReview':'' ,
# 		'/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'',
# 		'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'' ,
# 		'paymentMethod':'alipay',
# 		'_DARGS':'/ap/checkout/html/payment.jsp.billingForm'
# 	}
# 	params=urllib.urlencode(data)
	
# 	html=requests.post(posturl,headers=payhead,data=params,cookies=loginCookie,allow_redirects=False)
# 	print html.status_code
# 	print html.url
	#print html.text
	
	

	
if __name__ == '__main__':
			
	
	#修改数据
 	stid='3'#json.loads(r.text)['data'][0]['site_id']
 	spurl='https://store.nike.com/cn/zh_cn/pd/air-zoom-mariah-flyknit-racer-%E7%94%B7%E5%AD%90%E8%BF%90%E5%8A%A8%E9%9E%8B/pid-11598426/pgid-11805238'
 	#spurl=json.loads(r.text)['data'][0]['task_url']

 	
	
	if stid=='3':
		nike(spurl)

	if stid=='1':
		adidas(spurl,size_valueList)

