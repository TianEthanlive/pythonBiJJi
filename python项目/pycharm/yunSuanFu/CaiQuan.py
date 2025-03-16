import random

ran = random.randint(1, 10)
count = 0

while True:
    guess = int(input('请输入一个数：'))
    #count改变
    count += 1

    #猜对结束
    if guess == ran:
        if count == 1:
            print('1次过')
        elif 2 <= count <= 5:
            print('一般般')
        elif count>=6:
            print('不行啊')
        break
    elif guess > ran:
        print('小一点')
    else:
        print('大一点')
