spis = []

for chislo in range(7525, 13486+1):
    if chislo % 7 == 0 and chislo % 6 > 0 and chislo % 9 > 0 and chislo % 14 > 0 and chislo % 21 > 0:
        spis.append(chislo)

print(len(spis), min(spis))