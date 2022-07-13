def f(x):
    k = x % 6
    a,b = 0,0
    while x > 0:
        d = x % 6
        if d == k:
            a += 1
        b += d
        x //= 6
    return a,b

for x in range(1,100000):
    if f(x) == (2,15):
        print(x)
        break