def prov(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    else:
        return True

k = 0
sed = set()
for s1 in 'АДЖИКА':
    for s2 in 'АДЖИКА':
        for s3 in 'АДЖИКА':
            for s4 in 'АДЖИКА':
                for s5 in 'АДЖИКА':
                    for s6 in 'АДЖИКА':
                        if  prov(s1+s2+s3+s4+s5+s6):
                            k += 1
                            sed.add(s1+s2+s3+s4+s5+s6)
print(k,len(sed))