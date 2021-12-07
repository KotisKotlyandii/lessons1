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

for chislo in range(12094, 20075+1):
    if shesti(chislo)[-1] == "F" and chislo % 3 == 0 and chislo % 8 > 0 and chislo % 14 > 0 and chislo % 19 > 0:
        spis.append(chislo)

print(sum(spis), len(spis))