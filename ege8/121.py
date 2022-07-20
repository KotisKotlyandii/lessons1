sed = set()
for s1 in 'ТАРТАР':
    for s2 in 'ТАРТАР':
        for s3 in 'ТАРТАР':
            for s4 in 'ТАРТАР':
                for s5 in 'ТАРТАР':
                    for s6 in 'ТАРТАР':
                        a = s1+s2+s3+s4+s5+s6
                        if len(set(a)) == 3 and a.count('Т') == 2 and a.count('А') == 2 and a.count('Р') == 2:
                            sed.add(a)
print(len(sed))