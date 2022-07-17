def f(x):
    a = x - 61
    b = 3*x - 138
    while a != b and b >= 0 and a >= 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

for x in range(62,1000):
    if f(x) == 45:
        print(x)
        break