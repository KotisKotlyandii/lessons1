def f(x):
    a,b = 0,0
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += x % 10
        x //= 10
    return a,b

for x in range(1,100000):
    if f(x) == (3,18):
        print(x)
        break