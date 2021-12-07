kol = 0
maxim = 0


for chislo in range(1390,12567+1):
    if (chislo % 3 == 0 or chislo % 5 == 0) and (chislo % 7 > 0) and (chislo % 11 > 0) and (chislo % 13 > 0) and (chislo % 23 > 0):
        kol += 1
        maxim = chislo


print(kol,maxim)