def sum(spisok):
    chislo = 0
    for nom in range(0,len(spisok)):
        chislo += int(spisok[nom])
    return  chislo

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


for chislo in range(3912, 9193+1):
    if sum(list(str(chislo))) % 9 == 0 and (shesti(chislo)[-2] != "2" and shesti(chislo)[-1] != "1"):
        spis.append(chislo)

print(len(spis), max(spis))