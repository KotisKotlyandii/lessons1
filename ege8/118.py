def prov(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    else:
        return True

k = 0
sed = set()
for s1 in 'АВРОРА':
    for s2 in 'АВРОРА':
        for s3 in 'АВРОРА':
            for s4 in 'АВРОРА':
                for s5 in 'АВРОРА':
                    for s6 in 'АВРОРА':
                        if  prov(s1+s2+s3+s4+s5+s6):
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6)
print(k,len(sed))