def f(x):
    a,b = 0,10
    while x > 0:
        c = x % 10
        a += c
        if c < b:
            b = c
        x //= 10
    return '%d\n%d' % (a,b)

for x in range(1,100000):
    if f(x) == '19\n4':
        print(x)
        break