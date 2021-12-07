spis = []

for chislo in range(1812, 9285+1):
    if (chislo % 8 == 0 or chislo % 19 == 0) and chislo % 4 > 0 and chislo % 9 > 0 and int(str(chislo)[0]) % 2 != 0:
        spis.append(chislo)

print(min(spis), max(spis))