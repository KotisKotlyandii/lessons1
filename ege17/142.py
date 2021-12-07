spis = []

for chislo in range(1412, 7865+1):
    if (chislo % 8 == 0 or chislo % 19 == 0) and chislo % 4 > 0 and chislo % 9 > 0 and sum(map(int,str(chislo))) % 5 == 0:
        spis.append(chislo)

print(min(spis), max(spis))