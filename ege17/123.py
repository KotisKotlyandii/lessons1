spis = []

for chislo in range(10101, 11110+1):
    if (chislo % 4 == 0 and chislo % 64 == 0 and chislo % 256 == 0) and (chislo % 6 > 0 and chislo % 10 > 0 and chislo % 58 > 0):
        spis.append(chislo)

print(len(spis), min(spis))