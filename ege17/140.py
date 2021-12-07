spis = []

for chislo in range(4413, 10153+1):
    if chislo % 5 == 0 and chislo % 23 == 0 and chislo % 7 > 0 and chislo % 10 > 0 and  1 <= ((chislo // 10 ) % 10) <= 3:
        spis.append(chislo)

print(len(spis), min(spis))