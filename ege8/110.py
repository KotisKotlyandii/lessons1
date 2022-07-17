def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'ОЕА'
sogl = 'КМТ'
for s1 in 'РУЛЬКА':
    for s2 in 'РУЛЬКА':
        for s3 in 'РУЛЬКА':
            for s4 in 'РУЛЬКА':
                for s5 in 'РУЛЬКА':
                    for s6 in 'РУЛЬКА':
                        a = s1+s2+s3+s4+s5+s6
                        if s1 != 'Ь' and ("УЬ" not in a and 'АЬ' not in a) :
                            k += 1
print(k)