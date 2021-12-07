def semi(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%7) + chislo2
        chislo //= 7
    return chislo2

spis = []

for chislo in range(100001, 900009+1):
    if (int(semi(chislo)[-1]) + int(str(chislo)[-1])) == 10 and chislo % 11 == 0 and chislo % 55 > 0:
        spis.append(chislo)

print(max(spis), len(spis))