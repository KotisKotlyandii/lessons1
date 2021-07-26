def func(d):
    S = 5
    N = 7
    while S <= 3011:
        S = S + d
        N = N + 124
    return N

kol = 0

for d in range(1,1000):
    if func(d) == 1247 and d % 10 ==8:
        kol += 1

print(kol)