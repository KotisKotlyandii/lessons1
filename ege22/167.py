def f(x):
    S,A = 1,11
    while x // 7 > 0:
        if x % 7 < 4:
            S += A
        else:
            S += x % 7
        x //= 7
    return S

for x in range(1,100000):
    if f(x) > 25:
        print(x)
        break