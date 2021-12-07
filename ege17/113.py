def vosem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2

spis = []

for chislo in range(777, 19990+1):
    if max(list(map(int,vosem(chislo)))) == 6 and (chislo % 11 == 0 or chislo % 13 == 0) and chislo % 15 > 0:
        spis.append(chislo)

print(len(spis), max(spis) - min(spis))