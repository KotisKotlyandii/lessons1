sed = set()
k = 0
for s1 in 'РАДУГА':
    for s2 in 'РАДУГА':
        for s3 in 'РАДУГА':
            for s4 in 'РАДУГА':
                for s5 in 'РАДУГА':
                    for s6 in 'РАДУГА':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('Р') + a.count('Д') + a.count('Г') >= 3:
                            sed.add(a)
                            k += 1
print(k,len(sed))