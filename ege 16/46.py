def f(n):
    if n <= 3:
        return n
    if n > 3 and n%2 == 0:
        return 2*n*n + f(n-1)
    else:
        return n*n*n + n + f(n-1)

kol_n = 0

for n in range(1,1000):
    if f(n) < 10**7:
        kol_n += 1

print(kol_n)