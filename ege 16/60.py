def f(n):
    if n > 25:
        return n*n + 4*n + 3
    if n <= 25 and n % 3 == 0:
        return f(n+1) + 2 * f(n+4)
    else:
        return f(n+2) + 3 * f(n+5)


def vychisl_cymmu(chislo):
    symma_chifr = 0
    for _ in range(len(str(chislo))+1):
        symma_chifr += chislo % 10
        chislo = chislo // 10
    return symma_chifr

kol_n = 0

for n in range(1,1001):
    if vychisl_cymmu(f(n)) == 24:
        kol_n += 1

print(kol_n)