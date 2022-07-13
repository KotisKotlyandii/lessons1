def f(x):
    a,b = 0,1
    while x > 0:
        a += 1
        b *= x % 100
        x //= 100
    return '%d\n%d' % (a,b)

for x in range(1,10000000):
    if f(x) == '3\n18':
        print(x)