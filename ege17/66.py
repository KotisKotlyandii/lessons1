spis = []

for chislo in range(333666, 666999+1):
    if str(chislo).count("7") == 2 and chislo % 17 == 0:
        spis.append(chislo)

print(max(spis), len(spis))