def f(n):
    if n < 2:
        return 1
    if n % 2 == 0:
        return f(n//2) + 1
    else:
        return f(n-3) + 3

kol_n = 0

for n in range(1,100001):
    if f(n) == 12:
        kol_n += 1

print(kol_n)