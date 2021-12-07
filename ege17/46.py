spisok = []

for chislo in range(-7018, -3790+1):
    if chislo % 7 == 0 and chislo % 11 > 0 and chislo % 23 > 0 and str(chislo)[-1] != '2':
        spisok.append(chislo)

print(len(spisok), min(spisok))