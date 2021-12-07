spis = []

for chislo in range(3521, 13019+1):
    if chislo % 6 == 0 and chislo % 15 == 0 and chislo % 9 > 0 and chislo % 12 > 0 and chislo % 17 > 0 and chislo % 21 > 0:
        spis.append(chislo)

print(max(spis), min(spis))