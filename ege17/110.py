def tri(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%3) + chislo2
        chislo //= 3
    return chislo2

spis = []

for chislo in range(255,4095+1):
    if (tri(chislo).count("1") == 1 or tri(chislo).count("0") == 2) and chislo % 2 == 0 and chislo % 5 == 0 and chislo % 20 > 0:
        spis.append(chislo)

print(len(spis), sum(spis))