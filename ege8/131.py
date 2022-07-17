def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'ЕА'

k = 0
sed = set()
for s1 in 'АРЕАЛ':
    for s2 in 'АРЕАЛ':
        for s3 in 'АРЕАЛ':
            for s4 in 'АРЕАЛ':
                for s5 in 'АРЕАЛ':
                    if prov(s1+s2+s3+s4+s5):
                        k += 1
                        sed.add(s1+s2+s3+s4+s5)
print(k,len(sed))