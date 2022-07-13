def f(x):
    a,b,d = 0,0,0
    while x > 0:
        if d % 2 == 0:
            a += x % 10
        else:
            b += x % 10
        x //= 10
        d += 1
    return a,b

for x in range(1,100000):
    if f(x) == (4,15):
        print(x)
        break