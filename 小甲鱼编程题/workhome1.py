name=input('请输入姓名：')
print("hello ," + name + '!')

temp=input('请输入数字：')
number=int(temp)
if 1<= number <=100:
    print('nice')
else:
    print('bad')

num = input("请输入1到100之间的数字：")
while True:
    if not num.isdigit():
        print('重新输入:',end='')#end=表示不换行
        num = input()
    else:
        if num > 100:
            print('bad')
        else:
            print('good')
    break

