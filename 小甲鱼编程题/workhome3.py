#判断类型是否正确,input()的返回值始终是字符串
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# not操作符的作用是将布尔类型的结果翻转：即取反的意思，not True == Flase
while not isinstance(temp, int):#type(temp) != type(1)
    print("抱歉，输入不合法，", end='')
    temp = input("请输入一个整数：")