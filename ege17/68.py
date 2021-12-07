spis = []

for chislo in range(2079, 43167+1):
    if chislo % 7 == 0 and ("0" in str(chislo) and "2" in str(chislo) and "5" in str(chislo)):
        spis.append(chislo)

print(len(spis), min(spis))