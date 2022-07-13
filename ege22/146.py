def f(x):
    a,b = 0,1
    while x > 0:
        if x % 2 > 0:
            a += x % 12
        else:
            b *= x % 12
        x //= 12
    return a,b

for x in range(1,10000):
    if f(x) == (7,12):
        print(x)
        break