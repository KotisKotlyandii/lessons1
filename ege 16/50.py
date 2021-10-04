def f(n):
    if n <= 3:
        return n
    if n > 3 and n % 2 == 0:
        return n+3+f(n-1)
    else:
        return n*n+f(n-2)

kol_n = 0

for n in range(1,1001):
    if f(n) % 7 == 0:
        kol_n += 1

print(kol_n)
