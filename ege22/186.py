def f(x):
    a = 3*x + 71
    b = 3*x - 87
    while a != b :
        if a > b:
            a -= b
        else:
            b -= a
    return a

for x in range(30, 1000):
    if f(x) == 158:
        print(x)
        break