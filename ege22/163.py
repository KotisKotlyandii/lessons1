def f(x):
    B,S,A = x, -2, 4
    while B // 2 > 0:
        if B % 2 == 0:
            S += A
        else:
            S *= 3
        B //= 2
    return S

for x in range(1,100000):
    if f(x) > 100:
        print(x)
        break