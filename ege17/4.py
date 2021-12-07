kol = 0
max = 0


for chislo in range(1512,13203):
    if chislo % 7 == 0 and chislo % 11 > 0 and chislo % 13 > 0 and chislo % 17 > 0 and chislo % 23 > 0:
        kol += 1
        max = chislo


print(kol,max)