def f(x):
    a,b = 0,1
    while x > 0:
        if x % 2 == 0:
            a += x % 7
        else:
            b *= x % 7
        x //= 7
    return a,b

for x in range(1,100000):
    if f(x) == (3, 3):
        print(x)
        break