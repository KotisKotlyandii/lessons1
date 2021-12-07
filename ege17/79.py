def prost(chislo):
    k = 0
    for i in range(2, chislo // 2 + 1):
        if (chislo % i == 0):
            k = k + 1
    if (k == 0):
        return  True
    else:
        return  False

spis = []

for chislo in range(2095, 19402+1):
    if prost(chislo) and int(str(chislo)[0]) > int(str(chislo)[-1]):
        spis.append(chislo)

print(len(spis))


for prov in range(len(spis)):
    if str(spis[prov])[-1] == "1" and str(spis[prov])[-2] == "2":
        print(spis[prov])