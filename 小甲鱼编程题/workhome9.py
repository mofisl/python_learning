def zjmin(x):
    least = x[0]
    for i in x:
        if i< least:
            least = i
    return least
print(zjmin('21321'))