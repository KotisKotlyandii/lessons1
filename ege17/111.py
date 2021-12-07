def pyat(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%5) + chislo2
        chislo //= 5
    return chislo2

spis = []

for chislo in range(10,6000+1):
    if len(pyat(chislo)) == pyat(chislo).count('2') and chislo % 6 == 0:
        spis.append(chislo)

print(len(spis), sum(spis))