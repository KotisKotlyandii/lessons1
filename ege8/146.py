sed = set()
for s1 in 'РАЗМАХ':
    for s2 in 'РАЗМАХ':
        for s3 in 'РАЗМАХ':
            for s4 in 'РАЗМАХ':
                for s5 in 'РАЗМАХ':
                    for s6 in 'РАЗМАХ':
                        a = s1+s2+s3+s4+s5+s6
                        if a.count('Р') + a.count('З') + a.count('М') + a.count('Х') >= 3:
                            sed.add(a)
print(len(sed))