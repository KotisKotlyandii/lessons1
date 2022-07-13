def f(x):
    s = 0
    while x > 0:
        s += x % 9
        x //= 3
    return s

for x in range(81,1000000):
    if f(x) == 17:
        print(x)
        break