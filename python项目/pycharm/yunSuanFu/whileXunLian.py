'''
a.打印1-50间能被3整除的数
b.打印1-50间数字的累加和
'''
# a = 1
# while a <= 50:
#     n = 1
#     while n <= 50:
#         if n % 3 == 0:
#             print('--->', n)
#         n += 1
#     b = 3
#     while b <= 50:
#         print('-->', b)
#         b += 3
#     if n == b:
#         print('ok')
#     a += 1


n = 1
sum = 0
while n <= 50:
    sum += n
    print(sum)
    n += 1
