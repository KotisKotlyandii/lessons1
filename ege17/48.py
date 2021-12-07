spis = []

for chislo in range(1985, 8528+1):
    if (int(str(chislo)[-1]) + (int(str(chislo)[-2]))) == 6 and chislo % 2 > 0 and chislo % 7 > 0 and chislo % 47 > 0:
        spis.append(chislo)

proizv = spis[0]

for chislo in range(1, len(spis)):
    proizv = proizv * spis[chislo]

print(max(spis),proizv)