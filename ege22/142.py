def f(x):
    L,M = 0,1
    while x > 0:
        L += x % 8 * M
        x //= 8
        M *= 10
    return str(L)

for x in range(1,100000):
    if sum(map(int,f(x))) == 15:
        print(x)
        break