spis = []

for chislo in range(1213, 2223+1):
    if max(list(map(int,str(chislo)))) == 7 and sum(list(map(int,str(chislo)))) == 14 and chislo % 2 == 0:
        spis.append(chislo)

print(len(spis), max(spis) - min(spis))