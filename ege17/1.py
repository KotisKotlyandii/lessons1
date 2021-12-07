kol = 0
max = 0


for chislo in range(1012,9639):
    if chislo % 3 == 0 and chislo % 11 > 0 and chislo % 13 > 0 and chislo % 17 > 0 and chislo % 19 > 0:
        kol += 1
        max = chislo


print(kol,max)