spis = []

for chislo in range(4391, 9875+1):
    if ( chislo % 11 == 0 or chislo % 17 == 0) and chislo % 2 > 0 and chislo % 13 > 0 and int(str(chislo)[-3]) % 2 == 0 and int(str(chislo)[-2]) % 2 > 0:
        spis.append(chislo)

print(sum(spis) // len(spis), min(spis))