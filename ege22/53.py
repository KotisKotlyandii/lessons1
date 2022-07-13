def f(x):
    K,R = 0,9
    y = x % 10
    while x > 0:
        K += 1
        if R > x % 10:
            R = x % 10
        x //= 10
    R = y - R
    return '%d\n%d' % (K,R)

for x in range(1,100000):
    if f(x) == '4\n3':
        print(x)
        break