spis = [27]

nachalo = 27
for chislo in range(27, 900000):
    if chislo // 2 == nachalo and len(list(map(str, str(chislo)))) == len(set(map(str,str(chislo)))):
        nachalo = chislo
        spis.append(chislo)

print(len(spis), max(spis))