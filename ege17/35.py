spis = []

for chislo in range(1476, 7039+1):
    if chislo % 2 == 0 and chislo % 16 > 0 and ((chislo // 10) % 10 >= 4):
        spis.append(chislo)

print(len(spis), ((max(spis) + min(spis)) // 2))