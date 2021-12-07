def chetv(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%4) + chislo2
        chislo //= 4
    return chislo2


spis = []

for chislo in range(1000, 9999+1):
    if chislo % 3 > 0 and chislo % 17 > 0 and chislo % 19 > 0 and len(chetv(chislo)) == 6:
        spis.append(chislo)

print(min(spis), max(spis))