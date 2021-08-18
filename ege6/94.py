def func(s):
    n = 0
    while s*s < 101:
        s = s+1
        n = n+2
    return n

for s in range(1,1000):
    if func(s) == 16:
        print(s)
        break