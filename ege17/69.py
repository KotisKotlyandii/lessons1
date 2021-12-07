spis = []

for chislo in range(1388, 63252+1):
    if chislo % 12 > 0 and ("7" in str(chislo) or "4" in str(chislo)):
        spis.append(chislo)

print(len(spis), max(spis))