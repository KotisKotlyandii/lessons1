def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'АИО'
sogl = 'БРКС'
for s1 in 'ВЕНТИЛЬ':
    for s2 in 'ВЕНТИЛЬ':
        for s3 in 'ВЕНТИЛЬ':
            for s4 in 'ВЕНТИЛЬ':
                for s5 in 'ВЕНТИЛЬ':
                    for s6 in 'ВЕНТИЛЬ':
                        for s7 in 'ВЕНТИЛЬ':
                            a = s1+s2+s3+s4+s5+s6+s7
                            if len(set(a)) == 7 and s7 != 'Ь' and ("ЕЬИ" not  in a) and ('ИЬЕ' not in a ) and ('ЕЬЕ' not in a) and ('ИЬИ' not in a):
                                k += 1
print(k)