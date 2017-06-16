# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import pytesseract
import StringIO
from PIL import Image
import sys
reload(sys)   
sys.setdefaultencoding('utf8')

#注册
infoHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
          'Referer':'https://www.adidas.com.cn/customer/account/create/'}
regUrl="https://www.adidas.com.cn/customer/account/createpost/"
cookie=requests.get(regUrl,headers=infoHead).cookies
print cookie

regHead= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
          'Referer':'https://www.adidas.com.cn/customer/account/create/',
          'cookie':'utag_main=v_id:015ca4469ca7004a978e3c4743101c048003200d00bd0$_sn:5$_ss:0$_st:1497576490801$ses_id:1497574600286%3Bexp-session$_pn:3%3Bexp-session; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C17334%7CMCMID%7C76771862484335116949050987265245610648%7CMCAAMLH-1498009510%7C11%7CMCAAMB-1498179400%7Chmk_Lq6TPIBMW925SPhw3Q%7CMCOPTOUT-1497581800s%7CNONE%7CMCAID%7CNONE; __v3_c_sesslist_11403=equgad51u9_ddh%252Ceqtpqh2eta_ddg%252Cddg%252Cddf%252Cddf%252Cddf; __v3_c_review_11403=5; __v3_c_last_11403=1497574639204; __v3_c_visitor=1497404742163628; s_pers=%20s_vnum%3D1498838400124%2526vn%253D5%7C1498838400124%3B%20v56%3D%255B%255B%2527EXTERNAL%252520CHANNEL%2527%252C%25271497574600868%2527%255D%255D%7C1655341000868%3B%20pn%3D7%7C1500166600876%3B%20c4%3DACCOUNT%257CCREATE%2520PROFILE%7C1497576754643%3B%20s_invisit%3Dtrue%7C1497576754653%3B; _ga=GA1.3.624641298.1497404712; _gid=GA1.3.604441172.1497404712; Hm_lvt_690ef42ff30759b60f6c189b11f82369=1497405447,1497408891,1497488705,1497516920; Hm_lvt_c29ad6ea0a27499743676357b8867377=1497405447,1497408891,1497488705,1497516920; __v3_c_isactive_11403=1; __v3_c_uactiveat_11403=1497408475066; ak_bmsc=3AA66830857E2796FC0CCB748DC24FB8DB9A411EFF3C0000E62C4359748CF176~pl7NLUERVXeUiqJ4qc9c/RLhKYmd2EWvFAPQeYEp/LQ1J91CH3ZeQB5DkbaCHX1YPaR6gYnhkY5eoJIH7xqaV1B75+Ovd/EuascJSasholnSsJM79yFJSjQCE8OXnk6vJdL4wjQbc+xyKQBqa/GveSwjzbIcXNo2JfUn4Bv7Lu8hG+wQm35GGfBFqP/DclIkAM3vae3D/HJOYoPBvP05AAqOERxFDX8xOZDEgKTuRsMsJdfzbjz1pp3grl/T18KqSx; bm_mi=B8E73C2E07E2428BAF163D7615C2FD21~h20V1qPu+I0ZzsvYGCrrMPn+0DtGMzo7+YdQCgx6+h/xAyF6fnCRPwrHzouaYwFxkRWaIUE3bfV8mVQxGaei0pa+wmVcqwjUvTtSbzXhaNeBJS9oTwwQAUdaHC2z3ivupzGGVoT17pS7lAw8Yov8gnfGuCHBz33093w5FMCxIOspNP/C184GJq/1cSl18PoDM7qNjMh4jgzV5cC7b6wpcIZ83PG4NUgUjB4gtFLWOosiXKq2bF70vCdgi44TE5xRrXVTqhd4hhA0LaRBNyp7PQ==; frontend=dt7q7d6ipt57l7cror4jn8v0c2; bm_sv=11824BC29F9AA812E06BE6A406A87254~f+tpQWADm8X3CIejpOlZ5W6hfUzXG4AcAzKm/tJGBhMM5BDUhZRuX8pfPXZHLhNEvP+6DlZ0/rhp70pZj6iVqLDbLYk2UjorL5DVGBPKnE96OQsNjcye07CdVJLgPkksn9xIYUiapMS47AwY9fJ9kPcTDtnh1BUUrziNyGBt6kY=; __v3_c_pv_11403=3; __v3_c_session_11403=1497574631124369; __v3_c_today_11403=1; __v3_c_session_at_11403=1497574691170; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; s_cc=true; s_sq=ag-adi-cn-prod%3D%2526pid%253DACCOUNT%25257CCREATE%252520PROFILE%2526pidt%253D1%2526oid%253D%2525E6%2525B3%2525A8%2525E5%252586%25258C%2526oidt%253D3%2526ot%253DSUBMIT; frontend=dt7q7d6ipt57l7cror4jn8v0c2'}


infoUrl='https://www.adidas.com.cn/customer/account/create/'
html=requests.get(infoUrl,headers=infoHead).text
#print html
#获得token
soup=BeautifulSoup(html,'html.parser')
token=soup.select('input')[1]['value']
#print token
#获得验证码
imageUrl=soup.select('#captchaCode1')[0]['src']
imageHtml=requests.get(imageUrl,headers=infoHead).content
imgFile=StringIO.StringIO(imageHtml) #缓存图片
img=Image.open(imgFile)
#print img
vcode = pytesseract.image_to_string(img)
#print (vcode)
regData={
 		 'token':token,
         'firstname':'yangsheng99',
         'mobile':'17786596348',
         'gender':'1',
         'day':'2',
         'year':'1994',
         'dob':'1994-3-2',
         'osolCatchaTxt':vcode,
         'osolCatchaTxtInst':1,
         'email':'cky24@qq.com',
         'username':'yeelink11',
         'password':'112358yS',
         'confirmation':'112358yS',
         'agree_terms':1
}

regHtml= requests.post(regUrl,data=regData,headers =regHead)
#print regHtml.text
# # 登陆
# loginUrl="https://www.adidas.com.cn/customer/account/login/"
# head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'http://store.nike.com/cn/zh_cn/'}
# data={"login[username]":"cky12t@qq.com","login[password]":"112358yS","rememberMe":"true"}
# loginhtml = requests.post(loginUrl,data= data,headers = head)
# print loginhtml.text
# print "登陆状态:"
# print loginhtml.status_code



