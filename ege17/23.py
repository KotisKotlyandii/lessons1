list = []

for chislo in range(1221,9763+1):
    if (chislo % 2 == 0 and chislo % 7 == 0) and  (chislo % 15 > 0) and (chislo % 28 > 0) and (chislo % 41 > 0):
        list.append(chislo)

print(min(list), max(list))