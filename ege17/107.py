def nacho_del(chislo):
    kol_del = 0
    for prov in range(1,int(chislo**0.5)+1):
        if chislo % prov == 0 and chislo // prov != prov:
            kol_del += 2
        elif chislo % prov == 0:
            kol_del += 1
    return kol_del

spis = []

for chislo in range(23561, 64354+1):
    if nacho_del(chislo) > 20:
        spis.append(chislo)

print(len(spis), min(spis))