spis = []

for chislo in range(1031, 125888+1):
    if str(chislo)[-1] != "5" and (chislo ** 0.5 == int(chislo ** 0.5)):
        spis.append(chislo)

print(len(spis))

for nomer in range(len(spis)):
    prov = spis[nomer]
    if str(prov)[-1] == "6" and str(prov)[-2] == '3':
        print(spis[nomer])
        break