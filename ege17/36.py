spis = []

for chislo in range(2476, 7857+1):
    if chislo % 2 == 0 and chislo % 8 > 0 and ((chislo // 100) % 10 <= 7):
        spis.append(chislo)

print(len(spis), ((max(spis) + min(spis)) // 2))