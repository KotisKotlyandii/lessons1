def f(n):
    if n < 3:
        return n+1
    if n >= 3 and n % 2 == 0:
        return n + 2*f(n+2)
    else:
        return f(n-2) + n - 2

kol_n = 0

for n in range(3,1001,2):
    if len(str(f(n))) == 3:
        kol_n += 1

print(kol_n)
