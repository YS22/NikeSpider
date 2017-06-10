import requests
from bs4 import BeautifulSoup
import sys
reload(sys)   
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup

loginUrl="https://www.nike.com/profile/login?Content-Locale=zh_CN"
head= {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0','Referer': 'http://store.nike.com/cn/zh_cn/'}
data={"login":"cky111@qq.com","password":"Nikecky111","rememberMe":"true"}
loginhtml = requests.post(loginUrl,data= data,headers = head)
# print loginhtml.text
c= loginhtml.cookies
#print c

cartUrl="https://secure-store.nike.com/cn/checkout/html/cart.jsp?country=CN&country=CN&l=cart&country=cn&lang_locale=zh_cn&site=nikestore"
carthead= {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0','Referer': 'http://store.nike.com/cn/'}

cookies= dict(AnalysisUserId= c["AnalysisUserId"],
          ak_bmsc= c["ak_bmsc"],
          llCheck= c["llCheck"],
          slCheck= c["slCheck"],
          sls= c["sls"],
          NIKE_COMMERCE_COUNTRY='CN')

carthtml = requests.get(cartUrl,headers = carthead,cookies=cookies)
html=carthtml.text
#print html

soup=BeautifulSoup(html,'html.parser')
for item in soup.select('.ch4_cartItemContent'):
    price=item.select('p')[0].text
    dsc=item.select('p')[1].text
    a=item.select('a')[0]['href']
    print price
    print dsc
    print a