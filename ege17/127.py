spis = []

for chislo in range(4616, 52311+1):
    if sum(map(int,str(chislo))) == 10 and str(chislo).count('0') > 0:
        spis.append(chislo)

print(len(spis), min(spis))