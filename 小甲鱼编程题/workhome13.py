def findstr(s, ss):
    count = 0
    for i in range(len(ss)):
        if s in ss[i:i+2]:
            count += 1
    print(count)
findstr('hh','jintianhhnidhhhc')