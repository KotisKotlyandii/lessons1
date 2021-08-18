def func(d):
    s = 0
    n = 0
    while n < 200:
        s = s+64
        n = n+d
    return s

for d in range(1,1000):
    if func(d) == 192:
        print(d)
        break