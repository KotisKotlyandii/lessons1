def f(x):
    L,M = 0,0
    while x > 0:
        M += 1
        if x % 2 != 0:
            L += 1
        x //= 2
    return '%d\n%d' % (L,M)

for x in range(1,100000):
    if f(x) == '5\n8':
        print(x)