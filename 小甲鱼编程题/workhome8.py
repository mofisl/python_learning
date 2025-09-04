print('--进制转换--')
number = input('请输入一个整数：')
while number.upper() != 'Q':
    if number.isdigit():
        number = int(number)#这里已经变为int后续要重新输入
        print('10-16 {0:d}={0:#x}'.format(number))
        print('10-8 {0:d}={0:#o}'.format(number))
        print('10-8 {0:d}={0:#b}'.format(number))# bin(number) 返回的是字符串
        number = input('请输入一个整数：')
    else:
        if number == 'Q':
            break
        else:
            number = input('不合法，输入Q结束：')