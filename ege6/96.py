def func(s):
    n = 0
    while s < 1000:
        s = s*2
        n = n+5
    return n

for s in range(1,1000):
    if func(s) == 10:
        print(s)
        break
