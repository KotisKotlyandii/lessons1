def f(n):
    if n < 2:
        return 1
    if n % 3 == 0:
        return f(n//3) + 1
    else:
        return f(n-2) + 5

kol_n = 0

for n in range(1,100001):
    if f(n) == 55:
        kol_n += 1

print(kol_n)