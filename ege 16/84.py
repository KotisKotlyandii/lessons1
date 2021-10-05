def f(n):
    if n < 2:
        return n
    if n % 2 == 0:
        return f(n//2) + 1
    else:
        return f(3*n+1) + 1

def vychisl_na_chislo(n):
    while True:
        if n < 2:
            return True
        if n % 2 == 0:
            n = n // 2
        else:
            return  False

kol_n = 0

for n in range(1,101):
    if vychisl_na_chislo(n):
        if f(n) > 100:
            kol_n += 1

print(kol_n)
