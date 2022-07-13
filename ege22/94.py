def f(x):
    x0 = x
    N = 0
    while x > 0:
        d = x % 3
        N = 10*N + d
        x //= 3
    N += x0
    return N

for x in range(1,10000):
    if len(str(f(x))) == 4:
        print(f(x))
        print(x)
        break