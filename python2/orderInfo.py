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


def nike():
	pass
	
	
def adidas(data):
	loginHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	 		   'Referer': 'https://www.adidas.com.cn/customer/account/login/'}
	
	orderUrl='https://www.adidas.com.cn/sales/guest/view/'
	orderHtml=requests.post(orderUrl,data=data,headers=loginHead)
	ordersoup=BeautifulSoup(orderHtml.text,"html.parser")
	orderNumber=ordersoup.select('title')[0]
	print orderNumber.text
	styleNumber=ordersoup.select('.wd90')[0]
	print "款号:",styleNumber.text
	size=ordersoup.select('.proShow span')[0]
	print '尺寸:',size.text
	qty=1#orderinfosSoup.select('.pl25')[0]
	print '数量:',qty
	total=ordersoup.select('.price')[0]
	print '总价:',total.text
      
	
if __name__ == '__main__':
	website='1'
	data={'oar_email':'leishaofa@163.com', 'oar_order_id':'2244796163'}
	#平台选择
	if website=='3':
		nike()

	if website=='1':
		adidas(data)

