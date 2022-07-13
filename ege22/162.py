def f(x):
    L,M = 0,10
    while x > 5:
        L += 1
        if x % 8 < M:
            M = x % 8
        x //= 8
    return L,M

for x in range(1,1000000):
    if f(x) == (2,4):
        print(x)