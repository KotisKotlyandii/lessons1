def f(x):
    a = 2*x - 91
    b = 3*x - 159
    while a != b and b >= 0 and a >= 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

for x in range(62,1000):
    if f(x) == 15:
        print(x)
        break