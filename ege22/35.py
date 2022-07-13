def f(x):
    L,M = 0,9
    while x > 5:
        L += 1
        if M > x % 10:
            M = x % 10
        x //= 10
    return '%d\n%d' % (L,M)

for x in range(1,100000):
    if f(x) == '3\n4':
        print(x)
