# for i in range(0, 10):
#     print(i)
# print('**************' * 10)
# sum = 0
# for i in range(1, 51):
#     sum += i
# print(sum)
#
# print('*' * 60)

username0 = 'admin'
password0 = '1234'

i = 0
for i in range(3):
    username = input('用户名：')
    password = input('密码：')
    if username == username0 and password == password0:
        print('成功')
        break
    print('没有该用户')
if i == 2:
    print("账户被锁定")
