def f(x):
    a,b = 0,1
    while x > 0:
        if x % 2 == 0:
            a += x % 9
        else:
            b *= x % 9
        x //= 9
    return a,b

for x in range(1,100000):
    if f(x) == (1,9):
        print(x)
        break