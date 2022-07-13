def f(x):
    a,b = 0,0
    while x > 0:
        a += 1
        if x % 2 != 0:
            b += 1
        x //= 2
    return a,b

for x in range(1,100000000):
    if f(x) == (24,4):
        print(x)