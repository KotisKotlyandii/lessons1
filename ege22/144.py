def f(x):
    a,b = 0,10
    while x > 0:
        d = x % 6
        if d > a: a = d
        if d < b: b = d
        x //= 6
    return a+b

for x in range(10,100):
    if f(x) == 8:
        print(x)
        break