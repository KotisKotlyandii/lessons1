def nacho_del(chislo):
    kol_del = []
    for prov in range(1,int(chislo**0.5)+1):
        if chislo % prov == 0 and chislo // prov != prov:
            kol_del.append(prov)
            kol_del.append(chislo//prov)
        elif chislo % prov == 0:
            kol_del.append(prov)
    k = 0
    for i in kol_del:
        if len(str(i)) == 2:
            k += 1
    return k

spis = []

for chislo in range(25552, 58885+1):
    if nacho_del(chislo) >= 15:
        spis.append(chislo)

print(max(spis), len(spis))