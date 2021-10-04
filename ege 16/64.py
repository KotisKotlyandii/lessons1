def f(n):
    if n <= 18:
        return n+3
    if n > 18 and n % 3 == 0:
        return (n//3) * f(n//3) + n - 12
    else:
        return f(n-1) + n*n + 5

def chet_ili_net(chislo):
    for _ in range(len(str(chislo))+1):
        if len(str(chislo)) == 1 and chislo % 2 == 0:
            return True
        if  (chislo % 10) % 2 == 0:
            chislo = chislo // 10
            continue
        else:
            return False

kol_n = 0

for n in range(1,801):
    if chet_ili_net(f(n)):
        kol_n += 1

print(kol_n)