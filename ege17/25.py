list = []

for chislo in range(3672, 9117+1):
    if chislo % 3 == 2 and chislo % 5 == 4:
        list.append(chislo)

print(len(list), sum(list))