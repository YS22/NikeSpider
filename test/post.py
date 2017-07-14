# -*- coding: utf-8 -*-
import requests
from PIL import Image
from bs4 import BeautifulSoup
import json
#from lxml import etree

appleUrl='https://appleid.apple.com/account?&localang=CN-ZH#!&page=create'
appleHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
	  'Referer':'https://appleid.apple.com/account?&localang=CN-ZH#!&page=create'}
html=requests.get(appleUrl,headers=appleHead)
cookie=html.cookies


# captchaUrl='https://appleid.apple.com/captcha'
# captchaHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
# 	  'Referer':'https://appleid.apple.com/account?&localang=CN-ZH&app_id=2083&returnURL=https%3A%2F%2Fsecure1.store.apple.com%2Fcn%2Fshop%2Fsign_in%3Fc%3DaHR0cHM6Ly93d3cuYXBwbGUuY29tL2NuLy8_YWZpZD1wMjM4JTdDMVo2eXQ0aUJ2LWRjX210aWRfMTg3MDd2eHUzODQ4NF9wY3JpZF8xNDk3MjQ0MDkyOV8mY2lkPWFvcy1jbi1rd2JhLWJyYW5kfDFhb3M3YTc4YmJlZTZhMDhlODBiYTAyMjU3MmQzZDM3NmIyMTIyYTU3ZjM4%26r%3DSCDHYHP7CY4H9XK2H%26s%3DaHR0cHM6Ly93d3cuYXBwbGUuY29tL2NuLy8_YWZpZD1wMjM4JTdDMVo2eXQ0aUJ2LWRjX210aWRfMTg3MDd2eHUzODQ4NF9wY3JpZF8xNDk3MjQ0MDkyOV8mY2lkPWFvcy1jbi1rd2JhLWJyYW5kfDFhb3M3YTc4YmJlZTZhMDhlODBiYTAyMjU3MmQzZDM3NmIyMTIyYTU3ZjM4',
# 	  'cookie':str(cookie)
# 	  }
# payload={'type': "IMAGE"}
# info=requests.post(captchaUrl,headers=captchaHead,data=payload)
# print info.text

## xpath抓取
# selector=etree.HTML(html)
# img=selector.xpath(".//*[@id='idms-step-1497929972721-0']/div[2]/div/div/div[6]/div/create-captcha/div/div/div/div/div[1]/div/idms-captcha/div/img")
# print img

## BeautifulSoup抓取
# soup=BeautifulSoup(res,'html.parser')
# imageinfo=soup.select('img')
# print imageinfo

## 超级鹰soft
# softurl='http://upload.chaojiying.net/Upload/Processing.php'
# data={
# 	  'user':'yangshneg11',
# 	  'pass':'112358ys',
# 	  'softid':'893594',
# 	  'codetype':'1006',
# 	  'file_base64':'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'
# }
# res=requests.post(softurl,data=data)
# print res.text

