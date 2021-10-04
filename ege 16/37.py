def f(n,m):
    if m == 0:
        d = 1
    else:
        d = n*f(n,m-1)
    return d

kol_n = 0
for n in range(0,100000):
    if f(n,2) in range(100,1001):
        kol_n += 1

print(kol_n)