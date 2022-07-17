def prov(a):
    for i in range(len(a)-1):
        if a[i] in glasn and a[i+1] in glasn:
            return False
    else:
        return True
glasn = 'ЕАИ'

k = 0
for s1 in 'ЗДАНИЕ':
    for s2 in 'ЗДАНИЕ':
        for s3 in 'ЗДАНИЕ':
            for s4 in 'ЗДАНИЕ':
                for s5 in 'ЗДАНИЕ':
                    for s6 in 'ЗДАНИЕ':
                        if len(set(s1+s2+s3+s4+s5+s6)) == 6 and prov(s1+s2+s3+s4+s5+s6):
                            k += 1
print(k) 