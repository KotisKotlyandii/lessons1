spis = []

for chislo in range(1234567, 7654321):
    if int(str(chislo)[0:2]) - ((int(str(chislo)[-2])*10) + int(str(chislo)[-1])) == 0:
        continue
    else:
        if chislo % (abs(int(str(chislo)[0:2]) - ((int(str(chislo)[-2])*10) + int(str(chislo)[-1])))) == 0:
            spis.append(chislo)

print(len(spis), max(spis))