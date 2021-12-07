spis = []

for chislo in range(198372, 876193+1):
    if chislo % sum(map(int,str(chislo))) == 11:
        spis.append(chislo)

print(len(spis),max(spis))