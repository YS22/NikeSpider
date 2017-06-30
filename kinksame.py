# 程序基本框架
import requests 
...
...

def nike(nikeUrl,spurl,registerinfo):
	pass
	return payurl 
	
def adidas(adidasUrl,spurl,registerinfo):
	pass
	return payurl

def apple(appleUrl,spurl,registerinfo):
	pass
	return payurl

...  #待加入平台函数

# 以下数据是后台获得
registerUrl=""
splurl=""
registerinfo={}

if registerUrl==nikeUrl:
	payurl=nike(nikeUrl,spurl,registerinfo)
	
if registerUrl==adidasUrl:
	payurl=adidas(adidasUrl,spurl,registerinfo)
	
if registerUrl==appleUrl:
	payurl=apple(appleUrl,spurl,registerinfo)
	
... #待加入平台
