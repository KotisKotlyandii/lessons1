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

def devyat(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%9) + chislo2
        chislo //= 9
    return chislo2

spis = []

for chislo in range(100, 10000+1):
    if shesti(chislo)[-1] == "A" and shesti(chislo)[0] == "B" and chislo % 12 > 0:
        spis.append(chislo)

print(len(spis), max(spis))