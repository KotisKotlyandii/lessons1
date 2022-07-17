def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'АИО'
sogl = 'БРКС'
for s1 in 'АЙСБЕРГ':
    for s2 in 'АЙСБЕРГ':
        for s3 in 'АЙСБЕРГ':
            for s4 in 'АЙСБЕРГ':
                for s5 in 'АЙСБЕРГ':
                    for s6 in 'АЙСБЕРГ':
                        for s7 in 'АЙСБЕРГ':
                            a = s1+s2+s3+s4+s5+s6+s7
                            if len(set(a)) == 7 and s1 != 'Й' and ('ЙА' not in a) and ('ЙЕ' not in a ):
                                k += 1
print(k)