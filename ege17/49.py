def vosmi(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2

spis = []

for chislo in range(127, 9852+1):
    if (len(vosmi(chislo)) == len(str(chislo))) and chislo % 3 == 0 and chislo % 9 > 0:
        spis.append(chislo)

print(len(spis), max(spis))