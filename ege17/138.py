spis = []

for chislo in range(2121, 13469+1):
    if chislo % 3 == 0 and chislo % 15 == 0 and chislo % 6 > 0 and chislo % 12 > 0 and int(str(chislo)[2]) % 3 == 0:
        spis.append(chislo)

print(max(spis), min(spis))