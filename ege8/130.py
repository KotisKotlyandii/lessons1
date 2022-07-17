def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'ЕА'

k = 0
for s1 in 'ЕСАУЛ':
    for s2 in 'ЕСАУЛ':
        for s3 in 'ЕСАУЛ':
            for s4 in 'ЕСАУЛ':
                for s5 in 'ЕСАУЛ':
                    if len(set(s1+s2+s3+s4+s5)) == 5 and prov(s1+s2+s3+s4+s5):
                        k += 1
print(k)