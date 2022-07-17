def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'ОА'

sed = set()
k = 0
for s1 in 'ВОРОТА':
    for s2 in 'ВОРОТА':
        for s3 in 'ВОРОТА':
            for s4 in 'ВОРОТА':
                for s5 in 'ВОРОТА':
                    for s6 in 'ВОРОТА':
                        if prov(s1+s2+s3+s4+s5+s6):
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6)
print(k,len(sed))