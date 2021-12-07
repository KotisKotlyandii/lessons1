dlya_16 = ['A','B','C','D','E','F']

def shesti(chislo):
    chislo_2 = ''
    while chislo != 0:
        if chislo % 16 > 9:
            chislo_2 = dlya_16[0+((chislo%16)-10)] + chislo_2
            chislo //= 16
        else:
            chislo_2 = str(chislo%16) + chislo_2
            chislo //= 16
    return chislo_2

def vosem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2

def sem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%7) + chislo2
        chislo //= 7
    return chislo2
spis = []

for chislo in range(697, 3458+1):
    if shesti(chislo)[-1] == "E" and (vosem(chislo)[-1] == sem(chislo)[-1]):
        spis.append(chislo)
        
print(sum(spis), len(spis))