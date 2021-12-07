def vosmi(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2


spis = []

for chislo in range(2371, 9432+1):
    if ((vosmi(chislo)[-2] == '1' and (vosmi(chislo)[-1] == '5' or vosmi(chislo)[-1] == '7')) and (chislo % 3 != 0) and (chislo % 5 != 0)):
        spis.append(chislo)

print(len(spis), max(spis))
