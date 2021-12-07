spis = []

for chislo in range(1007, 746001+1):
    if int(str(chislo)[0]) >= max(list(map(int,str(chislo)[1::]))) and str(chislo).count('5') % 2 == 0 and str(chislo).count("5") >= 2:
        spis.append(chislo)

print(len(spis))

for prov in range(len(spis)):
    print(spis[prov])