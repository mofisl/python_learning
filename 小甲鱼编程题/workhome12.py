def Daffodils():
    print('所有的水仙花数为：',end='')
    temp = 100
    while temp < 1000:
        if temp == (temp//100)**3 + ((temp%100)//10)**3 + (temp%10)**3:
            print(temp)
            temp += 1
        else:
            temp += 1
Daffodils()