price = float(input('商品单价：'))
number = int(input('商品数量：'))

total = price * number

chioce = input('付款方式：\n1.现金    2.微信\n3.支付宝   4.刷卡\n请输入：')
if chioce == '1':
    print('现金支付无折扣，应付金额：%.2f' % total)
elif chioce == '2':
    print('微信支付')
    total *= 0.95
    print('应付金额：%.2f' % total)
elif chioce == '3':
    print('支付宝')
    total = total - total * 0.1
    print('应付金额：%.2f' % total)
elif chioce == '4':
    print('刷卡')
    if total > 100:
        total-=20
        print('应付金额：%.2f' % total)
    else:
        print('没有折扣，应付金额：%.2f' % total)
else:
    print('暂时不支持该支付方式。。。')