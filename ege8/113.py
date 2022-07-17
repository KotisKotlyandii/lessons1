def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'АИО'
sogl = 'БРКС'
for s1 in 'ПЕСКАРЬ':
    for s2 in 'ПЕСКАРЬ':
        for s3 in 'ПЕСКАРЬ':
            for s4 in 'ПЕСКАРЬ':
                for s5 in 'ПЕСКАРЬ':
                    for s6 in 'ПЕСКАРЬ':
                        for s7 in 'ПЕСКАРЬ':
                            a = s1+s2+s3+s4+s5+s6+s7
                            if len(set(a)) == 7 and s1 != 'Ь' and ('ЕЬ' not in a) and ('АЬ' not in a) and ('РЬ' not in a):
                                k += 1
print(k)