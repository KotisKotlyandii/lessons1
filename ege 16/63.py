def f(n):
    if n <= 13:
        return n*n*n + n*n + 1
    if n > 13 and n % 3 == 0:
        return f(n-1) + 2*n*n - 3
    else:
        return f(n-2) + 3*n + 6

def chet_ili_net(chislo):
    for _ in range(len(str(chislo))+1):
        if len(str(chislo)) == 1 and chislo % 2 == 1:
            return True
        if  (chislo % 10) % 2 == 1:
            chislo = chislo // 10
            continue
        else:
            return False

kol_n = 0

for n in range(1,1001):
    if chet_ili_net(f(n)):
        kol_n += 1

print(kol_n)