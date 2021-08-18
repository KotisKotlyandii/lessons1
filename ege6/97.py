def func(s):
    n = 50
    while s > 0:
        s = s //2
        n = n - 3
    return n

for s in range(-1000,1000):
    if func(s) == 23:
        print(s)
        break