def vuchisl(chislo):
    kol = 0
    for nom in range(0,4):
        if chislo % spis_del[nom] == 0:
            kol += 1
    if kol == 2:
        return  True
    else:
        return  False

spis_del = [5, 11, 17, 19]

spis = []

for chislo in range(10000, 20000+1):
    if vuchisl(chislo):
        spis.append(chislo)


print(len(spis), min(spis))
