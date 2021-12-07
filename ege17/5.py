kol = 0
max = 0


for chislo in range(1606,9681):
    if chislo % 11 == 0 and chislo % 7 > 0 and chislo % 13 > 0 and chislo % 17 > 0 and chislo % 19 > 0:
        kol += 1
        max = chislo


print(kol,max)