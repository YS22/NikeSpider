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


def nike(spurl):
	#添加购物车

	session=requests.Session()
	head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	 		   'Referer': 'https://www.adidas.com.cn/customer/account/login/'}

	spHtml=session.get(spurl,headers=head)
	#print session.cookies

	#spCookie=spHtml.cookies
	#AnalysisUserId=session.cookies['AnalysisUserId']
	# guidA=session.cookies['guidA']
	# guidS=session.cookies['guidS']
	# print spCookie
	# print spHtml.text
	# print spHtml.url
	# #print spCookie
	soup=BeautifulSoup(spHtml.text,'html.parser')
	action=soup.select('.add-to-cart-form input')[0]['value']
	lang_locale=soup.select('.add-to-cart-form input')[1]['value']
	country=soup.select('.add-to-cart-form input')[2]['value']
	catalogId=soup.select('.add-to-cart-form input')[3]['value']
	productId=soup.select('.add-to-cart-form input')[4]['value']
	price=soup.select('.add-to-cart-form input')[5]['value']
	siteId=soup.select('.add-to-cart-form input')[6]['value']
	sizeType=soup.select('.add-to-cart-form input')[8]['value']
	qty=soup.select('.add-to-cart-form input')[9]['value']

	print action,lang_locale,country,catalogId,productId,price,qty

	info={'callback':'nike_Cart_handleJCartResponse',
		'action':'addItem',
		'lang_locale':'zh_CN',
		'country':'CN',
		'catalogId':catalogId,
		'productId':productId,
		'price':price,
		'siteId':siteId,
		'passcode':'null',
		'sizeType':sizeType,
		'qty':'1',
		'skuAndSize':'20054144:41',
		'rt':'json',
		'view':'3',
		'skuId':'20054144',
		'displaySize':'41',
		'_':'1500945055182'} #时间参数，可以固定

	session.cookies['guidU']='9e35ac0b-c90c-4724-e2f0-1bc70651ff05'
	session.cookies['guidS']='42dc9fe8-86d2-48dd-c570-654f3e1e37a5'
	addHead1={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
			 'referer':spurl}
	url='https://secure-store.nike.com/ap/services/jcartService?' #参数从URL传递params
	add=session.get(url,headers=addHead1,params=info)
	print add.text
	# #print add.url

	session.cookies['NIKE_COMMERCE_COUNTRY']='CN'
	
	# cartUrl='https://secure-store.nike.com/cn/checkout/html/cart.jsp?country=CN&country=CN&l=cart&country=cn&lang_locale=zh_cn&site=nikestore'
	# cartHtml=session.get(cartUrl,headers=head)
	#print cartHtml.text
	# # print cartHtml.url
	# # print cartHtml.history[0].url

	# #结算方式
	payStyle=session.get('https://secure-store.nike.com/cn/checkout/html/forward_to_checkout.jsp?register=unchecked',headers=head)
	print payStyle.url

	# # 添加收货信息
	# ## 1
	# url='https://secure-store.nike.com/cn/checkout/html/shipping.jsp?country=CN&register=unchecked'
	# html=session.get(url,headers=head)
	# print html.text

	soup=BeautifulSoup(payStyle.text,'html.parser')
	_dynSessConf=soup.select('.formValidation input')[1]['value']
	print _dynSessConf

	data={'_dyncharset':'UTF-8',
		'_dynSessConf':_dynSessConf,
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.copyfrom':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.copyfrom': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.copyAddress':'true',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.copyAddress': '',
		'copyShipToBillingAddress':'true',
		'_D:copyShipToBillingAddress': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.saveShipAddressToProfile':'false',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.saveShipAddressToProfile': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.firstName':'胜',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.firstName': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.lastName':'杨',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.lastName': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altFirstName':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altFirstName': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altLastName':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.altLastName': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.postalCode':'432000',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.postalCode': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address1':'汉阳造',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address1': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address2':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address2': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address3':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.address3': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.city':'武汉市',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.city': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.county':'汉阳区',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.county': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.state':'CN-42',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.state': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.companyName':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.companyName': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.accessPointId':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.accessPointId': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.cppId':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.cppId': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.validatedCode':'0',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.validatedCode': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.phoneNumber':'17786493932',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.phoneNumber': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.faxNumber':'',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.faxNumber': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.email':'494178251@qq.com',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.shippingGroup.shippingAddress.email': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.captureFapiao':'false',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.captureFapiao': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.capturePreferredDeliveryDay':'true',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.capturePreferredDeliveryDay': '',
		'hasSavedAddresses':'false',
		'selectAddressType':'singleAddress',
		'lname':'杨',
		'fname':'胜',
		'singleState':'CN-42',
		'city':'武汉市',
		'countyField':'汉阳区',
		'address1Field':'汉阳造',
		'address2Field':'',
		'postalCodeField':'432000',
		'countryField':'CN',
		'phoneNumber':'17786493932',
		'email':'494178252@qq.com',
		'lname':'杨',
		'fname':'胜',
		'singleState':'',
		'phoneNumber':'17786493932',
		'email':'494178252@qq.com',
		'companyName':'',
		'address1Field':'汉阳造',
		'address2Field':'',
		'accessPointField':'',
		'cppField':'',
		'shippingMethod_single':'Ground Service',
		'preferredDeliveryDay':'noPreference',
		'/shared/UserAttributes.isNewMember':'',
		'_D:/shared/UserAttributes.isNewMember':'' ,
		'/shared/UserAttributes.emailOptIn':'',
		'_D:/shared/UserAttributes.emailOptIn': '',
		'apoFlag':'false',
		'langLocale':'zh_CN',
		'country':'CN',
		'route':'html',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoErrorURL':'shippingPageURL',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoErrorURL': '',
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoSuccessURL':'paymentPageURL',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfoSuccessURL':'' ,
		'/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfo':'true',
		'_D:/atg/commerce/order/purchase/ShippingGroupFormHandler.applyShippingInfo':'' ,
		'_DARGS':'/ap/checkout/common/includes/shippingFormInputsIdentity.jsp.shippingForm'}
	#print session.cookies
	postUrl='https://secure-store.nike.com/cn/checkout/html/shipping.jsp?_DARGS=/ap/checkout/common/includes/shippingFormInputsIdentity.jsp.shippingForm'
	addHead={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
			 'referer':spurl,
			 'Content-Type':'application/x-www-form-urlencoded'
			  }
	data=urllib.urlencode(data)
	html=session.post(postUrl,data=data,headers=addHead)
	cookies=html.cookies
	#print html.text
	print html.status_code
	print html.url
	
	# ## 2
	soup=BeautifulSoup(html.text,'html.parser')
	#_dyncharset=soup.select('#billingForm input')[0]['value']
	_dynSessConf=soup.select('#billingForm input')[1]['value']

	secureProxyKey=soup.select('.ch4_checkoutAccordion input')[0]['value']
	print _dynSessConf,secureProxyKey

 	posturl='https://secure-store.nike.com/cn/checkout/html/payment.jsp?_DARGS=/ap/checkout/html/payment.jsp.billingForm'

	data={'_dyncharset':'UTF-8',
			'_dynSessConf':_dynSessConf,
			'/atg/userprofiling/Profile.email':'',
			'_D:/atg/userprofiling/Profile.email': '',
			'secureProxyKey':secureProxyKey,
			'runPaymentValidation':'false',
			'route':'html',
			'/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoSuccessURL':'https://secure-store.nike.com/cn/checkout/html/confirm.jsp',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoSuccessURL':'' ,
			'/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoErrorURL':'https://secure-store.nike.com/cn/checkout/html/payment.jsp',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.applyPaymentInfoErrorURL': '',
			'/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'alipay',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'',
			'/atg/commerce/order/purchase/PaymentGroupFormHandler.captureFapiao':'true',
			'_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.captureFapiao':'',
			'/atg/commerce/order/purchase/CommitOrderFormHandler.captureFapiao':'true',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.captureFapiao':'',
			'/atg/commerce/order/purchase/CommitOrderFormHandler.values.bankName':'',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.values.bankName':'' ,
			'/atg/commerce/order/purchase/CommitOrderFormHandler.submitMode':'billingReviewSubmit',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.submitMode':'',
			'/atg/commerce/order/purchase/PaymentGroupFormHandler.useProfileEmailAddress':'false',
			'_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.useProfileEmailAddress':'',
			'deviceId':'',
			'_D:deviceId':'',
			'atg/commerce/order/purchase/CommitOrderFormHandler.executeBillingReview':'true',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.executeBillingReview':'',
			'/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'',
			'_D:/atg/commerce/order/purchase/CommitOrderFormHandler.paymentType':'',
			'paymentMethod':'alipay',
			'fapiaoFlag':'on',
			'fapiaoTitle':'个人',
			'_DARGS':'/ap/checkout/html/payment.jsp.billingForm'
	}
	
 	Head={
			'content-type':'application/x-www-form-urlencoded',
			'referer':html.url,
			'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
			}
	data=urllib.urlencode(data)
	html=session.post(posturl,data=data,headers=Head)
	print session.cookies
	print html.status_code
	print html.url
	print html.text

	# print html.history
	# print html.history[0].url
	#print session.cookies
	#print html.headers['location']
	
		
if __name__ == '__main__':
			
	
	#修改数据
 	stid='3'#json.loads(r.text)['data'][0]['site_id']
 	spurl='https://store.nike.com/cn/zh_cn/pd/kyrie-3-ep-%E7%94%B7%E5%AD%90%E7%AF%AE%E7%90%83%E9%9E%8B/pid-11890058/pgid-11393222'
 	#spurl=json.loads(r.text)['data'][0]['task_url']

 	
	
	if stid=='3':
		nike(spurl)

	if stid=='1':
		adidas(spurl,size_valueList)

