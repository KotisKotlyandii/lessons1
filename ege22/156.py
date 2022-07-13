def f(x):
    a,b = 0,0
    while x > 0:
        x //= 9
        if x % 2 > 0:
            a += x % 9
        else:
            b += 1
    return a,b

for x in range(1,100000):
    if f(x) == (11,3):
        print(x)
        break