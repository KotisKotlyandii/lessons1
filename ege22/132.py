def f(x):
    a,b = 0,0
    while x > 0:
        if x % 2 > 0:
            a += x % 9
        else:
            b += x % 9
        x //= 9
    return a,b

for x in range(1000,10000):
    if f(x) == (4,4):
        print(x)
        break