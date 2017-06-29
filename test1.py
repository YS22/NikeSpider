# -*- coding: utf-8 -*-
# 程序基本框架
import requests 
# ...

def nike(spurl,registerinfo,userinfo):
    pass
    return payurl 
    
def adidas(spurl,registerinfo,userinfo):
    pass
    return payurl

def apple(spurl,registerinfo,userinfo):
    pass
    return payurl


nikeUrl='https://store.nike.com/cn/zh_cn'
adidasUrl='http://www.adidas.com.cn/'
appleUrl='https://www.apple.com/cn/'

weburl=''
splurl=""
userinfo={}
registerinfo={}



if registerUrl==nikeUrl:
    payurl=nike(spurl,registerinfo,userinfo)
    
if registerUrl==adidasUrl:
    payurl=adidas(spurl,registerinfo,userinfo)
    
if registerUrl==appleUrl:
    payurl=apple(spurl,registerinfo,userinfo)