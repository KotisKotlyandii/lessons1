kol = 0
maxim = 0


for chislo in range(1305,14064):
    if (chislo % 2 == 0 or chislo % 3 == 0) and (chislo % 7 > 0) and (chislo % 11 > 0) and (chislo % 17 > 0) and (chislo % 23 > 0):
        kol += 1
        maxim = chislo


print(kol,maxim)