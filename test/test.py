# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import requests
from bs4 import BeautifulSoup
import pytesseract
import StringIO
from PIL import Image
#注册
browser=webdriver.Chrome()
browser.get("https://www.adidas.com.cn/customer/account/create/")
time.sleep(1)
#注册提交字段
name = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[1]/div/input')
tel = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[2]/input')
gender_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[3]/p[2]/span[2]/em')  
gender_btn.click()
day_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[4]/div[1]/div[1]/div[2]/em')  
day_btn.click()
dayValue_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[4]/div[1]/div[2]/div/span[21]')  
dayValue_btn.click()
mon_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[4]/div[2]/div[1]/div[2]/em')  
mon_btn.click()
monValue_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[4]/div[2]/div[2]/div/span[2]')  
monValue_btn.click()
year_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[4]/div[3]/div[1]/div[2]/em')  
year_btn.click()
yearValue_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[4]/div[3]/div[2]/div/span[25]')  
yearValue_btn.click()
#验证码
verify_code = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[1]/div[5]/div[1]/input[1]')  
#verify_code_ = raw_input('verify_code')
#获取验证码
# infoUrl='https://www.adidas.com.cn/customer/account/create/'
# infoHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
#           'Referer':'https://www.adidas.com.cn/customer/account/create/'}

#html=requests.get(infoUrl,headers=infoHead).text
html = browser.page_source
soup=BeautifulSoup(html,'html.parser')
imageUrl=soup.select('#captchaCode1')[0]['src']
imageHtml=requests.get(imageUrl,headers=infoHead).content
imgFile=StringIO.StringIO(imageHtml) #缓存图片
img=Image.open(imgFile)
#print img
vcode = pytesseract.image_to_string(img)
verify_code.clear()  
verify_code.send_keys(vcode)
#输入验证码结束
email = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[2]/div[1]/div/input')
username = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[2]/div[2]/div/input')
password = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[2]/div[3]/div/input')
conpassword = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/div[2]/div[4]/input')
# 提交输入框数据
name.clear()  
name.send_keys(u'杨胜') 
tel.clear()
tel.send_keys('17786493831')
email.clear()
email.send_keys('1774507012@qq.com')
username.clear()
username.send_keys('adidasyangsheng')
password.clear()
password.send_keys('112358YS')
conpassword.clear()
conpassword.send_keys('112358YS')
# 提交注册
reg_btn = browser.find_element_by_xpath('html/body/div[5]/div[1]/form/div/button')  
reg_btn.click()

###登陆添加购物车的实现
# browser=webdriver.Chrome()
# # 进入商品页面
# browser.get('http://www.adidas.com.cn/br8706')
# time.sleep(1)
# sub_btn = browser.find_element_by_xpath('html/body/div[7]/div/div[1]/div[2]/div[3]/form/div[1]/div[1]/div[1]/div[2]/em')  
# sub_btn.click()
# time.sleep(1)

# sub1_btn = browser.find_element_by_xpath('html/body/div[7]/div/div[1]/div[2]/div[3]/form/div[1]/div[1]/div[2]/div/span[1]')  
# sub1_btn.click()
# time.sleep(1)

# add_btn = browser.find_element_by_xpath('html/body/div[7]/div/div[1]/div[2]/div[3]/form/div[2]/a')
# add_btn.click()
# time.sleep(4)

# #如果上一个add_btn的内容还未加载出来这个会报错找到合适time.sleep(5)可以解决
# catr_btn = browser.find_element_by_xpath('html/body/div[13]/div[1]/div[2]/div[2]/div[2]/a[2]')
# catr_btn.click()
# time.sleep(1)

# # 输入用户名,密码  
# username = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/div[1]/input')  
# password = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/div[2]/input')  
# username.clear()  
# username.send_keys('ys95279521') #用户名
# password.clear()  
# password.send_keys('112358yS')   #密码
      
# # 提交登陆  
# login_btn = browser.find_element_by_xpath('html/body/div[5]/div/div[2]/div[1]/div/form/a')  
# login_btn.click() 
# time.sleep(1)
# #到此处商品已加入用户购物车

