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

spis = []

for chislo in range(1871, 9197+1):
    if (len(str(chislo)) != len(shesti(chislo))) and (chislo % 9 ==2 or chislo % 9 == 4):
        spis.append(chislo)

print(len(spis), min(spis))