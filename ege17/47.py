spis = []

for chislo in range(2055, 9414+1):
    if (int(str(chislo)[-1]) + (int(str(chislo)[-2]))) != 5 and chislo % 4 > 0 and chislo % 5 > 0 and chislo % 41 > 0:
        spis.append(chislo)

proizv = spis[0]

for chislo in range(1, len(spis)):
    proizv = proizv * spis[chislo]

print(min(spis),proizv)