import random

ran = random.randint(1, 10)
print(ran)

guess = int(input('请输入一个数：'))
if ran == guess:
    print('成功！')
else:
    print('失败。。。')