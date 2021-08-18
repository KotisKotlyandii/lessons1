def func(s):
    n = 0
    while s < s*s:
        s = s-1
        n = n+3
    return n

for s in range(1,1000):
    if func(s) > 2000:
        print(s)
        break