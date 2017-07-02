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





















