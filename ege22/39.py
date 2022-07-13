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
    return a, x, y


for i in range(1, 1000):
    for j in range(1, 1000):
        a, b, c = f(i, j)
        if a == 7 and b == 42:
            print(c)