
# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0") #设置user-agent请求头
dcap["phantomjs.page.settings.loadImages"] = False #禁止加载图片
driver = webdriver.PhantomJS(desired_capabilities=dcap)
#driver.set_page_load_timeout(30) #设置页面最长加载时间为40s
try:
	driver.get("https://www.adidas.com.cn/customer/account/login/")
	username = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/div[1]/input')  
	password = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/div[2]/input')  
	username.clear()  
	username.send_keys('ys95279521') 
	password.clear()  
	password.send_keys('112358yS')  
	      
	# 提交登陆  
	login_btn = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/a').click() 
	time.sleep(1)
	print "登陆成功"
	cookies=driver.get_cookies
	regUrl="https://www.adidas.com.cn/customer/account/createpost/"
	reghtml=requests.get(regUrl,headers=loginHead,cookies=cookies)
	print reghtml.text
	#print driver.page_source
	driver.quit()

except:
	print "退出浏览器"
	driver.quit() #退出浏览器