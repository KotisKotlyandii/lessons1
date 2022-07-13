def f(x):
    k = x % 8
    a,b = 0,0
    while x > 0:
        d = x % 8
        if d == k:
            a += 1
        b += d
        x //= 8
    return a,b

for x in range(1,100000):
    if f(x) == (3,20):
        print(x)
        break