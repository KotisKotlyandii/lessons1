def tri(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%3) + chislo2
        chislo //= 3
    return chislo2


def vosem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2


dlya_12 = ['A','B']

def dven(chislo):
    chislo_2 = ''
    while chislo != 0:
        if chislo % 12 > 9:
            chislo_2 = dlya_12[0+((chislo%12)-10)] + chislo_2
            chislo //= 12
        else:
            chislo_2 = str(chislo%12) + chislo_2
            chislo //= 12
    return chislo_2


def sem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%7) + chislo2
        chislo //= 7
    return chislo2

spis = []

for chislo in range(100000,10000000):
    if len(sem(chislo)) == 7 and tri(chislo)[-1] == "2" and vosem(chislo)[-1] != "3" and dven(chislo)[-1] != "5":
        spis.append(chislo)

print(len(spis), max(spis))