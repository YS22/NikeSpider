# 流程
## 模拟用户注册登陆
- 目标网站
- 注册和登陆信息
- 手机，邮箱的验证码

## 登陆成功抢购商品
- 抢购商品，提取抢购成功订单付款链接
- 提交付款链接


## 物流追踪
- 付款用户信息
- 模拟用户登陆查询物流跟踪


# 问题
- 哪些目标网站
- 每个网站分开做？
- 注册验证，手机验证，邮箱验证
- 登陆验证，每个网站登陆验证方式不同
- 需要抢购的商品？
- 抢购商品的样式？
- 怎么模拟点击生成订单(post样式数据)
- 获得付款链接

# Nike 
### 注册信息(注册不需要验证码)
- 注册url: https://unite.nike.com/join
- 需要提交的字段
```
"username":"1774507013@qq.com" ,
"password":"112358yS"(写死)
"lastName:":"杨",
"firstName":"胜",
"dateOfBirth":"1994-01-20"(写死)
"country":"CN"(写死)
"mobileNumber":"17786493932",
"gender":"male"(写死)
"receiveEmail":true(写死)
```
- 耐克中邮箱和手机号要生成，其余可以写死
- 无验证码

### 添加购物车流程
- 进入需要购买商品链接
- 提交颜色，尺码等信息加入购物车
- 同一种商品不同用户加入购物车时post的数据
####同一个人同一种商品(相同upm,analysisUserId,guid,cookies,deviceAtlas,platform,source  不同：t,event里面的t)
```
{"t":1498033109322,
"upm":"16076584660",
"analysisUserId":"WUDmUwoMQ10AACGkllAAAARv",
"guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05",
"cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},

"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1",
"platform":{"id":"nike.com","v":"main"},
"source":{"id":"dreamcatcher","v":"3.29.2"},
"events":[{"pid":"11454915","qty":"1",
           "skuAndSize":"18466798:40",
           "name":"addToCartEvent",
           "t":1498033109319,
           "url":"http://store.nike.com/cn/zh_cn/pd/air-jordan-4-retro-复刻男子运动鞋/pid-11454915/pgid-11088472",
           "swoosh":false,
           "location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},

           "guidS":"a84e884d-055e-49ed-f3a1-f794eb8747f0"}]}

```

```
{"t":1498032437308,"upm":"16076584660","analysisUserId":"WUDmUwoMQ10AACGkllAAAARv","guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05","cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1","platform":{"id":"nike.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11454915","qty":"1","skuAndSize":"18466798:40","name":"addToCartEvent","t":1498032437304,"url":"http://store.nike.com/cn/zh_cn/pd/air-jordan-4-retro-复刻男子运动鞋/pid-11454915/pgid-11088472","swoosh":false,"location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},"guidS":"a84e884d-055e-49ed-f3a1-f794eb8747f0"}]}
```
以上数据能找到出处的：analysisUserId，
- 重新构造data

### 结算

# adidas
### 注册信息（注册需要数字验证码）
- 需要提交的字段
```
token(html中获取)
firstname：杨胜
mobile：17786493932
gender：male
day：2
year：1994
dob：1994-3-2
osolCatchaTxt(验证码)
osolCatchaTxtInst(不用管)
email
username:yangsheng
password
confirmation(密码确认)
agree_terms(不用管)
```
- 阿迪达斯中mobile,email,username要生成，其余可以写死或页面爬取

### 加入购物车问题
- 
- 要post的内容在类似http://www.adidas.com.cn/specific/product/ajaxview/?id=348123的链接里面
- 如何获得这个链接？
- 提交购物车需要post的字段
```
token:98f5feff8f4740794cfb2f577f873600(网页中获取)
isajax:yes(可固定)
release2:yes(可固定)
product:348111(产品id)
super_attribute[184]:95(尺码)
qty:1(数量)
```

# apple
## 注册问题
- 邮箱验证
- 验证码(干扰线，重叠)-->(打码平台解决)
- 验证码直接请求注册页面得不到

