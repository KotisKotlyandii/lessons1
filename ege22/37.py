def f(x):
    a,b = 0,0
    while x > 0:
        a += 2
        b += x % 10
        x //= 10
    return '%d\n%d' % (a,b)

for x in range(1,100000):
    if f(x) == '6\n5':
        print(x)
        break