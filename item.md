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
{"t":1498033109322,"upm":"16076584660","analysisUserId":"WUDmUwoMQ10AACGkllAAAARv","guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05","cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1","platform":{"id":"nike.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11454915","qty":"1","skuAndSize":"18466798:40","name":"addToCartEvent","t":1498033109319,"url":"http://store.nike.com/cn/zh_cn/pd/air-jordan-4-retro-复刻男子运动鞋/pid-11454915/pgid-11088472","swoosh":false,"location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},"guidS":"a84e884d-055e-49ed-f3a1-f794eb8747f0"}]}

```

```
{"t":1498032437308,"upm":"16076584660","analysisUserId":"WUDmUwoMQ10AACGkllAAAARv","guidU":"9e35ac0b-c90c-4724-e2f0-1bc70651ff05","cookies":{"CONSUMERCHOICE":"cn/zh_cn","neo.experiments":"{\"main\":{},\"snkrs\":{},\"ocp\":{},\"thirdparty\":{}}","neo.swimlane":"24"},"deviceAtlas":"sdevicePixelRatio:1|sdeviceAspectRatio:16/9|bcookieSupport:1","platform":{"id":"nike.com","v":"main"},"source":{"id":"dreamcatcher","v":"3.29.2"},"events":[{"pid":"11454915","qty":"1","skuAndSize":"18466798:40","name":"addToCartEvent","t":1498032437304,"url":"http://store.nike.com/cn/zh_cn/pd/air-jordan-4-retro-复刻男子运动鞋/pid-11454915/pgid-11088472","swoosh":false,"location":{"cc":"CN","rc":"HB","tp":"vhigh","tz":"GMT+8","la":"30.58","lo":"114.27","bw":"5000"},"guidS":"a84e884d-055e-49ed-f3a1-f794eb8747f0"}]}
```
以上数据能找到出处的：analysisUserId，
- 重新构造data

### 结算

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
- regData中mobile,email,username在注册字段是唯一的

# apple
## 注册问题
- 邮箱验证
- 验证码(干扰线，重叠)
- 图片在js里面怎么抓取 script id="jstache_750318036"

### 获得验证码
- 图片位于js里无法获取图片(1.上网搜关于解析js 2.模拟刷新验证码获取验证码数据)

# 任务
- 完成3个网站的注册登陆

# 进度
- nike网站大致完成
- adidas网站大致完成



###
<script type="text/stache" id="jstache_750318036">
  <div class="create-captcha-wrapper">
    <div class="input-group">
        <div class="row-container">
            <div class="row">
                <div class="column large-4 captcha-img-wrapper">
                    <div class="field-wrapper padding right">
                        <idms-captcha {(type)}="type"
                                      {(mime-type)}="mimeType"
                                      {(base64-data)}="base64Data"
                                      {(is-loading)}="isLoading"
                                      {^@play}="@playAudio"
                                      {^@stop}="@stopAudio"
                                      play-audio-text="播放安全提示音频"
                                      pause-audio-text="暂停安全提示音频"
                                      image-alternate-text="安全提示图片"
                                      paused-audio-image-path="https://appleid.cdn-apple.com/static/bin/cb983233127/dist/assets/images/captcha-audio-paused.png"
                                      audio-image-path="https://appleid.cdn-apple.com/static/bin/cb1764815236/dist/assets/images/captcha-audio.jpg">
                        </idms-captcha>
                    </div>
                </div>
                <div class="column large-8 captcha-field-wrapper">
                    <label class="a11y">Captcha</label>
                    <div class="field-wrapper padding left">
                        <div class="pop-wrapper field-pop-wrapper">
                            <captcha-input id="captcha" {(value)}="value" errors="{errors}"
                                           classes="form-cell form-textbox form-textbox-text form-field captcha-field{{#errors.hasErrors}} has-errors{{/if}}"
                                           placeholder="{{#is type 'image'}}键入图中的字符{{else}}输入您听到的代码{{/if}}">
                            </captcha-input>
                            {{#errors.showErrors}}
                                <idms-popover {show}="errors.hasErrors"
                                              anchor-element=".captcha-field"
                                              max-width="auto"
                                              type="error">
                                  {{#is errors.main.message 'empty_input'}}
                                    {{#is type 'image'}}
                                      <div class="error-message">输入图中的文本</div>
                                    {{/is}}
                                    {{#is type 'audio'}}
                                      <div class="error-message">输入朗读的代码。</div>
                                    {{/is}}
                                  {{else}}
                                    <div class="error-message">{{errors.main.message}}</div>
                                  {{/is}}
                                </idms-popover>
                            {{/if}}
                        </div>
                        <div class="captcha-controls">
                            <button class="button link first"
                                    ($click)="getNewCaptcha(false)">
                                <span class="icon icon_reload" aria-hidden="true"></span>
                                新代码
                            </button>
                            <button class="button link"
                                    ($click)="getNewCaptcha()">
                                {{#is type 'image'}}
                                <span class="icon icon_sound" aria-hidden="true"></span>
                                视力障碍
                                {{/is}}
                                {{#is type 'audio'}}
                                <span class="icon icon_text" aria-hidden="true"></span>
                                文本形式
                                {{/is}}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</script>



