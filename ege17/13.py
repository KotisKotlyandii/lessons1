kol = 0
maxim = 0


for chislo in range(2320,10987+1):
    if (chislo % 2 == 0 or chislo % 7 == 0) and (chislo % 11 > 0) and (chislo % 13 > 0) and (chislo % 17 > 0) and (chislo % 19 > 0):
        kol += 1
        maxim = chislo


print(kol,maxim)