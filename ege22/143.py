def f(x):
    L,M = 0,1
    while x > 0:
        L += x % 16 * M
        x //= 16
        M *= 10
    return L

for x in range(1,100000):
    if f(x) == 110:
        print(x)
        break