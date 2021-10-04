def f(n):
    if n > 25:
        return 2*n*n*n+1
    else:
        return f(n+2)+2*f(n+3)

kol_n = 0

for n in range(1,1001):
    if f(n) % 11 == 0:
        kol_n += 1

print(kol_n)
