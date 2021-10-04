def f(n):
    if n > 30:
        return n*n + 3*n + 5
    if n <= 30 and n % 2 == 0:
        return 2 * f(n+1) + f(n+4)
    else:
        return  f(n+2) + 3*f(n+5)

def vishicl_2x_znakov(chislo):
    kol_nyzh_znakov = 0
    while True:
        if chislo % 10 == 0:
            kol_nyzh_znakov += 1
        if kol_nyzh_znakov == 2:
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
