def bosmi(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2


spis = []

for chislo in range(3466, 9081+1):
    if (len(str(chislo)) != len(bosmi(chislo))) and (chislo % 7 == 1 or chislo % 7 == 5):
        spis.append(chislo)

print(len(spis), max(spis))