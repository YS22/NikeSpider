# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
import time 

def register():
	"""
	多平台注册
	"""
	regUrl='' #变量
	regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	          'Referer':'http://store.nike.com/cn/zh_cn/'}
	regData={} #变量
	requests.post(regUrl,data=json.dumps(regData),headers =regHead)

def addcart():
	"""
	1.添加货物到购物车
	2.实现登陆
	"""
	browser=webdriver.PhantomJS()
	print 'browser...'
	browser.get('http://store.nike.com/cn/zh_cn/pd/air-zoom-pegasus-34-%E5%A5%B3%E5%AD%90%E8%B7%91%E6%AD%A5%E9%9E%8B/pid-11792697/pgid-11631050')
	time.sleep(5)
	print "get ok"
	# style_btn=browser.find_element_by_xpath('html/body/div[9]/div/div/div/div/div[1]/div[2]/div[3]/div[1]/ul/li[1]/a/img').click()
	# time.sleep(1)
	# size_btn=browser.find_element_by_xpath('html/body/div[9]/div/div/div/div/div[1]/div[2]/div[4]/form/div[1]/div/a').click()
	# selectSize_btn=browser.find_element_by_xpath('html/body/div[9]/div/div/div/div/div[1]/div[2]/div[4]/form/div[1]/div/div[2]/ul/li[6]').click()
	# time.sleep(1)
	# add_btn=browser.find_element_by_xpath('html/body/div[9]/div/div/div/div/div[1]/div[2]/div[4]/form/div[2]/button').click()
	# time.sleep(10)
	# to_cart=browser.find_element_by_xpath('html/body/div[6]/nav/div[1]/ul[2]/li[5]/a/span').click()
	# time.sleep(1)
	# to_login_btn=browser.find_element_by_xpath('html/body/div[2]/div[1]/div[5]/a/span').click()
	# email_input=browser.find_element_by_xpath('html/body/div[2]/div[1]/div[5]/div/form[1]/div[4]/input')
	# email_input.clear()
	# email_input.send_keys('cky111@qq.com')
	# password_input=browser.find_element_by_xpath('html/body/div[2]/div[1]/div[5]/div/form[1]/div[5]/input')
	# password_input.clear()
	# password_input.send_keys('Nikecky111')
	# login_btn=browser.find_element_by_xpath('html/body/div[2]/div[1]/div[5]/div/form[1]/div[8]/input').click()

if __name__ == '__main__':
	#register()
	addcart()




