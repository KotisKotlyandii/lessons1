def f(x):
    a = 5*x + 345
    b = 5*x - 807
    while a != b and b >0 and a > 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

for x in range(1000):
    if f(x) == 96:
        print(x)
        break