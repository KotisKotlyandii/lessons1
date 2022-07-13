def f(x):
    m,s = 0,0
    while x > 0:
        d = x % 7
        s += d
        if d > m: m = d
        x //= 7
    return m,s

for x in range(1,100000):
    if f(x) == (5,12):
        print(x)
        break