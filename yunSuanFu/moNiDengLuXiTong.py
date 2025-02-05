username = input('用户名：')
password = input('密码：')
is_remember = False
if username == 'admin' and password == '1234':
    if is_remember:
        print('%s已成功记住密码！' % username)
    else:
        print('未记住密码，下次仍须键入...')
else:
    print('用户名或密码有误！！！')