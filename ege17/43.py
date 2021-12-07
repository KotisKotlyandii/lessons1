def sum(spisok):
    chislo = 0
    for nom in range(0,len(spisok)):
        chislo += int(spisok[nom])
    return  chislo


def dvyh(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

spis = []
for chislo in range(3721,7752+1):
    if sum(list(str(chislo))) % 3 == 0 and (dvyh(chislo)[-3] != '0' and dvyh(chislo)[-2] != '0' and dvyh(chislo)[-1] != '0'):
        spis.append(chislo)

print(len(spis), min(spis))