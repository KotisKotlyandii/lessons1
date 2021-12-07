spis = []

for chislo in range(2020,647038+1):
    if sum(map(int, str(chislo))) < 10 and min(list(map(str,str(chislo)))) not in str(chislo)[0:3]:
        spis.append(chislo)

for prov in range(len(spis)):
    print(spis[prov])

print(len(spis), sum(spis) // len(spis))