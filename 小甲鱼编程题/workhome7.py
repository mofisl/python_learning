while True:
    hehe = input('请输入：')
    hehec = '正确'
    if hehe == hehec:
        print("bing go")
        break
    else:
        print('bad')
print('end')     
#break终止循环
for i in range(0,10):
    if i % 2 != 0:
        print(i)
        continue #满足条件，riaoc
    i += 3
    print(i)
#验证密码
count = 3
password = 'fish'
while count:
    passwd = input('please input:')
    if passwd == password:
        print('ok')
        break
    elif '*' in passwd:
        print('no', count, end= ' ')
        continue
    else:
        print('nono', count -1)
    count -= 1

for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)