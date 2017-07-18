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


def nike(spurl,addressinfo):
	#添加购物车
	head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	 		   'Referer': 'https://www.adidas.com.cn/customer/account/login/'}
	spHtml=requests.get(spurl,headers=head)
	spCookie=spHtml.cookies
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
		  'action':action,
		  'lang_locale':lang_locale,
		  'country':country,
		  'catalogId':catalogId,
		  'productId':productId,
		  'price':price,
		  'siteId':'null',
		  'passcode':'null',
		  'sizeType':'null',
		  'qty':qty,
		  'skuAndSize':'15811028:36.5',#尺码参数
		  'rt':'json',
		  'view':'3',
		  'skuId':'15811028',#尺码参数
		  'displaySize':'36.5',#尺码参数
		  '_':'1500376125723'} #时间参数，可以固定
	params = urllib.urlencode(info)
	print params

	addHead={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
			 'referer':spurl}
	url='https://secure-store.nike.com/ap/services/jcartService?'+params #参数从RUL传递
	add=requests.get(url,headers=addHead,cookies=spCookie)
	print add.status_code
	print add.text
	
	# 添加收货信息
	url='https://secure-store.nike.com/ap/services/jcartService?action=getCartSummary&rt=json'
	#upm=json.loads(requests.get(url,headers=head,cookies=spCookie).text)['profileId']
	upm=requests.get(url,headers=head,cookies=spCookie)
	cookie=upm.cookies
	upm=json.loads(upm.text)['profileId']
	print upm
	if upm:
		addressUrl='https://www.nike.com/profile/services/users/'+upm+'/addresses'
		data={"additionalPhoneNumber":"",
			  "address1":"江夏",
			  "address2":"",
			  "address3":"",
			  "city":"绥化市",
			  "country":"CN",
			  "firstName":"胜",
			  "id":'',
			  "lastName":"杨",
			  "otherName":'',
			  "phoneNumber":"17786493932",
			  "postalCode":"432000",
			  "preferred":'true',
			  "state":"CN-23",
			  "type":"SHIPPING",
			  "district":"15488",
			  "countyDistrict":"安达市"}
		address=requests.post(addressUrl,data=json.dumps(data),headers=head,cookies=cookie)
		print address.status_code
		print address.text

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
	
	
def adidas(spurl,addressinfo,size_valueList):
	"""
	1.商品抢购
	2.填写收货信息
	3.生成订单
	4.提取付款链接和订单编号
	"""
	loginHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	 		   'Referer': 'https://www.adidas.com.cn/customer/account/login/'}
	spHtml=requests.get(spurl,headers=loginHead) #info['data'][0]['task_url']商品链接
	soup=BeautifulSoup(spHtml.text,'html.parser')
	sptitle=soup.select('title')[0].text
	price=soup.select('.pdpPrice')[0].text.replace(' ', '')
	price='\n'.join(price.split())
	script=soup.select('script')[-4]
	productid=str(script).split(',')[2].split('+')[1]
	#print productid
	infoUrl='http://www.adidas.com.cn/specific/product/ajaxview/?id='+productid
	infoHml=requests.get(infoUrl,headers=loginHead)

	infosoup=BeautifulSoup(infoHml.text,'html.parser')
	sizeHtml=infosoup.select('#size_box')[0]
	token=infosoup.select('input')[0]['value']
	isajax=infosoup.select('input')[1]['value']
	release2=infosoup.select('input')[2]['value']
	product=infosoup.select('input')[3]['value']
	super_attribute=infosoup.select('.size')[0]['name']
	#print super_attribute


	# 2 抢购
	while True:
		print "开始抢购"
		addurl='http://www.adidas.com.cn/checkout/cart/add/'
		addHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
				 'Referer': spurl,
				 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}

		# sizeValue=random.sample(size_valueList,1)[0] 随机一个尺码
		for sizeValue in size_valueList:
			print sizeValue
			params = {'token':token,'isajax':isajax,'release2':release2,'product':product,super_attribute:sizeValue,'qty':'1'}        
			payload= urllib.urlencode(params)
			print payload
			#print type(payload)
			addcart=requests.post(addurl,data=payload,headers=addHead)
			cartCookie=addcart.cookies
			#print cartCookie
			print addcart.status_code
			if addcart.url=='http://www.adidas.com.cn/checkout/cart/add/': #判断是否抢购成功
				#开始下单
				##1.获取地区id
				zone={'北京':'485','天津':'515','河北省':'486','山西省':'487','内蒙古':'488','辽宁省':'489','吉林省':'490','黑龙江':'491','上海':'492','江苏省':'493','浙江省':'494','安徽省':'495','福建省':'496','江西省':'497','山东省':'498','河南省':'499','湖北省':'500','湖南省':'501','广东省':'502','广西':'503','海南省':'504','重庆':'505','四川省':'506','贵州省':'507','云南省':'508','西藏':'509','陕西省':'510','甘肃省':'511','青海省':'512','宁夏':'513','新疆':'514'}
				region_id=zone[addressinfo['region']]
				if region_id:
					cityData={'region_id':region_id}
					cityHtml=requests.post('https://www.adidas.com.cn/specific/ajaxcustomer/ajaxcity',data=cityData,headers=loginHead)
					#print cityHtml.text.decode("unicode-escape") #unicode转中文
					dic=json.loads(cityHtml.text)
					#print dic
					city_id=list(dic.keys())[list(dic.values()).index(addressinfo['city'].decode('utf-8'))]
					print city_id
					if city_id:
						districtData={'city_id':city_id}
						districtHtml=requests.post('https://www.adidas.com.cn/specific/ajaxcustomer/ajaxdistrict',data=districtData,headers=loginHead)
						#print districtHtml.text.decode("unicode-escape")
						dic=json.loads(districtHtml.text)
						#print dic
						district_id=list(dic.keys())[list(dic.values()).index(addressinfo['district'].decode('utf-8'))]
						print district_id


						infoUrl='https://www.adidas.com.cn/yancheckout/process/'
						html=requests.get(infoUrl,headers=loginHead,cookies=cartCookie)
						#print html.text
						soup=BeautifulSoup(html.text,"html.parser")
						token=soup.select('input')[18]['value'] #20
						print token
						#shipping_address_id=soup.select('input')[18]['value'] #18 添加之前添加收货地址才会有shipping_address_id
						#print shipping_address_id
						addresUrl='https://www.adidas.com.cn/yancheckout/process/saveShippingAndPayment/'
						userinfo={'shipping[firstname]':addressinfo['firstname'],
									'shipping[email]':addressinfo['email'],
									'shipping[country_id]':'CN',
									'shipping[region_id]':region_id,
									'shipping[region]':addressinfo['region'],
									'shipping[city_id]':city_id,
									'shipping[district_id]':district_id,
									'shipping[city]':addressinfo['city'],
									'shipping[district]':addressinfo['district'],
									'shipping[street][]':addressinfo['street'],
									'shipping[postcode]':addressinfo['postcode'],
									'shipping[mobile]':addressinfo['mobile'],
									'shipping[tel_areacode]':'',
									'shipping[telephone]':'',
									'shipping[save_in_address_book]':'1',
									'shipping[use_for_shipping]':'1',
									'shipping[update_region]':'0',
									'shipping[primary_shipping]':'1',
									'shipping[primary_billing]':'1',
									'shipping[delivery_memo]':addressinfo['delivery_memo'],
									'delivery_type':'Normal',
									'token':token,
									'payment[alipay_pay_bank]':'ALIPAY',
									'payment[alipay_pay_method]':'bankPay',
									'shipping_method':'carrier_bestway',
									'fapiao[fapiao_type]':'personal',
									'fapiao[fapiao_title]':'',
									'fapiao[fapiao_memo]':''}
						data = urllib.urlencode(userinfo)
						add_head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
								 'Referer': 'https://www.adidas.com.cn/yancheckout/process/',
								 'Content-Type':'application/x-www-form-urlencoded'}
						add_addres=requests.post(addresUrl,data=data,headers=add_head,cookies=cartCookie)
						#print add_addres.text
						print add_addres.status_code
						# 提取付款链接
						soup=BeautifulSoup(add_addres.text,"html.parser")
						url=soup.select('a')[2]
						#print url
						zhifuhtml=requests.get(url['href'],headers=loginHead).text
						zhifusoup=BeautifulSoup(zhifuhtml,"html.parser")
						payurl=zhifusoup.select('input')[8]['value']
						orderNumber=zhifusoup.select('.long-content')[0].text.replace(' ', '')
						orderNumber='\n'.join(orderNumber.split())
						print '订单编号:',orderNumber
						print '支付链接:',payurl
						print '商品名称:',sptitle
						print '价格:',price
						break
		break
	
