def f(x):
    L,M = 0,0
    while x > 0:
        L += 1
        if M < x and x % 2 == 0:
            M = x % 10
        x //= 10
    return '%d\n%d' % (L,M)

for x in range(1,100000):
    if f(x) == '3\n8':
        print(x)