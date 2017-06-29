# 注册
## 完成要求
- 任何一个平台都可以通过注册模块完成注册
- 返回注册结果

# Nike 
### 注册信息(注册不需要验证码)
- 注册url: https://unite.nike.com/join
- 注册post data
```
"account":{"email": "cky123@qq.com", "passwordSettings": {"password": "112358yS", "passwordConfirm": "112358yS"}}  (email变量)
"country": "CN",
"dateOfBirth": "1994-01-25",
"firstName": "sheng",
"gender": "male",
"lastName": "yang",
"locale": "zh_CN",
"mobileNumber": "17786493932",  (变量)
"receiveEmail": "true",
"registrationSiteId": "nikedotcom",
"username": "cky123@qq.com",  (邮箱作为username)
"welcomeEmailTemplate": "TSD_PROF_COMM_WELCOME_V1.0"
```
注册页面输入信息
```
"username":"1774507013@qq.com",
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


# adidas
### 注册信息（注册需要数字验证码）
- 注册post data
```
token(html中获取)
firstname：杨胜
mobile：17786493932(变量)
gender：1(1男2女)
day：2
year：1994
dob：1994-3-2
osolCatchaTxt(验证码)
osolCatchaTxtInst(写死 例如：1 验证码检验状态表示)
email：1774507011@qq.com(变量)
username:yangsheng(变量)
password
confirmation(密码确认)
agree_terms
```
- 阿迪达斯中mobile,email,username要生成，其余可以写死或页面爬取

# 登陆字段
## 阿迪达斯：username password
## 耐克：email password

# 问题
- 注册提交公共字段
```
邮箱
密码
确认密码
手机号
出生日期
```

 
# 添加购物车
- 商品链接
- 抢购规则



# 问题
## 耐克
- 添加购物车要post出处的数据难以分析
如：
```
{"t":1498723379052,"upm":"16138156515","analysisUserId":"WUDmUwoMQ10AACGkllAAAARv","guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05","cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1","platform":{"id":"nike.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11395927","qty":"1","skuAndSize":"18410747:42","name":"addToCartEvent","t":1498723379047,"url":"https://store.nike.com/cn/zh_cn/pd/air-zoom-pegasus-34-男子跑步鞋/pid-11395927/pgid-11631049","swoosh":false,"location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},"guidS":"8b35890e-c179-4483-fc8f-c6e33962e927"}]}
```




