spis = []

for chislo in range(4563, 7912+1):
    if chislo % 7 == 0 and (int(str(chislo)[0]) + int(str(chislo)[-1])) > 10:
        spis.append(chislo)

print(max(spis), len(spis))