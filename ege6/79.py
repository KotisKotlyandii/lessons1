def func(s):
    n = 5
    while s < 110:
        s = s+n
        n = n+1
    return n

for s in range(1,1000):
    if func(s) == 15:
        print(s)
        break