### 获得验证码
- 需要模拟请求获得验证码



# 任务
- 完成3个网站的注册登陆



  
# 第一步
- 获取信息
```
token:c2f042f91848322c15d55510f70f6410
isajax:yes
release2:yes
product:346598
super_attribute[185]:52
qty:1
```
http://www.adidas.com.cn/specific/product/ajaxview/?id=352549(信息在这个链接)
如何获取id

# 第二步
- 构造data
1
```
{"t":1498895696600,"upm":"16148434344","analysisUserId":"118.123.105.20.300811496813701754","guidU":"89eb2d42-da51-4460-85ab-c27f62ff6deb"
,"cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"ocp\":{}}","neo.swimlane":"22"
},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/10|bcookieSupport:1","platform":{"id":"nike
.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11382127","qty":"1","skuAndSize"
:"18294708:42","name":"addToCartEvent","t":1498895696597,"url":"https://store.nike.com/cn/zh_cn/pd/air-zoom-pegasus-34-
男子跑步鞋/pid-11382127/pgid-11631049","swoosh":false,"location":{"cc":"CN","rc":"HN","tp":"vhigh","tz":"GMT
+8","la":"28.20","lo":"112.97","bw":"5000"},"guidS":"12f9ac20-3154-4996-d72c-75242d07dd32"}]}


```
2
```
{"t":1498896324473,"upm":"16148434344","analysisUserId":"118.123.105.20.300811496813701754","guidU":"89eb2d42-da51-4460-85ab-c27f62ff6deb"
,"cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"ocp\":{}}","neo.swimlane":"22"
},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/10|bcookieSupport:1","platform":{"id":"nike
.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11198752","qty":"1","skuAndSize"
:"17256559:M","name":"addToCartEvent","t":1498896324470,"url":"https://store.nike.com/cn/zh_cn/pd/dry-knit-
男子短袖跑步上衣/pid-11198752/pgid-11402153","swoosh":false,"location":{"cc":"CN","rc":"HN","tp":"vhigh","tz"
:"GMT+8","la":"28.20","lo":"112.97","bw":"5000"},"guidS":"12f9ac20-3154-4996-d72c-75242d07dd32"}]}
```
3
```
{"t":1498897985229,"upm":"16148434344","analysisUserId":"118.123.105.20.300811496813701754","guidU":"89eb2d42-da51-4460-85ab-c27f62ff6deb"
,"cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"ocp\":{}}","neo.swimlane":"22"
},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/10|bcookieSupport:1","platform":{"id":"nike
.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11597116","qty":"1","skuAndSize"
:"19264597:36.5","name":"addToCartEvent","t":1498897985227,"url":"https://store.nike.com/cn/zh_cn/pd
/loden-女子运动鞋/pid-11597116/pgid-11631130","swoosh":false,"location":{"cc":"CN","rc":"HN","tp":"vhigh"
,"tz":"GMT+8","la":"28.20","lo":"112.97","bw":"5000"},"guidS":"12f9ac20-3154-4996-d72c-75242d07dd32"
}]}
```


{"t":1498895698156,"upm":"16148434344","analysisUserId":"118.123.105.20.300811496813701754","guidU":"89eb2d42-da51-4460-85ab-c27f62ff6deb"
,"cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"ocp\":{}}","neo.swimlane":"22"
},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/10|bcookieSupport:1","platform":{"id":"nike
.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"name":"addToCartSuccessEvent"
,"t":1498895698154,"url":"https://store.nike.com/cn/zh_cn/pd/air-zoom-pegasus-34-男子跑步鞋/pid-11382127/pgid-11631049"
,"swoosh":false,"location":{"cc":"CN","rc":"HN","tp":"vhigh","tz":"GMT+8","la":"28.20","lo":"112.97"
,"bw":"5000"},"guidS":"12f9ac20-3154-4996-d72c-75242d07dd32"}]}



