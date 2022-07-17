def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'ОА'

sed = set()
for s1 in 'КАБАЛА':
    for s2 in 'КАБАЛА':
        for s3 in 'КАБАЛА':
            for s4 in 'КАБАЛА':
                for s5 in 'КАБАЛА':
                    for s6 in 'КАБАЛА':
                        if prov(s1+s2+s3+s4+s5+s6):
                            sed.add(s1+s2+s3+s4+s5+s6)
print(len(sed))