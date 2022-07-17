def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'ОУ'
sogl = 'КЛН'
for s1 in 'КОЛУН':
    for s2 in 'КОЛУН':
        for s3 in 'КОЛУН':
            for s4 in 'КОЛУН':
                for s5 in 'КОЛУН':
                    a = s1+s2+s3+s4+s5
                    if len(set(a)) == 5 and prov(a):
                        k += 1
print(k)