def f(x):
    L,M = 0,0
    while x > 0:
        L += 1
        if x % 8 != 0:
            M += x % 8
        x //= 8
    return L,M

for x in range(1,10000):
    if f(x) == (3,6):
        print(x)
        