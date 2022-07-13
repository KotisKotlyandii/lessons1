def f(x):
    S,A = 1,5
    while x // 7 > 0:
        if x % 2 == 0:
            S += A
        else:
            S *= x % 7
        x //= 7
    return S

for x in range(1,100000):
    if f(x) > 100:
        print(x)
        break