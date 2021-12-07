spis = []

for chislo in range(5883, 15906+1):
    if (chislo % 9 == 0 or chislo % 23 == 0) and chislo % 13 > 0 and chislo % 18 > 0 and chislo % 19 > 0 and chislo % 22 > 0:
        spis.append(chislo)

print(len(spis), max(spis))