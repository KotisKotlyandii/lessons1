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

for chislo in range(777, 3777+1):
    if shesti(chislo)[0] == "A" and shesti(chislo)[-1] == "F" and chislo % 11 > 0:
        spis.append(chislo)

print(len(spis), max(spis))