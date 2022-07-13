def f(x):
    k = x % 7
    a,b = 0,0
    while x > 0:
        d = x % 7
        if d == k:
            a += 1
        b += d
        x //= 7
    return a,b

for x in range(1,100000):
    if f(x) == (4,11):
        print(x)
        break