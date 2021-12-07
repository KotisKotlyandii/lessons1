spis = []

nachalo = 15
for chislo in range(15, 2000000+1):
    if chislo // 2 == nachalo:
        nachalo = chislo
        if len(list(map(str, str(chislo)))) != len(set(map(str,str(chislo)))):
            spis.append(chislo)

print(len(spis), max(spis)-min(spis))