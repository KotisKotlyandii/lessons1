def sem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo % 7) + chislo2
        chislo //= 7
    return chislo2

spis = []

for chislo in range(3399, 225599+1):
    if chislo % 5 == 3 and sem(chislo).count("0") == 0:
        spis.append(chislo)

print(max(spis), len(spis))