def func(s):
    n = 1
    while s < 51:
        s =s+5
        n =n*2
    return n


for s in range(1,1000):
    if func(s) == 64:
        print(s)
        break

