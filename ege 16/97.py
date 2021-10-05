def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n//2) + 3
    else:
        return f(n-1) + 3

kol_n = 0

for n in range(1,1001):
    if f(n) == 18:
        kol_n += 1

print(kol_n)