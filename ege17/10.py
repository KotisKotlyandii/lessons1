kol = 0
minimum = 0


for chislo in range(1098,13766):
    if chislo % 2 == 0 and chislo % 7 > 0 and chislo % 11 > 0 and chislo % 13 > 0 and chislo % 23 > 0:
        kol += 1
        if kol == 1:
            minimum = chislo


print(kol,minimum)