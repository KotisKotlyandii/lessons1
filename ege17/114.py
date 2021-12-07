spis = []

for chislo in range(9919, 21987+1):
    if min(list(map(int,str(chislo)))) == 3 and (chislo % 2 == 0 or chislo % 3 == 0) and chislo % 16 > 0:
        spis.append(chislo)

print(len(spis), max(spis) - min(spis))