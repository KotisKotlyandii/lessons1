def f(n):
    if n <= 15:
        return n*n + 11
    if n > 15 and n % 2 == 0:
        return f(n//2) + n*n*n - 5 * n
    else:
        return f(n-1) + 2 * n + 3

def vishicl_2x_znakov(chislo):
    kol_nyzh_znakov = 0
    while True:
        if chislo % 10 == 6:
            kol_nyzh_znakov += 1
        if kol_nyzh_znakov == 3:
            return  True
        if len(str(chislo)) == 1:
            return False
        else:
            chislo = chislo // 10

kol_n = 0

for n in range(1,1001):
    if vishicl_2x_znakov(f(n)):
        kol_n += 1

print(kol_n)