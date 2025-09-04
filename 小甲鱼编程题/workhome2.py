temp=input('请输入数字：')
guess=int(temp)
if guess == 8:
    print('let\' go')
else:
    if guess > 8:
        print(r'D:\ding\data')
    else :
        print('D:\\hehe\\hehe')
#改进
import random
secret = random.randint(1,10)
times = 3
while times :
    temp = input('请输入数字：')
    guess = int(temp)
    times = times - 1
    if guess == secret :
        print('let\' go')
    else:
        if guess > secret :
            print(r'D:\ding\data')
        else :
            print('D:\\hehe\\hehe')
        if times > 0 :
            print('again')
        else :
            print('no')
print('w')