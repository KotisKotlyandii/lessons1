spis = []

for chislo in range(5913, 11753+1):
    if chislo % 5 == 0 and chislo % 11 == 0 and chislo % 7 > 0 and chislo % 10 > 0 and chislo % 13 > 0 and chislo % 22 > 0:
        spis.append(chislo)

print(len(spis), min(spis))