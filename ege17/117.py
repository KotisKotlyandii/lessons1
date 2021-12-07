def vosem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2

spis = []

for chislo in range(100, 555555+1):
    if ((vosem(chislo)[-2] == "6" and vosem(chislo)[-1] == "6") or vosem(chislo)[-1] == "7") and (chislo % 12 == 0 or chislo % 15 > 0):
        spis.append(chislo)

print(len(spis), min(spis)**2)