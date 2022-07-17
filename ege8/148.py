sed = set()
for s1 in 'КАРКАС':
    for s2 in 'КАРКАС':
        for s3 in 'КАРКАС':
            for s4 in 'КАРКАС':
                for s5 in 'КАРКАС':
                    for s6 in 'КАРКАС':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('К') + a.count('Р') + a.count('С') >= 3:
                            sed.add(a)
print(len(sed))