{"t":1498895966535,"upm":"16148434344","analysisUserId":"118.123.105.20.300811496813701754","guidU":"89eb2d42-da51-4460-85ab-c27f62ff6deb"
,"cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"ocp\":{}}","neo.swimlane":"22"
},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/10|bcookieSupport:1","platform":{"id":"nike
.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"name":"addToCartSuccessEvent"
,"t":1498895966534,"url":"https://store.nike.com/cn/zh_cn/pd/air-zoom-pegasus-34-男子跑步鞋/pid-11382129/pgid-11631049"
,"swoosh":false,"location":{"cc":"CN","rc":"HN","tp":"vhigh","tz":"GMT+8","la":"28.20","lo":"112.97"
,"bw":"5000"},"guidS":"12f9ac20-3154-4996-d72c-75242d07dd32"}]}




# adidas问题
##　购物车
- 当购物车没有商品程序不能把商品加入购物车，反之可以加入购物车

## 加入地址问题
- 当程用户没有收货地址序不能加入个人信息，反之可以加入新的收货信息

## 如何判断注册，登录加入购物车，加入个人信息的状态（分别print出来）




product=350198&release2=yes&qty=1&super_attribute%5B184%5D=493&token=e82e0ce22690bf917995ce5994dfab18&isajax=yes
200

product=350198&release2=yes&qty=1&super_attribute%5B184%5D=493&token=e4fe46de5f2e4dce8ee96da553987bed&isajax=yes
200


loginUrl="https://www.adidas.com.cn/customer/account/loginPost/"
    loginHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Referer': 'https://www.adidas.com.cn/customer/account/login/'}
    nologinCookie=requests.get(loginUrl,headers=loginHead).cookies
    head= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
           'Referer': 'https://www.adidas.com.cn/customer/account/login/',
           'cookie':str(nologinCookie)
           }
    data={"login[username]":registerinfo['username'],"login[password]":"112358yS",'send':''}
    print "login..." 
    loginHtml = requests.post(loginUrl,data=data,headers = head)
    #print loginHtml.text
    loginCookie=loginHtml.cookies

    # # 查看购物车
    cartUrl='http://www.adidas.com.cn/checkout/cart/'
    cartHtml=requests.get(cartUrl,headers=loginHead,cookies=loginCookie)
    loginCookie=cartHtml.cookies
    print cartHtml.text
    # #print loginCookie
    # #添加购物车
    # ## 获取验证信息
    spHtml=requests.get(spurl,headers=loginHead,cookies=loginCookie)
    loginCookie=spHtml.cookies
    
    soup=BeautifulSoup(spHtml.text,'html.parser')
    script=soup.select('script')[-4]
    productid=str(script).split(',')[2].split('+')[1]
    infoUrl='http://www.adidas.com.cn/specific/product/ajaxview/?id='+productid
    infoHml=requests.get(infoUrl,headers=loginHead,cookies=loginCookie)
    #loginCookie=infoHml.cookies

    #print infoHml
    infosoup=BeautifulSoup(infoHml.text,'html.parser')
    token=infosoup.select('input')[0]['value']
    #print token
    isajax=infosoup.select('input')[1]['value']
    #print isajax
    release2=infosoup.select('input')[2]['value']
    #print release2
    product=infosoup.select('input')[3]['value']
    #print product
    ## 添加
    addurl='http://www.adidas.com.cn/checkout/cart/add/'
    addHead={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
             'Referer': 'https://www.adidas.com.cn/customer/account/login/',
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
             }
    params = {'token':token,'isajax':isajax,'release2':release2,'product':product,'super_attribute[184]':'493','qty':'1'}        
    data = urllib.urlencode(params)
    print data
    #payload = "token="+token+"&isajax="+isajax+"&release2="+release2+"&product="+product+"&super_attribute%5B184%5D="+"811"+"&qty="+"1"
    #print payload

    add=requests.post(addurl,data=data,headers=addHead,cookies=loginCookie)
    print add.status_code

