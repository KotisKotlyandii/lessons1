def f(x,y):
    if y > x:
        z = x
        x = y
        y = z
    a,b = x,y
    while b > 0:
        r = a % b
        a = b
        b = r
    return '%d\n%d' % (a,x)

for x in range(1,1000):
    for y in range(1,1000):
        if f(x,y)== '7\n42':
            print(y)