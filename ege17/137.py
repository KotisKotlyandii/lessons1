spis = []

for chislo in range(4565, 13346+1):
    if chislo % 7 == 0 and chislo % 6 > 0 and chislo % 3 > 0 and (int(str(chislo)[-2])+ int(str(chislo)[-1])) % 2 == 0:
        spis.append(chislo)

print(len(spis), min(spis))