if __name__ == '__main__':
	# 拉取数据
	# loginHead={'User-Agent':'FLASHSALE',
	# 		   'Referer': 'http://store.nike.com/cn/zh_cn/'}
 # 	r=requests.get('http://sale.com/index.php/Rpc/planTask',headers=loginHead)

 # 	info= json.loads(r.text)
 # 	if info['code'] is 1:  #(当状态为1时，表示接收到了抢购任务)

 		# 平台标识(1：阿迪达斯 2：苹果 3：耐克)
	website='3' #info['data'][0]['site_id'] #获取平台标识方法

	# 数据处理区
	#info['data'][0]['task_url'] #获取spurl方法
	spurl='https://store.nike.com/cn/zh_cn/pd/tanjun-女子运动鞋/pid-10869064/pgid-11840210'
	
	addressinfo={ 'firstname':'庄婵冰',
              'region':'湖北省',
		      'city':'武汉市',
		      'district':'汉阳区',
		      'street':'高新6路藏龙星天地',
		      'delivery_memo':'这是一个送货备注',
		      'postcode':'420105',
		      'mobile':'18827448197',
		      'email':'leishaofa@163.com'
		      }

	size_valueList=[69]#json.loads(info['data'][0]['rules'])['allSize'][1] #获取尺码的方法
	

	#平台选择
	if website=='3':
		nike(spurl,addressinfo)

	if website=='1':
		adidas(spurl,addressinfo,size_valueList)

