kol = 0
min = 0


for chislo in range(1056,7563+1):
    if (chislo % 3 == 0 or chislo % 11 == 0) and (chislo % 13 > 0) and (chislo % 17 > 0) and (chislo % 19 > 0) and (chislo % 23 > 0):
        kol += 1
        if kol == 1:
            min = chislo


print(kol,min)