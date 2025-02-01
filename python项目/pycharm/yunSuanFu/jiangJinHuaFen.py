name = input('请输入名称：')
money = float(input('请输入绩效：'))
if 7 < money < 15:
    print(name + ',奖金260')
elif 15 <= money < 20:
    print(name + ',奖金为500')
elif 20 <= money < 25:
    print(name + ',奖金为800')
elif 25 <= money <= 31:
    print(name + ',奖金为1000')
else:
    print(name + ',请准备材料到财务！！！')
