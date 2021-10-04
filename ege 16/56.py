def f(n):
    if n > 20:
        return n*n*n+n
    if n <= 20 and n % 2 == 0:
        return 3*f(n+1) + f(n+3)
    else:
        return f(n+2)+2*f(n+3)

def proverka_na_1(chislo):
    while True:
        if chislo % 10 == 1:
            return  False
        if len(str(chislo)) == 1 and chislo != 1:
            return  True
        else:
            chislo = chislo // 10

kol_n = 0


for n in range(1,1001):
    if proverka_na_1(f(n)):
        kol_n += 1

print(kol_n)
