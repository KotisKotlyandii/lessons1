list = []

for chislo in range(3394, 8599+1):
    if chislo % 3 == 1 and chislo % 7 == 5:
        list.append(chislo)

print(max(list), len(list))