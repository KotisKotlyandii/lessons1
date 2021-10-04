def f(n,m):
    if m == 0:
        return n
    else:
        return f(m,n%m)

kol_n = 0

for n in range(100,1001):
    for m in range(100,1001):
        if f(n,m) == 30:
            kol_n += 1

print(kol_n)