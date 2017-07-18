# 模块
- 商品抢购+填写收货信息+生成订单+提取付款链接模块
- 查询订单信息模块

orderUrl='https://www.adidas.com.cn/sales/order/history/'
    # orderHtml=requests.get(orderUrl,headers=loginHead)
    # #print orderHtml.text
    # ordersoup=BeautifulSoup(orderHtml.text,"html.parser")
    # infoUrl=ordersoup.select('.blue a')
    # for infoUrls in infoUrl:
    #   print infoUrls['href']
    #   orderinfosHtml=requests.get(infoUrls['href'],headers=loginHead)
    #   orderinfosSoup=BeautifulSoup(orderinfosHtml.text,"html.parser")
    #   orderNumber=orderinfosSoup.select('title')[0]
    #   print orderNumber.text
    #   styleNumber=orderinfosSoup.select('.wd90')[0]
    #   print "款号:",styleNumber.text
    #   size=orderinfosSoup.select('.proShow span')[0]
    #   print '尺寸:',size.text
    #   qty=1#orderinfosSoup.select('.pl25')[0]
    #   print '数量:',qty
    #   total=orderinfosSoup.select('.price')[0]
    #   print '总价:',total.text
    #   print '付款链接:',payurl
    #   print '商品名称:',sptitle
    #   print '价格:',price
    #   print type(total.text.encode('utf8')),type(price.encode('utf8'))
    #   print '快递费:',float(total.text.encode('utf8').split('¥')[1])-float(price.encode('utf8').split('¥')[1])