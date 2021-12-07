import  math

def vosem(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%8) + chislo2
        chislo //= 8
    return chislo2

spis = []

for chislo in range(12345, 67890+1):
    if sum(map(int,vosem(chislo))) == 19 and vosem(chislo).count("0") == 0:
        if math.prod(map(int,vosem(chislo))) % 5 == 0:
            spis.append(chislo)

print(len(spis), min(spis))