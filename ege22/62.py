def f(x):
    a,b = 0,0
    while x > 0:
        y = x % 10
        if y > 3: a += 1
        if y < 8: b += 1
        x //= 10
    return '%d\n%d' % (a,b)

for x in range(10000,100000):
    if f(x) == '5\n3':
        print(x)
        break