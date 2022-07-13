def f(x):
    a,b = 0,0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += x % 6
        x //= 6
    return a,b

for x in range(1,10000):
    if f(x) == (1,4):
        print(x)
        break