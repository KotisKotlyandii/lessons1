kol = 0
minimum = 0


for chislo in range(1325,15368):
    if chislo % 13 == 0 and chislo % 7 > 0 and chislo % 17 > 0 and chislo % 19 > 0 and chislo % 23 > 0:
        kol += 1
        if kol == 1:
            minimum = chislo


print(kol,minimum)