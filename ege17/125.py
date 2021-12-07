spis = []

for chislo in range(3212, 64212+1):
    if sum(map(int,str(chislo))) == 5 and str(chislo).count('0') > 0:
        spis.append(chislo)

print(len(spis), max(spis))