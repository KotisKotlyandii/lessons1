def f(x):
    L,M = 0,0
    while x > 12:
        L += 1
        x //= 4
        M = x
    if L > M:
        L, M = M, L
    return L,M

for x in range(1,10000):
    if f(x) == (3,7):
        print(x)