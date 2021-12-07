spis = []

for chislo in range(4855, 7856):
    if chislo % 6 == 0 and chislo % 15 == 0 and chislo % 7 > 0 and chislo % 16 > 0 and ((chislo // 10) % 10) % 2 == 0 and ((chislo // 100) % 10) % 2 == 0:
        spis.append(chislo)

print(sum(spis) // len(spis), max(spis), min(spis)) 