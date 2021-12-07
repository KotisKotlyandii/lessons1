spis = []

for chislo in range(1110, 1111101+1):
    if (chislo % 16 == 0 or chislo % 48 == 0) and ( chislo % 2 == 0 or (chislo % 3 > 0 and chislo % 18 > 0 and chislo % 63 > 0)):
        spis.append(chislo)

print(len(spis), min(spis))