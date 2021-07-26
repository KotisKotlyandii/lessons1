def func(s):
    n = 1
    while n < 21:
        s = s -1
        n = n +2
    return s

for s in range(1,1000):
    if func(s) > 600:
        print(s)
        break