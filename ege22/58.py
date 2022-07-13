def f(x):
    a,b = 0,10
    while x > 0:
        y = x % 10
        x //= 10
        if y > a:
            a = y
        if y < b:
            b = y
    return '%d\n%d' % (a,b)

for x in range(10000,100000):
    if f(x) == '5\n2':
        print(x)
        break