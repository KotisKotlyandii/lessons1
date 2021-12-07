spis = []

for chislo in range(1361,7724+1):
    if chislo % 2 == 0 and chislo % 19 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))