def prov(chislo):
    kol_chet = 0
    while chislo != 0:
        if chislo % 10 > 4:
            kol_chet += 1
            chislo //= 10
        else:
            chislo //= 10
    return kol_chet


spis = []

for chislo in range(5903, 174203+1):
    if len(list(map(str, str(chislo)))) == len(set(list(map(str,str(chislo))))) and prov(chislo) == 3:
        spis.append(chislo)
print(len(spis))

for prov in range(len(spis)):
    print(spis[prov])