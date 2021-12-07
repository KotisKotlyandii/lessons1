def nacho_del(chislo):
    kol_del = 0
    for prov in range(2,int(chislo**0.5)):
        if chislo % prov == 0 and chislo // prov != prov:
            kol_del += prov
        elif chislo % prov == 0:
            kol_del += prov
    return kol_del

spis = []

for chislo in range(123, 1151+1):
    if nacho_del(chislo) > 40 and chislo % 5 > 0:
        spis.append(chislo)

print(len(spis), max(spis) - min(spis))