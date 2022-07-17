def prov(a):
    for i in range(len(a)-1):
        if (a[i] in glasn and a[i+1] in glasn) or (a[i] in sogl and a[i+1] in sogl):
            return False
    else:
        return True
k = 0
glasn = 'ОА'
sogl = 'НД'
for s1 in 'НОДА':
    for s2 in 'НОДА':
        for s3 in 'НОДА':
            for s4 in 'НОДА':
                a = s1+s2+s3+s4
                if len(set(a)) == 4 and prov(a):
                    k += 1
print(k)