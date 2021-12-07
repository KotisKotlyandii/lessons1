spis = []

for chislo in range(1753,7420+1):
    if chislo % 11 == 0 and chislo % 13 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))