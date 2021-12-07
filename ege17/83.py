import  math

spis = []

for chislo in range(1111, 9999+1):
    if chislo % sum(map(int,str(chislo))) == 0:
        if 0 in list(map(int,str(chislo))):
            continue
        else:
            if chislo % math.prod(list(map(int,str(chislo)))) == 0:
                spis.append(chislo)


print(len(spis), max(spis))