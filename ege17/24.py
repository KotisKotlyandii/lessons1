list = []

for chislo in range(2568,7858+1):
    if (chislo % 4 == 0 or chislo % 5 == 0) and  (chislo % 11 > 0) and (chislo % 20 > 0) and (chislo % 27 > 0):
        list.append(chislo)

print(min(list), max(list))