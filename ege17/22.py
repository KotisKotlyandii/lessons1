list = []

for chislo in range(2477,7849+1):
    if chislo % 2 == 0 and chislo % 5 > 0 and chislo % 8 > 0 and chislo % 9 > 0 and chislo % 13 > 0:
        list.append(chislo)

print(len(list), min(list))