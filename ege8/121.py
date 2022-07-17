sed = set()
for s1 in 'ТАРТАР':
    for s2 in 'ТАРТАР':
        for s3 in 'ТАРТАР':
            for s4 in 'ТАРТАР':
                for s5 in 'ТАРТАР':
                    for s6 in 'ТАРТАР':

                        sed.add(s1+s2+s3+s4+s5+s6)
print(len(sed))