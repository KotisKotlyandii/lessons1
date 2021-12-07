def dvyh(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

def dev(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%9) + chislo2
        chislo //= 9
    return chislo2


spis = []

for chislo in range(2807, 8558+1):
    if (dvyh(chislo)[-2] == '1' and dvyh(chislo)[-1] == '1') and (dev(chislo)[-1] == '5'):
        spis.append(chislo)

print(max(spis),sum(spis))
