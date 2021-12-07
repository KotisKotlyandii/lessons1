spis = []

for chislo in range(1840,9052+1):
    if chislo % 7 == 0 and chislo % 23 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))