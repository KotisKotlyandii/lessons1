list = []

for chislo in range(1221,9763+1):
    if chislo % 7 == 0 and chislo % 2 > 0 and chislo % 5 > 0 and chislo % 11 > 0 and chislo % 49 > 0:
        list.append(chislo)

print(len(list), max(list))