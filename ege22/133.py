def f(x):
    a,b = 0,0
    while x > 0:
        if x % 2 > 0:
            a += x % 5
        else:
            b += x % 5
        x //= 5
    return a,b

for x in range(100,1000):
    if f(x) == (4,4):
        print(x)