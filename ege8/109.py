def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'АИО'
sogl = 'БРКС'
for s1 in 'АБРИКОС':
    for s2 in 'АБРИКОС':
        for s3 in 'АБРИКОС':
            for s4 in 'АБРИКОС':
                for s5 in 'АБРИКОС':
                    for s6 in 'АБРИКОС':
                        for s7 in 'АБРИКОС':
                            a = s1+s2+s3+s4+s5+s6+s7
                            if len(set(a)) == 7 and prov(a):
                                k += 1
print(k)