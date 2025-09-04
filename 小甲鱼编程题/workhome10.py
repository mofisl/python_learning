def load():
    dict1 = {}
    while True:
        print('新建用户：N/n')
        print('登陆账号：E/e')
        print('退出程序：Q/q')
        key = input('请输入指令代码:')
        if key == 'N' or key == 'n':
            key_name = input('用户名：')
            while key_name in dict1:
                key_name = input('用户名已存在，重新输入：')
            value_name = input('密码：')
            dict1[key_name] = value_name
            print('注册成功，赶紧试试登录吧^_^')
            continue
        elif key == 'E' or key == 'e':
            key_name = input('用户名：')
            while key_name not in dict1:
                key_name = input('用户名不存在，重新输入：')
            value_name = input('密码：')
            while value_name not in dict1.values(): #while temp_password != dict1[temp_name]:
                value_name = input('密码不正确，重新输入：')
            print('欢迎进入')
            continue
        elif key == 'Q' or key == 'q':
            break
load()