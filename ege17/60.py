spis = []

for chislo in range(1389,9345+1):
    if chislo % 2 == 0 and chislo % 19 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))