form_key:I03R1wx2VC6asmHw
success_url:
error_url:
token:d7781617924bea89949a082594c0d00b
country_id:CN
firstname:杨胜
region_id:515
region:天津
city_id:342
district_id:3127
city:天津市
district:河东区
street[]:家居巴拉克的
postcode:432000
tel_areacode:
telephone:
mobile:17786493932
default_billing:1
default_shipping:1




# 取得付款链接（qrImgUrl）
1.
https://tfsimg.alipay.com/images/mobilecodec/T1ZmtEXcpbXXXXXXXX(二维码)
|
https://excashier.alipay.com/standard/auth.htm?payOrderId=b1eb3c3324e34467ae7ad1d197b2fffd.80
|
payOrderId=b1eb3c3324e34467ae7ad1d197b2fffd.80


2.
填写订单->确认订单（取得该页面立即支付绑定的链接）->到达付款页面->取得二维码付款链接






添加地址
# addresUrl='https://www.adidas.com.cn/customer/address/new/'
  # newaddreshtml=requests.get(addresUrl,headers=loginHead,cookies=loginCookie)
  # print newaddreshtml.text
  # #print newaddreshtml.text
  # soup=BeautifulSoup(newaddreshtml.text,'html.parser')
  # token=soup.select('input')[4]['value']
  # #print token
  # form_key=soup.select('input')[1]['value']
  # #print form_key
  # posturl='https://www.adidas.com.cn/customer/address/formPost/'
  # userinfo={'form_key':form_key,
  #       'success_url':'',
  #       'error_url':'',
  #       'token':token,
  #       'country_id':'CN',
  #       'firstname':'杨胜',
  #       'region_id':'515',
  #       'region':'天津',
  #       'city_id':'342',
  #       'district_id':'3127',
  #       'city':'天津市',
  #       'district':'河东区',
  #       'street[]':'家居巴拉克的',
  #       'postcode':'432000',
  #       'tel_areacode':'',
  #       'telephone':'',
  #       'mobile':'17786493932',
  #       'default_billing':'1',
  #       'default_shipping':'1'}
  # data=urllib.urlencode(userinfo)
  # #print data
  # addres=requests.post(posturl,headers=addHead,data=data,cookies=loginCookie)
  # print addres.status_code


1.提交结算的所有信息
2.解决location
3.根据location的url找到付款页面
4.到达付款页面提二维码url


https://www.adidas.com.cn/yancheckout/process/overview/reserved_order_id/6163790821/

29
shipping[firstname]:杨胜
shipping[country_id]:CN
shipping[region_id]:515
shipping[region]:天津
shipping[city_id]:342
shipping[district_id]:3126
shipping[city]:天津市
shipping[district]:和平区
shipping[street][]:款和放假吧按时
shipping[postcode]:432000
shipping[mobile]:17786493932
shipping[tel_areacode]:
shipping[telephone]:
shipping[save_in_address_book]:1
shipping[use_for_shipping]:1
shipping[update_region]:0
shipping[primary_shipping]:1
shipping[primary_billing]:1
shipping[delivery_memo]:大江南北将
shipping[id]:
shipping[yancheckout_page]:1
delivery_type:Normal
token:c515845e6e0bff446a62f7b27bdebbae
payment[alipay_pay_bank]:ALIPAY
payment[alipay_pay_method]:bankPay
shipping_method:carrier_bestway
fapiao[fapiao_type]:personal
fapiao[fapiao_title]:
fapiao[fapiao_memo]:

30
shipping[firstname]:杨胜
shipping[country_id]:CN
shipping[region_id]:515
shipping[region]:天津
shipping[city_id]:342
shipping[district_id]:3126
shipping[city]:天津市
shipping[district]:和平区
shipping[street][]:款和放假吧按时
shipping[postcode]:432000
shipping[mobile]:17786493932
shipping[tel_areacode]:
shipping[telephone]:
shipping[save_in_address_book]:1
shipping[use_for_shipping]:1
shipping[update_region]:0
shipping[primary_shipping]:1
shipping[primary_billing]:1
shipping[delivery_memo]:大江南北将
shipping[id]:
shipping[yancheckout_page]:
shipping_address_id:724309
delivery_type:Normal
token:c515845e6e0bff446a62f7b27bdebbae
payment[alipay_pay_bank]:ALIPAY
payment[alipay_pay_method]:bankPay
shipping_method:carrier_bestway
fapiao[fapiao_type]:personal
fapiao[fapiao_title]:
fapiao[fapiao_memo]:




