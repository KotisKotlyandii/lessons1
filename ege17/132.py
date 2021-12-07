spis = []

for chislo in range(2481, 14832+1):
    if (chislo % 5 == 0 or chislo % 11 == 0) and chislo % 6 > 0 and chislo % 7 > 0 and chislo % 10 > 0 and chislo % 23 > 0:
        spis.append(chislo)

print(sum(spis) // len(spis), max(spis))