def f(x):
    L,M = 0,0
    while x > 0:
        L += 1
        M += x % 10
        x //= 10
    return '%d\n%d' % (L,M)

for x in range(1,100000):
    if f(x) == '3\n7':
        print(x)
        break