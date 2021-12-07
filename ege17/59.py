spis = []

for chislo in range(1213,8310+1):
    if chislo % 3 == 0 and chislo % 23 > 0:
        spis.append(chislo)

print(len(spis),sum(spis))