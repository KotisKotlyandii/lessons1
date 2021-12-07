spis = []

for chislo in range(3905, 7998+1):
    if ((chislo // 10) % 10) != 0 and ((chislo // 10) % 10) != 5 and 2 <= ((chislo // 100) % 10) <= 6:
        spis.append(chislo)

print(len(spis), min(spis))