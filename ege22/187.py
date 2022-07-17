def f(x):
    a = 3*x - 112
    b = 3*x + 58
    while a != b and b >= 0 and a >= 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

for x in range(100000):
    if f(x) == 34:
        print(x)
        break