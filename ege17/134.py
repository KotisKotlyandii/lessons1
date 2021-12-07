spis = []

for chislo in range(6391, 8185+1):
    if (chislo % 11 == 0 and chislo % 17 == 0) and chislo % 2 > 0 and chislo % 13 > 0 and chislo % 14 > 0 and chislo % 34 > 0:
        spis.append(chislo)

print(min(spis), max(spis))