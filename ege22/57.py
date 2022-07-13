def f(x):
    a,b = 0,0
    while x > 0:
        a += 1
        b += x % 10
        x //= 10
    return '%d\n%d' % (a,b)
kol = 0
for x in range(1,100000):
    if f(x) == '2\n15':
        kol += 1

print(kol)