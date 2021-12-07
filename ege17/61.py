spis = []

for chislo in range(2738,7514+1):
    if chislo % 7 == 0 and chislo % 19 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))