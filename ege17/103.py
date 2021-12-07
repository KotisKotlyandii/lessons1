def dva(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

spis = []

for chislo in range(10,9999+1):
    if dva(chislo)[-1] == '1' and dva(chislo).count("0") == 5:
        spis.append(chislo)

print(len(spis), max(spis))