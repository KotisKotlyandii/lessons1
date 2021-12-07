spis = []

for chislo in range(-9563,-3102+1):
    if chislo % 7 == 0 and chislo % 11 > 0 and chislo % 23 > 0 and str(chislo)[-1] != '8':
        spis.append(chislo)

print(len(spis), max(spis))