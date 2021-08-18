def func(s):
    n = 18
    while s > 0:
        s = s - 7
        n = n + 4
    return n


for s in range(1,1000):
    if func(s) == 66:
        print(s)
        break