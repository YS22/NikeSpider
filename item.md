#流程
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

# adidas
### 注册信息（注册需要数字验证码）
- 注册url：https://www.adidas.com.cn/customer/account/create/
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

# 核心
- 模拟注册登陆的逻辑要清楚

# 任务
- 完成3个网站的注册登陆

# 进度
- nike网站完成
