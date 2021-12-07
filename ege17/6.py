kol = 0
minimum = 0


for chislo in range(1200,11201):
    if chislo % 5 == 0 and chislo % 7 > 0 and chislo % 13 > 0 and chislo % 17 > 0 and chislo % 19 > 0:
        kol += 1
        if kol == 1:
            minimum = chislo


print(kol,minimum)