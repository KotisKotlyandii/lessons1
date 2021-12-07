spis = []

for chislo in range(4735, 8756+1):
    if chislo % 5 == 0 and chislo % 17 == 0 and chislo % 7 > 0 and chislo % 14 > 0 and int(str(chislo)[-2]) == min(list(map(int,str(chislo)))):
        spis.append(chislo)

print(sum(spis) // len(spis), max(spis), min(spis))