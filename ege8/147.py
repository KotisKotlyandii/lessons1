k = 0
sed = set()
for s1 in 'КОРТИК':
    for s2 in 'КОРТИК':
        for s3 in 'КОРТИК':
            for s4 in 'КОРТИК':
                for s5 in 'КОРТИК':
                    for s6 in 'КОРТИК':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('К') + a.count('Р') + a.count('Т') >= 3:
                            sed.add(a)
print(len(sed))