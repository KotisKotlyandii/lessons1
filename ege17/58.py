spis = []

for chislo in range(1705,7474+1):
    if chislo % 11 == 0 and chislo % 19 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))