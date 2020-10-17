a = int(input())
stroka = []
cravn = 0
for _ in range(a):
    chislo = int(input())
    if chislo > cravn:
        stroka.append(chislo)
        cravn = chislo
    elif chislo == cravn:
        if len(str(chislo)) > len(str(cravn)):
            stroka.append(chislo)
        else:
            stroka.insert(-2, chislo)
    else:
        for number in range (chislo):
