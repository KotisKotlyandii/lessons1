def pyat(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%5) + chislo2
        chislo //= 5
    return chislo2


spis = []

for chislo in range(1000, 9999+1):
    if len(pyat(chislo)) >= 6 and (( pyat(chislo)[-2] == '2' and (pyat(chislo)[-1] == '1' or pyat(chislo)[-1] == '3'))):
        spis.append(chislo)

print(len(spis), min(spis))
