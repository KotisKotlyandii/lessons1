def shest(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%6) + chislo2
        chislo //= 6
    return chislo2


spis = []

for chislo in range(1000, 9999+1):
    if len(shest(chislo)) <= 5 and (( shest(chislo)[-2] == '1' and (shest(chislo)[-1] == '3' or shest(chislo)[-1] == '4'))):
        spis.append(chislo)

print(len(spis), max(spis))
