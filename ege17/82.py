import  math

spis = []

for chislo in range(9999, 99999+1):
    if chislo % sum(map(int,str(chislo))) == 0:
        spis.append(chislo)


print(len(spis), max(spis))