添加地址
infoUrl='https://www.adidas.com.cn/yancheckout/process/'
  head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
      'Referer': 'http://www.adidas.com.cn/checkout/cart/'}

  infohtml=requests.get(infoUrl,headers=head,cookies=loginCookie)
  #print infohtml.text
  soup=BeautifulSoup(infohtml.text,"html.parser")
  token=soup.select('input')[19]['value']
  print token
  # shipping_address_id=soup.select('')
  # print shipping_address_id

  #print token
  addresUrl='https://www.adidas.com.cn/yancheckout/process/saveShippingAndPayment/'
  userinfo={"shipping[firstname]":"杨胜",
        "shipping[country_id]":"CN",
        "shipping[region_id]":"515",
        "shipping[region]":"天津",
        "shipping[city_id]":"342",
        "shipping[district_id]":"3127",
        "shipping[city]":"天津市",
        "shipping[district]":"河东区",
        "shipping[street][]":"高新6路",
        "shipping[postcode]":"432000",
        "shipping[mobile]":"17786493932",
        "shipping[tel_areacode]":"",
        "shipping[telephone]":"",
        "shipping[save_in_address_book]":"1",
        "shipping[use_for_shipping]":"1",
        "shipping[update_region]":"0",
        "shipping[primary_shipping]":"1",
        "shipping[primary_billing]":"1",
        "shipping[delivery_memo]":"湖区",
        "shipping[id]":"",
        "shipping[yancheckout_page]":"1",
        "delivery_type":"Normal",
        # 'shipping_address_id':shipping_address_id,
        "token":token,
        "payment[alipay_pay_bank]":"ALIPAY",
        "payment[alipay_pay_method]":"bankPay",
        "shipping_method":"carrier_bestway",
        "fapiao[fapiao_type]":"personal",
        "fapiao[fapiao_title]":"",
        "fapiao[fapiao_memo]":""}
  data = urllib.urlencode(userinfo)
  #print data
  add_head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
       'Referer': 'https://www.adidas.com.cn/yancheckout/process/',
       'Content-Type':'application/x-www-form-urlencoded'}
  add_addres=requests.post(addresUrl,data=data,headers=add_head,cookies=loginCookie)
  print add_addres.status_code


  [<a class="adidasLogo" href="/" title="adidas \u963f\u8fea\u8fbe\u65af\u5b98\u7f51 \u9996\u9875"><img alt="adidas\u963f\u8fea\u8fbe\u65af\u5b98\u7f51 \u9996\u9875" src="https://www.adidas.com.cn/skin/frontend/arvato/default/imgs/logo.png"/></a>, <a href="javascript:void(0);" onclick="adidasopenwindow('http://adidas.800teleservices.com.cn/AdidasChat/WebPages/CM/ChatCustomer.html', 'newwindow', '900','600')" style="padding-right:10px;color:#ffffff;"><b>400-999-5999</b></a>, <a class="btnCommon btnBlueLinear btnArrow w160 fl" href="https://mapi.alipay.com/gateway.do?_input_charset=utf-8&amp;logistics_fee=0&amp;logistics_payment=BUYER_PAY&amp;logistics_type=EXPRESS&amp;notify_url=https%3A%2F%2Fwww.adidas.com.cn%2Falipay%2Fpayment%2Fconfirm%2F&amp;out_trade_no=2317053486&amp;partner=2088801058693440&amp;payment_type=1&amp;paymethod=motoPay&amp;price=1499.00&amp;quantity=1&amp;return_url=https%3A%2F%2Fwww.adidas.com.cn%2Falipay%2Fpayment%2Fsuccess%2F&amp;seller_email=shopadidascn2012%40gmail.com&amp;service=create_direct_pay_by_user&amp;subject=2317053486&amp;sign=1f515110a92fcb6e99fc4d510caff680&amp;sign_type=MD5" title="\u7acb\u5373\u652f\u4ed8">\u7acb\u5373\u652f\u4ed8<em></em></a>, <a href="http://www.adidas.com.cn/directory/">\u5173\u4e8e\u8ba2\u5355</a>, <a href="http://www.adidas.com.cn/directory/">\u9a8c\u6536\u9a8c\u8d27</a>, <a href="http://www.adidas.com.cn/directory/">\u7269\u6d41\u914d\u9001</a>, <a href="http://www.adidas.com.cn/directory/">\u552e\u540e\u670d\u52a1</a>, <a href="http://www.adidas.com.cn/privacy-policy" title="\u9690\u79c1\u6761\u6b3e">\u9690\u79c1\u6761\u6b3e</a>, <a class="popCloseBtn closePop" href="javascript:;" title="\u5173\u95ed">\u5173\u95ed</a>, <a class="continue btnCommon btnBlueLinear btnArrow" href="#">\u4e0d\u4fdd\u5b58\u7ee7\u7eed</a>, <a class="cancel btnCommon btnBlueLinear closePop" href="javascript:;">\u53d6\u6d88</a>]


