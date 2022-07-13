def f(x):
    S = 0
    while x > 0:
        if x % 2 > 0:
            S += x % 7
        else:
            S -= x % 7
        x //= 7
    return S

for x in range(51,100000):
    if f(x) == 1:
        print(x)
        break
