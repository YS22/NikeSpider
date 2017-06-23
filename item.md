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
"password":"112358yS",
"lastName:":"杨",
"firstName":"胜",
"dateOfBirth":"1994-01-20",
"country":"CN",
"mobileNumber":"17786493932",
"gender":"male",
"receiveEmail":true
```
### 添加购物车流程
- 进入需要购买商品链接:https://www.nike.com/cn/launch/
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
firstname(真实姓名)
mobile
gender
day
year
dob(出生日期)
osolCatchaTxt
osolCatchaTxtInst
email
username
password
confirmation(密码确认)
agree_terms
```
- regData中mobile,email,username在注册字段是唯一的

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

# 进度
- nike网站大致完成
- adidas网站大致完成




