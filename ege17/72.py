def sum(chislo):
    chislo_2 = 0
    while chislo != 0:
        if chislo % 10 > 5:
            chislo_2 += chislo % 10
            chislo //= 10
        else:
            chislo //= 10
    return chislo_2

spis = []

for chislo in range(2848, 109499+1):
    if "9" in str(chislo) and sum(chislo) % 3 == 0:
        spis.append(chislo)

print(len(spis))

for nomer in range(len(spis)):
    prov = spis[nomer]
    if str(prov)[0] == "8":
        print(spis[nomer])