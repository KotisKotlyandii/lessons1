def proiz(chislo):
    chislo_2 = 1
    while chislo != 0:
        chislo_2 = chislo_2 * (chislo % 10)
        chislo //= 10
    return chislo_2

spis = []

for chislo in range(8800, 55535+1):
    if proiz(chislo) > 35 and ("7" in str(chislo)):
        spis.append(chislo)

print(max(spis), len(spis))