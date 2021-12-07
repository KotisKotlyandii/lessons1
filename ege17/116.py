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

for chislo in range(100, 555555+1):
    if ((shesti(chislo)[-2] == "F" and shesti(chislo)[-1] == "F") or shesti(chislo)[-1] == "A") and chislo % 6 == 0:
        spis.append(chislo)

print(len(spis), min(spis)**2)