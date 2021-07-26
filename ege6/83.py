def func(d):
    S = 15
    N = 10
    while S <= 2400:
        S = S + d
        N = N + 5
    return N

kol = 0

for d in range(1,1000):
    if func(d) == 50 and d % 10 == 8:
        kol +=1

print(kol)