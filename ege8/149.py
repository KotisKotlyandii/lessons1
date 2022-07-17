sed = set()
for s1 in 'КАНКАН':
    for s2 in 'КАНКАН':
        for s3 in 'КАНКАН':
            for s4 in 'КАНКАН':
                for s5 in 'КАНКАН':
                    for s6 in 'КАНКАН':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('К') + a.count('Н') >= 3:
                            sed.add(a)
print(len(sed))