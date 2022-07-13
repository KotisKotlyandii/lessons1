def f(x,y):
    a,b = 0,0
    while x > 0 or y > 0:
        if x > 0:
            a += 1
        if y > 0:
            b += 1
        x //= 2
        y //= 10
    return a,b


for x in range(1,100000):
    for y in range(1,10000000):
        if f(x,y) == (6,7):
            print(x*y)