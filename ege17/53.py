spis = []
prov = ['0','2','6','8']
for chislo in range(10,1178+1):
    if str(chislo)[-1] not in prov and (str(chislo)[-2] != '1' and str(chislo)[-1] != '2'):
        spis.append(chislo)

print(sum(spis), min(spis))