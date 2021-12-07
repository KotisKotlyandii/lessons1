def troi(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%3) + chislo2
        chislo //= 3
    return chislo2


spis = []

for chislo in range(1000, 9999+1):
    if chislo % 5 > 0 and chislo % 7 > 0 and chislo % 11 > 0 and len(troi(chislo)) == 8:
        spis.append(chislo)

print(min(spis), max(spis))