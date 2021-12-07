spis =  []

for chislo in range(2381, 14655+1):
    if (chislo % 6 == 0 and chislo % 11 == 0) and chislo % 5 > 0 and chislo % 7 > 0 and ((chislo // 100) % 10) != ((chislo // 10) % 10):
        spis.append(chislo)

print(sum(spis) // len(spis), max(spis))