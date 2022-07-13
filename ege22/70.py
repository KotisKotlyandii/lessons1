def f(x):
    a,b = 0,1
    while x > 0:
        a += 2
        b *= x % 1000
        x //= 1000
    return '%d\n%d' % (a,b)

for x in range(1,100000):
    if f(x) == '4\n13':
        print(x)