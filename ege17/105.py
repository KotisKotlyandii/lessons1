def dva(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

spis = []

for chislo in range(31, 2047+1):
    if dva(chislo)[-1] == "0" and sum(map(int,dva(chislo))) == 5 and chislo % 10 > 0:
        spis.append(chislo)

print(len(spis), max(spis))