spis = []

for chislo in range(1346,7996+1):
    if chislo % 3 == 0 and chislo % 13 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))