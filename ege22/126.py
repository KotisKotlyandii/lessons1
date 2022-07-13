def f(x):
    a,b = 0,1
    while x > 0:
        if x % 2 == 0:
            a += x % 11
        else:
            b *= x % 11
        x //= 11
    return a,b

for x in range(1,100000):
    if f(x) == (2,9):
        print(x)
        break