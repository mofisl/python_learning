def count(*args):
    length = len(args)
    for i in range(length):
        word = 0
        num = 0
        spa = 0
        oth = 0
        for j in args[i]:
            if j.isalpha():
                word += 1
            elif j.isspace():
                spa += 1
            elif j.isdigit():
                num += 1
            else:
                oth += 1
        print('{2:d} {1:d} {0:d}'.format(word,spa,num))
count('I love fish.com 123', 'I love you', 'you love 123')