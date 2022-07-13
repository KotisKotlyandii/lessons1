def f(x):
    a,b = 0,10
    while x > 0:
        d = x % 9
        if d > a: a = d
        if d < b: b = d
        x //= 9
    return a*b

for x in range(1,100000):
    if f(x) == 18:
        print(x)
        break