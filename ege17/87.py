def vuchisl(chislo):
    kol = 0
    for nom in range(len(spis_del)):
        if chislo % spis_del[nom] == 0:
            kol += 1
    if kol == 5:
        return  True
    else:
        return  False

spis_del = [10, 11, 12, 13, 14, 15 , 16, 17, 18, 19, 20]

spis = []

for chislo in range(54123, 75321+1):
    if vuchisl(chislo):
        spis.append(chislo)


print(len(spis), max(spis))