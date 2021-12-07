def prover(chislo, spisok):
    kol = 0
    for nom in range(len(spisok)):
        if chislo % spisok[nom] == 0:
            kol += 1
    return kol

spis = []

perv_spis = [9, 11, 13, 15]
vtor_spis = [25, 33, 40, 45]

for chislo in range(45000, 46000+1):
    if prover(chislo,perv_spis) < prover(chislo,vtor_spis):
        spis.append(chislo)

print(len(spis), sum(spis) // len(spis))