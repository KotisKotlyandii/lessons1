def f(x):
    a,b = 0,1
    while x > 0:
        if x % 2 == 0:
            a += x % 13
        else:
            b *= x % 13
        x //= 13
    return a,b

for x in range(1,100000):
    if f(x) == (3,12):
        print(x)
        break