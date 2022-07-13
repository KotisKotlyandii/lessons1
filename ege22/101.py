def f(x):
    a,b = 0,1
    while x > 0:
        if x % 3 > 0:
            a += 1
        if x % 3 > 1:
            b += 1
        x //= 10
    return a,b

for x in range(1,100000):
    if f(x) == (3,3):
        print(x)
        break