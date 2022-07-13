def f(x):
    a = 3*x + 67
    b = 3*x - 61
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

for x in range(21, 1000):
    if f(x) == 64:
        print(x)
        break