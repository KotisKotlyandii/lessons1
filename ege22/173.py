def f(x):
    a,b = 0,0
    while x > 0:
        a += 1
        if x % 11 > b:
            b = x % 11
        x //= 11
    return a,b

for x in range(-10000,10000000):
    if f(x) == (7,7):
        print(x)
        break