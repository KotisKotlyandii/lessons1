def f(x):
    a,b = 0,0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:

            b += 1
        x //= 2
    return a,b

for x in range(1,1000000):
    if f(x) == (10,8):
        print(x)