def f(x):
    a,b = 1,10
    while x > 0:
        c = x % 10
        a *= c
        if c < b:
            b = c
        x //= 10
    return a,b

for x in range(1,100000):
    if f(x) == (45,5):
        print(x)
        break