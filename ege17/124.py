spis = []

for chislo in range(1000, 10001+1):
    if (chislo % 10 == 0 or chislo % 63 == 0) and (chislo % 255 == 0):
        spis.append(chislo)

print(len(spis), min(spis))