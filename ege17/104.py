def dva(chislo):
    chislo2 = ''
    while chislo != 0:
        chislo2 = str(chislo%2) + chislo2
        chislo //= 2
    return chislo2

spis = []

for chislo in range(64, 1024+1):
    if dva(chislo)[-1] == "0" and dva(chislo).count("1") == 3 and chislo % 8 == 0 and chislo % 5 > 0:
        spis.append(chislo)

print(len(spis), max(spis))