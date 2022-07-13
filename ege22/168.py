def f(x):
    S = 5
    while x > 0:
        if x % 8 > 4:
            S += x % 8
        else:
            S *= x % 8
        x //= 8
    return S

for x in range(1,100000):
    if f(x) % 100 == 0:
        print(x)
        break