def f(n):
    if n == 60:
        return 123586943
    if n <= 3:
        return n
    if n>3 and n%2 == 0:
        return f(n-1) + 2*f(n//2)
    if n>3 and n%2 == 1:
        return f(n-1)+f(n-3)

kol_n = 0

for n in range(1,1000):
    if f(n) < 10**8:
        kol_n += 1
    elif f(n) >= 10**8:
        break

print(kol_n)
