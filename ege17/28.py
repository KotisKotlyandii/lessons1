def dvyh(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

def chest(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%6) + chislo2
        chislo //= 6
    return chislo2


spis = []

for chislo in range(3439, 7410+1):
    if (dvyh(chislo)[-1] != chest(chislo)[-1]) and (chislo % 9 == 0 or chislo % 10 == 0 or chislo % 11 == 0):
        spis.append(chislo)

print(len(spis), max(spis))