[<input id="J_orderId" name="oid" type="hidden" value="d62be67f90bd426482addaf5612d12dd.00"/>, <input id="J_partnerId" name="pid" type="hidden" value="2088801058693440"/>, <input id="J_outBizID" name="pid" type="hidden" value="4481784749"/>, <input id="J_qrContextId" name="qrContextId" type="hidden" value="201707040049514200ff9f14896d43ab8f"/>, <input id="J_qrPayLoopCheckUrl" name="qrPayLoopCheckUrl" type="hidden" value="https://tradeexprod.alipay.com/fastpay/qrPayLoopCheck.json"/>, <input id="J_qrDiscountText" name="qrDiscountText" type="hidden" value=""/>, <input id="J_qrDiscountDesc" name="qrDiscountDesc" type="hidden" value=""/>, <input id="J_qrCode" name="qrCode" type="hidden" value="https://qr.alipay.com/upx00174mfyhaznexd4w0066"/>, <input id="J_qrImgUrl" name="qrImgUrl" type="hidden" value="https://mobilecodec.alipay.com/show.htm?code=upx00174mfyhaznexd4w0066"/>, <input id="J_qrUseImage" name="qrUseImage" type="hidden" value="false"/>, <input id="J_qrContextId" name="qrContextId" type="hidden" value="201707040049514200ff9f14896d43ab8f"/>, <input id="J_qrRenewalURL" name="qrRenewalURL" type="hidden" value="https://excashier.alipay.com:443/standard/renewQRCode.json?payOrderId=d62be67f90bd426482addaf5612d12dd.00"/>, <input id="J_qrPushCheckURL" name="qrPushCheckURL" type="hidden" value=""/>, <input id="J_qrLoopCheckURL" name="qrLoopCheckURL" type="hidden" value="https://excashier.alipay.com:443/standard/queryQRStatus.json?payOrderId=d62be67f90bd426482addaf5612d12dd.00"/>, <input id="J_qrPaySuccGotoURL" name="qrPaySuccGotoURL" type="hidden" value="https://unitradeprod.alipay.com:443/acq/cashierReturn.htm?sign=K1iSL1GNZvFZh5qELxl8Oh5d80EmrBh03WEsXKP8i2FYCpHp%252BBHfKWPd41o%253D&amp;outTradeNo=4481784749&amp;pid=2088801058693440&amp;type=1"/>, <input id="J_qrCheckMode" name="qrCheckMode" type="hidden" value="LOOP"/>, <input id="J_qrExpirySeconds" name="qrExpirySeconds" type="hidden" value="99"/>, <input id="J_qrLogonId" name="qrLogonId" type="hidden" value=""/>, <input id="J_qrBizType" name="qrBizType" type="hidden" value="UNI_PC_MERCHANT"/>, <input id="J_resultPageStayTime" name="resultPageStayTime" type="hidden" value="5"/>, <input id="J_adName" name="adName" type="hidden" value=""/>, <input id="J_adInfo" name="adInfo" type="hidden" value=""/>, <input name="commonAccountIdentiAuthUrl" type="hidden" value="https://excashier.alipay.com:443/standard/securityRender.phtm?payOrderId=d62be67f90bd426482addaf5612d12dd.00&amp;viewModel=payerPwdLoginViewModel"/>, <input name="_form_token" type="hidden" value="a5c36c236b43c25725be7f5ed6e55694d73aa36a0561420eb0b80d8c88685cf7RZ25"/>, <input name="viewModelId" type="hidden" value=""/>, <input class="mi-input mi-input-account" id="J_tLoginId" name="loginId" placeholder="\u624b\u673a\u53f7\u7801/\u90ae\u7bb1" seed="NewQr_tAccountInput" type="email" value=""/>, <input id="J_tLoginIdValue" name="loginIdValue" type="hidden" value=""/>, <input id="J_password" name="password" type="hidden" value=""/>, <input name="pwdSecurityId" type="hidden" value="web|excashier_payment_pwd_control|38d4dead-932a-446d-abc7-8605cac5a046RZ25"/>, <input style="display:none"/>, <input style="display:none" type="password"/>, <input autocomplete="off" class="ui-input" id="payPasswd_input" name="payPasswd_input" oncontextmenu="return false" oncopy="return false" oncut="return false" onpaste="return false" tabindex="" type="password"/>, <input name="J_aliedit_using" type="hidden" value="true"/>, <input id="payPasswd" name="payPasswd" type="hidden" value=""/>, <input name="J_aliedit_key_hidn" type="hidden" value="payPasswd"/>, <input name="J_aliedit_uid_hidn" type="hidden" value="alieditUid"/>, <input id="alieditUid" name="alieditUid" type="hidden" value="fc950a4d01c60e94ff5740ed21f07a3e"/>, <input name="REMOTE_PCID_NAME" type="hidden" value="_seaside_gogo_pcid"/>, <input name="_seaside_gogo_pcid" type="hidden" value=""/>, <input name="_seaside_gogo_" type="hidden" value=""/>, <input name="_seaside_gogo_p" type="hidden" value=""/>, <input name="J_aliedit_prod_type" type="hidden" value=""/>, <input name="security_activeX_enabled" type="hidden" value=""/>, <input name="J_aliedit_net_info" type="hidden" value=""/>, <input id="edit_infor" type="hidden" value=""/>, <input id="J_pwdLoginFront" name="pwdLoginFront" type="hidden" value="false"/>, <input name="hasAntiFishingRisk" type="hidden" value="false"/>, <input name="needCheckIframe" type="hidden" value="true"/>, <input id="J_antiFishingStop" name="pay" seed="excashier-antiFishing-cancelPay" type="radio" value="N"/>, <input id="J_antiFishingPay" name="pay" seed="excashier-antiFishing-confirmPay" type="radio" value="Y"/>, <input seed="excashier-antiFishing-viewCase" tabindex="3" type="button" value="\u67e5\u770b\u76f8\u5173\u6848\u4f8b"/>, <input id="J_openUrl" type="hidden" value="https://bbs.taobao.com/catalog/thread/154504-251045688.htm"/>, <input name="commonAgreementUrl" type="hidden" value="https://excashier.alipay.com:443/standard/agreementDetail.phtm?payOrderId=d62be67f90bd426482addaf5612d12dd.00&amp;viewModel=standard%3AcommonAgreementViewModel.vm"/>, <input name="memoryPayAgreementUrl" type="hidden" value="https://excashier.alipay.com:443/standard/agreementDetail.phtm?payOrderId=d62be67f90bd426482addaf5612d12dd.00&amp;viewModel=standard%3AmemoryPayAgreementViewModel.vm"/>]

qrImgUrl