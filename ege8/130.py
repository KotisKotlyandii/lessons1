def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'ЕА'

k = 0
sed = set()
for s1 in 'ЕСАУЛ':
    for s2 in 'ЕСАУЛ':
        for s3 in 'ЕСАУЛ':
            for s4 in 'ЕСАУЛ':
                for s5 in 'ЕСАУЛ':
                    a = s1+s2+s3+s4+s5
                    if len(set(a)) == 5 and 'АУ' not in a and 'УА' not in a:
                        k += 1
                        sed.add(a)
print(k,len(sed))