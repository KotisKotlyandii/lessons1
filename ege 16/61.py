def f(n):
    if n <= 15:
        return n*n + 3*n + 9
    if n > 15 and n % 3 == 0:
        return f(n-1) + n - 2
    else:
        return f(n-2) + n + 2

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

for n in range(1,1001):
    if chet_ili_net(f(n)):
        kol_n += 1

print(kol_n)