spis = []

for chislo in range(2125, 665123+1):
    if sum(map(int,str(chislo))) > 12 and str(chislo).count("0") > 0:
        spis.append(chislo)

print(len(spis), sum(spis))