# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import pytesseract
import StringIO
from PIL import Image
from selenium import webdriver
import time

def addcart():
	"""
	1.商品加入购物车
	2.完成登陆
	"""
	browser=webdriver.PhantomJS()
	print 'browser...'
	browser.get('http://www.adidas.com.cn/br7144')
	print 'get ok'
	time.sleep(3)
	style_btn=browser.find_element_by_xpath('html/body/div[7]/div/div[1]/div[2]/div[3]/form/div[1]/div[1]/div[1]/div[2]/em')
	#style_btn = browser.find_element_by_class_name('selectVal')
	style_btn.click()

	selectStyle_btn = browser.find_element_by_xpath('html/body/div[7]/div/div[1]/div[2]/div[3]/form/div[1]/div[1]/div[2]/div/span[1]')  
	selectStyle_btn.click()

	add_btn = browser.find_element_by_xpath('html/body/div[7]/div/div[1]/div[2]/div[3]/form/div[2]/a')
	add_btn.click()
	time.sleep(6)

	#如果上一个add_btn的内容还未加载出来这个会报错找到合适time.sleep(5)可以解决
	catr_btn = browser.find_element_by_xpath('html/body/div[12]/div[1]/div[2]/div[2]/div[2]/a[2]')
	catr_btn.click()
	time.sleep(1)

	# 输入用户名,密码  
	username = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/div[1]/input')  
	password = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/div[2]/input')  
	username.clear()  
	username.send_keys('ys95279521') 
	password.clear()  
	password.send_keys('112358yS')  
	      
	# 提交登陆  
	login_btn = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/a')  
	login_btn.click() 
	time.sleep(1)



if __name__=='__main__':
	addcart()