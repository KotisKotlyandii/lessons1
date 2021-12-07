def vosem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2

spis = []

for chislo in range(99,998+1):
    if str(chislo)[-1] == "9" and vosem(chislo)[-1] == "1" and chislo % 18 > 0:
        spis.append(chislo)

print(len(spis), max(spis))