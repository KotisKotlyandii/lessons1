def f(x):
    a,b = 0,1
    while x > 0:
        a += 1
        b *= x % 6
        x //= 6
    return '%d\n%d' % (a,b)

for x in range(1,100000):
    if f(x) == '3\n6':
        print(x)
        break