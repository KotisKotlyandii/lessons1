def prov(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return False
    else:
        return True

k = 0
sed = set()
for s1 in 'АБАК':
    for s2 in 'АБАК':
        for s3 in 'АБАК':
            for s4 in 'АБАК':
                if  prov(s1+s2+s3+s4):
                    k += 1
                    sed.add(s1+s2+s3+s4)
print(k,len(sed))