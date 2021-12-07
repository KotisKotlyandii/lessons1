kol = 0
min = 0


for chislo in range(980,5320+1):
    if (chislo % 4 == 0 or chislo % 5 == 0) and (chislo % 11 > 0) and (chislo % 17 > 0) and (chislo % 19 > 0) and (chislo % 23 > 0):
        kol += 1
        if kol == 1:
            min = chislo


print(kol,min)