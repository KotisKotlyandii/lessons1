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

def pyat(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%5) + chislo2
        chislo //= 5
    return chislo2

spisok = []

for chislo in range(1000,70000+1):
    if len(vosem(chislo)) == 5 and len(pyat(chislo)) == 6 and (shesti(chislo)[-2] == "F" and shesti(chislo)[-1] == "A"):
        spisok.append(chislo)

print(len(spisok), max(spisok))