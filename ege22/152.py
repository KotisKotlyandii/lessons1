def f(x):
    L,M = 0,0
    while x > 0:
        M += 1
        if x % 2 == 0:
            L += x % 8
        x //= 8
    return L,M

for x in range(1,10000):
    if f(x) == (12,3):
        print(x)