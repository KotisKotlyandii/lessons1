def sum(chislo):
    chislo_2 = 0
    while chislo != 0:
        chislo_2 += chislo % 10
        chislo //= 10
    return chislo_2

spis = []

for chislo in range(2894, 174882+1):
    if str(chislo)[-1] == "8" and sum(chislo) > 22:
        spis.append(chislo)

print(len(spis), spis[12])
