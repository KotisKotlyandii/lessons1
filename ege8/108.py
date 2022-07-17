def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'ОЕА'
sogl = 'КМТ'
for s1 in 'КОМЕТА':
    for s2 in 'КОМЕТА':
        for s3 in 'КОМЕТА':
            for s4 in 'КОМЕТА':
                for s5 in 'КОМЕТА':
                    for s6 in 'КОМЕТА':
                        a = s1+s2+s3+s4+s5+s6
                        if len(set(a)) == 6 and prov(a):
                            k += 1
print(k)