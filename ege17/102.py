def seme(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%7) + chislo2
        chislo //= 7
    return chislo2

spis = []

for chislo in range(15,1000+1):
    if seme(chislo)[-1] == "6" and chislo % 32 == 0:
        spis.append(chislo)

print(len(spis), max(spis))