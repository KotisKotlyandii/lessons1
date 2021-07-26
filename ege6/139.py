def func(s):
    n = 740
    while s+n<1200:
        s = s + 6
        n = n - 4
    return n


for s in range(1,1000):
    if func(s) == 68:
        print(s)
        break