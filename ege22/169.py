def f(x):
    S = 0
    while x > 0:
        if x % 5 > 0:
            S += x % 5
        else:
            S *= x % 5
        x //= 5
    return S
kol = 0
for x in range(1,501):
    if f(x) == 13:
        kol += 1

print(kol)