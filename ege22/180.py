def f(x):
    k = x % 5
    a,b = 0,0
    while x > 0:
        d = x % 5
        if d == k:
            a += 1
        b += d
        x //= 5
    return a,b

for x in range(1,100000):
    if f(x) == (3,10):
        print(x)
        break