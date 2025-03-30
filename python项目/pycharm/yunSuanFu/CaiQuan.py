# import random
#
# ran = random.randint(1, 10)
# count = 0
#
# while True:
#     guess = int(input('请输入一个数：'))
#     #count改变
#     count += 1
#
#     #猜对结束
#     if guess == ran:
#         if count == 1:
#             print('1次过')
#         elif 2 <= count <= 5:
#             print('一般般')
#         elif count>=6:
#             print('不行啊')
#         break
#     elif guess > ran:
#         print('小一点')
#     else:
#         print('大一点')


# ----------------------------------------------------------------------------------------------------------------------

import random

n = 1
p_count = 0
m_count = 0

while n <= 3:

    ran = random.randint(0, 2)
    guess = int(input('请输入：剪刀（0），石头（1），布（2）'))

    if (guess == 0 and ran == 2) or (guess == 1 and ran == 0) or (guess == 2 and ran == 1):
        print('胜利！！')
        p_count += 1
    elif (ran == 0 and guess == 2) or (ran == 1 and guess == 0) or (ran == 2 and guess == 1):
        print('失败.....')
        m_count += 1
    else:
        print('平局')

    n += 1

if p_count > m_count:
    print('本次人赢')
elif p_count < m_count:
    print('本次机器赢')
elif p_count == m_count:
    print('最终平局')
