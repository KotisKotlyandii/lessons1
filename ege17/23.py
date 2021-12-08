list = []

for chislo in range(3232,8299+1):
    if (chislo % 2 == 0 or chislo % 7 == 0) and  (chislo % 15 > 0) and (chislo % 28 > 0) and (chislo % 41 > 0):
        list.append(chislo)

print(min(list), max(list))