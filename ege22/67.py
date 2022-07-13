def f(x):
    a,b = 0,0
    while x > 0:
        y = x % 10
        if y > 4: a += 1
        if y < 7: b += 1
        x //= 10
    return '%d\n%d' % (a,b)

for x in range(10000,100000):
    if f(x) == '2\n4':
        print(x)