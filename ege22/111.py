def f(x):
    a,b = 0,0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 4
        x //= 4
    return a,b

for x in range(1,10000):
    if f(x) == (2,7):
        print(x)
        break