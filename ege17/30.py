def dvyh(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

def pyat(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%5) + chislo2
        chislo //= 5
    return chislo2


spis = []

for chislo in range(1529, 9482+1):
    if (dvyh(chislo)[-2] == '0' and dvyh(chislo)[-1] == '1') and (pyat(chislo)[-1] == '3'):
        spis.append(chislo)

print(min(spis),sum(spis))
