spis = []

for chislo in range(2595,8401+1):
    if chislo % 2 == 0 and chislo % 13 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))