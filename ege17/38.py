spis = []

for chislo in range(2461, 9719+1):
    if ((chislo // 100) % 10) != 1 and ((chislo // 100) % 10) != 9 and 3 <= ((chislo // 10) % 10) <= 7:
        spis.append(chislo)

print(len(spis), max(spis))