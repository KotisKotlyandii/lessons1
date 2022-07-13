def f(x):
    a,b = 0,0
    while x > 0:
        c = x % 2
        if c == 0:
            a += 1
        else:
            b += 1
        x //= 6
    return '%d\n%d' % (a,b)

for x in range(1,10000000):
    if f(x) == '4\n0':
        print(x)
        break