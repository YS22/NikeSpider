import requests
from PIL import Image
from bs4 import BeautifulSoup
# appleurl='https://appleid.apple.com/account?localang=zh_CN#!&page=create'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
# 	  'Referer':'https://appleid.apple.com/account'
# }
# html=requests.get(appleurl,headers=head).text
# print html
# soup=BeautifulSoup(html,'html.parser')
# image=soup.select('img')
# print image
softurl='http://upload.chaojiying.net/Upload/Processing.php'
data={
	  'user':'yangsheng11',
	  'password':'112358ys',
	  'softid':'893587',
	  'codetype':'1006',
	  'userfile':Image.open(r'C:\Users\Administrator\Desktop\test')}
res=requests.post(softurl,data=data)
print res.text