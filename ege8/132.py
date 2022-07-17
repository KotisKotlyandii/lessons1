def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'ЕА'

k = 0
for s1 in 'АСПЕКТ':
    for s2 in 'АСПЕКТ':
        for s3 in 'АСПЕКТ':
            for s4 in 'АСПЕКТ':
                for s5 in 'АСПЕКТ':
                    for s6 in 'АСПЕКТ':
                        k += 1
print(k)