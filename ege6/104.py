def func(s):
    n = 32
    while n > s:
        s = s + 1
        n = n - 1
    return n

for s in range(1,1000):
    if func(s) >= 30:
        print(s)
        break
        