def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'О'

k = 0
sed = set()
for s1 in 'ВОРОН':
    for s2 in 'ВОРОН':
        for s3 in 'ВОРОН':
            for s4 in 'ВОРОН':
                for s5 in 'ВОРОН':
                    a = s1+s2+s3+s4+s5
                    if len(set(a)) == 4 and a.count('О') == 2:
                        k += 1
                        sed.add(s1+s2+s3+s4+s5)
print(k,len(sed))