spis = []

for chislo in range(251763, 514827+1):
        if chislo % sum(map(int,str(chislo))) == 0:
            spis.append(chislo)

print(len(spis), min(spis))