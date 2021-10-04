def f(n,m):
    if m == 0:
        d = 0
    else:
        d = n+f(n,m-1)
    return d

kol_n = 0

for n in range(1,100):
    for m in range(1,100):
        if f(n,m) == 30:
            kol_n += 1

print(kol_n)