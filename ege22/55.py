def f(x):
    a,b = 0,0
    while x > 0:
        a += 1
        b += x % 100
        x //= 100
    return '%d\n%d' % (a,b)

for x in range(1,100000):
    if f(x) == '2\n13':
        print(x)
        break