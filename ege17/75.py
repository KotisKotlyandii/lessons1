def sum(chislo):
    chislo_2 = 0
    while chislo != 0:
        chislo_2 += chislo % 10
        chislo //= 10
    return chislo_2



def ff(n):
    if n == 1:
        return True
    elif n % 3 != 0:
        return False
    return(ff(n // 3))

spis = []

for chislo in range(138, 603884+1):
    if len(list(map(str, str(chislo)))) != len(set(list(map(str,str(chislo))))) and ff(chislo):
        spis.append(chislo)

print(len(spis))

for prov in range(len(spis)):
    print(spis[prov], sum(spis[prov]))