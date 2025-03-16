import random

username = input('名称：')
total = float(input('消费金额：'))
money = 0  # 账户金额
coupon = 0  # 优惠劵
if 0 < total < 500:  # lv1
    quan1 = random.randint(1, 10)
    quan2 = random.randint(1, 10)
    quan3 = random.randint(1, 10)
    # 将 quan 加到 coupon
    coupon = quan1 + quan2 + quan3
elif 500 <= total < 2000:  # lv2
    coupon += 2 * 50
    recharge = input('是否要充值？（y/n）')
    if recharge == 'y':
        money += 1.1 * float(input('请输入充值金额：'))
elif total >= 2000:  # lv3
    coupon += 2 * 100
    recharge = input('%s,是否要充值？（y/n）')
    if recharge == 'y':
        money += 1.15 * float(input('请输入充值金额：'))
print('账户金额' + str(money))
print('优惠劵总金额' + str(coupon))
