def dvyh(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

def chet(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%4) + chislo2
        chislo //= 4
    return chislo2


spis = []

for chislo in range(3712, 8432+1):
    if (dvyh(chislo)[-1] == chet(chislo)[-1]) and (chislo % 13 == 0 or chislo % 14 == 0 or chislo % 15 == 0):
        spis.append(chislo)

print(len(spis),min(spis))