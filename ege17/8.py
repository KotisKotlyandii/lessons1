kol = 0
minimum = 0


for chislo in range(1107,9505):
    if chislo % 9 == 0 and chislo % 7 > 0 and chislo % 15 > 0 and chislo % 17 > 0 and chislo % 19 > 0:
        kol += 1
        if kol == 1:
            minimum = chislo


print(kol,minimum)