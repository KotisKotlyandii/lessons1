def vosem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2

spis = []

for chislo in range(100, 10000+1):
    if str(chislo)[-1] == "3" and vosem(chislo)[-1] == "7" and chislo % 13 > 0 and chislo % 16 > 0 and chislo % 19 > 0 and chislo% 21 == 0:
        spis.append(chislo)

print(len(spis), max(spis))