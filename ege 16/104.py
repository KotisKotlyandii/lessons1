def f(n):
    if n == 0:
        return 1
    if 0 < n <= 10:
        return f(n-1)
    if 10 < n < 100:
        return 2.2*f(n-3)
    else:
        return 1.7*f(n-2)


def vychisl_cymmu(chislo):
    symma_chifr = 0
    for _ in range(len(str(chislo))+1):
        symma_chifr += chislo % 10
        chislo = chislo // 10
    return symma_chifr

print(vychisl_cymmu(int(f(40))))