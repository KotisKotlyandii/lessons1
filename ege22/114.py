def f(x):
    a,b = 0,1
    while x > 0:
        if x % 2 > 0:
            a += x % 8
        else:
            b *= x % 8
        x //= 8
    return a,b

for x in range(100,1000):
    if f(x) == (2,8):
        print(x)